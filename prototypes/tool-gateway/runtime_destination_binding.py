from __future__ import annotations

from typing import Any

from local_target_lab import validate_local_target_lab_gate_result, validate_local_target_lab_profile
from runtime_readiness import validate_runtime_profile, validate_runtime_readiness_result


class RuntimeDestinationBindingError(ValueError):
    pass


REQUIRED_BINDING_FIELDS = [
    "runtime_destination_binding_id",
    "binding_type",
    "binding_status",
    "scope_registry_destination_id",
    "runtime_profile_id",
    "runtime_readiness_status",
    "lab_profile_id",
    "target_id",
    "scope_id",
    "target_url",
    "target_mode",
    "tool",
    "adapter",
    "operation_family",
    "runtime_detection_only",
    "target_defined",
    "runtime_detected",
    "target_allowed_for_future_runtime_transition",
    "bounded_execution_transition_candidate_allowed",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "external_process_execution_allowed",
    "scope_registry_binding_required",
    "runtime_readiness_required",
    "local_target_lab_required",
    "human_approval_required_for_execution_transition",
    "sanitizer_required_before_ai_visible",
    "customer_target",
    "external_network_target",
    "binding_notes",
    "blockers",
    "next_actions",
]


REQUIRED_GATE_FIELDS = [
    "runtime_destination_binding_gate_type",
    "runtime_destination_binding_gate_status",
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
    "bounded_execution_transition_candidate_allowed",
    "scan_execution_allowed",
    "network_activity_allowed",
    "real_execution_permitted",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "external_process_execution_allowed",
    "customer_target",
    "external_network_target",
    "blockers",
    "next_actions",
]


def build_scope_registry_runtime_destination_binding(
    runtime_profile: dict[str, Any],
    runtime_readiness: dict[str, Any],
    lab_profile: dict[str, Any],
    lab_gate: dict[str, Any],
    *,
    scope_registry_destination_id: str = "scope-destination-local-lab-001",
    operation_family: str = "local_lab_web_assessment",
) -> dict[str, Any]:
    validate_runtime_profile(runtime_profile)
    validate_runtime_readiness_result(runtime_readiness)
    validate_local_target_lab_profile(lab_profile)
    validate_local_target_lab_gate_result(lab_gate)

    if runtime_profile["runtime_profile_id"] != runtime_readiness["runtime_profile_id"]:
        raise RuntimeDestinationBindingError("runtime profile/readiness runtime_profile_id mismatch")

    if lab_profile["lab_profile_id"] != lab_gate["lab_profile_id"]:
        raise RuntimeDestinationBindingError("lab profile/gate lab_profile_id mismatch")

    if runtime_profile["tool"] != lab_profile["allowed_tools"][0]:
        raise RuntimeDestinationBindingError("runtime tool must match local lab allowed tool")

    if runtime_readiness["tool"] != runtime_profile["tool"]:
        raise RuntimeDestinationBindingError("runtime readiness tool mismatch")

    if runtime_readiness["adapter"] != runtime_profile["adapter"]:
        raise RuntimeDestinationBindingError("runtime readiness adapter mismatch")

    blockers = [
        "bounded_execution_transition_not_defined",
        "scan_execution_disabled",
        "network_activity_disabled",
        "real_execution_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "external_process_execution_disabled",
    ]

    if not runtime_readiness["runtime_detected"]:
        blockers.append("runtime_binary_not_detected")

    binding = {
        "runtime_destination_binding_id": (
            f"runtime-destination-binding-{runtime_profile['runtime_profile_id']}-{lab_profile['target_id']}"
        ),
        "binding_type": "scope_registry_runtime_destination_binding",
        "binding_status": "bound_execution_blocked",
        "scope_registry_destination_id": scope_registry_destination_id,
        "runtime_profile_id": runtime_profile["runtime_profile_id"],
        "runtime_readiness_status": runtime_readiness["runtime_readiness_status"],
        "lab_profile_id": lab_profile["lab_profile_id"],
        "target_id": lab_profile["target_id"],
        "scope_id": lab_profile["scope_id"],
        "target_url": lab_profile["target_url"],
        "target_mode": lab_profile["target_mode"],
        "tool": runtime_profile["tool"],
        "adapter": runtime_profile["adapter"],
        "operation_family": operation_family,
        "runtime_detection_only": True,
        "target_defined": True,
        "runtime_detected": runtime_readiness["runtime_detected"],
        "target_allowed_for_future_runtime_transition": lab_gate["target_allowed_for_future_runtime_transition"],
        "bounded_execution_transition_candidate_allowed": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "external_process_execution_allowed": False,
        "scope_registry_binding_required": True,
        "runtime_readiness_required": True,
        "local_target_lab_required": True,
        "human_approval_required_for_execution_transition": True,
        "sanitizer_required_before_ai_visible": True,
        "customer_target": False,
        "external_network_target": False,
        "binding_notes": (
            "This binding records that a controlled local runtime readiness profile is associated "
            "with a local target lab profile through a scope-registry-style destination record. "
            "It does not permit scans, network activity, process execution, credential injection, "
            "or raw artifact capture."
        ),
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "bounded_execution_transition_not_defined",
                "next_action": "Define a separate bounded execution transition gate before any local execution.",
            },
            {
                "blocker": "scan_execution_disabled",
                "next_action": "Keep scan operations disabled until explicit local-only execution controls exist.",
            },
            {
                "blocker": "network_activity_disabled",
                "next_action": "Do not perform network traffic, even to localhost, from this binding layer.",
            },
            {
                "blocker": "real_execution_disabled",
                "next_action": "Treat binding as a prerequisite, not execution authority.",
            },
        ],
    }

    validate_scope_registry_runtime_destination_binding(binding)
    return binding


