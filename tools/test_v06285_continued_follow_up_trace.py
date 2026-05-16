from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/360-v06285-continued-follow-up-trace.md"
ADR = ROOT / "planning/decisions/ADR-0360-add-v06285-continued-follow-up-trace.md"
ISSUE = ROOT / "planning/issues/0360-add-v06285-continued-follow-up-trace.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['continued_follow_up_trace_performed = true', 'continued_follow_up_trace_completed = true', 'continued_follow_up_trace_id = continued_follow_up_trace_v06285', 'continued_follow_up_trace_status = completed_non_claim_continued_follow_up_trace_records', 'continued_follow_up_trace_scope = bounded_continued_trace_of_accepted_continued_follow_up_trace_candidate', 'selected_work_item = continued_follow_up_trace', 'selected_work_item_status = continued_follow_up_trace_completed', 'reviewed_continued_follow_up_trace_candidate_id = continued_follow_up_trace_candidate_v06282', 'reviewed_continued_follow_up_trace_candidate_status = accepted_for_future_continued_follow_up_trace', 'reviewed_continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279', 'reviewed_manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276', 'continued_follow_up_trace_candidate_accepted = true', 'future_continued_follow_up_trace_accepted = true', 'future_continued_follow_up_trace_candidate_inputs_accepted = true', 'future_continued_follow_up_trace_candidate_questions_accepted = true', 'future_continued_follow_up_trace_candidate_scope_accepted = true', 'future_continued_follow_up_trace_candidate_record_schema_accepted = true', 'future_continued_follow_up_trace_candidate_expected_outputs_accepted = true', 'future_continued_follow_up_trace_candidate_non_claim_boundaries_accepted = true', 'future_continued_follow_up_trace_candidate_procedure_accepted = true', 'continued_follow_up_trace_records_created = true', 'continued_follow_up_trace_results_created = true', 'continued_follow_up_trace_dispositions_created = true', 'continued_follow_up_trace_gap_triage_created = true', 'continued_follow_up_trace_review_inputs_recorded = true', 'continued_follow_up_trace_record_count = 4', 'continued_follow_up_trace_result_count = 4', 'continued_follow_up_trace_disposition_count = 4', 'continued_follow_up_trace_gap_triage_count = 4', 'continued_follow_up_trace_conclusions_created = false', 'continued_follow_up_trace_report_findings_created = false', 'continued_follow_up_trace_review_and_decision_created = false', 'manual_trace_review_follow_up_trace_conclusions_created = false', 'manual_trace_review_follow_up_trace_report_findings_created = false', 'report_scope_candidate_planning_created = false', 'accepted_defect_candidate_planning_created = false', 'accepted_defect_records_created = false', 'accepted_defect_records_accepted = false', 'code_inspection_report_candidate_created = false', 'code_inspection_report_created = false', 'gateway_path_integration_verification_report_candidate_created = false', 'gateway_path_integration_verification_report_created = false', 'recommended_next_work_item = continued_follow_up_trace_review_and_decision', 'continued_follow_up_trace_review_and_decision_recommended = true', 'next_work_selection_recommended = false', 'report_scope_candidate_planning_recommended = false', 'accepted_defect_candidate_planning_recommended = false', 'code_inspection_report_candidate_recommended = false', 'gateway_path_integration_verification_report_recommended = false', 'implementation_change_required_count = 0', 'continued_follow_up_trace_records_accepted_as_defects = false', 'continued_follow_up_trace_results_accepted_as_report_findings = false', 'continued_follow_up_trace_dispositions_accepted_as_implementation_change = false', 'continued_follow_up_trace_dispositions_accepted_as_integration_proof = false', 'continued_follow_up_trace_gap_triage_accepted_as_defect_scope = false', 'continued_follow_up_trace_observations_accepted_as_gateway_proof = false', 'continued_follow_up_trace_observations_accepted_as_missing_integration_proof = false', 'continued_follow_up_trace_candidate_accepted_as_defect_planning = false', 'continued_follow_up_trace_candidate_accepted_as_report_scope = false', 'continued_follow_up_trace_candidate_accepted_as_integration_proof = false', 'continued_follow_up_trace_candidate_accepted_as_implementation_change = false', 'follow_up_trace_records_accepted_as_defects = false', 'follow_up_trace_results_accepted_as_report_findings = false', 'follow_up_trace_dispositions_accepted_as_implementation_change = false', 'gap_records_accepted_as_defects = false', 'verification_required_accepted_as_integration_proof = false', 'observed_symbol_records_accepted_as_integration_proof = false', 'observed_call_path_records_accepted_as_integration_proof = false', 'candidate_findings_accepted_as_defects = false', 'candidate_findings_accepted_as_integration_proof = false', 'candidate_findings_accepted_as_missing_integration_proof = false', 'candidate_findings_accepted_for_implementation_change = false', 'gateway_path_code_inspection_applied = false', 'gateway_execution_path_integration_verification_applied = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'validator_behavior_changed = false', 'fixture_semantics_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'record_candidate_artifact_creation_candidate_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'fixtures_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'publication_approval = false', 'production_readiness_claim = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['continued_follow_up_trace', 'continued_follow_up_trace_v06285', 'continued_follow_up_trace_review_and_decision', 'continued_follow_up_trace_candidate_v06282', 'continued_follow_up_trace_candidate', 'continued_follow_up_trace_planning_candidate_v06279', 'manual_trace_review_follow_up_trace_v06276', 'continued_follow_up_trace_records', 'continued_follow_up_trace_results', 'continued_follow_up_trace_dispositions', 'continued_follow_up_trace_gap_triage', 'continued_follow_up_trace_conclusions', 'continued_follow_up_trace_report_findings', 'continued_follow_up_trace_record_schema', 'continued_follow_up_trace_observations', 'continued_follow_up_trace_review_inputs', 'manual_trace_review_follow_up_trace_records', 'manual_trace_review_follow_up_trace_results', 'manual_trace_review_follow_up_trace_dispositions', 'manual_trace_review_follow_up_trace_gap_triage', 'report-scope candidate planning', 'accepted defect candidate planning', 'code-inspection report candidate', 'gateway-path integration verification report candidate', 'no-action non-claim closeout', 'Continued follow-up trace records are not accepted defects.', 'Continued follow-up trace results are not report findings.', 'Continued follow-up trace dispositions are not implementation changes.', 'Continued follow-up trace observations are not gateway execution path proof.', 'Continued follow-up trace is not gateway execution path modification.', 'No private generated outputs are moved public in v0.6.285.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.285 Continued Follow-Up Trace', 'Previous checkpoint: v0.6.284 Next Work Selection Using Risk-Tiered Granularity', 'Selected work item: `continued_follow_up_trace`', 'Trace result: continued follow-up trace performed with non-claim records', 'Application status: continued trace records only; no conclusions, defects, report, or gateway behavior changed', 'continued_follow_up_trace_records != accepted_defect_records', 'continued_follow_up_trace_results != report_findings', 'continued_follow_up_trace_dispositions != implementation_changes', 'continued_follow_up_trace_observations != gateway_execution_path_proof', 'continued_follow_up_trace_gap_triage != accepted_defect_scope', 'continued_follow_up_trace_conclusions_created = false', 'continued_follow_up_trace_report_findings_created = false', 'continued follow-up trace records support reviewer navigation', 'continued follow-up trace results support later review-and-decision', 'continued follow-up trace dispositions support non-claim triage', 'continued follow-up trace gap triage supports prioritization', 'continued follow-up trace does not establish accepted defects', 'continued follow-up trace does not establish report findings', 'continued follow-up trace does not establish gateway integration proof', 'continued follow-up trace does not establish missing integration proof', 'continued follow-up trace does not require implementation changes', 'recommended_next_work_item = continued_follow_up_trace_review_and_decision', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'runtime demo remains necessary but deferred', 'publication remains deferred', 'v0.6.286 Continued Follow-Up Trace Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06285_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06285_adr_tokens() -> None:
    assert_tokens(ADR, ["ADR-0360", "Status: accepted", "Perform the bounded Continued Follow-Up Trace"] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06285_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0360 - Add v0.6.285 Continued Follow-Up Trace",
        "Status: completed by v0.6.285",
        "continued_follow_up_trace_performed = true",
        "continued_follow_up_trace_records_created = true",
        "Proceed to v0.6.286 Continued Follow-Up Trace Review and Decision",
    ])

