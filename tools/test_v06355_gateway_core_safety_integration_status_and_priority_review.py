from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/430-v06355-gateway-core-safety-integration-status-and-priority-review.md"
ADR = ROOT / "planning/decisions/ADR-0430-add-v06355-gateway-core-safety-integration-status-and-priority-review.md"
ISSUE = ROOT / "planning/issues/0430-add-v06355-gateway-core-safety-integration-status-and-priority-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.355 Gateway Core Safety Integration Status and Priority Review', 'gateway_core_safety_integration_status_and_priority_review_completed = true', 'gateway_core_safety_integration_status = helper_ready_core_not_integrated', 'gateway_core_safety_integration_priority = p0', 'gateway_core_currently_enforces_request_decision_binding = true', 'gateway_core_currently_enforces_credential_ref_metadata_check = true', 'authorization_expiry_current_time_helper_exists = true', 'authorization_expiry_current_time_helper_tested = true', 'authorization_expiry_current_time_gateway_core_integrated = false', 'request_decision_constraint_diff_helper_exists = true', 'request_decision_constraint_diff_helper_tested = true', 'request_decision_constraint_diff_gateway_core_integrated = false', 'external_discovery_fail_closed_helper_exists = true', 'external_discovery_fail_closed_helper_tested = true', 'external_discovery_fail_closed_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'evidence_gateway_validation_result_modeling_required = true', 'implementation_maturity_matrix_required = true', 'readme_front_page_simplification_still_required = true', 'p0_sequence_1 = authorization_expiry_current_time_gateway_core_integration', 'p0_sequence_2 = request_decision_constraint_diff_gateway_core_integration', 'p0_sequence_3 = external_discovery_fail_closed_gateway_core_integration', 'p0_sequence_4 = controlled_executor_validation_gateway_core_connection', 'p0_sequence_5 = public_mock_dry_run_status_cleanup', 'p0_sequence_6 = gateway_validation_evidence_trace_modeling', 'history_rewrite_performed = false', 'repo_recreated = false', 'git_history_exposure_may_remain = true', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'tool_gateway_behavior_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'gateway_core_behavior_changed = false', 'gateway_core_integration_implemented = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_implementation_candidate', 'authorization_expiry_current_time_gateway_core_integration_implementation_candidate_recommended = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Gateway core status review is not Gateway core integration', 'Gateway core status review is not runtime wiring', 'Gateway core status review is not runtime application', 'Gateway core status review is not execution authorization', 'Gateway core status review is not real execution permission', 'Gateway core status review is not external target authorization', 'Gateway core status review is not scanner readiness', 'Gateway core status review is not production readiness', 'No private generated outputs are moved public in v0.6.355.', 'v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06355_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0430",
        "Status: accepted",
        "Prioritize Gateway core safety integration as P0 work",
    ])
    assert_tokens(ISSUE, [
        "0430 - Add v0.6.355 Gateway Core Safety Integration Status and Priority Review",
        "Status: completed by v0.6.355",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_implementation_candidate",
        "Proceed to v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate",
    ])

def test_v06355_index_files() -> None:
    assert_tokens(README, [
        "v0.6.355 Gateway Core Safety Integration Status and Priority Review",
        "gateway_core_safety_integration_status_and_priority_review_completed = true",
        "gateway_core_safety_integration_status = helper_ready_core_not_integrated",
        "gateway_core_safety_integration_priority = p0",
        "authorization_expiry_current_time_gateway_core_integrated = false",
        "request_decision_constraint_diff_gateway_core_integrated = false",
        "external_discovery_fail_closed_gateway_core_integrated = false",
        "controlled_executor_validation_gateway_core_integrated = false",
        "gateway_core_behavior_changed = false",
        "gateway_core_integration_implemented = false",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_implementation_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.355 - Gateway Core Safety Integration Status and Priority Review",
        "gateway_core_safety_integration_status = helper_ready_core_not_integrated",
        "gateway_core_safety_integration_priority = p0",
        "recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_implementation_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.355",
        "v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate",
        "Gateway core integration is not yet implemented",
        "no Gateway core behavior change in v0.6.355",
    ])

def test_v06355_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06355_gateway_core_safety_integration_status_and_priority_review.py"])

def test_v06355_no_unsupported_claims() -> None:
    scanned_paths = [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
        "production-ready scanner",
        "runtime-enforced scanner",
        "external-target-ready demo",
        "customer-ready PoC",
        "certified / audit-ready system",
        "compliance-sufficient control",
        "diagnostically complete",
        "diagnostically-complete",
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06355_primary_files()
    test_v06355_index_files()
    test_v06355_registered_in_run_all()
    test_v06355_no_unsupported_claims()
    print("v0.6.355 gateway core safety integration status and priority review checks passed")

if __name__ == "__main__":
    main()
