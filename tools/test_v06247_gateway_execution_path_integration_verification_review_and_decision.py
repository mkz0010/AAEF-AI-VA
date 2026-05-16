from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/322-v06247-gateway-execution-path-integration-verification-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0322-add-v06247-gateway-execution-path-integration-verification-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0322-add-v06247-gateway-execution-path-integration-verification-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "gateway_execution_path_integration_verification_candidate_review_completed = true",
    "gateway_execution_path_integration_verification_candidate_accepted = true",
    "gateway_execution_path_integration_verification_candidate_id = gateway_execution_path_integration_verification_candidate_v06246",
    "gateway_execution_path_integration_verification_candidate_review_result = accepted_for_future_gateway_path_integration_verification_report_or_inspection_checkpoint",
    "gateway_execution_path_integration_verification_candidate_status = accepted_for_future_gateway_path_integration_verification_report_or_inspection_checkpoint",
    "gateway_execution_path_integration_verification_candidate_applied = false",
    "future_gateway_path_integration_verification_report_accepted = true",
    "future_gateway_path_integration_inspection_checkpoint_accepted = true",
    "gateway_execution_path_integration_verification_report_created = false",
    "gateway_execution_path_integration_inspection_performed = false",
    "gateway_execution_path_behavior_modified = false",
    "tool_gateway_behavior_changed = false",
    "adapter_behavior_changed = false",
    "schema_changed = false",
    "runtime_behavior_changed = false",
    "scanner_behavior_changed = false",
    "publication_approval = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
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
]

REQUIRED_DOC_TOKENS = [
    "v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
    "Previous checkpoint: v0.6.246 Gateway Execution Path Integration Verification Candidate",
    "Reviewed candidate: `gateway_execution_path_integration_verification_candidate_v06246`",
    "Decision result: accepted for future gateway-path integration verification report or inspection checkpoint",
    "Application status: review only; no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.247.",
    "helper_exists",
    "helper_tested",
    "helper_invoked_by_gateway_path",
    "helper_enforced_before_dispatch",
    "helper_result_evidenced",
    "helper_gap_identified",
    "helper_exists != helper_enforced_before_dispatch",
    "helper_tested != helper_invoked_by_gateway_path",
    "gateway_runner_passes != all_safety_helpers_integrated",
    "mock_completion != real_execution_completion",
    "verified_integrated",
    "verified_not_integrated",
    "partially_integrated",
    "verification_required",
    "gap_identified",
    "accepted report model is not a verification report",
    "code inspection is not performed in v0.6.247",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06247_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_INVENTORY_TOKENS)


def test_v06247_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0322",
            "Status: accepted",
            "Accept the v0.6.246 Gateway Execution Path Integration Verification Candidate",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.247.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06247_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0322 - Add v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
            "Status: completed by v0.6.247",
            "gateway_execution_path_integration_verification_candidate_review_completed = true",
            "future_gateway_path_integration_verification_report_accepted = true",
            "future_gateway_path_integration_inspection_checkpoint_accepted = true",
            "gateway_execution_path_integration_verification_report_created = false",
            "gateway_execution_path_integration_inspection_performed = false",
            "Proceed to v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06247_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.247 Gateway Execution Path Integration Verification Review and Decision",
            "gateway_execution_path_integration_verification_candidate_v06246",
            "gateway_execution_path_integration_verification_candidate_accepted = true",
            "future_gateway_path_integration_verification_report_accepted = true",
            "future_gateway_path_integration_inspection_checkpoint_accepted = true",
            "does not create a verification report",
            "does not create a verification report, perform code inspection, change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.247.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.247 - Gateway Execution Path Integration Verification Review and Decision",
            "Accepted the v0.6.246 documentation-only Gateway Execution Path Integration Verification Candidate",
            "gateway_execution_path_integration_verification_candidate_review_completed = true",
            "gateway_execution_path_integration_verification_candidate_accepted = true",
            "future_gateway_path_integration_verification_report_accepted = true",
            "future_gateway_path_integration_inspection_checkpoint_accepted = true",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.247",
            "v0.6.248 Next Work Selection Using Risk-Tiered Granularity",
            "gateway-path integration verification report",
            "gateway-path code-inspection checkpoint",
            "narrower pre-inspection checklist",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06247_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06247_gateway_execution_path_integration_verification_review_and_decision.py"])


def main() -> None:
    test_v06247_doc_tokens()
    test_v06247_adr_tokens()
    test_v06247_issue_tokens()
    test_v06247_index_tokens()
    test_v06247_registered_in_run_all()
    print("v0.6.247 gateway execution path integration verification review and decision checks passed")


if __name__ == "__main__":
    main()
