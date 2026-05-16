from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/338-v06263-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0338-add-v06263-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0338-add-v06263-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = read_only_symbol_level_tracing_pass",
    "selected_work_item_status = selected_for_next_read_only_pass_checkpoint",
    "selected_work_item_reason = accepted_read_only_symbol_level_tracing_pass_candidate_requires_read_only_pass_before_report_or_implementation",
    "read_only_symbol_level_tracing_pass_selected = true",
    "read_only_symbol_level_tracing_pass_candidate_accepted = true",
    "read_only_symbol_level_tracing_pass_performed = false",
    "read_only_symbol_level_tracing_pass_completed = false",
    "read_only_symbol_level_tracing_results_created = false",
    "symbol_level_tracing_selected = true",
    "symbol_level_tracing_performed = false",
    "symbol_level_tracing_completed = false",
    "symbol_level_tracing_results_created = false",
    "observed_symbol_records_created = false",
    "observed_call_path_records_created = false",
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

REQUIRED_COMPONENT_TOKENS = [
    "read_only_symbol_level_tracing_pass",
    "symbol_trace_inventory",
    "trace_stage_matrix",
    "source_file_candidate_list",
    "source_symbol_candidate_list",
    "call_path_trace_candidate_list",
    "trace_record_schema",
    "trace_status_vocabulary",
    "trace_pass_output_fields",
    "trace_candidate_procedure",
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
    "verified_repository_revision",
    "symbol_trace_records",
    "source_file_observed_status",
    "source_symbol_observed_status",
    "call_path_observed_status",
    "pre_dispatch_enforcement_status",
    "evidence_generation_status",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.262 Read-Only Symbol-Level Tracing Pass Candidate Review and Decision",
    "Selection result: `read_only_symbol_level_tracing_pass`",
    "Application status: selection only; no symbol-level tracing performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.263.",
    "read_only_symbol_level_tracing_pass_selected != read_only_symbol_level_tracing_pass_performed",
    "read_only_symbol_level_tracing_pass_selection != symbol_level_tracing_results",
    "accepted pass candidate != observed symbol records",
    "accepted pass candidate != observed call-path records",
    "gap candidates != accepted defects",
    "read-only symbol-level tracing pass selection is not symbol-level tracing execution",
    "selected read-only symbol-level tracing pass is not gateway execution path modification",
    "selected read-only symbol-level tracing pass is not proof that all helpers are integrated",
    "accepted source symbol candidates are not observed symbols",
    "accepted call path candidates are not observed call paths",
    "accepted pre-dispatch enforcement candidates are not observed enforcement",
    "accepted evidence generation candidates are not observed evidence generation",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.264 Read-Only Symbol-Level Tracing Pass",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06263_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06263_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0338",
            "Status: accepted",
            "Select the following next work item",
            "read_only_symbol_level_tracing_pass",
            "This is a selection-only checkpoint.",
            "Read-only symbol-level tracing pass selection is not symbol-level tracing execution.",
            "Accepted source symbol candidates are not observed symbols.",
            "Accepted call path candidates are not observed call paths.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.263.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06263_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0338 - Add v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.263",
            "selected_work_item = read_only_symbol_level_tracing_pass",
            "read_only_symbol_level_tracing_pass_selected = true",
            "read_only_symbol_level_tracing_pass_performed = false",
            "read_only_symbol_level_tracing_results_created = false",
            "observed_symbol_records_created = false",
            "observed_call_path_records_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.264 Read-Only Symbol-Level Tracing Pass",
        ],
    )


def test_v06263_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
            "read_only_symbol_level_tracing_pass",
            "This is selection only.",
            "does not perform symbol-level tracing",
            "create symbol-level tracing results",
            "create observed symbol records",
            "create observed call-path records",
            "create accepted defect records",
            "create a code-inspection report",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Accepted source symbol candidates are not observed symbols.",
            "Accepted call path candidates are not observed call paths.",
            "No private generated outputs are moved public in v0.6.263.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.263 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `read_only_symbol_level_tracing_pass` as the next work item",
            "next_work_selection_completed = true",
            "read_only_symbol_level_tracing_pass_selected = true",
            "read_only_symbol_level_tracing_pass_performed = false",
            "read_only_symbol_level_tracing_results_created = false",
            "observed symbol record",
            "observed call-path record",
            "accepted source symbol candidates are not observed symbols",
            "accepted call path candidates are not observed call paths",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.263",
            "v0.6.264 Read-Only Symbol-Level Tracing Pass",
            "no read-only symbol-level tracing results",
            "no symbol-level tracing results",
            "no observed symbol records",
            "no observed call-path records",
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


def test_v06263_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06263_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06263_doc_tokens()
    test_v06263_adr_tokens()
    test_v06263_issue_tokens()
    test_v06263_index_tokens()
    test_v06263_registered_in_run_all()
    print("v0.6.263 next work selection checks passed")


if __name__ == "__main__":
    main()
