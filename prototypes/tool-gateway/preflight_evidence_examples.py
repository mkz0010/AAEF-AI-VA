from __future__ import annotations

from typing import Any

from preflight_evidence_record import (
    validate_preflight_evidence_record_model,
    validate_preflight_evidence_record_model_gate_result,
)


class PreflightEvidenceExampleError(ValueError):
    pass


VALID_EXAMPLE_REVIEW_DECISIONS = {
    "examples_recorded",
    "needs_revision",
    "rejected",
}


REPRESENTATIVE_EXAMPLE_CHECKS = [
    "runtime_readiness_check",
    "runtime_destination_binding_check",
    "execution_authorization_check",
    "no_egress_guard_check",
    "sanitizer_boundary_check",
]


REQUIRED_EXAMPLE_SET_FIELDS = [
    "preflight_evidence_example_set_id",
    "example_set_type",
    "example_set_status",
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
    "examples_recorded",
    "example_records_generated",
    "live_evidence_records_generated",
    "all_required_evidence_records_generated",
    "all_required_checks_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "ready_for_runtime_execution",
    "ready_for_customer_target",
    "ready_for_external_network",
    "representative_examples",
    "example_set_invariants",
    "example_set_blockers",
    "next_actions",
    "example_set_notes",
]


REQUIRED_EXAMPLE_FIELDS = [
    "example_id",
    "check_name",
    "evidence_type",
    "example_type",
    "example_status",
    "example_record_generated",
    "live_evidence_record_generated",
    "check_implemented",
    "check_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "validation_result",
    "failure_mode",
    "fail_closed",
    "input_sources",
    "observed_inputs",
    "simulated_observations",
    "mismatch_detected",
    "stale_state_detected",
    "unsafe_state_detected",
    "ai_visible",
    "raw_artifact_capture_permitted",
    "sanitized_summary_required",
    "sanitized_summary",
    "reconstruction_hints",
    "example_notes",
]


