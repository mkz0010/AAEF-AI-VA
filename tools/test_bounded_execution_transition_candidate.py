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
    BoundedExecutionTransitionError,
    build_bounded_execution_transition_candidate,
    evaluate_bounded_execution_transition_gate,
    validate_bounded_execution_transition_candidate,
    validate_bounded_execution_transition_gate_result,
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


def expect_transition_error(fn, message: str) -> None:
    try:
        fn()
    except BoundedExecutionTransitionError:
        return
    raise AssertionError(message)


def build_demo_candidate():
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
    candidate = build_bounded_execution_transition_candidate(binding, binding_gate)
    return binding, binding_gate, candidate


def main() -> int:
    binding, binding_gate, candidate = build_demo_candidate()
    validate_bounded_execution_transition_candidate(candidate)

    assert_true(candidate["candidate_status"] == "execution_plan_review_required", "candidate status mismatch")
    assert_true(candidate["bounded_execution_transition_candidate_allowed"] is True, "candidate should be allowed")
    assert_true(candidate["local_only"] is True, "candidate must be local-only")
    assert_true(candidate["execution_plan_review_required"] is True, "execution plan review must be required")
    assert_true(candidate["human_approval_required"] is True, "human approval must be required")
    assert_true(candidate["no_egress_required"] is True, "no-egress must be required")
    assert_true(candidate["timeout_required"] is True, "timeout must be required")
    assert_true(candidate["kill_switch_required"] is True, "kill-switch must be required")
    assert_true(candidate["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(candidate["network_activity_allowed"] is False, "network activity must be false")
    assert_true(candidate["real_execution_permitted"] is False, "real execution must be false")
    assert_true(candidate["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(candidate["credential_injection_permitted"] is False, "credential injection must be false")
    assert_true(candidate["raw_artifact_capture_permitted"] is False, "raw artifact capture must be false")

    gate = evaluate_bounded_execution_transition_gate(candidate)
    assert_true(gate["bounded_execution_transition_gate_status"] == "candidate_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["transition_review_satisfied"] is False, "transition review must remain unsatisfied")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    assert_true(gate["network_activity_allowed"] is False, "gate network activity must be false")
    validate_bounded_execution_transition_gate_result(gate)

    needs_design_gate = evaluate_bounded_execution_transition_gate(candidate, transition_review_decision="needs_design")
    assert_true(needs_design_gate["bounded_execution_transition_gate_status"] == "needs_design", "needs_design status mismatch")
    assert_true(needs_design_gate["real_execution_permitted"] is False, "needs_design must not permit execution")

    rejected_gate = evaluate_bounded_execution_transition_gate(candidate, transition_review_decision="rejected")
    assert_true(rejected_gate["bounded_execution_transition_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["real_execution_permitted"] is False, "rejected must not permit execution")

    bad_candidate = copy.deepcopy(candidate)
    bad_candidate["real_execution_permitted"] = True
    expect_transition_error(
        lambda: validate_bounded_execution_transition_candidate(bad_candidate),
        "real_execution_permitted true should fail closed",
    )

    bad_candidate = copy.deepcopy(candidate)
    bad_candidate["network_activity_allowed"] = True
    expect_transition_error(
        lambda: validate_bounded_execution_transition_candidate(bad_candidate),
        "network_activity_allowed true should fail closed",
    )

    bad_candidate = copy.deepcopy(candidate)
    bad_candidate["no_egress_required"] = False
    expect_transition_error(
        lambda: validate_bounded_execution_transition_candidate(bad_candidate),
        "no_egress_required false should fail closed",
    )

    bad_candidate = copy.deepcopy(candidate)
    bad_candidate["customer_target"] = True
    expect_transition_error(
        lambda: validate_bounded_execution_transition_candidate(bad_candidate),
        "customer_target true should fail closed",
    )

    bad_gate = copy.deepcopy(gate)
    bad_gate["transition_review_satisfied"] = True
    expect_transition_error(
        lambda: validate_bounded_execution_transition_gate_result(bad_gate),
        "transition_review_satisfied true should fail closed",
    )

    bad_gate = copy.deepcopy(gate)
    bad_gate["raw_artifact_capture_permitted"] = True
    expect_transition_error(
        lambda: validate_bounded_execution_transition_gate_result(bad_gate),
        "raw_artifact_capture_permitted true should fail closed",
    )

    bad_binding_gate = copy.deepcopy(binding_gate)
    bad_binding_gate["target_id"] = "other-target"
    expect_transition_error(
        lambda: build_bounded_execution_transition_candidate(binding, bad_binding_gate),
        "binding/gate mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_bounded_execution_transition_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "bounded-execution-transition" / "demo" / "bounded-execution-transition-gate-result.generated.json"
    assert_true(generated.exists(), "generated bounded execution transition gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")
    assert_true(data["network_activity_allowed"] is False, "generated gate must block network activity")

    print("Bounded execution transition candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
