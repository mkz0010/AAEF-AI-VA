from __future__ import annotations

from urllib.parse import urlparse
from typing import Any


class LocalTargetLabError(ValueError):
    pass


ALLOWED_TARGET_MODES = {
    "localhost_only",
    "docker_internal_only",
    "intentionally_vulnerable_lab_only",
}


REQUIRED_PROFILE_FIELDS = [
    "lab_profile_id",
    "lab_profile_status",
    "target_mode",
    "target_id",
    "scope_id",
    "target_label",
    "target_url",
    "target_kind",
    "intentionally_vulnerable",
    "customer_target",
    "external_network_target",
    "scope_registry_binding_required",
    "runtime_readiness_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "credential_injection_allowed",
    "raw_artifact_capture_allowed",
    "human_approval_required_for_execution_transition",
    "allowed_tools",
    "allowed_operations",
    "prohibited_operations",
    "lab_notes",
]


REQUIRED_GATE_FIELDS = [
    "target_lab_gate_type",
    "target_lab_gate_status",
    "lab_profile_id",
    "target_id",
    "scope_id",
    "target_url",
    "target_mode",
    "target_kind",
    "target_allowed_for_future_runtime_transition",
    "customer_target",
    "external_network_target",
    "intentionally_vulnerable",
    "scope_registry_binding_required",
    "runtime_readiness_required",
    "scan_execution_allowed",
    "network_activity_allowed",
    "credential_injection_allowed",
    "raw_artifact_capture_allowed",
    "blockers",
    "next_actions",
]


def _host_from_url(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise LocalTargetLabError("target_url must use http or https for the current MVP")

    if not parsed.hostname:
        raise LocalTargetLabError("target_url must include a hostname")

    return parsed.hostname.lower()


def _is_localhost(host: str) -> bool:
    return host in {"localhost", "127.0.0.1", "::1"}


def _is_docker_internal(host: str) -> bool:
    allowed = {
        "juice-shop",
        "webgoat",
        "dvwa",
        "vulnapp",
        "target",
        "target.local",
        "host.docker.internal",
    }
    return host in allowed or host.endswith(".docker.internal")


def build_local_target_lab_profile(
    *,
    lab_profile_id: str = "local-target-lab-mvp",
    target_mode: str = "localhost_only",
    target_id: str = "local-lab-target-001",
    scope_id: str = "scope-local-lab-001",
    target_label: str = "Local intentionally vulnerable lab target",
    target_url: str = "http://127.0.0.1:3000",
    target_kind: str = "web_application",
) -> dict[str, Any]:
    profile = {
        "lab_profile_id": lab_profile_id,
        "lab_profile_status": "target_defined_execution_blocked",
        "target_mode": target_mode,
        "target_id": target_id,
        "scope_id": scope_id,
        "target_label": target_label,
        "target_url": target_url,
        "target_kind": target_kind,
        "intentionally_vulnerable": True,
        "customer_target": False,
        "external_network_target": False,
        "scope_registry_binding_required": True,
        "runtime_readiness_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "credential_injection_allowed": False,
        "raw_artifact_capture_allowed": False,
        "human_approval_required_for_execution_transition": True,
        "allowed_tools": ["zap"],
        "allowed_operations": [
            "runtime_detection",
            "target_profile_validation",
        ],
        "prohibited_operations": [
            "active_scan",
            "spider",
            "ajax_spider",
            "authenticated_crawl",
            "passive_scan_runtime_collection",
            "external_network_access",
            "customer_target_access",
            "credential_injection",
            "raw_artifact_capture",
        ],
        "lab_notes": (
            "This local lab profile defines an allowed future test target boundary only. "
            "It does not allow scans, network activity, credential injection, or raw artifact capture."
        ),
    }

    validate_local_target_lab_profile(profile)
    return profile


def validate_local_target_lab_profile(profile: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_PROFILE_FIELDS if field not in profile]
    if missing:
        raise LocalTargetLabError(f"local target lab profile missing required fields: {missing}")

    if profile.get("lab_profile_status") != "target_defined_execution_blocked":
        raise LocalTargetLabError("lab_profile_status must be target_defined_execution_blocked")

    if profile.get("target_mode") not in ALLOWED_TARGET_MODES:
        raise LocalTargetLabError(f"unsupported target_mode: {profile.get('target_mode')}")

    host = _host_from_url(profile["target_url"])

    if profile["target_mode"] == "localhost_only" and not _is_localhost(host):
        raise LocalTargetLabError("localhost_only target_mode requires localhost, 127.0.0.1, or ::1")

    if profile["target_mode"] == "docker_internal_only" and not _is_docker_internal(host):
        raise LocalTargetLabError("docker_internal_only target_mode requires an approved docker-internal host")

    if profile["target_mode"] == "intentionally_vulnerable_lab_only":
        if not (_is_localhost(host) or _is_docker_internal(host)):
            raise LocalTargetLabError("intentionally_vulnerable_lab_only target must remain local or docker-internal")

    if profile.get("intentionally_vulnerable") is not True:
        raise LocalTargetLabError("local lab target must be intentionally_vulnerable=true")

    if profile.get("customer_target") is not False:
        raise LocalTargetLabError("customer_target must be false in current MVP")

    if profile.get("external_network_target") is not False:
        raise LocalTargetLabError("external_network_target must be false in current MVP")

    for field in [
        "scope_registry_binding_required",
        "runtime_readiness_required",
        "human_approval_required_for_execution_transition",
    ]:
        if profile.get(field) is not True:
            raise LocalTargetLabError(f"{field} must be true")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "credential_injection_allowed",
        "raw_artifact_capture_allowed",
    ]:
        if profile.get(field) is not False:
            raise LocalTargetLabError(f"{field} must be false in current MVP")

    if "zap" not in profile.get("allowed_tools", []):
        raise LocalTargetLabError("allowed_tools must include zap for current MVP")

    prohibited = set(profile.get("prohibited_operations", []))
    required_prohibited = {
        "active_scan",
        "spider",
        "ajax_spider",
        "authenticated_crawl",
        "external_network_access",
        "customer_target_access",
        "credential_injection",
        "raw_artifact_capture",
    }
    missing_prohibited = required_prohibited - prohibited
    if missing_prohibited:
        raise LocalTargetLabError(f"missing prohibited operations: {sorted(missing_prohibited)}")


