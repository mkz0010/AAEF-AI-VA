from __future__ import annotations

from typing import Any

from bounded_execution_transition import (
    validate_bounded_execution_transition_candidate,
    validate_bounded_execution_transition_gate_result,
)


class LocalExecutionPlanError(ValueError):
    pass


ALLOWED_PLAN_OPERATIONS = {
    "runtime_detection",
    "health_check_plan_only",
}


PROHIBITED_RUNTIME_OPERATIONS = {
    "zap_start",
    "zap_stop",
    "zap_api_call",
    "spider",
    "ajax_spider",
    "active_scan",
    "passive_scan_runtime_collection",
    "authenticated_crawl",
    "credential_injection",
    "raw_artifact_capture",
    "external_network_access",
    "customer_target_access",
}


VALID_PLAN_REVIEW_DECISIONS = {
    "plan_recorded",
    "needs_revision",
    "rejected",
}


REQUIRED_PLAN_FIELDS = [
    "local_execution_plan_id",
    "plan_type",
    "plan_status",
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
    "allowed_plan_operations",
    "prohibited_runtime_operations",
    "execution_plan_review_required",
    "human_approval_required",
    "no_egress_required",
    "timeout_required",
    "kill_switch_required",
    "evidence_required",
    "sanitizer_required_before_ai_visible",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "plan_requirements",
    "plan_blockers",
    "plan_notes",
]


REQUIRED_GATE_FIELDS = [
    "local_execution_plan_review_gate_type",
    "local_execution_plan_review_gate_status",
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
    "allowed_plan_operations",
    "prohibited_runtime_operations",
    "plan_review_decision",
    "plan_review_satisfied",
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
    "blockers",
    "next_actions",
]


