from __future__ import annotations

from typing import Any

from preflight_evidence_examples import (
    REPRESENTATIVE_EXAMPLE_CHECKS,
    validate_preflight_evidence_example_gate_result,
    validate_preflight_evidence_example_set,
)


class PreflightEvidenceValidationRuleError(ValueError):
    pass


VALID_RULE_REVIEW_DECISIONS = {
    "validation_rules_recorded",
    "needs_revision",
    "rejected",
}


REQUIRED_RULE_SET_FIELDS = [
    "preflight_evidence_validation_rule_set_id",
    "rule_set_type",
    "rule_set_status",
    "preflight_evidence_example_set_id",
    "preflight_evidence_model_id",
    "preflight_check_implementation_id",
    "checkpoint_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "validation_rules_recorded",
    "validation_rules_defined",
    "validation_rules_executed_against_examples",
    "generated_examples_validated",
    "live_evidence_records_validated",
    "all_required_evidence_records_validated",
    "all_required_checks_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "ready_for_runtime_execution",
    "ready_for_customer_target",
    "ready_for_external_network",
    "validation_rules",
    "validation_rule_results",
    "rule_set_invariants",
    "rule_set_blockers",
    "next_actions",
    "rule_set_notes",
]


REQUIRED_RULE_FIELDS = [
    "rule_id",
    "rule_name",
    "rule_category",
    "applies_to",
    "severity",
    "required_result",
    "description",
]


REQUIRED_RULE_RESULT_FIELDS = [
    "rule_id",
    "rule_name",
    "applies_to",
    "evaluated",
    "passed_for_generated_examples",
    "live_evidence_validated",
    "failure_mode",
    "notes",
]


REQUIRED_GATE_FIELDS = [
    "preflight_evidence_validation_rule_gate_type",
    "preflight_evidence_validation_rule_gate_status",
    "preflight_evidence_validation_rule_set_id",
    "preflight_evidence_example_set_id",
    "preflight_evidence_model_id",
    "preflight_check_implementation_id",
    "checkpoint_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "rule_review_decision",
    "rule_review_satisfied",
    "validation_rules_defined",
    "validation_rules_executed_against_examples",
    "generated_examples_validated",
    "live_evidence_records_validated",
    "all_required_evidence_records_validated",
    "all_required_checks_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "ready_for_runtime_execution",
    "ready_for_customer_target",
    "ready_for_external_network",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "blockers",
    "next_actions",
]


def _validation_rules() -> list[dict[str, Any]]:
    return [
        {
            "rule_id": "PREFLIGHT-EVR-001",
            "rule_name": "examples_are_not_live_evidence",
            "rule_category": "example_boundary",
            "applies_to": "example_set",
            "severity": "blocking",
            "required_result": "live_evidence_records_generated_false",
            "description": "Generated example records must not be treated as live preflight evidence.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-002",
            "rule_name": "examples_do_not_satisfy_checks",
            "rule_category": "check_satisfaction_boundary",
            "applies_to": "representative_examples",
            "severity": "blocking",
            "required_result": "check_satisfied_false",
            "description": "Generated examples must not satisfy preflight checks.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-003",
            "rule_name": "examples_fail_closed",
            "rule_category": "fail_closed_behavior",
            "applies_to": "representative_examples",
            "severity": "blocking",
            "required_result": "validation_result_failed_closed",
            "description": "Generated examples must express fail-closed outcomes.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-004",
            "rule_name": "examples_do_not_authorize_execution",
            "rule_category": "authorization_boundary",
            "applies_to": "example_set",
            "severity": "blocking",
            "required_result": "execution_authorized_false",
            "description": "Generated examples must not authorize execution.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-005",
            "rule_name": "examples_do_not_satisfy_preflight",
            "rule_category": "preflight_boundary",
            "applies_to": "example_set",
            "severity": "blocking",
            "required_result": "preflight_satisfied_false",
            "description": "Generated examples must not satisfy preflight.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-006",
            "rule_name": "examples_are_not_ai_visible_raw_evidence",
            "rule_category": "ai_visibility_boundary",
            "applies_to": "representative_examples",
            "severity": "blocking",
            "required_result": "ai_visible_false",
            "description": "Generated example records must not be AI-visible raw evidence.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-007",
            "rule_name": "raw_artifact_capture_remains_forbidden",
            "rule_category": "artifact_boundary",
            "applies_to": "example_set",
            "severity": "blocking",
            "required_result": "raw_artifact_capture_permitted_false",
            "description": "Generated examples must not permit raw artifact capture.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-008",
            "rule_name": "sanitized_summary_required",
            "rule_category": "sanitization_boundary",
            "applies_to": "representative_examples",
            "severity": "blocking",
            "required_result": "sanitized_summary_required_true",
            "description": "Generated examples must require sanitized summaries.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-009",
            "rule_name": "representative_examples_cover_required_checks",
            "rule_category": "coverage",
            "applies_to": "example_set",
            "severity": "blocking",
            "required_result": "representative_checks_present",
            "description": "Generated examples must cover the required representative preflight checks.",
        },
        {
            "rule_id": "PREFLIGHT-EVR-010",
            "rule_name": "runtime_execution_remains_disabled",
            "rule_category": "runtime_boundary",
            "applies_to": "example_gate",
            "severity": "blocking",
            "required_result": "ready_for_runtime_execution_false",
            "description": "Validation of examples must not make the platform ready for runtime execution.",
        },
    ]


