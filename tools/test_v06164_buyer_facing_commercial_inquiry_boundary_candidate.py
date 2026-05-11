from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"
DOC = ROOT / "docs/240-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0234-add-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md"
ISSUE = ROOT / "planning/issues/0233-add-v06164-buyer-facing-commercial-inquiry-boundary-candidate.md"
V06163_DOC = ROOT / "docs/239-v06163-next-work-selection-using-risk-tiered-granularity.md"
V06162_DOC = ROOT / "docs/238-v06162-public-review-entry-point-polish-review-and-decision.md"
V06159_DOC = ROOT / "docs/235-v06159-external-review-package-integration-review-and-decision.md"
V06156_DOC = ROOT / "docs/232-v06156-reviewer-walkthrough-review-and-decision.md"
V06153_DOC = ROOT / "docs/229-v06153-control-matrix-review-and-decision.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_BOUNDARY_PHRASES = ['# Buyer-Facing Commercial Inquiry Boundary', 'Reader', 'Purpose', 'Contact channel', 'Email-based inquiry is the selected contact model.', 'The public repository does not commit an email address in this candidate.', 'Use the maintainer-provided email address when it is published or otherwise provided by the maintainer.', 'Allowed commercial inquiry topics', 'Topics requiring separate agreement', 'Inquiry is not a contract', 'Inquiry does not approve a paid engagement', 'Inquiry does not authorize customer PoC activity', 'Inquiry does not authorize runtime or scanner execution', 'Inquiry does not authorize credential use, customer target use, or delivery', 'Relationship to the External Review Package', 'Relationship to the Safe PoC Boundary Template', 'Relationship to licensing and commercial-use boundaries', 'Public/private material boundary', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'Commercial inquiry is not action authority.', 'Commercial inquiry is not PoC approval.', 'Commercial inquiry is not runtime approval.', 'Commercial inquiry is not scanner approval.', 'Commercial inquiry is not delivery approval.']
REQUIRED_README_PHRASES = ['## Commercial Inquiry Boundary', 'Commercial inquiry is welcome as a boundary discussion, but inquiry is not authorization.', 'Email-based inquiry is the selected contact model.', 'This repository does not commit an email address in this candidate.', 'Use the maintainer-provided email address when it is published or otherwise provided by the maintainer.', '`docs/buyer-facing-commercial-inquiry-boundary.md`', 'Commercial inquiry is not a contract.', 'Commercial inquiry is not PoC approval.', 'Commercial inquiry is not runtime approval.', 'Commercial inquiry is not scanner approval.', 'Commercial inquiry is not delivery approval.', 'Customer PoC, paid engagement, commercial license terms, runtime/scanner execution, credential use, customer targets, and delivery require separate written authorization or agreement.']
REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk buyer-facing documentation work item.', 'This checkpoint creates the Buyer-Facing Commercial Inquiry Boundary candidate.', 'The review and decision are deferred to v0.6.165.', 'Candidate implementation summary', 'Commercial inquiry boundary artifact', 'README commercial inquiry entry', 'Commercial inquiry contact model', 'Boundary scope', 'Claim boundaries', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision']
FLAGS = ['buyer_facing_commercial_inquiry_boundary_candidate_completed = true', 'buyer_facing_commercial_inquiry_boundary_candidate_is_medium_risk = true', 'buyer_facing_commercial_inquiry_boundary_candidate_checkpoint_1_of_2 = true', 'buyer_facing_commercial_inquiry_boundary_review_decision_deferred_to_v06165 = true', 'buyer_facing_commercial_inquiry_boundary_created = true', 'buyer_facing_commercial_inquiry_boundary_candidate_claim_safe = true', 'buyer_facing_commercial_inquiry_boundary_email_based_contact_selected = true', 'buyer_facing_commercial_inquiry_email_address_not_specified = true', 'buyer_facing_commercial_inquiry_uses_maintainer_provided_email = true', 'buyer_facing_commercial_inquiry_boundary_allowed_topics_included = true', 'buyer_facing_commercial_inquiry_boundary_topics_requiring_separate_agreement_included = true', 'buyer_facing_commercial_inquiry_boundary_not_contract_notice_included = true', 'buyer_facing_commercial_inquiry_boundary_no_paid_engagement_approval_included = true', 'buyer_facing_commercial_inquiry_boundary_no_customer_poc_authorization_included = true', 'buyer_facing_commercial_inquiry_boundary_no_runtime_scanner_authorization_included = true', 'buyer_facing_commercial_inquiry_boundary_no_credential_customer_delivery_authorization_included = true', 'buyer_facing_commercial_inquiry_boundary_relationship_to_external_review_package_included = true', 'buyer_facing_commercial_inquiry_boundary_relationship_to_safe_poc_template_included = true', 'buyer_facing_commercial_inquiry_boundary_license_commercial_use_boundary_included = true', 'buyer_facing_commercial_inquiry_boundary_public_private_material_boundary_included = true', 'buyer_facing_commercial_inquiry_boundary_claim_boundaries_included = true', 'readme_commercial_inquiry_entry_modified = true', 'commercial_inquiry_contact_channel_is_email = true', 'commercial_inquiry_email_address_placeholder_used = false', 'commercial_inquiry_email_address_committed = false', 'commercial_inquiry_boundary_review_decision_completed = false', 'review_decision_completed = false', 'public_review_entry_point_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.165 Buyer-Facing Commercial Inquiry Boundary Review and Decision']

