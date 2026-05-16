from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/344-v06269-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0344-add-v06269-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0344-add-v06269-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = narrower_manual_trace_review",
    "selected_work_item_status = selected_for_next_manual_trace_review_checkpoint",
    "selected_work_item_reason = accepted_narrower_manual_trace_review_candidate_requires_manual_review_before_report_defect_or_implementation",
    "narrower_manual_trace_review_selected = true",
    "narrower_manual_trace_review_candidate_accepted = true",
    "future_narrower_manual_trace_review_accepted = true",
    "narrower_manual_trace_review_performed = false",
    "narrower_manual_trace_review_completed = false",
    "narrower_manual_trace_review_records_created = false",
    "manual_trace_review_records_created = false",
    "manual_trace_review_results_created = false",
    "manual_trace_review_conclusions_created = false",
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
    "source_file_observation_records_accepted = true",
    "source_symbol_observation_records_accepted = true",
    "call_path_status_records_accepted = true",
    "symbol_trace_records_accepted = true",
    "trace_record_schema_accepted = true",
    "trace_status_vocabulary_accepted = true",
    "gap_records_accepted_for_triage = true",
    "recommended_next_action_records_accepted_for_planning = true",
    "manual_trace_review_scope_accepted = true",
    "manual_trace_review_gap_triage_accepted_for_triage = true",
    "observed_symbol_records_accepted_as_integration_proof = false",
    "observed_call_path_records_accepted_as_integration_proof = false",
    "manual_trace_review_questions_accepted_as_conclusions = false",
    "manual_trace_review_scope_accepted_as_defect_scope = false",
    "gap_records_accepted_as_defects = false",
    "verification_required_accepted_as_integration_proof = false",
    "candidate_findings_accepted_as_defects = false",
    "candidate_findings_accepted_as_integration_proof = false",
    "candidate_findings_accepted_as_missing_integration_proof = false",
    "candidate_findings_accepted_for_implementation_change = false",
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

REQUIRED_SCOPE_TOKENS = [
    "source_file_observation_records",
    "source_symbol_observation_records",
    "call_path_status_records",
    "symbol_trace_records",
    "trace_record_schema",
    "trace_status_vocabulary",
    "pass_level_counts",
    "gap_records",
    "recommended_next_action_records",
    "verification_required statuses",
    "lane_01_pre_dispatch_enforcement_review",
    "lane_02_fail_closed_review",
    "lane_03_adapter_boundary_review",
    "lane_04_result_status_review",
    "lane_05_evidence_linkage_review",
    "lane_06_claim_boundary_review",
    "manual_trace_review_id",
    "reviewed_read_only_symbol_level_tracing_pass_id",
    "reviewed_symbol_trace_id",
    "manual_trace_review_lane_id",
    "manual_trace_review_question",
    "manual_trace_review_disposition",
    "manual_trace_review_rationale",
    "manual_trace_review_gap_triage",
    "implementation_change_required",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
    "Selection result: `narrower_manual_trace_review`",
    "Application status: selection only; no manual trace review performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.269.",
    "narrower_manual_trace_review_selected != narrower_manual_trace_review_performed",
    "narrower_manual_trace_review_selection != manual_trace_review_records",
    "narrower_manual_trace_review_selection != accepted_defect_records",
    "narrower_manual_trace_review_selection != code_inspection_report",
    "narrower_manual_trace_review_selection != gateway_path_integration_verification_report",
    "manual_trace_review_questions != manual_trace_review_conclusions",
    "manual_trace_review_scope != accepted_defect_scope",
    "gap_records != accepted_defects",
    "verification_required != integration_proof",
    "narrower manual trace review selection is not manual trace review execution",
    "narrower manual trace review selection is not gateway execution path modification",
    "narrower manual trace review selection is not proof that all helpers are integrated",
    "manual review questions are not manual review conclusions",
    "manual review scope is not accepted defect scope",
    "gap records are not accepted defects",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "manual_trace_review_scope",
    "manual_trace_review_gap_triage",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
    "v0.6.270 Narrower Manual Trace Review",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06269_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06269_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0344",
            "Status: accepted",
            "Select the following next work item",
            "narrower_manual_trace_review",
            "This is a selection-only checkpoint.",
            "Narrower manual trace review selection is not manual trace review execution.",
            "Manual review questions are not manual review conclusions.",
            "Gap records are not accepted defects.",
            "No private generated outputs are moved public in v0.6.269.",
            "manual_trace_review_scope",
            "manual_trace_review_gap_triage",
            "readme_front_page_rewritten = false",
            "repository_metadata_changed = false",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06269_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0344 - Add v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.269",
            "selected_work_item = narrower_manual_trace_review",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "manual_trace_review_results_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.270 Narrower Manual Trace Review",
        ],
    )


def test_v06269_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
            "selected_work_item = narrower_manual_trace_review",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "manual_trace_review_results_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
            "This is selection only.",
            "does not perform manual trace review",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Manual review questions are not manual review conclusions.",
            "Gap records are not accepted defects.",
            "No private generated outputs are moved public in v0.6.269.",
            "manual_trace_review_scope",
            "manual_trace_review_gap_triage",
            "readme_front_page_rewritten = false",
            "repository_metadata_changed = false",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.269 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `narrower_manual_trace_review` as the next work item",
            "next_work_selection_completed = true",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report",
            "manual_trace_review_scope",
            "manual_trace_review_gap_triage",
            "readme_front_page_rewritten = false",
            "repository_metadata_changed = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.269",
            "v0.6.270 Narrower Manual Trace Review",
            "no narrower manual trace review records",
            "no manual trace review results",
            "no manual trace review conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06269_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06269_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06269_doc_tokens()
    test_v06269_adr_tokens()
    test_v06269_issue_tokens()
    test_v06269_index_tokens()
    test_v06269_registered_in_run_all()
    print("v0.6.269 next work selection checks passed")


if __name__ == "__main__":
    main()
