from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from controlled_executor import ControlledExecutorError, evaluate_command_plan
from models import load_json


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_executor_error(command_plan: dict, message: str) -> None:
    try:
        evaluate_command_plan(command_plan)
    except ControlledExecutorError:
        return
    raise AssertionError(message)


def load_allowed_zap_plan() -> dict:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    decision = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
    adapter = get_adapter("zap")
    return adapter.build_command_plan(request, decision, "mock-vault")


def main() -> int:
    plan = load_allowed_zap_plan()
    result = evaluate_command_plan(plan)

    assert_true(result["executor_result"] == "accepted_for_dry_run_only", "plan should be accepted only for dry-run")
    assert_true(result["network_destination_ref"].startswith("scope-registry://"), "executor should use target ref")
    assert_true(result["external_process_executed"] is False, "executor must not execute external process")
    assert_true(result["network_activity_performed"] is False, "executor must not perform network activity")
    assert_true(result["secret_material_observed"] is False, "executor must not observe secret material")

    bad = copy.deepcopy(plan)
    bad["external_process_execution"] = True
    expect_executor_error(bad, "external_process_execution=true should fail closed")

    bad = copy.deepcopy(plan)
    bad["execution_mode"] = "execute"
    expect_executor_error(bad, "non-dry-run execution mode should fail closed")

    bad = copy.deepcopy(plan)
    bad["secret_material_included"] = True
    expect_executor_error(bad, "secret material in command plan should fail closed")

    bad = copy.deepcopy(plan)
    bad["approved_constraints"]["destructive_tests"] = True
    expect_executor_error(bad, "destructive tests should fail closed")

    bad = copy.deepcopy(plan)
    bad["approved_constraints"]["external_discovery"] = True
    expect_executor_error(bad, "external discovery should fail closed")

    bad = copy.deepcopy(plan)
    bad["shell_command"] = "zap.sh -cmd -quickurl https://example.invalid"
    expect_executor_error(bad, "shell command field should fail closed")

    bad = copy.deepcopy(plan)
    bad["target_url"] = "https://example.invalid"
    expect_executor_error(bad, "raw target URL should fail closed")

    bad = copy.deepcopy(plan)
    bad["target_binding"]["raw_destination_included"] = True
    expect_executor_error(bad, "raw destination in target binding should fail closed")

    bad = copy.deepcopy(plan)
    bad["target_binding"]["network_execution_allowed"] = True
    expect_executor_error(bad, "network execution allowed should fail closed in dry-run MVP")

    bad = copy.deepcopy(plan)
    bad["artifact_refs"]["raw_artifact_ref"] = "tracked/raw.json"
    expect_executor_error(bad, "tracked raw artifact path should fail closed")

    print("Controlled executor policy tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