def test_v06285_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.285 Continued Follow-Up Trace",
        "continued_follow_up_trace_performed = true",
        "continued_follow_up_trace_completed = true",
        "continued_follow_up_trace_id = continued_follow_up_trace_v06285",
        "continued_follow_up_trace_records_created = true",
        "continued_follow_up_trace_results_created = true",
        "continued_follow_up_trace_dispositions_created = true",
        "continued_follow_up_trace_gap_triage_created = true",
        "continued_follow_up_trace_conclusions_created = false",
        "accepted_defect_records_created = false",
        "code_inspection_report_created = false",
        "gateway_path_integration_verification_report_created = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.285 - Continued Follow-Up Trace",
        "Performed the bounded Continued Follow-Up Trace.",
        "continued_follow_up_trace_performed = true",
        "continued_follow_up_trace_completed = true",
        "continued_follow_up_trace_id = continued_follow_up_trace_v06285",
        "continued_follow_up_trace_records",
        "continued_follow_up_trace_conclusions_created = false",
        "accepted_defect_records_created = false",
        "validator success is structural only",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.285",
        "v0.6.286 Continued Follow-Up Trace Review and Decision",
        "no continued follow-up trace conclusions",
        "no continued follow-up trace report findings",
        "no accepted defect records",
        "no code-inspection report",
        "no gateway-path integration verification report",
        "no gateway behavior change",
    ])

def test_v06285_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06285_continued_follow_up_trace.py"])

def main() -> None:
    test_v06285_doc_tokens()
    test_v06285_adr_tokens()
    test_v06285_issue_tokens()
    test_v06285_index_tokens()
    test_v06285_registered_in_run_all()
    print("v0.6.285 continued follow-up trace checks passed")

if __name__ == "__main__":
    main()
