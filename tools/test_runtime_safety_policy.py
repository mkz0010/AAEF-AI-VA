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
from runtime_readiness import build_zap_runtime_profile, evaluate_local_runtime_readiness
from runtime_safety_policy import (
    RuntimeSafetyPolicyError,
    build_runtime_safety_policy,
    evaluate_runtime_safety_policy_gate,
    validate_runtime_safety_policy,
    validate_runtime_safety_policy_gate_result,
)


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_policy_error(fn, message: str) -> None:
    try:
        fn()
    except RuntimeSafetyPolicyError:
        return
    raise AssertionError(message)


def build_demo_policy():
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
    return plan, plan_gate, policy


def main() -> int:
    plan, plan_gate, policy = build_demo_policy()
    validate_runtime_safety_policy(policy)

    assert_true(policy["policy_status"] == "policy_recorded_execution_blocked", "policy status mismatch")
    assert_true(policy["local_only"] is True, "policy must be local-only")
    assert_true(policy["no_egress_required"] is True, "no-egress must be required")
    assert_true(policy["no_egress_policy_defined"] is True, "no-egress policy must be defined")
    assert_true(policy["timeout_required"] is True, "timeout must be required")
    assert_true(policy["timeout_policy_defined"] is True, "timeout policy must be defined")
    assert_true(policy["kill_switch_required"] is True, "kill-switch must be required")
    assert_true(policy["kill_switch_policy_defined"] is True, "kill-switch policy must be defined")
    assert_true(policy["process_tree_termination_required"] is True, "process tree termination must be required")
    assert_true(policy["max_runtime_seconds"] == 60, "default max runtime should be 60 seconds")
    assert_true(policy["idle_timeout_seconds"] == 15, "default idle timeout should be 15 seconds")
    assert_true("public_internet" in policy["denied_destination_categories"], "public internet must be denied")
    assert_true("customer_network" in policy["denied_destination_categories"], "customer network must be denied")
    assert_true("operator_manual_stop" in policy["kill_switch_modes"], "manual stop must be present")
    assert_true("timeout_forced_stop" in policy["kill_switch_modes"], "timeout forced stop must be present")
    assert_true(policy["scan_execution_allowed"] is False, "scan execution must be false")
    assert_true(policy["network_activity_allowed"] is False, "network activity must be false")
    assert_true(policy["real_execution_permitted"] is False, "real execution must be false")
    assert_true(policy["external_process_execution_allowed"] is False, "external process execution must be false")
    assert_true(policy["raw_artifact_capture_permitted"] is False, "raw artifact capture must be false")

    gate = evaluate_runtime_safety_policy_gate(policy)
    assert_true(gate["runtime_safety_policy_gate_status"] == "policy_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["policy_review_satisfied"] is False, "policy review must remain unsatisfied")
    assert_true(gate["real_execution_permitted"] is False, "gate real execution must be false")
    assert_true(gate["network_activity_allowed"] is False, "gate network activity must be false")
    validate_runtime_safety_policy_gate_result(gate)

    needs_revision_gate = evaluate_runtime_safety_policy_gate(policy, policy_review_decision="needs_revision")
    assert_true(needs_revision_gate["runtime_safety_policy_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["real_execution_permitted"] is False, "needs_revision must not permit execution")

    rejected_gate = evaluate_runtime_safety_policy_gate(policy, policy_review_decision="rejected")
    assert_true(rejected_gate["runtime_safety_policy_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["real_execution_permitted"] is False, "rejected must not permit execution")

    bad_policy = copy.deepcopy(policy)
    bad_policy["real_execution_permitted"] = True
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "real_execution_permitted true should fail closed")

    bad_policy = copy.deepcopy(policy)
    bad_policy["network_activity_allowed"] = True
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "network_activity_allowed true should fail closed")

    bad_policy = copy.deepcopy(policy)
    bad_policy["external_process_execution_allowed"] = True
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "external process execution true should fail closed")

    bad_policy = copy.deepcopy(policy)
    bad_policy["no_egress_policy_defined"] = False
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "no-egress policy false should fail closed")

    bad_policy = copy.deepcopy(policy)
    bad_policy["idle_timeout_seconds"] = 120
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "idle timeout larger than max should fail closed")

    bad_policy = copy.deepcopy(policy)
    bad_policy["denied_destination_categories"] = ["public_internet"]
    expect_policy_error(lambda: validate_runtime_safety_policy(bad_policy), "missing denied categories should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["policy_review_satisfied"] = True
    expect_policy_error(lambda: validate_runtime_safety_policy_gate_result(bad_gate), "policy_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["credential_injection_permitted"] = True
    expect_policy_error(lambda: validate_runtime_safety_policy_gate_result(bad_gate), "credential injection true should fail closed")

    bad_plan_gate = copy.deepcopy(plan_gate)
    bad_plan_gate["scope_id"] = "other-scope"
    expect_policy_error(
        lambda: build_runtime_safety_policy(plan, bad_plan_gate),
        "plan/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_runtime_safety_policy_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "runtime-safety-policy" / "demo" / "runtime-safety-policy-gate-result.generated.json"
    assert_true(generated.exists(), "generated runtime safety policy gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["real_execution_permitted"] is False, "generated gate must block real execution")
    assert_true(data["network_activity_allowed"] is False, "generated gate must block network activity")
    assert_true(data["external_process_execution_allowed"] is False, "generated gate must block external process execution")

    print("Runtime safety policy tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
