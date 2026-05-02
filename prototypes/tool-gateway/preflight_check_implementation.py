from __future__ import annotations

from typing import Any

from preflight_validation import PREFLIGHT_CHECKS
from runtime_transition_checkpoint import (
    RuntimeTransitionCheckpointError,
    validate_runtime_transition_checkpoint,
)


class PreflightCheckImplementationError(ValueError):
    pass


VALID_IMPLEMENTATION_REVIEW_DECISIONS = {
    "implementation_scaffold_recorded",
    "needs_revision",
    "rejected",
}


CHECK_IMPLEMENTATION_DETAILS = {
    "runtime_readiness_check": {
        "input_sources": ["runtime_profile", "runtime_readiness_result"],
        "evidence_type": "runtime_readiness_verification_evidence",
        "responsibility": "verify the current local runtime readiness result immediately before any future execution request",
    },
    "local_target_lab_profile_check": {
        "input_sources": ["local_target_lab_profile", "local_target_lab_gate_result"],
        "evidence_type": "local_target_lab_verification_evidence",
        "responsibility": "verify that the target is local, intentionally vulnerable, non-customer, and non-external",
    },
    "runtime_destination_binding_check": {
        "input_sources": ["runtime_destination_binding", "runtime_destination_binding_gate_result"],
        "evidence_type": "runtime_destination_binding_verification_evidence",
        "responsibility": "verify that runtime, target, scope, and destination binding match at execution-request time",
    },
    "bounded_execution_transition_check": {
        "input_sources": ["bounded_execution_transition_candidate", "bounded_execution_transition_gate_result"],
        "evidence_type": "bounded_execution_transition_verification_evidence",
        "responsibility": "verify that the transition candidate remains local-only and execution-blocked",
    },
    "local_execution_plan_check": {
        "input_sources": ["local_execution_plan", "local_execution_plan_review_gate_result"],
        "evidence_type": "local_execution_plan_verification_evidence",
        "responsibility": "verify that only allowed plan-level operations are present and prohibited runtime operations remain blocked",
    },
    "runtime_safety_policy_check": {
        "input_sources": ["runtime_safety_policy", "runtime_safety_policy_gate_result"],
        "evidence_type": "runtime_safety_policy_verification_evidence",
        "responsibility": "verify no-egress, timeout, kill-switch, evidence, sanitizer, and approval policy requirements",
    },
    "runtime_enforcement_design_check": {
        "input_sources": ["runtime_enforcement_design", "runtime_enforcement_design_gate_result"],
        "evidence_type": "runtime_enforcement_design_verification_evidence",
        "responsibility": "verify that enforcement components are defined but still not implemented in the current scaffold",
    },
    "execution_authorization_check": {
        "input_sources": ["execution_authorization", "execution_authorization_gate_result"],
        "evidence_type": "execution_authorization_verification_evidence",
        "responsibility": "verify execution authorization remains unsatisfied and execution_authorized remains false",
    },
    "human_approval_check": {
        "input_sources": ["human_approval_record", "execution_authorization"],
        "evidence_type": "human_approval_binding_evidence",
        "responsibility": "verify whether a future human approval record is present and bound to the execution request",
    },
    "operator_confirmation_check": {
        "input_sources": ["operator_confirmation_record", "execution_authorization"],
        "evidence_type": "operator_confirmation_binding_evidence",
        "responsibility": "verify whether a future operator confirmation record is present and bound to the execution request",
    },
    "scope_owner_approval_check": {
        "input_sources": ["scope_owner_approval_record", "scope_registry_destination_binding"],
        "evidence_type": "scope_owner_approval_binding_evidence",
        "responsibility": "verify whether a future scope owner approval record is present and bound to the scoped destination",
    },
    "no_egress_guard_check": {
        "input_sources": ["runtime_safety_policy", "no_egress_guard_verification_record"],
        "evidence_type": "no_egress_guard_verification_evidence",
        "responsibility": "verify local-only destination constraints and denied destination categories before any future network-capable execution",
    },
    "timeout_watcher_check": {
        "input_sources": ["runtime_safety_policy", "timeout_watcher_verification_record"],
        "evidence_type": "timeout_watcher_verification_evidence",
        "responsibility": "verify max runtime and idle timeout controls before any future process launch",
    },
    "kill_switch_controller_check": {
        "input_sources": ["runtime_safety_policy", "kill_switch_controller_verification_record"],
        "evidence_type": "kill_switch_controller_verification_evidence",
        "responsibility": "verify manual, timeout, policy-violation, and process-tree stop behavior before any future process launch",
    },
    "evidence_emitter_check": {
        "input_sources": ["evidence_emitter_verification_record"],
        "evidence_type": "evidence_emitter_verification_evidence",
        "responsibility": "verify future evidence emission for preflight, authorization, runtime, stop, and artifact handling events",
    },
    "sanitizer_boundary_check": {
        "input_sources": ["sanitizer_policy", "sanitizer_boundary_verification_record"],
        "evidence_type": "sanitizer_boundary_verification_evidence",
        "responsibility": "verify raw artifacts remain non-AI-visible until sanitizer output is generated and validated",
    },
}


