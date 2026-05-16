from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/352-v06277-manual-trace-review-follow-up-trace-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0352-add-v06277-manual-trace-review-follow-up-trace-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0352-add-v06277-manual-trace-review-follow-up-trace-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "manual_trace_review_follow_up_trace_review_completed = true",
    "manual_trace_review_follow_up_trace_accepted = true",
    "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_review_result = accepted_as_non_claim_follow_up_trace_records_for_next_work_selection",
    "manual_trace_review_follow_up_trace_status = accepted_as_non_claim_follow_up_trace_records_for_next_work_selection",
    "manual_trace_review_follow_up_trace_applied = false",
    "manual_trace_review_follow_up_trace_records_accepted = true",
    "manual_trace_review_follow_up_trace_results_accepted = true",
    "manual_trace_review_follow_up_trace_dispositions_accepted = true",
    "manual_trace_review_follow_up_trace_gap_triage_accepted = true",
    "manual_trace_review_follow_up_trace_review_inputs_accepted = true",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_follow_up_trace_conclusions_accepted = false",
    "manual_trace_review_follow_up_trace_report_findings_created = false",
    "manual_trace_review_follow_up_trace_report_findings_accepted = false",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
    "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
    "next_work_selection_recommended = true",
    "continued_follow_up_trace_planning_recommended = true",
    "code_inspection_report_candidate_recommended = false",
    "accepted_defect_candidate_planning_recommended = false",
    "gateway_path_integration_verification_report_recommended = false",
    "implementation_change_required_count = 0",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_candidate_created = false",
    "gateway_path_integration_verification_report_created = false",
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
    "manual_trace_review_follow_up_trace_candidate_v06273",
    "manual_trace_review_records",
    "manual_trace_review_results",
    "manual_trace_review_dispositions",
    "manual_trace_review_gap_triage",
    "manual_trace_review_rationale",
    "manual_trace_review_disposition",
    "manual_trace_review_scope",
    "next_work_selection_using_risk_tiered_granularity",
    "continued_follow_up_trace_planning",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "Follow-up trace records are not accepted defects.",
    "Follow-up trace results are not report findings.",
    "Follow-up trace dispositions are not implementation changes.",
    "Follow-up trace review is not defect acceptance.",
    "Follow-up trace review is not report finding creation.",
    "Follow-up trace review is not gateway execution path modification.",
    "No private generated outputs are moved public in v0.6.277.",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
    "Previous checkpoint: v0.6.276 Manual Trace Review Follow-Up Trace",
    "Reviewed trace: `manual_trace_review_follow_up_trace_v06276`",
    "Decision result: accepted as non-claim follow-up trace records for next-work selection",
    "Application status: review only; no conclusions, defects, report, or gateway behavior changed",
    "follow-up trace records support reviewer navigation",
    "follow-up trace results support next-work selection",
    "follow-up trace dispositions support non-claim triage",
    "follow-up trace gap triage supports prioritization",
    "follow-up trace conclusions remain uncreated",
    "follow-up trace report findings remain uncreated",
    "follow-up trace records are not accepted defects",
    "follow-up trace results are not report findings",
    "follow-up trace dispositions are not implementation changes",
    "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
    "continued_follow_up_trace_planning_recommended = true",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06277_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)


def test_v06277_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0352",
            "Status: accepted",
            "Accept the v0.6.276 Manual Trace Review Follow-Up Trace",
            "manual_trace_review_follow_up_trace_review_completed = true",
            "manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_records_accepted = true",
            "Follow-up trace review is not defect acceptance.",
            "Follow-up trace records are not accepted defects.",
            "Follow-up trace results are not report findings.",
            "Follow-up trace dispositions are not implementation changes.",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06277_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0352 - Add v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
            "Status: completed by v0.6.277",
            "manual_trace_review_follow_up_trace_review_completed = true",
            "manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_review_result = accepted_as_non_claim_follow_up_trace_records_for_next_work_selection",
            "manual_trace_review_follow_up_trace_records_accepted = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06277_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
            "manual_trace_review_follow_up_trace_review_completed = true",
            "manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
            "manual_trace_review_follow_up_trace_records_accepted = true",
            "manual_trace_review_follow_up_trace_results_accepted = true",
            "manual_trace_review_follow_up_trace_dispositions_accepted = true",
            "manual_trace_review_follow_up_trace_gap_triage_accepted = true",
            "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.277 - Manual Trace Review Follow-Up Trace Review and Decision",
            "Accepted the v0.6.276 Manual Trace Review Follow-Up Trace",
            "manual_trace_review_follow_up_trace_review_completed = true",
            "manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
            "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "accepted_defect_records_created = false",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.277",
            "v0.6.278 Next Work Selection Using Risk-Tiered Granularity",
            "continued_follow_up_trace_planning",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report candidate",
            "no follow-up trace conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06277_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06277_manual_trace_review_follow_up_trace_review_and_decision.py"])


def main() -> None:
    test_v06277_doc_tokens()
    test_v06277_adr_tokens()
    test_v06277_issue_tokens()
    test_v06277_index_tokens()
    test_v06277_registered_in_run_all()
    print("v0.6.277 manual trace review follow-up trace review and decision checks passed")


if __name__ == "__main__":
    main()
