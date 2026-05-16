from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/350-v06275-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0350-add-v06275-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0350-add-v06275-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = manual_trace_review_follow_up_trace",
    "selected_work_item_status = selected_for_next_follow_up_trace_checkpoint",
    "selected_work_item_reason = accepted_follow_up_trace_candidate_requires_follow_up_trace_before_report_defect_or_implementation",
    "manual_trace_review_follow_up_trace_selected = true",
    "manual_trace_review_follow_up_trace_candidate_accepted = true",
    "future_manual_trace_review_follow_up_trace_accepted = true",
    "manual_trace_review_follow_up_trace_performed = false",
    "manual_trace_review_follow_up_trace_completed = false",
    "manual_trace_review_follow_up_trace_records_created = false",
    "manual_trace_review_follow_up_trace_results_created = false",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_follow_up_trace_review_and_decision_created = false",
    "manual_trace_review_follow_up_trace_candidate_id = manual_trace_review_follow_up_trace_candidate_v06273",
    "manual_trace_review_follow_up_trace_candidate_review_completed = true",
    "manual_trace_review_follow_up_trace_candidate_accepted = true",
    "manual_trace_review_follow_up_trace_candidate_review_result = accepted_for_future_manual_trace_review_follow_up_trace",
    "future_follow_up_trace_candidate_lanes_accepted = true",
    "future_follow_up_trace_candidate_input_records_accepted = true",
    "future_follow_up_trace_candidate_questions_accepted = true",
    "future_follow_up_trace_candidate_scope_accepted = true",
    "future_follow_up_trace_candidate_record_schema_accepted = true",
    "future_follow_up_trace_candidate_expected_outputs_accepted = true",
    "future_follow_up_trace_candidate_non_claim_boundaries_accepted = true",
    "future_follow_up_trace_candidate_procedure_accepted = true",
    "manual_trace_review_records_accepted = true",
    "manual_trace_review_results_accepted = true",
    "manual_trace_review_dispositions_accepted = true",
    "manual_trace_review_gap_triage_accepted = true",
    "manual_trace_review_follow_up_trace_candidates_accepted = true",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
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
    "gateway_behavior_implementation_change_selected = false",
    "implementation_change_required_count = 0",
    "manual_trace_review_records_accepted_as_implementation_change = false",
    "manual_trace_review_results_accepted_as_report_findings = false",
    "manual_trace_review_dispositions_accepted_as_defects = false",
    "manual_trace_review_dispositions_accepted_as_report_findings = false",
    "manual_trace_review_dispositions_accepted_as_integration_proof = false",
    "follow_up_trace_candidate_accepted_as_implementation_change = false",
    "follow_up_trace_candidate_questions_accepted_as_conclusions = false",
    "follow_up_trace_candidate_scope_accepted_as_defect_scope = false",
    "gap_records_accepted_as_defects = false",
    "verification_required_accepted_as_integration_proof = false",
    "observed_symbol_records_accepted_as_integration_proof = false",
    "observed_call_path_records_accepted_as_integration_proof = false",
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
    "manual_trace_review_follow_up_trace",
    "manual_trace_review_follow_up_trace_candidate",
    "manual_trace_review_follow_up_trace_candidate_v06273",
    "manual_trace_review_follow_up_trace_candidate_review_completed",
    "manual_trace_review_follow_up_trace_candidate_accepted",
    "manual_trace_review_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_conclusions",
    "future_manual_trace_review_follow_up_trace_accepted",
    "future_follow_up_trace_candidate_lanes_accepted",
    "future_follow_up_trace_candidate_questions_accepted",
    "future_follow_up_trace_candidate_record_schema_accepted",
    "follow_up_trace_candidate_lanes",
    "follow_up_trace_candidate_questions",
    "follow_up_trace_candidate_scope",
    "follow_up_trace_candidate_record_schema",
    "follow_up_trace_candidate_expected_outputs",
    "follow_up_trace_candidate_non_claim_boundaries",
    "follow_up_trace_candidate_procedure",
    "manual_trace_review_records",
    "manual_trace_review_results",
    "manual_trace_review_dispositions",
    "manual_trace_review_gap_triage",
    "manual_trace_review_rationale",
    "manual_trace_review_disposition",
    "manual_trace_review_scope",
    "lane_01_pre_dispatch_enforcement_review",
    "lane_03_adapter_boundary_review",
    "lane_05_evidence_linkage_review",
    "verification_required statuses",
    "manual_review_requires_follow_up",
    "manual_review_candidate_for_follow_up_trace",
    "manual_review_gap_triage_only",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "Manual trace review records are not accepted defects.",
    "Manual trace review results are not report findings.",
    "Manual trace review dispositions are not implementation changes.",
    "Follow-up trace candidate is not follow-up trace execution.",
    "Follow-up trace candidate acceptance is not follow-up trace execution.",
    "Follow-up trace selection is not follow-up trace execution.",
    "No private generated outputs are moved public in v0.6.275.",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.275 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.274 Manual Trace Review Follow-Up Trace Candidate Review and Decision",
    "Selection result: `manual_trace_review_follow_up_trace`",
    "Application status: selection only; no follow-up trace performed and no gateway behavior changed",
    "recommended_next_work_item = manual_trace_review_follow_up_trace",
    "manual_trace_review_follow_up_trace_selected != manual_trace_review_follow_up_trace_performed",
    "manual_trace_review_follow_up_trace_selection != manual_trace_review_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_selection != manual_trace_review_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_selection != manual_trace_review_follow_up_trace_conclusions",
    "manual_trace_review_follow_up_trace_selection != accepted_defect_records",
    "manual_trace_review_follow_up_trace_selection != code_inspection_report",
    "manual_trace_review_follow_up_trace_selection != gateway_path_integration_verification_report",
    "Follow-up trace selection is not follow-up trace execution.",
    "follow-up trace selection is not gateway execution path modification",
    "manual trace review records are not accepted defects",
    "manual trace review results are not report findings",
    "manual trace review dispositions are not implementation changes",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.276 Manual Trace Review Follow-Up Trace",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06275_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)


