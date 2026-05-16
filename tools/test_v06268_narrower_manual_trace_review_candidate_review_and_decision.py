from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/343-v06268-narrower-manual-trace-review-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0343-add-v06268-narrower-manual-trace-review-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0343-add-v06268-narrower-manual-trace-review-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "narrower_manual_trace_review_candidate_review_completed = true",
    "narrower_manual_trace_review_candidate_accepted = true",
    "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
    "narrower_manual_trace_review_candidate_review_result = accepted_for_future_narrower_manual_trace_review",
    "narrower_manual_trace_review_candidate_status = accepted_for_future_narrower_manual_trace_review",
    "narrower_manual_trace_review_candidate_applied = false",
    "future_narrower_manual_trace_review_accepted = true",
    "future_manual_trace_review_lanes_accepted = true",
    "future_manual_trace_review_input_records_accepted = true",
    "future_manual_trace_review_questions_accepted = true",
    "future_manual_trace_review_disposition_vocabulary_accepted = true",
    "future_manual_trace_review_record_schema_accepted = true",
    "future_manual_trace_review_output_fields_accepted = true",
    "future_manual_trace_review_candidate_procedure_accepted = true",
    "future_manual_trace_review_non_claim_boundaries_accepted = true",
    "manual_trace_review_scope_accepted = true",
    "manual_trace_review_gap_triage_accepted_for_triage = true",
    "narrower_manual_trace_review_selected = false",
    "narrower_manual_trace_review_performed = false",
    "narrower_manual_trace_review_completed = false",
    "narrower_manual_trace_review_records_created = false",
    "manual_trace_review_records_created = false",
    "manual_trace_review_results_created = false",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_candidate_created = false",
    "gateway_path_integration_verification_report_created = false",
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

REQUIRED_COMPONENT_TOKENS = [
    "manual_trace_review_lanes",
    "manual_trace_review_input_records",
    "manual_trace_review_questions",
    "manual_trace_review_disposition_vocabulary",
    "manual_trace_review_record_schema",
    "manual_trace_review_output_fields",
    "manual_trace_review_candidate_procedure",
    "manual_trace_review_non_claim_boundaries",
    "manual_trace_review_scope",
    "manual_trace_review_gap_triage",
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
    "manual_trace_review_rationale",
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
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
    "Previous checkpoint: v0.6.267 Narrower Manual Trace Review Candidate",
    "Reviewed candidate: `narrower_manual_trace_review_candidate_v06267`",
    "Decision result: accepted for future narrower manual trace review",
    "Application status: review only; no manual trace review performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.268.",
    "narrower_manual_trace_review_candidate != narrower_manual_trace_review_performed",
    "narrower_manual_trace_review_candidate != manual_trace_review_records",
    "manual_review_question != manual_review_conclusion",
    "manual_review_scope != accepted_defect_scope",
    "manual_review_gap_triage != accepted_defect_records",
    "manual_review_candidate != code_inspection_report",
    "manual_review_candidate != gateway_path_integration_verification_report",
    "manual_trace_question_01",
    "manual_trace_question_10",
    "manual_review_not_performed",
    "manual_review_candidate_for_follow_up_trace",
    "manual_trace_review_status_default = manual_review_not_performed",
    "narrower manual trace review candidate acceptance is not manual trace review execution",
    "narrower manual trace review candidate acceptance is not gateway execution path modification",
    "narrower manual trace review candidate acceptance is not proof that all helpers are integrated",
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
    "v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06268_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06268_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0343",
            "Status: accepted",
            "Accept the v0.6.267 Narrower Manual Trace Review Candidate",
            "future_narrower_manual_trace_review_accepted = true",
            "future_manual_trace_review_record_schema_accepted = true",
            "Narrower manual trace review candidate acceptance is not manual trace review execution.",
            "Manual review questions are not manual review conclusions.",
            "Gap records are not accepted defects.",
            "No private generated outputs are moved public in v0.6.268.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06268_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0343 - Add v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
            "Status: completed by v0.6.268",
            "narrower_manual_trace_review_candidate_review_completed = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "narrower_manual_trace_review_candidate_review_result = accepted_for_future_narrower_manual_trace_review",
            "future_narrower_manual_trace_review_accepted = true",
            "future_manual_trace_review_record_schema_accepted = true",
            "manual_trace_review_records_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06268_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
            "narrower_manual_trace_review_candidate_review_completed = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
            "future_narrower_manual_trace_review_accepted = true",
            "future_manual_trace_review_lanes_accepted = true",
            "future_manual_trace_review_questions_accepted = true",
            "future_manual_trace_review_record_schema_accepted = true",
            "narrower_manual_trace_review_performed = false",
            "manual_trace_review_records_created = false",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
            "does not perform manual trace review",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Manual review questions are not manual review conclusions.",
            "Gap records are not accepted defects.",
            "No private generated outputs are moved public in v0.6.268.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.268 - Narrower Manual Trace Review Candidate Review and Decision",
            "Accepted the v0.6.267 documentation-only Narrower Manual Trace Review Candidate",
            "narrower_manual_trace_review_candidate_review_completed = true",
            "narrower_manual_trace_review_candidate_accepted = true",
            "future_narrower_manual_trace_review_accepted = true",
            "manual review questions are not manual review conclusions",
            "gap records are not accepted defects",
            "manual_trace_review_scope",
            "readme_front_page_rewritten = false",
            "repository_metadata_changed = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.268",
            "v0.6.269 Next Work Selection Using Risk-Tiered Granularity",
            "future narrower manual trace review",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report candidate",
            "no narrower manual trace review records",
            "no manual trace review results",
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


def test_v06268_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06268_narrower_manual_trace_review_candidate_review_and_decision.py"])


def main() -> None:
    test_v06268_doc_tokens()
    test_v06268_adr_tokens()
    test_v06268_issue_tokens()
    test_v06268_index_tokens()
    test_v06268_registered_in_run_all()
    print("v0.6.268 narrower manual trace review candidate review and decision checks passed")


if __name__ == "__main__":
    main()
