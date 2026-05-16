from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/329-v06254-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0329-add-v06254-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0329-add-v06254-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = read_only_gateway_path_code_inspection_pass_with_findings",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_read_only_inspection_pass_candidate_requires_findings_before_report_or_implementation",
    "read_only_gateway_path_code_inspection_pass_with_findings_selected = true",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_created = false",
    "read_only_gateway_path_code_inspection_performed = false",
    "read_only_gateway_path_code_inspection_findings_recorded = false",
    "narrower_inspection_findings_candidate_selected = false",
    "narrower_inspection_findings_candidate_created = false",
    "code_inspection_report_candidate_selected = false",
    "code_inspection_report_candidate_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_selected = false",
    "gateway_path_integration_verification_report_created = false",
    "gateway_behavior_implementation_change_selected = false",
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
    "read_only_gateway_path_code_inspection_pass_with_findings",
    "narrower_inspection_findings_candidate",
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
    "target_id",
    "target_description",
    "source_file_candidates",
    "source_symbol_candidates",
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
    "v0.6.254 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.253 Read-Only Gateway Path Code Inspection Pass Review and Decision",
    "Selection result: `read_only_gateway_path_code_inspection_pass_with_findings`",
    "Application status: selection only; no code inspection findings recorded and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.254.",
    "Are the safety helpers and controls actually invoked, enforced, and evidenced in the gateway execution path before dispatch?",
    "This selection begins the transition from planning-only scaffolds toward actual read-only inspection findings.",
    "read-only inspection findings selection is not code inspection",
    "read-only inspection findings selection is not gateway execution path modification",
    "read-only inspection findings selection is not proof that all helpers are integrated",
    "findings are not implementation changes",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06254_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06254_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0329",
            "Status: accepted",
            "Select the following next work item",
            "read_only_gateway_path_code_inspection_pass_with_findings",
            "This is a selection-only checkpoint.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.254.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06254_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0329 - Add v0.6.254 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.254",
            "selected_work_item = read_only_gateway_path_code_inspection_pass_with_findings",
            "read_only_gateway_path_code_inspection_pass_with_findings_selected = true",
            "read_only_gateway_path_code_inspection_findings_recorded = false",
            "Proceed to v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
        ],
    )


def test_v06254_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.254 Next Work Selection Using Risk-Tiered Granularity",
            "read_only_gateway_path_code_inspection_pass_with_findings",
            "This is selection only.",
            "does not perform code inspection",
            "record inspection findings",
            "create a code-inspection report",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.254.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.254 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `read_only_gateway_path_code_inspection_pass_with_findings` as the next work item",
            "next_work_selection_completed = true",
            "read_only_gateway_path_code_inspection_pass_with_findings_selected = true",
            "read_only_gateway_path_code_inspection_findings_recorded = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.254",
            "v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
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


def test_v06254_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06254_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06254_doc_tokens()
    test_v06254_adr_tokens()
    test_v06254_issue_tokens()
    test_v06254_index_tokens()
    test_v06254_registered_in_run_all()
    print("v0.6.254 next work selection checks passed")


if __name__ == "__main__":
    main()
