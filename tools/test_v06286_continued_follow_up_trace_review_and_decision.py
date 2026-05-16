from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/361-v06286-continued-follow-up-trace-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0361-add-v06286-continued-follow-up-trace-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0361-add-v06286-continued-follow-up-trace-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['continued_follow_up_trace_review_completed = true', 'continued_follow_up_trace_accepted = true', 'continued_follow_up_trace_id = continued_follow_up_trace_v06285', 'continued_follow_up_trace_review_result = accepted_as_non_claim_continued_trace_records_for_demo_path_inventory', 'continued_follow_up_trace_status = accepted_as_non_claim_continued_trace_records_for_demo_path_inventory', 'continued_follow_up_trace_applied = false', 'continued_follow_up_trace_records_accepted = true', 'continued_follow_up_trace_results_accepted = true', 'continued_follow_up_trace_dispositions_accepted = true', 'continued_follow_up_trace_gap_triage_accepted = true', 'continued_follow_up_trace_review_inputs_accepted = true', 'continued_follow_up_trace_record_count = 4', 'continued_follow_up_trace_result_count = 4', 'continued_follow_up_trace_disposition_count = 4', 'continued_follow_up_trace_gap_triage_count = 4', 'continued_follow_up_trace_conclusions_created = false', 'continued_follow_up_trace_conclusions_accepted = false', 'continued_follow_up_trace_report_findings_created = false', 'continued_follow_up_trace_report_findings_accepted = false', 'continued_follow_up_trace_review_and_decision_created = true', 'reviewed_continued_follow_up_trace_id = continued_follow_up_trace_v06285', 'reviewed_continued_follow_up_trace_candidate_id = continued_follow_up_trace_candidate_v06282', 'reviewed_continued_follow_up_trace_candidate_accepted = true', 'reviewed_continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279', 'reviewed_manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276', 'safe_runnable_demo_gap_inventory_recommended = true', 'recommended_next_work_item = safe_runnable_demo_gap_inventory', 'next_work_selection_recommended = false', 'continued_follow_up_trace_recommended = false', 'continued_follow_up_trace_candidate_recommended = false', 'report_scope_candidate_planning_recommended = false', 'accepted_defect_candidate_planning_recommended = false', 'code_inspection_report_candidate_recommended = false', 'gateway_path_integration_verification_report_recommended = false', 'report_scope_candidate_planning_created = false', 'accepted_defect_candidate_planning_created = false', 'accepted_defect_records_created = false', 'accepted_defect_records_accepted = false', 'code_inspection_report_candidate_created = false', 'code_inspection_report_created = false', 'gateway_path_integration_verification_report_candidate_created = false', 'gateway_path_integration_verification_report_created = false', 'safe_runnable_demo_gap_inventory_created = false', 'safe_runnable_demo_path_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'implementation_change_required_count = 0', 'continued_follow_up_trace_records_accepted_as_defects = false', 'continued_follow_up_trace_results_accepted_as_report_findings = false', 'continued_follow_up_trace_dispositions_accepted_as_implementation_change = false', 'continued_follow_up_trace_dispositions_accepted_as_integration_proof = false', 'continued_follow_up_trace_gap_triage_accepted_as_defect_scope = false', 'continued_follow_up_trace_observations_accepted_as_gateway_proof = false', 'continued_follow_up_trace_observations_accepted_as_missing_integration_proof = false', 'safe_runnable_demo_gap_inventory_accepted_as_runtime_demo = false', 'safe_runnable_demo_gap_inventory_accepted_as_scanner_readiness = false', 'safe_runnable_demo_gap_inventory_accepted_as_production_readiness = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'fixtures_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'publication_approval = false', 'production_readiness_claim = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['continued_follow_up_trace_review_and_decision', 'continued_follow_up_trace_review_completed', 'continued_follow_up_trace_accepted', 'continued_follow_up_trace_v06285', 'continued_follow_up_trace_records', 'continued_follow_up_trace_results', 'continued_follow_up_trace_dispositions', 'continued_follow_up_trace_gap_triage', 'continued_follow_up_trace_conclusions', 'continued_follow_up_trace_report_findings', 'continued_follow_up_trace_candidate_v06282', 'continued_follow_up_trace_planning_candidate_v06279', 'manual_trace_review_follow_up_trace_v06276', 'safe_runnable_demo_gap_inventory', 'safe_runnable_demo_path_selection', 'local_only_demo_execution_boundary_candidate', 'runtime readiness status', 'target lab gate status', 'transition gate status', 'execution authorized', 'real execution permitted', 'mock demo is not live scanner execution', 'safe mock demo', 'local-only runnable demo', 'real scanner execution remains blocked', 'Continued follow-up trace records are not accepted defects.', 'Continued follow-up trace results are not report findings.', 'Continued follow-up trace dispositions are not implementation changes.', 'Continued follow-up trace review is not gateway execution path modification.', 'Safe runnable demo gap inventory is not runtime demo readiness.', 'No private generated outputs are moved public in v0.6.286.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.286 Continued Follow-Up Trace Review and Decision', 'Previous checkpoint: v0.6.285 Continued Follow-Up Trace', 'Reviewed trace: `continued_follow_up_trace_v06285`', 'Decision result: accepted as non-claim continued trace records for demo path inventory', 'Application status: review only; no conclusions, defects, report, verification report, runtime demo, or gateway behavior changed', 'continued follow-up trace records support reviewer navigation', 'continued follow-up trace results support safe runnable demo gap inventory', 'continued follow-up trace dispositions support non-claim triage', 'continued follow-up trace gap triage supports demo-path prioritization', 'continued follow-up trace conclusions remain uncreated', 'continued follow-up trace report findings remain uncreated', 'continued follow-up trace records are not accepted defects', 'continued follow-up trace results are not report findings', 'continued follow-up trace dispositions are not implementation changes', 'recommended_next_work_item = safe_runnable_demo_gap_inventory', 'safe_runnable_demo_gap_inventory_recommended = true', 'Safe runnable demo gap inventory is not runtime demo readiness.', 'mock demo is not live scanner execution', 'real scanner execution remains blocked', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'runtime demo remains necessary but deferred', 'publication remains deferred', 'v0.6.287 Safe Runnable Demo Gap Inventory']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06286_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06286_adr_tokens() -> None:
    assert_tokens(ADR, ["ADR-0361", "Status: accepted", "Accept the v0.6.285 Continued Follow-Up Trace"] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06286_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0361 - Add v0.6.286 Continued Follow-Up Trace Review and Decision",
        "Status: completed by v0.6.286",
        "continued_follow_up_trace_review_completed = true",
        "continued_follow_up_trace_accepted = true",
        "recommended_next_work_item = safe_runnable_demo_gap_inventory",
        "Proceed to v0.6.287 Safe Runnable Demo Gap Inventory",
    ])

