from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter, registered_adapter_names
from models import load_json
from policy import load_default_vault_metadata
from gateway import run_mock_tool_gateway


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

    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)

    assert_true(result["execution_status"] == "completed", "allowed action should complete")
    assert_true(result["credential_resolved_by"] == "mock-vault", "credential should resolve through mock-vault")
    assert_true(result.get("_adapter_output", {}).get("adapter") == "zap", "allowed action should use zap adapter")
    assert_true(evidence["credential_ref_used"] == "test-account-001", "evidence should record credential_ref")

    print("Tool Gateway adapter tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
