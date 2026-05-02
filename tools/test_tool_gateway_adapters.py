from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter, registered_adapter_names
from gateway import run_mock_tool_gateway
from models import load_json
from policy import load_default_vault_metadata


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    names = registered_adapter_names()
    assert_true(names == ["browser", "nmap", "nuclei", "zap"], f"unexpected adapters: {names}")

    for name in names:
        adapter = get_adapter(name)
        assert_true(adapter.tool_name == name, f"adapter tool_name mismatch for {name}")

    example_dir = TGW / "examples"
    request = load_json(example_dir / "allowed-action.tool-action-request.json")
    decision = load_json(example_dir / "allowed-action.authorization-decision.json")
    vault_metadata = load_default_vault_metadata()

    zap_adapter = get_adapter("zap")
    command_plan = zap_adapter.build_command_plan(request, decision, "mock-vault")

    assert_true(command_plan["execution_mode"] == "dry_run_plan_only", "ZAP command plan must be dry-run only")
    assert_true(command_plan["external_process_execution"] is False, "ZAP plan must not execute external process")
    assert_true(command_plan["secret_material_included"] is False, "ZAP plan must not include secret material")
    assert_true(command_plan["credential_ref"] == "test-account-001", "ZAP plan should reference credential_ref")
    assert_true("artifact_refs" in command_plan, "ZAP plan should include artifact refs")
    assert_true("raw_artifact_ref" in command_plan["artifact_refs"], "ZAP plan should include raw artifact ref")
    assert_true("sanitized_artifact_ref" in command_plan["artifact_refs"], "ZAP plan should include sanitized artifact ref")

    adapter_output = zap_adapter.execute(request, decision, "mock-vault")
    assert_true(adapter_output["adapter"] == "zap", "direct adapter output should identify zap")
    assert_true(adapter_output["mock_execution"] is True, "adapter output should be marked mock")
    assert_true(adapter_output["command_plan"]["execution_mode"] == "dry_run_plan_only", "adapter output should include dry-run plan")

    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)

    assert_true(result["execution_status"] == "completed", "allowed action should complete")
    assert_true(result["credential_resolved_by"] == "mock-vault", "credential should resolve through mock-vault")
    assert_true("_adapter_output" not in result, "adapter output must not be included in public result")
    assert_true(evidence["credential_ref_used"] == "test-account-001", "evidence should record credential_ref")

    print("Tool Gateway adapter tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
