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

from preflight_evidence_validation_rules import (
    PreflightEvidenceValidationRuleError,
    build_preflight_evidence_validation_rule_set,
    evaluate_preflight_evidence_validation_rule_gate,
    validate_preflight_evidence_validation_rule_gate_result,
    validate_preflight_evidence_validation_rule_set,
)
from preflight_evidence_examples import (
    build_preflight_evidence_example_set,
    evaluate_preflight_evidence_example_gate,
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


def expect_rule_error(fn, message: str) -> None:
    try:
        fn()
    except PreflightEvidenceValidationRuleError:
        return
    raise AssertionError(message)


def build_demo_rule_set():
    preflight, preflight_gate = build_demo_preflight_pair()
    checkpoint = build_runtime_transition_checkpoint(preflight, preflight_gate)
    implementation = build_preflight_check_implementation_scaffold(checkpoint)
    implementation_gate = evaluate_preflight_check_implementation_gate(implementation)
    model = build_preflight_evidence_record_model(implementation, implementation_gate)
    model_gate = evaluate_preflight_evidence_record_model_gate(model)
    example_set = build_preflight_evidence_example_set(model, model_gate)
    example_gate = evaluate_preflight_evidence_example_gate(example_set)
    rule_set = build_preflight_evidence_validation_rule_set(example_set, example_gate)
    return example_set, example_gate, rule_set


def main() -> int:
    example_set, example_gate, rule_set = build_demo_rule_set()
    validate_preflight_evidence_validation_rule_set(rule_set)

    assert_true(rule_set["rule_set_status"] == "validation_rules_recorded_execution_blocked", "rule set status mismatch")
    assert_true(rule_set["local_only"] is True, "rule set must be local-only")
    assert_true(rule_set["validation_rules_defined"] is True, "validation rules should be defined")
    assert_true(rule_set["validation_rules_executed_against_examples"] is True, "rules should execute against examples")
    assert_true(rule_set["generated_examples_validated"] is True, "generated examples should validate")
    assert_true(rule_set["live_evidence_records_validated"] is False, "live evidence must not be validated")
    assert_true(rule_set["all_required_evidence_records_validated"] is False, "all required evidence must not be validated")
    assert_true(rule_set["preflight_satisfied"] is False, "preflight must not be satisfied")
    assert_true(rule_set["execution_authorized"] is False, "execution must not be authorized")
    assert_true(rule_set["ready_for_runtime_execution"] is False, "must not be runtime-ready")
    assert_true(len(rule_set["validation_rules"]) == 10, "rule count mismatch")
    assert_true(len(rule_set["validation_rule_results"]) == 10, "rule result count mismatch")
    assert_true(all(result["evaluated"] is True for result in rule_set["validation_rule_results"]), "all rules must be evaluated")
    assert_true(all(result["passed_for_generated_examples"] is True for result in rule_set["validation_rule_results"]), "all rules must pass for examples")
    assert_true(all(result["live_evidence_validated"] is False for result in rule_set["validation_rule_results"]), "live evidence validation must be false")

    gate = evaluate_preflight_evidence_validation_rule_gate(rule_set)
    assert_true(gate["preflight_evidence_validation_rule_gate_status"] == "validation_rules_recorded_execution_blocked", "gate status mismatch")
    assert_true(gate["rule_review_satisfied"] is False, "rule review must not be satisfied")
    assert_true(gate["generated_examples_validated"] is True, "gate generated examples validated should be true")
    assert_true(gate["live_evidence_records_validated"] is False, "gate live evidence validation must be false")
    assert_true(gate["preflight_satisfied"] is False, "gate preflight must be false")
    assert_true(gate["execution_authorized"] is False, "gate execution authorized must be false")
    validate_preflight_evidence_validation_rule_gate_result(gate)

    needs_revision_gate = evaluate_preflight_evidence_validation_rule_gate(rule_set, rule_review_decision="needs_revision")
    assert_true(needs_revision_gate["preflight_evidence_validation_rule_gate_status"] == "needs_revision", "needs_revision status mismatch")
    assert_true(needs_revision_gate["execution_authorized"] is False, "needs_revision must not authorize execution")

    rejected_gate = evaluate_preflight_evidence_validation_rule_gate(rule_set, rule_review_decision="rejected")
    assert_true(rejected_gate["preflight_evidence_validation_rule_gate_status"] == "rejected", "rejected status mismatch")
    assert_true(rejected_gate["execution_authorized"] is False, "rejected must not authorize execution")

    bad = copy.deepcopy(rule_set)
    bad["live_evidence_records_validated"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "live evidence validated true should fail closed")

    bad = copy.deepcopy(rule_set)
    bad["preflight_satisfied"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "preflight_satisfied true should fail closed")

    bad = copy.deepcopy(rule_set)
    bad["execution_authorized"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "execution_authorized true should fail closed")

    bad = copy.deepcopy(rule_set)
    bad["validation_rule_results"][0]["passed_for_generated_examples"] = False
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "failed validation rule should fail closed")

    bad = copy.deepcopy(rule_set)
    bad["validation_rule_results"][0]["live_evidence_validated"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "live evidence validated result should fail closed")

    bad = copy.deepcopy(rule_set)
    bad["rule_set_invariants"]["real_execution_permitted"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_set(bad), "real execution invariant true should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["rule_review_satisfied"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_gate_result(bad_gate), "rule review satisfied should fail closed")

    bad_gate = copy.deepcopy(gate)
    bad_gate["ready_for_runtime_execution"] = True
    expect_rule_error(lambda: validate_preflight_evidence_validation_rule_gate_result(bad_gate), "runtime ready true should fail closed")

    bad_example_gate = copy.deepcopy(example_gate)
    bad_example_gate["scope_id"] = "other-scope"
    expect_rule_error(
        lambda: build_preflight_evidence_validation_rule_set(example_set, bad_example_gate),
        "example/gate scope mismatch should fail closed",
    )

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_preflight_evidence_validation_rules_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "preflight-evidence-validation-rules" / "demo" / "preflight-evidence-validation-rule-gate-result.generated.json"
    assert_true(generated.exists(), "generated preflight evidence validation rule gate missing")
    data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(data["generated_examples_validated"] is True, "generated gate should validate examples")
    assert_true(data["live_evidence_records_validated"] is False, "generated gate must not validate live evidence")
    assert_true(data["preflight_satisfied"] is False, "generated gate must not satisfy preflight")
    assert_true(data["execution_authorized"] is False, "generated gate must not authorize execution")
    assert_true(data["ready_for_runtime_execution"] is False, "generated gate must not be runtime-ready")

    print("Preflight evidence validation rule tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
