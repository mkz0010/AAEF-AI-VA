from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATEWAY_PATH = ROOT / "prototypes/tool-gateway/gateway.py"
DOC = ROOT / "docs/433-v06358-request-decision-constraint-diff-gateway-core-integration-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0433-add-v06358-request-decision-constraint-diff-gateway-core-integration-candidate.md"
ISSUE = ROOT / "planning/issues/0433-add-v06358-request-decision-constraint-diff-gateway-core-integration-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.358 Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate', 'request_decision_constraint_diff_gateway_core_integration_candidate_created = true', 'request_decision_constraint_diff_gateway_core_integration_candidate_status = candidate_implemented_pending_review', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integration_scope = explicit_request_decision_constraint_map_diff_blocks_before_dispatch', 'request_decision_constraint_diff_helper_exists = true', 'request_decision_constraint_diff_helper_tested = true', 'request_decision_constraint_diff_mismatch_blocks_before_dispatch = true', 'request_decision_constraint_diff_missing_constraint_maps_legacy_path_preserved = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_integrated = false', 'gateway_core_behavior_changed = true', 'tool_gateway_behavior_changed = true', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'publication_approval = false', 'commercial_offer_approval = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision', 'request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision_recommended = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Request/decision constraint diff Gateway core integration candidate is not execution authorization', 'Request/decision constraint diff Gateway core integration candidate is not real execution permission', 'Request/decision constraint diff Gateway core integration candidate is not external target authorization', 'Request/decision constraint diff Gateway core integration candidate is not scanner readiness', 'Request/decision constraint diff Gateway core integration candidate is not production readiness', 'No private generated outputs are moved public in v0.6.358.', 'v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision']

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
    spec = importlib.util.spec_from_file_location("aaef_v06358_gateway", GATEWAY_PATH)
    assert spec and spec.loader, "could not load gateway module spec"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_v06358_direct_constraint_diff_gate_blocks_before_dispatch() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06358_request_decision_constraint_diff_gate(
        {"requested_constraints": {"external_discovery": False, "rate_limit": "low"}},
        {"constraints": {"external_discovery": True, "rate_limit": "low"}},
    )
    assert gate["allowed_to_continue"] is False
    assert gate["status"] == "blocked_before_dispatch"
    assert gate["reason"] == "request_decision_constraint_diff_detected"
    assert "external_discovery" in gate["diff"]["mismatched_keys"]


def test_v06358_denied_decision_legacy_path_preserved() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06358_request_decision_constraint_diff_gate(
        {"requested_constraints": {"external_discovery": False}},
        {
            "status": "blocked",
            "constraints": {"external_discovery": True},
        },
    )
    assert gate["allowed_to_continue"] is True
    assert gate["status"] == "not_applicable_decision_not_dispatch_authorized_legacy_path_preserved"


def test_v06358_missing_constraint_maps_legacy_path_preserved() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06358_request_decision_constraint_diff_gate(
        {"tool_action_request_id": "request-without-constraints"},
        {"authorization_decision_id": "decision-without-constraints"},
    )
    assert gate["allowed_to_continue"] is True
    assert gate["status"] == "not_applicable_missing_constraint_maps_legacy_path_preserved"

def test_v06358_destructive_tests_policy_error_path_preserved() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06358_request_decision_constraint_diff_gate(
        {"requested_constraints": {"destructive_tests": False}},
        {"constraints": {"destructive_tests": True}},
    )
    assert gate["allowed_to_continue"] is True
    assert gate["status"] == "not_applicable_existing_policy_error_path_preserved"


def test_v06358_gateway_wrappers_installed_or_inventory_available() -> None:
    gateway = load_gateway_module()
    wrapped = getattr(gateway, "_AAEF_V06358_WRAPPED_GATEWAY_FUNCTIONS", [])
    inventory = getattr(gateway, "_AAEF_V06358_GATEWAY_FUNCTION_INVENTORY", [])
    assert inventory, "gateway function inventory was not recorded"
    assert wrapped, "no request/decision Gateway function wrappers were installed"

def test_v06358_gateway_source_contains_integration_marker() -> None:
    text = read_text(GATEWAY_PATH)
    assert "AAEF-AI-VA v0.6.358 request/decision constraint diff Gateway core integration candidate" in text
    assert "_aaef_v06358_request_decision_constraint_diff_gate" in text
    assert "v0.6.358 constraint diff dispatch-decision scope fix" in text
    assert "v0.6.358 constraint diff existing PolicyError path preservation fix" in text
    assert "_aaef_v06358_install_gateway_wrappers" in text
    assert "request_decision_constraint_diff_detected" in text

def test_v06358_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, ["ADR-0433", "Status: proposed implementation candidate"])
    assert_tokens(ISSUE, [
        "0433 - Add v0.6.358 Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate",
        "Status: completed by v0.6.358",
        "recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision",
    ])

def test_v06358_index_files() -> None:
    assert_tokens(README, [
        "v0.6.358 Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate",
        "request_decision_constraint_diff_gateway_core_integrated = true",
        "request_decision_constraint_diff_mismatch_blocks_before_dispatch = true",
        "authorization_expiry_current_time_gateway_core_integrated = true",
        "external_discovery_fail_closed_gateway_core_integrated = false",
        "gateway_core_behavior_changed = true",
        "tool_gateway_behavior_changed = true",
        "runtime_behavior_changed = false",
        "scanner_behavior_changed = false",
        "recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.358 - Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate",
        "request/decision constraint-diff pre-dispatch wrappers",
        "recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.358",
        "v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision",
        "request/decision constraint-diff Gateway core integration candidate is pending review",
    ])

def test_v06358_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06358_request_decision_constraint_diff_gateway_core_integration_candidate.py"])

def main() -> None:
    test_v06358_direct_constraint_diff_gate_blocks_before_dispatch()
    test_v06358_missing_constraint_maps_legacy_path_preserved()
    test_v06358_gateway_wrappers_installed_or_inventory_available()
    test_v06358_gateway_source_contains_integration_marker()
    test_v06358_primary_files()
    test_v06358_index_files()
    test_v06358_registered_in_run_all()
    print("v0.6.358 request/decision constraint diff Gateway core integration candidate checks passed")

if __name__ == "__main__":
    main()