def validate_scope_registry_runtime_destination_binding(binding: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_BINDING_FIELDS if field not in binding]
    if missing:
        raise RuntimeDestinationBindingError(f"runtime destination binding missing required fields: {missing}")

    if binding.get("binding_type") != "scope_registry_runtime_destination_binding":
        raise RuntimeDestinationBindingError("binding_type must be scope_registry_runtime_destination_binding")

    if binding.get("binding_status") != "bound_execution_blocked":
        raise RuntimeDestinationBindingError("binding_status must be bound_execution_blocked")

    if binding.get("runtime_detection_only") is not True:
        raise RuntimeDestinationBindingError("runtime_detection_only must be true")

    if binding.get("target_defined") is not True:
        raise RuntimeDestinationBindingError("target_defined must be true")

    if binding.get("target_allowed_for_future_runtime_transition") is not True:
        raise RuntimeDestinationBindingError("target_allowed_for_future_runtime_transition must be true")

    if binding.get("bounded_execution_transition_candidate_allowed") is not True:
        raise RuntimeDestinationBindingError("bounded_execution_transition_candidate_allowed must be true for valid binding")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "external_process_execution_allowed",
        "customer_target",
        "external_network_target",
    ]:
        if binding.get(field) is not False:
            raise RuntimeDestinationBindingError(f"{field} must be false")

    for field in [
        "scope_registry_binding_required",
        "runtime_readiness_required",
        "local_target_lab_required",
        "human_approval_required_for_execution_transition",
        "sanitizer_required_before_ai_visible",
    ]:
        if binding.get(field) is not True:
            raise RuntimeDestinationBindingError(f"{field} must be true")

    if binding.get("tool") != "zap":
        raise RuntimeDestinationBindingError("current MVP binding supports zap only")

    if binding.get("adapter") != "zap":
        raise RuntimeDestinationBindingError("current MVP binding supports zap adapter only")

    required_blockers = {
        "bounded_execution_transition_not_defined",
        "scan_execution_disabled",
        "network_activity_disabled",
        "real_execution_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "external_process_execution_disabled",
    }
    missing_blockers = required_blockers - set(binding.get("blockers", []))
    if missing_blockers:
        raise RuntimeDestinationBindingError(f"binding missing blockers: {sorted(missing_blockers)}")

    if binding.get("runtime_detected") is False and "runtime_binary_not_detected" not in binding.get("blockers", []):
        raise RuntimeDestinationBindingError("runtime_binary_not_detected blocker required when runtime not detected")


def evaluate_runtime_destination_binding_gate(binding: dict[str, Any]) -> dict[str, Any]:
    validate_scope_registry_runtime_destination_binding(binding)

    gate = {
        "runtime_destination_binding_gate_type": "scope_registry_runtime_destination_binding_gate",
        "runtime_destination_binding_gate_status": "bound_execution_blocked",
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
        "bounded_execution_transition_candidate_allowed": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_permitted": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "external_process_execution_allowed": False,
        "customer_target": False,
        "external_network_target": False,
        "blockers": list(binding["blockers"]),
        "next_actions": list(binding["next_actions"]),
    }

    validate_runtime_destination_binding_gate_result(gate)
    return gate


def validate_runtime_destination_binding_gate_result(gate: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in gate]
    if missing:
        raise RuntimeDestinationBindingError(f"runtime destination binding gate missing required fields: {missing}")

    if gate.get("runtime_destination_binding_gate_status") != "bound_execution_blocked":
        raise RuntimeDestinationBindingError("runtime_destination_binding_gate_status must be bound_execution_blocked")

    if gate.get("bounded_execution_transition_candidate_allowed") is not True:
        raise RuntimeDestinationBindingError("bounded_execution_transition_candidate_allowed must be true")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "real_execution_permitted",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
        "external_process_execution_allowed",
        "customer_target",
        "external_network_target",
    ]:
        if gate.get(field) is not False:
            raise RuntimeDestinationBindingError(f"{field} must be false")

    required_blockers = {
        "bounded_execution_transition_not_defined",
        "scan_execution_disabled",
        "network_activity_disabled",
        "real_execution_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "external_process_execution_disabled",
    }
    missing_blockers = required_blockers - set(gate.get("blockers", []))
    if missing_blockers:
        raise RuntimeDestinationBindingError(f"gate missing blockers: {sorted(missing_blockers)}")
