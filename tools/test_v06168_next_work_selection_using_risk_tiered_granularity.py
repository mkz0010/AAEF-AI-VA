from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/244-v06168-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0238-add-v06168-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0237-add-v06168-next-work-selection-using-risk-tiered-granularity.md"
V06167_DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06166_DOC = ROOT / "docs/242-v06166-maintainer-inquiry-address-publication-candidate.md"
V06165_DOC = ROOT / "docs/241-v06165-buyer-facing-commercial-inquiry-boundary-review-and-decision.md"
V06162_DOC = ROOT / "docs/238-v06162-public-review-entry-point-polish-review-and-decision.md"
V06159_DOC = ROOT / "docs/235-v06159-external-review-package-integration-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"
README = ROOT / "README.md"
BOUNDARY = ROOT / "docs/buyer-facing-commercial-inquiry-boundary.md"

ADDRESS = 'hexroot0010@gmail.com'
REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Public Entry and Inquiry Route Consistency Review.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate.', 'This checkpoint does not create the public entry and inquiry route consistency review.', 'This checkpoint does not modify README public entry language.', 'This checkpoint does not modify commercial inquiry language.', 'This checkpoint does not modify the inquiry address publication.', 'This checkpoint does not reopen the AAEF main handback sequence.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Public Entry and Inquiry Route Consistency Review scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06168_completed = true', 'next_work_selection_v06168_is_documentation_only = true', 'next_work_selection_v06168_uses_v06120_granularity_policy = true', 'next_work_selection_v06168_uses_v06167_completed_work_item = true', 'v06168_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = public_entry_and_inquiry_route_consistency_review', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.169 Public Entry and Inquiry Route Consistency Review Candidate', 'selected_followup_checkpoint = v0.6.170 Public Entry and Inquiry Route Consistency Review Review and Decision', 'public_entry_and_inquiry_route_consistency_review_selected = true', 'maintainer_inquiry_address_publication_work_item_closed = true', 'buyer_facing_commercial_inquiry_boundary_work_item_closed = true', 'public_review_entry_point_polish_work_item_closed = true', 'external_review_package_integration_work_item_closed = true', 'reviewer_walkthrough_work_item_closed = true', 'control_matrix_work_item_closed = true', 'safe_poc_boundary_template_work_item_closed = true', 'technical_due_diligence_summary_work_item_closed = true', 'enterprise_review_guide_work_item_closed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'public_entry_and_inquiry_route_consistency_review_created = false', 'public_entry_and_inquiry_route_consistency_review_modified = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'public_review_entry_point_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN_DOC_PHRASES = ['this checkpoint creates the public entry and inquiry route consistency review', 'this checkpoint modifies readme public entry language', 'this checkpoint modifies commercial inquiry language', 'this checkpoint modifies the inquiry address publication', 'this checkpoint opens an aaef main issue', 'this checkpoint submits to aaef main', 'runtime execution is authorized by this checkpoint', 'scanner execution is authorized by this checkpoint', 'credential injection is permitted by this checkpoint', 'customer target is authorized by this checkpoint', 'delivery is authorized by this checkpoint', 'commercial contract is created by this checkpoint', 'customer poc is authorized by this checkpoint', 'certification claim is made', 'legal compliance claim is made', 'audit opinion claim is made', 'production readiness claim is made', 'external-framework equivalence claim is made']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06167_DOC, V06166_DOC, V06165_DOC, V06162_DOC, V06159_DOC, V06120_DOC, V06119_DOC, README, BOUNDARY]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.168 document missing required text: {phrase}")

    v06167 = V06167_DOC.read_text(encoding="utf-8")
    for phrase in [
        "maintainer_inquiry_address_publication_review_decision_completed = true",
        "maintainer_inquiry_address_publication_candidate_accepted = true",
        "maintainer_inquiry_address_publication_work_item_closed = true",
        "maintainer_approved_interim_aaef_wide_inquiry_address = hexroot0010@gmail.com",
        "selected_next_checkpoint = v0.6.168 Next Work Selection Using Risk-Tiered Granularity",
        "customer_poc_authorized = false",
        "commercial_contract_created = false",
        "paid_engagement_approved = false",
        "commercial_license_terms_created = false",
        "runtime_execution_authorized = false",
        "scanner_execution_authorized = false",
        "delivery_authorized = false",
    ]:
        require(phrase in v06167, f"v0.6.167 baseline missing required phrase: {phrase}")

    require(ADDRESS in README.read_text(encoding="utf-8"), "README must retain accepted maintainer inquiry address")
    require(ADDRESS in BOUNDARY.read_text(encoding="utf-8"), "commercial inquiry boundary must retain accepted maintainer inquiry address")
    require("maintainer_inquiry_address_publication_candidate_completed = true" in V06166_DOC.read_text(encoding="utf-8"), "v0.6.166 contact publication candidate must remain recorded")
    require("buyer_facing_commercial_inquiry_boundary_work_item_closed = true" in V06165_DOC.read_text(encoding="utf-8"), "v0.6.165 commercial inquiry boundary work item must remain closed")
    require("public_review_entry_point_polish_work_item_closed = true" in V06162_DOC.read_text(encoding="utf-8"), "v0.6.162 public review entry work item must remain closed")
    require("external_review_package_integration_work_item_closed = true" in V06159_DOC.read_text(encoding="utf-8"), "v0.6.159 external review package work item must remain closed")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    for phrase in ["risk_tiered_granularity_adopted = true", "Low risk", "Medium risk", "High risk", "Critical risk"]:
        require(phrase in v06120, f"v0.6.120 policy missing required phrase: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in ["aaef_main_handback_sequence_paused = true", "aaef_main_issue_opened = false", "aaef_main_pull_request_opened = false"]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN_DOC_PHRASES:
        require(phrase not in lower_doc, f"v0.6.168 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.168 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
