from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/319-v06244-external-security-practitioner-review-intake-priority-reassessment.md"
ADR = ROOT / "planning/decisions/ADR-0319-add-v06244-external-security-practitioner-review-intake-priority-reassessment.md"
ISSUE = ROOT / "planning/issues/0319-add-v06244-external-security-practitioner-review-intake-priority-reassessment.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "external_review_intake_completed = true",
    "external_security_practitioner_review_received = true",
    "external_security_practitioner_review_date = 2026-05-16",
    "external_security_practitioner_review_target = v0.5.0_and_v0.6.243_equivalent",
    "external_review_overall_rating = B_conditional_poc_candidate",
    "priority_reassessment_completed = true",
    "prior_selected_work_item = record_candidate_artifact_creation_candidate",
    "prior_selected_work_item_source = v0.6.243",
    "prior_selected_work_item_deferred = true",
    "reassessed_next_priority = gateway_execution_path_integration_verification",
    "gateway_execution_path_integration_verification_selected = true",
    "record_candidate_artifact_creation_candidate_selected = false",
    "record_candidate_artifact_creation_candidate_created = false",
    "record_candidate_artifacts_created = false",
    "actual_records_created = false",
    "fixtures_created = false",
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

REQUIRED_REVIEW_TOKENS = [
    "external_review_design_quality_assessment = strong",
    "external_review_evidence_concept_assessment = strong",
    "external_review_initial_understanding_assessment = needs_entrypoint_improvement",
    "external_review_field_utility_assessment = poc_stage",
    "external_review_overclaim_risk_assessment = very_low",
    "external_review_commercial_explainability_assessment = promising_but_needs_demo",
]

REQUIRED_DOC_TOKENS = [
    "v0.6.244 External Security Practitioner Review Intake and Priority Reassessment",
    "Previous checkpoint: v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
    "Review source: external security practitioner review report dated 2026-05-16",
    "No private generated outputs are moved public in v0.6.244.",
    "gateway_execution_path_integration_verification",
    "authorization_expiry_current_time",
    "request_decision_constraint_diff_enforcement",
    "external_discovery_fail_closed_behavior",
    "scope_registry` runtime target validity checks",
    "mock_dry_run_completed_status_terminology",
    "human_approval` gate boundary",
    "This is not a scanner.",
    "external review intake is not customer PoC approval",
    "priority reassessment is not implementation",
    "gateway execution path verification selection is not gateway execution path modification",
    "record candidate artifact creation candidate deferral is not rejection",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06244_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_REVIEW_TOKENS)


def test_v06244_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0319",
            "Status: accepted",
            "Record the external review intake and reassess the next priority toward gateway execution path integration verification.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.244.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06244_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0319 - Add v0.6.244 External Security Practitioner Review Intake and Priority Reassessment",
            "Status: completed by v0.6.244",
            "external_review_intake_completed = true",
            "gateway_execution_path_integration_verification_selected = true",
            "Proceed to v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06244_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.244 External Security Practitioner Review Intake and Priority Reassessment",
            "prior_selected_work_item = record_candidate_artifact_creation_candidate",
            "reassessed_next_priority = gateway_execution_path_integration_verification",
            "does not change gateway behavior",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.244.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.244 - External Security Practitioner Review Intake and Priority Reassessment",
            "external_review_intake_completed = true",
            "external_review_overall_rating = B_conditional_poc_candidate",
            "priority_reassessment_completed = true",
            "gateway_execution_path_integration_verification",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.244",
            "v0.6.245 Next Work Selection Using Risk-Tiered Granularity",
            "gateway_execution_path_integration_verification",
            "README entrypoint compression planning",
            "mock/dry-run versus real execution status separation review",
            "safe local live demo planning",
            "human approval authenticity planning",
            "evidence tamper-evidence planning",
            "repository metadata scanner-misread cleanup",
        ],
    )


def test_v06244_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06244_external_security_practitioner_review_intake_priority_reassessment.py"])


def main() -> None:
    test_v06244_doc_tokens()
    test_v06244_adr_tokens()
    test_v06244_issue_tokens()
    test_v06244_index_tokens()
    test_v06244_registered_in_run_all()
    print("v0.6.244 external security practitioner review intake and priority reassessment checks passed")


if __name__ == "__main__":
    main()
