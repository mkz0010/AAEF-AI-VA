from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/354-v06279-continued-follow-up-trace-planning-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0354-add-v06279-continued-follow-up-trace-planning-candidate.md"
ISSUE = ROOT / "planning/issues/0354-add-v06279-continued-follow-up-trace-planning-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "continued_follow_up_trace_planning_candidate_created = true",
    "continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279",
    "continued_follow_up_trace_planning_candidate_status = candidate_not_applied",
    "continued_follow_up_trace_planning_candidate_scope = documentation_only_planning_candidate_for_accepted_non_claim_follow_up_trace_records",
    "selected_work_item = continued_follow_up_trace_planning",
    "selected_work_item_status = continued_follow_up_trace_planning_candidate_created",
    "reviewed_manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
    "reviewed_manual_trace_review_follow_up_trace_review_result = accepted_as_non_claim_follow_up_trace_records_for_next_work_selection",
    "reviewed_manual_trace_review_follow_up_trace_records_accepted = true",
    "reviewed_manual_trace_review_follow_up_trace_results_accepted = true",
    "reviewed_manual_trace_review_follow_up_trace_dispositions_accepted = true",
    "reviewed_manual_trace_review_follow_up_trace_gap_triage_accepted = true",
    "continued_follow_up_trace_planning_candidate_input_records_defined = true",
    "continued_follow_up_trace_planning_candidate_questions_defined = true",
    "continued_follow_up_trace_planning_candidate_scope_defined = true",
    "continued_follow_up_trace_planning_candidate_decision_options_defined = true",
    "continued_follow_up_trace_planning_candidate_non_claim_boundaries_defined = true",
    "continued_follow_up_trace_planning_candidate_procedure_defined = true",
    "continued_follow_up_trace_planning_candidate_expected_outputs_defined = true",
    "continued_follow_up_trace_planning_candidate_review_inputs_defined = true",
    "continued_follow_up_trace_planning_completed = false",
    "continued_follow_up_trace_planning_applied = false",
    "continued_follow_up_trace_records_created = false",
    "continued_follow_up_trace_results_created = false",
    "continued_follow_up_trace_dispositions_created = false",
    "continued_follow_up_trace_gap_triage_created = false",
    "continued_follow_up_trace_conclusions_created = false",
    "continued_follow_up_trace_report_findings_created = false",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_follow_up_trace_report_findings_created = false",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
    "report_scope_candidate_planning_created = false",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_candidate_created = false",
    "gateway_path_integration_verification_report_created = false",
    "recommended_next_work_item = continued_follow_up_trace_planning_candidate_review_and_decision",
    "continued_follow_up_trace_planning_candidate_review_and_decision_recommended = true",
    "report_scope_candidate_planning_recommended = false",
    "accepted_defect_candidate_planning_recommended = false",
    "code_inspection_report_candidate_recommended = false",
    "gateway_path_integration_verification_report_recommended = false",
    "implementation_change_required_count = 0",
    "continued_follow_up_trace_planning_candidate_accepted_as_defect_planning = false",
    "continued_follow_up_trace_planning_candidate_accepted_as_report_scope = false",
    "continued_follow_up_trace_planning_candidate_accepted_as_integration_proof = false",
    "continued_follow_up_trace_planning_candidate_accepted_as_implementation_change = false",
    "continued_follow_up_trace_records_accepted_as_defects = false",
    "continued_follow_up_trace_results_accepted_as_report_findings = false",
    "continued_follow_up_trace_dispositions_accepted_as_implementation_change = false",
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
    "continued_follow_up_trace_planning_candidate",
    "continued_follow_up_trace_planning_candidate_v06279",
    "continued_follow_up_trace_planning_candidate_review_and_decision",
    "continued_follow_up_trace_planning",
    "continued_follow_up_trace_records",
    "continued_follow_up_trace_results",
    "continued_follow_up_trace_dispositions",
    "continued_follow_up_trace_gap_triage",
    "continued_follow_up_trace_conclusions",
    "continued_follow_up_trace_report_findings",
    "continued_follow_up_trace_decision_options",
    "manual_trace_review_follow_up_trace_review_and_decision",
    "manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_dispositions",
    "manual_trace_review_follow_up_trace_gap_triage",
    "manual_trace_review_follow_up_trace_conclusions",
    "manual_trace_review_follow_up_trace_report_findings",
    "report-scope candidate planning",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "no-action non-claim closeout",
    "Follow-up trace records are not accepted defects.",
    "Follow-up trace results are not report findings.",
    "Follow-up trace dispositions are not implementation changes.",
    "Continued follow-up trace planning candidate is not continued trace execution.",
    "Continued follow-up trace planning candidate is not defect acceptance.",
    "Continued follow-up trace planning candidate is not report finding creation.",
    "Continued follow-up trace planning candidate is not gateway execution path modification.",
    "No private generated outputs are moved public in v0.6.279.",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.279 Continued Follow-Up Trace Planning Candidate",
    "Previous checkpoint: v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `continued_follow_up_trace_planning`",
    "Candidate result: continued follow-up trace planning candidate created",
    "Application status: candidate only; no continued trace records, defects, report, or gateway behavior changed",
    "continued_follow_up_trace_planning_candidate != continued_follow_up_trace_records",
    "continued_follow_up_trace_planning_candidate != continued_follow_up_trace_results",
    "continued_follow_up_trace_planning_candidate != continued_follow_up_trace_conclusions",
    "continued_follow_up_trace_planning_candidate != accepted_defect_records",
    "continued_follow_up_trace_planning_candidate != code_inspection_report",
    "continued_follow_up_trace_planning_candidate != gateway_path_integration_verification_report",
    "continued_follow_up_trace_question_01",
    "continued_follow_up_trace_question_10",
    "continued_follow_up_trace_planning_candidate_review_and_decision",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.280 Continued Follow-Up Trace Planning Candidate Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06279_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)


