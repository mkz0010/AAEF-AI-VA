from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/330-v06255-read-only-gateway-path-code-inspection-pass-with-findings-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0330-add-v06255-read-only-gateway-path-code-inspection-pass-with-findings-candidate.md"
ISSUE = ROOT / "planning/issues/0330-add-v06255-read-only-gateway-path-code-inspection-pass-with-findings-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_created = true",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_id = read_only_gateway_path_code_inspection_pass_with_findings_candidate_v06255",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_status = candidate_with_read_only_findings",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_scope = read_only_keyword_and_file_existence_inspection",
    "selected_work_item = read_only_gateway_path_code_inspection_pass_with_findings",
    "selected_work_item_status = read_only_gateway_path_code_inspection_pass_with_findings_candidate_created",
    "read_only_gateway_path_code_inspection_performed = true",
    "read_only_gateway_path_code_inspection_findings_recorded = true",
    "read_only_gateway_path_code_inspection_findings_status = candidate_findings_not_yet_reviewed",
    "read_only_gateway_path_code_inspection_findings_scope = source_file_existence_and_keyword_level_indicators_only",
    "verified_repository_revision_recorded = true",
    "inspection_target_count_recorded = true",
    "source_file_exists_count_recorded = true",
    "gap_identified_count_recorded = true",
    "symbol_level_tracing_completed = false",
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
    "inspection_finding_id",
    "inventory_target_id",
    "source_file_exists_status",
    "source_symbol_exists_status",
    "helper_exists_status",
    "helper_tested_status",
    "gateway_path_invocation_status",
    "pre_dispatch_enforcement_status",
    "evidence_result_status",
    "gap_status",
    "gap_description",
    "recommended_next_action",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
    "Previous checkpoint: v0.6.254 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `read_only_gateway_path_code_inspection_pass_with_findings`",
    "Application status: read-only finding candidates only; no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.255.",
    "Are the safety helpers and controls actually invoked, enforced, and evidenced in the gateway execution path before dispatch?",
    "source-file existence and keyword-level indicators",
    "keyword_level_indicator != symbol_level_proof",
    "source_file_exists_status != source_symbol_exists_status",
    "gap_candidate != accepted_defect",
    "read-only finding candidates are not implementation changes",
    "read-only finding candidates are not proof that all helpers are integrated",
    "keyword-level indicators are not symbol-level proof",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06255_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06255_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0330",
            "Status: proposed candidate",
            "Create a Read-Only Gateway Path Code Inspection Pass With Findings Candidate.",
            "Keyword-level indicators are not symbol-level proof.",
            "Read-only finding candidates are not implementation changes.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.255.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06255_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0330 - Add v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
            "Status: completed by v0.6.255",
            "read_only_gateway_path_code_inspection_pass_with_findings",
            "read_only_gateway_path_code_inspection_pass_with_findings_candidate_created = true",
            "read_only_gateway_path_code_inspection_performed = true",
            "read_only_gateway_path_code_inspection_findings_recorded = true",
            "symbol_level_tracing_completed = false",
            "Proceed to v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
        ],
    )


def test_v06255_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
            "read_only_gateway_path_code_inspection_pass_with_findings_candidate_created = true",
            "read_only_gateway_path_code_inspection_performed = true",
            "read_only_gateway_path_code_inspection_findings_recorded = true",
            "symbol_level_tracing_completed = false",
            "does not create a code-inspection report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Keyword-level indicators are not symbol-level proof.",
            "No private generated outputs are moved public in v0.6.255.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.255 - Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
            "read_only_gateway_path_code_inspection_pass_with_findings_candidate_created = true",
            "read_only_gateway_path_code_inspection_performed = true",
            "read_only_gateway_path_code_inspection_findings_recorded = true",
            "source-file existence and keyword-level indicators",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.255",
            "v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06255_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06255_read_only_gateway_path_code_inspection_pass_with_findings_candidate.py"])


def main() -> None:
    test_v06255_doc_tokens()
    test_v06255_adr_tokens()
    test_v06255_issue_tokens()
    test_v06255_index_tokens()
    test_v06255_registered_in_run_all()
    print("v0.6.255 read-only gateway path code inspection pass with findings candidate checks passed")


if __name__ == "__main__":
    main()
