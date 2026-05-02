from __future__ import annotations

import os
import shutil
from pathlib import Path
from typing import Any


class RuntimeReadinessError(ValueError):
    pass


DEFAULT_ZAP_CANDIDATES = [
    "zap.sh",
    "zap.bat",
    "zaproxy",
    "zap",
]


ALLOWED_TARGET_MODES = {
    "localhost_only",
    "docker_internal_only",
    "isolated_lab_only",
}


REQUIRED_RUNTIME_PROFILE_FIELDS = [
    "runtime_profile_id",
    "runtime_profile_status",
    "tool",
    "adapter",
    "runtime_detection_only",
    "binary_candidates",
    "allowed_target_modes",
    "external_process_execution_allowed",
    "network_activity_allowed",
    "real_execution_allowed",
    "credential_injection_allowed",
    "raw_artifact_capture_allowed",
    "sanitizer_required_before_ai_visible",
    "scope_registry_required",
    "human_approval_required_for_execution_transition",
    "runtime_notes",
]


REQUIRED_READINESS_RESULT_FIELDS = [
    "runtime_readiness_gate_type",
    "runtime_readiness_status",
    "tool",
    "adapter",
    "runtime_profile_id",
    "runtime_detected",
    "detected_binary_path",
    "runtime_detection_only",
    "external_process_executed",
    "network_activity_performed",
    "real_execution_permitted",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "sanitizer_required_before_ai_visible",
    "scope_registry_required",
    "human_approval_required_for_execution_transition",
    "allowed_target_modes",
    "blockers",
    "next_actions",
]


def build_zap_runtime_profile(
    *,
    runtime_profile_id: str = "local-zap-runtime-readiness-mvp",
    binary_candidates: list[str] | None = None,
    allowed_target_modes: list[str] | None = None,
) -> dict[str, Any]:
    candidates = list(binary_candidates or DEFAULT_ZAP_CANDIDATES)
    target_modes = list(allowed_target_modes or ["localhost_only", "docker_internal_only"])

    profile = {
        "runtime_profile_id": runtime_profile_id,
        "runtime_profile_status": "runtime_detection_only",
        "tool": "zap",
        "adapter": "zap",
        "runtime_detection_only": True,
        "binary_candidates": candidates,
        "allowed_target_modes": target_modes,
        "external_process_execution_allowed": False,
        "network_activity_allowed": False,
        "real_execution_allowed": False,
        "credential_injection_allowed": False,
        "raw_artifact_capture_allowed": False,
        "sanitizer_required_before_ai_visible": True,
        "scope_registry_required": True,
        "human_approval_required_for_execution_transition": True,
        "runtime_notes": (
            "This profile may detect a local ZAP runtime path but must not start ZAP, "
            "spawn external processes, perform network activity, inject credentials, or capture raw artifacts."
        ),
    }

    validate_runtime_profile(profile)
    return profile


def validate_runtime_profile(profile: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_RUNTIME_PROFILE_FIELDS if field not in profile]
    if missing:
        raise RuntimeReadinessError(f"runtime profile missing required fields: {missing}")

    if profile.get("runtime_profile_status") != "runtime_detection_only":
        raise RuntimeReadinessError("runtime_profile_status must be runtime_detection_only")

    if profile.get("tool") != "zap":
        raise RuntimeReadinessError("current MVP runtime readiness supports zap only")

    if profile.get("adapter") != "zap":
        raise RuntimeReadinessError("current MVP runtime readiness supports zap adapter only")

    if profile.get("runtime_detection_only") is not True:
        raise RuntimeReadinessError("runtime_detection_only must be true")

    for field in [
        "external_process_execution_allowed",
        "network_activity_allowed",
        "real_execution_allowed",
        "credential_injection_allowed",
        "raw_artifact_capture_allowed",
    ]:
        if profile.get(field) is not False:
            raise RuntimeReadinessError(f"{field} must be false in current MVP")

    for field in [
        "sanitizer_required_before_ai_visible",
        "scope_registry_required",
        "human_approval_required_for_execution_transition",
    ]:
        if profile.get(field) is not True:
            raise RuntimeReadinessError(f"{field} must be true in current MVP")

    if not profile.get("binary_candidates"):
        raise RuntimeReadinessError("binary_candidates must not be empty")

    unknown_modes = set(profile.get("allowed_target_modes", [])) - ALLOWED_TARGET_MODES
    if unknown_modes:
        raise RuntimeReadinessError(f"unsupported allowed_target_modes: {sorted(unknown_modes)}")


