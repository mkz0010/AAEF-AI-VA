from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/258-v06182-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0252-add-v06182-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0251-add-v06182-next-work-selection-using-risk-tiered-granularity.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06180 = ROOT / "docs/256-v06180-next-work-selection-using-risk-tiered-granularity.md"
V06179 = ROOT / "docs/255-v06179-public-demo-positioning-review-and-decision.md"
POSITIONING = ROOT / "docs/public-demo-positioning.md"
SUMMARY = ROOT / "docs/current-state-executive-summary.md"
V06173 = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Safe Demo Scenario Definition.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.183 Safe Demo Scenario Definition Candidate.', 'The follow-up checkpoint is v0.6.184 Safe Demo Scenario Definition Review and Decision.', 'This checkpoint does not create the Safe Demo Scenario Definition artifact.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not start runtime or scanner work.', 'This checkpoint does not authorize customer PoC intake.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Safe Demo Scenario Definition scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06182_completed = true', 'next_work_selection_v06182_is_documentation_only = true', 'next_work_selection_v06182_uses_v06120_granularity_policy = true', 'next_work_selection_v06182_uses_v06181_deferral_decision = true', 'v06182_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = safe_demo_scenario_definition', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.183 Safe Demo Scenario Definition Candidate', 'selected_followup_checkpoint = v0.6.184 Safe Demo Scenario Definition Review and Decision', 'safe_demo_scenario_definition_selected = true', 'safe_demo_scenario_definition_created = false', 'safe_demo_scenario_definition_review_decision_completed = false', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'public_demo_positioning_work_item_closed = true', 'current_state_executive_summary_work_item_closed = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'safe_demo_should_precede_real_scanner_execution = true', 'non_execution_demo_is_preferred_first_demo = true', 'local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true', 'blocked_execution_can_be_valid_demo_outcome = true', 'evidence_trace_should_be_demo_focus = true', 'safe_demo_scenario_should_define_request_gate_evidence_flow = true', 'safe_demo_scenario_should_not_create_runtime_execution = true', 'safe_demo_scenario_should_not_create_scanner_execution = true', 'safe_demo_scenario_should_not_create_customer_poc = true', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'safe_demo_created = false', 'public_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN = ['safe demo scenario definition is created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06181, V06180, V06179, POSITIONING, SUMMARY, V06173, V06172, V06120, V06119]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.182 document missing required text: {phrase}")

    v06181 = V06181.read_text(encoding="utf-8")
    for phrase in [
        "commercial_inquiry_response_boundary_deferral_decision_completed = true",
        "v06180_selection_deferred_before_candidate_creation = true",
        "commercial_inquiry_response_boundary_deferred = true",
        "commercial_inquiry_response_template_deferred = true",
        "commercial_inquiry_response_boundary_created = false",
        "commercial_inquiry_response_template_created = false",
        "selected_next_checkpoint = v0.6.182 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06181, f"v0.6.181 deferral missing required phrase: {phrase}")

    v06180 = V06180.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06180_completed = true",
        "selected_next_work_item = commercial_inquiry_response_boundary",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
    ]:
        require(phrase in v06180, f"v0.6.180 selection missing required phrase: {phrase}")

    v06179 = V06179.read_text(encoding="utf-8")
    for phrase in [
        "public_demo_positioning_review_decision_completed = true",
        "public_demo_positioning_candidate_accepted = true",
        "public_demo_positioning_work_item_closed = true",
        "blocked_execution_can_be_valid_demo_outcome_accepted = true",
        "evidence_trace_should_be_demo_focus_accepted = true",
    ]:
        require(phrase in v06179, f"v0.6.179 closeout missing required phrase: {phrase}")

    positioning = POSITIONING.read_text(encoding="utf-8")
    for phrase in [
        "A safe public demo should demonstrate control boundaries, not live diagnostic power.",
        "Blocked execution can be a valid demo outcome.",
        "Evidence trace should be the demo focus.",
        "The first public demo should prefer non-execution, mock, fixture, or local-only forms.",
    ]:
        require(phrase in positioning, f"public demo positioning missing required phrase: {phrase}")

    summary = SUMMARY.read_text(encoding="utf-8")
    for phrase in [
        "AAEF-AI-VA is a safety-first reference implementation",
        "AI may generate a tool_action_request, but execution is decided by gates.",
        "Safe demo layer: near-term candidate.",
        "Runtime and scanner execution remain deferred.",
        "Customer PoC intake also remains deferred.",
    ]:
        require(phrase in summary, f"current-state executive summary missing required phrase: {phrase}")

    v06173 = V06173.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_layer_status = near_term_candidate",
        "runtime_scanner_layer_status = deferred_pending_readiness_review",
        "customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries",
        "non_execution_demo_is_preferred_first_demo = true",
        "local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true",
    ]:
        require(phrase in v06173, f"v0.6.173 priority review missing required phrase: {phrase}")

    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN:
        require(phrase not in lower_doc, f"v0.6.182 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.182 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
