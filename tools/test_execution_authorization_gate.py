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
from execution_authorization import (
    ExecutionAuthorizationError,
    build_execution_authorization_scaffold,
    evaluate_execution_authorization_gate,
    validate_execution_authorization_gate_result,
    validate_execution_authorization_scaffold,
)
from local_execution_plan import build_local_only_execution_plan, evaluate_local_execution_plan_review_gate
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from runtime_destination_binding import (
    build_scope_registry_runtime_destination_binding,
    evaluate_runtime_destination_binding_gate,
)
from runtime_enforcement_design import build_runtime_enforcement_design, evaluate_runtime_enforcement_design_gate
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness
from runtime_safety_policy import build_runtime_safety_policy, evaluate_runtime_safety_policy_gate


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_authorization_error(fn, message: str) -> None:
    try:
        fn()
    except ExecutionAuthorizationError:
        return
    raise AssertionError(message)


def build_demo_authorization():
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
    design_gate = evaluate_runtime_enforcement_design_gate(design)
    authorization = build_execution_authorization_scaffold(design, design_gate)
    return design, design_gate, authorization


def main() -> int:
    design, design_gate, authorization = build_demo_authorization()
    validate_execution_authorization_scaffold(authorization)

    assert_true(authorization["authorization_status"] == "authorization_scaffold_recorded_execution_blocked", "authorization status mismatch")
    assert_true(authorization["local_only"] is True, "authorization must be local-only")
    assert_true(authorization["authorization_scaffold_recorded"] is True, "authorization scaffold must be recorded")
    assert_true(authorization["execution_authorized"] is False, "execution must not be authorized")
    assert_true(authorization["execution_authorization_satisfied"] is False, "execution authorization must not be satisfied")
    assert_true(authorization["runtime_enforcement_implemented"] is False, "runtime enforcement must remain not implemented")
    assert_true(authorization["preflight_check_required"] is True, "preflight check must be required")
    assert_true(authorization["preflight_check_satisfied"] is False, "preflight check must not be satisfied")
    assert_true(authorization["human_approval_required"] is True, "human approval must be required")
    assert_true(authorization["human_approval_recorded"] is False, "human approval must not be recorded")
    assert_true(authorization["operator_confirmation_required"] is True, "operator confirmation must be required")
    assert_true(authorization["scope_owner_approval_required"] is True, "scope owner approval must be required")
    assert_true(authorization["no_egress_guard_required"] is True, "no-egress guard must be required")
    assert_true(authorization["no_egress_guard_verified"] is False, "no-egress guard must not be verified")
    assert_true(authorization["timeout_watcher_required"] is True, "timeout watcher must be required")
    assert_true(authorization["kill_switch_controller_required"] is True, "kill-switch controller must be required")
    assert_true(authorization["evidence_emitter_required"] is True, "evidence emitter must be required")
    assert_true(authorization["sanitizer_boundary_required"] is True, "sanitizer boundary must be required")
    assert_true(authorization["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(authorization["network_activity_allowed"] is False, "network activity must be false")
    assert_true(authorization["real_execution_permitted"] is False, "real execution must be false")
    assert_true(authorization["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(authorization["raw_artifact_capture_permitted"] is False, "raw artifact capture must be false")

    gate = evaluate_execution_authorization_gate(authorization)
    assert_true(gate["execution_authorization_gate_status"] == "authorization_scaffold_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["authorization_review_satisfied"] is False, "authorization review must remain unsatisfied")
    assert_true(gate["execution_authorized"] is False, "gate must not authorize execution")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    assert_true(gate["external_process_execution_allowed"] is False, "gate external process execution must be false")
    validate_execution_authorization_gate_result(gate)

    needs_revision_gate = evaluate_execution_authorization_gate(authorization, authorization_review_decision="needs_revision")
    assert_true(needs_revision_gate["execution_authorization_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_execution_authorization_gate(authorization, authorization_review_decision="rejected")
    assert_true(rejected_gate["execution_authorization_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad_authorization = copy.deepcopy(authorization)
    bad_authorization["execution_authorized"] = True
    expect_authorization_error(lambda: validate_execution_authorization_scaffold(bad_authorization), "execution_authorized true should fail closed")

    bad_authorization = copy.deepcopy(authorization)
    bad_authorization["real_execution_permitted"] = True
    expect_authorization_error(lambda: validate_execution_authorization_scaffold(bad_authorization), "real_execution_permitted true should fail closed")

    bad_authorization = copy.deepcopy(authorization)
    bad_authorization["human_approval_recorded"] = True
    expect_authorization_error(lambda: validate_execution_authorization_scaffold(bad_authorization), "human_approval_recorded true should fail closed")

    bad_authorization = copy.deepcopy(authorization)
    bad_authorization["runtime_enforcement_implemented"] = True
    expect_authorization_error(lambda: validate_execution_authorization_scaffold(bad_authorization), "runtime_enforcement_implemented true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["authorization_review_satisfied"] = True
    expect_authorization_error(lambda: validate_execution_authorization_gate_result(bad_gate), "authorization_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["network_activity_allowed"] = True
    expect_authorization_error(lambda: validate_execution_authorization_gate_result(bad_gate), "network activity true should fail closed")

    bad_design_gate = copy.deepcopy(design_gate)
    bad_design_gate["scope_id"] = "other-scope"
    expect_authorization_error(
        lambda: build_execution_authorization_scaffold(design, bad_design_gate),
        "design/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_execution_authorization_gate_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "execution-authorization" / "demo" / "execution-authorization-gate-result.generated.json"
    assert_true(generated.exists(), "generated execution authorization gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")
    assert_true(data["external_process_execution_allowed"] is False, "generated gate must block external process execution")

    print("Execution authorization gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
