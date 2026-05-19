from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/437-v06362-gateway-core-integration-maturity-matrix-and-evidence-trace-review.md"
ADR = ROOT / "planning/decisions/ADR-0437-add-v06362-gateway-core-integration-maturity-matrix-and-evidence-trace-review.md"
ISSUE = ROOT / "planning/issues/0437-add-v06362-gateway-core-integration-maturity-matrix-and-evidence-trace-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review', 'gateway_core_integration_maturity_matrix_review_completed = true', 'gateway_core_integration_maturity_matrix_review_id = gateway_core_integration_maturity_matrix_review_v06362', 'gateway_core_authorization_expiry_current_time_status = gateway_core_integrated_and_accepted', 'gateway_core_request_decision_constraint_diff_status = gateway_core_integrated_and_accepted', 'gateway_core_external_discovery_fail_closed_status = gateway_core_integrated_and_accepted', 'gateway_core_controlled_executor_validation_status = separate_helper_not_gateway_core_integrated', 'gateway_core_common_target_scope_tool_operation_binding_status = partial_not_common_gateway_core_integrated', 'gateway_core_mock_dry_run_status_terminology_status = helper_exists_public_output_cleanup_required', 'gateway_core_evidence_trace_status = minimal_reconstruction_trace_gateway_validation_result_modeling_required', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_candidate_accepted = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_candidate_accepted = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_candidate_accepted = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'gateway_validation_result_evidence_trace_modeling_required = true', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'implementation_maturity_matrix_added = true', 'evidence_trace_gap_review_added = true', 'readme_front_page_simplification_still_required = true', 'v06362_gateway_core_behavior_changed = false', 'v06362_tool_gateway_behavior_changed = false', 'v06362_runtime_behavior_changed = false', 'v06362_scanner_behavior_changed = false', 'v06362_schema_changed = false', 'v06362_fixtures_created = false', 'v06362_actual_records_created = false', 'v06362_private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate', 'gateway_validation_result_evidence_trace_modeling_candidate_recommended = true', 'gateway_core_integration_maturity_matrix_and_evidence_trace_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Maturity matrix visibility is not production readiness.', 'Maturity matrix visibility is not scanner readiness.', 'Maturity matrix visibility is not execution authorization.', 'Maturity matrix visibility is not real execution permission.', 'Maturity matrix visibility is not external target authorization.', 'Maturity matrix visibility is not customer demo approval.', 'Maturity matrix visibility is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.362.', 'v0.6.363 Gateway Validation Result Evidence Trace Modeling Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06362_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, [
        "| Control area | Helper exists | Helper tested | Gateway core integrated | Candidate accepted | Evidence trace status | Public/demo status |",
        "| Authorization expiry current-time | yes | yes | yes | yes |",
        "| Request/decision constraint diff | yes | yes | yes | yes |",
        "| External discovery fail-closed | yes | yes | yes | yes |",
        "gateway validation results are not yet modeled as a structured evidence-trace field",
    ])
    assert_tokens(ADR, [
        "ADR-0437",
        "Status: accepted",
        "Add a Gateway core integration maturity matrix and evidence trace gap review",
    ])
    assert_tokens(ISSUE, [
        "0437 - Add v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review",
        "Status: completed by v0.6.362",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate",
    ])

def test_v06362_index_files() -> None:
    assert_tokens(README, [
        "v0.6.362 Gateway Core Integration Maturity Matrix and Evidence Trace Review",
        "gateway_core_authorization_expiry_current_time_status = gateway_core_integrated_and_accepted",
        "gateway_core_request_decision_constraint_diff_status = gateway_core_integrated_and_accepted",
        "gateway_core_external_discovery_fail_closed_status = gateway_core_integrated_and_accepted",
        "gateway_core_controlled_executor_validation_status = separate_helper_not_gateway_core_integrated",
        "gateway_validation_result_evidence_trace_modeling_required = true",
        "v06362_gateway_core_behavior_changed = false",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.362 - Gateway Core Integration Maturity Matrix and Evidence Trace Review",
        "Gateway core integration maturity matrix",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.362",
        "v0.6.363 Gateway Validation Result Evidence Trace Modeling Candidate",
        "no new Gateway core behavior change in v0.6.362",
    ])

def test_v06362_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06362_gateway_core_integration_maturity_matrix_and_evidence_trace_review.py"])

def test_v06362_no_unsupported_claims() -> None:
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
    test_v06362_primary_files()
    test_v06362_index_files()
    test_v06362_registered_in_run_all()
    test_v06362_no_unsupported_claims()
    print("v0.6.362 gateway core integration maturity matrix and evidence trace review checks passed")

if __name__ == "__main__":
    main()
