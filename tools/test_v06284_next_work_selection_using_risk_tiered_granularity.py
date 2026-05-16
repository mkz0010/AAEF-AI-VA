from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/359-v06284-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0359-add-v06284-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0359-add-v06284-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['next_work_selection_completed = true', 'selected_work_item = continued_follow_up_trace', 'selected_work_item_status = selected_for_next_continued_follow_up_trace_checkpoint', 'selected_work_item_reason = accepted_continued_follow_up_trace_candidate_requires_selection_before_records_report_defect_or_implementation', 'continued_follow_up_trace_selected = true', 'continued_follow_up_trace_candidate_review_completed = true', 'continued_follow_up_trace_candidate_accepted = true', 'continued_follow_up_trace_candidate_id = continued_follow_up_trace_candidate_v06282', 'continued_follow_up_trace_candidate_review_result = accepted_for_future_continued_follow_up_trace', 'future_continued_follow_up_trace_accepted = true', 'continued_follow_up_trace_recommended = true', 'continued_follow_up_trace_performed = false', 'continued_follow_up_trace_completed = false', 'continued_follow_up_trace_records_created = false', 'continued_follow_up_trace_results_created = false', 'continued_follow_up_trace_dispositions_created = false', 'continued_follow_up_trace_gap_triage_created = false', 'continued_follow_up_trace_conclusions_created = false', 'continued_follow_up_trace_report_findings_created = false', 'continued_follow_up_trace_review_and_decision_created = false', 'report_scope_candidate_planning_selected = false', 'report_scope_candidate_planning_created = false', 'accepted_defect_candidate_planning_selected = false', 'accepted_defect_candidate_planning_created = false', 'accepted_defect_records_created = false', 'accepted_defect_records_accepted = false', 'code_inspection_report_candidate_selected = false', 'code_inspection_report_candidate_created = false', 'code_inspection_report_created = false', 'gateway_path_integration_verification_report_selected = false', 'gateway_path_integration_verification_report_candidate_created = false', 'gateway_path_integration_verification_report_created = false', 'no_action_non_claim_closeout_selected = false', 'gateway_behavior_implementation_change_selected = false', 'implementation_change_required_count = 0', 'continued_follow_up_trace_candidate_accepted_as_defect_planning = false', 'continued_follow_up_trace_candidate_accepted_as_report_scope = false', 'continued_follow_up_trace_candidate_accepted_as_integration_proof = false', 'continued_follow_up_trace_candidate_accepted_as_implementation_change = false', 'continued_follow_up_trace_records_accepted_as_defects = false', 'continued_follow_up_trace_results_accepted_as_report_findings = false', 'continued_follow_up_trace_dispositions_accepted_as_implementation_change = false', 'continued_follow_up_trace_dispositions_accepted_as_integration_proof = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'fixtures_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'publication_approval = false', 'production_readiness_claim = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['continued_follow_up_trace', 'continued_follow_up_trace_selected', 'continued_follow_up_trace_candidate_review_and_decision', 'continued_follow_up_trace_candidate_review_completed', 'continued_follow_up_trace_candidate_accepted', 'continued_follow_up_trace_candidate_v06282', 'continued_follow_up_trace_candidate', 'continued_follow_up_trace_records', 'continued_follow_up_trace_results', 'continued_follow_up_trace_dispositions', 'continued_follow_up_trace_gap_triage', 'continued_follow_up_trace_conclusions', 'continued_follow_up_trace_report_findings', 'next_work_selection_using_risk_tiered_granularity', 'report-scope candidate planning', 'accepted defect candidate planning', 'code-inspection report candidate', 'gateway-path integration verification report candidate', 'no-action non-claim closeout', 'Continued follow-up trace selection is not continued trace execution.', 'Continued follow-up trace selection is not defect acceptance.', 'Continued follow-up trace selection is not report finding creation.', 'Continued follow-up trace selection is not gateway execution path modification.', 'No private generated outputs are moved public in v0.6.284.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.284 Next Work Selection Using Risk-Tiered Granularity', 'Previous checkpoint: v0.6.283 Continued Follow-Up Trace Candidate Review and Decision', 'Selection result: `continued_follow_up_trace`', 'Application status: selection only; no continued follow-up trace records created and no gateway behavior changed', 'continued_follow_up_trace_recommended = true', 'continued_follow_up_trace_selected != continued_follow_up_trace_performed', 'continued_follow_up_trace != continued_follow_up_trace_records', 'continued_follow_up_trace != continued_follow_up_trace_results', 'continued_follow_up_trace != continued_follow_up_trace_conclusions', 'continued_follow_up_trace != accepted_defect_records', 'continued_follow_up_trace != code_inspection_report', 'continued_follow_up_trace != gateway_path_integration_verification_report', 'continued_follow_up_trace != gateway_execution_path_behavior_modified', 'continued_follow_up_trace_id', 'continued_follow_up_trace_record_schema', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'runtime demo remains necessary but deferred', 'publication remains deferred', 'v0.6.285 Continued Follow-Up Trace']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06284_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06284_adr_tokens() -> None:
    assert_tokens(ADR, ["ADR-0359", "Status: accepted", "Select the following next work item"] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06284_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0359 - Add v0.6.284 Next Work Selection Using Risk-Tiered Granularity",
        "Status: completed by v0.6.284",
        "continued_follow_up_trace",
        "Proceed to v0.6.285 Continued Follow-Up Trace",
    ])

def test_v06284_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.284 Next Work Selection Using Risk-Tiered Granularity",
        "selected_work_item = continued_follow_up_trace",
        "continued_follow_up_trace_selected = true",
        "continued_follow_up_trace_performed = false",
        "continued_follow_up_trace_records_created = false",
        "continued_follow_up_trace_results_created = false",
        "continued_follow_up_trace_conclusions_created = false",
        "accepted_defect_records_created = false",
        "code_inspection_report_created = false",
        "gateway_path_integration_verification_report_created = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.284 - Next Work Selection Using Risk-Tiered Granularity",
        "Selected `continued_follow_up_trace` as the next work item",
        "next_work_selection_completed = true",
        "continued_follow_up_trace_selected = true",
        "continued_follow_up_trace_performed = false",
        "validator success is structural only",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.284",
        "v0.6.285 Continued Follow-Up Trace",
        "no continued follow-up trace records",
        "no continued follow-up trace results",
        "no continued follow-up trace conclusions",
        "no accepted defect records",
        "no code-inspection report",
        "no gateway-path integration verification report",
        "no gateway behavior change",
    ])

def test_v06284_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06284_next_work_selection_using_risk_tiered_granularity.py"])

def main() -> None:
    test_v06284_doc_tokens()
    test_v06284_adr_tokens()
    test_v06284_issue_tokens()
    test_v06284_index_tokens()
    test_v06284_registered_in_run_all()
    print("v0.6.284 next work selection checks passed")

if __name__ == "__main__":
    main()
