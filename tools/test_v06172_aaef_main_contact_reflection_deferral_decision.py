from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
ADR = ROOT / "planning/decisions/ADR-0242-add-v06172-aaef-main-contact-reflection-deferral-decision.md"
ISSUE = ROOT / "planning/issues/0241-add-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06171_DOC = ROOT / "docs/247-v06171-next-work-selection-using-risk-tiered-granularity.md"
V06170_DOC = ROOT / "docs/246-v06170-public-entry-and-inquiry-route-consistency-review-review-and-decision.md"
V06167_DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"
README = ROOT / "README.md"
COMMERCIAL_BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"

ADDRESS = "hexroot0010@gmail.com"
REQUIRED = ['Status: decision', 'This checkpoint records a maintainer clarification after v0.6.171.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'AAEF main should not publish `hexroot0010@gmail.com` in README or other public docs for now.', 'AAEF-AI-VA may continue treating `hexroot0010@gmail.com` as the interim maintainer-provided inquiry route.', 'For AAEF main, the address is retained only as an internal future candidate.', 'A dedicated email or domain is preferred before AAEF main public publication.', 'Any AAEF main publication requires a separate explicit maintainer decision.', 'No AAEF main repository modification occurs.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'The v0.6.119 AAEF main handback sequence remains paused.', 'Decision record', 'Reasoning', 'Deferral decision', 'AAEF-AI-VA interpretation', 'AAEF main interpretation', 'Future publication minimum wording', 'What did not happen', 'Next direction']
FLAGS = ['aaef_main_contact_reflection_deferral_decision_completed = true', 'aaef_main_contact_reflection_deferral_decision_is_low_risk = true', 'aaef_main_contact_reflection_deferral_decision_one_checkpoint = true', 'v06172_completed_as_low_risk_one_checkpoint = true', 'maintainer_clarification_received_after_v06171 = true', 'v06171_selected_proposal_work_not_started = true', 'aaef_team_inquiry_address_reflection_proposal_created = false', 'aaef_team_inquiry_address_reflection_proposal_sent = false', 'aaef_team_inquiry_address_reflection_proposal_submitted_to_aaef_main = false', 'aaef_main_contact_reflection_deferred = true', 'aaef_main_readme_contact_publication_deferred = true', 'aaef_main_public_docs_contact_publication_deferred = true', 'aaef_main_future_candidate_address_retained_internally = true', 'aaef_main_future_candidate_address = hexroot0010@gmail.com', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'dedicated_email_or_domain_preferred_before_aaef_main_publication = true', 'explicit_aaef_main_maintainer_decision_required_before_publication = true', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.173 Next Work Selection Using Risk-Tiered Granularity']
FORBIDDEN_DOC_PHRASES = ['aaef main should publish `hexroot0010@gmail.com` now', 'aaef main readme contact publication completed = true', 'aaef main contact publication modified = true', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'aaef team inquiry address reflection proposal created = true', 'aaef team inquiry address reflection proposal sent = true', 'aaef main issue opened = true', 'aaef main pull request opened = true', 'runtime execution is authorized by this checkpoint', 'scanner execution is authorized by this checkpoint', 'credential injection is permitted by this checkpoint', 'customer target is authorized by this checkpoint', 'delivery is authorized by this checkpoint', 'commercial contract is created by this checkpoint', 'customer poc is authorized by this checkpoint', 'certification claim is made', 'legal compliance claim is made', 'audit opinion claim is made', 'production readiness claim is made', 'external-framework equivalence claim is made']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06171_DOC, V06170_DOC, V06167_DOC, V06119_DOC, README, COMMERCIAL_BOUNDARY]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.172 document missing required text: {phrase}")

    v06171 = V06171_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = aaef_team_inquiry_address_reflection_proposal",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_checkpoint = v0.6.172 AAEF Team Inquiry Address Reflection Proposal Candidate",
        "aaef_team_proposal_created = false",
        "aaef_main_repository_modified = false",
        "aaef_main_handback_sequence_reopened = false",
    ]:
        require(phrase in v06171, f"v0.6.171 selection missing required phrase: {phrase}")

    v06170 = V06170_DOC.read_text(encoding="utf-8")
    require("public_entry_and_inquiry_route_consistency_review_work_item_closed = true" in v06170, "v0.6.170 route consistency work item must remain closed")
    require("selected_next_checkpoint = v0.6.171 Next Work Selection Using Risk-Tiered Granularity" in v06170, "v0.6.170 must point to v0.6.171 next selection")

    v06167 = V06167_DOC.read_text(encoding="utf-8")
    require("maintainer_inquiry_address_publication_work_item_closed = true" in v06167, "v0.6.167 contact publication work item must remain closed")
    require("maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com" in v06167, "v0.6.167 must record accepted inquiry address")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in ["aaef_main_handback_sequence_paused = true", "aaef_main_issue_opened = false", "aaef_main_pull_request_opened = false"]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    require(ADDRESS in README.read_text(encoding="utf-8"), "README must retain AAEF-AI-VA interim inquiry address")
    require(ADDRESS in COMMERCIAL_BOUNDARY.read_text(encoding="utf-8"), "commercial boundary must retain AAEF-AI-VA interim inquiry address")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN_DOC_PHRASES:
        require(phrase not in lower_doc, f"v0.6.172 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.172 AAEF Main Contact Reflection Deferral Decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