def test_v06275_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0350",
            "Status: accepted",
            "Select the following next work item",
            "manual_trace_review_follow_up_trace",
            "This is a selection-only checkpoint.",
            "Follow-up trace selection is not follow-up trace execution.",
            "Manual trace review records are not accepted defects.",
            "Manual trace review results are not report findings.",
            "Manual trace review dispositions are not implementation changes.",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06275_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0350 - Add v0.6.275 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.275",
            "selected_work_item = manual_trace_review_follow_up_trace",
            "manual_trace_review_follow_up_trace_selected = true",
            "manual_trace_review_follow_up_trace_performed = false",
            "manual_trace_review_follow_up_trace_records_created = false",
            "manual_trace_review_follow_up_trace_results_created = false",
            "future_manual_trace_review_follow_up_trace_accepted = true",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.276 Manual Trace Review Follow-Up Trace",
        ],
    )


def test_v06275_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.275 Next Work Selection Using Risk-Tiered Granularity",
            "selected_work_item = manual_trace_review_follow_up_trace",
            "manual_trace_review_follow_up_trace_selected = true",
            "manual_trace_review_follow_up_trace_candidate_accepted = true",
            "future_manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_performed = false",
            "manual_trace_review_follow_up_trace_records_created = false",
            "manual_trace_review_follow_up_trace_results_created = false",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "manual_trace_review_conclusions_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.275 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `manual_trace_review_follow_up_trace` as the next work item",
            "next_work_selection_completed = true",
            "manual_trace_review_follow_up_trace_selected = true",
            "manual_trace_review_follow_up_trace_candidate_accepted = true",
            "future_manual_trace_review_follow_up_trace_accepted = true",
            "manual_trace_review_follow_up_trace_performed = false",
            "manual_trace_review_follow_up_trace_records_created = false",
            "manual_trace_review_follow_up_trace_results_created = false",
            "accepted_defect_records_created = false",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.275",
            "v0.6.276 Manual Trace Review Follow-Up Trace",
            "no follow-up trace records",
            "no follow-up trace results",
            "no follow-up trace conclusions",
            "no manual trace review conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06275_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06275_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06275_doc_tokens()
    test_v06275_adr_tokens()
    test_v06275_issue_tokens()
    test_v06275_index_tokens()
    test_v06275_registered_in_run_all()
    print("v0.6.275 next work selection checks passed")


if __name__ == "__main__":
    main()
