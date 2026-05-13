from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/267-v06191-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0261-add-v06191-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0260-add-v06191-next-work-selection-using-risk-tiered-granularity.md"
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
FIXTURE_PLAN = ROOT / "docs/safe-demo-fixture-set-planning.md"
V06189 = ROOT / "docs/265-v06189-safe-demo-fixture-set-planning-candidate.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
V06184 = ROOT / "docs/260-v06184-safe-demo-scenario-definition-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Safe Demo Fixture Set Creation.', 'The selected next work item risk tier is High risk.', 'The selected checkpoint count is 3 checkpoints.', 'The next checkpoint is v0.6.192 Safe Demo Fixture Set Creation Readiness Review.', 'The follow-up checkpoint is v0.6.193 Safe Demo Fixture Set Candidate.', 'The final checkpoint is v0.6.194 Safe Demo Fixture Set Review and Decision.', 'This checkpoint does not create fixture files.', 'This checkpoint does not create public samples.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not create an executable demo.', 'This checkpoint does not start runtime or scanner work.', 'This checkpoint does not authorize customer PoC intake.', 'This checkpoint does not modify runtime behavior.', 'This checkpoint does not modify validator behavior.', 'This checkpoint does not add a JSON Schema.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is High risk', 'Why not Critical risk', 'Why not Medium or Low risk', 'Planned checkpoint split', 'Expected readiness review scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06191_completed = true', 'next_work_selection_v06191_is_documentation_only = true', 'next_work_selection_v06191_uses_v06120_granularity_policy = true', 'next_work_selection_v06191_uses_v06190_fixture_set_planning_closeout = true', 'v06191_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = safe_demo_fixture_set_creation', 'selected_next_work_item_risk_tier = high', 'selected_next_work_item_checkpoint_count = 3', 'selected_next_work_item_first_checkpoint = readiness_review', 'selected_next_work_item_second_checkpoint = candidate_implementation', 'selected_next_work_item_third_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.192 Safe Demo Fixture Set Creation Readiness Review', 'selected_followup_checkpoint = v0.6.193 Safe Demo Fixture Set Candidate', 'selected_final_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision', 'safe_demo_fixture_set_creation_selected = true', 'safe_demo_fixture_set_creation_readiness_review_selected = true', 'safe_demo_fixture_set_candidate_selected_as_future_checkpoint = true', 'safe_demo_fixture_set_review_decision_selected_as_future_checkpoint = true', 'safe_demo_fixture_set_creation_created = false', 'safe_demo_fixture_set_creation_readiness_review_created = false', 'safe_demo_fixture_set_candidate_created = false', 'safe_demo_fixture_set_review_decision_completed = false', 'safe_demo_fixture_set_planning_work_item_closed = true', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_fixture_set_planning_candidate_accepted = true', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'high_risk_three_checkpoint_pattern_selected = true', 'readiness_before_fixture_creation_required = true', 'fixture_creation_should_follow_accepted_fixture_plan = true', 'fixture_creation_should_remain_static_mock_and_non_execution = true', 'fixture_creation_should_create_only_safe_static_fixtures_if_later_approved = true', 'fixture_creation_should_include_publication_boundary_review = true', 'fixture_creation_should_include_static_validation_review = true', 'fixture_creation_should_not_modify_runtime_behavior = true', 'fixture_creation_should_not_authorize_runtime_execution = true', 'fixture_creation_should_not_authorize_scanner_execution = true', 'fixture_creation_should_not_authorize_customer_target_activity = true', 'fixture_creation_should_not_authorize_customer_poc = true', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'fixture_set_created = false', 'fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN = ['fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06190, FIXTURE_PLAN, V06189, V06187, V06184, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.191 document missing required text: {phrase}")

    v06190 = V06190.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_planning_review_decision_completed = true",
        "safe_demo_fixture_set_planning_candidate_accepted = true",
        "safe_demo_fixture_set_planning_work_item_closed = true",
        "safe_demo_fixture_set_planning_status = accepted",
        "fixture_inventory_accepted = true",
        "request_fixture_boundary_accepted = true",
        "gate_decision_fixture_boundary_accepted = true",
        "non_execution_result_fixture_boundary_accepted = true",
        "evidence_trace_fixture_boundary_accepted = true",
        "selected_next_checkpoint = v0.6.191 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06190, f"v0.6.190 closeout missing required phrase: {phrase}")

    fixture_plan = FIXTURE_PLAN.read_text(encoding="utf-8")
    for phrase in [
        "This planning document supports the accepted Safe Demo Artifact Planning document.",
        "Fixture inventory",
        "Request fixture boundary",
        "Gate decision fixture boundary",
        "Non-execution result fixture boundary",
        "Evidence trace fixture boundary",
        "Fixtures intentionally not created yet",
    ]:
        require(phrase in fixture_plan, f"safe demo fixture set planning missing required phrase: {phrase}")

    v06189 = V06189.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_planning_candidate_completed = true",
        "safe_demo_fixture_set_planning_created = true",
        "safe_demo_fixture_set_planning_status = draft_candidate",
        "selected_next_checkpoint = v0.6.190 Safe Demo Fixture Set Planning Review and Decision",
    ]:
        require(phrase in v06189, f"v0.6.189 candidate missing required phrase: {phrase}")

    require("safe_demo_artifact_planning_work_item_closed = true" in V06187.read_text(encoding="utf-8"), "v0.6.187 artifact planning closeout must remain recorded")
    require("safe_demo_scenario_definition_work_item_closed = true" in V06184.read_text(encoding="utf-8"), "v0.6.184 scenario definition closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN:
        require(phrase not in lower_doc, f"v0.6.191 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.191 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
