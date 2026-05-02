from __future__ import annotations

from typing import Any

from runtime_destination_binding import (
    validate_runtime_destination_binding_gate_result,
    validate_scope_registry_runtime_destination_binding,
)


class BoundedExecutionTransitionError(ValueError):
    pass


VALID_TRANSITION_REVIEW_DECISIONS = {
    "candidate_recorded",
    "needs_design",
    "rejected",
}


REQUIRED_CANDIDATE_FIELDS = [
    "bounded_execution_transition_candidate_id",
    "candidate_type",
    "candidate_status",
    "runtime_destination_binding_id",
    "scope_registry_destination_id",
    "runtime_profile_id",
    "lab_profile_id",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "operation_family",
    "proposed_execution_mode",
    "local_only",
    "bounded_execution_transition_candidate_allowed",
    "execution_plan_review_required",
    "human_approval_required",
    "runtime_readiness_required",
    "scope_registry_binding_required",
    "local_target_lab_required",
    "sanitizer_required_before_ai_visible",
    "no_egress_required",
    "timeout_required",
    "kill_switch_required",
    "evidence_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "candidate_requirements",
    "candidate_blockers",
    "candidate_notes",
]


REQUIRED_GATE_FIELDS = [
    "bounded_execution_transition_gate_type",
    "bounded_execution_transition_gate_status",
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
    "execution_plan_review_required",
    "human_approval_required",
    "no_egress_required",
    "timeout_required",
    "kill_switch_required",
    "evidence_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "transition_review_decision",
    "transition_review_satisfied",
    "blockers",
    "next_actions",
]


def build_bounded_execution_transition_candidate(
    binding: dict[str, Any],
    binding_gate: dict[str, Any],
    *,
    proposed_execution_mode: str = "local_only_zap_runtime_dry_transition",
) -> dict[str, Any]:
    validate_scope_registry_runtime_destination_binding(binding)
    validate_runtime_destination_binding_gate_result(binding_gate)

    if binding["runtime_destination_binding_id"] != binding_gate["runtime_destination_binding_id"]:
        raise BoundedExecutionTransitionError("binding/gate runtime_destination_binding_id mismatch")

    if binding["scope_registry_destination_id"] != binding_gate["scope_registry_destination_id"]:
        raise BoundedExecutionTransitionError("binding/gate scope_registry_destination_id mismatch")

    if binding["target_id"] != binding_gate["target_id"]:
        raise BoundedExecutionTransitionError("binding/gate target_id mismatch")

    if binding["scope_id"] != binding_gate["scope_id"]:
        raise BoundedExecutionTransitionError("binding/gate scope_id mismatch")

    candidate = {
        "bounded_execution_transition_candidate_id": (
            f"bounded-execution-transition-candidate-{binding['runtime_destination_binding_id']}"
        ),
        "candidate_type": "bounded_execution_transition_candidate",
        "candidate_status": "execution_plan_review_required",
        "runtime_destination_binding_id": binding["runtime_destination_binding_id"],
        "scope_registry_destination_id": binding["scope_registry_destination_id"],
        "runtime_profile_id": binding["runtime_profile_id"],
        "lab_profile_id": binding["lab_profile_id"],
        "target_id": binding["target_id"],
        "scope_id": binding["scope_id"],
        "tool": binding["tool"],
        "adapter": binding["adapter"],
        "target_url": binding["target_url"],
        "target_mode": binding["target_mode"],
        "operation_family": binding["operation_family"],
        "proposed_execution_mode": proposed_execution_mode,
        "local_only": True,
        "bounded_execution_transition_candidate_allowed": True,
        "execution_plan_review_required": True,
        "human_approval_required": True,
        "runtime_readiness_required": True,
        "scope_registry_binding_required": True,
        "local_target_lab_required": True,
        "sanitizer_required_before_ai_visible": True,
        "no_egress_required": True,
        "timeout_required": True,
        "kill_switch_required": True,
        "evidence_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "candidate_requirements": [
            "runtime readiness must be present and current",
            "target must be local, Docker-internal, and intentionally vulnerable",
            "scope registry runtime destination binding must match",
            "operation must be explicitly allowlisted in a future execution plan",
            "no-egress controls must be designed before execution",
            "timeout and kill-switch controls must be designed before execution",
            "human approval must be recorded before execution transition",
            "raw artifact capture boundary must be designed before execution",
            "sanitizer policy must be bound before any AI-visible output",
            "evidence generation must be required for any future transition",
        ],
        "candidate_blockers": [
            "execution_plan_not_defined",
            "no_egress_controls_not_defined",
            "timeout_not_defined",
            "kill_switch_not_defined",
            "raw_artifact_capture_boundary_not_defined",
            "operation_allowlist_not_defined",
            "human_approval_for_execution_transition_not_recorded",
        ],
        "candidate_notes": (
            "This candidate structures the conditions for a future bounded local execution transition. "
            "It does not permit execution, process launch, scanning, network activity, credential injection, "
            "or raw artifact capture."
        ),
    }

    validate_bounded_execution_transition_candidate(candidate)
    return candidate


