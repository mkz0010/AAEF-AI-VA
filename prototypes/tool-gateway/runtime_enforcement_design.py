from __future__ import annotations

from typing import Any

from runtime_safety_policy import (
    validate_runtime_safety_policy,
    validate_runtime_safety_policy_gate_result,
)


class RuntimeEnforcementDesignError(ValueError):
    pass


VALID_DESIGN_REVIEW_DECISIONS = {
    "design_recorded",
    "needs_revision",
    "rejected",
}


REQUIRED_DESIGN_FIELDS = [
    "runtime_enforcement_design_id",
    "design_type",
    "design_status",
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
    "enforcement_design_recorded",
    "runtime_enforcement_implemented",
    "preflight_check_required",
    "process_wrapper_required",
    "no_egress_guard_required",
    "timeout_watcher_required",
    "kill_switch_controller_required",
    "process_tree_termination_required",
    "evidence_emitter_required",
    "sanitizer_boundary_required",
    "human_approval_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "customer_target",
    "external_network_target",
    "enforcement_components",
    "enforcement_sequence",
    "design_blockers",
    "design_notes",
]


REQUIRED_GATE_FIELDS = [
    "runtime_enforcement_design_gate_type",
    "runtime_enforcement_design_gate_status",
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
    "design_review_decision",
    "design_review_satisfied",
    "runtime_enforcement_implemented",
    "preflight_check_required",
    "process_wrapper_required",
    "no_egress_guard_required",
    "timeout_watcher_required",
    "kill_switch_controller_required",
    "process_tree_termination_required",
    "evidence_emitter_required",
    "sanitizer_boundary_required",
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


def build_runtime_enforcement_design(
    runtime_safety_policy: dict[str, Any],
    runtime_safety_policy_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_runtime_safety_policy(runtime_safety_policy)
    validate_runtime_safety_policy_gate_result(runtime_safety_policy_gate)

    if runtime_safety_policy["runtime_safety_policy_id"] != runtime_safety_policy_gate["runtime_safety_policy_id"]:
        raise RuntimeEnforcementDesignError("runtime safety policy/gate ID mismatch")

    if runtime_safety_policy["local_execution_plan_id"] != runtime_safety_policy_gate["local_execution_plan_id"]:
        raise RuntimeEnforcementDesignError("runtime safety policy/gate local_execution_plan_id mismatch")

    if runtime_safety_policy["target_id"] != runtime_safety_policy_gate["target_id"]:
        raise RuntimeEnforcementDesignError("runtime safety policy/gate target_id mismatch")

    if runtime_safety_policy["scope_id"] != runtime_safety_policy_gate["scope_id"]:
        raise RuntimeEnforcementDesignError("runtime safety policy/gate scope_id mismatch")

    design = {
        "runtime_enforcement_design_id": f"runtime-enforcement-design-{runtime_safety_policy['runtime_safety_policy_id']}",
        "design_type": "runtime_enforcement_design_scaffold",
        "design_status": "design_recorded_execution_blocked",
        "runtime_safety_policy_id": runtime_safety_policy["runtime_safety_policy_id"],
        "local_execution_plan_id": runtime_safety_policy["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": runtime_safety_policy["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": runtime_safety_policy["runtime_destination_binding_id"],
        "scope_registry_destination_id": runtime_safety_policy["scope_registry_destination_id"],
        "target_id": runtime_safety_policy["target_id"],
        "scope_id": runtime_safety_policy["scope_id"],
        "tool": runtime_safety_policy["tool"],
        "adapter": runtime_safety_policy["adapter"],
        "target_url": runtime_safety_policy["target_url"],
        "target_mode": runtime_safety_policy["target_mode"],
        "local_only": True,
        "enforcement_design_recorded": True,
        "runtime_enforcement_implemented": False,
        "preflight_check_required": True,
        "process_wrapper_required": True,
        "no_egress_guard_required": True,
        "timeout_watcher_required": True,
        "kill_switch_controller_required": True,
        "process_tree_termination_required": True,
        "evidence_emitter_required": True,
        "sanitizer_boundary_required": True,
        "human_approval_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "customer_target": False,
        "external_network_target": False,
        "enforcement_components": [
            {
                "component": "preflight_check",
                "status": "design_required_not_implemented",
                "responsibility": "validate runtime, target, binding, policy, approval, timeout, no-egress, and sanitizer requirements before any future process launch",
            },
            {
                "component": "process_wrapper",
                "status": "design_required_not_implemented",
                "responsibility": "future controlled wrapper for any local ZAP process; not implemented in current MVP",
            },
            {
                "component": "no_egress_guard",
                "status": "design_required_not_implemented",
                "responsibility": "future guard for local-only destinations and denied destination categories",
            },
            {
                "component": "timeout_watcher",
                "status": "design_required_not_implemented",
                "responsibility": "future max runtime and idle timeout enforcement",
            },
            {
                "component": "kill_switch_controller",
                "status": "design_required_not_implemented",
                "responsibility": "future manual, timeout, and policy-violation stop control",
            },
            {
                "component": "evidence_emitter",
                "status": "design_required_not_implemented",
                "responsibility": "future evidence event generation for preflight, runtime, stop, and artifact handling",
            },
            {
                "component": "sanitizer_boundary",
                "status": "design_required_not_implemented",
                "responsibility": "future raw artifact to sanitized artifact boundary before any AI-visible output",
            },
        ],
        "enforcement_sequence": [
            "load_scope_registry_runtime_destination_binding",
            "validate_local_target_lab_profile",
            "validate_runtime_readiness",
            "validate_local_execution_plan",
            "validate_runtime_safety_policy",
            "require_human_approval_for_execution_transition",
            "perform_preflight_check",
            "start_future_process_wrapper_only_if_authorized",
            "enforce_no_egress_guard",
            "enforce_timeout_watcher",
            "enable_kill_switch_controller",
            "emit_evidence_events",
            "store_raw_artifacts_outside_ai_visibility",
            "run_sanitizer_before_ai_visible_output",
            "keep_customer_targets_and_external_networks_forbidden",
        ],
        "design_blockers": [
            "runtime_enforcement_not_implemented",
            "process_wrapper_not_implemented",
            "no_egress_guard_not_implemented",
            "timeout_watcher_not_implemented",
            "kill_switch_controller_not_implemented",
            "process_tree_termination_not_implemented",
            "evidence_emitter_not_implemented",
            "sanitizer_boundary_not_runtime_bound",
            "human_approval_for_execution_transition_not_recorded",
            "execution_authorization_gate_not_defined",
        ],
        "design_notes": (
            "This runtime enforcement design scaffold describes future enforcement components and sequence. "
            "It does not implement process launch, no-egress enforcement, timeout enforcement, kill-switch behavior, "
            "network activity, scans, credential injection, or raw artifact capture."
        ),
    }

    validate_runtime_enforcement_design(design)
    return design


def validate_runtime_enforcement_design(design: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_DESIGN_FIELDS if field not in design]
    if missing:
        raise RuntimeEnforcementDesignError(f"runtime enforcement design missing fields: {missing}")

    if design.get("design_type") != "runtime_enforcement_design_scaffold":
        raise RuntimeEnforcementDesignError("design_type must be runtime_enforcement_design_scaffold")

    if design.get("design_status") != "design_recorded_execution_blocked":
        raise RuntimeEnforcementDesignError("design_status must be design_recorded_execution_blocked")

    if design.get("local_only") is not True:
        raise RuntimeEnforcementDesignError("local_only must be true")

    if design.get("enforcement_design_recorded") is not True:
        raise RuntimeEnforcementDesignError("enforcement_design_recorded must be true")

    if design.get("runtime_enforcement_implemented") is not False:
        raise RuntimeEnforcementDesignError("runtime_enforcement_implemented must be false in current MVP")

    for field in [
        "preflight_check_required",
        "process_wrapper_required",
        "no_egress_guard_required",
        "timeout_watcher_required",
        "kill_switch_controller_required",
        "process_tree_termination_required",
        "evidence_emitter_required",
        "sanitizer_boundary_required",
        "human_approval_required",
    ]:
        if design.get(field) is not True:
            raise RuntimeEnforcementDesignError(f"{field} must be true")

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
        if design.get(field) is not False:
            raise RuntimeEnforcementDesignError(f"{field} must be false")

    required_components = {
        "preflight_check",
        "process_wrapper",
        "no_egress_guard",
        "timeout_watcher",
        "kill_switch_controller",
        "evidence_emitter",
        "sanitizer_boundary",
    }
    components = {item.get("component") for item in design.get("enforcement_components", [])}
    missing_components = required_components - components
    if missing_components:
        raise RuntimeEnforcementDesignError(f"runtime enforcement design missing components: {sorted(missing_components)}")

    for item in design.get("enforcement_components", []):
        if item.get("status") != "design_required_not_implemented":
            raise RuntimeEnforcementDesignError("all enforcement components must remain design_required_not_implemented")

    required_blockers = {
        "runtime_enforcement_not_implemented",
        "process_wrapper_not_implemented",
        "no_egress_guard_not_implemented",
        "timeout_watcher_not_implemented",
        "kill_switch_controller_not_implemented",
        "process_tree_termination_not_implemented",
        "evidence_emitter_not_implemented",
        "sanitizer_boundary_not_runtime_bound",
        "human_approval_for_execution_transition_not_recorded",
        "execution_authorization_gate_not_defined",
    }
    missing_blockers = required_blockers - set(design.get("design_blockers", []))
    if missing_blockers:
        raise RuntimeEnforcementDesignError(f"runtime enforcement design missing blockers: {sorted(missing_blockers)}")


def evaluate_runtime_enforcement_design_gate(
    design: dict[str, Any],
    *,
    design_review_decision: str = "design_recorded",
) -> dict[str, Any]:
    validate_runtime_enforcement_design(design)

    if design_review_decision not in VALID_DESIGN_REVIEW_DECISIONS:
        raise RuntimeEnforcementDesignError(f"unsupported design_review_decision: {design_review_decision}")

    if design_review_decision == "design_recorded":
        gate_status = "design_recorded_execution_blocked"
        decision_recommendation = "define_execution_authorization_gate_and_enforcement_tests"
        blockers = list(design["design_blockers"])
    elif design_review_decision == "needs_revision":
        gate_status = "needs_revision"
        decision_recommendation = "revise_runtime_enforcement_design"
        blockers = list(design["design_blockers"])
    else:
        gate_status = "rejected"
        decision_recommendation = "do_not_continue_to_execution_authorization_design"
        blockers = ["runtime_enforcement_design_rejected"]

    gate = {
        "runtime_enforcement_design_gate_type": "runtime_enforcement_design_gate",
        "runtime_enforcement_design_gate_status": gate_status,
        "runtime_enforcement_design_id": design["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": design["runtime_safety_policy_id"],
        "local_execution_plan_id": design["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": design["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": design["runtime_destination_binding_id"],
        "scope_registry_destination_id": design["scope_registry_destination_id"],
        "target_id": design["target_id"],
        "scope_id": design["scope_id"],
        "tool": design["tool"],
        "adapter": design["adapter"],
        "target_url": design["target_url"],
        "target_mode": design["target_mode"],
        "local_only": True,
        "design_review_decision": design_review_decision,
        "design_review_satisfied": False,
        "runtime_enforcement_implemented": False,
        "preflight_check_required": True,
        "process_wrapper_required": True,
        "no_egress_guard_required": True,
        "timeout_watcher_required": True,
        "kill_switch_controller_required": True,
        "process_tree_termination_required": True,
        "evidence_emitter_required": True,
        "sanitizer_boundary_required": True,
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
                "blocker": "execution_authorization_gate_not_defined",
                "next_action": "Define an execution authorization gate before any runtime enforcement implementation can be used.",
            },
            {
                "blocker": "process_wrapper_not_implemented",
                "next_action": "Design tests for a future process wrapper before any ZAP launch is enabled.",
            },
            {
                "blocker": "no_egress_guard_not_implemented",
                "next_action": "Design no-egress guard checks before any network activity is enabled.",
            },
            {
                "blocker": "timeout_watcher_not_implemented",
                "next_action": "Design timeout watcher tests before any external process execution is enabled.",
            },
            {
                "blocker": "kill_switch_controller_not_implemented",
                "next_action": "Design manual and policy-triggered stop tests before any external process execution is enabled.",
            },
            {
                "blocker": "sanitizer_boundary_not_runtime_bound",
                "next_action": "Bind runtime output to sanitizer policy before any raw artifact capture is enabled.",
            },
        ],
    }

    validate_runtime_enforcement_design_gate_result(gate)
    return gate


def validate_runtime_enforcement_design_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise RuntimeEnforcementDesignError(f"runtime enforcement design gate missing fields: {missing}")

    if gate.get("runtime_enforcement_design_gate_type") != "runtime_enforcement_design_gate":
        raise RuntimeEnforcementDesignError("runtime_enforcement_design_gate_type mismatch")

    if gate.get("design_review_decision") not in VALID_DESIGN_REVIEW_DECISIONS:
        raise RuntimeEnforcementDesignError("unsupported design_review_decision")

    if gate.get("design_review_satisfied") is not False:
        raise RuntimeEnforcementDesignError("design_review_satisfied must remain false in current MVP")

    if gate.get("runtime_enforcement_implemented") is not False:
        raise RuntimeEnforcementDesignError("runtime_enforcement_implemented must remain false")

    if gate.get("local_only") is not True:
        raise RuntimeEnforcementDesignError("local_only must be true")

    for field in [
        "preflight_check_required",
        "process_wrapper_required",
        "no_egress_guard_required",
        "timeout_watcher_required",
        "kill_switch_controller_required",
        "process_tree_termination_required",
        "evidence_emitter_required",
        "sanitizer_boundary_required",
        "human_approval_required",
    ]:
        if gate.get(field) is not True:
            raise RuntimeEnforcementDesignError(f"{field} must be true")

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
            raise RuntimeEnforcementDesignError(f"{field} must be false")

    if not gate.get("blockers"):
        raise RuntimeEnforcementDesignError("runtime enforcement design gate must include blockers")
