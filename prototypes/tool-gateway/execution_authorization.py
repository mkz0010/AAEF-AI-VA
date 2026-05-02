from __future__ import annotations

from typing import Any

from runtime_enforcement_design import (
    validate_runtime_enforcement_design,
    validate_runtime_enforcement_design_gate_result,
)


class ExecutionAuthorizationError(ValueError):
    pass


VALID_AUTHORIZATION_REVIEW_DECISIONS = {
    "authorization_scaffold_recorded",
    "needs_revision",
    "rejected",
}


REQUIRED_AUTHORIZATION_FIELDS = [
    "execution_authorization_id",
    "authorization_type",
    "authorization_status",
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
    "authorization_scaffold_recorded",
    "execution_authorized",
    "execution_authorization_satisfied",
    "runtime_enforcement_implemented",
    "preflight_check_required",
    "preflight_check_satisfied",
    "human_approval_required",
    "human_approval_recorded",
    "operator_confirmation_required",
    "operator_confirmation_recorded",
    "scope_owner_approval_required",
    "scope_owner_approval_recorded",
    "no_egress_guard_required",
    "no_egress_guard_verified",
    "timeout_watcher_required",
    "timeout_watcher_verified",
    "kill_switch_controller_required",
    "kill_switch_controller_verified",
    "evidence_emitter_required",
    "evidence_emitter_verified",
    "sanitizer_boundary_required",
    "sanitizer_boundary_verified",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "authorization_requirements",
    "authorization_blockers",
    "authorization_notes",
]


