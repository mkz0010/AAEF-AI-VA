from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/337-v06262-read-only-symbol-level-tracing-pass-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0337-add-v06262-read-only-symbol-level-tracing-pass-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0337-add-v06262-read-only-symbol-level-tracing-pass-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "read_only_symbol_level_tracing_pass_candidate_review_completed = true",
    "read_only_symbol_level_tracing_pass_candidate_accepted = true",
    "read_only_symbol_level_tracing_pass_candidate_id = read_only_symbol_level_tracing_pass_candidate_v06261",
    "read_only_symbol_level_tracing_pass_candidate_review_result = accepted_for_future_read_only_symbol_level_tracing_pass",
    "read_only_symbol_level_tracing_pass_candidate_status = accepted_for_future_read_only_symbol_level_tracing_pass",
    "read_only_symbol_level_tracing_pass_candidate_applied = false",
    "future_read_only_symbol_level_tracing_pass_accepted = true",
    "future_symbol_trace_inventory_accepted = true",
    "future_trace_stage_matrix_accepted = true",
    "future_source_file_candidate_list_accepted = true",
    "future_source_symbol_candidate_list_accepted = true",
    "future_call_path_trace_candidate_list_accepted = true",
    "future_trace_record_schema_accepted = true",
    "future_trace_status_vocabulary_accepted = true",
    "future_trace_pass_output_fields_accepted = true",
    "future_trace_candidate_procedure_accepted = true",
    "gateway_entrypoint_symbol_dimension_accepted = true",
    "request_load_symbol_dimension_accepted = true",
    "decision_load_symbol_dimension_accepted = true",
    "request_decision_binding_symbol_dimension_accepted = true",
    "pre_dispatch_check_symbol_dimension_accepted = true",
    "helper_invocation_symbol_dimension_accepted = true",
    "fail_closed_symbol_dimension_accepted = true",
    "adapter_dispatch_symbol_dimension_accepted = true",
    "result_generation_symbol_dimension_accepted = true",
    "evidence_generation_symbol_dimension_accepted = true",
    "read_only_symbol_level_tracing_pass_selected = false",
    "read_only_symbol_level_tracing_pass_performed = false",
    "read_only_symbol_level_tracing_pass_completed = false",
    "read_only_symbol_level_tracing_results_created = false",
    "symbol_level_tracing_selected = false",
    "symbol_level_tracing_performed = false",
    "symbol_level_tracing_completed = false",
    "symbol_level_tracing_results_created = false",
    "observed_symbol_records_created = false",
    "observed_call_path_records_created = false",
    "accepted_defect_records_created = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
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
    "publication_approval = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]

REQUIRED_COMPONENT_TOKENS = [
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
    "symbol_trace_id",
    "inventory_target_id",
    "trace_stage_id",
    "source_symbol_candidate",
    "source_symbol_observed",
    "call_path_candidate",
    "call_path_observed_status",
    "pre_dispatch_enforcement_status",
    "evidence_generation_status",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.262 Read-Only Symbol-Level Tracing Pass Candidate Review and Decision",
    "Previous checkpoint: v0.6.261 Read-Only Symbol-Level Tracing Pass Candidate",
    "Reviewed candidate: `read_only_symbol_level_tracing_pass_candidate_v06261`",
    "Decision result: accepted for future read-only symbol-level tracing pass",
    "Application status: review only; no symbol-level tracing performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.262.",
    "read_only_symbol_level_tracing_pass_candidate != symbol_level_tracing_results",
    "source_symbol_candidate != source_symbol_observed",
    "call_path_candidate != call_path_observed",
    "pre_dispatch_enforcement_candidate != pre_dispatch_enforcement_observed",
    "evidence_generation_candidate != evidence_generation_observed",
    "gap_candidate != accepted_defect",
    "symbol_trace_status_default = trace_not_performed",
    "read-only symbol-level tracing pass candidate acceptance is not symbol-level tracing",
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
    "v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06262_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06262_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0337",
            "Status: accepted",
            "Accept the v0.6.261 Read-Only Symbol-Level Tracing Pass Candidate",
            "Read-only symbol-level tracing pass candidate acceptance is not symbol-level tracing.",
            "Accepted source symbol candidates are not observed symbols.",
            "Accepted call path candidates are not observed call paths.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.262.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06262_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0337 - Add v0.6.262 Read-Only Symbol-Level Tracing Pass Candidate Review and Decision",
            "Status: completed by v0.6.262",
            "read_only_symbol_level_tracing_pass_candidate_review_completed = true",
            "read_only_symbol_level_tracing_pass_candidate_accepted = true",
            "future_read_only_symbol_level_tracing_pass_accepted = true",
            "read_only_symbol_level_tracing_pass_performed = false",
            "read_only_symbol_level_tracing_results_created = false",
            "observed_symbol_records_created = false",
            "observed_call_path_records_created = false",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06262_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.262 Read-Only Symbol-Level Tracing Pass Candidate Review and Decision",
            "read_only_symbol_level_tracing_pass_candidate_review_completed = true",
            "read_only_symbol_level_tracing_pass_candidate_accepted = true",
            "future_read_only_symbol_level_tracing_pass_accepted = true",
            "future_symbol_trace_inventory_accepted = true",
            "future_trace_record_schema_accepted = true",
            "future_trace_status_vocabulary_accepted = true",
            "future_trace_pass_output_fields_accepted = true",
            "future_trace_candidate_procedure_accepted = true",
            "read_only_symbol_level_tracing_pass_performed = false",
            "read_only_symbol_level_tracing_results_created = false",
            "observed_symbol_records_created = false",
            "observed_call_path_records_created = false",
            "accepted_defect_records_created = false",
            "does not perform symbol-level tracing",
            "create symbol-level tracing results",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Accepted source symbol candidates are not observed symbols.",
            "Accepted call path candidates are not observed call paths.",
            "No private generated outputs are moved public in v0.6.262.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.262 - Read-Only Symbol-Level Tracing Pass Candidate Review and Decision",
            "Accepted the v0.6.261 documentation-only Read-Only Symbol-Level Tracing Pass Candidate",
            "read_only_symbol_level_tracing_pass_candidate_review_completed = true",
            "read_only_symbol_level_tracing_pass_candidate_accepted = true",
            "future_read_only_symbol_level_tracing_pass_accepted = true",
            "trace record schema",
            "accepted source symbol candidates are not observed symbols",
            "accepted call path candidates are not observed call paths",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.262",
            "v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
            "future read-only symbol-level tracing pass",
            "narrower symbol trace inventory",
            "code-inspection report candidate",
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


def test_v06262_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06262_read_only_symbol_level_tracing_pass_candidate_review_and_decision.py"])


def main() -> None:
    test_v06262_doc_tokens()
    test_v06262_adr_tokens()
    test_v06262_issue_tokens()
    test_v06262_index_tokens()
    test_v06262_registered_in_run_all()
    print("v0.6.262 read-only symbol-level tracing pass candidate review and decision checks passed")


if __name__ == "__main__":
    main()
