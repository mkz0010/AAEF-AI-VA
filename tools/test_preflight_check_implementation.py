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

from preflight_validation import PREFLIGHT_CHECKS
from preflight_check_implementation import (
    PreflightCheckImplementationError,
    build_preflight_check_implementation_scaffold,
    evaluate_preflight_check_implementation_gate,
    validate_preflight_check_implementation_gate_result,
    validate_preflight_check_implementation_scaffold,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair
from runtime_transition_checkpoint import build_runtime_transition_checkpoint


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_implementation_error(fn, message: str) -> None:
    try:
        fn()
    except PreflightCheckImplementationError:
        return
    raise AssertionError(message)


def build_demo_implementation():
    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    return checkpoint, implementation


def main() -> int:
    checkpoint, implementation = build_demo_implementation()
    validate_preflight_check_implementation_scaffold(implementation)

    assert_true(implementation["implementation_status"] == "implementation_scaffold_recorded_execution_blocked", "implementation status mismatch")
    assert_true(implementation["current_version_target"] == "v0.3.0", "version target mismatch")
    assert_true(implementation["local_only"] is True, "implementation must be local-only")
    assert_true(implementation["preflight_check_implementation_scaffold_recorded"] is True, "scaffold must be recorded")
    assert_true(implementation["concrete_checks_implemented"] is False, "concrete checks must not be implemented")
    assert_true(implementation["all_required_checks_satisfied"] is False, "all checks must not be satisfied")
    assert_true(implementation["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(implementation["execution_authorized"] is False, "execution must not be authorized")
    assert_true(implementation["ready_for_runtime_execution"] is False, "must not be runtime-ready")
    assert_true(len(implementation["check_implementations"]) == len(PREFLIGHT_CHECKS), "check implementation count mismatch")

    names = {item["check_name"] for item in implementation["check_implementations"]}
    assert_true(names == set(PREFLIGHT_CHECKS), "check implementation names mismatch")
    assert_true(all(item["implemented"] is False for item in implementation["check_implementations"]), "all checks must be unimplemented")
    assert_true(all(item["satisfied"] is False for item in implementation["check_implementations"]), "all checks must be unsatisfied")
    assert_true(all(item["evidence_record_required"] is True for item in implementation["check_implementations"]), "evidence must be required")
    assert_true(all(item["evidence_record_generated"] is False for item in implementation["check_implementations"]), "evidence must not be generated")
    assert_true(all(item["fail_closed_on_missing_input"] is True for item in implementation["check_implementations"]), "missing inputs must fail closed")
    assert_true(all(item["fail_closed_on_mismatch"] is True for item in implementation["check_implementations"]), "mismatches must fail closed")
    assert_true(all(item["fail_closed_on_stale_state"] is True for item in implementation["check_implementations"]), "stale state must fail closed")

    runtime_check = next(item for item in implementation["check_implementations"] if item["check_name"] == "runtime_readiness_check")
    assert_true("runtime_readiness_result" in runtime_check["input_sources"], "runtime readiness input missing")

    authorization_check = next(item for item in implementation["check_implementations"] if item["check_name"] == "execution_authorization_check")
    assert_true(authorization_check["evidence_type"] == "execution_authorization_verification_evidence", "authorization evidence type mismatch")

    gate = evaluate_preflight_check_implementation_gate(implementation)
    assert_true(gate["preflight_check_implementation_gate_status"] == "implementation_scaffold_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["implementation_review_satisfied"] is False, "implementation review must not be satisfied")
    assert_true(gate["concrete_checks_implemented"] is False, "gate concrete checks must be false")
    assert_true(gate["preflight_satisfied"] is False, "gate preflight must be false")
    assert_true(gate["execution_authorized"] is False, "gate execution authorized must be false")
    assert_true(gate["ready_for_runtime_execution"] is False, "gate runtime-ready must be false")
    validate_preflight_check_implementation_gate_result(gate)

    needs_revision_gate = evaluate_preflight_check_implementation_gate(implementation, implementation_review_decision="needs_revision")
    assert_true(needs_revision_gate["preflight_check_implementation_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_preflight_check_implementation_gate(implementation, implementation_review_decision="rejected")
    assert_true(rejected_gate["preflight_check_implementation_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad = copy.deepcopy(implementation)
    bad["concrete_checks_implemented"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "implemented true should fail closed")

    bad = copy.deepcopy(implementation)
    bad["preflight_satisfied"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "preflight_satisfied true should fail closed")

    bad = copy.deepcopy(implementation)
    bad["execution_authorized"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "execution_authorized true should fail closed")

    bad = copy.deepcopy(implementation)
    bad["check_implementations"][0]["implemented"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "implemented check should fail closed")

    bad = copy.deepcopy(implementation)
    bad["check_implementations"][0]["satisfied"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "satisfied check should fail closed")

    bad = copy.deepcopy(implementation)
    bad["implementation_invariants"]["real_execution_permitted"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_scaffold(bad), "real execution invariant true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["implementation_review_satisfied"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_gate_result(bad_gate), "implementation review satisfied should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["ready_for_runtime_execution"] = True
    expect_implementation_error(lambda: validate_preflight_check_implementation_gate_result(bad_gate), "runtime ready true should fail closed")

    bad_checkpoint = copy.deepcopy(checkpoint)
    bad_checkpoint["safety_invariants"]["execution_authorized"] = True
    expect_implementation_error(
        lambda: build_preflight_check_implementation_scaffold(bad_checkpoint),
        "unsafe checkpoint should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_preflight_check_implementation_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "preflight-check-implementation" / "demo" / "preflight-check-implementation-gate-result.generated.json"
    assert_true(generated.exists(), "generated preflight check implementation gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["concrete_checks_implemented"] is False, "generated gate must not implement checks")
    assert_true(data["preflight_satisfied"] is False, "generated gate must not satisfy preflight")
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["ready_for_runtime_execution"] is False, "generated gate must not be runtime-ready")

    print("Preflight check implementation tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
