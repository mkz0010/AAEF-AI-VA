from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/safe-demo-fixture-set-planning.md"
DOC = ROOT / "docs/265-v06189-safe-demo-fixture-set-planning-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0259-add-v06189-safe-demo-fixture-set-planning-candidate.md"
ISSUE = ROOT / "planning/issues/0258-add-v06189-safe-demo-fixture-set-planning-candidate.md"
V06188 = ROOT / "docs/264-v06188-next-work-selection-using-risk-tiered-granularity.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
ARTIFACT_PLAN = ROOT / "docs/safe-demo-artifact-planning.md"
V06184 = ROOT / "docs/260-v06184-safe-demo-scenario-definition-review-and-decision.md"
SCENARIO = ROOT / "docs/safe-demo-scenario-definition.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06179 = ROOT / "docs/255-v06179-public-demo-positioning-review-and-decision.md"
POSITIONING = ROOT / "docs/public-demo-positioning.md"
SUMMARY = ROOT / "docs/current-state-executive-summary.md"
V06173 = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['safe_demo_fixture_set_planning_candidate_completed = true', 'safe_demo_fixture_set_planning_candidate_is_medium_risk = true', 'safe_demo_fixture_set_planning_candidate_checkpoint_1_of_2 = true', 'safe_demo_fixture_set_planning_review_decision_deferred_to_v06190 = true', 'safe_demo_fixture_set_planning_created = true', 'safe_demo_fixture_set_planning_status = draft_candidate', 'safe_demo_fixture_set_planning_claim_safe = true', 'safe_demo_fixture_set_planning_is_documentation_only = true', 'safe_demo_fixture_set_planning_supports_accepted_artifact_plan = true', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_artifact_planning_supports_accepted_scenario = true', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'fixture_inventory_defined = true', 'fixture_file_boundary_defined = true', 'request_fixture_boundary_defined = true', 'gate_decision_fixture_boundary_defined = true', 'non_execution_result_fixture_boundary_defined = true', 'evidence_trace_fixture_boundary_defined = true', 'reviewer_walkthrough_boundary_defined = true', 'static_validation_expectations_defined = true', 'file_naming_expectations_defined = true', 'public_private_fixture_distinction_defined = true', 'fixture_creation_sequence_defined = true', 'fixture_files_created = false', 'public_samples_created = false', 'actual_fixture_creation_deferred = true', 'safe_demo_artifact_creation_deferred = true', 'public_demo_artifact_creation_deferred = true', 'executable_demo_creation_deferred = true', 'runtime_scanner_readiness_deferred = true', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'public_demo_positioning_work_item_closed = true', 'current_state_executive_summary_work_item_closed = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'review_decision_completed = false', 'safe_demo_fixture_set_planning_review_decision_completed = false', 'fixture_set_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.190 Safe Demo Fixture Set Planning Review and Decision']
FORBIDDEN = ['fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']
REQUIRED_PLAN_PHRASES = ['# Safe Demo Fixture Set Planning', 'Status: draft_candidate', 'This planning document supports the accepted Safe Demo Artifact Planning document.', 'The plan is documentation-only at this checkpoint.', 'No fixture files are added by this planning document.', 'No public samples are added by this planning document.', 'No executable demo artifact is added by this planning document.', 'Fixture inventory', 'Fixture file boundary', 'Request fixture boundary', 'Gate decision fixture boundary', 'Non-execution result fixture boundary', 'Evidence trace fixture boundary', 'Reviewer walkthrough boundary', 'Static validation expectations', 'File naming expectations', 'Public and private fixture distinction', 'Future fixture creation sequence', 'Fixtures intentionally not created yet', 'v0.6.190 Safe Demo Fixture Set Planning Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [PLAN, DOC, ADR, ISSUE, V06188, V06187, ARTIFACT_PLAN, V06184, SCENARIO, V06181, V06179, POSITIONING, SUMMARY, V06173, V06172, V06119]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    plan_text = PLAN.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_PLAN_PHRASES:
        require(phrase in plan_text, f"safe demo fixture set planning missing required phrase: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.189 candidate document missing flag: {phrase}")

    v06188 = V06188.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06188_completed = true",
        "selected_next_work_item = safe_demo_fixture_set_planning",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.189 Safe Demo Fixture Set Planning Candidate",
    ]:
        require(phrase in v06188, f"v0.6.188 selection missing required phrase: {phrase}")

    v06187 = V06187.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_artifact_planning_review_decision_completed = true",
        "safe_demo_artifact_planning_candidate_accepted = true",
        "safe_demo_artifact_planning_work_item_closed = true",
        "safe_demo_artifact_planning_status = accepted",
        "artifact_inventory_accepted = true",
        "fixture_boundary_accepted = true",
        "evidence_trace_boundary_accepted = true",
    ]:
        require(phrase in v06187, f"v0.6.187 closeout missing required phrase: {phrase}")

    artifact_plan = ARTIFACT_PLAN.read_text(encoding="utf-8")
    for phrase in [
        "This planning document supports the accepted Blocked Tool Action Request Review scenario.",
        "Artifact inventory",
        "Fixture boundary",
        "Evidence trace boundary",
        "Future artifact creation sequence",
        "Artifacts intentionally not created yet",
    ]:
        require(phrase in artifact_plan, f"safe demo artifact planning missing required phrase: {phrase}")

    v06184 = V06184.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_scenario_definition_review_decision_completed = true",
        "safe_demo_scenario_definition_candidate_accepted = true",
        "safe_demo_scenario_definition_work_item_closed = true",
        "safe_demo_scenario_story = blocked_tool_action_request_review",
    ]:
        require(phrase in v06184, f"v0.6.184 closeout missing required phrase: {phrase}")

    scenario = SCENARIO.read_text(encoding="utf-8")
    for phrase in [
        "Scenario name: Blocked Tool Action Request Review",
        "Primary outcome: blocked or non-executed request with reviewable evidence.",
        "The scenario uses mock or fixture-only inputs.",
        "Evidence trace should be the core of the scenario.",
    ]:
        require(phrase in scenario, f"safe demo scenario definition missing required phrase: {phrase}")

    v06181 = V06181.read_text(encoding="utf-8")
    for phrase in [
        "commercial_inquiry_response_boundary_deferral_decision_completed = true",
        "commercial_inquiry_response_boundary_deferred = true",
        "commercial_inquiry_response_template_deferred = true",
    ]:
        require(phrase in v06181, f"v0.6.181 deferral missing required phrase: {phrase}")

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
    ]:
        require(phrase in v06173, f"v0.6.173 priority review missing required phrase: {phrase}")

    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (plan_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.189 Safe Demo Fixture Set Planning candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
