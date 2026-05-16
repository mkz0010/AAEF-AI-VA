from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/320-v06245-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0320-add-v06245-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0320-add-v06245-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = gateway_execution_path_integration_verification",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = external_review_prioritized_gateway_execution_path_integration_verification_before_more_artifact_candidate_work",
    "gateway_execution_path_integration_verification_selected = true",
    "gateway_execution_path_integration_verification_candidate_created = false",
    "gateway_execution_path_integration_verification_applied = false",
    "record_candidate_artifact_creation_candidate_selected = false",
    "record_candidate_artifact_creation_candidate_created = false",
    "record_candidate_artifacts_created = false",
    "actual_records_created = false",
    "fixtures_created = false",
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

REQUIRED_VERIFICATION_TOKENS = [
    "authorization_expiry_current_time",
    "request_decision_constraint_diff_enforcement",
    "external_discovery_fail_closed_behavior",
    "scope_registry` runtime target validity checks",
    "mock_dry_run_completed_status_terminology",
    "credential_ref` resolution boundary",
    "human_approval` gate boundary",
    "helper_exists",
    "helper_tested",
    "helper_invoked_by_gateway_path",
    "helper_enforced_before_dispatch",
    "helper_result_evidenced",
    "helper_gap_identified",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.244 External Security Practitioner Review Intake and Priority Reassessment",
    "Selection result: `gateway_execution_path_integration_verification`",
    "Application status: selection only; no gateway behavior changed",
    "No private generated outputs are moved public in v0.6.245.",
    "gateway execution path integration verification",
    "helper existence is not helper enforcement",
    "helper unit tests are not gateway path integration",
    "gateway execution path verification selection is not gateway execution path modification",
    "gateway execution path verification selection is not proof that all helpers are integrated",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.246 Gateway Execution Path Integration Verification Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06245_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_VERIFICATION_TOKENS)


def test_v06245_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0320",
            "Status: accepted",
            "Select the following next work item",
            "gateway_execution_path_integration_verification",
            "This is a selection-only checkpoint.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.245.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06245_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0320 - Add v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.245",
            "selected_work_item = gateway_execution_path_integration_verification",
            "gateway_execution_path_integration_verification_selected = true",
            "gateway_execution_path_integration_verification_candidate_created = false",
            "Proceed to v0.6.246 Gateway Execution Path Integration Verification Candidate",
        ],
    )


def test_v06245_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
            "gateway_execution_path_integration_verification",
            "This is selection only.",
            "does not change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.245.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.245 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `gateway_execution_path_integration_verification` as the next work item",
            "next_work_selection_completed = true",
            "gateway_execution_path_integration_verification_selected = true",
            "gateway_execution_path_integration_verification_candidate_created = false",
            "validator success is structural only",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.245",
            "v0.6.246 Gateway Execution Path Integration Verification Candidate",
            "authorization_expiry_current_time",
            "request_decision_constraint_diff_enforcement",
            "external_discovery_fail_closed_behavior",
            "no gateway behavior change",
            "no adapter behavior change",
            "no schema behavior change",
            "no runtime behavior change",
            "no scanner behavior change",
        ],
    )


def test_v06245_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06245_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06245_doc_tokens()
    test_v06245_adr_tokens()
    test_v06245_issue_tokens()
    test_v06245_index_tokens()
    test_v06245_registered_in_run_all()
    print("v0.6.245 next work selection checks passed")


if __name__ == "__main__":
    main()
