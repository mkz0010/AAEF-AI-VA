from __future__ import annotations

import json
import runpy
import shutil
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TOOL_GATEWAY_DIR = ROOT / "prototypes" / "tool-gateway"

if str(TOOL_GATEWAY_DIR) not in sys.path:
    sys.path.insert(0, str(TOOL_GATEWAY_DIR))

from gateway import run_mock_tool_gateway
from models import load_json
from policy import PolicyError


EXAMPLE_DIR = TOOL_GATEWAY_DIR / "examples"
TEST_OUTPUT_DIR = ROOT / "private-not-in-git" / "test-runs" / "tool-gateway-runner"

SCENARIOS = {
    "allowed-action": {
        "request": EXAMPLE_DIR / "allowed-action.tool-action-request.json",
        "decision": EXAMPLE_DIR / "allowed-action.authorization-decision.json",
        "expected_status": "completed",
    },
    "denied-action": {
        "request": EXAMPLE_DIR / "denied-action.tool-action-request.json",
        "decision": EXAMPLE_DIR / "denied-action.authorization-decision.json",
        "expected_status": "blocked",
    },
    "human-approval-required": {
        "request": EXAMPLE_DIR / "human-approval-required.tool-action-request.json",
        "decision": EXAMPLE_DIR / "human-approval-required.authorization-decision.json",
        "expected_status": "requires_human_approval",
    },
}


def fail(message: str) -> None:
    raise AssertionError(message)


def assert_equal(actual: Any, expected: Any, label: str) -> None:
    if actual != expected:
        fail(f"{label}: expected {expected!r}, got {actual!r}")


def assert_false(value: Any, label: str) -> None:
    if value is not False:
        fail(f"{label}: expected false, got {value!r}")


def require_policy_error(label: str, request: dict[str, Any], decision: dict[str, Any]) -> None:
    try:
        run_mock_tool_gateway(request, decision)
    except PolicyError:
        return
    fail(f"{label}: expected PolicyError")


def load_pair(scenario: str) -> tuple[dict[str, Any], dict[str, Any]]:
    spec = SCENARIOS[scenario]
    return load_json(spec["request"]), load_json(spec["decision"])


def validate_positive_scenarios() -> None:
    for name, spec in SCENARIOS.items():
        request, decision = load_pair(name)
        result, evidence = run_mock_tool_gateway(request, decision)

        assert_equal(result["execution_status"], spec["expected_status"], f"{name} status")
        assert_equal(evidence["tool_execution_id"], result["tool_execution_id"], f"{name} evidence execution link")
        assert_equal(evidence["tool_action_request_id"], request["tool_action_request_id"], f"{name} evidence request link")
        assert_equal(evidence["authorization_decision_id"], decision["authorization_decision_id"], f"{name} evidence authz link")
        assert_false(result["secret_exposed_to_ai"], f"{name} result secret exposure")
        assert_false(evidence["secret_exposed_to_ai"], f"{name} evidence secret exposure")

        if name == "allowed-action":
            assert_equal(result["credential_ref_used"], "test-account-001", f"{name} credential_ref")
            assert_equal(result["credential_resolved_by"], "mock-vault", f"{name} credential resolver")
            assert_equal(evidence["sanitization_status"], "completed", f"{name} sanitization")
        elif name == "denied-action":
            assert_equal(result["credential_ref_used"], None, f"{name} credential_ref")
            assert_equal(evidence["human_review_status"], "not_required", f"{name} human review")
        elif name == "human-approval-required":
            assert_equal(result["credential_ref_used"], None, f"{name} credential_ref")
            assert_equal(evidence["human_review_status"], "pending", f"{name} human review")


def validate_negative_scenarios() -> None:
    request, decision = load_pair("allowed-action")

    mutated = deepcopy(decision)
    mutated["target_id"] = "different-target"
    require_policy_error("mismatched target_id", request, mutated)

    mutated = deepcopy(decision)
    mutated["scope_id"] = "different-scope"
    require_policy_error("mismatched scope_id", request, mutated)

    mutated = deepcopy(decision)
    mutated["tool"] = "nmap"
    require_policy_error("mismatched tool", request, mutated)

    mutated = deepcopy(decision)
    mutated["operation"] = "passive_scan"
    require_policy_error("mismatched operation", request, mutated)

    mutated = deepcopy(decision)
    mutated["credential_ref"] = "different-credential"
    require_policy_error("mismatched credential_ref", request, mutated)

    mutated = deepcopy(decision)
    mutated["constraints"]["destructive_tests"] = True
    require_policy_error("destructive_tests true", request, mutated)

    mutated = deepcopy(decision)
    mutated["evidence_required"] = False
    require_policy_error("evidence_required false", request, mutated)

    mutated = deepcopy(decision)
    mutated["expires_at"] = mutated["decided_at"]
    require_policy_error("expires_at not after decided_at", request, mutated)


def validate_generated_runner_outputs() -> None:
    if TEST_OUTPUT_DIR.exists():
        shutil.rmtree(TEST_OUTPUT_DIR)

    runner = ROOT / "tools" / "run_tool_gateway_example.py"

    old_argv = sys.argv[:]
    try:
        sys.argv = [
            str(runner),
            "all",
            "--out-dir",
            str(TEST_OUTPUT_DIR),
        ]
        runpy.run_path(str(runner), run_name="__main__")
    finally:
        sys.argv = old_argv

    expected = {
        "allowed-action": "completed",
        "denied-action": "blocked",
        "human-approval-required": "requires_human_approval",
    }

    for scenario, expected_status in expected.items():
        result_path = TEST_OUTPUT_DIR / scenario / "tool-execution-result.generated.json"
        evidence_path = TEST_OUTPUT_DIR / scenario / "evidence-record.generated.json"

        if not result_path.exists():
            fail(f"generated result missing: {result_path}")
        if not evidence_path.exists():
            fail(f"generated evidence missing: {evidence_path}")

        result = json.loads(result_path.read_text(encoding="utf-8"))
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

        assert_equal(result["execution_status"], expected_status, f"{scenario} generated status")
        assert_false(result["secret_exposed_to_ai"], f"{scenario} generated result secret exposure")
        assert_false(evidence["secret_exposed_to_ai"], f"{scenario} generated evidence secret exposure")
        assert_equal(evidence["tool_execution_id"], result["tool_execution_id"], f"{scenario} generated evidence link")


def main() -> int:
    tests = [
        ("positive scenarios", validate_positive_scenarios),
        ("negative fail-closed scenarios", validate_negative_scenarios),
        ("generated runner outputs", validate_generated_runner_outputs),
    ]

    for label, func in tests:
        func()
        print(f"PASS: {label}")

    print("Tool Gateway runner tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
