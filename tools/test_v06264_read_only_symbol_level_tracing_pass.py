from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/339-v06264-read-only-symbol-level-tracing-pass.md"
ADR = ROOT / "planning/decisions/ADR-0339-add-v06264-read-only-symbol-level-tracing-pass.md"
ISSUE = ROOT / "planning/issues/0339-add-v06264-read-only-symbol-level-tracing-pass.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "read_only_symbol_level_tracing_pass_performed = true",
    "read_only_symbol_level_tracing_pass_completed = true",
    "read_only_symbol_level_tracing_pass_id = read_only_symbol_level_tracing_pass_v06264",
    "read_only_symbol_level_tracing_pass_status = completed_read_only_static_symbol_inspection",
    "read_only_symbol_level_tracing_pass_scope = static_source_file_symbol_and_call_status_inspection",
    "selected_work_item = read_only_symbol_level_tracing_pass",
    "selected_work_item_status = read_only_symbol_level_tracing_pass_completed",
    "verified_repository_revision_recorded = true",
    "source_file_observation_records_created = true",
    "source_symbol_observation_records_created = true",
    "call_path_status_records_created = true",
    "symbol_trace_records_created = true",
    "read_only_symbol_level_tracing_results_created = true",
    "symbol_level_tracing_results_created = true",
    "accepted_defect_records_created = false",
    "candidate_findings_accepted_as_defects = false",
    "candidate_findings_accepted_as_integration_proof = false",
    "candidate_findings_accepted_as_missing_integration_proof = false",
    "candidate_findings_accepted_for_implementation_change = false",
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
    "source_file_observed_status",
    "source_symbol_observed",
    "source_symbol_kind",
    "call_path_observed_status",
    "pre_dispatch_enforcement_status",
    "evidence_generation_status",
    "implementation_change_required",
    "source_file_candidate_count",
    "source_file_observed_count",
    "source_symbol_observed_count",
    "call_path_status_records_created",
    "symbol_trace_record_count",
    "trace_record_schema",
    "trace_candidate",
    "source_file_observed",
    "source_symbol_observed",
    "call_path_observed",
    "verification_required",
    "gap_identified",
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
    "v0.6.264 Read-Only Symbol-Level Tracing Pass",
    "Previous checkpoint: v0.6.263 Next Work Selection Using Risk-Tiered Granularity",
    "Pass result: read-only symbol-level tracing pass performed with static inspection records",
    "Application status: read-only inspection only; no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.264.",
    "Which concrete source symbols and static call-path status records can be observed",
    "static_symbol_observation != runtime_execution_proof",
    "static_call_path_status != gateway_integration_proof",
    "source_symbol_observed != helper_enforced_before_dispatch",
    "call_path_observed != complete_gateway_execution_path_verification",
    "trace_result != accepted_defect",
    "trace_result != implementation_change",
    "source-symbol observations support reviewer navigation",
    "call-path status records support further review",
    "gap records support triage",
    "verification_required means do not claim integration yet",
    "read-only trace results are not implementation changes",
    "read-only symbol-level tracing results are static inspection records",
    "read-only symbol-level tracing results are not gateway execution path modification",
    "read-only symbol-level tracing results are not proof that all helpers are integrated",
    "observed source symbols are not proof of pre-dispatch enforcement",
    "observed call-path status records are not full gateway integration proof",
    "call-path not observed is not proof of missing integration",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.265 Read-Only Symbol-Level Tracing Pass Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06264_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_COMPONENT_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06264_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0339",
            "Status: accepted",
            "Perform a read-only symbol-level tracing pass using static source inspection.",
            "read_only_symbol_level_tracing_pass_performed = true",
            "source_file_observation_records_created = true",
            "source_symbol_observation_records_created = true",
            "call_path_status_records_created = true",
            "symbol_trace_records_created = true",
            "Read-only symbol-level tracing results are static inspection records.",
            "Observed source symbols are not proof of pre-dispatch enforcement.",
            "Observed call-path status records are not full gateway integration proof.",
            "No private generated outputs are moved public in v0.6.264.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06264_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0339 - Add v0.6.264 Read-Only Symbol-Level Tracing Pass",
            "Status: completed by v0.6.264",
            "read_only_symbol_level_tracing_pass",
            "read_only_symbol_level_tracing_pass_performed = true",
            "source_file_observation_records_created = true",
            "source_symbol_observation_records_created = true",
            "call_path_status_records_created = true",
            "symbol_trace_records_created = true",
            "read_only_symbol_level_tracing_results_created = true",
            "accepted_defect_records_created = false",
            "Proceed to v0.6.265 Read-Only Symbol-Level Tracing Pass Review and Decision",
        ],
    )


def test_v06264_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.264 Read-Only Symbol-Level Tracing Pass",
            "read_only_symbol_level_tracing_pass_performed = true",
            "read_only_symbol_level_tracing_pass_completed = true",
            "read_only_symbol_level_tracing_pass_id = read_only_symbol_level_tracing_pass_v06264",
            "source_file_observation_records_created = true",
            "source_symbol_observation_records_created = true",
            "call_path_status_records_created = true",
            "symbol_trace_records_created = true",
            "read_only_symbol_level_tracing_results_created = true",
            "accepted_defect_records_created = false",
            "does not create accepted defect records",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Read-only symbol-level tracing results are static inspection records.",
            "Observed source symbols are not proof of pre-dispatch enforcement.",
            "Observed call-path status records are not full gateway integration proof.",
            "No private generated outputs are moved public in v0.6.264.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.264 - Read-Only Symbol-Level Tracing Pass",
            "Performed the first read-only static symbol-level tracing pass.",
            "read_only_symbol_level_tracing_pass_performed = true",
            "read_only_symbol_level_tracing_pass_completed = true",
            "read_only_symbol_level_tracing_pass_id = read_only_symbol_level_tracing_pass_v06264",
            "source-file observation records",
            "source-symbol observation records",
            "call-path status records",
            "symbol trace records",
            "read_only_symbol_level_tracing_results_created = true",
            "accepted_defect_records_created = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.264",
            "v0.6.265 Read-Only Symbol-Level Tracing Pass Review and Decision",
            "narrower manual trace review",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report candidate",
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


def test_v06264_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06264_read_only_symbol_level_tracing_pass.py"])


def main() -> None:
    test_v06264_doc_tokens()
    test_v06264_adr_tokens()
    test_v06264_issue_tokens()
    test_v06264_index_tokens()
    test_v06264_registered_in_run_all()
    print("v0.6.264 read-only symbol-level tracing pass checks passed")


if __name__ == "__main__":
    main()
