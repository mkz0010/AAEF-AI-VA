from __future__ import annotations

from typing import Any

from scope_registry import validate_command_plan_target_binding


class ControlledExecutorError(ValueError):
    pass


REQUIRED_PLAN_FIELDS = [
    "plan_id",
    "execution_mode",
    "external_process_execution",
    "adapter",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "target_binding",
    "secret_material_included",
    "approved_constraints",
    "artifact_refs",
]


FORBIDDEN_PLAN_FIELDS = {
    "username",
    "password",
    "api_key",
    "secret",
    "secret_key",
    "cookie",
    "authorization",
    "bearer_token",
    "zap_api_key",
    "shell_command",
    "command",
    "argv",
    "target_url",
    "target_uri",
    "ip_address",
    "host",
}


def validate_command_plan_for_dry_run(command_plan: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_PLAN_FIELDS if field not in command_plan]
    if missing:
        raise ControlledExecutorError(f"command plan missing required fields: {missing}")

    for field in FORBIDDEN_PLAN_FIELDS:
        if field in command_plan:
            raise ControlledExecutorError(f"command plan contains forbidden field: {field}")

    if command_plan["execution_mode"] != "dry_run_plan_only":
        raise ControlledExecutorError("only dry_run_plan_only execution_mode is allowed in MVP")

    if command_plan["external_process_execution"] is not False:
        raise ControlledExecutorError("external_process_execution must be false in MVP")

    if command_plan["secret_material_included"] is not False:
        raise ControlledExecutorError("secret_material_included must be false")

    constraints = command_plan.get("approved_constraints", {})
    if constraints.get("destructive_tests") is True:
        raise ControlledExecutorError("destructive_tests must not be true")

    if constraints.get("external_discovery") is True:
        raise ControlledExecutorError("external_discovery must not be true for current MVP executor")

    artifact_refs = command_plan.get("artifact_refs", {})
    for ref_name in ["raw_artifact_ref", "sanitized_artifact_ref"]:
        if ref_name not in artifact_refs:
            raise ControlledExecutorError(f"command plan missing artifact ref: {ref_name}")
        ref_value = artifact_refs[ref_name]
        if not isinstance(ref_value, str) or not ref_value.startswith("private-not-in-git/"):
            raise ControlledExecutorError(f"{ref_name} must point to ignored private path")

    try:
        validate_command_plan_target_binding(command_plan)
    except Exception as exc:
        raise ControlledExecutorError(f"target binding validation failed: {exc}") from exc


def evaluate_command_plan(command_plan: dict[str, Any]) -> dict[str, Any]:
    validate_command_plan_for_dry_run(command_plan)

    return {
        "executor_result": "accepted_for_dry_run_only",
        "plan_id": command_plan["plan_id"],
        "tool": command_plan["tool"],
        "operation": command_plan["operation"],
        "target_id": command_plan["target_id"],
        "scope_id": command_plan["scope_id"],
        "network_destination_ref": command_plan["target_binding"]["network_destination_ref"],
        "external_process_executed": False,
        "network_activity_performed": False,
        "secret_material_observed": False,
        "raw_artifact_ref": command_plan["artifact_refs"]["raw_artifact_ref"],
        "sanitized_artifact_ref": command_plan["artifact_refs"]["sanitized_artifact_ref"],
    }
