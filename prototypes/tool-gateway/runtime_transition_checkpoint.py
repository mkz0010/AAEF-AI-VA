from __future__ import annotations

from typing import Any

from preflight_validation import (
    PREFLIGHT_CHECKS,
    validate_preflight_validation_gate_result,
    validate_preflight_validation_scaffold,
)


class RuntimeTransitionCheckpointError(ValueError):
    pass


REQUIRED_CHECKPOINT_FIELDS = [
    "checkpoint_id",
    "checkpoint_type",
    "checkpoint_status",
    "project_phase",
    "current_version_target",
    "target_id",
    "scope_id",
    "tool",
    "adapter",
    "target_url",
    "target_mode",
    "local_only",
    "preflight_validation_id",
    "execution_authorization_id",
    "runtime_enforcement_design_id",
    "runtime_safety_policy_id",
    "local_execution_plan_id",
    "bounded_execution_transition_candidate_id",
    "runtime_destination_binding_id",
    "scope_registry_destination_id",
    "transition_layers",
    "required_preflight_checks",
    "safety_invariants",
    "explicit_non_goals",
    "readiness_summary",
    "checkpoint_blockers",
    "next_phase_candidates",
    "checkpoint_notes",
]


def build_runtime_transition_checkpoint(
    preflight_validation: dict[str, Any],
    preflight_gate: dict[str, Any],
) -> dict[str, Any]:
    validate_preflight_validation_scaffold(preflight_validation)
    validate_preflight_validation_gate_result(preflight_gate)

    if preflight_validation["preflight_validation_id"] != preflight_gate["preflight_validation_id"]:
        raise RuntimeTransitionCheckpointError("preflight validation/gate ID mismatch")

    if preflight_validation["execution_authorization_id"] != preflight_gate["execution_authorization_id"]:
        raise RuntimeTransitionCheckpointError("preflight validation/gate execution_authorization_id mismatch")

    if preflight_validation["target_id"] != preflight_gate["target_id"]:
        raise RuntimeTransitionCheckpointError("preflight validation/gate target_id mismatch")

    if preflight_validation["scope_id"] != preflight_gate["scope_id"]:
        raise RuntimeTransitionCheckpointError("preflight validation/gate scope_id mismatch")

    checkpoint = {
        "checkpoint_id": "v0.2.9-runtime-transition-checkpoint",
        "checkpoint_type": "runtime_transition_checkpoint",
        "checkpoint_status": "passed_execution_blocked",
        "project_phase": "v0.2.x-runtime-transition-readiness",
        "current_version_target": "v0.2.9",
        "target_id": preflight_validation["target_id"],
        "scope_id": preflight_validation["scope_id"],
        "tool": preflight_validation["tool"],
        "adapter": preflight_validation["adapter"],
        "target_url": preflight_validation["target_url"],
        "target_mode": preflight_validation["target_mode"],
        "local_only": True,
        "preflight_validation_id": preflight_validation["preflight_validation_id"],
        "execution_authorization_id": preflight_validation["execution_authorization_id"],
        "runtime_enforcement_design_id": preflight_validation["runtime_enforcement_design_id"],
        "runtime_safety_policy_id": preflight_validation["runtime_safety_policy_id"],
        "local_execution_plan_id": preflight_validation["local_execution_plan_id"],
        "bounded_execution_transition_candidate_id": preflight_validation["bounded_execution_transition_candidate_id"],
        "runtime_destination_binding_id": preflight_validation["runtime_destination_binding_id"],
        "scope_registry_destination_id": preflight_validation["scope_registry_destination_id"],
        "transition_layers": [
            {
                "version": "v0.2.0",
                "layer": "controlled_local_runtime_readiness",
                "status": "defined_detection_only",
                "execution_authority": False,
            },
            {
                "version": "v0.2.1",
                "layer": "local_target_lab_profile",
                "status": "defined_local_lab_target_boundary",
                "execution_authority": False,
            },
            {
                "version": "v0.2.2",
                "layer": "scope_registry_runtime_destination_binding",
                "status": "bound_runtime_to_target_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.3",
                "layer": "bounded_execution_transition_candidate",
                "status": "candidate_recorded_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.4",
                "layer": "local_only_execution_plan_review",
                "status": "plan_recorded_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.5",
                "layer": "runtime_safety_policy_scaffold",
                "status": "policy_recorded_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.6",
                "layer": "runtime_enforcement_design_scaffold",
                "status": "design_recorded_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.7",
                "layer": "execution_authorization_gate_scaffold",
                "status": "authorization_scaffold_recorded_execution_blocked",
                "execution_authority": False,
            },
            {
                "version": "v0.2.8",
                "layer": "preflight_validation_scaffold",
                "status": "preflight_scaffold_recorded_execution_blocked",
                "execution_authority": False,
            },
        ],
        "required_preflight_checks": list(PREFLIGHT_CHECKS),
        "safety_invariants": {
            "local_only": True,
            "preflight_satisfied": False,
            "execution_authorized": False,
            "execution_authorization_satisfied": False,
            "runtime_enforcement_implemented": False,
            "all_required_checks_satisfied": False,
            "scan_execution_allowed": False,
            "network_activity_allowed": False,
            "real_execution_permitted": False,
            "external_process_execution_allowed": False,
            "credential_injection_permitted": False,
            "raw_artifact_capture_permitted": False,
            "customer_target": False,
            "external_network_target": False,
        },
        "explicit_non_goals": [
            "Do not start ZAP.",
            "Do not call the ZAP API.",
            "Do not run spider, ajax spider, authenticated crawl, passive runtime collection, or active scan.",
            "Do not perform network activity, including localhost traffic, from this checkpoint.",
            "Do not spawn external processes.",
            "Do not inject credentials.",
            "Do not capture raw runtime artifacts.",
            "Do not mark preflight as satisfied.",
            "Do not authorize execution.",
            "Do not target customer systems or external networks.",
        ],
        "readiness_summary": {
            "runtime_transition_layers_defined": True,
            "preflight_checklist_defined": True,
            "ready_for_preflight_implementation": True,
            "ready_for_runtime_execution": False,
            "ready_for_customer_target": False,
            "ready_for_external_network": False,
            "requires_next_phase": "preflight_check_implementation_and_evidence_records",
        },
        "checkpoint_blockers": [
            "preflight_checks_not_implemented",
            "preflight_not_satisfied",
            "execution_authorization_not_satisfied",
            "runtime_enforcement_not_implemented",
            "no_egress_guard_not_verified",
            "timeout_watcher_not_verified",
            "kill_switch_controller_not_verified",
            "evidence_emitter_not_verified",
            "sanitizer_boundary_not_verified",
            "human_approval_not_recorded",
            "operator_confirmation_not_recorded",
            "scope_owner_approval_not_recorded",
        ],
        "next_phase_candidates": [
            "v0.3.0: concrete preflight check implementation scaffold",
            "preflight evidence record model",
            "current runtime readiness verification",
            "current scope registry binding verification",
            "no-egress verification evidence",
            "timeout and kill-switch verification evidence",
            "human/operator/scope-owner approval binding",
            "sanitizer boundary verification",
        ],
        "checkpoint_notes": (
            "v0.2.9 records the runtime transition readiness checkpoint. The platform has structured the "
            "runtime, target, binding, execution plan, safety policy, enforcement design, execution authorization, "
            "and preflight validation layers. This checkpoint confirms that the project is ready to design concrete "
            "preflight implementations next, while execution remains blocked."
        ),
    }

    validate_runtime_transition_checkpoint(checkpoint)
    return checkpoint