def test_v06286_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.286 Continued Follow-Up Trace Review and Decision",
        "continued_follow_up_trace_review_completed = true",
        "continued_follow_up_trace_accepted = true",
        "continued_follow_up_trace_id = continued_follow_up_trace_v06285",
        "continued_follow_up_trace_records_accepted = true",
        "continued_follow_up_trace_results_accepted = true",
        "continued_follow_up_trace_dispositions_accepted = true",
        "continued_follow_up_trace_gap_triage_accepted = true",
        "recommended_next_work_item = safe_runnable_demo_gap_inventory",
        "safe_runnable_demo_gap_inventory_recommended = true",
        "continued_follow_up_trace_conclusions_created = false",
        "accepted_defect_records_created = false",
        "code_inspection_report_created = false",
        "gateway_path_integration_verification_report_created = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.286 - Continued Follow-Up Trace Review and Decision",
        "Accepted the v0.6.285 Continued Follow-Up Trace",
        "continued_follow_up_trace_review_completed = true",
        "continued_follow_up_trace_accepted = true",
        "recommended_next_work_item = safe_runnable_demo_gap_inventory",
        "safe_runnable_demo_gap_inventory_recommended = true",
        "validator success is structural only",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.286",
        "v0.6.287 Safe Runnable Demo Gap Inventory",
        "no continued follow-up trace conclusions",
        "no continued follow-up trace report findings",
        "no accepted defect records",
        "no code-inspection report",
        "no gateway-path integration verification report",
        "no safe runnable demo gap inventory yet",
        "no local-only demo execution boundary candidate",
        "no gateway behavior change",
    ])

def test_v06286_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06286_continued_follow_up_trace_review_and_decision.py"])

def main() -> None:
    test_v06286_doc_tokens()
    test_v06286_adr_tokens()
    test_v06286_issue_tokens()
    test_v06286_index_tokens()
    test_v06286_registered_in_run_all()
    print("v0.6.286 continued follow-up trace review and decision checks passed")

if __name__ == "__main__":
    main()
