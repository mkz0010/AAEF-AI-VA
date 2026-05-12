from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"
DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0237-add-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0236-add-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06166_DOC = ROOT / "docs/242-v06166-maintainer-inquiry-address-publication-candidate.md"
V06165_DOC = ROOT / "docs/241-v06165-buyer-facing-commercial-inquiry-boundary-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

ADDRESS = 'hexroot0010@gmail.com'
FLAGS = ['maintainer_inquiry_address_publication_review_decision_completed = true', 'maintainer_inquiry_address_publication_review_decision_is_medium_risk = true', 'maintainer_inquiry_address_publication_review_decision_checkpoint_2_of_2 = true', 'maintainer_inquiry_address_publication_candidate_reviewed = true', 'maintainer_inquiry_address_publication_candidate_accepted = true', 'maintainer_inquiry_address_publication_work_item_closed = true', 'maintainer_approved_interim_aaef_wide_inquiry_address_reviewed = true', 'maintainer_approved_interim_aaef_wide_inquiry_address_accepted = true', 'maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com', 'readme_inquiry_address_publication_accepted = true', 'buyer_facing_commercial_inquiry_boundary_address_publication_accepted = true', 'inquiry_route_only_interpretation_confirmed = true', 'aaef_wide_inquiry_framing_confirmed = true', 'aaef_ai_va_commercial_inquiry_framing_confirmed = true', 'contact_publication_not_contract_confirmed = true', 'contact_publication_not_customer_poc_approval_confirmed = true', 'contact_publication_not_paid_engagement_approval_confirmed = true', 'contact_publication_not_runtime_authorization_confirmed = true', 'contact_publication_not_scanner_authorization_confirmed = true', 'contact_publication_not_delivery_authorization_confirmed = true', 'contact_publication_claim_boundaries_confirmed = true', 'review_decision_completed = true', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.168 Next Work Selection Using Risk-Tiered Granularity']
FORBIDDEN = ['customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [README, BOUNDARY, DOC, ADR, ISSUE, V06166_DOC, V06165_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    readme_text = README.read_text(encoding="utf-8")
    boundary_text = BOUNDARY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    require(ADDRESS in readme_text, "README must publish the accepted maintainer inquiry address")
    require(ADDRESS in boundary_text, "commercial inquiry boundary must publish the accepted maintainer inquiry address")
    require(ADDRESS in doc_text, "v0.6.167 review/decision must include the accepted maintainer inquiry address")

    for phrase in [
        "The maintainer-approved interim AAEF-wide inquiry address is `hexroot0010@gmail.com`.",
        "For buyer-facing or commercial inquiry, contact `hexroot0010@gmail.com`.",
        "Commercial inquiry is not a contract.",
        "Commercial inquiry is not PoC approval.",
        "Commercial inquiry is not runtime approval.",
        "Commercial inquiry is not scanner approval.",
        "Commercial inquiry is not delivery approval.",
    ]:
        require(phrase in readme_text, f"README missing accepted inquiry boundary phrase: {phrase}")

    for phrase in [
        "The maintainer-approved interim AAEF-wide inquiry address is `hexroot0010@gmail.com`.",
        "For buyer-facing, commercial, framework review, research discussion, or general inquiry, contact `hexroot0010@gmail.com`.",
        "Publishing this address provides an inquiry route only.",
        "Commercial inquiry is not action authority.",
        "Commercial inquiry is not PoC approval.",
        "Commercial inquiry is not runtime approval.",
        "Commercial inquiry is not scanner approval.",
        "Commercial inquiry is not delivery approval.",
    ]:
        require(phrase in boundary_text, f"commercial inquiry boundary missing accepted inquiry boundary phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.167 document missing flag: {phrase}")

    combined_lower = (readme_text + "\n" + boundary_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06166 = V06166_DOC.read_text(encoding="utf-8")
    for phrase in [
        "maintainer_inquiry_address_publication_candidate_completed = true",
        "maintainer_approved_interim_aaef_wide_inquiry_address_published = true",
        "maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com",
        "readme_inquiry_address_published = true",
        "buyer_facing_commercial_inquiry_boundary_address_published = true",
        "selected_next_checkpoint = v0.6.167 Maintainer Inquiry Address Publication Review and Decision",
    ]:
        require(phrase in v06166, f"v0.6.166 candidate missing required phrase: {phrase}")

    require("actual_inquiry_address_publication_deferred = true" in V06165_DOC.read_text(encoding="utf-8"), "v0.6.165 must have deferred actual address publication")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    print("v0.6.167 Maintainer Inquiry Address Publication review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