def _detect_binary(candidates: list[str], lookup: dict[str, str | None] | None = None) -> tuple[bool, str | None]:
    if lookup is not None:
        for candidate in candidates:
            resolved = lookup.get(candidate)
            if resolved:
                return True, resolved
        return False, None

    for candidate in candidates:
        resolved = shutil.which(candidate)
        if resolved:
            return True, resolved
    return False, None


def evaluate_local_runtime_readiness(
    profile: dict[str, Any],
    *,
    lookup: dict[str, str | None] | None = None,
) -> dict[str, Any]:
    validate_runtime_profile(profile)

    runtime_detected, detected_binary_path = _detect_binary(profile["binary_candidates"], lookup=lookup)

    blockers: list[str] = [
        "real_execution_disabled",
        "external_process_execution_disabled",
        "network_activity_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "bounded_execution_transition_not_defined",
    ]

    if not runtime_detected:
        blockers.append("runtime_binary_not_detected")

    next_actions = [
        {
            "blocker": "real_execution_disabled",
            "next_action": "Keep real execution disabled until a bounded execution transition is explicitly designed.",
        },
        {
            "blocker": "external_process_execution_disabled",
            "next_action": "Do not spawn ZAP or any external process in this runtime readiness phase.",
        },
        {
            "blocker": "network_activity_disabled",
            "next_action": "Do not perform scans, crawls, proxy traffic, or API calls in this phase.",
        },
        {
            "blocker": "bounded_execution_transition_not_defined",
            "next_action": "Define a future transition gate before any local-only execution can be attempted.",
        },
    ]

    if not runtime_detected:
        next_actions.append(
            {
                "blocker": "runtime_binary_not_detected",
                "next_action": "Install or configure ZAP later, but do not execute it from this readiness gate.",
            }
        )

    result = {
        "runtime_readiness_gate_type": "controlled_local_runtime_readiness",
        "runtime_readiness_status": "detected_but_execution_blocked" if runtime_detected else "not_detected_execution_blocked",
        "tool": profile["tool"],
        "adapter": profile["adapter"],
        "runtime_profile_id": profile["runtime_profile_id"],
        "runtime_detected": runtime_detected,
        "detected_binary_path": detected_binary_path,
        "runtime_detection_only": True,
        "external_process_executed": False,
        "network_activity_performed": False,
        "real_execution_permitted": False,
        "credential_injection_permitted": False,
        "raw_artifact_capture_permitted": False,
        "sanitizer_required_before_ai_visible": True,
        "scope_registry_required": True,
        "human_approval_required_for_execution_transition": True,
        "allowed_target_modes": profile["allowed_target_modes"],
        "blockers": blockers,
        "next_actions": next_actions,
    }

    validate_runtime_readiness_result(result)
    return result


def validate_runtime_readiness_result(result: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_READINESS_RESULT_FIELDS if field not in result]
    if missing:
        raise RuntimeReadinessError(f"runtime readiness result missing required fields: {missing}")

    if result.get("runtime_detection_only") is not True:
        raise RuntimeReadinessError("runtime readiness must remain detection-only")

    for field in [
        "external_process_executed",
        "network_activity_performed",
        "real_execution_permitted",
        "credential_injection_permitted",
        "raw_artifact_capture_permitted",
    ]:
        if result.get(field) is not False:
            raise RuntimeReadinessError(f"{field} must be false in current MVP")

    for field in [
        "sanitizer_required_before_ai_visible",
        "scope_registry_required",
        "human_approval_required_for_execution_transition",
    ]:
        if result.get(field) is not True:
            raise RuntimeReadinessError(f"{field} must be true")

    required_blockers = {
        "real_execution_disabled",
        "external_process_execution_disabled",
        "network_activity_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "bounded_execution_transition_not_defined",
    }
    missing_blockers = required_blockers - set(result.get("blockers", []))
    if missing_blockers:
        raise RuntimeReadinessError(f"runtime readiness result missing blockers: {sorted(missing_blockers)}")

    if result.get("runtime_detected") is False and "runtime_binary_not_detected" not in result.get("blockers", []):
        raise RuntimeReadinessError("runtime_binary_not_detected blocker required when runtime is not detected")

    unknown_modes = set(result.get("allowed_target_modes", [])) - ALLOWED_TARGET_MODES
    if unknown_modes:
        raise RuntimeReadinessError(f"unsupported allowed_target_modes in result: {sorted(unknown_modes)}")
