from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/351-v06276-manual-trace-review-follow-up-trace.md"
ADR = ROOT / "planning/decisions/ADR-0351-add-v06276-manual-trace-review-follow-up-trace.md"
ISSUE = ROOT / "planning/issues/0351-add-v06276-manual-trace-review-follow-up-trace.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "manual_trace_review_follow_up_trace_performed = true",
    "manual_trace_review_follow_up_trace_completed = true",
    "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_status = completed_non_claim_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_scope = bounded_follow_up_trace_of_accepted_non_claim_manual_review_records",
    "selected_work_item = manual_trace_review_follow_up_trace",
    "selected_work_item_status = manual_trace_review_follow_up_trace_completed",
    "reviewed_manual_trace_review_follow_up_trace_candidate_id = manual_trace_review_follow_up_trace_candidate_v06273",
    "reviewed_manual_trace_review_follow_up_trace_candidate_status = accepted_for_future_manual_trace_review_follow_up_trace",
    "reviewed_narrower_manual_trace_review_id = narrower_manual_trace_review_v06270",
    "manual_trace_review_follow_up_trace_candidate_accepted = true",
    "future_manual_trace_review_follow_up_trace_accepted = true",
    "future_follow_up_trace_candidate_lanes_accepted = true",
    "future_follow_up_trace_candidate_questions_accepted = true",
    "future_follow_up_trace_candidate_record_schema_accepted = true",
    "manual_trace_review_records_accepted = true",
    "manual_trace_review_results_accepted = true",
    "manual_trace_review_dispositions_accepted = true",
    "manual_trace_review_gap_triage_accepted = true",
    "manual_trace_review_follow_up_trace_candidates_accepted = true",
    "follow_up_trace_candidate_lanes_used = true",
    "follow_up_trace_candidate_questions_used = true",
    "follow_up_trace_candidate_scope_used = true",
    "follow_up_trace_candidate_record_schema_used = true",
    "follow_up_trace_records_created = true",
    "manual_trace_review_follow_up_trace_records_created = true",
    "manual_trace_review_follow_up_trace_results_created = true",
    "manual_trace_review_follow_up_trace_dispositions_created = true",
    "manual_trace_review_follow_up_trace_gap_triage_created = true",
    "manual_trace_review_follow_up_trace_review_inputs_recorded = true",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_follow_up_trace_report_findings_created = false",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
    "manual_trace_review_report_scope_candidates_created = false",
    "manual_trace_review_defect_planning_candidates_created = false",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_candidate_created = false",
    "gateway_path_integration_verification_report_created = false",
    "recommended_next_work_item = manual_trace_review_follow_up_trace_review_and_decision",
    "manual_trace_review_follow_up_trace_review_and_decision_recommended = true",
    "code_inspection_report_candidate_recommended = false",
    "accepted_defect_candidate_planning_recommended = false",
    "gateway_path_integration_verification_report_recommended = false",
    "implementation_change_required_count = 0",
    "manual_trace_review_records_accepted_as_implementation_change = false",
    "manual_trace_review_results_accepted_as_report_findings = false",
    "manual_trace_review_dispositions_accepted_as_defects = false",
    "follow_up_trace_records_accepted_as_defects = false",
    "follow_up_trace_results_accepted_as_report_findings = false",
    "follow_up_trace_dispositions_accepted_as_implementation_change = false",
    "follow_up_trace_dispositions_accepted_as_integration_proof = false",
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
    "manual_trace_review_follow_up_trace_v06276",
    "manual_trace_review_follow_up_trace_candidate",
    "manual_trace_review_follow_up_trace_candidate_v06273",
    "manual_trace_review_follow_up_trace_records",
    "manual_trace_review_follow_up_trace_results",
    "manual_trace_review_follow_up_trace_dispositions",
    "manual_trace_review_follow_up_trace_gap_triage",
    "manual_trace_review_follow_up_trace_conclusions",
    "manual_trace_review_follow_up_trace_review_and_decision",
    "follow_up_trace_records_created",
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
    "lane_06_claim_boundary_review",
    "verification_required statuses",
    "manual_review_requires_follow_up",
    "manual_review_candidate_for_follow_up_trace",
    "manual_review_verification_required",
    "manual_review_gap_triage_only",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "Manual trace review records are not accepted defects.",
    "Manual trace review results are not report findings.",
    "Manual trace review dispositions are not implementation changes.",
    "Follow-up trace records are not accepted defects.",
    "Follow-up trace results are not report findings.",
    "Follow-up trace dispositions are not implementation changes.",
    "Manual trace review follow-up trace is not gateway execution path modification.",
    "No private generated outputs are moved public in v0.6.276.",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.276 Manual Trace Review Follow-Up Trace",
    "Previous checkpoint: v0.6.275 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `manual_trace_review_follow_up_trace`",
    "Trace result: manual trace review follow-up trace performed with non-claim records",
    "Application status: follow-up trace records only; no conclusions, defects, report, or gateway behavior changed",
    "manual_trace_review_follow_up_trace_records != accepted_defect_records",
    "manual_trace_review_follow_up_trace_results != report_findings",
    "manual_trace_review_follow_up_trace_dispositions != implementation_changes",
    "manual_trace_review_follow_up_trace_gap_triage != accepted_defect_records",
    "manual_trace_review_follow_up_trace_conclusions_created = false",
    "manual_trace_review_conclusions_created = false",
    "follow-up trace records support reviewer navigation",
    "follow-up trace results support later review-and-decision",
    "follow-up trace dispositions support non-claim triage",
    "follow-up trace gap triage supports prioritization",
    "follow-up trace does not establish accepted defects",
    "follow-up trace does not establish report findings",
    "follow-up trace does not establish gateway integration proof",
    "follow-up trace does not establish missing integration proof",
    "follow-up trace does not require implementation changes",
    "recommended_next_work_item = manual_trace_review_follow_up_trace_review_and_decision",
    "follow-up trace records are not accepted defects",
    "follow-up trace results are not report findings",
    "follow-up trace dispositions are not implementation changes",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06276_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)


