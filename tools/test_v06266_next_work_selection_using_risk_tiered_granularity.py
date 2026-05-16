from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/341-v06266-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0341-add-v06266-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0341-add-v06266-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = narrower_manual_trace_review",
    "selected_work_item_status = selected_for_next_manual_trace_review_checkpoint",
    "selected_work_item_reason = read_only_static_inspection_records_require_manual_trace_review_before_report_or_implementation",
    "narrower_manual_trace_review_selected = true",
    "narrower_manual_trace_review_performed = false",
    "narrower_manual_trace_review_completed = false",
    "narrower_manual_trace_review_records_created = false",
    "read_only_symbol_level_tracing_pass_review_completed = true",
    "read_only_symbol_level_tracing_pass_accepted = true",
    "read_only_symbol_level_tracing_results_created = true",
    "symbol_level_tracing_results_created = true",
    "source_file_observation_records_accepted = true",
    "source_symbol_observation_records_accepted = true",
    "call_path_status_records_accepted = true",
    "symbol_trace_records_accepted = true",
    "trace_record_schema_accepted = true",
    "trace_status_vocabulary_accepted = true",
    "gap_records_accepted_for_triage = true",
    "recommended_next_action_records_accepted_for_planning = true",
    "recommended_next_work_item = narrower_manual_trace_review",
    "code_inspection_report_candidate_selected = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "accepted_defect_candidate_planning_selected = false",
    "accepted_defect_candidate_planning_created = false",
    "accepted_defect_records_created = false",
    "accepted_defect_records_accepted = false",
    "gateway_path_integration_verification_report_selected = false",
    "gateway_path_integration_verification_report_created = false",
    "gateway_behavior_implementation_change_selected = false",
    "observed_symbol_records_accepted_as_integration_proof = false",
    "observed_call_path_records_accepted_as_integration_proof = false",
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

REQUIRED_COMPONENT_TOKENS = [
    "source_file_observation_records",
    "source_symbol_observation_records",
    "call_path_status_records",
    "symbol_trace_records",
    "trace_record_schema",
    "trace_status_vocabulary",
    "gap_records",
    "recommended_next_action_records",
    "verification_required statuses",
    "manual_trace_review_scope",
    "manual_trace_review_questions",
    "manual_trace_review_disposition",
    "manual_trace_review_gap_triage",
    "implementation_change_required",
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
    "narrower_manual_trace_review",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.266 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.265 Read-Only Symbol-Level Tracing Pass Review and Decision",
    "Selection result: `narrower_manual_trace_review`",
    "Application status: selection only; no manual trace review performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.266.",
    "narrower_manual_trace_review_selected != narrower_manual_trace_review_performed",
    "narrower_manual_trace_review_selection != accepted_defect_records",
    "narrower_manual_trace_review_selection != code_inspection_report",
    "narrower_manual_trace_review_selection != gateway_path_integration_verification_report",
    "read_only_static_inspection_records != gateway_execution_path_modification",
    "observed_source_symbols != pre_dispatch_enforcement_proof",
    "observed_call_path_status_records != full_gateway_integration_proof",
    "gap_records != accepted_defects",
    "verification_required != integration_proof",
    "narrower manual trace review selection is not manual trace review execution",
    "narrower manual trace review selection is not gateway execution path modification",
    "narrower manual trace review selection is not proof that all helpers are integrated",
    "observed source symbols are not proof of pre-dispatch enforcement",
    "observed call-path status records are not full gateway integration proof",
    "call-path not observed is not proof of missing integration",
    "verification_required is not integration proof",
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
    "v0.6.267 Narrower Manual Trace Review Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06266_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06266_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0341",
            "Status: accepted",
            "Select the following next work item",
            "narrower_manual_trace_review",
            "This is a selection-only checkpoint.",
            "Narrower manual trace review selection is not manual trace review execution.",
            "Observed source symbols are not proof of pre-dispatch enforcement.",
            "Observed call-path status records are not full gateway integration proof.",
            "No private generated outputs are moved public in v0.6.266.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06266_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0341 - Add v0.6.266 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.266",
            "selected_work_item = narrower_manual_trace_review",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "recommended_next_work_item = narrower_manual_trace_review",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.267 Narrower Manual Trace Review Candidate",
        ],
    )


def test_v06266_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.266 Next Work Selection Using Risk-Tiered Granularity",
            "narrower_manual_trace_review",
            "next_work_selection_completed = true",
            "selected_work_item = narrower_manual_trace_review",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "recommended_next_work_item = narrower_manual_trace_review",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
            "This is selection only.",
            "does not perform manual trace review",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Observed source symbols are not proof of pre-dispatch enforcement.",
            "Observed call-path status records are not full gateway integration proof.",
            "No private generated outputs are moved public in v0.6.266.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.266 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `narrower_manual_trace_review` as the next work item",
            "next_work_selection_completed = true",
            "narrower_manual_trace_review_selected = true",
            "narrower_manual_trace_review_performed = false",
            "narrower_manual_trace_review_records_created = false",
            "recommended_next_work_item = narrower_manual_trace_review",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.266",
            "v0.6.267 Narrower Manual Trace Review Candidate",
            "no narrower manual trace review records",
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


def test_v06266_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06266_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06266_doc_tokens()
    test_v06266_adr_tokens()
    test_v06266_issue_tokens()
    test_v06266_index_tokens()
    test_v06266_registered_in_run_all()
    print("v0.6.266 next work selection checks passed")


if __name__ == "__main__":
    main()
