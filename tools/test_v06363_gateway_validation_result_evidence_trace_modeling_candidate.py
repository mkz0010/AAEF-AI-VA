from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/438-v06363-gateway-validation-result-evidence-trace-modeling-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0438-add-v06363-gateway-validation-result-evidence-trace-modeling-candidate.md"
ISSUE = ROOT / "planning/issues/0438-add-v06363-gateway-validation-result-evidence-trace-modeling-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.363 Gateway Validation Result Evidence Trace Modeling Candidate', 'gateway_validation_result_evidence_trace_modeling_candidate_created = true', 'gateway_validation_result_evidence_trace_modeling_candidate_id = gateway_validation_result_evidence_trace_modeling_candidate_v06363', 'gateway_validation_result_evidence_trace_modeling_candidate_status = candidate_defined_pending_review', 'gateway_validation_result_evidence_trace_model_defined = true', 'gateway_validation_result_evidence_trace_model_runtime_applied = false', 'gateway_validation_result_evidence_record_schema_changed = false', 'gateway_validation_result_generated_outputs_changed = false', 'gateway_validation_result_existing_generated_output_compatibility_preserved = true', 'gateway_validation_result_model_scope = reviewer_facing_gateway_validation_trace_field_candidate', 'gateway_validation_result_model_gate_set_includes_authorization_expiry_current_time = true', 'gateway_validation_result_model_gate_set_includes_request_decision_constraint_diff = true', 'gateway_validation_result_model_gate_set_includes_external_discovery_fail_closed = true', 'gateway_validation_result_model_gate_set_includes_non_dispatch_legacy_path_preservation = true', 'gateway_validation_result_model_gate_set_includes_existing_policy_error_path_preservation = true', 'gateway_validation_result_model_external_process_executed_field_required = true', 'gateway_validation_result_model_network_activity_performed_field_required = true', 'gateway_validation_result_model_limitations_field_required = true', 'gateway_validation_result_model_producer_identity_future_work = true', 'gateway_validation_result_model_hash_or_signature_future_work = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'authorization_expiry_current_time_gateway_core_candidate_accepted = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_candidate_accepted = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_candidate_accepted = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'implementation_maturity_matrix_available = true', 'readme_front_page_simplification_still_required = true', 'v06363_gateway_core_behavior_changed = false', 'v06363_tool_gateway_behavior_changed = false', 'v06363_runtime_behavior_changed = false', 'v06363_scanner_behavior_changed = false', 'v06363_schema_changed = false', 'v06363_fixtures_created = false', 'v06363_actual_records_created = false', 'v06363_private_generated_outputs_moved_public = false', 'history_rewrite_performed = false', 'repo_recreated = false', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'runtime_enforcement_implemented = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision', 'gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision_recommended = true', 'gateway_validation_result_evidence_trace_modeling_candidate_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Gateway validation result evidence trace modeling is not production readiness.', 'Gateway validation result evidence trace modeling is not scanner readiness.', 'Gateway validation result evidence trace modeling is not execution authorization.', 'Gateway validation result evidence trace modeling is not real execution permission.', 'Gateway validation result evidence trace modeling is not external target authorization.', 'Gateway validation result evidence trace modeling is not customer demo approval.', 'Gateway validation result evidence trace modeling is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.363.', 'v0.6.364 Gateway Validation Result Evidence Trace Modeling Candidate Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06363_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, [
        '"gateway_validation_result"',
        '"gate_results"',
        '"gate_id": "authorization_expiry_current_time"',
        '"gate_id": "request_decision_constraint_diff"',
        '"gate_id": "external_discovery_fail_closed"',
        '"external_process_executed": false',
        '"network_activity_performed": false',
        "| `gateway_validation_result.model_version` |",
        "| `gateway_validation_result.summary_status` |",
        "This checkpoint does not change:",
        "`schemas/evidence-record.schema.json`",
    ])
    assert_tokens(ADR, [
        "ADR-0438",
        "Status: proposed modeling candidate",
        "Define a candidate Gateway validation result evidence trace model",
    ])
    assert_tokens(ISSUE, [
        "0438 - Add v0.6.363 Gateway Validation Result Evidence Trace Modeling Candidate",
        "Status: completed by v0.6.363",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision",
    ])

def test_v06363_index_files() -> None:
    assert_tokens(README, [
        "v0.6.363 Gateway Validation Result Evidence Trace Modeling Candidate",
        "gateway_validation_result_evidence_trace_modeling_candidate_created = true",
        "gateway_validation_result_evidence_trace_model_defined = true",
        "gateway_validation_result_evidence_record_schema_changed = false",
        "gateway_validation_result_generated_outputs_changed = false",
        "gateway_validation_result_existing_generated_output_compatibility_preserved = true",
        "v06363_schema_changed = false",
        "v06363_gateway_core_behavior_changed = false",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.363 - Gateway Validation Result Evidence Trace Modeling Candidate",
        "Gateway validation result evidence traces",
        "recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.363",
        "v0.6.364 Gateway Validation Result Evidence Trace Modeling Candidate Review and Decision",
        "no evidence-record schema change in v0.6.363",
    ])

def test_v06363_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06363_gateway_validation_result_evidence_trace_modeling_candidate.py"])

def test_v06363_no_unsupported_claims() -> None:
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
    test_v06363_primary_files()
    test_v06363_index_files()
    test_v06363_registered_in_run_all()
    test_v06363_no_unsupported_claims()
    print("v0.6.363 gateway validation result evidence trace modeling candidate checks passed")

if __name__ == "__main__":
    main()
