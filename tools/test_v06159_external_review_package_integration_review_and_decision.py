from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "docs/external-review-package.md"
DOC = ROOT / "docs/235-v06159-external-review-package-integration-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0229-add-v06159-external-review-package-integration-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0228-add-v06159-external-review-package-integration-review-and-decision.md"
V06158_DOC = ROOT / "docs/234-v06158-external-review-package-integration-candidate.md"
V06157_DOC = ROOT / "docs/233-v06157-next-work-selection-using-risk-tiered-granularity.md"
V06156_DOC = ROOT / "docs/232-v06156-reviewer-walkthrough-review-and-decision.md"
V06155_DOC = ROOT / "docs/231-v06155-reviewer-walkthrough-candidate.md"
V06153_DOC = ROOT / "docs/229-v06153-control-matrix-review-and-decision.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 2 of 2 for a Medium-risk external-review-facing documentation work item.', 'This checkpoint reviews and accepts the External Review Package Integration candidate from v0.6.158.', 'The External Review Package Integration work item is closed.', 'Review conclusion', 'Candidate accepted', 'Reader and purpose confirmed', 'Non-authorizing notice confirmed', 'Document inventory confirmed', 'Recommended entry points confirmed', 'Reviewer paths confirmed', 'Evidence and test-family index confirmed', 'Boundary and non-goal summary confirmed', 'Package-level claim-boundary summary confirmed', 'Questions this package can answer confirmed', 'Questions this package cannot answer confirmed', 'Safe PoC Boundary Template guidance confirmed', 'When not to request a PoC confirmed', 'Outside-public-package boundary confirmed', 'Explicit non-goals confirmed', 'Claim boundaries confirmed', 'Reviewed package sections', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.160 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_PACKAGE_PHRASES = ['# External Review Package', 'Reader', 'Purpose', 'Non-authorizing notice', 'Document inventory', 'Recommended entry points', 'Reviewer paths', 'Evidence and test-family index', 'Boundary and non-goal summary', 'Package-level claim-boundary summary', 'Questions this package can answer', 'Questions this package cannot answer', 'When to use the Safe PoC Boundary Template', 'When not to request a PoC', 'What remains outside the public package', 'Explicit non-goals', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'This package does not authorize a PoC.', 'This package does not approve runtime execution.', 'This package does not approve scanner execution.', 'This package does not grant permission to test any system.', 'This package does not create a commercial contract.', 'This package does not approve customer delivery.']
FORBIDDEN_AFFIRMATIVE_PHRASES = ['customer poc is authorized', 'commercial contract is created', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'authorized for third-party testing by this package', 'permission to test third-party systems is granted', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'audit sufficiency achieved', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'complete vulnerability assessment capability is provided', 'equivalent to nist', 'equivalent to iso', 'safe to run without gates', 'ai can safely run tools without gates', 'aaef core promotion = true', 'aaef profile promotion = true', 'aaef practical package promotion = true']
FLAGS = ['external_review_package_integration_review_decision_completed = true', 'external_review_package_integration_review_decision_is_medium_risk = true', 'external_review_package_integration_review_decision_checkpoint_2_of_2 = true', 'external_review_package_candidate_reviewed = true', 'external_review_package_candidate_accepted = true', 'external_review_package_integration_work_item_closed = true', 'external_review_package_file_reviewed = true', 'external_review_package_reader_confirmed = true', 'external_review_package_purpose_confirmed = true', 'external_review_package_non_authorizing_notice_confirmed = true', 'external_review_package_document_inventory_confirmed = true', 'external_review_package_recommended_entry_points_confirmed = true', 'external_review_package_reviewer_paths_confirmed = true', 'external_review_package_evidence_test_family_index_confirmed = true', 'external_review_package_boundary_non_goal_summary_confirmed = true', 'external_review_package_claim_boundary_summary_confirmed = true', 'external_review_package_questions_can_answer_confirmed = true', 'external_review_package_questions_cannot_answer_confirmed = true', 'external_review_package_safe_poc_template_use_guidance_confirmed = true', 'external_review_package_when_not_to_request_poc_confirmed = true', 'external_review_package_outside_public_package_confirmed = true', 'external_review_package_explicit_non_goals_confirmed = true', 'external_review_package_claim_boundaries_confirmed = true', 'external_review_package_reviewer_usefulness_confirmed = true', 'external_review_package_created = true', 'external_review_package_review_decision_completed = true', 'review_decision_completed = true', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.160 Next Work Selection Using Risk-Tiered Granularity']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [PACKAGE, DOC, ADR, ISSUE, V06158_DOC, V06157_DOC, V06156_DOC, V06155_DOC, V06153_DOC, V06150_DOC, V06147_DOC, V06144_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    package_text = PACKAGE.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_PACKAGE_PHRASES:
        require(phrase in package_text, f"External Review Package missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.159 document missing required text: {phrase}")

    for phrase in [
        "`README.md`",
        "`docs/enterprise-review-guide.md`",
        "`docs/technical-due-diligence-summary.md`",
        "`docs/safe-poc-boundary-template.md`",
        "`docs/control-matrix.md`",
        "`docs/reviewer-walkthrough.md`",
        "These tests support reviewability. They do not grant operational permission.",
        "Do not use it as permission.",
        "Whether production readiness has been established.",
        "Those questions require separate authorization, legal/commercial review, technical review, or scope-specific evidence outside this public package.",
        "AAEF-AI-VA provides a public external-review package for navigating its safety-first documentation and evidence-boundary materials without authorizing real-world action.",
    ]:
        require(phrase in package_text, f"External Review Package missing reviewed safeguard/detail: {phrase}")

    combined_lower = (package_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06158 = V06158_DOC.read_text(encoding="utf-8")
    for phrase in [
        "external_review_package_integration_candidate_completed = true",
        "external_review_package_integration_candidate_checkpoint_1_of_2 = true",
        "external_review_package_created = true",
        "external_review_package_candidate_claim_safe = true",
        "external_review_package_document_inventory_included = true",
        "external_review_package_recommended_entry_points_included = true",
        "external_review_package_reviewer_paths_included = true",
        "external_review_package_evidence_test_family_index_included = true",
        "external_review_package_claim_boundary_summary_included = true",
        "external_review_package_questions_can_answer_included = true",
        "external_review_package_questions_cannot_answer_included = true",
        "external_review_package_safe_poc_template_use_guidance_included = true",
        "external_review_package_when_not_to_request_poc_included = true",
        "external_review_package_outside_public_package_included = true",
        "external_review_package_claim_boundary_summary_included = true",
        "selected_next_checkpoint = v0.6.159 External Review Package Integration Review and Decision",
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
        require(phrase in v06158, f"v0.6.158 candidate missing required phrase: {phrase}")

    v06157 = V06157_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = external_review_package_integration",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.158 External Review Package Integration Candidate",
    ]:
        require(phrase in v06157, f"v0.6.157 selection missing required phrase: {phrase}")

    require("reviewer_walkthrough_work_item_closed = true" in V06156_DOC.read_text(encoding="utf-8"), "v0.6.156 Reviewer Walkthrough work item must remain closed")
    require("reviewer_walkthrough_candidate_completed = true" in V06155_DOC.read_text(encoding="utf-8"), "v0.6.155 Reviewer Walkthrough candidate must remain recorded")
    require("control_matrix_work_item_closed = true" in V06153_DOC.read_text(encoding="utf-8"), "v0.6.153 Control Matrix work item must remain closed")
    require("safe_poc_boundary_template_work_item_closed = true" in V06150_DOC.read_text(encoding="utf-8"), "v0.6.150 Safe PoC Boundary Template work item must remain closed")
    require("technical_due_diligence_summary_work_item_closed = true" in V06147_DOC.read_text(encoding="utf-8"), "v0.6.147 Technical Due Diligence Summary work item must remain closed")
    require("enterprise_review_guide_work_item_closed = true" in V06144_DOC.read_text(encoding="utf-8"), "v0.6.144 Enterprise Review Guide work item must remain closed")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.159 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.159 External Review Package Integration review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
