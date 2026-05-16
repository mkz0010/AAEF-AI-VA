from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/327-v06252-read-only-gateway-path-code-inspection-pass-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0327-add-v06252-read-only-gateway-path-code-inspection-pass-candidate.md"
ISSUE = ROOT / "planning/issues/0327-add-v06252-read-only-gateway-path-code-inspection-pass-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "read_only_gateway_path_code_inspection_pass_candidate_created = true",
    "read_only_gateway_path_code_inspection_pass_candidate_id = read_only_gateway_path_code_inspection_pass_candidate_v06252",
    "read_only_gateway_path_code_inspection_pass_candidate_status = candidate_not_applied",
    "read_only_gateway_path_code_inspection_pass_candidate_scope = documentation_only_read_only_gateway_path_code_inspection_pass",
    "selected_work_item = read_only_gateway_path_code_inspection_pass",
    "selected_work_item_status = read_only_gateway_path_code_inspection_pass_candidate_created",
    "planned_read_only_inspection_inventory_defined = true",
    "planned_source_file_candidates_defined = true",
    "planned_inspection_dimensions_defined = true",
    "planned_status_vocabulary_defined = true",
    "planned_read_only_procedure_defined = true",
    "planned_pass_output_fields_defined = true",
    "planned_finding_fields_defined = true",
    "source_file_exists_status_dimension_defined = true",
    "source_symbol_exists_status_dimension_defined = true",
    "implementation_change_required_dimension_defined = true",
    "read_only_gateway_path_code_inspection_performed = false",
    "read_only_gateway_path_code_inspection_findings_recorded = false",
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

REQUIRED_SOURCE_FILE_TOKENS = [
    "tools/run_tool_gateway_example.py",
    "tools/test_tool_gateway_runner.py",
    "tools/test_tool_gateway_adapters.py",
    "tools/validate_mvp_schemas.py",
    "tools/validate_mvp_examples.py",
    "tools/test_controlled_executor_policy.py",
    "tools/test_real_execution_readiness_gate.py",
    "tools/test_authorization_expiry_current_time_check.py",
    "tools/test_request_decision_constraint_diff_enforcement.py",
    "tools/test_external_discovery_fail_closed_behavior.py",
    "tools/test_mock_dry_run_completed_status_terminology.py",
    "tools/test_scope_registry.py",
    "tools/validate_generated_outputs.py",
    "tools/test_human_approval_gate.py",
    "tools/test_evidence_chain_linkage.py",
]

REQUIRED_INVENTORY_TOKENS = [
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
    "helper_exists",
    "helper_tested",
    "helper_invoked_by_gateway_path",
    "helper_enforced_before_dispatch",
    "helper_result_evidenced",
    "helper_gap_identified",
    "source_file_exists_status",
    "source_symbol_exists_status",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.252 Read-Only Gateway Path Code Inspection Pass Candidate",
    "Previous checkpoint: v0.6.251 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `read_only_gateway_path_code_inspection_pass`",
    "Application status: inspection pass candidate only; no code inspection findings recorded and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.252.",
    "Does the gateway execution path invoke, enforce, and evidence each safety helper or control before dispatch?",
    "read_only_inspection_pass_candidate != inspection_findings",
    "inspection_findings != implementation_change",
    "inspection_status_default = inspection_not_performed",
    "read-only inspection pass candidate is not code inspection",
    "read-only inspection pass candidate is not gateway execution path modification",
    "planned source-file candidates are not confirmed existing targets",
    "planned findings fields are not findings",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.253 Read-Only Gateway Path Code Inspection Pass Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06252_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SOURCE_FILE_TOKENS + REQUIRED_INVENTORY_TOKENS)


def test_v06252_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0327",
            "Status: proposed candidate",
            "Create a Read-Only Gateway Path Code Inspection Pass Candidate.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.252.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06252_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0327 - Add v0.6.252 Read-Only Gateway Path Code Inspection Pass Candidate",
            "Status: completed by v0.6.252",
            "read_only_gateway_path_code_inspection_pass",
            "read_only_gateway_path_code_inspection_pass_candidate_created = true",
            "read_only_gateway_path_code_inspection_performed = false",
            "read_only_gateway_path_code_inspection_findings_recorded = false",
            "Proceed to v0.6.253 Read-Only Gateway Path Code Inspection Pass Review and Decision",
        ],
    )


def test_v06252_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.252 Read-Only Gateway Path Code Inspection Pass Candidate",
            "helper_invoked_by_gateway_path",
            "helper_enforced_before_dispatch",
            "source_file_exists_status",
            "source_symbol_exists_status",
            "implementation_change_required",
            "does not perform code inspection",
            "record inspection findings",
            "create a code-inspection report",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.252.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.252 - Read-Only Gateway Path Code Inspection Pass Candidate",
            "read_only_gateway_path_code_inspection_pass_candidate_created = true",
            "read_only_gateway_path_code_inspection_pass_candidate_id = read_only_gateway_path_code_inspection_pass_candidate_v06252",
            "planned read-only inspection inventory",
            "source-file candidates",
            "finding fields",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.252",
            "v0.6.253 Read-Only Gateway Path Code Inspection Pass Review and Decision",
            "no code inspection findings",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06252_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06252_read_only_gateway_path_code_inspection_pass_candidate.py"])


def main() -> None:
    test_v06252_doc_tokens()
    test_v06252_adr_tokens()
    test_v06252_issue_tokens()
    test_v06252_index_tokens()
    test_v06252_registered_in_run_all()
    print("v0.6.252 read-only gateway path code inspection pass candidate checks passed")


if __name__ == "__main__":
    main()
