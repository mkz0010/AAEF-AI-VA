from __future__ import annotations

from typing import Any

from controlled_executor import ControlledExecutorError, evaluate_command_plan


class RealExecutionReadinessError(ValueError):
    pass


REQUIRED_CONFIG_FIELDS = [
    "real_execution_enabled",
    "runtime_configured",
    "egress_profile_configured",
    "artifact_paths_private",
    "sanitizer_configured",
    "stop_timeout_configured",
    "evidence_emission_required",
    "target_binding_approved",
    "credential_injection_policy_configured",
    "human_approval_status",
]


def default_readiness_config() -> dict[str, Any]:
    return {
        "real_execution_enabled": False,
        "runtime_configured": False,
        "egress_profile_configured": False,
        "artifact_paths_private": True,
        "sanitizer_configured": False,
        "stop_timeout_configured": False,
        "evidence_emission_required": True,
        "target_binding_approved": False,
        "credential_injection_policy_configured": False,
        "human_approval_status": "not_requested",
        "real_tool_runtime": None,
        "network_egress_profile": None,
        "notes": "MVP default: real execution is disabled.",
    }


def _require_config_shape(config: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_CONFIG_FIELDS if field not in config]
    if missing:
        raise RealExecutionReadinessError(f"readiness config missing required fields: {missing}")

    if config.get("evidence_emission_required") is not True:
        raise RealExecutionReadinessError("evidence emission must be required for real execution readiness")

    if config.get("artifact_paths_private") is not True:
        raise RealExecutionReadinessError("artifact paths must be private/ignored")

    if config.get("human_approval_status") not in {"not_required", "approved", "not_requested", "required"}:
        raise RealExecutionReadinessError("unsupported human_approval_status")


def evaluate_real_execution_readiness(
    command_plan: dict[str, Any],
    readiness_config: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluate whether a command plan may move toward real execution.

    This function does not execute tools. It evaluates gate readiness only.
    """
    config = readiness_config if readiness_config is not None else default_readiness_config()
    _require_config_shape(config)

    # Reuse the current dry-run executor validation as the baseline plan safety check.
    try:
        dry_run_result = evaluate_command_plan(command_plan)
    except ControlledExecutorError as exc:
        raise RealExecutionReadinessError(f"command plan failed controlled executor validation: {exc}") from exc

    blockers: list[str] = []

    if config["real_execution_enabled"] is not True:
        blockers.append("real_execution_disabled")

    required_true_flags = [
        "runtime_configured",
        "egress_profile_configured",
        "artifact_paths_private",
        "sanitizer_configured",
        "stop_timeout_configured",
        "evidence_emission_required",
        "target_binding_approved",
        "credential_injection_policy_configured",
    ]

    for flag in required_true_flags:
        if config.get(flag) is not True:
            blockers.append(f"{flag}_not_ready")

    human_status = config.get("human_approval_status")
    if human_status not in {"not_required", "approved"}:
        blockers.append("human_approval_not_satisfied")

    # Current command plans are intentionally dry-run-only.
    # Even if all environmental readiness flags are true, the current MVP plan
    # cannot be executed until a future execution-mode transition is explicitly designed.
    if command_plan.get("execution_mode") == "dry_run_plan_only":
        blockers.append("command_plan_is_dry_run_only")

    return {
        "gate_result": "not_ready" if blockers else "ready_for_future_real_execution",
        "real_execution_permitted": False if blockers else True,
        "external_process_executed": False,
        "network_activity_performed": False,
        "command_plan_id": command_plan.get("plan_id"),
        "tool": command_plan.get("tool"),
        "operation": command_plan.get("operation"),
        "target_id": command_plan.get("target_id"),
        "scope_id": command_plan.get("scope_id"),
        "dry_run_executor_result": dry_run_result,
        "blockers": blockers,
    }
