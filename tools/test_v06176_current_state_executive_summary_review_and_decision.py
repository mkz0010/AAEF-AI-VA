from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "docs/current-state-executive-summary.md"
DOC = ROOT / "docs/252-v06176-current-state-executive-summary-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0246-add-v06176-current-state-executive-summary-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0245-add-v06176-current-state-executive-summary-review-and-decision.md"
V06175_DOC = ROOT / "docs/251-v06175-current-state-executive-summary-candidate.md"
V06174_DOC = ROOT / "docs/250-v06174-next-work-selection-using-risk-tiered-granularity.md"
V06173_DOC = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
V06172_DOC = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06170_DOC = ROOT / "docs/246-v06170-public-entry-and-inquiry-route-consistency-review-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['current_state_executive_summary_review_decision_completed = true', 'current_state_executive_summary_review_decision_is_medium_risk = true', 'current_state_executive_summary_review_decision_checkpoint_2_of_2 = true', 'current_state_executive_summary_candidate_reviewed = true', 'current_state_executive_summary_candidate_accepted = true', 'current_state_executive_summary_work_item_closed = true', 'current_state_executive_summary_status = accepted', 'current_state_executive_summary_claim_safe = true', 'current_state_executive_summary_for_reviewers_and_decision_makers = true', 'current_state_executive_summary_for_technically_informed_buyers = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'public_evaluation_package_summary_accepted = true', 'buyer_facing_material_summary_accepted = true', 'tool_action_request_boundary_summary_accepted = true', 'gate_decision_boundary_summary_accepted = true', 'evidence_traceability_summary_accepted = true', 'safe_demo_positioning_summary_accepted = true', 'deferred_runtime_scanner_summary_accepted = true', 'deferred_customer_poc_summary_accepted = true', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'review_decision_completed = true', 'safe_demo_created = false', 'public_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.177 Next Work Selection Using Risk-Tiered Granularity']
FORBIDDEN = ['customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']
REQUIRED_SUMMARY_PHRASES = ['# Current-State Executive Summary', 'Status: draft_candidate', 'AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.', 'AI may generate a tool_action_request, but execution is decided by gates.', 'The documentation and review package layer is implemented.', 'Safe demo layer: near-term candidate.', 'Runtime and scanner execution remain deferred.', 'Customer PoC intake also remains deferred.', 'AAEF main contact publication remains deferred.', 'This summary is not:', 'v0.6.176 Current-State Executive Summary Review and Decision', 'hexroot0010@gmail.com']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [SUMMARY, DOC, ADR, ISSUE, V06175_DOC, V06174_DOC, V06173_DOC, V06172_DOC, V06170_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    summary_text = SUMMARY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_SUMMARY_PHRASES:
        require(phrase in summary_text, f"summary missing required phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.176 review/decision document missing flag: {phrase}")

    v06175 = V06175_DOC.read_text(encoding="utf-8")
    for phrase in [
        "current_state_executive_summary_candidate_completed = true",
        "current_state_executive_summary_created = true",
        "current_state_executive_summary_status = draft_candidate",
        "current_state_executive_summary_review_decision_deferred_to_v06176 = true",
        "selected_next_checkpoint = v0.6.176 Current-State Executive Summary Review and Decision",
    ]:
        require(phrase in v06175, f"v0.6.175 candidate missing required phrase: {phrase}")

    v06174 = V06174_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = current_state_executive_summary",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
    ]:
        require(phrase in v06174, f"v0.6.174 selection missing required phrase: {phrase}")

    v06173 = V06173_DOC.read_text(encoding="utf-8")
    for phrase in [
        "current_state_and_priority_review_v06173_completed = true",
        "documentation_and_review_package_layer_status = implemented",
        "safe_demo_layer_status = near_term_candidate",
        "runtime_scanner_layer_status = deferred_pending_readiness_review",
        "customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries",
    ]:
        require(phrase in v06173, f"v0.6.173 baseline missing required phrase: {phrase}")

    require("aaef_main_contact_reflection_deferred = true" in V06172_DOC.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("public_entry_and_inquiry_route_consistency_review_work_item_closed = true" in V06170_DOC.read_text(encoding="utf-8"), "v0.6.170 route consistency work item must remain closed")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (summary_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.176 Current-State Executive Summary review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
