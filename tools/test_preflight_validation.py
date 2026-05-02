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
from execution_authorization import build_execution_authorization_scaffold, evaluate_execution_authorization_gate
from local_execution_plan import build_local_only_execution_plan, evaluate_local_execution_plan_review_gate
from local_target_lab import build_local_target_lab_profile, evaluate_local_target_lab_gate
from preflight_validation import (
    PREFLIGHT_CHECKS,
    PreflightValidationError,
    build_preflight_validation_scaffold,
    evaluate_preflight_validation_gate,
    validate_preflight_validation_gate_result,
    validate_preflight_validation_scaffold,
)
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


def expect_preflight_error(fn, message: str) -> None:
    try:
        fn()
    except PreflightValidationError:
        return
    raise AssertionError(message)


def build_demo_preflight():
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
    authorization_gate = evaluate_execution_authorization_gate(authorization)
    preflight = build_preflight_validation_scaffold(authorization, authorization_gate)
    return authorization, authorization_gate, preflight


def main() -> int:
    authorization, authorization_gate, preflight = build_demo_preflight()
    validate_preflight_validation_scaffold(preflight)

    assert_true(preflight["preflight_status"] == "preflight_scaffold_recorded_execution_blocked", "preflight status mismatch")
    assert_true(preflight["local_only"] is True, "preflight must be local-only")
    assert_true(preflight["preflight_required"] is True, "preflight must be required")
    assert_true(preflight["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(preflight["execution_authorized"] is False, "execution must not be authorized")
    assert_true(preflight["execution_authorization_satisfied"] is False, "execution authorization must not be satisfied")
    assert_true(preflight["runtime_enforcement_implemented"] is False, "runtime enforcement must remain not implemented")
    assert_true(preflight["all_required_checks_defined"] is True, "all checks should be defined")
    assert_true(preflight["all_required_checks_satisfied"] is False, "all checks must not be satisfied")
    assert_true(set(preflight["required_checks"]) == set(PREFLIGHT_CHECKS), "required checks mismatch")
    assert_true(len(preflight["check_results"]) == len(PREFLIGHT_CHECKS), "check result count mismatch")
    assert_true(all(item["satisfied"] is False for item in preflight["check_results"]), "all checks must remain unsatisfied")
    assert_true(preflight["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(preflight["network_activity_allowed"] is False, "network activity must be false")
    assert_true(preflight["real_execution_permitted"] is False, "real execution must be false")
    assert_true(preflight["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(preflight["raw_artifact_capture_permitted"] is False, "raw artifact capture must be false")

    gate = evaluate_preflight_validation_gate(preflight)
    assert_true(gate["preflight_validation_gate_status"] == "preflight_scaffold_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["preflight_review_satisfied"] is False, "preflight review must remain unsatisfied")
    assert_true(gate["preflight_satisfied"] is False, "preflight must remain unsatisfied")
    assert_true(gate["execution_authorized"] is False, "gate must not authorize execution")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    validate_preflight_validation_gate_result(gate)

    needs_revision_gate = evaluate_preflight_validation_gate(preflight, preflight_review_decision="needs_revision")
    assert_true(needs_revision_gate["preflight_validation_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_preflight_validation_gate(preflight, preflight_review_decision="rejected")
    assert_true(rejected_gate["preflight_validation_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad_preflight = copy.deepcopy(preflight)
    bad_preflight["preflight_satisfied"] = True
    expect_preflight_error(lambda: validate_preflight_validation_scaffold(bad_preflight), "preflight_satisfied true should fail closed")

    bad_preflight = copy.deepcopy(preflight)
    bad_preflight["execution_authorized"] = True
    expect_preflight_error(lambda: validate_preflight_validation_scaffold(bad_preflight), "execution_authorized true should fail closed")

    bad_preflight = copy.deepcopy(preflight)
    bad_preflight["all_required_checks_satisfied"] = True
    expect_preflight_error(lambda: validate_preflight_validation_scaffold(bad_preflight), "all checks satisfied true should fail closed")

    bad_preflight = copy.deepcopy(preflight)
    bad_preflight["check_results"][0]["satisfied"] = True
    expect_preflight_error(lambda: validate_preflight_validation_scaffold(bad_preflight), "satisfied check should fail closed")

    bad_preflight = copy.deepcopy(preflight)
    bad_preflight["network_activity_allowed"] = True
    expect_preflight_error(lambda: validate_preflight_validation_scaffold(bad_preflight), "network activity true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["preflight_review_satisfied"] = True
    expect_preflight_error(lambda: validate_preflight_validation_gate_result(bad_gate), "preflight_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["real_execution_permitted"] = True
    expect_preflight_error(lambda: validate_preflight_validation_gate_result(bad_gate), "real execution true should fail closed")

    bad_authorization_gate = copy.deepcopy(authorization_gate)
    bad_authorization_gate["scope_id"] = "other-scope"
    expect_preflight_error(
        lambda: build_preflight_validation_scaffold(authorization, bad_authorization_gate),
        "authorization/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_preflight_validation_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "preflight-validation" / "demo" / "preflight-validation-gate-result.generated.json"
    assert_true(generated.exists(), "generated preflight validation gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["preflight_satisfied"] is False, "generated gate must not satisfy preflight")
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")

    print("Preflight validation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