def _evaluate_rule(rule: dict[str, Any], example_set: dict[str, Any], example_gate: dict[str, Any]) -> dict[str, Any]:
    examples = example_set["representative_examples"]

    checks = {
        "PREFLIGHT-EVR-001": example_set["live_evidence_records_generated"] is False and example_gate["live_evidence_records_generated"] is False,
        "PREFLIGHT-EVR-002": all(example["check_satisfied"] is False for example in examples),
        "PREFLIGHT-EVR-003": all(example["validation_result"] == "failed_closed" and example["fail_closed"] is True for example in examples),
        "PREFLIGHT-EVR-004": example_set["execution_authorized"] is False and example_gate["execution_authorized"] is False,
        "PREFLIGHT-EVR-005": example_set["preflight_satisfied"] is False and example_gate["preflight_satisfied"] is False,
        "PREFLIGHT-EVR-006": all(example["ai_visible"] is False for example in examples),
        "PREFLIGHT-EVR-007": example_set["example_set_invariants"]["raw_artifact_capture_permitted"] is False and example_gate["raw_artifact_capture_permitted"] is False,
        "PREFLIGHT-EVR-008": all(example["sanitized_summary_required"] is True and bool(example["sanitized_summary"]) for example in examples),
        "PREFLIGHT-EVR-009": {example["check_name"] for example in examples} == set(REPRESENTATIVE_EXAMPLE_CHECKS),
        "PREFLIGHT-EVR-010": example_set["ready_for_runtime_execution"] is False and example_gate["ready_for_runtime_execution"] is False,
    }

    passed = checks.get(rule["rule_id"], False)

    return {
        "rule_id": rule["rule_id"],
        "rule_name": rule["rule_name"],
        "applies_to": rule["applies_to"],
        "evaluated": True,
        "passed_for_generated_examples": passed,
        "live_evidence_validated": False,
        "failure_mode": "none" if passed else "generated_example_validation_rule_failed",
        "notes": (
            "Rule evaluated against generated examples only. Passing this rule validates the example boundary "
            "and does not validate live evidence, satisfy preflight, or authorize execution."
        ),
    }


