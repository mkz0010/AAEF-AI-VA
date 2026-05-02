from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class ScopeRegistryError(ValueError):
    pass


DEFAULT_SCOPE_REGISTRY_PATH = Path("prototypes/tool-gateway/scope_registry/registry.json")


def load_default_scope_registry() -> dict[str, Any]:
    return json.loads(DEFAULT_SCOPE_REGISTRY_PATH.read_text(encoding="utf-8"))


def _get_target(registry: dict[str, Any], target_id: str) -> dict[str, Any]:
    targets = registry.get("targets", {})
    if target_id not in targets:
        raise ScopeRegistryError(f"target_id is not registered: {target_id}")
    target = targets[target_id]
    if not isinstance(target, dict):
        raise ScopeRegistryError(f"target registry entry must be an object: {target_id}")
    return target


def resolve_target_binding(
    target_id: str,
    scope_id: str,
    tool: str,
    operation: str,
    registry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    registry_data = registry if registry is not None else load_default_scope_registry()
    target = _get_target(registry_data, target_id)

    if target.get("approval_status") != "approved":
        raise ScopeRegistryError(f"target is not approved: {target_id}")

    if scope_id not in target.get("scope_ids", []):
        raise ScopeRegistryError(
            f"target_id {target_id!r} is not bound to scope_id {scope_id!r}"
        )

    allowed_tools = target.get("allowed_tools", [])
    if tool not in allowed_tools:
        raise ScopeRegistryError(f"target_id {target_id!r} does not allow tool {tool!r}")

    allowed_operations = target.get("allowed_operations", [])
    if operation not in allowed_operations:
        raise ScopeRegistryError(
            f"target_id {target_id!r} does not allow operation {operation!r}"
        )

    if target.get("raw_destination_included") is True:
        raise ScopeRegistryError(f"target registry entry exposes raw destination: {target_id}")

    return {
        "target_id": target_id,
        "scope_id": scope_id,
        "target_type": target.get("target_type"),
        "environment": target.get("environment"),
        "approval_status": target.get("approval_status"),
        "approved_for_tool": True,
        "approved_operation": operation,
        "network_destination_ref": target.get("network_destination_ref"),
        "raw_destination_included": False,
        "network_execution_allowed": target.get("network_execution_allowed", False),
        "egress_profile": target.get("egress_profile"),
        "notes": target.get("notes", ""),
    }


def validate_command_plan_target_binding(command_plan: dict[str, Any]) -> None:
    target_binding = command_plan.get("target_binding")
    if not isinstance(target_binding, dict):
        raise ScopeRegistryError("command plan missing target_binding")

    if target_binding.get("target_id") != command_plan.get("target_id"):
        raise ScopeRegistryError("target_binding target_id does not match command plan")

    if target_binding.get("scope_id") != command_plan.get("scope_id"):
        raise ScopeRegistryError("target_binding scope_id does not match command plan")

    if target_binding.get("approved_for_tool") is not True:
        raise ScopeRegistryError("target_binding is not approved for tool")

    if target_binding.get("raw_destination_included") is not False:
        raise ScopeRegistryError("target_binding must not include raw destination")

    destination_ref = target_binding.get("network_destination_ref")
    if not isinstance(destination_ref, str) or not destination_ref.startswith("scope-registry://"):
        raise ScopeRegistryError("target_binding must use scope-registry destination reference")

    if target_binding.get("network_execution_allowed") is not False:
        raise ScopeRegistryError("network execution is not allowed in current dry-run MVP")