def test_v06276_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0351",
            "Status: accepted",
            "Perform the manual trace review follow-up trace",
            "manual_trace_review_follow_up_trace_performed = true",
            "manual_trace_review_follow_up_trace_records_created = true",
            "manual_trace_review_follow_up_trace_results_created = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "Follow-up trace records are not accepted defects.",
            "Follow-up trace results are not report findings.",
            "Follow-up trace dispositions are not implementation changes.",
            "No private generated outputs are moved public in v0.6.276.",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06276_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0351 - Add v0.6.276 Manual Trace Review Follow-Up Trace",
            "Status: completed by v0.6.276",
            "manual_trace_review_follow_up_trace_performed = true",
            "manual_trace_review_follow_up_trace_completed = true",
            "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
            "manual_trace_review_follow_up_trace_records_created = true",
            "manual_trace_review_follow_up_trace_results_created = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "implementation_change_required_count = 0",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
        ],
    )


def test_v06276_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.276 Manual Trace Review Follow-Up Trace",
            "manual_trace_review_follow_up_trace_performed = true",
            "manual_trace_review_follow_up_trace_completed = true",
            "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
            "manual_trace_review_follow_up_trace_records_created = true",
            "manual_trace_review_follow_up_trace_results_created = true",
            "manual_trace_review_follow_up_trace_dispositions_created = true",
            "manual_trace_review_follow_up_trace_gap_triage_created = true",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "manual_trace_review_conclusions_created = false",
            "manual_trace_review_report_findings_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
            "Follow-up trace records are not accepted defects.",
            "Follow-up trace results are not report findings.",
            "Follow-up trace dispositions are not implementation changes.",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.276 - Manual Trace Review Follow-Up Trace",
            "Performed the first bounded Manual Trace Review Follow-Up Trace.",
            "manual_trace_review_follow_up_trace_performed = true",
            "manual_trace_review_follow_up_trace_completed = true",
            "manual_trace_review_follow_up_trace_id = manual_trace_review_follow_up_trace_v06276",
            "follow-up trace records",
            "manual_trace_review_follow_up_trace_conclusions_created = false",
            "manual_trace_review_conclusions_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
            "follow-up trace records are not accepted defects",
            "follow-up trace results are not report findings",
            "follow-up trace dispositions are not implementation changes",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.276",
            "v0.6.277 Manual Trace Review Follow-Up Trace Review and Decision",
            "no follow-up trace conclusions",
            "no manual trace review conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06276_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06276_manual_trace_review_follow_up_trace.py"])


def main() -> None:
    test_v06276_doc_tokens()
    test_v06276_adr_tokens()
    test_v06276_issue_tokens()
    test_v06276_index_tokens()
    test_v06276_registered_in_run_all()
    print("v0.6.276 manual trace review follow-up trace checks passed")


if __name__ == "__main__":
    main()
