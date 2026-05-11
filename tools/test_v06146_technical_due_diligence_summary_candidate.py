from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "docs/technical-due-diligence-summary.md"
DOC = ROOT / "docs/222-v06146-technical-due-diligence-summary-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0216-add-v06146-technical-due-diligence-summary-candidate.md"
ISSUE = ROOT / "planning/issues/0215-add-v06146-technical-due-diligence-summary-candidate.md"
V06145_DOC = ROOT / "docs/221-v06145-next-work-selection-using-risk-tiered-granularity.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06143_DOC = ROOT / "docs/219-v06143-enterprise-review-guide-candidate.md"
V06141_DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk technical reviewer-facing documentation work item.', 'This checkpoint creates the Technical Due Diligence Summary candidate.', 'The review and decision are deferred to v0.6.147.', 'Candidate implementation summary', 'Candidate summary', 'Claim boundaries', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.147 Technical Due Diligence Summary Review and Decision']
REQUIRED_SUMMARY_PHRASES = ['# Technical Due Diligence Summary', 'Reader', 'Purpose', 'Technical positioning', 'Control surface overview', 'Repository review surface', 'Evidence paths', 'Gate-semantics checks', 'Non-execution boundaries', 'Runtime boundary', 'Credential and data boundary', 'Public/private artifact boundary', 'Due-diligence questions', 'Review artifacts to inspect', 'Follow-on PoC considerations', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'This summary is not a certification scheme.', 'This summary is not a legal compliance statement.', 'This summary is not an audit opinion.', 'This summary does not grant permission to test third-party systems.', 'This summary does not assert deployment sufficiency.', 'This summary does not assert equivalence with external frameworks.']
FLAGS = ['technical_due_diligence_summary_candidate_completed = true', 'technical_due_diligence_summary_candidate_is_medium_risk = true', 'technical_due_diligence_summary_candidate_checkpoint_1_of_2 = true', 'technical_due_diligence_summary_review_decision_deferred_to_v06147 = true', 'technical_due_diligence_summary_created = true', 'technical_due_diligence_summary_candidate_claim_safe = true', 'technical_due_diligence_summary_target_reader_identified = true', 'technical_due_diligence_summary_control_surface_included = true', 'technical_due_diligence_summary_repository_review_surface_included = true', 'technical_due_diligence_summary_evidence_paths_included = true', 'technical_due_diligence_summary_gate_semantics_checks_included = true', 'technical_due_diligence_summary_non_execution_boundary_included = true', 'technical_due_diligence_summary_runtime_boundary_included = true', 'technical_due_diligence_summary_credential_data_boundary_included = true', 'technical_due_diligence_summary_public_private_artifact_boundary_included = true', 'technical_due_diligence_summary_due_diligence_questions_included = true', 'technical_due_diligence_summary_claim_boundaries_included = true', 'technical_due_diligence_summary_review_decision_completed = false', 'review_decision_completed = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'enterprise_review_guide_modified = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.147 Technical Due Diligence Summary Review and Decision']

FORBIDDEN_AFFIRMATIVE_PHRASES = [
    "is certified as",
    "certified framework for",
    "legally compliant with",
    "legal compliance achieved",
    "audit opinion provided",
    "audit sufficiency achieved",
    "deployment approved",
    "is production ready",
    "production-ready scanner",
    "complete vulnerability scanner",
    "complete vulnerability assessment capability is provided",
    "authorized to test third-party systems",
    "authorized for third-party testing by this summary",
    "equivalent to nist",
    "equivalent to iso",
    "safe to run without gates",
    "ai can safely run tools without gates",
    "aaef core promotion = true",
    "aaef profile promotion = true",
    "aaef practical package promotion = true",
]

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [SUMMARY, DOC, ADR, ISSUE, V06145_DOC, V06144_DOC, V06143_DOC, V06141_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    summary_text = SUMMARY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_SUMMARY_PHRASES:
        require(phrase in summary_text, f"Technical Due Diligence Summary missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.146 document missing required text: {phrase}")

    for phrase in [
        "What exact action did the AI request?",
        "What gate made the execution decision?",
        "What evidence supported the gate outcome?",
        "Was authorization current at the relevant time?",
        "Did request constraints drift from decision constraints?",
        "Was external discovery explicitly allowed and boundary-compatible?",
        "Are mock/dry-run statuses disambiguated?",
        "AAEF-AI-VA is a safety-first reference implementation and technical control-boundary example",
    ]:
        require(phrase in summary_text, f"Technical Due Diligence Summary missing reviewer question/framing: {phrase}")

    combined_lower = (summary_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06145 = V06145_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = technical_due_diligence_summary",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.146 Technical Due Diligence Summary Candidate",
        "technical_due_diligence_summary_created = false",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06145, f"v0.6.145 selection missing required phrase: {phrase}")

    v06144 = V06144_DOC.read_text(encoding="utf-8")
    require("enterprise_review_guide_work_item_closed = true" in v06144, "v0.6.144 Enterprise Review Guide work item must remain closed")
    require("enterprise_review_guide_claim_boundaries_confirmed = true" in v06144, "v0.6.144 claim boundaries must remain confirmed")

    v06143 = V06143_DOC.read_text(encoding="utf-8")
    require("enterprise_review_guide_created = true" in v06143, "v0.6.143 Enterprise Review Guide creation must remain recorded")

    v06141 = V06141_DOC.read_text(encoding="utf-8")
    require("mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true" in v06141, "v0.6.141 mock/dry-run terminology work item must remain closed")

    v06138 = V06138_DOC.read_text(encoding="utf-8")
    require("external_discovery_fail_closed_behavior_work_item_closed = true" in v06138, "v0.6.138 external discovery work item must remain closed")

    v06134 = V06134_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_work_item_closed = true" in v06134, "v0.6.134 constraint-diff work item must remain closed")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must remain closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "runtime execution is authorized by this candidate",
        "scanner execution is authorized by this candidate",
        "credential injection is permitted by this candidate",
        "this candidate opens an aaef main issue",
        "this candidate submits to aaef main",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.146 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.146 Technical Due Diligence Summary candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
