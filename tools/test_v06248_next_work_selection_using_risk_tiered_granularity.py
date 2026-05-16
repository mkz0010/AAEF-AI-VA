from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/323-v06248-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0323-add-v06248-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0323-add-v06248-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = gateway_path_code_inspection_checkpoint",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_gateway_path_verification_candidate_requires_code_inspection_before_verification_report",
    "gateway_path_code_inspection_checkpoint_selected = true",
    "gateway_path_code_inspection_checkpoint_created = false",
    "gateway_path_code_inspection_performed = false",
    "gateway_path_integration_verification_report_selected = false",
    "gateway_path_integration_verification_report_created = false",
    "narrower_pre_inspection_checklist_selected = false",
    "record_candidate_artifact_creation_candidate_selected = false",
    "record_candidate_artifact_creation_candidate_created = false",
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

REQUIRED_INSPECTION_TOKENS = [
    "gateway_path_code_inspection_checkpoint",
    "gateway_path_integration_verification_report",
    "narrower_pre_inspection_checklist",
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
]

REQUIRED_DOC_TOKENS = [
    "v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
    "Selection result: `gateway_path_code_inspection_checkpoint`",
    "Application status: selection only; no code inspection performed and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.248.",
    "A direct verification report would be premature",
    "The selected checkpoint should inspect code paths and document findings",
    "code-inspection checkpoint selection is not code inspection",
    "code-inspection checkpoint selection is not gateway execution path modification",
    "code-inspection checkpoint selection is not proof that all helpers are integrated",
    "verification report selection is deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06248_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_INSPECTION_TOKENS)


def test_v06248_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0323",
            "Status: accepted",
            "Select the following next work item",
            "gateway_path_code_inspection_checkpoint",
            "This is a selection-only checkpoint.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.248.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06248_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0323 - Add v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.248",
            "selected_work_item = gateway_path_code_inspection_checkpoint",
            "gateway_path_code_inspection_checkpoint_selected = true",
            "gateway_path_code_inspection_performed = false",
            "Proceed to v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
        ],
    )


def test_v06248_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
            "gateway_path_code_inspection_checkpoint",
            "This is selection only.",
            "does not perform code inspection",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.248.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.248 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `gateway_path_code_inspection_checkpoint` as the next work item",
            "gateway_path_code_inspection_checkpoint_selected = true",
            "gateway_path_code_inspection_performed = false",
            "gateway_path_integration_verification_report",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.248",
            "v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
            "no code inspection performed yet",
            "no gateway-path integration verification report",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06248_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06248_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06248_doc_tokens()
    test_v06248_adr_tokens()
    test_v06248_issue_tokens()
    test_v06248_index_tokens()
    test_v06248_registered_in_run_all()
    print("v0.6.248 next work selection checks passed")


if __name__ == "__main__":
    main()
