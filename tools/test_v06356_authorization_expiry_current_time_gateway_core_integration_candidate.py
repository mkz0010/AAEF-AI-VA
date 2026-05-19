from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATEWAY_PATH = ROOT / "prototypes/tool-gateway/gateway.py"
DOC = ROOT / "docs/431-v06356-authorization-expiry-current-time-gateway-core-integration-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0431-add-v06356-authorization-expiry-current-time-gateway-core-integration-candidate.md"
ISSUE = ROOT / "planning/issues/0431-add-v06356-authorization-expiry-current-time-gateway-core-integration-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate', 'authorization_expiry_current_time_gateway_core_integration_candidate_created = true', 'authorization_expiry_current_time_gateway_core_integration_candidate_id = authorization_expiry_current_time_gateway_core_integration_candidate_v06356', 'authorization_expiry_current_time_gateway_core_integration_candidate_status = candidate_implemented_pending_review', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_integration_scope = expired_authorization_blocks_before_dispatch', 'authorization_expiry_current_time_helper_exists = true', 'authorization_expiry_current_time_helper_tested = true', 'authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true', 'authorization_expiry_current_time_missing_expiry_legacy_path_preserved = true', 'request_decision_constraint_diff_gateway_core_integrated = false', 'external_discovery_fail_closed_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_integrated = false', 'gateway_core_behavior_changed = true', 'tool_gateway_behavior_changed = true', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'schema_changed = false', 'fixtures_created = false', 'private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision', 'authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision_recommended = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Authorization expiry current-time Gateway core integration candidate is not execution authorization', 'Authorization expiry current-time Gateway core integration candidate is not real execution permission', 'Authorization expiry current-time Gateway core integration candidate is not external target authorization', 'Authorization expiry current-time Gateway core integration candidate is not scanner readiness', 'Authorization expiry current-time Gateway core integration candidate is not production readiness', 'No private generated outputs are moved public in v0.6.356.', 'v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision']

def read_text(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read_text(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def load_gateway_module():
    gateway_dir = str(GATEWAY_PATH.parent)
    if gateway_dir not in sys.path:
        sys.path.insert(0, gateway_dir)
    spec = importlib.util.spec_from_file_location("aaef_v06356_gateway", GATEWAY_PATH)
    assert spec and spec.loader, "could not load gateway module spec"
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_v06356_direct_expired_authorization_gate_blocks_before_dispatch() -> None:
    gateway = load_gateway_module()
    assert hasattr(gateway, "_aaef_v06356_authorization_expiry_current_time_gate")
    gate = gateway._aaef_v06356_authorization_expiry_current_time_gate(
        {"authorization": {"expires_at": "2000-01-01T00:00:00Z"}},
        current_time=datetime(2026, 5, 19, tzinfo=timezone.utc),
    )
    assert gate["allowed_to_continue"] is False
    assert gate["status"] == "blocked_before_dispatch"
    assert gate["reason"] == "authorization_expired_at_current_time"

def test_v06356_missing_expiry_legacy_path_preserved() -> None:
    gateway = load_gateway_module()
    gate = gateway._aaef_v06356_authorization_expiry_current_time_gate(
        {"credential_metadata": {"valid_until": "2000-01-01T00:00:00Z"}},
        current_time=datetime(2026, 5, 19, tzinfo=timezone.utc),
    )
    assert gate["allowed_to_continue"] is True
    assert gate["status"] == "not_applicable_missing_expiry_legacy_path_preserved"


def test_v06356_gateway_wrappers_installed_or_inventory_available() -> None:
    gateway = load_gateway_module()
    wrapped = getattr(gateway, "_AAEF_V06356_WRAPPED_GATEWAY_FUNCTIONS", [])
    inventory = getattr(gateway, "_AAEF_V06356_GATEWAY_FUNCTION_INVENTORY", [])
    assert inventory, "gateway function inventory was not recorded"
    assert wrapped, "no request/decision Gateway function wrappers were installed"

def test_v06356_gateway_source_contains_integration_marker() -> None:
    text = read_text(GATEWAY_PATH)
    assert "AAEF-AI-VA v0.6.356 authorization expiry current-time Gateway core integration candidate" in text
    assert "_aaef_v06356_authorization_expiry_current_time_gate" in text
    assert "v0.6.356 authorization expiry scope fix: targeted authorization expiry only" in text
    assert "_aaef_v06356_install_gateway_wrappers" in text
    assert "_aaef_v06356_shape_blocked_gateway_return" in text
    assert "authorization_expired_at_current_time" in text

def test_v06356_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0431",
        "Status: proposed implementation candidate",
        "function-signature discovery",
    ])
    assert_tokens(ISSUE, [
        "0431 - Add v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate",
        "Status: completed by v0.6.356",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision",
    ])

def test_v06356_index_files() -> None:
    assert_tokens(README, [
        "v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate",
        "authorization_expiry_current_time_gateway_core_integrated = true",
        "authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true",
        "request_decision_constraint_diff_gateway_core_integrated = false",
        "external_discovery_fail_closed_gateway_core_integrated = false",
        "gateway_core_behavior_changed = true",
        "tool_gateway_behavior_changed = true",
        "runtime_behavior_changed = false",
        "scanner_behavior_changed = false",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.356 - Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate",
        "authorization-expiry pre-dispatch wrappers",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.356",
        "v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision",
        "authorization expiry current-time Gateway core integration candidate is pending review",
    ])

def test_v06356_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06356_authorization_expiry_current_time_gateway_core_integration_candidate.py"])

def main() -> None:
    test_v06356_direct_expired_authorization_gate_blocks_before_dispatch()
    test_v06356_gateway_wrappers_installed_or_inventory_available()
    test_v06356_gateway_source_contains_integration_marker()
    test_v06356_primary_files()
    test_v06356_index_files()
    test_v06356_registered_in_run_all()
    print("v0.6.356 authorization expiry current-time Gateway core integration candidate checks passed")

if __name__ == "__main__":
    main()
