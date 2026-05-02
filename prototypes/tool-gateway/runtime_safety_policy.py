from __future__ import annotations

from typing import Any

from local_execution_plan import (
    validate_local_execution_plan_review_gate_result,
    validate_local_only_execution_plan,
)


class RuntimeSafetyPolicyError(ValueError):
    pass


VALID_POLICY_REVIEW_DECISIONS = {
    "policy_recorded",
    "needs_revision",
    "rejected",
}


REQUIRED_POLICY_FIELDS = [
    "runtime_safety_policy_id",
    "policy_type",
    "policy_status",
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
    "no_egress_required",
    "no_egress_policy_defined",
    "allowed_destination_hosts",
    "denied_destination_categories",
    "timeout_required",
    "timeout_policy_defined",
    "max_runtime_seconds",
    "idle_timeout_seconds",
    "kill_switch_required",
    "kill_switch_policy_defined",
    "kill_switch_modes",
    "process_tree_termination_required",
    "evidence_required",
    "sanitizer_required_before_ai_visible",
    "human_approval_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "policy_requirements",
    "policy_blockers",
    "policy_notes",
]


REQUIRED_GATE_FIELDS = [
    "runtime_safety_policy_gate_type",
    "runtime_safety_policy_gate_status",
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
    "policy_review_decision",
    "policy_review_satisfied",
    "no_egress_required",
    "no_egress_policy_defined",
    "timeout_required",
    "timeout_policy_defined",
    "kill_switch_required",
    "kill_switch_policy_defined",
    "process_tree_termination_required",
    "evidence_required",
    "sanitizer_required_before_ai_visible",
    "human_approval_required",
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


DEFAULT_ALLOWED_DESTINATION_HOSTS = [
    "127.0.0.1",
    "localhost",
    "::1",
    "juice-shop",
    "webgoat",
    "dvwa",
    "target.local",
    "host.docker.internal",
]


DEFAULT_DENIED_DESTINATION_CATEGORIES = [
    "public_internet",
    "customer_network",
    "production_network",
    "metadata_service",
    "cloud_control_plane",
    "private_corporate_network",
    "unknown_external_host",
]


DEFAULT_KILL_SWITCH_MODES = [
    "operator_manual_stop",
    "timeout_forced_stop",
    "policy_violation_stop",
    "future_process_tree_termination",
]


def build_runtime_safety_policy(
    local_execution_plan: dict[str, Any],
    plan_review_gate: dict[str, Any],
    *,
    max_runtime_seconds: int = 60,
    idle_timeout_seconds: int = 15,
) -> dict[str, Any]:
    validate_local_only_execution_plan(local_execution_plan)
    validate_local_execution_plan_review_gate_result(plan_review_gate)

    if local_execution_plan["local_execution_plan_id"] != plan_review_gate["local_execution_plan_id"]:
        raise RuntimeSafetyPolicyError("local execution plan/gate ID mismatch")

    if local_execution_plan["bounded_execution_transition_candidate_id"] != plan_review_gate["bounded_execution_transition_candidate_id"]:
        raise RuntimeSafetyPolicyError("local execution plan/gate transition candidate mismatch")

    if local_execution_plan["target_id"] != plan_review_gate["target_id"]:
        raise RuntimeSafetyPolicyError("local execution plan/gate target_id mismatch")

    if local_execution_plan["scope_id"] != plan_review_gate["scope_id"]:
        raise RuntimeSafetyPolicyError("local execution plan/gate scope_id mismatch")

    policy = {
        "runtime_safety_policy_id": f"runtime-safety-policy-{local_execution_plan['local_execution_plan_id']}",
        "policy_type": "no_egress_timeout_kill_switch_policy_scaffold",
        "policy_status": "policy_recorded_execution_blocked",
        "local_execution_plan_id": local_execution_plan["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": local_execution_plan["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": local_execution_plan["runtime_destination_binding_id"],
        "scope_registry_destination_id": local_execution_plan["scope_registry_destination_id"],
        "target_id": local_execution_plan["target_id"],
        "scope_id": local_execution_plan["scope_id"],
        "tool": local_execution_plan["tool"],
        "adapter": local_execution_plan["adapter"],
        "target_url": local_execution_plan["target_url"],
        "target_mode": local_execution_plan["target_mode"],
        "local_only": True,
        "no_egress_required": True,
        "no_egress_policy_defined": True,
        "allowed_destination_hosts": list(DEFAULT_ALLOWED_DESTINATION_HOSTS),
        "denied_destination_categories": list(DEFAULT_DENIED_DESTINATION_CATEGORIES),
        "timeout_required": True,
        "timeout_policy_defined": True,
        "max_runtime_seconds": max_runtime_seconds,
        "idle_timeout_seconds": idle_timeout_seconds,
        "kill_switch_required": True,
        "kill_switch_policy_defined": True,
        "kill_switch_modes": list(DEFAULT_KILL_SWITCH_MODES),
        "process_tree_termination_required": True,
        "evidence_required": True,
        "sanitizer_required_before_ai_visible": True,
        "human_approval_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "policy_requirements": [
            "All runtime traffic must remain local-only in any future execution transition.",
            "No public internet, customer network, production network, cloud metadata, or unknown external destination may be allowed.",
            "A maximum runtime timeout must be enforced before any future process launch.",
            "An idle timeout must be enforced before any future process launch.",
            "A manual operator stop path must exist before any future process launch.",
            "Policy violation must stop the future runtime immediately.",
            "Future process tree termination must be required before any external process launch.",
            "Evidence must be generated for any future policy evaluation.",
            "Raw output must remain non-AI-visible until sanitizer policy succeeds.",
        ],
        "policy_blockers": [
            "runtime_execution_still_disabled",
            "external_process_execution_still_disabled",
            "network_activity_still_disabled",
            "no_egress_not_runtime_enforced",
            "timeout_not_runtime_enforced",
            "kill_switch_not_runtime_enforced",
            "process_tree_termination_not_implemented",
            "raw_artifact_capture_boundary_not_implemented",
            "human_approval_for_execution_transition_not_recorded",
        ],
        "policy_notes": (
            "This policy scaffold defines no-egress, timeout, and kill-switch requirements for future local-only "
            "runtime execution. It does not execute, start ZAP, call ZAP APIs, scan targets, perform network "
            "activity, inject credentials, or capture raw artifacts."
        ),
    }

    validate_runtime_safety_policy(policy)
    return policy


def validate_runtime_safety_policy(policy: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_POLICY_FIELDS if field not in policy]
    if missing:
        raise RuntimeSafetyPolicyError(f"runtime safety policy missing fields: {missing}")

    if policy.get("policy_type") != "no_egress_timeout_kill_switch_policy_scaffold":
        raise RuntimeSafetyPolicyError("policy_type must be no_egress_timeout_kill_switch_policy_scaffold")

    if policy.get("policy_status") != "policy_recorded_execution_blocked":
        raise RuntimeSafetyPolicyError("policy_status must be policy_recorded_execution_blocked")

    if policy.get("local_only") is not True:
        raise RuntimeSafetyPolicyError("local_only must be true")

    for field in [
        "no_egress_required",
        "no_egress_policy_defined",
        "timeout_required",
        "timeout_policy_defined",
        "kill_switch_required",
        "kill_switch_policy_defined",
        "process_tree_termination_required",
        "evidence_required",
        "sanitizer_required_before_ai_visible",
        "human_approval_required",
    ]:
        if policy.get(field) is not True:
            raise RuntimeSafetyPolicyError(f"{field} must be true")

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
        if policy.get(field) is not False:
            raise RuntimeSafetyPolicyError(f"{field} must be false")

    if not isinstance(policy.get("max_runtime_seconds"), int) or policy["max_runtime_seconds"] <= 0:
        raise RuntimeSafetyPolicyError("max_runtime_seconds must be a positive integer")

    if not isinstance(policy.get("idle_timeout_seconds"), int) or policy["idle_timeout_seconds"] <= 0:
        raise RuntimeSafetyPolicyError("idle_timeout_seconds must be a positive integer")

    if policy["idle_timeout_seconds"] > policy["max_runtime_seconds"]:
        raise RuntimeSafetyPolicyError("idle_timeout_seconds must be less than or equal to max_runtime_seconds")

    allowed_hosts = set(policy.get("allowed_destination_hosts", []))
    if not {"127.0.0.1", "localhost"}.issubset(allowed_hosts):
        raise RuntimeSafetyPolicyError("allowed_destination_hosts must include localhost and 127.0.0.1")

    denied_categories = set(policy.get("denied_destination_categories", []))
    required_denied = {
        "public_internet",
        "customer_network",
        "production_network",
        "metadata_service",
        "cloud_control_plane",
        "unknown_external_host",
    }
    missing_denied = required_denied - denied_categories
    if missing_denied:
        raise RuntimeSafetyPolicyError(f"denied_destination_categories missing: {sorted(missing_denied)}")

    kill_modes = set(policy.get("kill_switch_modes", []))
    required_kill_modes = {
        "operator_manual_stop",
        "timeout_forced_stop",
        "policy_violation_stop",
        "future_process_tree_termination",
    }
    missing_kill_modes = required_kill_modes - kill_modes
    if missing_kill_modes:
        raise RuntimeSafetyPolicyError(f"kill_switch_modes missing: {sorted(missing_kill_modes)}")

    required_blockers = {
        "runtime_execution_still_disabled",
        "external_process_execution_still_disabled",
        "network_activity_still_disabled",
        "no_egress_not_runtime_enforced",
        "timeout_not_runtime_enforced",
        "kill_switch_not_runtime_enforced",
        "process_tree_termination_not_implemented",
        "raw_artifact_capture_boundary_not_implemented",
        "human_approval_for_execution_transition_not_recorded",
    }
    missing_blockers = required_blockers - set(policy.get("policy_blockers", []))
    if missing_blockers:
        raise RuntimeSafetyPolicyError(f"runtime safety policy missing blockers: {sorted(missing_blockers)}")


def evaluate_runtime_safety_policy_gate(
    policy: dict[str, Any],
    *,
    policy_review_decision: str = "policy_recorded",
) -> dict[str, Any]:
    validate_runtime_safety_policy(policy)

    if policy_review_decision not in VALID_POLICY_REVIEW_DECISIONS:
        raise RuntimeSafetyPolicyError(f"unsupported policy_review_decision: {policy_review_decision}")

    if policy_review_decision == "policy_recorded":
        gate_status = "policy_recorded_execution_blocked"
        decision_recommendation = "define_runtime_enforcement_and_process_control_design"
        blockers = list(policy["policy_blockers"])
    elif policy_review_decision == "needs_revision":
        gate_status = "needs_revision"
        decision_recommendation = "revise_no_egress_timeout_kill_switch_policy"
        blockers = list(policy["policy_blockers"])
    else:
        gate_status = "rejected"
        decision_recommendation = "do_not_continue_to_runtime_execution_design"
        blockers = ["runtime_safety_policy_rejected"]

    gate = {
        "runtime_safety_policy_gate_type": "no_egress_timeout_kill_switch_policy_gate",
        "runtime_safety_policy_gate_status": gate_status,
        "runtime_safety_policy_id": policy["runtime_safety_policy_id"],
        "local_execution_plan_id": policy["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": policy["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": policy["runtime_destination_binding_id"],
        "scope_registry_destination_id": policy["scope_registry_destination_id"],
        "target_id": policy["target_id"],
        "scope_id": policy["scope_id"],
        "tool": policy["tool"],
        "adapter": policy["adapter"],
        "target_url": policy["target_url"],
        "target_mode": policy["target_mode"],
        "local_only": True,
        "policy_review_decision": policy_review_decision,
        "policy_review_satisfied": False,
        "no_egress_required": True,
        "no_egress_policy_defined": True,
        "timeout_required": True,
        "timeout_policy_defined": True,
        "kill_switch_required": True,
        "kill_switch_policy_defined": True,
        "process_tree_termination_required": True,
        "evidence_required": True,
        "sanitizer_required_before_ai_visible": True,
        "human_approval_required": True,
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
                "blocker": "no_egress_not_runtime_enforced",
                "next_action": "Design a runtime-enforced no-egress control before any local runtime network activity.",
            },
            {
                "blocker": "timeout_not_runtime_enforced",
                "next_action": "Implement timeout enforcement before any future process launch.",
            },
            {
                "blocker": "kill_switch_not_runtime_enforced",
                "next_action": "Implement manual and policy-triggered stop behavior before any future process launch.",
            },
            {
                "blocker": "process_tree_termination_not_implemented",
                "next_action": "Define process tree termination behavior before enabling external process launch.",
            },
            {
                "blocker": "raw_artifact_capture_boundary_not_implemented",
                "next_action": "Define raw artifact capture, storage, sanitizer, and AI-visible boundaries.",
            },
        ],
    }

    validate_runtime_safety_policy_gate_result(gate)
    return gate


def validate_runtime_safety_policy_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise RuntimeSafetyPolicyError(f"runtime safety policy gate missing fields: {missing}")

    if gate.get("runtime_safety_policy_gate_type") != "no_egress_timeout_kill_switch_policy_gate":
        raise RuntimeSafetyPolicyError("runtime_safety_policy_gate_type mismatch")

    if gate.get("policy_review_decision") not in VALID_POLICY_REVIEW_DECISIONS:
        raise RuntimeSafetyPolicyError("unsupported policy_review_decision")

    if gate.get("policy_review_satisfied") is not False:
        raise RuntimeSafetyPolicyError("policy_review_satisfied must remain false in current MVP")

    if gate.get("local_only") is not True:
        raise RuntimeSafetyPolicyError("local_only must be true")

    for field in [
        "no_egress_required",
        "no_egress_policy_defined",
        "timeout_required",
        "timeout_policy_defined",
        "kill_switch_required",
        "kill_switch_policy_defined",
        "process_tree_termination_required",
        "evidence_required",
        "sanitizer_required_before_ai_visible",
        "human_approval_required",
    ]:
        if gate.get(field) is not True:
            raise RuntimeSafetyPolicyError(f"{field} must be true")

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
            raise RuntimeSafetyPolicyError(f"{field} must be false")

    if not gate.get("blockers"):
        raise RuntimeSafetyPolicyError("runtime safety policy gate must include blockers")
