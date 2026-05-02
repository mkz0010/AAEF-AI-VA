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

from preflight_evidence_examples import (
    REPRESENTATIVE_EXAMPLE_CHECKS,
    PreflightEvidenceExampleError,
    build_preflight_evidence_example_set,
    evaluate_preflight_evidence_example_gate,
    validate_preflight_evidence_example,
    validate_preflight_evidence_example_gate_result,
    validate_preflight_evidence_example_set,
)
from preflight_evidence_record import (
    build_preflight_evidence_record_model,
    evaluate_preflight_evidence_record_model_gate,
)
from preflight_check_implementation import (
    build_preflight_check_implementation_scaffold,
    evaluate_preflight_check_implementation_gate,
)
from generate_runtime_transition_checkpoint_demo import build_demo_preflight_pair
from runtime_transition_checkpoint import build_runtime_transition_checkpoint


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_example_error(fn, message: str) -> None:
    try:
        fn()
    except PreflightEvidenceExampleError:
        return
    raise AssertionError(message)


def build_demo_example_set():
    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    implementation_gate = evaluate_preflight_check_implementation_gate(implementation)
    model = build_preflight_evidence_record_model(implementation, implementation_gate)
    model_gate = evaluate_preflight_evidence_record_model_gate(model)
    example_set = build_preflight_evidence_example_set(model, model_gate)
    return model, model_gate, example_set


def main() -> int:
    model, model_gate, example_set = build_demo_example_set()
    validate_preflight_evidence_example_set(example_set)

    assert_true(example_set["example_set_status"] == "examples_recorded_execution_blocked", "example set status mismatch")
    assert_true(example_set["local_only"] is True, "example set must be local-only")
    assert_true(example_set["examples_recorded"] is True, "examples should be recorded")
    assert_true(example_set["example_records_generated"] is True, "example records should be generated")
    assert_true(example_set["live_evidence_records_generated"] is False, "live evidence must not be generated")
    assert_true(example_set["all_required_evidence_records_generated"] is False, "all required evidence must not be generated")
    assert_true(example_set["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(example_set["execution_authorized"] is False, "execution must not be authorized")
    assert_true(example_set["ready_for_runtime_execution"] is False, "must not be runtime-ready")
    assert_true(len(example_set["representative_examples"]) == len(REPRESENTATIVE_EXAMPLE_CHECKS), "representative example count mismatch")

    names = {example["check_name"] for example in example_set["representative_examples"]}
    assert_true(names == set(REPRESENTATIVE_EXAMPLE_CHECKS), "representative example names mismatch")
    assert_true(all(example["example_record_generated"] is True for example in example_set["representative_examples"]), "example records should be generated")
    assert_true(all(example["live_evidence_record_generated"] is False for example in example_set["representative_examples"]), "live evidence must not be generated")
    assert_true(all(example["validation_result"] == "failed_closed" for example in example_set["representative_examples"]), "examples must fail closed")
    assert_true(all(example["check_satisfied"] is False for example in example_set["representative_examples"]), "checks must not be satisfied")
    assert_true(all(example["ai_visible"] is False for example in example_set["representative_examples"]), "examples must not be AI-visible raw evidence")
    assert_true(all(example["raw_artifact_capture_permitted"] is False for example in example_set["representative_examples"]), "raw artifact capture must be false")
    assert_true(all(example["sanitized_summary_required"] is True for example in example_set["representative_examples"]), "sanitized summary must be required")

    authorization_example = next(example for example in example_set["representative_examples"] if example["check_name"] == "execution_authorization_check")
    assert_true(authorization_example["failure_mode"] == "execution_authorization_not_satisfied", "authorization failure mode mismatch")
    validate_preflight_evidence_example(authorization_example)

    sanitizer_example = next(example for example in example_set["representative_examples"] if example["check_name"] == "sanitizer_boundary_check")
    assert_true("sanitizer" in sanitizer_example["sanitized_summary"].lower(), "sanitizer summary missing")

    gate = evaluate_preflight_evidence_example_gate(example_set)
    assert_true(gate["preflight_evidence_example_gate_status"] == "examples_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["example_review_satisfied"] is False, "example review must not be satisfied")
    assert_true(gate["example_records_generated"] is True, "gate examples generated must be true")
    assert_true(gate["live_evidence_records_generated"] is False, "gate live evidence must be false")
    assert_true(gate["preflight_satisfied"] is False, "gate preflight must be false")
    assert_true(gate["execution_authorized"] is False, "gate execution authorized must be false")
    validate_preflight_evidence_example_gate_result(gate)

    needs_revision_gate = evaluate_preflight_evidence_example_gate(example_set, example_review_decision="needs_revision")
    assert_true(needs_revision_gate["preflight_evidence_example_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_preflight_evidence_example_gate(example_set, example_review_decision="rejected")
    assert_true(rejected_gate["preflight_evidence_example_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad = copy.deepcopy(example_set)
    bad["live_evidence_records_generated"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "live evidence generated true should fail closed")

    bad = copy.deepcopy(example_set)
    bad["preflight_satisfied"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "preflight_satisfied true should fail closed")

    bad = copy.deepcopy(example_set)
    bad["execution_authorized"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "execution_authorized true should fail closed")

    bad = copy.deepcopy(example_set)
    bad["representative_examples"][0]["check_satisfied"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "satisfied example should fail closed")

    bad = copy.deepcopy(example_set)
    bad["representative_examples"][0]["live_evidence_record_generated"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "live example evidence should fail closed")

    bad = copy.deepcopy(example_set)
    bad["representative_examples"][0]["ai_visible"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "AI-visible example should fail closed")

    bad = copy.deepcopy(example_set)
    bad["example_set_invariants"]["real_execution_permitted"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_set(bad), "real execution invariant true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["example_review_satisfied"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_gate_result(bad_gate), "example review satisfied should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["ready_for_runtime_execution"] = True
    expect_example_error(lambda: validate_preflight_evidence_example_gate_result(bad_gate), "runtime ready true should fail closed")

    bad_model_gate = copy.deepcopy(model_gate)
    bad_model_gate["scope_id"] = "other-scope"
    expect_example_error(
        lambda: build_preflight_evidence_example_set(model, bad_model_gate),
        "model/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_preflight_evidence_examples_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "preflight-evidence-examples" / "demo" / "preflight-evidence-example-gate-result.generated.json"
    assert_true(generated.exists(), "generated preflight evidence example gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["example_records_generated"] is True, "generated gate should record generated examples")
    assert_true(data["live_evidence_records_generated"] is False, "generated gate must not create live evidence")
    assert_true(data["preflight_satisfied"] is False, "generated gate must not satisfy preflight")
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["ready_for_runtime_execution"] is False, "generated gate must not be runtime-ready")

    print("Preflight evidence example tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
