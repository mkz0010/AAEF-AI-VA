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
from local_execution_plan import build_local_only_execution_plan, evaluate_local_execution_plan_review_gate
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from runtime_destination_binding import (
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
)
from runtime_enforcement_design import (
    RuntimeEnforcementDesignError,
    build_runtime_enforcement_design,
    evaluate_runtime_enforcement_design_gate,
    validate_runtime_enforcement_design,
    validate_runtime_enforcement_design_gate_result,
)
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness
from runtime_safety_policy import build_runtime_safety_policy, evaluate_runtime_safety_policy_gate


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_design_error(fn, message: str) -> None:
    try:
        fn()
    except RuntimeEnforcementDesignError:
        return
    raise AssertionError(message)


def build_demo_design():
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
    plan_gate = evaluate_local_execution_plan_review_gate(plan)
    policy = build_runtime_safety_policy(plan, plan_gate)
    policy_gate = evaluate_runtime_safety_policy_gate(policy)
    design = build_runtime_enforcement_design(policy, policy_gate)
    return policy, policy_gate, design


def main() -> int:
    policy, policy_gate, design = build_demo_design()
    validate_runtime_enforcement_design(design)

    assert_true(design["design_status"] == "design_recorded_execution_blocked", "design status mismatch")
    assert_true(design["local_only"] is True, "design must be local-only")
    assert_true(design["enforcement_design_recorded"] is True, "design must be recorded")
    assert_true(design["runtime_enforcement_implemented"] is False, "runtime enforcement must not be implemented")
    assert_true(design["preflight_check_required"] is True, "preflight check must be required")
    assert_true(design["process_wrapper_required"] is True, "process wrapper must be required")
    assert_true(design["no_egress_guard_required"] is True, "no-egress guard must be required")
    assert_true(design["timeout_watcher_required"] is True, "timeout watcher must be required")
    assert_true(design["kill_switch_controller_required"] is True, "kill-switch controller must be required")
    assert_true(design["evidence_emitter_required"] is True, "evidence emitter must be required")
    assert_true(design["sanitizer_boundary_required"] is True, "sanitizer boundary must be required")
    assert_true(design["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(design["network_activity_allowed"] is False, "network activity must be false")
    assert_true(design["real_execution_permitted"] is False, "real execution must be false")
    assert_true(design["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(design["raw_artifact_capture_permitted"] is False, "raw artifact capture must be false")

    components = {item["component"] for item in design["enforcement_components"]}
    assert_true("preflight_check" in components, "preflight component missing")
    assert_true("process_wrapper" in components, "process wrapper component missing")
    assert_true("no_egress_guard" in components, "no-egress component missing")
    assert_true("timeout_watcher" in components, "timeout component missing")
    assert_true("kill_switch_controller" in components, "kill-switch component missing")
    assert_true("evidence_emitter" in components, "evidence emitter missing")
    assert_true("sanitizer_boundary" in components, "sanitizer boundary missing")

    gate = evaluate_runtime_enforcement_design_gate(design)
    assert_true(gate["runtime_enforcement_design_gate_status"] == "design_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["design_review_satisfied"] is False, "design review must remain unsatisfied")
    assert_true(gate["runtime_enforcement_implemented"] is False, "runtime enforcement must remain not implemented")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    assert_true(gate["external_process_execution_allowed"] is False, "gate external process execution must be false")
    validate_runtime_enforcement_design_gate_result(gate)

    needs_revision_gate = evaluate_runtime_enforcement_design_gate(design, design_review_decision="needs_revision")
    assert_true(needs_revision_gate["runtime_enforcement_design_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["real_execution_permitted"] is False, "needs_revision must not permit execution")

    rejected_gate = evaluate_runtime_enforcement_design_gate(design, design_review_decision="rejected")
    assert_true(rejected_gate["runtime_enforcement_design_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["real_execution_permitted"] is False, "rejected must not permit execution")

    bad_design = copy.deepcopy(design)
    bad_design["runtime_enforcement_implemented"] = True
    expect_design_error(lambda: validate_runtime_enforcement_design(bad_design), "runtime enforcement implemented should fail closed")

    bad_design = copy.deepcopy(design)
    bad_design["real_execution_permitted"] = True
    expect_design_error(lambda: validate_runtime_enforcement_design(bad_design), "real execution true should fail closed")

    bad_design = copy.deepcopy(design)
    bad_design["external_process_execution_allowed"] = True
    expect_design_error(lambda: validate_runtime_enforcement_design(bad_design), "external process execution true should fail closed")

    bad_design = copy.deepcopy(design)
    bad_design["enforcement_components"][0]["status"] = "implemented"
    expect_design_error(lambda: validate_runtime_enforcement_design(bad_design), "implemented component should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["design_review_satisfied"] = True
    expect_design_error(lambda: validate_runtime_enforcement_design_gate_result(bad_gate), "design_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["network_activity_allowed"] = True
    expect_design_error(lambda: validate_runtime_enforcement_design_gate_result(bad_gate), "network activity true should fail closed")

    bad_policy_gate = copy.deepcopy(policy_gate)
    bad_policy_gate["scope_id"] = "other-scope"
    expect_design_error(
        lambda: build_runtime_enforcement_design(policy, bad_policy_gate),
        "policy/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_runtime_enforcement_design_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "runtime-enforcement-design" / "demo" / "runtime-enforcement-design-gate-result.generated.json"
    assert_true(generated.exists(), "generated runtime enforcement design gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["runtime_enforcement_implemented"] is False, "generated gate must not implement enforcement")
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")
    assert_true(data["external_process_execution_allowed"] is False, "generated gate must block external process execution")

    print("Runtime enforcement design tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
