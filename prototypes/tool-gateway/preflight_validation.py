from __future__ import annotations

from typing import Any

from execution_authorization import (
    validate_execution_authorization_gate_result,
    validate_execution_authorization_scaffold,
)


class PreflightValidationError(ValueError):
    pass


VALID_PREFLIGHT_REVIEW_DECISIONS = {
    "preflight_scaffold_recorded",
    "needs_revision",
    "rejected",
}


PREFLIGHT_CHECKS = [
    "runtime_readiness_check",
    "local_target_lab_profile_check",
    "runtime_destination_binding_check",
    "bounded_execution_transition_check",
    "local_execution_plan_check",
    "runtime_safety_policy_check",
    "runtime_enforcement_design_check",
    "execution_authorization_check",
    "human_approval_check",
    "operator_confirmation_check",
    "scope_owner_approval_check",
    "no_egress_guard_check",
    "timeout_watcher_check",
    "kill_switch_controller_check",
    "evidence_emitter_check",
    "sanitizer_boundary_check",
]


REQUIRED_PREFLIGHT_FIELDS = [
    "preflight_validation_id",
    "preflight_type",
    "preflight_status",
    "execution_authorization_id",
    "runtime_enforcement_design_id",
    "runtime_safety_policy_id",
    "local_execution_plan_id",
    "bounded_execution_transition_candidate_id",
    "runtime_destination_binding_id",
    "scope_registry_destination_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "preflight_scaffold_recorded",
    "preflight_required",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "all_required_checks_defined",
    "all_required_checks_satisfied",
    "required_checks",
    "check_results",
    "human_approval_recorded",
    "operator_confirmation_recorded",
    "scope_owner_approval_recorded",
    "no_egress_guard_verified",
    "timeout_watcher_verified",
    "kill_switch_controller_verified",
    "evidence_emitter_verified",
    "sanitizer_boundary_verified",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "preflight_requirements",
    "preflight_blockers",
    "preflight_notes",
]