FORBIDDEN_AFFIRMATIVE_PHRASES = [
    "customer poc is authorized",
    "commercial contract is created",
    "commercial license terms are created",
    "paid engagement is approved",
    "runtime execution is authorized",
    "scanner execution is authorized",
    "docker execution is authorized",
    "credential injection is permitted",
    "customer target is authorized",
    "delivery is authorized",
    "authorized to test third-party systems",
    "permission to test third-party systems is granted",
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
    for path in [README, BOUNDARY, DOC, ADR, ISSUE, V06163_DOC, V06162_DOC, V06159_DOC, V06156_DOC, V06153_DOC, V06150_DOC, V06147_DOC, V06144_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    readme_text = README.read_text(encoding="utf-8")
    boundary_text = BOUNDARY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_BOUNDARY_PHRASES:
        require(phrase in boundary_text, f"commercial inquiry boundary missing required text: {phrase}")

    for phrase in REQUIRED_README_PHRASES:
        require(phrase in readme_text, f"README missing required commercial inquiry text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.164 document missing required text: {phrase}")

    combined_lower = (readme_text + "\n" + boundary_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    for forbidden_contact in [
        "commercial-inquiry@example",
        "example.com",
        "sales@example",
        "contact@example",
        "mailto:",
    ]:
        require(forbidden_contact not in combined_lower, f"placeholder or mailto contact must not be committed: {forbidden_contact}")

    v06163 = V06163_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = buyer_facing_commercial_inquiry_boundary",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate",
        "buyer_facing_commercial_inquiry_boundary_created = false",
        "commercial_license_terms_created = false",
        "paid_engagement_approved = false",
        "customer_poc_authorized = false",
        "commercial_contract_created = false",
        "customer_specific_material_created = false",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06163, f"v0.6.163 selection missing required phrase: {phrase}")

    require("public_review_entry_point_polish_work_item_closed = true" in V06162_DOC.read_text(encoding="utf-8"), "v0.6.162 Public Review Entry Point work item must remain closed")
    require("external_review_package_integration_work_item_closed = true" in V06159_DOC.read_text(encoding="utf-8"), "v0.6.159 External Review Package work item must remain closed")
    require("reviewer_walkthrough_work_item_closed = true" in V06156_DOC.read_text(encoding="utf-8"), "v0.6.156 Reviewer Walkthrough work item must remain closed")
    require("control_matrix_work_item_closed = true" in V06153_DOC.read_text(encoding="utf-8"), "v0.6.153 Control Matrix work item must remain closed")
    require("safe_poc_boundary_template_work_item_closed = true" in V06150_DOC.read_text(encoding="utf-8"), "v0.6.150 Safe PoC Boundary Template work item must remain closed")
    require("technical_due_diligence_summary_work_item_closed = true" in V06147_DOC.read_text(encoding="utf-8"), "v0.6.147 Technical Due Diligence Summary work item must remain closed")
    require("enterprise_review_guide_work_item_closed = true" in V06144_DOC.read_text(encoding="utf-8"), "v0.6.144 Enterprise Review Guide work item must remain closed")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "customer poc is authorized by this candidate",
        "commercial contract is created by this candidate",
        "commercial license terms are created by this candidate",
        "paid engagement is approved by this candidate",
        "runtime execution is authorized by this candidate",
        "scanner execution is authorized by this candidate",
        "credential injection is permitted by this candidate",
        "customer target is authorized by this candidate",
        "delivery is authorized by this candidate",
        "this candidate opens an aaef main issue",
        "this candidate submits to aaef main",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.164 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.164 Buyer-Facing Commercial Inquiry Boundary candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
