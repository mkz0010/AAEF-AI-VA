from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/332-v06257-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0332-add-v06257-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0332-add-v06257-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = symbol_level_tracing_planning",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_keyword_level_findings_require_symbol_level_tracing_plan_before_report_or_implementation",
    "symbol_level_tracing_planning_selected = true",
    "symbol_level_tracing_planning_candidate_created = false",
    "symbol_level_tracing_selected = false",
    "symbol_level_tracing_performed = false",
    "symbol_level_tracing_completed = false",
    "symbol_level_tracing_results_created = false",
    "accepted_defect_records_created = false",
    "narrower_finding_disposition_matrix_selected = false",
    "narrower_finding_disposition_matrix_created = false",
    "code_inspection_report_candidate_selected = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_selected = false",
    "gateway_path_integration_verification_report_created = false",
    "gateway_behavior_implementation_change_selected = false",
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
    "symbol_level_tracing_planning",
    "narrower_finding_disposition_matrix",
    "code_inspection_report_candidate",
    "gateway_path_integration_verification_report",
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
    "source_file_exists_status",
    "source_symbol_exists_status",
    "gateway_entrypoint_symbol",
    "request_load_symbol",
    "decision_load_symbol",
    "pre_dispatch_check_symbol",
    "helper_invocation_symbol",
    "adapter_dispatch_symbol",
    "result_generation_symbol",
    "evidence_generation_symbol",
    "gateway_path_invocation_status",
    "pre_dispatch_enforcement_status",
    "evidence_result_status",
    "gap_status",
    "recommended_next_action",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
    "Selection result: `symbol_level_tracing_planning`",
    "Application status: selection only; no symbol-level tracing performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.257.",
    "keyword_level_indicator != symbol_level_proof",
    "source_file_exists_status != source_symbol_exists_status",
    "gap_candidate != accepted_defect",
    "helper_exists != helper_enforced_before_dispatch",
    "helper_tested != helper_invoked_by_gateway_path",
    "symbol-level tracing planning is not symbol-level tracing",
    "symbol-level tracing planning is not gateway execution path modification",
    "symbol-level tracing planning is not proof that all helpers are integrated",
    "keyword-level indicators are not symbol-level proof",
    "gap candidates are not accepted defects",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.258 Symbol-Level Tracing Planning Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06257_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06257_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0332",
            "Status: accepted",
            "Select the following next work item",
            "symbol_level_tracing_planning",
            "This is a selection-only checkpoint.",
            "Symbol-level tracing planning is not symbol-level tracing.",
            "Keyword-level indicators are not symbol-level proof.",
            "Gap candidates are not accepted defects.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.257.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06257_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0332 - Add v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.257",
            "selected_work_item = symbol_level_tracing_planning",
            "symbol_level_tracing_planning_selected = true",
            "symbol_level_tracing_completed = false",
            "symbol_level_tracing_results_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.258 Symbol-Level Tracing Planning Candidate",
        ],
    )


def test_v06257_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
            "symbol_level_tracing_planning",
            "This is selection only.",
            "does not perform symbol-level tracing",
            "create symbol-level tracing results",
            "create accepted defect records",
            "create a code-inspection report",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Keyword-level indicators are not symbol-level proof.",
            "Gap candidates are not accepted defects.",
            "No private generated outputs are moved public in v0.6.257.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.257 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `symbol_level_tracing_planning` as the next work item",
            "next_work_selection_completed = true",
            "symbol_level_tracing_planning_selected = true",
            "symbol_level_tracing_completed = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.257",
            "v0.6.258 Symbol-Level Tracing Planning Candidate",
            "no symbol-level tracing plan artifact",
            "no symbol-level tracing results",
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


def test_v06257_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06257_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06257_doc_tokens()
    test_v06257_adr_tokens()
    test_v06257_issue_tokens()
    test_v06257_index_tokens()
    test_v06257_registered_in_run_all()
    print("v0.6.257 next work selection checks passed")


if __name__ == "__main__":
    main()
