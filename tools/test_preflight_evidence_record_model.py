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
    build_preflight_check_implementation_scaffold,
    evaluate_preflight_check_implementation_gate,
)
from preflight_evidence_record import (
    PreflightEvidenceRecordError,
    build_preflight_evidence_record_model,
    evaluate_preflight_evidence_record_model_gate,
    validate_preflight_evidence_record,
    validate_preflight_evidence_record_model,
    validate_preflight_evidence_record_model_gate_result,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair
from runtime_transition_checkpoint import build_runtime_transition_checkpoint


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_evidence_error(fn, message: str) -> None:
    try:
        fn()
    except PreflightEvidenceRecordError:
        return
    raise AssertionError(message)


def build_demo_model():
    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    implementation_gate = evaluate_preflight_check_implementation_gate(implementation)
    model = build_preflight_evidence_record_model(implementation, implementation_gate)
    return implementation, implementation_gate, model


def main() -> int:
    implementation, implementation_gate, model = build_demo_model()
    validate_preflight_evidence_record_model(model)

    assert_true(model["evidence_model_status"] == "evidence_model_recorded_records_not_generated", "model status mismatch")
    assert_true(model["local_only"] is True, "model must be local-only")
    assert_true(model["evidence_records_defined"] is True, "evidence records should be defined")
    assert_true(model["evidence_records_generated"] is False, "evidence records must not be generated")
    assert_true(model["all_required_evidence_records_defined"] is True, "all required evidence records should be defined")
    assert_true(model["all_required_evidence_records_generated"] is False, "all required evidence records must not be generated")
    assert_true(model["all_required_checks_satisfied"] is False, "checks must not be satisfied")
    assert_true(model["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(model["execution_authorized"] is False, "execution must not be authorized")
    assert_true(model["ready_for_runtime_execution"] is False, "must not be runtime-ready")
    assert_true(len(model["preflight_evidence_records"]) == len(PREFLIGHT_CHECKS), "record count mismatch")

    record_names = {record["check_name"] for record in model["preflight_evidence_records"]}
    assert_true(record_names == set(PREFLIGHT_CHECKS), "record names mismatch")
    assert_true(all(record["evidence_record_generated"] is False for record in model["preflight_evidence_records"]), "records must not be generated")
    assert_true(all(record["check_satisfied"] is False for record in model["preflight_evidence_records"]), "records must not satisfy checks")
    assert_true(all(record["fail_closed"] is True for record in model["preflight_evidence_records"]), "records must fail closed")
    assert_true(all(record["ai_visible"] is False for record in model["preflight_evidence_records"]), "records must not be AI-visible")
    assert_true(all(record["raw_artifact_capture_permitted"] is False for record in model["preflight_evidence_records"]), "records must not permit raw artifact capture")
    assert_true(all(record["sanitized_summary_required"] is True for record in model["preflight_evidence_records"]), "sanitized summary must be required")

    runtime_record = next(record for record in model["preflight_evidence_records"] if record["check_name"] == "runtime_readiness_check")
    assert_true(runtime_record["evidence_type"] == "runtime_readiness_verification_evidence", "runtime evidence type mismatch")
    validate_preflight_evidence_record(runtime_record)

    gate = evaluate_preflight_evidence_record_model_gate(model)
    assert_true(gate["preflight_evidence_model_gate_status"] == "evidence_model_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["evidence_review_satisfied"] is False, "evidence review must not be satisfied")
    assert_true(gate["evidence_records_generated"] is False, "gate records generated must be false")
    assert_true(gate["preflight_satisfied"] is False, "gate preflight must be false")
    assert_true(gate["execution_authorized"] is False, "gate execution authorized must be false")
    validate_preflight_evidence_record_model_gate_result(gate)

    needs_revision_gate = evaluate_preflight_evidence_record_model_gate(model, evidence_review_decision="needs_revision")
    assert_true(needs_revision_gate["preflight_evidence_model_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_preflight_evidence_record_model_gate(model, evidence_review_decision="rejected")
    assert_true(rejected_gate["preflight_evidence_model_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad = copy.deepcopy(model)
    bad["evidence_records_generated"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "evidence records generated true should fail closed")

    bad = copy.deepcopy(model)
    bad["preflight_satisfied"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "preflight_satisfied true should fail closed")

    bad = copy.deepcopy(model)
    bad["execution_authorized"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "execution_authorized true should fail closed")

    bad = copy.deepcopy(model)
    bad["preflight_evidence_records"][0]["evidence_record_generated"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "generated record should fail closed")

    bad = copy.deepcopy(model)
    bad["preflight_evidence_records"][0]["check_satisfied"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "satisfied record should fail closed")

    bad = copy.deepcopy(model)
    bad["preflight_evidence_records"][0]["ai_visible"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "AI-visible record should fail closed")

    bad = copy.deepcopy(model)
    bad["evidence_model_invariants"]["real_execution_permitted"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model(bad), "real execution invariant true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["evidence_review_satisfied"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model_gate_result(bad_gate), "evidence_review_satisfied true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["ready_for_runtime_execution"] = True
    expect_evidence_error(lambda: validate_preflight_evidence_record_model_gate_result(bad_gate), "runtime ready true should fail closed")

    bad_implementation_gate = copy.deepcopy(implementation_gate)
    bad_implementation_gate["scope_id"] = "other-scope"
    expect_evidence_error(
        lambda: build_preflight_evidence_record_model(implementation, bad_implementation_gate),
        "implementation/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_preflight_evidence_record_model_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "preflight-evidence-record-model" / "demo" / "preflight-evidence-record-model-gate-result.generated.json"
    assert_true(generated.exists(), "generated preflight evidence model gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["evidence_records_generated"] is False, "generated gate must not generate evidence records")
    assert_true(data["preflight_satisfied"] is False, "generated gate must not satisfy preflight")
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["ready_for_runtime_execution"] is False, "generated gate must not be runtime-ready")

    print("Preflight evidence record model tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