def build_local_only_execution_plan(
    transition_candidate: dict[str, Any],
    transition_gate: dict[str, Any],
    *,
    allowed_plan_operations: list[str] | None = None,
) -> dict[str, Any]:
    validate_bounded_execution_transition_candidate(transition_candidate)
    validate_bounded_execution_transition_gate_result(transition_gate)

    if transition_candidate["bounded_execution_transition_candidate_id"] != transition_gate["bounded_execution_transition_candidate_id"]:
        raise LocalExecutionPlanError("transition candidate/gate ID mismatch")

    if transition_candidate["runtime_destination_binding_id"] != transition_gate["runtime_destination_binding_id"]:
        raise LocalExecutionPlanError("transition candidate/gate runtime_destination_binding_id mismatch")

    if transition_candidate["target_id"] != transition_gate["target_id"]:
        raise LocalExecutionPlanError("transition candidate/gate target_id mismatch")

    if transition_candidate["scope_id"] != transition_gate["scope_id"]:
        raise LocalExecutionPlanError("transition candidate/gate scope_id mismatch")

    operations = list(allowed_plan_operations or ["runtime_detection", "health_check_plan_only"])

    plan = {
        "local_execution_plan_id": (
            f"local-execution-plan-{transition_candidate['bounded_execution_transition_candidate_id']}"
        ),
        "plan_type": "local_only_execution_plan_review",
        "plan_status": "plan_recorded_execution_blocked",
        "bounded_execution_transition_candidate_id": transition_candidate["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": transition_candidate["runtime_destination_binding_id"],
        "scope_registry_destination_id": transition_candidate["scope_registry_destination_id"],
        "target_id": transition_candidate["target_id"],
        "scope_id": transition_candidate["scope_id"],
        "tool": transition_candidate["tool"],
        "adapter": transition_candidate["adapter"],
        "target_url": transition_candidate["target_url"],
        "target_mode": transition_candidate["target_mode"],
        "local_only": True,
        "allowed_plan_operations": operations,
        "prohibited_runtime_operations": sorted(PROHIBITED_RUNTIME_OPERATIONS),
        "execution_plan_review_required": True,
        "human_approval_required": True,
        "no_egress_required": True,
        "timeout_required": True,
        "kill_switch_required": True,
        "evidence_required": True,
        "sanitizer_required_before_ai_visible": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "plan_requirements": [
            "runtime detection may be described but not executed by this plan",
            "health check may be described as plan-only and must not call ZAP or target services",
            "all future execution operations must remain explicitly allowlisted",
            "active scan, spider, ajax spider, authenticated crawl, and API calls remain prohibited",
            "no-egress controls must be defined before network activity can be considered",
            "timeout and kill-switch behavior must be defined before process launch can be considered",
            "human approval must be recorded before any future execution transition",
            "raw artifact capture and sanitizer binding must be defined before runtime output can be handled",
            "evidence generation must remain mandatory",
        ],
        "plan_blockers": [
            "execution_review_not_satisfied",
            "runtime_process_launch_not_allowed",
            "network_activity_not_allowed",
            "zap_api_call_not_allowed",
            "scan_operations_not_allowed",
            "raw_artifact_capture_boundary_not_defined",
            "no_egress_controls_not_validated",
            "timeout_not_enforced",
            "kill_switch_not_enforced",
            "human_approval_for_execution_transition_not_recorded",
        ],
        "plan_notes": (
            "This local-only execution plan is a review artifact. It may record plan-level operations "
            "such as runtime_detection and health_check_plan_only, but it does not authorize process launch, "
            "network traffic, ZAP API calls, scans, credential injection, or raw artifact capture."
        ),
    }

    validate_local_only_execution_plan(plan)
    return plan


def validate_local_only_execution_plan(plan: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_PLAN_FIELDS if field not in plan]
    if missing:
        raise LocalExecutionPlanError(f"local-only execution plan missing fields: {missing}")

    if plan.get("plan_type") != "local_only_execution_plan_review":
        raise LocalExecutionPlanError("plan_type must be local_only_execution_plan_review")

    if plan.get("plan_status") != "plan_recorded_execution_blocked":
        raise LocalExecutionPlanError("plan_status must be plan_recorded_execution_blocked")

    if plan.get("local_only") is not True:
        raise LocalExecutionPlanError("local_only must be true")

    operations = set(plan.get("allowed_plan_operations", []))
    unknown_operations = operations - ALLOWED_PLAN_OPERATIONS
    if unknown_operations:
        raise LocalExecutionPlanError(f"unsupported allowed_plan_operations: {sorted(unknown_operations)}")

    if not operations:
        raise LocalExecutionPlanError("allowed_plan_operations must not be empty")

    prohibited = set(plan.get("prohibited_runtime_operations", []))
    missing_prohibited = PROHIBITED_RUNTIME_OPERATIONS - prohibited
    if missing_prohibited:
        raise LocalExecutionPlanError(f"prohibited_runtime_operations missing: {sorted(missing_prohibited)}")

    if operations & prohibited:
        raise LocalExecutionPlanError("allowed_plan_operations must not overlap prohibited_runtime_operations")

    for field in [
        "execution_plan_review_required",
        "human_approval_required",
        "no_egress_required",
        "timeout_required",
        "kill_switch_required",
        "evidence_required",
        "sanitizer_required_before_ai_visible",
    ]:
        if plan.get(field) is not True:
            raise LocalExecutionPlanError(f"{field} must be true")

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
        if plan.get(field) is not False:
            raise LocalExecutionPlanError(f"{field} must be false")

    required_blockers = {
        "execution_review_not_satisfied",
        "runtime_process_launch_not_allowed",
        "network_activity_not_allowed",
        "zap_api_call_not_allowed",
        "scan_operations_not_allowed",
        "raw_artifact_capture_boundary_not_defined",
        "no_egress_controls_not_validated",
        "timeout_not_enforced",
        "kill_switch_not_enforced",
        "human_approval_for_execution_transition_not_recorded",
    }
    missing_blockers = required_blockers - set(plan.get("plan_blockers", []))
    if missing_blockers:
        raise LocalExecutionPlanError(f"local-only execution plan missing blockers: {sorted(missing_blockers)}")


def evaluate_local_execution_plan_review_gate(
    plan: dict[str, Any],
    *,
    plan_review_decision: str = "plan_recorded",
) -> dict[str, Any]:
    validate_local_only_execution_plan(plan)

    if plan_review_decision not in VALID_PLAN_REVIEW_DECISIONS:
        raise LocalExecutionPlanError(f"unsupported plan_review_decision: {plan_review_decision}")

    if plan_review_decision == "plan_recorded":
        gate_status = "plan_recorded_execution_blocked"
        decision_recommendation = "define_no_egress_timeout_kill_switch_and_health_check_design"
        blockers = list(plan["plan_blockers"])
    elif plan_review_decision == "needs_revision":
        gate_status = "needs_revision"
        decision_recommendation = "revise_local_only_execution_plan"
        blockers = list(plan["plan_blockers"])
    else:
        gate_status = "rejected"
        decision_recommendation = "do_not_continue_to_runtime_execution_design"
        blockers = ["local_execution_plan_rejected"]

    gate = {
        "local_execution_plan_review_gate_type": "local_only_execution_plan_review_gate",
        "local_execution_plan_review_gate_status": gate_status,
        "local_execution_plan_id": plan["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": plan["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": plan["runtime_destination_binding_id"],
        "scope_registry_destination_id": plan["scope_registry_destination_id"],
        "target_id": plan["target_id"],
        "scope_id": plan["scope_id"],
        "tool": plan["tool"],
        "adapter": plan["adapter"],
        "target_url": plan["target_url"],
        "target_mode": plan["target_mode"],
        "local_only": True,
        "allowed_plan_operations": list(plan["allowed_plan_operations"]),
        "prohibited_runtime_operations": list(plan["prohibited_runtime_operations"]),
        "plan_review_decision": plan_review_decision,
        "plan_review_satisfied": False,
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
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "runtime_process_launch_not_allowed",
                "next_action": "Do not start ZAP or any external process from this plan review gate.",
            },
            {
                "blocker": "network_activity_not_allowed",
                "next_action": "Define no-egress and health-check design before any network activity is considered.",
            },
            {
                "blocker": "zap_api_call_not_allowed",
                "next_action": "Do not call the ZAP API until a separate runtime control gate exists.",
            },
            {
                "blocker": "scan_operations_not_allowed",
                "next_action": "Keep spider, ajax spider, authenticated crawl, passive runtime collection, and active scan prohibited.",
            },
            {
                "blocker": "raw_artifact_capture_boundary_not_defined",
                "next_action": "Define raw artifact storage, sanitizer binding, and AI-visible boundaries before output capture.",
            },
        ],
    }

    validate_local_execution_plan_review_gate_result(gate)
    return gate


def validate_local_execution_plan_review_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise LocalExecutionPlanError(f"local execution plan review gate missing fields: {missing}")

    if gate.get("local_execution_plan_review_gate_type") != "local_only_execution_plan_review_gate":
        raise LocalExecutionPlanError("local_execution_plan_review_gate_type mismatch")

    if gate.get("plan_review_decision") not in VALID_PLAN_REVIEW_DECISIONS:
        raise LocalExecutionPlanError("unsupported plan_review_decision")

    if gate.get("plan_review_satisfied") is not False:
        raise LocalExecutionPlanError("plan_review_satisfied must remain false in current MVP")

    if gate.get("local_only") is not True:
        raise LocalExecutionPlanError("local_only must be true")

    operations = set(gate.get("allowed_plan_operations", []))
    unknown_operations = operations - ALLOWED_PLAN_OPERATIONS
    if unknown_operations:
        raise LocalExecutionPlanError(f"unsupported allowed_plan_operations in gate: {sorted(unknown_operations)}")

    prohibited = set(gate.get("prohibited_runtime_operations", []))
    if operations & prohibited:
        raise LocalExecutionPlanError("allowed operations must not overlap prohibited operations in gate")

    for field in [
        "execution_plan_review_required",
        "human_approval_required",
        "no_egress_required",
        "timeout_required",
        "kill_switch_required",
        "evidence_required",
    ]:
        if gate.get(field) is not True:
            raise LocalExecutionPlanError(f"{field} must be true")

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
            raise LocalExecutionPlanError(f"{field} must be false")

    if not gate.get("blockers"):
        raise LocalExecutionPlanError("local execution plan review gate must include blockers")
