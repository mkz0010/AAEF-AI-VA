from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/250-v06174-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0244-add-v06174-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0243-add-v06174-next-work-selection-using-risk-tiered-granularity.md"
V06173_DOC = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
V06172_DOC = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06170_DOC = ROOT / "docs/246-v06170-public-entry-and-inquiry-route-consistency-review-review-and-decision.md"
V06167_DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Current-State Executive Summary.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.175 Current-State Executive Summary Candidate.', 'The follow-up checkpoint is v0.6.176 Current-State Executive Summary Review and Decision.', 'This checkpoint does not create the Current-State Executive Summary.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not start runtime or scanner work.', 'This checkpoint does not authorize customer PoC intake.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Current-State Executive Summary scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06174_completed = true', 'next_work_selection_v06174_is_documentation_only = true', 'next_work_selection_v06174_uses_v06120_granularity_policy = true', 'next_work_selection_v06174_uses_v06173_current_state_priority_review = true', 'v06174_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = current_state_executive_summary', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.175 Current-State Executive Summary Candidate', 'selected_followup_checkpoint = v0.6.176 Current-State Executive Summary Review and Decision', 'current_state_executive_summary_selected = true', 'current_state_executive_summary_created = false', 'current_state_executive_summary_review_decision_completed = false', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'safe_demo_should_precede_real_scanner_execution = true', 'non_execution_demo_is_preferred_first_demo = true', 'local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true', 'real_scanner_execution_remains_unselected = true', 'runtime_execution_remains_unselected = true', 'customer_poc_intake_remains_unselected = true', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN_DOC_PHRASES = ['current-state executive summary is created in this checkpoint', 'safe demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06173_DOC, V06172_DOC, V06170_DOC, V06167_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.174 document missing required text: {phrase}")

    v06173 = V06173_DOC.read_text(encoding="utf-8")
    for phrase in [
        "current_state_and_priority_review_v06173_completed = true",
        "documentation_and_review_package_layer_status = implemented",
        "safe_demo_layer_status = near_term_candidate",
        "runtime_scanner_layer_status = deferred_pending_readiness_review",
        "customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries",
        "recommended_next_work_item = current_state_executive_summary",
        "recommended_next_work_item_risk_tier = medium",
        "recommended_next_work_item_checkpoint_count = 2",
        "recommended_next_checkpoint = v0.6.174 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06173, f"v0.6.173 baseline missing required phrase: {phrase}")

    v06172 = V06172_DOC.read_text(encoding="utf-8")
    require("aaef_main_contact_reflection_deferred = true" in v06172, "v0.6.172 AAEF main contact deferral must remain recorded")

    v06170 = V06170_DOC.read_text(encoding="utf-8")
    require("public_entry_and_inquiry_route_consistency_review_work_item_closed = true" in v06170, "v0.6.170 route consistency work item must remain closed")

    v06167 = V06167_DOC.read_text(encoding="utf-8")
    require("maintainer_inquiry_address_publication_work_item_closed = true" in v06167, "v0.6.167 inquiry address work item must remain closed")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    for phrase in ["risk_tiered_granularity_adopted = true", "Low risk", "Medium risk", "High risk", "Critical risk"]:
        require(phrase in v06120, f"v0.6.120 policy missing required phrase: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in ["aaef_main_handback_sequence_paused = true", "aaef_main_issue_opened = false", "aaef_main_pull_request_opened = false"]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN_DOC_PHRASES:
        require(phrase not in lower_doc, f"v0.6.174 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.174 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
