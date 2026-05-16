from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/335-v06260-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0335-add-v06260-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0335-add-v06260-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = read_only_symbol_level_tracing_pass_candidate",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_symbol_level_tracing_plan_requires_read_only_pass_candidate_before_results_or_report",
    "read_only_symbol_level_tracing_pass_candidate_selected = true",
    "read_only_symbol_level_tracing_pass_candidate_created = false",
    "read_only_symbol_level_tracing_pass_performed = false",
    "read_only_symbol_level_tracing_results_created = false",
    "symbol_level_tracing_selected = false",
    "symbol_level_tracing_performed = false",
    "symbol_level_tracing_completed = false",
    "symbol_level_tracing_results_created = false",
    "accepted_defect_records_created = false",
    "narrower_symbol_trace_inventory_selected = false",
    "narrower_symbol_trace_inventory_created = false",
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

REQUIRED_STAGE_TOKENS = [
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
    "read_only_symbol_level_tracing_pass_candidate",
    "narrower_symbol_trace_inventory",
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
    "symbol_trace_inventory",
    "trace_stage_matrix",
    "source_file_candidate_list",
    "source_symbol_candidate_list",
    "call_path_trace_candidate_list",
    "trace_record_schema",
    "trace_status_vocabulary",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.260 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.259 Symbol-Level Tracing Planning Review and Decision",
    "Selection result: `read_only_symbol_level_tracing_pass_candidate`",
    "Application status: selection only; no symbol-level tracing performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.260.",
    "accepted tracing plan != tracing execution",
    "read_only_symbol_level_tracing_pass_candidate != symbol_level_tracing_results",
    "planned symbol candidates != observed symbols",
    "planned call paths != observed call paths",
    "gap candidates != accepted defects",
    "read-only symbol-level tracing pass candidate selection is not symbol-level tracing",
    "read-only symbol-level tracing pass candidate selection is not gateway execution path modification",
    "read-only symbol-level tracing pass candidate selection is not proof that all helpers are integrated",
    "planned symbol candidates are not observed symbols",
    "planned call paths are not observed call paths",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.261 Read-Only Symbol-Level Tracing Pass Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06260_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_STAGE_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06260_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0335",
            "Status: accepted",
            "Select the following next work item",
            "read_only_symbol_level_tracing_pass_candidate",
            "This is a selection-only checkpoint.",
            "Read-only symbol-level tracing pass candidate selection is not symbol-level tracing.",
            "Planned symbol candidates are not observed symbols.",
            "Planned call paths are not observed call paths.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.260.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06260_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0335 - Add v0.6.260 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.260",
            "selected_work_item = read_only_symbol_level_tracing_pass_candidate",
            "read_only_symbol_level_tracing_pass_candidate_selected = true",
            "read_only_symbol_level_tracing_pass_candidate_created = false",
            "read_only_symbol_level_tracing_results_created = false",
            "symbol_level_tracing_completed = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.261 Read-Only Symbol-Level Tracing Pass Candidate",
        ],
    )


def test_v06260_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.260 Next Work Selection Using Risk-Tiered Granularity",
            "read_only_symbol_level_tracing_pass_candidate",
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
            "Planned symbol candidates are not observed symbols.",
            "Planned call paths are not observed call paths.",
            "No private generated outputs are moved public in v0.6.260.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.260 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `read_only_symbol_level_tracing_pass_candidate` as the next work item",
            "next_work_selection_completed = true",
            "read_only_symbol_level_tracing_pass_candidate_selected = true",
            "symbol_level_tracing_completed = false",
            "symbol_level_tracing_results_created = false",
            "planned symbol candidates are not observed symbols",
            "planned call paths are not observed call paths",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.260",
            "v0.6.261 Read-Only Symbol-Level Tracing Pass Candidate",
            "no read-only symbol-level tracing pass candidate artifact",
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


def test_v06260_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06260_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06260_doc_tokens()
    test_v06260_adr_tokens()
    test_v06260_issue_tokens()
    test_v06260_index_tokens()
    test_v06260_registered_in_run_all()
    print("v0.6.260 next work selection checks passed")


if __name__ == "__main__":
    main()
