from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATEWAY_PATH = ROOT / "prototypes/tool-gateway/gateway.py"
DOC = ROOT / "docs/435-v06360-external-discovery-fail-closed-gateway-core-integration-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0435-add-v06360-external-discovery-fail-closed-gateway-core-integration-candidate.md"
ISSUE = ROOT / "planning/issues/0435-add-v06360-external-discovery-fail-closed-gateway-core-integration-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
REQUIRED = ['v0.6.360 External Discovery Fail-Closed Gateway Core Integration Implementation Candidate', 'external_discovery_fail_closed_gateway_core_integration_candidate_created = true', 'external_discovery_fail_closed_gateway_core_integration_candidate_status = candidate_implemented_pending_review', 'external_discovery_fail_closed_gateway_core_integrated = true', 'external_discovery_true_blocks_before_dispatch = true', 'external_discovery_false_allows_continue = true', 'external_discovery_missing_legacy_path_preserved = true', 'non_dispatch_decision_legacy_paths_preserved = true', 'destructive_tests_policy_error_path_preserved = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'gateway_core_behavior_changed = true', 'tool_gateway_behavior_changed = true', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'External discovery fail-closed Gateway core integration candidate is not execution authorization', 'External discovery fail-closed Gateway core integration candidate is not real execution permission', 'External discovery fail-closed Gateway core integration candidate is not external target authorization', 'External discovery fail-closed Gateway core integration candidate is not scanner readiness', 'External discovery fail-closed Gateway core integration candidate is not production readiness', 'No private generated outputs are moved public in v0.6.360.', 'v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision']

def read_text(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read_text(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def load_gateway_module():
    import sys
    gateway_dir = str(GATEWAY_PATH.parent)
    if gateway_dir not in sys.path:
        sys.path.insert(0, gateway_dir)
    spec = importlib.util.spec_from_file_location("aaef_v06360_gateway", GATEWAY_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_v06360_gate_behavior() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"requested_constraints": {"external_discovery": True}}, {"constraints": {"external_discovery": False}})
    assert gate["allowed_to_continue"] is False
    assert gate["status"] == "blocked_before_dispatch"
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"requested_constraints": {"external_discovery": False}}, {"constraints": {"external_discovery": True}})
    assert gate["allowed_to_continue"] is False
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"requested_constraints": {"external_discovery": False}}, {"constraints": {"external_discovery": False}})
    assert gate["allowed_to_continue"] is True and gate["status"] == "passed"
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"id": "r"}, {"id": "d"})
    assert gate["status"] == "not_applicable_external_discovery_not_declared_legacy_path_preserved"
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"requested_constraints": {"external_discovery": True}}, {"status": "blocked", "constraints": {"external_discovery": True}})
    assert gate["status"] == "not_applicable_decision_not_dispatch_authorized_legacy_path_preserved"
    gate = gateway._aaef_v06360_external_discovery_fail_closed_gate({"requested_constraints": {"destructive_tests": False, "external_discovery": False}}, {"constraints": {"destructive_tests": True, "external_discovery": True}})
    assert gate["status"] == "not_applicable_existing_policy_error_path_preserved"

def test_v06360_gateway_markers_and_wrappers() -> None:
    gateway = load_gateway_module()
    assert getattr(gateway, "_AAEF_V06360_GATEWAY_FUNCTION_INVENTORY", [])
    assert getattr(gateway, "_AAEF_V06360_WRAPPED_GATEWAY_FUNCTIONS", [])
    text = read_text(GATEWAY_PATH)
    assert "AAEF-AI-VA v0.6.360 external discovery fail-closed Gateway core integration candidate" in text
    assert "_aaef_v06360_external_discovery_fail_closed_gate" in text
    assert "external_discovery_true_fail_closed" in text

def test_v06360_files_and_indexes() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, ["ADR-0435", "Status: proposed implementation candidate", "external_discovery=true"])
    assert_tokens(ISSUE, ["0435 - Add v0.6.360", "recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision"])
    assert_tokens(README, ["v0.6.360 External Discovery Fail-Closed", "external_discovery_fail_closed_gateway_core_integrated = true", "external_discovery_true_blocks_before_dispatch = true", "runtime_behavior_changed = false"])
    assert_tokens(CHANGELOG, ["v0.6.360 - External Discovery Fail-Closed", "external-discovery pre-dispatch wrappers"])
    assert_tokens(ROADMAP, ["After v0.6.360", "v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision"])
    assert_tokens(RUN_ALL, ["tools/test_v06360_external_discovery_fail_closed_gateway_core_integration_candidate.py"])

def main() -> None:
    test_v06360_gate_behavior()
    test_v06360_gateway_markers_and_wrappers()
    test_v06360_files_and_indexes()
    print("v0.6.360 external discovery fail-closed Gateway core integration candidate checks passed")

if __name__ == "__main__":
    main()