REQUIRED_GATE_FIELDS = [
    "execution_authorization_gate_type",
    "execution_authorization_gate_status",
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
    "authorization_review_decision",
    "authorization_review_satisfied",
    "execution_authorized",
    "runtime_enforcement_implemented",
    "preflight_check_satisfied",
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


def build_execution_authorization_scaffold(
    runtime_enforcement_design: dict[str, Any],
    runtime_enforcement_design_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_runtime_enforcement_design(runtime_enforcement_design)
    validate_runtime_enforcement_design_gate_result(runtime_enforcement_design_gate)

    if runtime_enforcement_design["runtime_enforcement_design_id"] != runtime_enforcement_design_gate["runtime_enforcement_design_id"]:
        raise ExecutionAuthorizationError("runtime enforcement design/gate ID mismatch")

    if runtime_enforcement_design["runtime_safety_policy_id"] != runtime_enforcement_design_gate["runtime_safety_policy_id"]:
        raise ExecutionAuthorizationError("runtime enforcement design/gate runtime_safety_policy_id mismatch")

    if runtime_enforcement_design["target_id"] != runtime_enforcement_design_gate["target_id"]:
        raise ExecutionAuthorizationError("runtime enforcement design/gate target_id mismatch")

    if runtime_enforcement_design["scope_id"] != runtime_enforcement_design_gate["scope_id"]:
        raise ExecutionAuthorizationError("runtime enforcement design/gate scope_id mismatch")

    authorization = {
        "execution_authorization_id": f"execution-authorization-{runtime_enforcement_design['runtime_enforcement_design_id']}",
        "authorization_type": "execution_authorization_gate_scaffold",
        "authorization_status": "authorization_scaffold_recorded_execution_blocked",
        "runtime_enforcement_design_id": runtime_enforcement_design["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": runtime_enforcement_design["runtime_safety_policy_id"],
        "local_execution_plan_id": runtime_enforcement_design["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": runtime_enforcement_design["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": runtime_enforcement_design["runtime_destination_binding_id"],
        "scope_registry_destination_id": runtime_enforcement_design["scope_registry_destination_id"],
        "target_id": runtime_enforcement_design["target_id"],
        "scope_id": runtime_enforcement_design["scope_id"],
        "tool": runtime_enforcement_design["tool"],
        "adapter": runtime_enforcement_design["adapter"],
        "target_url": runtime_enforcement_design["target_url"],
        "target_mode": runtime_enforcement_design["target_mode"],
        "local_only": True,
        "authorization_scaffold_recorded": True,
        "execution_authorized": False,
        "execution_authorization_satisfied": False,
        "runtime_enforcement_implemented": False,
        "preflight_check_required": True,
        "preflight_check_satisfied": False,
        "human_approval_required": True,
        "human_approval_recorded": False,
        "operator_confirmation_required": True,
        "operator_confirmation_recorded": False,
        "scope_owner_approval_required": True,
        "scope_owner_approval_recorded": False,
        "no_egress_guard_required": True,
        "no_egress_guard_verified": False,
        "timeout_watcher_required": True,
        "timeout_watcher_verified": False,
        "kill_switch_controller_required": True,
        "kill_switch_controller_verified": False,
        "evidence_emitter_required": True,
        "evidence_emitter_verified": False,
        "sanitizer_boundary_required": True,
        "sanitizer_boundary_verified": False,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "authorization_requirements": [
            "runtime enforcement must be implemented and independently validated before execution authorization can be satisfied",
            "preflight check must be implemented and satisfied before execution authorization can be satisfied",
            "human approval for execution transition must be recorded before execution authorization can be satisfied",
            "operator confirmation must be recorded before execution authorization can be satisfied",
            "scope owner approval must be recorded before execution authorization can be satisfied",
            "no-egress guard must be verified before execution authorization can be satisfied",
            "timeout watcher must be verified before execution authorization can be satisfied",
            "kill-switch controller must be verified before execution authorization can be satisfied",
            "evidence emitter must be verified before execution authorization can be satisfied",
            "sanitizer boundary must be verified before execution authorization can be satisfied",
            "customer targets and external network targets remain forbidden",
        ],
        "authorization_blockers": [
            "runtime_enforcement_not_implemented",
            "preflight_check_not_satisfied",
            "human_approval_not_recorded",
            "operator_confirmation_not_recorded",
            "scope_owner_approval_not_recorded",
            "no_egress_guard_not_verified",
            "timeout_watcher_not_verified",
            "kill_switch_controller_not_verified",
            "evidence_emitter_not_verified",
            "sanitizer_boundary_not_verified",
            "execution_authorization_policy_not_satisfied",
        ],
        "authorization_notes": (
            "This execution authorization scaffold records who/what must approve and what controls must be "
            "verified before a future local-only execution could ever be authorized. It does not authorize "
            "execution, process launch, network activity, scans, credential injection, or raw artifact capture."
        ),
    }

    validate_execution_authorization_scaffold(authorization)
    return authorization


def validate_execution_authorization_scaffold(authorization: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_AUTHORIZATION_FIELDS if field not in authorization]
    if missing:
        raise ExecutionAuthorizationError(f"execution authorization scaffold missing fields: {missing}")

    if authorization.get("authorization_type") != "execution_authorization_gate_scaffold":
        raise ExecutionAuthorizationError("authorization_type must be execution_authorization_gate_scaffold")

    if authorization.get("authorization_status") != "authorization_scaffold_recorded_execution_blocked":
        raise ExecutionAuthorizationError("authorization_status must be authorization_scaffold_recorded_execution_blocked")

    if authorization.get("local_only") is not True:
        raise ExecutionAuthorizationError("local_only must be true")

    if authorization.get("authorization_scaffold_recorded") is not True:
        raise ExecutionAuthorizationError("authorization_scaffold_recorded must be true")

    if authorization.get("execution_authorized") is not False:
        raise ExecutionAuthorizationError("execution_authorized must be false in current MVP")

    if authorization.get("execution_authorization_satisfied") is not False:
        raise ExecutionAuthorizationError("execution_authorization_satisfied must be false in current MVP")

    if authorization.get("runtime_enforcement_implemented") is not False:
        raise ExecutionAuthorizationError("runtime_enforcement_implemented must be false in current MVP")

    required_true = [
        "preflight_check_required",
        "human_approval_required",
        "operator_confirmation_required",
        "scope_owner_approval_required",
        "no_egress_guard_required",
        "timeout_watcher_required",
        "kill_switch_controller_required",
        "evidence_emitter_required",
        "sanitizer_boundary_required",
    ]
    for field in required_true:
        if authorization.get(field) is not True:
            raise ExecutionAuthorizationError(f"{field} must be true")

    required_false = [
        "preflight_check_satisfied",
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
        if authorization.get(field) is not False:
            raise ExecutionAuthorizationError(f"{field} must be false")

    required_blockers = {
        "runtime_enforcement_not_implemented",
        "preflight_check_not_satisfied",
        "human_approval_not_recorded",
        "operator_confirmation_not_recorded",
        "scope_owner_approval_not_recorded",
        "no_egress_guard_not_verified",
        "timeout_watcher_not_verified",
        "kill_switch_controller_not_verified",
        "evidence_emitter_not_verified",
        "sanitizer_boundary_not_verified",
        "execution_authorization_policy_not_satisfied",
    }
    missing_blockers = required_blockers - set(authorization.get("authorization_blockers", []))
    if missing_blockers:
        raise ExecutionAuthorizationError(f"execution authorization scaffold missing blockers: {sorted(missing_blockers)}")


def evaluate_execution_authorization_gate(
    authorization: dict[str, Any],
    *,
    authorization_review_decision: str = "authorization_scaffold_recorded",
) -> dict[str, Any]:
    validate_execution_authorization_scaffold(authorization)

    if authorization_review_decision not in VALID_AUTHORIZATION_REVIEW_DECISIONS:
        raise ExecutionAuthorizationError(f"unsupported authorization_review_decision: {authorization_review_decision}")

    if authorization_review_decision == "authorization_scaffold_recorded":
        gate_status = "authorization_scaffold_recorded_execution_blocked"
        decision_recommendation = "define_preflight_and_execution_authorization_tests"
        blockers = list(authorization["authorization_blockers"])
    elif authorization_review_decision == "needs_revision":
        gate_status = "needs_revision"
        decision_recommendation = "revise_execution_authorization_scaffold"
        blockers = list(authorization["authorization_blockers"])
    else:
        gate_status = "rejected"
        decision_recommendation = "do_not_continue_to_execution_implementation"
        blockers = ["execution_authorization_scaffold_rejected"]

    gate = {
        "execution_authorization_gate_type": "execution_authorization_gate_scaffold",
        "execution_authorization_gate_status": gate_status,
        "execution_authorization_id": authorization["execution_authorization_id"],
        "runtime_enforcement_design_id": authorization["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": authorization["runtime_safety_policy_id"],
        "local_execution_plan_id": authorization["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": authorization["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": authorization["runtime_destination_binding_id"],
        "scope_registry_destination_id": authorization["scope_registry_destination_id"],
        "target_id": authorization["target_id"],
        "scope_id": authorization["scope_id"],
        "tool": authorization["tool"],
        "adapter": authorization["adapter"],
        "target_url": authorization["target_url"],
        "target_mode": authorization["target_mode"],
        "local_only": True,
        "authorization_review_decision": authorization_review_decision,
        "authorization_review_satisfied": False,
        "execution_authorized": False,
        "runtime_enforcement_implemented": False,
        "preflight_check_satisfied": False,
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
                "blocker": "runtime_enforcement_not_implemented",
                "next_action": "Implement and test runtime enforcement before any execution authorization can be considered.",
            },
            {
                "blocker": "preflight_check_not_satisfied",
                "next_action": "Define preflight validation that checks runtime, target, binding, policy, and approval state.",
            },
            {
                "blocker": "human_approval_not_recorded",
                "next_action": "Define human approval record requirements for future execution transition.",
            },
            {
                "blocker": "operator_confirmation_not_recorded",
                "next_action": "Define operator confirmation requirements for future local-only execution.",
            },
            {
                "blocker": "no_egress_guard_not_verified",
                "next_action": "Verify no-egress guard before any future network-capable process launch.",
            },
            {
                "blocker": "sanitizer_boundary_not_verified",
                "next_action": "Verify sanitizer boundary before any runtime output can become AI-visible.",
            },
        ],
    }

    validate_execution_authorization_gate_result(gate)
    return gate


def validate_execution_authorization_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise ExecutionAuthorizationError(f"execution authorization gate missing fields: {missing}")

    if gate.get("execution_authorization_gate_type") != "execution_authorization_gate_scaffold":
        raise ExecutionAuthorizationError("execution_authorization_gate_type mismatch")

    if gate.get("authorization_review_decision") not in VALID_AUTHORIZATION_REVIEW_DECISIONS:
        raise ExecutionAuthorizationError("unsupported authorization_review_decision")

    if gate.get("authorization_review_satisfied") is not False:
        raise ExecutionAuthorizationError("authorization_review_satisfied must remain false in current MVP")

    if gate.get("execution_authorized") is not False:
        raise ExecutionAuthorizationError("execution_authorized must remain false in current MVP")

    if gate.get("runtime_enforcement_implemented") is not False:
        raise ExecutionAuthorizationError("runtime_enforcement_implemented must remain false")

    if gate.get("local_only") is not True:
        raise ExecutionAuthorizationError("local_only must be true")

    required_false = [
        "preflight_check_satisfied",
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
            raise ExecutionAuthorizationError(f"{field} must be false")

    if not gate.get("blockers"):
        raise ExecutionAuthorizationError("execution authorization gate must include blockers")