REQUIRED_GATE_FIELDS = [
    "preflight_evidence_example_gate_type",
    "preflight_evidence_example_gate_status",
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
    "example_review_decision",
    "example_review_satisfied",
    "example_records_generated",
    "live_evidence_records_generated",
    "all_required_evidence_records_generated",
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


def _records_by_check(model: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {record["check_name"]: record for record in model["preflight_evidence_records"]}


def _example_for_record(record: dict[str, Any]) -> dict[str, Any]:
    check_name = record["check_name"]

    if check_name == "runtime_readiness_check":
        validation_result = "failed_closed"
        failure_mode = "runtime_not_detected_or_not_current"
        simulated_observations = [
            "runtime readiness evidence exists as model input only",
            "current runtime verification has not been implemented",
            "future runtime execution must remain blocked",
        ]
        sanitized_summary = "Runtime readiness check example remains fail-closed because current runtime verification is not implemented."
    elif check_name == "runtime_destination_binding_check":
        validation_result = "failed_closed"
        failure_mode = "binding_reverification_not_implemented"
        simulated_observations = [
            "runtime-target binding exists as a scaffolded destination record",
            "execution-time rebinding verification has not been implemented",
            "targetless or mismatched execution must remain blocked",
        ]
        sanitized_summary = "Runtime destination binding check example remains fail-closed because execution-time rebinding verification is not implemented."
    elif check_name == "execution_authorization_check":
        validation_result = "failed_closed"
        failure_mode = "execution_authorization_not_satisfied"
        simulated_observations = [
            "execution_authorized is false",
            "execution_authorization_satisfied is false",
            "authorization scaffold is recorded but not satisfied",
        ]
        sanitized_summary = "Execution authorization check example confirms execution remains unauthorized."
    elif check_name == "no_egress_guard_check":
        validation_result = "failed_closed"
        failure_mode = "no_egress_guard_not_verified"
        simulated_observations = [
            "no-egress policy is defined as a scaffold",
            "runtime no-egress enforcement is not implemented",
            "network activity remains disabled",
        ]
        sanitized_summary = "No-egress guard check example remains fail-closed because enforcement verification is not implemented."
    elif check_name == "sanitizer_boundary_check":
        validation_result = "failed_closed"
        failure_mode = "sanitizer_boundary_not_verified"
        simulated_observations = [
            "sanitized summary is required",
            "raw artifact capture is not permitted",
            "AI-visible evidence is disabled until sanitizer boundary verification exists",
        ]
        sanitized_summary = "Sanitizer boundary check example remains fail-closed and non-AI-visible except for this sanitized summary."
    else:
        raise PreflightEvidenceExampleError(f"unsupported representative example check: {check_name}")

    return {
        "example_id": f"preflight-evidence-example-{check_name}",
        "check_name": check_name,
        "evidence_type": record["evidence_type"],
        "example_type": "generated_preflight_evidence_record_example",
        "example_status": "example_generated_fail_closed",
        "example_record_generated": True,
        "live_evidence_record_generated": False,
        "check_implemented": False,
        "check_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "validation_result": validation_result,
        "failure_mode": failure_mode,
        "fail_closed": True,
        "input_sources": list(record["input_sources"]),
        "observed_inputs": [],
        "simulated_observations": simulated_observations,
        "mismatch_detected": False,
        "stale_state_detected": False,
        "unsafe_state_detected": False,
        "ai_visible": False,
        "raw_artifact_capture_permitted": False,
        "sanitized_summary_required": True,
        "sanitized_summary": sanitized_summary,
        "reconstruction_hints": [
            "link example to preflight evidence record model",
            "link example to check_name and evidence_type",
            "preserve fail-closed reason",
            "do not infer execution authorization from example generation",
        ],
        "example_notes": (
            "This is a generated example record for scaffold validation only. It is not live evidence, "
            "does not satisfy the check, and does not authorize execution."
        ),
    }


def build_preflight_evidence_example_set(
    preflight_evidence_model: dict[str, Any],
    preflight_evidence_model_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_preflight_evidence_record_model(preflight_evidence_model)
    validate_preflight_evidence_record_model_gate_result(preflight_evidence_model_gate)

    if preflight_evidence_model["preflight_evidence_model_id"] != preflight_evidence_model_gate["preflight_evidence_model_id"]:
        raise PreflightEvidenceExampleError("preflight evidence model/gate ID mismatch")

    if preflight_evidence_model["preflight_check_implementation_id"] != preflight_evidence_model_gate["preflight_check_implementation_id"]:
        raise PreflightEvidenceExampleError("preflight evidence model/gate implementation ID mismatch")

    if preflight_evidence_model["target_id"] != preflight_evidence_model_gate["target_id"]:
        raise PreflightEvidenceExampleError("preflight evidence model/gate target_id mismatch")

    if preflight_evidence_model["scope_id"] != preflight_evidence_model_gate["scope_id"]:
        raise PreflightEvidenceExampleError("preflight evidence model/gate scope_id mismatch")

    records = _records_by_check(preflight_evidence_model)
    examples = [_example_for_record(records[check_name]) for check_name in REPRESENTATIVE_EXAMPLE_CHECKS]

    example_set = {
        "preflight_evidence_example_set_id": (
            f"preflight-evidence-example-set-{preflight_evidence_model['preflight_evidence_model_id']}"
        ),
        "example_set_type": "generated_preflight_evidence_record_examples",
        "example_set_status": "examples_recorded_execution_blocked",
        "preflight_evidence_model_id": preflight_evidence_model["preflight_evidence_model_id"],
        "preflight_check_implementation_id": preflight_evidence_model["preflight_check_implementation_id"],
        "checkpoint_id": preflight_evidence_model["checkpoint_id"],
        "target_id": preflight_evidence_model["target_id"],
        "scope_id": preflight_evidence_model["scope_id"],
        "tool": preflight_evidence_model["tool"],
        "adapter": preflight_evidence_model["adapter"],
        "target_url": preflight_evidence_model["target_url"],
        "target_mode": preflight_evidence_model["target_mode"],
        "local_only": True,
        "examples_recorded": True,
        "example_records_generated": True,
        "live_evidence_records_generated": False,
        "all_required_evidence_records_generated": False,
        "all_required_checks_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "ready_for_runtime_execution": False,
        "ready_for_customer_target": False,
        "ready_for_external_network": False,
        "representative_examples": examples,
        "example_set_invariants": {
            "local_only": True,
            "examples_recorded": True,
            "example_records_generated": True,
            "live_evidence_records_generated": False,
            "all_required_evidence_records_generated": False,
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
        "example_set_blockers": [
            "examples_are_not_live_evidence",
            "live_preflight_evidence_records_not_generated",
            "all_required_evidence_records_not_generated",
            "concrete_preflight_checks_not_implemented",
            "all_required_checks_not_satisfied",
            "preflight_not_satisfied",
            "execution_authorization_not_satisfied",
            "runtime_enforcement_not_implemented",
            "runtime_execution_not_allowed",
        ],
        "next_actions": [
            "Define validation rules for generated example records.",
            "Add more negative examples for missing inputs, mismatched bindings, and stale state.",
            "Add sanitized summary examples for evidence that would otherwise be unsafe for AI visibility.",
            "Define live preflight evidence generation separately from example generation.",
        ],
        "example_set_notes": (
            "v0.3.2 records representative generated preflight evidence examples. These are examples, not live "
            "preflight evidence. They do not satisfy checks, satisfy preflight, authorize execution, or permit runtime activity."
        ),
    }

    validate_preflight_evidence_example_set(example_set)
    return example_set


def validate_preflight_evidence_example_set(example_set: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_EXAMPLE_SET_FIELDS if field not in example_set]
    if missing:
        raise PreflightEvidenceExampleError(f"preflight evidence example set missing fields: {missing}")

    if example_set.get("example_set_type") != "generated_preflight_evidence_record_examples":
        raise PreflightEvidenceExampleError("example_set_type must be generated_preflight_evidence_record_examples")

    if example_set.get("example_set_status") != "examples_recorded_execution_blocked":
        raise PreflightEvidenceExampleError("example_set_status must be examples_recorded_execution_blocked")

    if example_set.get("local_only") is not True:
        raise PreflightEvidenceExampleError("local_only must be true")

    required_true = [
        "examples_recorded",
        "example_records_generated",
    ]
    for field in required_true:
        if example_set.get(field) is not True:
            raise PreflightEvidenceExampleError(f"{field} must be true")

    required_false = [
        "live_evidence_records_generated",
        "all_required_evidence_records_generated",
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
        if example_set.get(field) is not False:
            raise PreflightEvidenceExampleError(f"{field} must be false")

    examples = example_set.get("representative_examples", [])
    if not isinstance(examples, list):
        raise PreflightEvidenceExampleError("representative_examples must be a list")

    example_names = {example.get("check_name") for example in examples}
    missing_examples = set(REPRESENTATIVE_EXAMPLE_CHECKS) - example_names
    if missing_examples:
        raise PreflightEvidenceExampleError(f"representative_examples missing checks: {sorted(missing_examples)}")

    for example in examples:
        validate_preflight_evidence_example(example)

    invariants = example_set.get("example_set_invariants", {})
    if invariants.get("local_only") is not True:
        raise PreflightEvidenceExampleError("example set invariant local_only must be true")
    if invariants.get("examples_recorded") is not True:
        raise PreflightEvidenceExampleError("example set invariant examples_recorded must be true")
    if invariants.get("example_records_generated") is not True:
        raise PreflightEvidenceExampleError("example set invariant example_records_generated must be true")

    invariant_false = [
        "live_evidence_records_generated",
        "all_required_evidence_records_generated",
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
            raise PreflightEvidenceExampleError(f"example set invariant must be false: {field}")

    required_blockers = {
        "examples_are_not_live_evidence",
        "live_preflight_evidence_records_not_generated",
        "all_required_evidence_records_not_generated",
        "concrete_preflight_checks_not_implemented",
        "all_required_checks_not_satisfied",
        "preflight_not_satisfied",
        "execution_authorization_not_satisfied",
        "runtime_enforcement_not_implemented",
        "runtime_execution_not_allowed",
    }
    missing_blockers = required_blockers - set(example_set.get("example_set_blockers", []))
    if missing_blockers:
        raise PreflightEvidenceExampleError(f"example set missing blockers: {sorted(missing_blockers)}")


def validate_preflight_evidence_example(example: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_EXAMPLE_FIELDS if field not in example]
    if missing:
        raise PreflightEvidenceExampleError(f"preflight evidence example missing fields: {missing}")

    if example.get("check_name") not in REPRESENTATIVE_EXAMPLE_CHECKS:
        raise PreflightEvidenceExampleError(f"unsupported example check_name: {example.get('check_name')}")

    if example.get("example_type") != "generated_preflight_evidence_record_example":
        raise PreflightEvidenceExampleError("example_type must be generated_preflight_evidence_record_example")

    if example.get("example_status") != "example_generated_fail_closed":
        raise PreflightEvidenceExampleError("example_status must be example_generated_fail_closed")

    required_true = [
        "example_record_generated",
        "fail_closed",
        "sanitized_summary_required",
    ]
    for field in required_true:
        if example.get(field) is not True:
            raise PreflightEvidenceExampleError(f"{field} must be true")

    required_false = [
        "live_evidence_record_generated",
        "check_implemented",
        "check_satisfied",
        "preflight_satisfied",
        "execution_authorized",
        "mismatch_detected",
        "stale_state_detected",
        "unsafe_state_detected",
        "ai_visible",
        "raw_artifact_capture_permitted",
    ]
    for field in required_false:
        if example.get(field) is not False:
            raise PreflightEvidenceExampleError(f"{field} must be false")

    if example.get("validation_result") != "failed_closed":
        raise PreflightEvidenceExampleError("validation_result must be failed_closed")

    if not example.get("failure_mode"):
        raise PreflightEvidenceExampleError("failure_mode must not be empty")

    if not example.get("input_sources"):
        raise PreflightEvidenceExampleError("input_sources must not be empty")

    if example.get("observed_inputs") != []:
        raise PreflightEvidenceExampleError("observed_inputs must be empty for non-live examples")

    if not example.get("simulated_observations"):
        raise PreflightEvidenceExampleError("simulated_observations must not be empty")

    if not example.get("sanitized_summary"):
        raise PreflightEvidenceExampleError("sanitized_summary must not be empty")


def evaluate_preflight_evidence_example_gate(
    example_set: dict[str, Any],
    *,
    example_review_decision: str = "examples_recorded",
) -> dict[str, Any]:
    validate_preflight_evidence_example_set(example_set)

    if example_review_decision not in VALID_EXAMPLE_REVIEW_DECISIONS:
        raise PreflightEvidenceExampleError(f"unsupported example_review_decision: {example_review_decision}")

    if example_review_decision == "examples_recorded":
        gate_status = "examples_recorded_execution_blocked"
        blockers = list(example_set["example_set_blockers"])
    elif example_review_decision == "needs_revision":
        gate_status = "needs_revision"
        blockers = list(example_set["example_set_blockers"])
    else:
        gate_status = "rejected"
        blockers = ["preflight_evidence_examples_rejected"]

    invariants = example_set["example_set_invariants"]

    gate = {
        "preflight_evidence_example_gate_type": "generated_preflight_evidence_record_examples_gate",
        "preflight_evidence_example_gate_status": gate_status,
        "preflight_evidence_example_set_id": example_set["preflight_evidence_example_set_id"],
        "preflight_evidence_model_id": example_set["preflight_evidence_model_id"],
        "preflight_check_implementation_id": example_set["preflight_check_implementation_id"],
        "checkpoint_id": example_set["checkpoint_id"],
        "target_id": example_set["target_id"],
        "scope_id": example_set["scope_id"],
        "tool": example_set["tool"],
        "adapter": example_set["adapter"],
        "target_url": example_set["target_url"],
        "target_mode": example_set["target_mode"],
        "local_only": True,
        "example_review_decision": example_review_decision,
        "example_review_satisfied": False,
        "example_records_generated": True,
        "live_evidence_records_generated": False,
        "all_required_evidence_records_generated": False,
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
                "blocker": "examples_are_not_live_evidence",
                "next_action": "Keep generated examples separate from live preflight evidence records.",
            },
            {
                "blocker": "live_preflight_evidence_records_not_generated",
                "next_action": "Define live evidence generation only after concrete preflight checks exist.",
            },
            {
                "blocker": "concrete_preflight_checks_not_implemented",
                "next_action": "Implement pure validation checks without enabling runtime execution.",
            },
            {
                "blocker": "runtime_execution_not_allowed",
                "next_action": "Keep runtime execution disabled until a later explicit execution boundary change.",
            },
        ],
    }

    validate_preflight_evidence_example_gate_result(gate)
    return gate


def validate_preflight_evidence_example_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise PreflightEvidenceExampleError(f"preflight evidence example gate missing fields: {missing}")

    if gate.get("preflight_evidence_example_gate_type") != "generated_preflight_evidence_record_examples_gate":
        raise PreflightEvidenceExampleError("preflight_evidence_example_gate_type mismatch")

    if gate.get("example_review_decision") not in VALID_EXAMPLE_REVIEW_DECISIONS:
        raise PreflightEvidenceExampleError("unsupported example_review_decision")

    if gate.get("local_only") is not True:
        raise PreflightEvidenceExampleError("local_only must be true")

    if gate.get("example_records_generated") is not True:
        raise PreflightEvidenceExampleError("example_records_generated must be true")

    required_false = [
        "example_review_satisfied",
        "live_evidence_records_generated",
        "all_required_evidence_records_generated",
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
            raise PreflightEvidenceExampleError(f"{field} must be false")

    if not gate.get("blockers"):
        raise PreflightEvidenceExampleError("preflight evidence example gate must include blockers")
