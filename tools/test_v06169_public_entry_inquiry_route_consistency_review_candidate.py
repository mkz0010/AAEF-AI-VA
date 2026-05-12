from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
REVIEW = ROOT / "docs/public-entry-and-inquiry-route-consistency-review.md"
DOC = ROOT / "docs/245-v06169-public-entry-and-inquiry-route-consistency-review-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0239-add-v06169-public-entry-and-inquiry-route-consistency-review-candidate.md"
ISSUE = ROOT / "planning/issues/0238-add-v06169-public-entry-and-inquiry-route-consistency-review-candidate.md"
EXTERNAL_REVIEW_PACKAGE = ROOT / "docs/external-review-package.md"
COMMERCIAL_BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"
REVIEWER_WALKTHROUGH = ROOT / "docs/reviewer-walkthrough.md"
CONTROL_MATRIX = ROOT / "docs/control-matrix.md"
TDD_SUMMARY = ROOT / "docs/technical-due-diligence-summary.md"
ENTERPRISE_GUIDE = ROOT / "docs/enterprise-review-guide.md"
SAFE_POC_TEMPLATE = ROOT / "docs/safe-poc-boundary-template.md"
V06168_DOC = ROOT / "docs/244-v06168-next-work-selection-using-risk-tiered-granularity.md"
V06167_DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

ADDRESS = 'hexroot0010@gmail.com'
FLAGS = ['public_entry_and_inquiry_route_consistency_review_candidate_completed = true', 'public_entry_and_inquiry_route_consistency_review_candidate_is_medium_risk = true', 'public_entry_and_inquiry_route_consistency_review_candidate_checkpoint_1_of_2 = true', 'public_entry_and_inquiry_route_consistency_review_decision_deferred_to_v06170 = true', 'public_entry_and_inquiry_route_consistency_review_created = true', 'public_entry_and_inquiry_route_consistency_review_claim_safe = true', 'readme_public_review_entry_point_checked = true', 'readme_commercial_inquiry_boundary_checked = true', 'external_review_package_entry_route_checked = true', 'buyer_facing_commercial_inquiry_boundary_checked = true', 'maintainer_inquiry_address_publication_checked = true', 'reviewer_walkthrough_route_checked = true', 'control_matrix_route_checked = true', 'technical_due_diligence_summary_route_checked = true', 'enterprise_review_guide_route_checked = true', 'safe_poc_boundary_template_route_checked = true', 'public_review_route_consistency_candidate_result = pass_with_review_notes', 'commercial_inquiry_route_consistency_candidate_result = pass_with_review_notes', 'contact_publication_consistency_candidate_result = pass_with_review_notes', 'inquiry_route_only_interpretation_candidate_result = pass', 'non_authorizing_language_candidate_result = pass', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'public_entry_and_inquiry_route_consistency_review_review_decision_completed = false', 'review_decision_completed = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.170 Public Entry and Inquiry Route Consistency Review Review and Decision']
FORBIDDEN = ['customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    required_paths = [
        README, REVIEW, DOC, ADR, ISSUE, EXTERNAL_REVIEW_PACKAGE, COMMERCIAL_BOUNDARY,
        REVIEWER_WALKTHROUGH, CONTROL_MATRIX, TDD_SUMMARY, ENTERPRISE_GUIDE,
        SAFE_POC_TEMPLATE, V06168_DOC, V06167_DOC, V06119_DOC,
    ]
    for path in required_paths:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    readme_text = README.read_text(encoding="utf-8")
    review_text = REVIEW.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")
    commercial_text = COMMERCIAL_BOUNDARY.read_text(encoding="utf-8")

    for phrase in [
        "## Public Review Entry Point",
        "## Commercial Inquiry Boundary",
        "For external review, start with `docs/external-review-package.md`.",
        "Commercial inquiry is welcome as a boundary discussion, but inquiry is not authorization.",
        ADDRESS,
    ]:
        require(phrase in readme_text, f"README missing expected public/inquiry route phrase: {phrase}")

    for phrase in [
        "# Public Entry and Inquiry Route Consistency Review",
        "public_review_route_consistency_candidate_result = pass_with_review_notes",
        "commercial_inquiry_route_consistency_candidate_result = pass_with_review_notes",
        "contact_publication_consistency_candidate_result = pass_with_review_notes",
        "inquiry_route_only_interpretation_candidate_result = pass",
        "non_authorizing_language_candidate_result = pass",
        ADDRESS,
        "v0.6.170 Public Entry and Inquiry Route Consistency Review Review and Decision",
    ]:
        require(phrase in review_text, f"consistency review missing expected phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.169 document missing flag: {phrase}")

    for phrase in [
        "Publishing this address provides an inquiry route only.",
        "Commercial inquiry is not action authority.",
        "Commercial inquiry is not PoC approval.",
        "Commercial inquiry is not runtime approval.",
        "Commercial inquiry is not scanner approval.",
        "Commercial inquiry is not delivery approval.",
        ADDRESS,
    ]:
        require(phrase in commercial_text, f"commercial inquiry boundary missing expected phrase: {phrase}")

    v06168 = V06168_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = public_entry_and_inquiry_route_consistency_review",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate",
    ]:
        require(phrase in v06168, f"v0.6.168 selection missing required phrase: {phrase}")

    v06167 = V06167_DOC.read_text(encoding="utf-8")
    for phrase in [
        "maintainer_inquiry_address_publication_work_item_closed = true",
        "maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com",
        "selected_next_checkpoint = v0.6.168 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06167, f"v0.6.167 baseline missing required phrase: {phrase}")

    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (readme_text + "\n" + review_text + "\n" + doc_text + "\n" + commercial_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.169 Public Entry and Inquiry Route Consistency Review candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
