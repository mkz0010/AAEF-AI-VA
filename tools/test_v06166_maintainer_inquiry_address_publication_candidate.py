from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"
DOC = ROOT / "docs/242-v06166-maintainer-inquiry-address-publication-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0236-add-v06166-maintainer-inquiry-address-publication-candidate.md"
ISSUE = ROOT / "planning/issues/0235-add-v06166-maintainer-inquiry-address-publication-candidate.md"
V06165_DOC = ROOT / "docs/241-v06165-buyer-facing-commercial-inquiry-boundary-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

ADDRESS = 'hexroot0010@gmail.com'
FLAGS = ['maintainer_inquiry_address_publication_candidate_completed = true', 'maintainer_inquiry_address_publication_candidate_is_medium_risk = true', 'maintainer_inquiry_address_publication_candidate_checkpoint_1_of_2 = true', 'maintainer_inquiry_address_publication_review_decision_deferred_to_v06167 = true', 'maintainer_approved_interim_aaef_wide_inquiry_address_published = true', 'maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com', 'inquiry_address_publication_is_email_based = true', 'inquiry_address_publication_is_aaef_wide = true', 'readme_inquiry_address_published = true', 'buyer_facing_commercial_inquiry_boundary_address_published = true', 'contact_publication_is_not_contract = true', 'contact_publication_is_not_customer_poc_approval = true', 'contact_publication_is_not_paid_engagement_approval = true', 'contact_publication_is_not_runtime_authorization = true', 'contact_publication_is_not_scanner_authorization = true', 'contact_publication_is_not_delivery_authorization = true', 'maintainer_inquiry_address_publication_review_decision_completed = false', 'review_decision_completed = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.167 Maintainer Inquiry Address Publication Review and Decision']
FORBIDDEN = ['customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'audit sufficiency achieved', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'complete vulnerability assessment capability is provided', 'equivalent to nist', 'equivalent to iso', 'safe to run without gates', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [README, BOUNDARY, DOC, ADR, ISSUE, V06165_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    readme_text = README.read_text(encoding="utf-8")
    boundary_text = BOUNDARY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for text, label in [(readme_text, "README"), (boundary_text, "commercial inquiry boundary"), (doc_text, "v0.6.166 candidate")]:
        require(ADDRESS in text, f"{label} must contain the maintainer-approved interim inquiry address")

    for phrase in [
        "The maintainer-approved interim AAEF-wide inquiry address is `hexroot0010@gmail.com`.",
        "For buyer-facing or commercial inquiry, contact `hexroot0010@gmail.com`.",
        "Commercial inquiry is not a contract.",
        "Commercial inquiry is not PoC approval.",
        "Commercial inquiry is not runtime approval.",
        "Commercial inquiry is not scanner approval.",
        "Commercial inquiry is not delivery approval.",
    ]:
        require(phrase in readme_text, f"README missing required publication phrase: {phrase}")

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
        require(phrase in boundary_text, f"commercial inquiry boundary missing required publication phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.166 candidate missing flag: {phrase}")

    require("mailto:" not in readme_text.lower(), "README should publish address as text, not mailto")
    require("mailto:" not in boundary_text.lower(), "commercial inquiry boundary should publish address as text, not mailto")

    combined_lower = (readme_text + "\n" + boundary_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06165 = V06165_DOC.read_text(encoding="utf-8")
    for phrase in [
        "buyer_facing_commercial_inquiry_boundary_review_decision_completed = true",
        "email_based_inquiry_model_accepted = true",
        "maintainer_provided_inquiry_address_model_accepted = true",
        "actual_inquiry_address_publication_deferred = true",
        "selected_next_checkpoint = v0.6.166 Maintainer Inquiry Address Publication Candidate",
    ]:
        require(phrase in v06165, f"v0.6.165 review/decision missing required phrase: {phrase}")

    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    print("v0.6.166 Maintainer Inquiry Address Publication candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
