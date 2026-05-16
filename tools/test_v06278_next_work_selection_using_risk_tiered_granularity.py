from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/353-v06278-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0353-add-v06278-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0353-add-v06278-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = continued_follow_up_trace_planning",
    "selected_work_item_status = selected_for_next_continued_follow_up_trace_planning_candidate",
    "selected_work_item_reason = accepted_non_claim_follow_up_trace_records_require_continued_planning_before_report_defect_or_implementation",
    "continued_follow_up_trace_planning_selected = true",
    "continued_follow_up_trace_planning_candidate_created = false",
    "continued_follow_up_trace_planning_completed = false",
    "continued_follow_up_trace_records_created = false",
    "continued_follow_up_trace_results_created = false",
    "manual_trace_review_follow_up_trace_review_completed = true",
    "manual_trace_review_follow_up_trace_accepted = true",
    "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_review_result = accepted_as_non_claim_follow_up_trace_records_for_next_work_selection",
    "manual_trace_review_follow_up_trace_records_accepted = true",
    "manual_trace_review_follow_up_trace_results_accepted = true",
    "manual_trace_review_follow_up_trace_dispositions_accepted = true",
    "manual_trace_review_follow_up_trace_gap_triage_accepted = true",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_follow_up_trace_report_findings_created = false",
    "report_scope_candidate_planning_selected = false",
    "report_scope_candidate_planning_created = false",
    "accepted_defect_candidate_planning_selected = false",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "code_inspection_report_candidate_selected = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_selected = false",
    "gateway_path_integration_verification_report_candidate_created = false",
    "gateway_path_integration_verification_report_created = false",
    "no_action_non_claim_closeout_selected = false",
    "gateway_behavior_implementation_change_selected = false",
    "implementation_change_required_count = 0",
    "follow_up_trace_records_accepted_as_defects = false",
    "follow_up_trace_results_accepted_as_report_findings = false",
    "follow_up_trace_dispositions_accepted_as_implementation_change = false",
    "follow_up_trace_dispositions_accepted_as_integration_proof = false",
    "gateway_execution_path_behavior_modified = false",
    "tool_gateway_behavior_changed = false",
    "adapter_behavior_changed = false",
    "schema_changed = false",
    "runtime_behavior_changed = false",
    "scanner_behavior_changed = false",
    "record_candidate_artifacts_created = false",
    "actual_records_created = false",
    "fixtures_created = false",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
    "publication_approval = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]

REQUIRED_SHARED_TOKENS = [
    "continued_follow_up_trace_planning",
    "continued_follow_up_trace_planning_selected",
    "continued_follow_up_trace_planning_candidate",
    "continued_follow_up_trace_records",
    "continued_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_review_and_decision",
    "manual_trace_review_follow_up_trace_review_completed",
    "manual_trace_review_follow_up_trace_accepted",
    "manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_dispositions",
    "manual_trace_review_follow_up_trace_gap_triage",
    "manual_trace_review_follow_up_trace_conclusions",
    "manual_trace_review_follow_up_trace_report_findings",
    "next_work_selection_using_risk_tiered_granularity",
    "report-scope candidate planning",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "no-action non-claim closeout",
    "Follow-up trace records are not accepted defects.",
    "Follow-up trace results are not report findings.",
    "Follow-up trace dispositions are not implementation changes.",
    "Continued follow-up trace planning is not defect acceptance.",
    "Continued follow-up trace planning is not report finding creation.",
    "Continued follow-up trace planning is not gateway execution path modification.",
    "No private generated outputs are moved public in v0.6.278.",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
    "Selection result: `continued_follow_up_trace_planning`",
    "Application status: selection only; no continued follow-up trace planning candidate created and no gateway behavior changed",
    "continued_follow_up_trace_planning_recommended = true",
    "continued_follow_up_trace_planning_selected != continued_follow_up_trace_planning_candidate_created",
    "continued_follow_up_trace_planning != continued_follow_up_trace_records",
    "continued_follow_up_trace_planning != continued_follow_up_trace_results",
    "continued_follow_up_trace_planning != follow_up_trace_conclusions",
    "continued_follow_up_trace_planning != accepted_defect_records",
    "continued_follow_up_trace_planning != code_inspection_report",
    "continued_follow_up_trace_planning != gateway_path_integration_verification_report",
    "continued follow-up trace planning candidate",
    "continued_follow_up_trace_planning_candidate_id",
    "continued_follow_up_trace_decision_options",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.279 Continued Follow-Up Trace Planning Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06278_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)


def test_v06278_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0353",
            "Status: accepted",
            "Select the following next work item",
            "continued_follow_up_trace_planning",
            "This is a selection-only checkpoint.",
            "Continued follow-up trace planning is not defect acceptance.",
            "Continued follow-up trace planning is not report finding creation.",
            "Continued follow-up trace planning is not gateway execution path modification.",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06278_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0353 - Add v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.278",
            "selected_work_item = continued_follow_up_trace_planning",
            "continued_follow_up_trace_planning_selected = true",
            "continued_follow_up_trace_planning_candidate_created = false",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "manual_trace_review_follow_up_trace_records_accepted = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.279 Continued Follow-Up Trace Planning Candidate",
        ],
    )


def test_v06278_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
            "selected_work_item = continued_follow_up_trace_planning",
            "continued_follow_up_trace_planning_selected = true",
            "continued_follow_up_trace_planning_candidate_created = false",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "manual_trace_review_follow_up_trace_records_accepted = true",
            "manual_trace_review_follow_up_trace_results_accepted = true",
            "manual_trace_review_follow_up_trace_dispositions_accepted = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "manual_trace_review_follow_up_trace_report_findings_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.278 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `continued_follow_up_trace_planning` as the next work item",
            "next_work_selection_completed = true",
            "continued_follow_up_trace_planning_selected = true",
            "continued_follow_up_trace_planning_candidate_created = false",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.278",
            "v0.6.279 Continued Follow-Up Trace Planning Candidate",
            "no continued follow-up trace planning candidate",
            "no continued follow-up trace records",
            "no continued follow-up trace results",
            "no follow-up trace conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06278_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06278_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06278_doc_tokens()
    test_v06278_adr_tokens()
    test_v06278_issue_tokens()
    test_v06278_index_tokens()
    test_v06278_registered_in_run_all()
    print("v0.6.278 next work selection checks passed")


if __name__ == "__main__":
    main()