REQUIRED_GATE_FIELDS = [
    "preflight_validation_gate_type",
    "preflight_validation_gate_status",
    "preflight_validation_id",
    "execution_authorization_id",
    "runtime_enforcement_design_id",
    "runtime_safety_policy_id",
    "local_execution_plan_id",
    "bounded_execution_transition_candidate_id",
    "runtime_destination_binding_id",
    "scope_registry_destination_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "preflight_review_decision",
    "preflight_review_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "all_required_checks_satisfied",
    "human_approval_recorded",
    "operator_confirmation_recorded",
    "scope_owner_approval_recorded",
    "no_egress_guard_verified",
    "timeout_watcher_verified",
    "kill_switch_controller_verified",
    "evidence_emitter_verified",
    "sanitizer_boundary_verified",
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


def _build_check_results(execution_authorization: dict[str, Any]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    status_by_check = {
        "runtime_readiness_check": False,
        "local_target_lab_profile_check": False,
        "runtime_destination_binding_check": False,
        "bounded_execution_transition_check": False,
        "local_execution_plan_check": False,
        "runtime_safety_policy_check": False,
        "runtime_enforcement_design_check": execution_authorization["runtime_enforcement_implemented"],
        "execution_authorization_check": execution_authorization["execution_authorization_satisfied"],
        "human_approval_check": execution_authorization["human_approval_recorded"],
        "operator_confirmation_check": execution_authorization["operator_confirmation_recorded"],
        "scope_owner_approval_check": execution_authorization["scope_owner_approval_recorded"],
        "no_egress_guard_check": execution_authorization["no_egress_guard_verified"],
        "timeout_watcher_check": execution_authorization["timeout_watcher_verified"],
        "kill_switch_controller_check": execution_authorization["kill_switch_controller_verified"],
        "evidence_emitter_check": execution_authorization["evidence_emitter_verified"],
        "sanitizer_boundary_check": execution_authorization["sanitizer_boundary_verified"],
    }

    for check_name in PREFLIGHT_CHECKS:
        checks.append(
            {
                "check_name": check_name,
                "required": True,
                "satisfied": bool(status_by_check[check_name]),
                "status": "not_satisfied",
                "notes": "Preflight check is defined as required but is not satisfied in the current MVP.",
            }
        )

    return checks


def build_preflight_validation_scaffold(
    execution_authorization: dict[str, Any],
    execution_authorization_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_execution_authorization_scaffold(execution_authorization)
    validate_execution_authorization_gate_result(execution_authorization_gate)

    if execution_authorization["execution_authorization_id"] != execution_authorization_gate["execution_authorization_id"]:
        raise PreflightValidationError("execution authorization/gate ID mismatch")

    if execution_authorization["runtime_enforcement_design_id"] != execution_authorization_gate["runtime_enforcement_design_id"]:
        raise PreflightValidationError("execution authorization/gate runtime_enforcement_design_id mismatch")

    if execution_authorization["target_id"] != execution_authorization_gate["target_id"]:
        raise PreflightValidationError("execution authorization/gate target_id mismatch")

    if execution_authorization["scope_id"] != execution_authorization_gate["scope_id"]:
        raise PreflightValidationError("execution authorization/gate scope_id mismatch")

    check_results = _build_check_results(execution_authorization)

    preflight = {
        "preflight_validation_id": f"preflight-validation-{execution_authorization['execution_authorization_id']}",
        "preflight_type": "preflight_validation_scaffold",
        "preflight_status": "preflight_scaffold_recorded_execution_blocked",
        "execution_authorization_id": execution_authorization["execution_authorization_id"],
        "runtime_enforcement_design_id": execution_authorization["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": execution_authorization["runtime_safety_policy_id"],
        "local_execution_plan_id": execution_authorization["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": execution_authorization["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": execution_authorization["runtime_destination_binding_id"],
        "scope_registry_destination_id": execution_authorization["scope_registry_destination_id"],
        "target_id": execution_authorization["target_id"],
        "scope_id": execution_authorization["scope_id"],
        "tool": execution_authorization["tool"],
        "adapter": execution_authorization["adapter"],
        "target_url": execution_authorization["target_url"],
        "target_mode": execution_authorization["target_mode"],
        "local_only": True,
        "preflight_scaffold_recorded": True,
        "preflight_required": True,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "all_required_checks_defined": True,
        "all_required_checks_satisfied": False,
        "required_checks": list(PREFLIGHT_CHECKS),
        "check_results": check_results,
        "human_approval_recorded": False,
        "operator_confirmation_recorded": False,
        "scope_owner_approval_recorded": False,
        "no_egress_guard_verified": False,
        "timeout_watcher_verified": False,
        "kill_switch_controller_verified": False,
        "evidence_emitter_verified": False,
        "sanitizer_boundary_verified": False,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "preflight_requirements": [
            "runtime readiness must be checked immediately before any future execution authorization can be satisfied",
            "local target lab profile must be checked immediately before any future execution authorization can be satisfied",
            "runtime destination binding must be checked immediately before any future execution authorization can be satisfied",
            "bounded execution transition candidate must be checked immediately before any future execution authorization can be satisfied",
            "local-only execution plan must be checked immediately before any future execution authorization can be satisfied",
            "runtime safety policy must be checked immediately before any future execution authorization can be satisfied",
            "runtime enforcement design and implementation status must be checked immediately before any future execution authorization can be satisfied",
            "human approval, operator confirmation, and scope owner approval must be checked before execution authorization can be satisfied",
            "no-egress, timeout, kill-switch, evidence emitter, and sanitizer boundary verification must be checked before execution authorization can be satisfied",
        ],
        "preflight_blockers": [
            "runtime_readiness_not_checked",
            "local_target_lab_profile_not_checked",
            "runtime_destination_binding_not_checked",
            "bounded_execution_transition_not_checked",
            "local_execution_plan_not_checked",
            "runtime_safety_policy_not_checked",
            "runtime_enforcement_design_not_checked",
            "runtime_enforcement_not_implemented",
            "execution_authorization_not_satisfied",
            "human_approval_not_recorded",
            "operator_confirmation_not_recorded",
            "scope_owner_approval_not_recorded",
            "no_egress_guard_not_verified",
            "timeout_watcher_not_verified",
            "kill_switch_controller_not_verified",
            "evidence_emitter_not_verified",
            "sanitizer_boundary_not_verified",
        ],
        "preflight_notes": (
            "This preflight validation scaffold records the checks that must pass immediately before any future "
            "local-only execution could ever be authorized. It does not satisfy preflight, authorize execution, "
            "launch processes, perform network activity, scan targets, inject credentials, or capture raw artifacts."
        ),
    }

    validate_preflight_validation_scaffold(preflight)
    return preflight


def validate_preflight_validation_scaffold(preflight: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_PREFLIGHT_FIELDS if field not in preflight]
    if missing:
        raise PreflightValidationError(f"preflight validation scaffold missing fields: {missing}")

    if preflight.get("preflight_type") != "preflight_validation_scaffold":
        raise PreflightValidationError("preflight_type must be preflight_validation_scaffold")

    if preflight.get("preflight_status") != "preflight_scaffold_recorded_execution_blocked":
        raise PreflightValidationError("preflight_status must be preflight_scaffold_recorded_execution_blocked")

    if preflight.get("local_only") is not True:
        raise PreflightValidationError("local_only must be true")

    if preflight.get("preflight_scaffold_recorded") is not True:
        raise PreflightValidationError("preflight_scaffold_recorded must be true")

    if preflight.get("preflight_required") is not True:
        raise PreflightValidationError("preflight_required must be true")

    if preflight.get("all_required_checks_defined") is not True:
        raise PreflightValidationError("all_required_checks_defined must be true")

    required_false = [
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "all_required_checks_satisfied",
        "human_approval_recorded",
        "operator_confirmation_recorded",
        "scope_owner_approval_recorded",
        "no_egress_guard_verified",
        "timeout_watcher_verified",
        "kill_switch_controller_verified",
        "evidence_emitter_verified",
        "sanitizer_boundary_verified",
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
        if preflight.get(field) is not False:
            raise PreflightValidationError(f"{field} must be false")

    required_checks = set(preflight.get("required_checks", []))
    missing_checks = set(PREFLIGHT_CHECKS) - required_checks
    if missing_checks:
        raise PreflightValidationError(f"preflight required_checks missing: {sorted(missing_checks)}")

    check_results = preflight.get("check_results", [])
    if not isinstance(check_results, list):
        raise PreflightValidationError("check_results must be a list")

    result_names = {item.get("check_name") for item in check_results}
    missing_result_names = set(PREFLIGHT_CHECKS) - result_names
    if missing_result_names:
        raise PreflightValidationError(f"preflight check_results missing: {sorted(missing_result_names)}")

    for item in check_results:
        if item.get("required") is not True:
            raise PreflightValidationError("every preflight check must be required")
        if item.get("satisfied") is not False:
            raise PreflightValidationError("every preflight check must remain unsatisfied in current MVP")
        if item.get("status") != "not_satisfied":
            raise PreflightValidationError("every preflight check status must be not_satisfied in current MVP")

    required_blockers = {
        "runtime_readiness_not_checked",
        "local_target_lab_profile_not_checked",
        "runtime_destination_binding_not_checked",
        "bounded_execution_transition_not_checked",
        "local_execution_plan_not_checked",
        "runtime_safety_policy_not_checked",
        "runtime_enforcement_design_not_checked",
        "runtime_enforcement_not_implemented",
        "execution_authorization_not_satisfied",
        "human_approval_not_recorded",
        "operator_confirmation_not_recorded",
        "scope_owner_approval_not_recorded",
        "no_egress_guard_not_verified",
        "timeout_watcher_not_verified",
        "kill_switch_controller_not_verified",
        "evidence_emitter_not_verified",
        "sanitizer_boundary_not_verified",
    }
    missing_blockers = required_blockers - set(preflight.get("preflight_blockers", []))
    if missing_blockers:
        raise PreflightValidationError(f"preflight missing blockers: {sorted(missing_blockers)}")


def evaluate_preflight_validation_gate(
    preflight: dict[str, Any],
    *,
    preflight_review_decision: str = "preflight_scaffold_recorded",
) -> dict[str, Any]:
    validate_preflight_validation_scaffold(preflight)

    if preflight_review_decision not in VALID_PREFLIGHT_REVIEW_DECISIONS:
        raise PreflightValidationError(f"unsupported preflight_review_decision: {preflight_review_decision}")

    if preflight_review_decision == "preflight_scaffold_recorded":
        gate_status = "preflight_scaffold_recorded_execution_blocked"
        decision_recommendation = "define_preflight_check_implementations_and_evidence_requirements"
        blockers = list(preflight["preflight_blockers"])
    elif preflight_review_decision == "needs_revision":
        gate_status = "needs_revision"
        decision_recommendation = "revise_preflight_validation_scaffold"
        blockers = list(preflight["preflight_blockers"])
    else:
        gate_status = "rejected"
        decision_recommendation = "do_not_continue_to_preflight_implementation"
        blockers = ["preflight_validation_scaffold_rejected"]

    gate = {
        "preflight_validation_gate_type": "preflight_validation_scaffold_gate",
        "preflight_validation_gate_status": gate_status,
        "preflight_validation_id": preflight["preflight_validation_id"],
        "execution_authorization_id": preflight["execution_authorization_id"],
        "runtime_enforcement_design_id": preflight["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": preflight["runtime_safety_policy_id"],
        "local_execution_plan_id": preflight["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": preflight["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": preflight["runtime_destination_binding_id"],
        "scope_registry_destination_id": preflight["scope_registry_destination_id"],
        "target_id": preflight["target_id"],
        "scope_id": preflight["scope_id"],
        "tool": preflight["tool"],
        "adapter": preflight["adapter"],
        "target_url": preflight["target_url"],
        "target_mode": preflight["target_mode"],
        "local_only": True,
        "preflight_review_decision": preflight_review_decision,
        "preflight_review_satisfied": False,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "all_required_checks_satisfied": False,
        "human_approval_recorded": False,
        "operator_confirmation_recorded": False,
        "scope_owner_approval_recorded": False,
        "no_egress_guard_verified": False,
        "timeout_watcher_verified": False,
        "kill_switch_controller_verified": False,
        "evidence_emitter_verified": False,
        "sanitizer_boundary_verified": False,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "runtime_readiness_not_checked",
                "next_action": "Define a concrete preflight check for current runtime readiness state.",
            },
            {
                "blocker": "runtime_destination_binding_not_checked",
                "next_action": "Define a concrete preflight check that verifies runtime-target binding at the moment of execution request.",
            },
            {
                "blocker": "execution_authorization_not_satisfied",
                "next_action": "Keep execution authorization unsatisfied until all required approvals and verifications are present.",
            },
            {
                "blocker": "no_egress_guard_not_verified",
                "next_action": "Define concrete no-egress verification evidence before any future network-capable execution.",
            },
            {
                "blocker": "sanitizer_boundary_not_verified",
                "next_action": "Define concrete sanitizer boundary verification before any runtime output can be AI-visible.",
            },
        ],
    }

    validate_preflight_validation_gate_result(gate)
    return gate


def validate_preflight_validation_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise PreflightValidationError(f"preflight validation gate missing fields: {missing}")

    if gate.get("preflight_validation_gate_type") != "preflight_validation_scaffold_gate":
        raise PreflightValidationError("preflight_validation_gate_type mismatch")

    if gate.get("preflight_review_decision") not in VALID_PREFLIGHT_REVIEW_DECISIONS:
        raise PreflightValidationError("unsupported preflight_review_decision")

    if gate.get("local_only") is not True:
        raise PreflightValidationError("local_only must be true")

    required_false = [
        "preflight_review_satisfied",
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "all_required_checks_satisfied",
        "human_approval_recorded",
        "operator_confirmation_recorded",
        "scope_owner_approval_recorded",
        "no_egress_guard_verified",
        "timeout_watcher_verified",
        "kill_switch_controller_verified",
        "evidence_emitter_verified",
        "sanitizer_boundary_verified",
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
            raise PreflightValidationError(f"{field} must be false")

    if not gate.get("blockers"):
        raise PreflightValidationError("preflight validation gate must include blockers")
