from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / 'docs/436-v06361-external-discovery-fail-closed-gateway-core-integration-candidate-review-and-decision.md'
ADR = ROOT / 'planning/decisions/ADR-0436-add-v06361-external-discovery-fail-closed-gateway-core-integration-candidate-review-and-decision.md'
ISSUE = ROOT / 'planning/issues/0436-add-v06361-external-discovery-fail-closed-gateway-core-integration-candidate-review-and-decision.md'
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision', 'external_discovery_fail_closed_gateway_core_integration_candidate_review_completed = true', 'external_discovery_fail_closed_gateway_core_integration_candidate_review_id = external_discovery_fail_closed_gateway_core_integration_candidate_review_v06361', 'external_discovery_fail_closed_gateway_core_integration_candidate_decision = accepted_for_mock_gateway_core_path', 'external_discovery_fail_closed_gateway_core_integration_candidate_accepted = true', 'external_discovery_fail_closed_gateway_core_integration_candidate_status = accepted_pending_follow_on_controls', 'external_discovery_fail_closed_gateway_core_integrated = true', 'external_discovery_true_blocks_before_dispatch = true', 'external_discovery_false_allows_continue = true', 'external_discovery_missing_legacy_path_preserved_for_now = true', 'non_dispatch_decision_legacy_paths_preserved = true', 'destructive_tests_policy_error_path_preserved = true', 'normal_fixture_runner_compatibility_preserved = true', 'generated_output_schema_compatibility_preserved = true', 'tool_gateway_runner_compatibility_preserved = true', 'run_tool_gateway_example_all_passed_before_v06360_commit = true', 'validate_generated_outputs_passed_before_v06360_commit = true', 'test_tool_gateway_runner_passed_before_v06360_commit = true', 'all_local_checks_passed_before_v06360_commit = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_candidate_accepted = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_candidate_accepted = true', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'evidence_gateway_validation_result_modeling_required = true', 'implementation_maturity_matrix_required = true', 'readme_front_page_simplification_still_required = true', 'v06361_gateway_core_behavior_changed = false', 'v06361_tool_gateway_behavior_changed = false', 'v06361_runtime_behavior_changed = false', 'v06361_scanner_behavior_changed = false', 'v06361_schema_changed = false', 'v06361_fixtures_created = false', 'v06361_actual_records_created = false', 'v06361_private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = gateway_core_integration_maturity_matrix_and_evidence_trace_review', 'gateway_core_integration_maturity_matrix_and_evidence_trace_review_recommended = true', 'external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Candidate acceptance is not production readiness.', 'Candidate acceptance is not scanner readiness.', 'Candidate acceptance is not execution authorization.', 'Candidate acceptance is not real execution permission.', 'Candidate acceptance is not external target authorization.', 'Candidate acceptance is not customer demo approval.', 'Candidate acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.361.', 'v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06361_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0436",
        "Status: accepted",
        "Accept the v0.6.360 external discovery fail-closed Gateway core integration candidate",
    ])
    assert_tokens(ISSUE, [
        "0436 - Add v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision",
        "Status: completed by v0.6.361",
        "recommended_next_work_item = gateway_core_integration_maturity_matrix_and_evidence_trace_review",
        "Proceed to v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review",
    ])

def test_v06361_index_files() -> None:
    assert_tokens(README, [
        "v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision",
        "external_discovery_fail_closed_gateway_core_integration_candidate_accepted = true",
        "external_discovery_fail_closed_gateway_core_integrated = true",
        "external_discovery_true_blocks_before_dispatch = true",
        "authorization_expiry_current_time_gateway_core_integrated = true",
        "request_decision_constraint_diff_gateway_core_integrated = true",
        "controlled_executor_validation_gateway_core_integrated = false",
        "v06361_gateway_core_behavior_changed = false",
        "recommended_next_work_item = gateway_core_integration_maturity_matrix_and_evidence_trace_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.361 - External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision",
        "Accepted the v0.6.360 external discovery fail-closed Gateway core integration candidate",
        "recommended_next_work_item = gateway_core_integration_maturity_matrix_and_evidence_trace_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.361",
        "v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review",
        "no new Gateway core behavior change in v0.6.361",
    ])

def test_v06361_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ['tools/test_v06361_external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision.py'])

def test_v06361_no_unsupported_claims() -> None:
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
    test_v06361_primary_files()
    test_v06361_index_files()
    test_v06361_registered_in_run_all()
    test_v06361_no_unsupported_claims()
    print("v0.6.361 external discovery fail-closed Gateway core integration candidate review and decision checks passed")

if __name__ == "__main__":
    main()