def validate_bounded_execution_transition_candidate(candidate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_CANDIDATE_FIELDS if field not in candidate]
    if missing:
        raise BoundedExecutionTransitionError(f"bounded execution transition candidate missing fields: {missing}")

    if candidate.get("candidate_type") != "bounded_execution_transition_candidate":
        raise BoundedExecutionTransitionError("candidate_type must be bounded_execution_transition_candidate")

    if candidate.get("candidate_status") != "execution_plan_review_required":
        raise BoundedExecutionTransitionError("candidate_status must be execution_plan_review_required")

    if candidate.get("bounded_execution_transition_candidate_allowed") is not True:
        raise BoundedExecutionTransitionError("bounded_execution_transition_candidate_allowed must be true")

    if candidate.get("local_only") is not True:
        raise BoundedExecutionTransitionError("local_only must be true")

    for field in [
        "execution_plan_review_required",
        "human_approval_required",
        "runtime_readiness_required",
        "scope_registry_binding_required",
        "local_target_lab_required",
        "sanitizer_required_before_ai_visible",
        "no_egress_required",
        "timeout_required",
        "kill_switch_required",
        "evidence_required",
    ]:
        if candidate.get(field) is not True:
            raise BoundedExecutionTransitionError(f"{field} must be true")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "external_process_execution_allowed",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "customer_target",
        "external_network_target",
    ]:
        if candidate.get(field) is not False:
            raise BoundedExecutionTransitionError(f"{field} must be false")

    if candidate.get("tool") != "zap":
        raise BoundedExecutionTransitionError("current MVP transition candidate supports zap only")

    if candidate.get("adapter") != "zap":
        raise BoundedExecutionTransitionError("current MVP transition candidate supports zap adapter only")

    required_blockers = {
        "execution_plan_not_defined",
        "no_egress_controls_not_defined",
        "timeout_not_defined",
        "kill_switch_not_defined",
        "raw_artifact_capture_boundary_not_defined",
        "operation_allowlist_not_defined",
        "human_approval_for_execution_transition_not_recorded",
    }
    missing_blockers = required_blockers - set(candidate.get("candidate_blockers", []))
    if missing_blockers:
        raise BoundedExecutionTransitionError(f"transition candidate missing blockers: {sorted(missing_blockers)}")


def evaluate_bounded_execution_transition_gate(
    candidate: dict[str, Any],
    *,
    transition_review_decision: str = "candidate_recorded",
) -> dict[str, Any]:
    validate_bounded_execution_transition_candidate(candidate)

    if transition_review_decision not in VALID_TRANSITION_REVIEW_DECISIONS:
        raise BoundedExecutionTransitionError(f"unsupported transition_review_decision: {transition_review_decision}")

    if transition_review_decision == "candidate_recorded":
        gate_status = "candidate_recorded_execution_blocked"
        transition_review_satisfied = False
        decision_recommendation = "define_local_only_execution_plan_review"
        blockers = list(candidate["candidate_blockers"])
    elif transition_review_decision == "needs_design":
        gate_status = "needs_design"
        transition_review_satisfied = False
        decision_recommendation = "complete_missing_execution_transition_design"
        blockers = list(candidate["candidate_blockers"])
    else:
        gate_status = "rejected"
        transition_review_satisfied = False
        decision_recommendation = "do_not_continue_to_execution_plan"
        blockers = ["transition_candidate_rejected"]

    gate = {
        "bounded_execution_transition_gate_type": "bounded_execution_transition_candidate_gate",
        "bounded_execution_transition_gate_status": gate_status,
        "bounded_execution_transition_candidate_id": candidate["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": candidate["runtime_destination_binding_id"],
        "scope_registry_destination_id": candidate["scope_registry_destination_id"],
        "target_id": candidate["target_id"],
        "scope_id": candidate["scope_id"],
        "tool": candidate["tool"],
        "adapter": candidate["adapter"],
        "target_url": candidate["target_url"],
        "target_mode": candidate["target_mode"],
        "local_only": True,
        "execution_plan_review_required": True,
        "human_approval_required": True,
        "no_egress_required": True,
        "timeout_required": True,
        "kill_switch_required": True,
        "evidence_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "transition_review_decision": transition_review_decision,
        "transition_review_satisfied": transition_review_satisfied,
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "execution_plan_not_defined",
                "next_action": "Define a local-only execution plan review object before any process launch can be considered.",
            },
            {
                "blocker": "no_egress_controls_not_defined",
                "next_action": "Define no-egress requirements and validation before any localhost or Docker traffic.",
            },
            {
                "blocker": "timeout_not_defined",
                "next_action": "Define strict timeout behavior before any runtime process can be launched.",
            },
            {
                "blocker": "kill_switch_not_defined",
                "next_action": "Define kill-switch behavior before any runtime process can be launched.",
            },
            {
                "blocker": "raw_artifact_capture_boundary_not_defined",
                "next_action": "Define raw artifact capture, storage, sanitizer, and AI-visible boundaries.",
            },
        ],
    }

    validate_bounded_execution_transition_gate_result(gate)
    return gate


def validate_bounded_execution_transition_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise BoundedExecutionTransitionError(f"bounded execution transition gate missing fields: {missing}")

    if gate.get("bounded_execution_transition_gate_type") != "bounded_execution_transition_candidate_gate":
        raise BoundedExecutionTransitionError("bounded_execution_transition_gate_type mismatch")

    if gate.get("transition_review_satisfied") is not False:
        raise BoundedExecutionTransitionError("transition_review_satisfied must remain false in current MVP")

    if gate.get("local_only") is not True:
        raise BoundedExecutionTransitionError("local_only must be true")

    for field in [
        "execution_plan_review_required",
        "human_approval_required",
        "no_egress_required",
        "timeout_required",
        "kill_switch_required",
        "evidence_required",
    ]:
        if gate.get(field) is not True:
            raise BoundedExecutionTransitionError(f"{field} must be true")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "external_process_execution_allowed",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "customer_target",
        "external_network_target",
    ]:
        if gate.get(field) is not False:
            raise BoundedExecutionTransitionError(f"{field} must be false")

    if gate.get("transition_review_decision") not in VALID_TRANSITION_REVIEW_DECISIONS:
        raise BoundedExecutionTransitionError("unsupported transition_review_decision")

    if not gate.get("blockers"):
        raise BoundedExecutionTransitionError("transition gate must include blockers")
