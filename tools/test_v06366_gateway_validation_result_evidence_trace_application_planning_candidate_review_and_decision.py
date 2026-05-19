from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/441-v06366-gateway-validation-result-evidence-trace-application-planning-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0441-add-v06366-gateway-validation-result-evidence-trace-application-planning-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0441-add-v06366-gateway-validation-result-evidence-trace-application-planning-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.366 Gateway Validation Result Evidence Trace Application Planning Candidate Review and Decision', 'gateway_validation_result_evidence_trace_application_planning_candidate_review_completed = true', 'gateway_validation_result_evidence_trace_application_planning_candidate_review_id = gateway_validation_result_evidence_trace_application_planning_candidate_review_v06366', 'gateway_validation_result_evidence_trace_application_planning_candidate_decision = accepted_for_private_reviewer_artifact_first_application_path', 'gateway_validation_result_evidence_trace_application_planning_candidate_accepted = true', 'gateway_validation_result_evidence_trace_application_planning_candidate_status = accepted_pending_private_reviewer_artifact_candidate', 'gateway_validation_result_evidence_trace_model_accepted = true', 'gateway_validation_result_evidence_trace_model_decision = accepted_for_reviewer_facing_evidence_trace_direction', 'gateway_validation_result_application_strategy_defined = true', 'gateway_validation_result_application_strategy = staged_private_first_then_schema_or_generated_output_decision', 'gateway_validation_result_application_phase_1_private_reviewer_artifact = accepted_as_first_application_target', 'gateway_validation_result_application_phase_2_schema_field_decision = deferred', 'gateway_validation_result_application_phase_3_generated_output_application_decision = deferred', 'gateway_validation_result_application_phase_4_runtime_application_decision = deferred', 'gateway_validation_result_application_public_artifact_change_decision = deferred', 'gateway_validation_result_application_raw_and_reviewer_status_separation_required = true', 'gateway_validation_result_application_raw_gate_result_preserved = true', 'gateway_validation_result_application_reviewer_status_required = true', 'gateway_validation_result_application_external_process_executed_required = true', 'gateway_validation_result_application_network_activity_performed_required = true', 'gateway_validation_result_application_limitations_required = true', 'gateway_validation_result_application_backward_compatibility_required = true', 'gateway_validation_result_application_schema_change_now = false', 'gateway_validation_result_application_generated_output_change_now = false', 'gateway_validation_result_application_runtime_change_now = false', 'gateway_validation_result_application_public_artifact_change_now = false', 'gateway_validation_result_application_private_reviewer_artifact_next = true', 'gateway_validation_result_application_private_reviewer_artifact_candidate_recommended = true', 'gateway_validation_result_application_public_output_cleanup_dependency = mock_dry_run_status_terminology_public_output_cleanup', 'gateway_validation_result_application_controlled_executor_dependency = controlled_executor_validation_gateway_core_connection', 'gateway_validation_result_application_producer_identity_deferred = true', 'gateway_validation_result_application_hash_or_signature_deferred = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_candidate_accepted = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_candidate_accepted = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_candidate_accepted = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'implementation_maturity_matrix_available = true', 'readme_front_page_simplification_still_required = true', 'v06366_gateway_core_behavior_changed = false', 'v06366_tool_gateway_behavior_changed = false', 'v06366_runtime_behavior_changed = false', 'v06366_scanner_behavior_changed = false', 'v06366_schema_changed = false', 'v06366_fixtures_created = false', 'v06366_actual_records_created = false', 'v06366_private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_recommended = true', 'gateway_validation_result_evidence_trace_application_planning_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Application planning acceptance is not production readiness.', 'Application planning acceptance is not scanner readiness.', 'Application planning acceptance is not execution authorization.', 'Application planning acceptance is not real execution permission.', 'Application planning acceptance is not external target authorization.', 'Application planning acceptance is not customer demo approval.', 'Application planning acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.366.', 'v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06366_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, [
        "| Review item | Decision |",
        "accepted as first application target",
        "| Private reviewer artifact requirement | Decision |",
        "Keep artifact under `private-not-in-git/` unless separately approved",
        "v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate",
    ])
    assert_tokens(ADR, [
        "ADR-0441",
        "Status: accepted",
        "Accept the v0.6.365 application plan",
    ])
    assert_tokens(ISSUE, [
        "0441 - Add v0.6.366 Gateway Validation Result Evidence Trace Application Planning Candidate Review and Decision",
        "Status: completed by v0.6.366",
        "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate",
    ])

def test_v06366_index_files() -> None:
    assert_tokens(README, [
        "v0.6.366 Gateway Validation Result Evidence Trace Application Planning Candidate Review and Decision",
        "gateway_validation_result_evidence_trace_application_planning_candidate_decision = accepted_for_private_reviewer_artifact_first_application_path",
        "gateway_validation_result_evidence_trace_application_planning_candidate_accepted = true",
        "gateway_validation_result_application_phase_1_private_reviewer_artifact = accepted_as_first_application_target",
        "gateway_validation_result_application_phase_2_schema_field_decision = deferred",
        "gateway_validation_result_application_public_artifact_change_decision = deferred",
        "gateway_validation_result_application_schema_change_now = false",
        "gateway_validation_result_application_generated_output_change_now = false",
        "v06366_schema_changed = false",
        "v06366_gateway_core_behavior_changed = false",
        "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.366 - Gateway Validation Result Evidence Trace Application Planning Candidate Review and Decision",
        "private reviewer-facing artifact candidate as the first application target",
        "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.366",
        "v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate",
        "no evidence-record schema change in v0.6.366",
    ])

def test_v06366_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06366_gateway_validation_result_evidence_trace_application_planning_candidate_review_and_decision.py"])

def test_v06366_no_unsupported_claims() -> None:
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
    test_v06366_primary_files()
    test_v06366_index_files()
    test_v06366_registered_in_run_all()
    test_v06366_no_unsupported_claims()
    print("v0.6.366 gateway validation result evidence trace application planning candidate review and decision checks passed")

if __name__ == "__main__":
    main()