def build_preflight_evidence_validation_rule_set(
    preflight_evidence_example_set: dict[str, Any],
    preflight_evidence_example_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_preflight_evidence_example_set(preflight_evidence_example_set)
    validate_preflight_evidence_example_gate_result(preflight_evidence_example_gate)

    if preflight_evidence_example_set["preflight_evidence_example_set_id"] != preflight_evidence_example_gate["preflight_evidence_example_set_id"]:
        raise PreflightEvidenceValidationRuleError("preflight evidence example set/gate ID mismatch")

    if preflight_evidence_example_set["preflight_evidence_model_id"] != preflight_evidence_example_gate["preflight_evidence_model_id"]:
        raise PreflightEvidenceValidationRuleError("preflight evidence example set/gate model ID mismatch")

    if preflight_evidence_example_set["target_id"] != preflight_evidence_example_gate["target_id"]:
        raise PreflightEvidenceValidationRuleError("preflight evidence example set/gate target_id mismatch")

    if preflight_evidence_example_set["scope_id"] != preflight_evidence_example_gate["scope_id"]:
        raise PreflightEvidenceValidationRuleError("preflight evidence example set/gate scope_id mismatch")

    rules = _validation_rules()
    results = [_evaluate_rule(rule, preflight_evidence_example_set, preflight_evidence_example_gate) for rule in rules]

    rule_set = {
        "preflight_evidence_validation_rule_set_id": (
            f"preflight-evidence-validation-rule-set-{preflight_evidence_example_set['preflight_evidence_example_set_id']}"
        ),
        "rule_set_type": "preflight_evidence_validation_rules",
        "rule_set_status": "validation_rules_recorded_execution_blocked",
        "preflight_evidence_example_set_id": preflight_evidence_example_set["preflight_evidence_example_set_id"],
        "preflight_evidence_model_id": preflight_evidence_example_set["preflight_evidence_model_id"],
        "preflight_check_implementation_id": preflight_evidence_example_set["preflight_check_implementation_id"],
        "checkpoint_id": preflight_evidence_example_set["checkpoint_id"],
        "target_id": preflight_evidence_example_set["target_id"],
        "scope_id": preflight_evidence_example_set["scope_id"],
        "tool": preflight_evidence_example_set["tool"],
        "adapter": preflight_evidence_example_set["adapter"],
        "target_url": preflight_evidence_example_set["target_url"],
        "target_mode": preflight_evidence_example_set["target_mode"],
        "local_only": True,
        "validation_rules_recorded": True,
        "validation_rules_defined": True,
        "validation_rules_executed_against_examples": True,
        "generated_examples_validated": True,
        "live_evidence_records_validated": False,
        "all_required_evidence_records_validated": False,
        "all_required_checks_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "ready_for_runtime_execution": False,
        "ready_for_customer_target": False,
        "ready_for_external_network": False,
        "validation_rules": rules,
        "validation_rule_results": results,
        "rule_set_invariants": {
            "local_only": True,
            "validation_rules_defined": True,
            "validation_rules_executed_against_examples": True,
            "generated_examples_validated": True,
            "live_evidence_records_validated": False,
            "all_required_evidence_records_validated": False,
            "all_required_checks_satisfied": False,
            "preflight_satisfied": False,
            "execution_authorized": False,
            "execution_authorization_satisfied": False,
            "runtime_enforcement_implemented": False,
            "scan_execution_allowed": False,
            "network_activity_allowed": False,
            "real_execution_permitted": False,
            "external_process_execution_allowed": False,
            "credential_injection_permitted": False,
            "raw_artifact_capture_permitted": False,
            "customer_target": False,
            "external_network_target": False,
        },
        "rule_set_blockers": [
            "validation_rules_apply_to_examples_only",
            "live_evidence_records_not_validated",
            "all_required_evidence_records_not_validated",
            "concrete_preflight_checks_not_implemented",
            "all_required_checks_not_satisfied",
            "preflight_not_satisfied",
            "execution_authorization_not_satisfied",
            "runtime_enforcement_not_implemented",
            "runtime_execution_not_allowed",
        ],
        "next_actions": [
            "Extend validation rules from representative examples to all generated example records.",
            "Define validation rules for live preflight evidence separately from generated examples.",
            "Add negative example cases for missing input, mismatch, stale state, unsafe state, and false authorization claims.",
            "Define evidence integrity fields and reconstruction validation rules.",
        ],
        "rule_set_notes": (
            "v0.3.3 defines and executes validation rules against generated preflight evidence examples. "
            "Passing these rules validates example structure only. It does not validate live evidence, satisfy checks, "
            "satisfy preflight, authorize execution, or permit runtime activity."
        ),
    }

    validate_preflight_evidence_validation_rule_set(rule_set)
    return rule_set


def validate_preflight_evidence_validation_rule_set(rule_set: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_RULE_SET_FIELDS if field not in rule_set]
    if missing:
        raise PreflightEvidenceValidationRuleError(f"preflight evidence validation rule set missing fields: {missing}")

    if rule_set.get("rule_set_type") != "preflight_evidence_validation_rules":
        raise PreflightEvidenceValidationRuleError("rule_set_type must be preflight_evidence_validation_rules")

    if rule_set.get("rule_set_status") != "validation_rules_recorded_execution_blocked":
        raise PreflightEvidenceValidationRuleError("rule_set_status must be validation_rules_recorded_execution_blocked")

    if rule_set.get("local_only") is not True:
        raise PreflightEvidenceValidationRuleError("local_only must be true")

    required_true = [
        "validation_rules_recorded",
        "validation_rules_defined",
        "validation_rules_executed_against_examples",
        "generated_examples_validated",
    ]
    for field in required_true:
        if rule_set.get(field) is not True:
            raise PreflightEvidenceValidationRuleError(f"{field} must be true")

    required_false = [
        "live_evidence_records_validated",
        "all_required_evidence_records_validated",
        "all_required_checks_satisfied",
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "ready_for_runtime_execution",
        "ready_for_customer_target",
        "ready_for_external_network",
    ]
    for field in required_false:
        if rule_set.get(field) is not False:
            raise PreflightEvidenceValidationRuleError(f"{field} must be false")

    rules = rule_set.get("validation_rules", [])
    results = rule_set.get("validation_rule_results", [])

    if not isinstance(rules, list) or not rules:
        raise PreflightEvidenceValidationRuleError("validation_rules must be a non-empty list")

    if not isinstance(results, list) or not results:
        raise PreflightEvidenceValidationRuleError("validation_rule_results must be a non-empty list")

    rule_ids = {rule.get("rule_id") for rule in rules}
    result_ids = {result.get("rule_id") for result in results}

    if rule_ids != result_ids:
        raise PreflightEvidenceValidationRuleError("validation rule IDs and result IDs must match")

    for rule in rules:
        validate_preflight_evidence_validation_rule(rule)

    for result in results:
        validate_preflight_evidence_validation_rule_result(result)

    invariants = rule_set.get("rule_set_invariants", {})
    if invariants.get("local_only") is not True:
        raise PreflightEvidenceValidationRuleError("rule set invariant local_only must be true")

    invariant_true = [
        "validation_rules_defined",
        "validation_rules_executed_against_examples",
        "generated_examples_validated",
    ]
    for field in invariant_true:
        if invariants.get(field) is not True:
            raise PreflightEvidenceValidationRuleError(f"rule set invariant must be true: {field}")

    invariant_false = [
        "live_evidence_records_validated",
        "all_required_evidence_records_validated",
        "all_required_checks_satisfied",
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "external_process_execution_allowed",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "customer_target",
        "external_network_target",
    ]
    for field in invariant_false:
        if invariants.get(field) is not False:
            raise PreflightEvidenceValidationRuleError(f"rule set invariant must be false: {field}")

    required_blockers = {
        "validation_rules_apply_to_examples_only",
        "live_evidence_records_not_validated",
        "all_required_evidence_records_not_validated",
        "concrete_preflight_checks_not_implemented",
        "all_required_checks_not_satisfied",
        "preflight_not_satisfied",
        "execution_authorization_not_satisfied",
        "runtime_enforcement_not_implemented",
        "runtime_execution_not_allowed",
    }
    missing_blockers = required_blockers - set(rule_set.get("rule_set_blockers", []))
    if missing_blockers:
        raise PreflightEvidenceValidationRuleError(f"rule set missing blockers: {sorted(missing_blockers)}")


def validate_preflight_evidence_validation_rule(rule: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_RULE_FIELDS if field not in rule]
    if missing:
        raise PreflightEvidenceValidationRuleError(f"validation rule missing fields: {missing}")

    if not str(rule.get("rule_id", "")).startswith("PREFLIGHT-EVR-"):
        raise PreflightEvidenceValidationRuleError("rule_id must start with PREFLIGHT-EVR-")

    if rule.get("severity") != "blocking":
        raise PreflightEvidenceValidationRuleError("validation rules must be blocking")

    if not rule.get("description"):
        raise PreflightEvidenceValidationRuleError("validation rule description must not be empty")


def validate_preflight_evidence_validation_rule_result(result: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_RULE_RESULT_FIELDS if field not in result]
    if missing:
        raise PreflightEvidenceValidationRuleError(f"validation rule result missing fields: {missing}")

    if result.get("evaluated") is not True:
        raise PreflightEvidenceValidationRuleError("validation rule result must be evaluated")

    if result.get("passed_for_generated_examples") is not True:
        raise PreflightEvidenceValidationRuleError("validation rule must pass for generated examples")

    if result.get("live_evidence_validated") is not False:
        raise PreflightEvidenceValidationRuleError("live_evidence_validated must be false")

    if result.get("failure_mode") != "none":
        raise PreflightEvidenceValidationRuleError("passing validation rule result failure_mode must be none")


def evaluate_preflight_evidence_validation_rule_gate(
    rule_set: dict[str, Any],
    *,
    rule_review_decision: str = "validation_rules_recorded",
) -> dict[str, Any]:
    validate_preflight_evidence_validation_rule_set(rule_set)

    if rule_review_decision not in VALID_RULE_REVIEW_DECISIONS:
        raise PreflightEvidenceValidationRuleError(f"unsupported rule_review_decision: {rule_review_decision}")

    if rule_review_decision == "validation_rules_recorded":
        gate_status = "validation_rules_recorded_execution_blocked"
        blockers = list(rule_set["rule_set_blockers"])
    elif rule_review_decision == "needs_revision":
        gate_status = "needs_revision"
        blockers = list(rule_set["rule_set_blockers"])
    else:
        gate_status = "rejected"
        blockers = ["preflight_evidence_validation_rules_rejected"]

    invariants = rule_set["rule_set_invariants"]

    gate = {
        "preflight_evidence_validation_rule_gate_type": "preflight_evidence_validation_rules_gate",
        "preflight_evidence_validation_rule_gate_status": gate_status,
        "preflight_evidence_validation_rule_set_id": rule_set["preflight_evidence_validation_rule_set_id"],
        "preflight_evidence_example_set_id": rule_set["preflight_evidence_example_set_id"],
        "preflight_evidence_model_id": rule_set["preflight_evidence_model_id"],
        "preflight_check_implementation_id": rule_set["preflight_check_implementation_id"],
        "checkpoint_id": rule_set["checkpoint_id"],
        "target_id": rule_set["target_id"],
        "scope_id": rule_set["scope_id"],
        "tool": rule_set["tool"],
        "adapter": rule_set["adapter"],
        "target_url": rule_set["target_url"],
        "target_mode": rule_set["target_mode"],
        "local_only": True,
        "rule_review_decision": rule_review_decision,
        "rule_review_satisfied": False,
        "validation_rules_defined": True,
        "validation_rules_executed_against_examples": True,
        "generated_examples_validated": True,
        "live_evidence_records_validated": False,
        "all_required_evidence_records_validated": False,
        "all_required_checks_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "ready_for_runtime_execution": False,
        "ready_for_customer_target": False,
        "ready_for_external_network": False,
        "scan_execution_allowed": invariants["scan_execution_allowed"],
        "network_activity_allowed": invariants["network_activity_allowed"],
        "real_execution_permitted": invariants["real_execution_permitted"],
        "external_process_execution_allowed": invariants["external_process_execution_allowed"],
        "credential_injection_permitted": invariants["credential_injection_permitted"],
        "raw_artifact_capture_permitted": invariants["raw_artifact_capture_permitted"],
        "customer_target": invariants["customer_target"],
        "external_network_target": invariants["external_network_target"],
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "validation_rules_apply_to_examples_only",
                "next_action": "Define separate validation rules for live preflight evidence records.",
            },
            {
                "blocker": "all_required_evidence_records_not_validated",
                "next_action": "Extend validation from representative examples to all required preflight evidence records.",
            },
            {
                "blocker": "concrete_preflight_checks_not_implemented",
                "next_action": "Implement pure preflight validation checks before live evidence validation.",
            },
            {
                "blocker": "runtime_execution_not_allowed",
                "next_action": "Keep runtime execution disabled until a later explicit execution boundary change.",
            },
        ],
    }

    validate_preflight_evidence_validation_rule_gate_result(gate)
    return gate