def validate_runtime_transition_checkpoint(checkpoint: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_CHECKPOINT_FIELDS if field not in checkpoint]
    if missing:
        raise RuntimeTransitionCheckpointError(f"runtime transition checkpoint missing fields: {missing}")

    if checkpoint.get("checkpoint_type") != "runtime_transition_checkpoint":
        raise RuntimeTransitionCheckpointError("checkpoint_type must be runtime_transition_checkpoint")

    if checkpoint.get("checkpoint_status") != "passed_execution_blocked":
        raise RuntimeTransitionCheckpointError("checkpoint_status must be passed_execution_blocked")

    if checkpoint.get("current_version_target") != "v0.2.9":
        raise RuntimeTransitionCheckpointError("current_version_target must be v0.2.9")

    if checkpoint.get("local_only") is not True:
        raise RuntimeTransitionCheckpointError("local_only must be true")

    layers = checkpoint.get("transition_layers", [])
    if len(layers) != 9:
        raise RuntimeTransitionCheckpointError("transition_layers must include v0.2.0 through v0.2.8")

    expected_versions = {f"v0.2.{i}" for i in range(0, 9)}
    actual_versions = {item.get("version") for item in layers}
    missing_versions = expected_versions - actual_versions
    if missing_versions:
        raise RuntimeTransitionCheckpointError(f"transition_layers missing versions: {sorted(missing_versions)}")

    for item in layers:
        if item.get("execution_authority") is not False:
            raise RuntimeTransitionCheckpointError("all transition layers must have execution_authority=false")

    required_checks = set(checkpoint.get("required_preflight_checks", []))
    missing_checks = set(PREFLIGHT_CHECKS) - required_checks
    if missing_checks:
        raise RuntimeTransitionCheckpointError(f"required_preflight_checks missing: {sorted(missing_checks)}")

    invariants = checkpoint.get("safety_invariants", {})
    if invariants.get("local_only") is not True:
        raise RuntimeTransitionCheckpointError("safety invariant local_only must be true")

    required_false = [
        "preflight_satisfied",
        "execution_authorized",
        "execution_authorization_satisfied",
        "runtime_enforcement_implemented",
        "all_required_checks_satisfied",
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
        if invariants.get(field) is not False:
            raise RuntimeTransitionCheckpointError(f"safety invariant must be false: {field}")

    readiness = checkpoint.get("readiness_summary", {})
    if readiness.get("runtime_transition_layers_defined") is not True:
        raise RuntimeTransitionCheckpointError("runtime_transition_layers_defined must be true")

    if readiness.get("preflight_checklist_defined") is not True:
        raise RuntimeTransitionCheckpointError("preflight_checklist_defined must be true")

    if readiness.get("ready_for_preflight_implementation") is not True:
        raise RuntimeTransitionCheckpointError("ready_for_preflight_implementation must be true")

    for field in [
        "ready_for_runtime_execution",
        "ready_for_customer_target",
        "ready_for_external_network",
    ]:
        if readiness.get(field) is not False:
            raise RuntimeTransitionCheckpointError(f"{field} must be false")

    required_blockers = {
        "preflight_checks_not_implemented",
        "preflight_not_satisfied",
        "execution_authorization_not_satisfied",
        "runtime_enforcement_not_implemented",
        "no_egress_guard_not_verified",
        "timeout_watcher_not_verified",
        "kill_switch_controller_not_verified",
        "evidence_emitter_not_verified",
        "sanitizer_boundary_not_verified",
        "human_approval_not_recorded",
        "operator_confirmation_not_recorded",
        "scope_owner_approval_not_recorded",
    }
    missing_blockers = required_blockers - set(checkpoint.get("checkpoint_blockers", []))
    if missing_blockers:
        raise RuntimeTransitionCheckpointError(f"checkpoint missing blockers: {sorted(missing_blockers)}")


def format_runtime_transition_checkpoint_markdown(checkpoint: dict[str, Any]) -> str:
    validate_runtime_transition_checkpoint(checkpoint)

    lines: list[str] = []
    lines.append("# Runtime Transition Checkpoint")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Checkpoint ID: `{checkpoint['checkpoint_id']}`")
    lines.append(f"- Checkpoint status: `{checkpoint['checkpoint_status']}`")
    lines.append(f"- Project phase: `{checkpoint['project_phase']}`")
    lines.append(f"- Version target: `{checkpoint['current_version_target']}`")
    lines.append(f"- Target ID: `{checkpoint['target_id']}`")
    lines.append(f"- Scope ID: `{checkpoint['scope_id']}`")
    lines.append(f"- Tool: `{checkpoint['tool']}`")
    lines.append(f"- Adapter: `{checkpoint['adapter']}`")
    lines.append("")
    lines.append("## Transition Layers")
    lines.append("")
    for item in checkpoint["transition_layers"]:
        lines.append(
            f"- `{item['version']}` `{item['layer']}`: `{item['status']}`; execution authority: `{item['execution_authority']}`"
        )
    lines.append("")
    lines.append("## Safety Invariants")
    lines.append("")
    for key, value in checkpoint["safety_invariants"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("## Explicit Non-Goals")
    lines.append("")
    for item in checkpoint["explicit_non_goals"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Required Preflight Checks")
    lines.append("")
    for item in checkpoint["required_preflight_checks"]:
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## Checkpoint Blockers")
    lines.append("")
    for item in checkpoint["checkpoint_blockers"]:
        lines.append(f"- `{item}`")
    lines.append("")
    lines.append("## Next Phase Candidates")
    lines.append("")
    for item in checkpoint["next_phase_candidates"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(checkpoint["checkpoint_notes"])
    lines.append("")
    return "\n".join(lines)
