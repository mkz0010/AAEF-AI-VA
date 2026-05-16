from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/331-v06256-read-only-gateway-path-code-inspection-pass-with-findings-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0331-add-v06256-read-only-gateway-path-code-inspection-pass-with-findings-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0331-add-v06256-read-only-gateway-path-code-inspection-pass-with-findings-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "read_only_gateway_path_code_inspection_pass_with_findings_review_completed = true",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_accepted = true",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_id = read_only_gateway_path_code_inspection_pass_with_findings_candidate_v06255",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_review_result = accepted_for_symbol_level_tracing_and_later_scoped_implementation_planning_consideration",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_status = accepted_for_symbol_level_tracing_and_later_scoped_implementation_planning_consideration",
    "read_only_gateway_path_code_inspection_pass_with_findings_candidate_applied = false",
    "candidate_findings_accepted_for_symbol_level_tracing = true",
    "candidate_findings_accepted_as_defects = false",
    "candidate_findings_accepted_as_integration_proof = false",
    "candidate_findings_accepted_as_missing_integration_proof = false",
    "candidate_findings_accepted_for_implementation_change = false",
    "symbol_level_tracing_selected = false",
    "symbol_level_tracing_completed = false",
    "future_symbol_level_tracing_consideration_accepted = true",
    "future_scoped_implementation_planning_consideration_accepted = true",
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
    "source_file_existence_status",
    "keyword_level_helper_indicators",
    "keyword_level_gateway_path_indicators",
    "keyword_level_evidence_result_indicators",
    "gap_candidates",
    "source_symbol_exists_status",
    "gateway_path_invocation_status",
    "pre_dispatch_enforcement_status",
    "evidence_result_status",
    "recommended_next_action",
    "implementation_change_required",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
    "Previous checkpoint: v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
    "Reviewed candidate: `read_only_gateway_path_code_inspection_pass_with_findings_candidate_v06255`",
    "Decision result: accepted for symbol-level tracing and later scoped implementation planning consideration",
    "No private generated outputs are moved public in v0.6.256.",
    "source_file_existence_and_keyword_level_indicators_only",
    "candidate_findings_not_yet_reviewed",
    "keyword_level_indicator != symbol_level_proof",
    "gap_candidate != accepted_defect",
    "read_only_inspection_findings != implementation_change",
    "candidate findings are useful for prioritizing symbol-level tracing",
    "candidate findings are not proof of gateway-path integration",
    "candidate findings are not proof of missing integration",
    "candidate findings are not implementation changes",
    "candidate findings are not production readiness evidence",
    "candidate findings are not scanner readiness evidence",
    "gap candidates without treating them as accepted defects",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_created = false",
    "implementation_changes_are_deferred = true",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06256_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SCOPE_TOKENS)


def test_v06256_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0331",
            "Status: accepted",
            "Accept the v0.6.255 finding candidate set",
            "Keyword-level indicators are not symbol-level proof.",
            "Gap candidates are not accepted defects.",
            "Read-only findings are not implementation changes.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.256.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06256_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0331 - Add v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
            "Status: completed by v0.6.256",
            "candidate_findings_accepted_for_symbol_level_tracing = true",
            "candidate_findings_accepted_as_defects = false",
            "candidate_findings_accepted_as_integration_proof = false",
            "candidate_findings_accepted_for_implementation_change = false",
            "symbol_level_tracing_completed = false",
            "Proceed to v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06256_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.256 Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
            "read_only_gateway_path_code_inspection_pass_with_findings_review_completed = true",
            "read_only_gateway_path_code_inspection_pass_with_findings_candidate_accepted = true",
            "candidate_findings_accepted_for_symbol_level_tracing = true",
            "candidate_findings_accepted_as_defects = false",
            "candidate_findings_accepted_as_integration_proof = false",
            "candidate_findings_accepted_for_implementation_change = false",
            "symbol_level_tracing_completed = false",
            "does not create symbol-level tracing results",
            "create a code-inspection report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Keyword-level indicators are not symbol-level proof.",
            "Gap candidates are not accepted defects.",
            "No private generated outputs are moved public in v0.6.256.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.256 - Read-Only Gateway Path Code Inspection Pass With Findings Review and Decision",
            "Accepted the v0.6.255 Read-Only Gateway Path Code Inspection Pass With Findings Candidate",
            "candidate_findings_accepted_for_symbol_level_tracing = true",
            "candidate findings are not accepted defects",
            "symbol_level_tracing_completed = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.256",
            "v0.6.257 Next Work Selection Using Risk-Tiered Granularity",
            "symbol-level tracing planning",
            "narrower finding-disposition matrix",
            "code-inspection report candidate",
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


def test_v06256_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06256_read_only_gateway_path_code_inspection_pass_with_findings_review_and_decision.py"])


def main() -> None:
    test_v06256_doc_tokens()
    test_v06256_adr_tokens()
    test_v06256_issue_tokens()
    test_v06256_index_tokens()
    test_v06256_registered_in_run_all()
    print("v0.6.256 read-only gateway path code inspection pass with findings review and decision checks passed")


if __name__ == "__main__":
    main()
