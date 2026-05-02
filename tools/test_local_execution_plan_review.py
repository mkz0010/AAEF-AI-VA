from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from bounded_execution_transition import (
    build_bounded_execution_transition_candidate,
    evaluate_bounded_execution_transition_gate,
)
from local_execution_plan import (
    LocalExecutionPlanError,
    build_local_only_execution_plan,
    evaluate_local_execution_plan_review_gate,
    validate_local_execution_plan_review_gate_result,
    validate_local_only_execution_plan,
)
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from runtime_destination_binding import (
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
)
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_plan_error(fn, message: str) -> None:
    try:
        fn()
    except LocalExecutionPlanError:
        return
    raise AssertionError(message)


def build_demo_plan():
    runtime_profile = build_zap_runtime_profile()
    runtime_readiness = evaluate_local_runtime_readiness(
        runtime_profile,
        lookup={"zap.sh": None, "zap.bat": None, "zaproxy": None, "zap": None},
    )
    lab_profile = build_local_target_lab_profile()
    lab_gate = evaluate_local_target_lab_gate(lab_profile)
    binding = build_scope_registry_runtime_destination_binding(
        runtime_profile,
        runtime_readiness,
        lab_profile,
        lab_gate,
    )
    binding_gate = evaluate_runtime_destination_binding_gate(binding)
    transition_candidate = build_bounded_execution_transition_candidate(binding, binding_gate)
    transition_gate = evaluate_bounded_execution_transition_gate(transition_candidate)
    plan = build_local_only_execution_plan(transition_candidate, transition_gate)
    return transition_candidate, transition_gate, plan


def main() -> int:
    transition_candidate, transition_gate, plan = build_demo_plan()
    validate_local_only_execution_plan(plan)

    assert_true(plan["plan_status"] == "plan_recorded_execution_blocked", "plan status mismatch")
    assert_true(plan["local_only"] is True, "plan must be local-only")
    assert_true(set(plan["allowed_plan_operations"]) == {"runtime_detection", "health_check_plan_only"}, "allowed operations mismatch")
    assert_true("active_scan" in plan["prohibited_runtime_operations"], "active_scan should be prohibited")
    assert_true("spider" in plan["prohibited_runtime_operations"], "spider should be prohibited")
    assert_true("authenticated_crawl" in plan["prohibited_runtime_operations"], "authenticated crawl should be prohibited")
    assert_true(plan["execution_plan_review_required"] is True, "plan review must be required")
    assert_true(plan["no_egress_required"] is True, "no-egress must be required")
    assert_true(plan["timeout_required"] is True, "timeout must be required")
    assert_true(plan["kill_switch_required"] is True, "kill-switch must be required")
    assert_true(plan["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(plan["network_activity_allowed"] is False, "network activity must be false")
    assert_true(plan["real_execution_permitted"] is False, "real execution must be false")
    assert_true(plan["external_process_execution_allowed"] is False, "external process execution must be false")

    gate = evaluate_local_execution_plan_review_gate(plan)
    assert_true(gate["local_execution_plan_review_gate_status"] == "plan_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["plan_review_satisfied"] is False, "plan review must remain unsatisfied")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    assert_true(gate["network_activity_allowed"] is False, "gate network activity must be false")
    validate_local_execution_plan_review_gate_result(gate)

    needs_revision_gate = evaluate_local_execution_plan_review_gate(plan, plan_review_decision="needs_revision")
    assert_true(needs_revision_gate["local_execution_plan_review_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["real_execution_permitted"] is False, "needs_revision must not permit execution")

    rejected_gate = evaluate_local_execution_plan_review_gate(plan, plan_review_decision="rejected")
    assert_true(rejected_gate["local_execution_plan_review_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["real_execution_permitted"] is False, "rejected must not permit execution")

    bad_plan = copy.deepcopy(plan)
    bad_plan["allowed_plan_operations"] = ["runtime_detection", "active_scan"]
    expect_plan_error(lambda: validate_local_only_execution_plan(bad_plan), "active_scan should not be allowed")

    bad_plan = copy.deepcopy(plan)
    bad_plan["real_execution_permitted"] = True
    expect_plan_error(lambda: validate_local_only_execution_plan(bad_plan), "real_execution_permitted true should fail closed")

    bad_plan = copy.deepcopy(plan)
    bad_plan["external_process_execution_allowed"] = True
    expect_plan_error(lambda: validate_local_only_execution_plan(bad_plan), "external process execution true should fail closed")

    bad_plan = copy.deepcopy(plan)
    bad_plan["network_activity_allowed"] = True
    expect_plan_error(lambda: validate_local_only_execution_plan(bad_plan), "network activity true should fail closed")

    bad_plan = copy.deepcopy(plan)
    bad_plan["no_egress_required"] = False
    expect_plan_error(lambda: validate_local_only_execution_plan(bad_plan), "no_egress_required false should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["plan_review_satisfied"] = True
    expect_plan_error(lambda: validate_local_execution_plan_review_gate_result(bad_gate), "plan_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["raw_artifact_capture_permitted"] = True
    expect_plan_error(lambda: validate_local_execution_plan_review_gate_result(bad_gate), "raw artifact capture true should fail closed")

    bad_transition_gate = copy.deepcopy(transition_gate)
    bad_transition_gate["scope_id"] = "other-scope"
    expect_plan_error(
        lambda: build_local_only_execution_plan(transition_candidate, bad_transition_gate),
        "transition candidate/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_local_execution_plan_review_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "local-execution-plan-review" / "demo" / "local-execution-plan-review-gate-result.generated.json"
    assert_true(generated.exists(), "generated local execution plan review gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")
    assert_true(data["network_activity_allowed"] is False, "generated gate must block network activity")
    assert_true(data["external_process_execution_allowed"] is False, "generated gate must block external process execution")

    print("Local execution plan review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
