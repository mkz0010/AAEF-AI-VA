from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/434-v06359-request-decision-constraint-diff-gateway-core-integration-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0434-add-v06359-request-decision-constraint-diff-gateway-core-integration-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0434-add-v06359-request-decision-constraint-diff-gateway-core-integration-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision', 'request_decision_constraint_diff_gateway_core_integration_candidate_review_completed = true', 'request_decision_constraint_diff_gateway_core_integration_candidate_review_id = request_decision_constraint_diff_gateway_core_integration_candidate_review_v06359', 'request_decision_constraint_diff_gateway_core_integration_candidate_decision = accepted_for_mock_gateway_core_path', 'request_decision_constraint_diff_gateway_core_integration_candidate_accepted = true', 'request_decision_constraint_diff_gateway_core_integration_candidate_status = accepted_pending_follow_on_controls', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_mismatch_blocks_before_dispatch = true', 'request_decision_constraint_diff_missing_constraint_maps_legacy_path_preserved_for_now = true', 'non_dispatch_decision_legacy_paths_preserved = true', 'destructive_tests_policy_error_path_preserved = true', 'normal_fixture_runner_compatibility_preserved = true', 'generated_output_schema_compatibility_preserved = true', 'tool_gateway_runner_compatibility_preserved = true', 'run_tool_gateway_example_all_passed_before_v06358_commit = true', 'validate_generated_outputs_passed_before_v06358_commit = true', 'test_tool_gateway_runner_passed_before_v06358_commit = true', 'all_local_checks_passed_before_v06358_commit = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_candidate_accepted = true', 'external_discovery_fail_closed_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'evidence_gateway_validation_result_modeling_required = true', 'implementation_maturity_matrix_required = true', 'readme_front_page_simplification_still_required = true', 'v06359_gateway_core_behavior_changed = false', 'v06359_tool_gateway_behavior_changed = false', 'v06359_runtime_behavior_changed = false', 'v06359_scanner_behavior_changed = false', 'v06359_schema_changed = false', 'v06359_fixtures_created = false', 'v06359_actual_records_created = false', 'v06359_private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_implementation_candidate', 'external_discovery_fail_closed_gateway_core_integration_implementation_candidate_recommended = true', 'request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Candidate acceptance is not production readiness.', 'Candidate acceptance is not scanner readiness.', 'Candidate acceptance is not execution authorization.', 'Candidate acceptance is not real execution permission.', 'Candidate acceptance is not external target authorization.', 'Candidate acceptance is not customer demo approval.', 'Candidate acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.359.', 'v0.6.360 External Discovery Fail-Closed Gateway Core Integration Implementation Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06359_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0434",
        "Status: accepted",
        "Accept the v0.6.358 request/decision constraint-diff Gateway core integration candidate",
    ])
    assert_tokens(ISSUE, [
        "0434 - Add v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision",
        "Status: completed by v0.6.359",
        "recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_implementation_candidate",
        "Proceed to v0.6.360 External Discovery Fail-Closed Gateway Core Integration Implementation Candidate",
    ])

def test_v06359_index_files() -> None:
    assert_tokens(README, [
        "v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision",
        "request_decision_constraint_diff_gateway_core_integration_candidate_accepted = true",
        "request_decision_constraint_diff_gateway_core_integrated = true",
        "request_decision_constraint_diff_mismatch_blocks_before_dispatch = true",
        "non_dispatch_decision_legacy_paths_preserved = true",
        "destructive_tests_policy_error_path_preserved = true",
        "normal_fixture_runner_compatibility_preserved = true",
        "generated_output_schema_compatibility_preserved = true",
        "tool_gateway_runner_compatibility_preserved = true",
        "external_discovery_fail_closed_gateway_core_integrated = false",
        "controlled_executor_validation_gateway_core_integrated = false",
        "v06359_gateway_core_behavior_changed = false",
        "recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_implementation_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.359 - Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision",
        "Accepted the v0.6.358 request/decision constraint-diff Gateway core integration candidate",
        "recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_implementation_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.359",
        "v0.6.360 External Discovery Fail-Closed Gateway Core Integration Implementation Candidate",
        "no new Gateway core behavior change in v0.6.359",
    ])

def test_v06359_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06359_request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision.py"])

def test_v06359_no_unsupported_claims() -> None:
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
    test_v06359_primary_files()
    test_v06359_index_files()
    test_v06359_registered_in_run_all()
    test_v06359_no_unsupported_claims()
    print("v0.6.359 request/decision constraint-diff Gateway core integration candidate review and decision checks passed")

if __name__ == "__main__":
    main()
