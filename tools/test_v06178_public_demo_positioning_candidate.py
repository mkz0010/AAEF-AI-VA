from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSITIONING = ROOT / "docs/public-demo-positioning.md"
DOC = ROOT / "docs/254-v06178-public-demo-positioning-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0248-add-v06178-public-demo-positioning-candidate.md"
ISSUE = ROOT / "planning/issues/0247-add-v06178-public-demo-positioning-candidate.md"
V06177_DOC = ROOT / "docs/253-v06177-next-work-selection-using-risk-tiered-granularity.md"
V06176_DOC = ROOT / "docs/252-v06176-current-state-executive-summary-review-and-decision.md"
SUMMARY = ROOT / "docs/current-state-executive-summary.md"
V06173_DOC = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
V06172_DOC = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['public_demo_positioning_candidate_completed = true', 'public_demo_positioning_candidate_is_medium_risk = true', 'public_demo_positioning_candidate_checkpoint_1_of_2 = true', 'public_demo_positioning_review_decision_deferred_to_v06179 = true', 'public_demo_positioning_created = true', 'public_demo_positioning_status = draft_candidate', 'public_demo_positioning_claim_safe = true', 'public_demo_positioning_for_reviewers_and_decision_makers = true', 'public_demo_positioning_for_technically_informed_buyers = true', 'public_demo_positioning_distinguishes_demo_types = true', 'non_execution_demo_positioning_included = true', 'mock_demo_positioning_included = true', 'fixture_demo_positioning_included = true', 'local_only_demo_positioning_included = true', 'runtime_execution_boundary_included = true', 'scanner_execution_boundary_included = true', 'customer_poc_boundary_included = true', 'blocked_execution_can_be_valid_demo_outcome = true', 'evidence_trace_should_be_demo_focus = true', 'tool_action_request_boundary_summary_included = true', 'gate_decision_boundary_summary_included = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'review_decision_completed = false', 'public_demo_positioning_review_decision_completed = false', 'safe_demo_created = false', 'public_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'readme_public_entry_modified = false', 'readme_commercial_inquiry_entry_modified = false', 'inquiry_address_publication_modified = false', 'buyer_facing_commercial_inquiry_boundary_modified = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.179 Public Demo Positioning Review and Decision']
FORBIDDEN = ['customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'public demo is created in this checkpoint', 'safe demo is created in this checkpoint', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']
REQUIRED_POSITIONING_PHRASES = ['# Public Demo Positioning', 'Status: draft_candidate', 'A safe public demo should demonstrate control boundaries, not live diagnostic power.', 'AI may generate a tool_action_request, but execution is decided by gates.', 'Blocked execution can be a valid demo outcome.', 'Evidence trace should be the demo focus.', 'Non-execution demo', 'Mock demo', 'Fixture demo', 'Local-only lab demo', 'Runtime execution', 'Scanner execution', 'Customer PoC', 'The first public demo should prefer non-execution, mock, fixture, or local-only forms.', 'This positioning does not create a demo artifact.', 'v0.6.179 Public Demo Positioning Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [POSITIONING, DOC, ADR, ISSUE, V06177_DOC, V06176_DOC, SUMMARY, V06173_DOC, V06172_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    positioning_text = POSITIONING.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_POSITIONING_PHRASES:
        require(phrase in positioning_text, f"positioning missing required phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.178 candidate document missing flag: {phrase}")

    v06177 = V06177_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = public_demo_positioning",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.178 Public Demo Positioning Candidate",
    ]:
        require(phrase in v06177, f"v0.6.177 selection missing required phrase: {phrase}")

    v06176 = V06176_DOC.read_text(encoding="utf-8")
    for phrase in [
        "current_state_executive_summary_review_decision_completed = true",
        "current_state_executive_summary_candidate_accepted = true",
        "current_state_executive_summary_work_item_closed = true",
    ]:
        require(phrase in v06176, f"v0.6.176 closeout missing required phrase: {phrase}")

    summary_text = SUMMARY.read_text(encoding="utf-8")
    for phrase in [
        "AAEF-AI-VA is a safety-first reference implementation",
        "AI may generate a tool_action_request, but execution is decided by gates.",
        "Safe demo layer: near-term candidate.",
        "Runtime and scanner execution remain deferred.",
        "Customer PoC intake also remains deferred.",
    ]:
        require(phrase in summary_text, f"current-state executive summary missing required phrase: {phrase}")

    v06173 = V06173_DOC.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_layer_status = near_term_candidate",
        "runtime_scanner_layer_status = deferred_pending_readiness_review",
        "customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries",
        "non_execution_demo_is_preferred_first_demo = true",
        "local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true",
    ]:
        require(phrase in v06173, f"v0.6.173 priority review missing required phrase: {phrase}")

    require("aaef_main_contact_reflection_deferred = true" in V06172_DOC.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (positioning_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.178 Public Demo Positioning candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
