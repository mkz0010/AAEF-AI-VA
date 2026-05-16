from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/321-v06246-gateway-execution-path-integration-verification-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0321-add-v06246-gateway-execution-path-integration-verification-candidate.md"
ISSUE = ROOT / "planning/issues/0321-add-v06246-gateway-execution-path-integration-verification-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "gateway_execution_path_integration_verification_candidate_created = true",
    "gateway_execution_path_integration_verification_candidate_id = gateway_execution_path_integration_verification_candidate_v06246",
    "gateway_execution_path_integration_verification_candidate_status = candidate_not_applied",
    "gateway_execution_path_integration_verification_candidate_scope = documentation_only_gateway_path_integration_verification",
    "selected_work_item = gateway_execution_path_integration_verification",
    "selected_work_item_status = gateway_execution_path_integration_verification_candidate_created",
    "helper_exists_dimension_defined = true",
    "helper_tested_dimension_defined = true",
    "helper_invoked_by_gateway_path_dimension_defined = true",
    "helper_enforced_before_dispatch_dimension_defined = true",
    "helper_result_evidenced_dimension_defined = true",
    "helper_gap_identified_dimension_defined = true",
    "authorization_expiry_current_time_inventory_included = true",
    "request_decision_constraint_diff_enforcement_inventory_included = true",
    "external_discovery_fail_closed_behavior_inventory_included = true",
    "gateway_execution_path_integration_verification_applied = false",
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

REQUIRED_VERIFICATION_TOKENS = [
    "helper_exists",
    "helper_tested",
    "helper_invoked_by_gateway_path",
    "helper_enforced_before_dispatch",
    "helper_result_evidenced",
    "helper_gap_identified",
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
]

REQUIRED_DOC_TOKENS = [
    "v0.6.246 Gateway Execution Path Integration Verification Candidate",
    "Previous checkpoint: v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `gateway_execution_path_integration_verification`",
    "Application status: verification candidate only; no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.246.",
    "helper_exists != helper_enforced_before_dispatch",
    "helper_tested != helper_invoked_by_gateway_path",
    "gateway_runner_passes != all_safety_helpers_integrated",
    "mock_completion != real_execution_completion",
    "verification_required",
    "helper existence is not helper enforcement",
    "helper unit tests are not gateway path integration",
    "gateway execution path verification candidate is not gateway execution path modification",
    "gateway execution path verification candidate is not proof that all helpers are integrated",
    "candidate inventory is not implementation evidence",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06246_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_VERIFICATION_TOKENS)


def test_v06246_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0321",
            "Status: proposed candidate",
            "Create a Gateway Execution Path Integration Verification Candidate.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.246.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06246_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0321 - Add v0.6.246 Gateway Execution Path Integration Verification Candidate",
            "Status: completed by v0.6.246",
            "gateway_execution_path_integration_verification",
            "gateway_execution_path_integration_verification_candidate_created = true",
            "helper_exists_dimension_defined = true",
            "helper_invoked_by_gateway_path_dimension_defined = true",
            "Proceed to v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
        ] + REQUIRED_VERIFICATION_TOKENS[:8],
    )


def test_v06246_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.246 Gateway Execution Path Integration Verification Candidate",
            "helper_invoked_by_gateway_path",
            "helper_enforced_before_dispatch",
            "helper_gap_identified",
            "does not change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.246.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.246 - Gateway Execution Path Integration Verification Candidate",
            "gateway_execution_path_integration_verification_candidate_created = true",
            "gateway_execution_path_integration_verification_candidate_id = gateway_execution_path_integration_verification_candidate_v06246",
            "helper_invoked_by_gateway_path",
            "authorization_expiry_current_time",
            "request_decision_constraint_diff_enforcement",
            "external_discovery_fail_closed_behavior",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.246",
            "v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06246_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06246_gateway_execution_path_integration_verification_candidate.py"])


def main() -> None:
    test_v06246_doc_tokens()
    test_v06246_adr_tokens()
    test_v06246_issue_tokens()
    test_v06246_index_tokens()
    test_v06246_registered_in_run_all()
    print("v0.6.246 gateway execution path integration verification candidate checks passed")


if __name__ == "__main__":
    main()
