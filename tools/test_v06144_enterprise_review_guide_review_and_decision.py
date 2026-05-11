from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "docs/enterprise-review-guide.md"
DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0214-add-v06144-enterprise-review-guide-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0213-add-v06144-enterprise-review-guide-review-and-decision.md"
V06143_DOC = ROOT / "docs/219-v06143-enterprise-review-guide-candidate.md"
V06142_DOC = ROOT / "docs/218-v06142-next-work-selection-using-risk-tiered-granularity.md"
V06141_DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 2 of 2 for a Medium-risk buyer/reviewer-facing documentation work item.', 'This checkpoint reviews and accepts the Enterprise Review Guide candidate from v0.6.143.', 'The Enterprise Review Guide work item is closed.', 'Review conclusion', 'Candidate accepted', 'Reader fit confirmed', 'Project positioning confirmed', 'Evidence review questions confirmed', 'Gate-semantics review questions confirmed', 'Demo boundary confirmed', 'Deployment due-diligence prompts confirmed', 'Commercial evaluation boundary confirmed', 'Claim boundaries confirmed', 'Non-authorizing boundary confirmed', 'Reviewed guide sections', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.145 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_GUIDE_PHRASES = ['# Enterprise Review Guide', 'Reader', 'Purpose', 'What AAEF-AI-VA demonstrates', 'What AAEF-AI-VA does not demonstrate', 'Review path', 'Evidence review questions', 'Gate-semantics review questions', 'Demo boundary review', 'Deployment due-diligence prompts', 'Commercial evaluation boundary', 'Claim boundaries', 'Decision-maker summary', 'AI output is a request; gates decide execution.', 'This guide is not a certification scheme.', 'This guide is not a legal compliance statement.', 'This guide is not an audit opinion.', 'This guide does not authorize third-party testing.', 'This guide does not assert deployment sufficiency.', 'This guide does not assert equivalence with external frameworks.']
FORBIDDEN_AFFIRMATIVE_PHRASES = ['is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'audit sufficiency achieved', 'deployment approved', 'is production ready', 'production-ready scanner', 'authorized to test third-party systems', 'authorized for third-party testing by this guide', 'equivalent to nist', 'equivalent to iso', 'safe to run without gates', 'ai can safely run tools without gates', 'aaef core promotion = true', 'aaef profile promotion = true', 'aaef practical package promotion = true']
FLAGS = ['enterprise_review_guide_review_decision_completed = true', 'enterprise_review_guide_review_decision_is_medium_risk = true', 'enterprise_review_guide_review_decision_checkpoint_2_of_2 = true', 'enterprise_review_guide_candidate_reviewed = true', 'enterprise_review_guide_candidate_accepted = true', 'enterprise_review_guide_work_item_closed = true', 'enterprise_review_guide_file_reviewed = true', 'enterprise_review_guide_reader_fit_confirmed = true', 'enterprise_review_guide_project_positioning_confirmed = true', 'enterprise_review_guide_review_path_confirmed = true', 'enterprise_review_guide_evidence_review_questions_confirmed = true', 'enterprise_review_guide_gate_semantics_review_questions_confirmed = true', 'enterprise_review_guide_demo_boundary_confirmed = true', 'enterprise_review_guide_deployment_due_diligence_prompts_confirmed = true', 'enterprise_review_guide_commercial_evaluation_boundary_confirmed = true', 'enterprise_review_guide_claim_boundaries_confirmed = true', 'enterprise_review_guide_non_authorizing_boundary_confirmed = true', 'enterprise_review_guide_reviewer_usefulness_confirmed = true', 'enterprise_review_guide_created = true', 'enterprise_review_guide_review_decision_completed = true', 'review_decision_completed = true', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.145 Next Work Selection Using Risk-Tiered Granularity']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [GUIDE, DOC, ADR, ISSUE, V06143_DOC, V06142_DOC, V06141_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    guide_text = GUIDE.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_GUIDE_PHRASES:
        require(phrase in guide_text, f"Enterprise Review Guide missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.144 document missing required text: {phrase}")

    for phrase in [
        "What did the AI request?",
        "What authority existed at decision time?",
        "What gate allowed, blocked, or required human approval?",
        "Can the project show what the AI requested?",
        "Can the project distinguish execution from non-execution?",
        "Is authorization evaluated against the relevant current time?",
        "Can a request drift from the authorization decision without being detected?",
        "Does external discovery fail closed unless explicitly allowed and boundary-compatible?",
        "Can this architecture make AI-assisted diagnostic requests reviewable, gated, and evidence-linked before any real action is allowed?",
    ]:
        require(phrase in guide_text, f"Enterprise Review Guide missing reviewed reviewer question/framing: {phrase}")

    combined_lower = (guide_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06143 = V06143_DOC.read_text(encoding="utf-8")
    for phrase in [
        "enterprise_review_guide_candidate_completed = true",
        "enterprise_review_guide_candidate_checkpoint_1_of_2 = true",
        "enterprise_review_guide_created = true",
        "enterprise_review_guide_candidate_claim_safe = true",
        "selected_next_checkpoint = v0.6.144 Enterprise Review Guide Review and Decision",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06143, f"v0.6.143 candidate missing required phrase: {phrase}")

    v06142 = V06142_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = enterprise_review_guide",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.143 Enterprise Review Guide Candidate",
    ]:
        require(phrase in v06142, f"v0.6.142 selection missing required phrase: {phrase}")

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
        "runtime execution is authorized by this review",
        "scanner execution is authorized by this review",
        "credential injection is permitted by this review",
        "this review opens an aaef main issue",
        "this review submits to aaef main",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.144 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.144 Enterprise Review Guide review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