def validate_preflight_evidence_validation_rule_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise PreflightEvidenceValidationRuleError(f"preflight evidence validation rule gate missing fields: {missing}")

    if gate.get("preflight_evidence_validation_rule_gate_type") != "preflight_evidence_validation_rules_gate":
        raise PreflightEvidenceValidationRuleError("preflight_evidence_validation_rule_gate_type mismatch")

    if gate.get("rule_review_decision") not in VALID_RULE_REVIEW_DECISIONS:
        raise PreflightEvidenceValidationRuleError("unsupported rule_review_decision")

    if gate.get("local_only") is not True:
        raise PreflightEvidenceValidationRuleError("local_only must be true")

    required_true = [
        "validation_rules_defined",
        "validation_rules_executed_against_examples",
        "generated_examples_validated",
    ]
    for field in required_true:
        if gate.get(field) is not True:
            raise PreflightEvidenceValidationRuleError(f"{field} must be true")

    required_false = [
        "rule_review_satisfied",
        "live_evidence_records_validated",
        "all_required_evidence_records_validated",
        "all_required_checks_satisfied",
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "ready_for_runtime_execution",
        "ready_for_customer_target",
        "ready_for_external_network",
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "external_process_execution_allowed",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "customer_target",
        "external_network_target",
    ]
    for field in required_false:
        if gate.get(field) is not False:
            raise PreflightEvidenceValidationRuleError(f"{field} must be false")

    if not gate.get("blockers"):
        raise PreflightEvidenceValidationRuleError("preflight evidence validation rule gate must include blockers")