def evaluate_local_target_lab_gate(profile: dict[str, Any]) -> dict[str, Any]:
    validate_local_target_lab_profile(profile)

    blockers = [
        "scan_execution_disabled",
        "network_activity_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "bounded_execution_transition_not_defined",
        "runtime_execution_not_authorized",
    ]

    result = {
        "target_lab_gate_type": "local_target_lab_profile_gate",
        "target_lab_gate_status": "target_defined_execution_blocked",
        "lab_profile_id": profile["lab_profile_id"],
        "target_id": profile["target_id"],
        "scope_id": profile["scope_id"],
        "target_url": profile["target_url"],
        "target_mode": profile["target_mode"],
        "target_kind": profile["target_kind"],
        "target_allowed_for_future_runtime_transition": True,
        "customer_target": False,
        "external_network_target": False,
        "intentionally_vulnerable": True,
        "scope_registry_binding_required": True,
        "runtime_readiness_required": True,
        "scan_execution_allowed": False,
        "network_activity_allowed": False,
        "credential_injection_allowed": False,
        "raw_artifact_capture_allowed": False,
        "blockers": blockers,
        "next_actions": [
            {
                "blocker": "scan_execution_disabled",
                "next_action": "Keep scans disabled until bounded local execution transition is explicitly defined.",
            },
            {
                "blocker": "network_activity_disabled",
                "next_action": "Do not perform network activity even against localhost in this phase.",
            },
            {
                "blocker": "bounded_execution_transition_not_defined",
                "next_action": "Define a future transition gate before local-only ZAP execution can be attempted.",
            },
            {
                "blocker": "runtime_execution_not_authorized",
                "next_action": "Require runtime readiness, scope binding, and human approval before any future execution transition.",
            },
        ],
    }

    validate_local_target_lab_gate_result(result)
    return result


def validate_local_target_lab_gate_result(result: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_GATE_FIELDS if field not in result]
    if missing:
        raise LocalTargetLabError(f"local target lab gate result missing required fields: {missing}")

    if result.get("target_lab_gate_status") != "target_defined_execution_blocked":
        raise LocalTargetLabError("target_lab_gate_status must be target_defined_execution_blocked")

    if result.get("target_allowed_for_future_runtime_transition") is not True:
        raise LocalTargetLabError("target_allowed_for_future_runtime_transition must be true for valid local lab targets")

    if result.get("customer_target") is not False:
        raise LocalTargetLabError("customer_target must be false")

    if result.get("external_network_target") is not False:
        raise LocalTargetLabError("external_network_target must be false")

    if result.get("intentionally_vulnerable") is not True:
        raise LocalTargetLabError("intentionally_vulnerable must be true")

    for field in [
        "scope_registry_binding_required",
        "runtime_readiness_required",
    ]:
        if result.get(field) is not True:
            raise LocalTargetLabError(f"{field} must be true")

    for field in [
        "scan_execution_allowed",
        "network_activity_allowed",
        "credential_injection_allowed",
        "raw_artifact_capture_allowed",
    ]:
        if result.get(field) is not False:
            raise LocalTargetLabError(f"{field} must be false")

    required_blockers = {
        "scan_execution_disabled",
        "network_activity_disabled",
        "credential_injection_disabled",
        "raw_artifact_capture_disabled",
        "bounded_execution_transition_not_defined",
        "runtime_execution_not_authorized",
    }
    missing_blockers = required_blockers - set(result.get("blockers", []))
    if missing_blockers:
        raise LocalTargetLabError(f"local target lab gate missing blockers: {sorted(missing_blockers)}")
