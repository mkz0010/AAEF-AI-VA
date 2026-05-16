from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/324-v06249-gateway-path-code-inspection-checkpoint-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0324-add-v06249-gateway-path-code-inspection-checkpoint-candidate.md"
ISSUE = ROOT / "planning/issues/0324-add-v06249-gateway-path-code-inspection-checkpoint-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "gateway_path_code_inspection_checkpoint_candidate_created = true",
    "gateway_path_code_inspection_checkpoint_candidate_id = gateway_path_code_inspection_checkpoint_candidate_v06249",
    "gateway_path_code_inspection_checkpoint_candidate_status = candidate_not_applied",
    "gateway_path_code_inspection_checkpoint_candidate_scope = documentation_only_code_inspection_checkpoint_planning",
    "selected_work_item = gateway_path_code_inspection_checkpoint",
    "selected_work_item_status = gateway_path_code_inspection_checkpoint_candidate_created",
    "planned_inspection_target_inventory_defined = true",
    "planned_inventory_targets_defined = true",
    "planned_inspection_dimensions_defined = true",
    "planned_inspection_status_vocabulary_defined = true",
    "planned_code_inspection_method_defined = true",
    "planned_findings_format_defined = true",
    "planned_summary_fields_defined = true",
    "gateway_path_code_inspection_performed = false",
    "gateway_path_code_inspection_findings_recorded = false",
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

REQUIRED_INSPECTION_TOKENS = [
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
    "v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
    "Previous checkpoint: v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `gateway_path_code_inspection_checkpoint`",
    "Application status: inspection checkpoint candidate only; no code inspection findings recorded and no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.249.",
    "Where, if anywhere, is each safety helper or control connected to the gateway execution path before dispatch?",
    "target_existence_verification_required",
    "inspection_status_default = verification_required",
    "code_inspection_candidate != code_inspection_findings",
    "code-inspection checkpoint candidate is not code inspection",
    "code-inspection checkpoint candidate is not gateway execution path modification",
    "planned inspection targets are not confirmed existing targets",
    "verification report creation is deferred",
    "implementation changes are deferred",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.250 Gateway Path Code Inspection Checkpoint Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06249_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_INSPECTION_TOKENS)


def test_v06249_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0324",
            "Status: proposed candidate",
            "Create a Gateway Path Code Inspection Checkpoint Candidate.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.249.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06249_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0324 - Add v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
            "Status: completed by v0.6.249",
            "gateway_path_code_inspection_checkpoint",
            "gateway_path_code_inspection_checkpoint_candidate_created = true",
            "gateway_path_code_inspection_performed = false",
            "gateway_path_code_inspection_findings_recorded = false",
            "Proceed to v0.6.250 Gateway Path Code Inspection Checkpoint Review and Decision",
        ],
    )


def test_v06249_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.249 Gateway Path Code Inspection Checkpoint Candidate",
            "helper_invoked_by_gateway_path",
            "helper_enforced_before_dispatch",
            "helper_gap_identified",
            "does not perform code inspection",
            "record inspection findings",
            "create a verification report",
            "change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.249.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.249 - Gateway Path Code Inspection Checkpoint Candidate",
            "gateway_path_code_inspection_checkpoint_candidate_created = true",
            "gateway_path_code_inspection_checkpoint_candidate_id = gateway_path_code_inspection_checkpoint_candidate_v06249",
            "planned inspection targets",
            "findings format",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.249",
            "v0.6.250 Gateway Path Code Inspection Checkpoint Review and Decision",
            "no code inspection findings",
            "no gateway-path integration verification report",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06249_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06249_gateway_path_code_inspection_checkpoint_candidate.py"])


def main() -> None:
    test_v06249_doc_tokens()
    test_v06249_adr_tokens()
    test_v06249_issue_tokens()
    test_v06249_index_tokens()
    test_v06249_registered_in_run_all()
    print("v0.6.249 gateway path code inspection checkpoint candidate checks passed")


if __name__ == "__main__":
    main()