def test_v06279_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0354",
            "Status: proposed candidate",
            "Create a Continued Follow-Up Trace Planning Candidate.",
            "continued_follow_up_trace_planning_candidate_created = true",
            "continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279",
            "Continued follow-up trace planning candidate is not continued trace execution.",
            "Continued follow-up trace planning candidate is not defect acceptance.",
            "Continued follow-up trace planning candidate is not report finding creation.",
            "Continued follow-up trace planning candidate is not gateway execution path modification.",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06279_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0354 - Add v0.6.279 Continued Follow-Up Trace Planning Candidate",
            "Status: completed by v0.6.279",
            "continued_follow_up_trace_planning_candidate_created = true",
            "continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279",
            "continued_follow_up_trace_planning_candidate_questions_defined = true",
            "continued_follow_up_trace_planning_candidate_decision_options_defined = true",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "continued_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.280 Continued Follow-Up Trace Planning Candidate Review and Decision",
        ],
    )


def test_v06279_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.279 Continued Follow-Up Trace Planning Candidate",
            "continued_follow_up_trace_planning_candidate_created = true",
            "continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279",
            "continued_follow_up_trace_planning_candidate_status = candidate_not_applied",
            "continued_follow_up_trace_planning_candidate_questions_defined = true",
            "continued_follow_up_trace_planning_candidate_decision_options_defined = true",
            "continued_follow_up_trace_planning_completed = false",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "continued_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.279 - Continued Follow-Up Trace Planning Candidate",
            "Created a documentation-only Continued Follow-Up Trace Planning Candidate.",
            "continued_follow_up_trace_planning_candidate_created = true",
            "continued_follow_up_trace_planning_candidate_id = continued_follow_up_trace_planning_candidate_v06279",
            "continued_follow_up_trace_planning_candidate_status = candidate_not_applied",
            "continued_follow_up_trace_records_created = false",
            "continued_follow_up_trace_results_created = false",
            "continued_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.279",
            "v0.6.280 Continued Follow-Up Trace Planning Candidate Review and Decision",
            "no continued follow-up trace records",
            "no continued follow-up trace results",
            "no continued follow-up trace conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06279_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06279_continued_follow_up_trace_planning_candidate.py"])


def main() -> None:
    test_v06279_doc_tokens()
    test_v06279_adr_tokens()
    test_v06279_issue_tokens()
    test_v06279_index_tokens()
    test_v06279_registered_in_run_all()
    print("v0.6.279 continued follow-up trace planning candidate checks passed")


if __name__ == "__main__":
    main()
