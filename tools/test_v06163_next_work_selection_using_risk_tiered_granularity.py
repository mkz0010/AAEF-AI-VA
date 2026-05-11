from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/239-v06163-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0233-add-v06163-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0232-add-v06163-next-work-selection-using-risk-tiered-granularity.md"
V06162_DOC = ROOT / "docs/238-v06162-public-review-entry-point-polish-review-and-decision.md"
V06161_DOC = ROOT / "docs/237-v06161-public-review-entry-point-polish-candidate.md"
V06159_DOC = ROOT / "docs/235-v06159-external-review-package-integration-review-and-decision.md"
V06156_DOC = ROOT / "docs/232-v06156-reviewer-walkthrough-review-and-decision.md"
V06153_DOC = ROOT / "docs/229-v06153-control-matrix-review-and-decision.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Buyer-Facing Commercial Inquiry Boundary.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate.', 'This checkpoint does not create the buyer-facing commercial inquiry boundary.', 'This checkpoint does not create commercial license terms.', 'This checkpoint does not approve a paid engagement.', 'This checkpoint does not authorize a customer PoC.', 'This checkpoint does not modify runtime behavior.', 'This checkpoint does not reopen the AAEF main handback sequence.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Buyer-Facing Commercial Inquiry Boundary scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06163_completed = true', 'next_work_selection_v06163_is_documentation_only = true', 'next_work_selection_v06163_uses_v06120_granularity_policy = true', 'next_work_selection_v06163_uses_v06162_completed_work_item = true', 'v06163_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = buyer_facing_commercial_inquiry_boundary', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.164 Buyer-Facing Commercial Inquiry Boundary Candidate', 'buyer_facing_commercial_inquiry_boundary_selected = true', 'public_review_entry_point_polish_work_item_closed = true', 'external_review_package_integration_work_item_closed = true', 'reviewer_walkthrough_work_item_closed = true', 'control_matrix_work_item_closed = true', 'safe_poc_boundary_template_work_item_closed = true', 'technical_due_diligence_summary_work_item_closed = true', 'enterprise_review_guide_work_item_closed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'buyer_facing_commercial_inquiry_boundary_created = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'public_review_entry_point_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06162_DOC, V06161_DOC, V06159_DOC, V06156_DOC, V06153_DOC, V06150_DOC, V06147_DOC, V06144_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.163 document missing required text: {phrase}")

    v06162 = V06162_DOC.read_text(encoding="utf-8")
    for phrase in [
        "public_review_entry_point_polish_review_decision_completed = true",
        "public_review_entry_point_candidate_accepted = true",
        "public_review_entry_point_polish_work_item_closed = true",
        "selected_next_checkpoint = v0.6.163 Next Work Selection Using Risk-Tiered Granularity",
        "customer_poc_authorized = false",
        "commercial_contract_created = false",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06162, f"v0.6.162 baseline missing required phrase: {phrase}")

    require("public_review_entry_point_polish_candidate_completed = true" in V06161_DOC.read_text(encoding="utf-8"), "v0.6.161 Public Review Entry Point candidate must remain recorded")
    require("external_review_package_integration_work_item_closed = true" in V06159_DOC.read_text(encoding="utf-8"), "v0.6.159 External Review Package Integration work item must be closed")
    require("reviewer_walkthrough_work_item_closed = true" in V06156_DOC.read_text(encoding="utf-8"), "v0.6.156 Reviewer Walkthrough work item must be closed")
    require("control_matrix_work_item_closed = true" in V06153_DOC.read_text(encoding="utf-8"), "v0.6.153 Control Matrix work item must be closed")
    require("safe_poc_boundary_template_work_item_closed = true" in V06150_DOC.read_text(encoding="utf-8"), "v0.6.150 Safe PoC Boundary Template work item must be closed")
    require("technical_due_diligence_summary_work_item_closed = true" in V06147_DOC.read_text(encoding="utf-8"), "v0.6.147 Technical Due Diligence Summary work item must be closed")
    require("enterprise_review_guide_work_item_closed = true" in V06144_DOC.read_text(encoding="utf-8"), "v0.6.144 Enterprise Review Guide work item must be closed")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    for phrase in ["risk_tiered_granularity_adopted = true", "Low risk", "Medium risk", "High risk", "Critical risk", "expanded_checkpoint_pattern_no_longer_default = true"]:
        require(phrase in v06120, f"v0.6.120 policy missing required phrase: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in ["aaef_main_handback_sequence_paused = true", "aaef_main_handback_sequence_closed_for_now = true", "aaef_main_issue_opened = false", "aaef_main_pull_request_opened = false"]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checkpoint creates the buyer-facing commercial inquiry boundary",
        "this checkpoint creates commercial license terms",
        "this checkpoint approves a paid engagement",
        "this checkpoint authorizes a customer poc",
        "this checkpoint modifies runtime behavior",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
        "customer target is authorized by this checkpoint",
        "delivery is authorized by this checkpoint",
        "commercial contract is created by this checkpoint",
        "customer poc is authorized by this checkpoint",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.163 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.163 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
