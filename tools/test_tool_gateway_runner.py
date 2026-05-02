from __future__ import annotations

import copy
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from gateway import run_mock_tool_gateway
from models import load_json
from policy import PolicyError, load_default_vault_metadata


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_pair(prefix: str) -> tuple[dict, dict]:
    request = load_json(EXAMPLE_DIR / f"{prefix}.tool-action-request.json")
    decision = load_json(EXAMPLE_DIR / f"{prefix}.authorization-decision.json")
    return request, decision


def expect_policy_error(request: dict, decision: dict, message: str) -> None:
    try:
        run_mock_tool_gateway(request, decision, vault_metadata=load_default_vault_metadata())
    except PolicyError:
        return
    raise AssertionError(message)


def expect_policy_error_with_metadata(
    request: dict,
    decision: dict,
    vault_metadata: dict,
    message: str,
) -> None:
    try:
        run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)
    except PolicyError:
        return
    raise AssertionError(message)


def test_positive_scenarios() -> None:
    vault_metadata = load_default_vault_metadata()

    request, decision = load_pair("allowed-action")
    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)
    assert_true(result["execution_status"] == "completed", "allowed action should complete")
    assert_true(result["credential_ref_used"] == "test-account-001", "credential_ref should be used")
    assert_true(result["credential_resolved_by"] == "mock-vault", "credential should resolve through mock-vault")
    assert_true(result["secret_exposed_to_ai"] is False, "secret must not be exposed")
    assert_true("_adapter_output" not in result, "adapter output must not be included in public result")
    assert_true(evidence["human_review_status"] == "pending", "allowed evidence should await review")

    request, decision = load_pair("denied-action")
    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)
    assert_true(result["execution_status"] == "blocked", "denied action should be blocked")
    assert_true(result["credential_ref_used"] is None, "denied action should not use credential")
    assert_true(evidence["human_review_status"] == "not_required", "denied evidence should not require review")

    request, decision = load_pair("human-approval-required")
    result, evidence = run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)
    assert_true(result["execution_status"] == "requires_human_approval", "human-gated action should pause")
    assert_true(result["credential_ref_used"] is None, "human-gated action should not use credential")
    assert_true(evidence["human_review_status"] == "pending", "human-gated evidence should be pending")


def test_negative_binding_scenarios() -> None:
    request, decision = load_pair("allowed-action")

    bad = copy.deepcopy(decision)
    bad["target_id"] = "other-target"
    expect_policy_error(request, bad, "target_id mismatch should fail closed")

    bad = copy.deepcopy(decision)
    bad["operation"] = "passive_scan"
    expect_policy_error(request, bad, "operation mismatch should fail closed")

    bad = copy.deepcopy(decision)
    bad["credential_ref"] = "other-credential-ref"
    expect_policy_error(request, bad, "credential_ref mismatch should fail closed")

    bad = copy.deepcopy(decision)
    bad["constraints"]["destructive_tests"] = True
    expect_policy_error(request, bad, "destructive_tests=true should fail closed")

    bad = copy.deepcopy(decision)
    bad["evidence_required"] = False
    expect_policy_error(request, bad, "evidence_required=false should fail closed")


def test_negative_vault_metadata_scenarios() -> None:
    request, decision = load_pair("allowed-action")
    base = load_default_vault_metadata()

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["target_id"] = "other-target"
    expect_policy_error_with_metadata(request, decision, bad, "vault target mismatch should fail closed")

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["scope_id"] = "other-scope"
    expect_policy_error_with_metadata(request, decision, bad, "vault scope mismatch should fail closed")

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["allowed_tools"] = ["browser"]
    expect_policy_error_with_metadata(request, decision, bad, "vault allowed_tools mismatch should fail closed")

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["allowed_operations"] = ["safe_login_check"]
    expect_policy_error_with_metadata(request, decision, bad, "vault allowed_operations mismatch should fail closed")

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["revoked"] = True
    expect_policy_error_with_metadata(request, decision, bad, "revoked credential_ref should fail closed")

    bad = copy.deepcopy(base)
    bad["credential_refs"]["test-account-001"]["expires_at"] = "2000-01-01T00:00:00Z"
    expect_policy_error_with_metadata(request, decision, bad, "expired credential_ref should fail closed")


def test_generated_runner_outputs() -> None:
    out_dir = ROOT / "private-not-in-git" / "test-runs" / "tool-gateway-runner"
    cmd = [
        sys.executable,
        str(ROOT / "tools" / "run_tool_gateway_example.py"),
        "all",
        "--out-dir",
        str(out_dir),
    ]
    subprocess.run(cmd, check=True)

    expected = {
        "allowed-action": "completed",
        "denied-action": "blocked",
        "human-approval-required": "requires_human_approval",
    }

    for scenario, status in expected.items():
        result = load_json(out_dir / scenario / "tool-execution-result.generated.json")
        evidence = load_json(out_dir / scenario / "evidence-record.generated.json")
        assert_true(result["execution_status"] == status, f"{scenario} status mismatch")
        assert_true(result["secret_exposed_to_ai"] is False, f"{scenario} secret exposure flag mismatch")
        assert_true("_adapter_output" not in result, f"{scenario} must not expose adapter output in result")
        assert_true(evidence["secret_exposed_to_ai"] is False, f"{scenario} evidence secret flag mismatch")


def main() -> int:
    test_positive_scenarios()
    print("PASS: positive scenarios")

    test_negative_binding_scenarios()
    print("PASS: negative fail-closed scenarios")

    test_negative_vault_metadata_scenarios()
    print("PASS: credential_ref mock Vault metadata negative scenarios")

    test_generated_runner_outputs()
    print("PASS: generated runner outputs")

    print("Tool Gateway runner tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
