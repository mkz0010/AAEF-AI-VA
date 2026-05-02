from __future__ import annotations

import copy
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO = Path(__file__).resolve().parents[1]
TOOL_GATEWAY_DIR = REPO / "prototypes" / "tool-gateway"
EXAMPLE_DIR = TOOL_GATEWAY_DIR / "examples"
TEST_OUT_DIR = REPO / "private-not-in-git" / "test-runs" / "tool-gateway-runner"

if str(TOOL_GATEWAY_DIR) not in sys.path:
    sys.path.insert(0, str(TOOL_GATEWAY_DIR))

from gateway import run_mock_tool_gateway
from models import load_json
from policy import PolicyError


def load_example(name: str, kind: str) -> dict[str, Any]:
    return load_json(EXAMPLE_DIR / f"{name}.{kind}.json")


def load_vault_metadata() -> dict[str, Any]:
    return load_json(TOOL_GATEWAY_DIR / "mock_vault" / "metadata.json")


def expect_policy_error(label: str, request: dict[str, Any], decision: dict[str, Any], vault_metadata: dict[str, Any] | None = None) -> None:
    try:
        run_mock_tool_gateway(request, decision, vault_metadata=vault_metadata)
    except PolicyError:
        return
    raise AssertionError(f"Expected PolicyError for {label}")


def test_positive_scenarios() -> None:
    vault_metadata = load_vault_metadata()

    allowed_req = load_example("allowed-action", "tool-action-request")
    allowed_dec = load_example("allowed-action", "authorization-decision")
    result, evidence = run_mock_tool_gateway(allowed_req, allowed_dec, vault_metadata=vault_metadata)
    assert result["execution_status"] == "completed"
    assert result["credential_ref_used"] == "test-account-001"
    assert result["credential_resolved_by"] == "mock-vault"
    assert result["secret_exposed_to_ai"] is False
    assert evidence["credential_ref_used"] == "test-account-001"

    denied_req = load_example("denied-action", "tool-action-request")
    denied_dec = load_example("denied-action", "authorization-decision")
    result, evidence = run_mock_tool_gateway(denied_req, denied_dec, vault_metadata=vault_metadata)
    assert result["execution_status"] == "blocked"
    assert result["credential_ref_used"] is None
    assert result["secret_exposed_to_ai"] is False
    assert evidence["human_review_status"] == "not_required"

    human_req = load_example("human-approval-required", "tool-action-request")
    human_dec = load_example("human-approval-required", "authorization-decision")
    result, evidence = run_mock_tool_gateway(human_req, human_dec, vault_metadata=vault_metadata)
    assert result["execution_status"] == "requires_human_approval"
    assert result["credential_ref_used"] is None
    assert result["secret_exposed_to_ai"] is False
    assert evidence["human_review_status"] == "pending"

    print("PASS: positive scenarios")


def test_negative_fail_closed_scenarios() -> None:
    vault_metadata = load_vault_metadata()
    request = load_example("allowed-action", "tool-action-request")
    decision = load_example("allowed-action", "authorization-decision")

    mutated_request = copy.deepcopy(request)
    mutated_request["target_id"] = "webapp-other"
    expect_policy_error("target_id mismatch", mutated_request, decision, vault_metadata)

    mutated_request = copy.deepcopy(request)
    mutated_request["operation"] = "passive_scan"
    expect_policy_error("operation mismatch", mutated_request, decision, vault_metadata)

    mutated_decision = copy.deepcopy(decision)
    mutated_decision["credential_ref"] = "test-account-other"
    expect_policy_error("credential_ref mismatch", request, mutated_decision, vault_metadata)

    mutated_decision = copy.deepcopy(decision)
    mutated_decision["constraints"]["destructive_tests"] = True
    expect_policy_error("destructive_tests true", request, mutated_decision, vault_metadata)

    mutated_decision = copy.deepcopy(decision)
    mutated_decision["evidence_required"] = False
    expect_policy_error("evidence_required false", request, mutated_decision, vault_metadata)

    print("PASS: negative fail-closed scenarios")


def test_credential_ref_vault_metadata_negative_scenarios() -> None:
    request = load_example("allowed-action", "tool-action-request")
    decision = load_example("allowed-action", "authorization-decision")
    vault_metadata = load_vault_metadata()

    expect_policy_error("missing vault metadata", request, decision, None)

    mutated_request = copy.deepcopy(request)
    mutated_decision = copy.deepcopy(decision)
    mutated_request["credential_ref"] = "missing-account-001"
    mutated_decision["credential_ref"] = "missing-account-001"
    expect_policy_error("credential_ref not found", mutated_request, mutated_decision, vault_metadata)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["target_id"] = "webapp-other"
    expect_policy_error("vault target mismatch", request, decision, bad_vault)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["scope_id"] = "scope-other"
    expect_policy_error("vault scope mismatch", request, decision, bad_vault)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["allowed_tools"] = ["browser"]
    expect_policy_error("vault tool not allowed", request, decision, bad_vault)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["allowed_operations"] = ["safe_login_check"]
    expect_policy_error("vault operation not allowed", request, decision, bad_vault)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["revoked"] = True
    expect_policy_error("vault credential revoked", request, decision, bad_vault)

    bad_vault = copy.deepcopy(vault_metadata)
    bad_vault["credential_refs"][0]["expires_at"] = "2026-05-02T09:59:59Z"
    expect_policy_error("vault credential expired", request, decision, bad_vault)

    print("PASS: credential_ref mock Vault metadata negative scenarios")


def test_generated_runner_outputs() -> None:
    if TEST_OUT_DIR.exists():
        shutil.rmtree(TEST_OUT_DIR)

    subprocess.run(
        [
            sys.executable,
            str(REPO / "tools" / "run_tool_gateway_example.py"),
            "all",
            "--out-dir",
            str(TEST_OUT_DIR),
        ],
        check=True,
        cwd=REPO,
    )

    expected = {
        "allowed-action": "completed",
        "denied-action": "blocked",
        "human-approval-required": "requires_human_approval",
    }

    for scenario, status in expected.items():
        result_path = TEST_OUT_DIR / scenario / "tool-execution-result.generated.json"
        evidence_path = TEST_OUT_DIR / scenario / "evidence-record.generated.json"
        assert result_path.exists(), result_path
        assert evidence_path.exists(), evidence_path

        result = load_json(result_path)
        evidence = load_json(evidence_path)

        assert result["execution_status"] == status
        assert result["secret_exposed_to_ai"] is False
        assert evidence["secret_exposed_to_ai"] is False
        assert result["tool_action_request_id"] == evidence["tool_action_request_id"]
        assert result["authorization_decision_id"] == evidence["authorization_decision_id"]

    print("PASS: generated runner outputs")


def main() -> int:
    test_positive_scenarios()
    test_negative_fail_closed_scenarios()
    test_credential_ref_vault_metadata_negative_scenarios()
    test_generated_runner_outputs()
    print("Tool Gateway runner tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
