from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from models import load_json
from real_execution_gate import (
    RealExecutionReadinessError,
    default_readiness_config,
    evaluate_real_execution_readiness,
)


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_readiness_error(command_plan: dict, config: dict, message: str) -> None:
    try:
        evaluate_real_execution_readiness(command_plan, config)
    except RealExecutionReadinessError:
        return
    raise AssertionError(message)


def load_allowed_zap_plan() -> dict:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    decision = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
    adapter = get_adapter("zap")
    return adapter.build_command_plan(request, decision, "mock-vault")


def main() -> int:
    plan = load_allowed_zap_plan()

    default_result = evaluate_real_execution_readiness(plan)
    assert_true(default_result["gate_result"] == "not_ready", "default MVP gate should not be ready")
    assert_true(default_result["real_execution_permitted"] is False, "real execution must not be permitted by default")
    assert_true("real_execution_disabled" in default_result["blockers"], "default gate should block real execution")
    assert_true("command_plan_is_dry_run_only" in default_result["blockers"], "dry-run plan should block real execution")

    config = default_readiness_config()
    config.update(
        {
            "real_execution_enabled": True,
            "runtime_configured": True,
            "egress_profile_configured": True,
            "artifact_paths_private": True,
            "sanitizer_configured": True,
            "stop_timeout_configured": True,
            "evidence_emission_required": True,
            "target_binding_approved": True,
            "credential_injection_policy_configured": True,
            "human_approval_status": "approved",
            "real_tool_runtime": "zap-runtime-demo",
            "network_egress_profile": "egress-dry-run-demo",
        }
    )
    future_result = evaluate_real_execution_readiness(plan, config)
    assert_true(future_result["gate_result"] == "not_ready", "dry-run command plan should still not permit real execution")
    assert_true(future_result["real_execution_permitted"] is False, "dry-run command plan must keep real execution disabled")
    assert_true("command_plan_is_dry_run_only" in future_result["blockers"], "dry-run blocker should remain")

    bad_config = copy.deepcopy(config)
    bad_config["evidence_emission_required"] = False
    expect_readiness_error(plan, bad_config, "evidence emission disabled should fail closed")

    bad_config = copy.deepcopy(config)
    bad_config["artifact_paths_private"] = False
    expect_readiness_error(plan, bad_config, "public artifact paths should fail closed")

    bad_config = copy.deepcopy(config)
    bad_config["human_approval_status"] = "unknown"
    expect_readiness_error(plan, bad_config, "unknown human approval status should fail closed")

    bad_plan = copy.deepcopy(plan)
    bad_plan["shell_command"] = "zap.sh -cmd -quickurl https://example.invalid"
    expect_readiness_error(bad_plan, config, "unsafe command plan should fail readiness gate")

    print("Real execution readiness gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
