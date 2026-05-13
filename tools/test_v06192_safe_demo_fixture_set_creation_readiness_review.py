from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/268-v06192-safe-demo-fixture-set-creation-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0262-add-v06192-safe-demo-fixture-set-creation-readiness-review.md"
ISSUE = ROOT / "planning/issues/0261-add-v06192-safe-demo-fixture-set-creation-readiness-review.md"
V06191 = ROOT / "docs/267-v06191-next-work-selection-using-risk-tiered-granularity.md"
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
FIXTURE_PLAN = ROOT / "docs/safe-demo-fixture-set-planning.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
ARTIFACT_PLAN = ROOT / "docs/safe-demo-artifact-planning.md"
V06184 = ROOT / "docs/260-v06184-safe-demo-scenario-definition-review-and-decision.md"
SCENARIO = ROOT / "docs/safe-demo-scenario-definition.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: readiness_review', 'This checkpoint is checkpoint 1 of 3 for the High-risk Safe Demo Fixture Set Creation work item.', 'This checkpoint performs a readiness review before any fixture files are created.', 'Readiness accepted.', 'The next checkpoint is v0.6.193 Safe Demo Fixture Set Candidate.', 'The final checkpoint remains v0.6.194 Safe Demo Fixture Set Review and Decision.', 'This checkpoint does not create fixture files.', 'This checkpoint does not create public samples.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not create an executable demo.', 'Allowed creation scope', 'Disallowed creation scope', 'Allowed fixture inventory', 'Allowed path boundary', 'Allowed file types', 'Request fixture constraints', 'Gate decision fixture constraints', 'Non-execution result fixture constraints', 'Evidence trace fixture constraints', 'Reviewer walkthrough constraints', 'Forbidden values', 'Forbidden claims', 'Publication boundary', 'Static validation review', 'Readiness decision', 'What did not happen', 'Next checkpoint']
FLAGS = ['safe_demo_fixture_set_creation_readiness_review_completed = true', 'safe_demo_fixture_set_creation_readiness_review_is_high_risk = true', 'safe_demo_fixture_set_creation_readiness_review_checkpoint_1_of_3 = true', 'safe_demo_fixture_set_candidate_deferred_to_v06193 = true', 'safe_demo_fixture_set_review_decision_deferred_to_v06194 = true', 'safe_demo_fixture_set_creation_readiness_accepted = true', 'safe_demo_fixture_set_creation_scope_defined = true', 'safe_demo_fixture_set_creation_allowed_scope_defined = true', 'safe_demo_fixture_set_creation_disallowed_scope_defined = true', 'safe_demo_fixture_set_allowed_paths_defined = true', 'safe_demo_fixture_set_allowed_file_types_defined = true', 'safe_demo_fixture_set_allowed_fixture_inventory_defined = true', 'safe_demo_fixture_set_request_fixture_constraints_defined = true', 'safe_demo_fixture_set_gate_decision_fixture_constraints_defined = true', 'safe_demo_fixture_set_non_execution_result_fixture_constraints_defined = true', 'safe_demo_fixture_set_evidence_trace_fixture_constraints_defined = true', 'safe_demo_fixture_set_reviewer_walkthrough_constraints_defined = true', 'safe_demo_fixture_set_publication_boundary_defined = true', 'safe_demo_fixture_set_static_validation_review_defined = true', 'safe_demo_fixture_set_forbidden_values_defined = true', 'safe_demo_fixture_set_forbidden_claims_defined = true', 'safe_demo_fixture_set_creation_may_proceed_to_candidate = true', 'safe_demo_fixture_set_candidate_allowed_next = true', 'safe_demo_fixture_set_planning_work_item_closed = true', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'fixture_creation_should_remain_static_mock_and_non_execution = true', 'fixture_creation_should_create_only_safe_static_fixtures_if_later_approved = true', 'fixture_creation_should_include_publication_boundary_review = true', 'fixture_creation_should_include_static_validation_review = true', 'fixture_creation_should_not_modify_runtime_behavior = true', 'fixture_creation_should_not_authorize_runtime_execution = true', 'fixture_creation_should_not_authorize_scanner_execution = true', 'fixture_creation_should_not_authorize_customer_target_activity = true', 'fixture_creation_should_not_authorize_customer_poc = true', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'fixture_set_created = false', 'fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.193 Safe Demo Fixture Set Candidate', 'selected_followup_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision']
FORBIDDEN = ['fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06191, V06190, FIXTURE_PLAN, V06187, ARTIFACT_PLAN, V06184, SCENARIO, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.192 readiness review missing required text: {phrase}")

    v06191 = V06191.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06191_completed = true",
        "selected_next_work_item = safe_demo_fixture_set_creation",
        "selected_next_work_item_risk_tier = high",
        "selected_next_work_item_checkpoint_count = 3",
        "selected_next_checkpoint = v0.6.192 Safe Demo Fixture Set Creation Readiness Review",
        "selected_followup_checkpoint = v0.6.193 Safe Demo Fixture Set Candidate",
        "selected_final_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision",
    ]:
        require(phrase in v06191, f"v0.6.191 selection missing required phrase: {phrase}")

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

    require("safe_demo_artifact_planning_work_item_closed = true" in V06187.read_text(encoding="utf-8"), "v0.6.187 artifact planning closeout must remain recorded")
    require("Safe Demo Artifact Planning" in ARTIFACT_PLAN.read_text(encoding="utf-8"), "safe demo artifact planning document must remain present")
    require("safe_demo_scenario_definition_work_item_closed = true" in V06184.read_text(encoding="utf-8"), "v0.6.184 scenario definition closeout must remain recorded")
    require("Scenario name: Blocked Tool Action Request Review" in SCENARIO.read_text(encoding="utf-8"), "safe demo scenario definition must remain present")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN:
        require(phrase not in lower_doc, f"v0.6.192 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.192 Safe Demo Fixture Set Creation readiness review tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
