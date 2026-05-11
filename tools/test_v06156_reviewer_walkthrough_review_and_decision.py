from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WALKTHROUGH = ROOT / "docs/reviewer-walkthrough.md"
DOC = ROOT / "docs/232-v06156-reviewer-walkthrough-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0226-add-v06156-reviewer-walkthrough-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0225-add-v06156-reviewer-walkthrough-review-and-decision.md"
V06155_DOC = ROOT / "docs/231-v06155-reviewer-walkthrough-candidate.md"
V06154_DOC = ROOT / "docs/230-v06154-next-work-selection-using-risk-tiered-granularity.md"
V06153_DOC = ROOT / "docs/229-v06153-control-matrix-review-and-decision.md"
V06152_DOC = ROOT / "docs/228-v06152-control-matrix-candidate.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 2 of 2 for a Medium-risk reviewer-facing documentation work item.', 'This checkpoint reviews and accepts the Reviewer Walkthrough candidate from v0.6.155.', 'The Reviewer Walkthrough work item is closed.', 'Review conclusion', 'Candidate accepted', 'Reader and purpose confirmed', 'Non-authorizing notice confirmed', 'Suggested reading sequence confirmed', 'First-pass review path confirmed', 'Technical due-diligence review path confirmed', 'PoC-boundary review path confirmed', 'Control Matrix review path confirmed', 'Evidence and test-family inspection path confirmed', 'Claim-boundary inspection path confirmed', 'Questions before asking for a PoC confirmed', 'Reviewer outputs confirmed', 'Interpretation limits confirmed', 'Explicit non-goals confirmed', 'Claim boundaries confirmed', 'Reviewed walkthrough sections', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.157 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_WALKTHROUGH_PHRASES = ['# Reviewer Walkthrough', 'Reader', 'Purpose', 'Non-authorizing notice', 'Suggested reading sequence', 'First-pass review path', 'Technical due-diligence review path', 'PoC-boundary review path', 'Control Matrix review path', 'Evidence and test-family inspection path', 'Claim-boundary inspection path', 'Questions before asking for a PoC', 'Reviewer outputs', 'Interpretation limits', 'Explicit non-goals', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'This walkthrough does not authorize a PoC.', 'This walkthrough does not approve runtime execution.', 'This walkthrough does not approve scanner execution.', 'This walkthrough does not grant permission to test any system.', 'This walkthrough does not create a commercial contract.', 'This walkthrough does not approve customer delivery.']
FORBIDDEN_AFFIRMATIVE_PHRASES = ['customer poc is authorized', 'commercial contract is created', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'authorized for third-party testing by this walkthrough', 'permission to test third-party systems is granted', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'audit sufficiency achieved', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'complete vulnerability assessment capability is provided', 'equivalent to nist', 'equivalent to iso', 'safe to run without gates', 'ai can safely run tools without gates', 'aaef core promotion = true', 'aaef profile promotion = true', 'aaef practical package promotion = true']
FLAGS = ['reviewer_walkthrough_review_decision_completed = true', 'reviewer_walkthrough_review_decision_is_medium_risk = true', 'reviewer_walkthrough_review_decision_checkpoint_2_of_2 = true', 'reviewer_walkthrough_candidate_reviewed = true', 'reviewer_walkthrough_candidate_accepted = true', 'reviewer_walkthrough_work_item_closed = true', 'reviewer_walkthrough_file_reviewed = true', 'reviewer_walkthrough_reader_confirmed = true', 'reviewer_walkthrough_non_authorizing_notice_confirmed = true', 'reviewer_walkthrough_suggested_reading_sequence_confirmed = true', 'reviewer_walkthrough_first_pass_review_path_confirmed = true', 'reviewer_walkthrough_technical_due_diligence_path_confirmed = true', 'reviewer_walkthrough_poc_boundary_review_path_confirmed = true', 'reviewer_walkthrough_control_matrix_review_path_confirmed = true', 'reviewer_walkthrough_evidence_test_family_path_confirmed = true', 'reviewer_walkthrough_claim_boundary_inspection_path_confirmed = true', 'reviewer_walkthrough_questions_before_poc_confirmed = true', 'reviewer_walkthrough_reviewer_outputs_confirmed = true', 'reviewer_walkthrough_interpretation_limits_confirmed = true', 'reviewer_walkthrough_explicit_non_goals_confirmed = true', 'reviewer_walkthrough_claim_boundaries_confirmed = true', 'reviewer_walkthrough_reviewer_usefulness_confirmed = true', 'reviewer_walkthrough_created = true', 'reviewer_walkthrough_review_decision_completed = true', 'review_decision_completed = true', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.157 Next Work Selection Using Risk-Tiered Granularity']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [WALKTHROUGH, DOC, ADR, ISSUE, V06155_DOC, V06154_DOC, V06153_DOC, V06152_DOC, V06150_DOC, V06147_DOC, V06144_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    walkthrough_text = WALKTHROUGH.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_WALKTHROUGH_PHRASES:
        require(phrase in walkthrough_text, f"Reviewer Walkthrough missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.156 document missing required text: {phrase}")

    for phrase in [
        "`README.md`",
        "`docs/enterprise-review-guide.md`",
        "`docs/technical-due-diligence-summary.md`",
        "`docs/safe-poc-boundary-template.md`",
        "`docs/control-matrix.md`",
        "The first-pass review should end with a list of open questions, not with approval to run anything.",
        "The reviewer should inspect test results as evidence of local boundary behavior, not as production readiness.",
        "A completed template should not be treated as permission. Separate written authorization would still be required.",
        "These tests support reviewability. They do not grant operational permission.",
        "These questions prepare a review conversation. They do not authorize testing.",
    ]:
        require(phrase in walkthrough_text, f"Reviewer Walkthrough missing reviewed safeguard/detail: {phrase}")

    combined_lower = (walkthrough_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06155 = V06155_DOC.read_text(encoding="utf-8")
    for phrase in [
        "reviewer_walkthrough_candidate_completed = true",
        "reviewer_walkthrough_candidate_checkpoint_1_of_2 = true",
        "reviewer_walkthrough_created = true",
        "reviewer_walkthrough_candidate_claim_safe = true",
        "reviewer_walkthrough_suggested_reading_sequence_included = true",
        "reviewer_walkthrough_first_pass_review_path_included = true",
        "reviewer_walkthrough_technical_due_diligence_path_included = true",
        "reviewer_walkthrough_poc_boundary_review_path_included = true",
        "reviewer_walkthrough_control_matrix_review_path_included = true",
        "reviewer_walkthrough_evidence_test_family_path_included = true",
        "reviewer_walkthrough_claim_boundary_inspection_path_included = true",
        "reviewer_walkthrough_questions_before_poc_included = true",
        "reviewer_walkthrough_claim_boundaries_included = true",
        "selected_next_checkpoint = v0.6.156 Reviewer Walkthrough Review and Decision",
        "customer_poc_authorized = false",
        "commercial_contract_created = false",
        "runtime_execution_authorized = false",
        "scanner_execution_authorized = false",
        "docker_execution_authorized = false",
        "credential_injection_permitted = false",
        "customer_target_authorized = false",
        "delivery_authorized = false",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06155, f"v0.6.155 candidate missing required phrase: {phrase}")

    v06154 = V06154_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = reviewer_walkthrough",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.155 Reviewer Walkthrough Candidate",
    ]:
        require(phrase in v06154, f"v0.6.154 selection missing required phrase: {phrase}")

    v06153 = V06153_DOC.read_text(encoding="utf-8")
    require("control_matrix_work_item_closed = true" in v06153, "v0.6.153 Control Matrix work item must remain closed")

    v06152 = V06152_DOC.read_text(encoding="utf-8")
    require("control_matrix_candidate_completed = true" in v06152, "v0.6.152 Control Matrix candidate must remain recorded")

    v06150 = V06150_DOC.read_text(encoding="utf-8")
    require("safe_poc_boundary_template_work_item_closed = true" in v06150, "v0.6.150 Safe PoC Boundary Template work item must remain closed")

    v06147 = V06147_DOC.read_text(encoding="utf-8")
    require("technical_due_diligence_summary_work_item_closed = true" in v06147, "v0.6.147 Technical Due Diligence Summary work item must remain closed")

    v06144 = V06144_DOC.read_text(encoding="utf-8")
    require("enterprise_review_guide_work_item_closed = true" in v06144, "v0.6.144 Enterprise Review Guide work item must remain closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "customer poc is authorized by this review",
        "commercial contract is created by this review",
        "runtime execution is authorized by this review",
        "scanner execution is authorized by this review",
        "credential injection is permitted by this review",
        "customer target is authorized by this review",
        "delivery is authorized by this review",
        "this review opens an aaef main issue",
        "this review submits to aaef main",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.156 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.156 Reviewer Walkthrough review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
