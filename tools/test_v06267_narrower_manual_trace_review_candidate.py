from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/342-v06267-narrower-manual-trace-review-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0342-add-v06267-narrower-manual-trace-review-candidate.md"
ISSUE = ROOT / "planning/issues/0342-add-v06267-narrower-manual-trace-review-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "narrower_manual_trace_review_candidate_created = true",
    "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
    "narrower_manual_trace_review_candidate_status = candidate_not_applied",
    "narrower_manual_trace_review_candidate_scope = documentation_only_manual_review_candidate_for_static_symbol_trace_records",
    "selected_work_item = narrower_manual_trace_review",
    "selected_work_item_status = narrower_manual_trace_review_candidate_created",
    "manual_trace_review_lanes_defined = true",
    "manual_trace_review_input_records_defined = true",
    "manual_trace_review_questions_defined = true",
    "manual_trace_review_disposition_vocabulary_defined = true",
    "manual_trace_review_record_schema_defined = true",
    "manual_trace_review_output_fields_defined = true",
    "manual_trace_review_candidate_procedure_defined = true",
    "manual_trace_review_non_claim_boundaries_defined = true",
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
    "manual_trace_review_scope",
    "manual_trace_review_questions",
    "manual_trace_review_disposition",
    "manual_trace_review_gap_triage",
    "implementation_change_required",
    "manual_trace_review_id",
    "reviewed_read_only_symbol_level_tracing_pass_id",
    "reviewed_symbol_trace_id",
    "manual_trace_review_lane_id",
    "manual_trace_review_rationale",
]

REQUIRED_SCOPE_TOKENS = [
    "authorization_expiry_current_time",
    "request_decision_constraint_diff_enforcement",
    "external_discovery_fail_closed_behavior",
    "scope_registry_runtime_target_validity",
    "mock_dry_run_completed_status_terminology",
    "credential_ref_resolution_boundary",
    "human_approval_gate_boundary",
    "execution_status_separation",
    "tool_gateway_dispatch_boundary",
    "adapter_execution_boundary",
    "unsupported_decision_fail_closed",
    "incomplete_binding_fail_closed",
    "scope_or_target_mismatch_fail_closed",
    "evidence_event_for_dispatch_or_non_dispatch",
    "stage_01_gateway_entrypoint",
    "stage_02_request_load",
    "stage_03_decision_load",
    "stage_04_binding",
    "stage_05_pre_dispatch_checks",
    "stage_06_helper_invocation",
    "stage_07_fail_closed",
    "stage_08_adapter_boundary",
    "stage_09_result_generation",
    "stage_10_evidence_generation",
    "gateway_entrypoint_symbol",
    "request_load_symbol",
    "decision_load_symbol",
    "request_decision_binding_symbol",
    "pre_dispatch_check_symbol",
    "helper_invocation_symbol",
    "fail_closed_symbol",
    "adapter_dispatch_symbol",
    "result_generation_symbol",
    "evidence_generation_symbol",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.267 Narrower Manual Trace Review Candidate",
    "Previous checkpoint: v0.6.266 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `narrower_manual_trace_review`",
    "Candidate result: narrower manual trace review candidate created",
    "Application status: candidate only; no manual trace review performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.267.",
    "Which v0.6.264 static symbol trace records should be manually reviewed first",
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
    "narrower manual trace review candidate is not manual trace review execution",
    "narrower manual trace review candidate is not gateway execution path modification",
    "narrower manual trace review candidate is not proof that all helpers are integrated",
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
    "v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06267_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06267_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0342",
            "Status: proposed candidate",
            "Create a Narrower Manual Trace Review Candidate.",
            "manual_trace_review_lanes_defined = true",
            "manual_trace_review_questions_defined = true",
            "manual_trace_review_record_schema_defined = true",
            "Narrower manual trace review candidate is not manual trace review execution.",
            "Manual review questions are not manual review conclusions.",
            "Gap records are not accepted defects.",
            "No private generated outputs are moved public in v0.6.267.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06267_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0342 - Add v0.6.267 Narrower Manual Trace Review Candidate",
            "Status: completed by v0.6.267",
            "narrower_manual_trace_review",
            "narrower_manual_trace_review_candidate_created = true",
            "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
            "manual_trace_review_lanes_defined = true",
            "manual_trace_review_disposition_vocabulary_defined = true",
            "narrower_manual_trace_review_performed = false",
            "manual_trace_review_results_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
        ],
    )


def test_v06267_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.267 Narrower Manual Trace Review Candidate",
            "narrower_manual_trace_review_candidate_created = true",
            "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
            "narrower_manual_trace_review_candidate_status = candidate_not_applied",
            "manual_trace_review_lanes_defined = true",
            "manual_trace_review_questions_defined = true",
            "manual_trace_review_disposition_vocabulary_defined = true",
            "manual_trace_review_record_schema_defined = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
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
            "No private generated outputs are moved public in v0.6.267.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.267 - Narrower Manual Trace Review Candidate",
            "Created a documentation-only Narrower Manual Trace Review Candidate.",
            "narrower_manual_trace_review_candidate_created = true",
            "narrower_manual_trace_review_candidate_id = narrower_manual_trace_review_candidate_v06267",
            "narrower_manual_trace_review_candidate_status = candidate_not_applied",
            "manual trace review lanes",
            "manual review questions are not manual review conclusions",
            "gap records are not accepted defects",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.267",
            "v0.6.268 Narrower Manual Trace Review Candidate Review and Decision",
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


def test_v06267_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06267_narrower_manual_trace_review_candidate.py"])


def main() -> None:
    test_v06267_doc_tokens()
    test_v06267_adr_tokens()
    test_v06267_issue_tokens()
    test_v06267_index_tokens()
    test_v06267_registered_in_run_all()
    print("v0.6.267 narrower manual trace review candidate checks passed")


if __name__ == "__main__":
    main()