REQUIRED_IMPLEMENTATION_FIELDS = [
    "preflight_check_implementation_id",
    "implementation_type",
    "implementation_status",
    "checkpoint_id",
    "project_phase",
    "current_version_target",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "preflight_check_implementation_scaffold_recorded",
    "concrete_checks_implemented",
    "all_required_checks_defined",
    "all_required_checks_have_implementation_scaffolds",
    "all_required_checks_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "ready_for_runtime_execution",
    "ready_for_customer_target",
    "ready_for_external_network",
    "check_implementations",
    "implementation_invariants",
    "implementation_blockers",
    "next_actions",
    "implementation_notes",
]


REQUIRED_GATE_FIELDS = [
    "preflight_check_implementation_gate_type",
    "preflight_check_implementation_gate_status",
    "preflight_check_implementation_id",
    "checkpoint_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "implementation_review_decision",
    "implementation_review_satisfied",
    "concrete_checks_implemented",
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


def _build_check_implementations(required_checks: list[str]) -> list[dict[str, Any]]:
    implementations: list[dict[str, Any]] = []

    for check_name in required_checks:
        details = CHECK_IMPLEMENTATION_DETAILS.get(check_name)
        if details is None:
            raise PreflightCheckImplementationError(f"missing implementation detail for check: {check_name}")

        implementations.append(
            {
                "check_name": check_name,
                "implementation_status": "implementation_scaffold_recorded_not_implemented",
                "implemented": False,
                "satisfied": False,
                "required": True,
                "input_sources": list(details["input_sources"]),
                "evidence_type": details["evidence_type"],
                "evidence_record_required": True,
                "evidence_record_generated": False,
                "fail_closed_on_missing_input": True,
                "fail_closed_on_mismatch": True,
                "fail_closed_on_stale_state": True,
                "responsibility": details["responsibility"],
            }
        )

    return implementations


def build_preflight_check_implementation_scaffold(
    runtime_transition_checkpoint: dict[str, Any],
) -> dict[str, Any]:
    try:
        validate_runtime_transition_checkpoint(runtime_transition_checkpoint)
    except RuntimeTransitionCheckpointError as exc:
        raise PreflightCheckImplementationError(str(exc)) from exc

    required_checks = list(runtime_transition_checkpoint["required_preflight_checks"])
    check_implementations = _build_check_implementations(required_checks)

    implementation = {
        "preflight_check_implementation_id": (
            f"preflight-check-implementation-{runtime_transition_checkpoint['checkpoint_id']}"
        ),
        "implementation_type": "concrete_preflight_check_implementation_scaffold",
        "implementation_status": "implementation_scaffold_recorded_execution_blocked",
        "checkpoint_id": runtime_transition_checkpoint["checkpoint_id"],
        "project_phase": "v0.3.0-preflight-implementation-scaffold",
        "current_version_target": "v0.3.0",
        "target_id": runtime_transition_checkpoint["target_id"],
        "scope_id": runtime_transition_checkpoint["scope_id"],
        "tool": runtime_transition_checkpoint["tool"],
        "adapter": runtime_transition_checkpoint["adapter"],
        "target_url": runtime_transition_checkpoint["target_url"],
        "target_mode": runtime_transition_checkpoint["target_mode"],
        "local_only": True,
        "preflight_check_implementation_scaffold_recorded": True,
        "concrete_checks_implemented": False,
        "all_required_checks_defined": True,
        "all_required_checks_have_implementation_scaffolds": True,
        "all_required_checks_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "ready_for_runtime_execution": False,
        "ready_for_customer_target": False,
        "ready_for_external_network": False,
        "check_implementations": check_implementations,
        "implementation_invariants": {
            "local_only": True,
            "concrete_checks_implemented": False,
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
        "implementation_blockers": [
            "concrete_check_functions_not_implemented",
            "preflight_evidence_records_not_implemented",
            "runtime_readiness_check_not_implemented",
            "scope_binding_check_not_implemented",
            "approval_binding_checks_not_implemented",
            "no_egress_verification_not_implemented",
            "timeout_verification_not_implemented",
            "kill_switch_verification_not_implemented",
            "evidence_emitter_verification_not_implemented",
            "sanitizer_boundary_verification_not_implemented",
            "preflight_not_satisfied",
            "execution_authorization_not_satisfied",
        ],
        "next_actions": [
            "Implement preflight check functions as pure validation logic before any runtime process launch exists.",
            "Define preflight evidence record schema for each check result.",
            "Add negative tests for missing, mismatched, stale, and unsafe preflight inputs.",
            "Bind approval records to execution authorization without authorizing execution.",
            "Define no-egress, timeout, kill-switch, evidence emitter, and sanitizer boundary verification records.",
        ],
        "implementation_notes": (
            "v0.3.0 records concrete implementation scaffolds for all required preflight checks. "
            "Each check receives input sources, evidence type, fail-closed behavior, and responsibility. "
            "The checks are not implemented or satisfied, and execution remains blocked."
        ),
    }

    validate_preflight_check_implementation_scaffold(implementation)
    return implementation


def validate_preflight_check_implementation_scaffold(implementation: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_IMPLEMENTATION_FIELDS if field not in implementation]
    if missing:
        raise PreflightCheckImplementationError(f"preflight check implementation scaffold missing fields: {missing}")

    if implementation.get("implementation_type") != "concrete_preflight_check_implementation_scaffold":
        raise PreflightCheckImplementationError("implementation_type must be concrete_preflight_check_implementation_scaffold")

    if implementation.get("implementation_status") != "implementation_scaffold_recorded_execution_blocked":
        raise PreflightCheckImplementationError("implementation_status must be implementation_scaffold_recorded_execution_blocked")

    if implementation.get("current_version_target") != "v0.3.0":
        raise PreflightCheckImplementationError("current_version_target must be v0.3.0")

    if implementation.get("local_only") is not True:
        raise PreflightCheckImplementationError("local_only must be true")

    required_true = [
        "preflight_check_implementation_scaffold_recorded",
        "all_required_checks_defined",
        "all_required_checks_have_implementation_scaffolds",
    ]
    for field in required_true:
        if implementation.get(field) is not True:
            raise PreflightCheckImplementationError(f"{field} must be true")

    required_false = [
        "concrete_checks_implemented",
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
        if implementation.get(field) is not False:
            raise PreflightCheckImplementationError(f"{field} must be false")

    check_implementations = implementation.get("check_implementations", [])
    if not isinstance(check_implementations, list):
        raise PreflightCheckImplementationError("check_implementations must be a list")

    check_names = {item.get("check_name") for item in check_implementations}
    missing_checks = set(PREFLIGHT_CHECKS) - check_names
    if missing_checks:
        raise PreflightCheckImplementationError(f"check_implementations missing checks: {sorted(missing_checks)}")

    for item in check_implementations:
        if item.get("implementation_status") != "implementation_scaffold_recorded_not_implemented":
            raise PreflightCheckImplementationError("every check implementation must remain not implemented")
        if item.get("implemented") is not False:
            raise PreflightCheckImplementationError("every check implemented flag must remain false")
        if item.get("satisfied") is not False:
            raise PreflightCheckImplementationError("every check satisfied flag must remain false")
        if item.get("required") is not True:
            raise PreflightCheckImplementationError("every check must be required")
        if item.get("evidence_record_required") is not True:
            raise PreflightCheckImplementationError("every check must require an evidence record")
        if item.get("evidence_record_generated") is not False:
            raise PreflightCheckImplementationError("evidence_record_generated must remain false")
        if item.get("fail_closed_on_missing_input") is not True:
            raise PreflightCheckImplementationError("fail_closed_on_missing_input must be true")
        if item.get("fail_closed_on_mismatch") is not True:
            raise PreflightCheckImplementationError("fail_closed_on_mismatch must be true")
        if item.get("fail_closed_on_stale_state") is not True:
            raise PreflightCheckImplementationError("fail_closed_on_stale_state must be true")
        if not item.get("input_sources"):
            raise PreflightCheckImplementationError("each check must define input_sources")
        if not item.get("evidence_type"):
            raise PreflightCheckImplementationError("each check must define evidence_type")

    invariants = implementation.get("implementation_invariants", {})
    if invariants.get("local_only") is not True:
        raise PreflightCheckImplementationError("implementation invariant local_only must be true")

    invariant_false = [
        "concrete_checks_implemented",
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
            raise PreflightCheckImplementationError(f"implementation invariant must be false: {field}")

    required_blockers = {
        "concrete_check_functions_not_implemented",
        "preflight_evidence_records_not_implemented",
        "runtime_readiness_check_not_implemented",
        "scope_binding_check_not_implemented",
        "approval_binding_checks_not_implemented",
        "no_egress_verification_not_implemented",
        "timeout_verification_not_implemented",
        "kill_switch_verification_not_implemented",
        "evidence_emitter_verification_not_implemented",
        "sanitizer_boundary_verification_not_implemented",
        "preflight_not_satisfied",
        "execution_authorization_not_satisfied",
    }
    missing_blockers = required_blockers - set(implementation.get("implementation_blockers", []))
    if missing_blockers:
        raise PreflightCheckImplementationError(f"implementation scaffold missing blockers: {sorted(missing_blockers)}")


def evaluate_preflight_check_implementation_gate(
    implementation: dict[str, Any],
    *,
    implementation_review_decision: str = "implementation_scaffold_recorded",
) -> dict[str, Any]:
    validate_preflight_check_implementation_scaffold(implementation)

    if implementation_review_decision not in VALID_IMPLEMENTATION_REVIEW_DECISIONS:
        raise PreflightCheckImplementationError(
            f"unsupported implementation_review_decision: {implementation_review_decision}"
        )

    if implementation_review_decision == "implementation_scaffold_recorded":
        gate_status = "implementation_scaffold_recorded_execution_blocked"
        blockers = list(implementation["implementation_blockers"])
    elif implementation_review_decision == "needs_revision":
        gate_status = "needs_revision"
        blockers = list(implementation["implementation_blockers"])
    else:
        gate_status = "rejected"
        blockers = ["preflight_check_implementation_scaffold_rejected"]

    invariants = implementation["implementation_invariants"]

    gate = {
        "preflight_check_implementation_gate_type": "concrete_preflight_check_implementation_scaffold_gate",
        "preflight_check_implementation_gate_status": gate_status,
        "preflight_check_implementation_id": implementation["preflight_check_implementation_id"],
        "checkpoint_id": implementation["checkpoint_id"],
        "target_id": implementation["target_id"],
        "scope_id": implementation["scope_id"],
        "tool": implementation["tool"],
        "adapter": implementation["adapter"],
        "target_url": implementation["target_url"],
        "target_mode": implementation["target_mode"],
        "local_only": True,
        "implementation_review_decision": implementation_review_decision,
        "implementation_review_satisfied": False,
        "concrete_checks_implemented": False,
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
                "blocker": "concrete_check_functions_not_implemented",
                "next_action": "Implement pure preflight validation functions without enabling process launch.",
            },
            {
                "blocker": "preflight_evidence_records_not_implemented",
                "next_action": "Define evidence records for each preflight check result.",
            },
            {
                "blocker": "approval_binding_checks_not_implemented",
                "next_action": "Implement approval binding checks while keeping execution_authorized=false.",
            },
            {
                "blocker": "no_egress_verification_not_implemented",
                "next_action": "Implement no-egress verification evidence checks before any network activity exists.",
            },
            {
                "blocker": "sanitizer_boundary_verification_not_implemented",
                "next_action": "Implement sanitizer boundary verification before any raw artifact capture exists.",
            },
        ],
    }

    validate_preflight_check_implementation_gate_result(gate)
    return gate


def validate_preflight_check_implementation_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise PreflightCheckImplementationError(f"preflight check implementation gate missing fields: {missing}")

    if gate.get("preflight_check_implementation_gate_type") != "concrete_preflight_check_implementation_scaffold_gate":
        raise PreflightCheckImplementationError("preflight_check_implementation_gate_type mismatch")

    if gate.get("implementation_review_decision") not in VALID_IMPLEMENTATION_REVIEW_DECISIONS:
        raise PreflightCheckImplementationError("unsupported implementation_review_decision")

    if gate.get("local_only") is not True:
        raise PreflightCheckImplementationError("local_only must be true")

    required_false = [
        "implementation_review_satisfied",
        "concrete_checks_implemented",
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
            raise PreflightCheckImplementationError(f"{field} must be false")

    if not gate.get("blockers"):
        raise PreflightCheckImplementationError("preflight check implementation gate must include blockers")
