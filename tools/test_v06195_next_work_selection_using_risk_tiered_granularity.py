from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/271-v06195-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0265-add-v06195-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0264-add-v06195-next-work-selection-using-risk-tiered-granularity.md"
V06194 = ROOT / "docs/270-v06194-safe-demo-fixture-set-review-and-decision.md"
V06193 = ROOT / "docs/269-v06193-safe-demo-fixture-set-candidate.md"
FIXTURE_DIR = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review"
REQUEST = FIXTURE_DIR / "request.fixture.json"
DECISION = FIXTURE_DIR / "gate-decision.fixture.json"
RESULT = FIXTURE_DIR / "non-execution-result.fixture.json"
TRACE = FIXTURE_DIR / "evidence-trace.fixture.json"
WALKTHROUGH = FIXTURE_DIR / "reviewer-walkthrough.md"
V06192 = ROOT / "docs/268-v06192-safe-demo-fixture-set-creation-readiness-review.md"
V06191 = ROOT / "docs/267-v06191-next-work-selection-using-risk-tiered-granularity.md"
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
V06184 = ROOT / "docs/260-v06184-safe-demo-scenario-definition-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Repository Landing and Demo Path Clarity.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.196 Repository Landing and Demo Path Clarity Candidate.', 'The follow-up checkpoint is v0.6.197 Repository Landing and Demo Path Clarity Review and Decision.', 'This checkpoint does not create the Repository Landing and Demo Path Clarity artifact.', 'This checkpoint does not create new fixture files.', 'This checkpoint does not create public samples.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not create an executable demo.', 'This checkpoint does not start runtime or scanner work.', 'This checkpoint does not authorize customer PoC intake.', 'This checkpoint does not modify runtime behavior.', 'This checkpoint does not modify validator behavior.', 'This checkpoint does not add a JSON Schema.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Repository Landing and Demo Path Clarity scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06195_completed = true', 'next_work_selection_v06195_is_documentation_only = true', 'next_work_selection_v06195_uses_v06120_granularity_policy = true', 'next_work_selection_v06195_uses_v06194_fixture_set_closeout = true', 'v06195_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = repository_landing_demo_path_clarity', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.196 Repository Landing and Demo Path Clarity Candidate', 'selected_followup_checkpoint = v0.6.197 Repository Landing and Demo Path Clarity Review and Decision', 'repository_landing_demo_path_clarity_selected = true', 'repository_landing_demo_path_clarity_created = false', 'repository_landing_demo_path_clarity_review_decision_completed = false', 'repository_landing_demo_path_clarity_should_reference_accepted_fixture_set = true', 'repository_landing_demo_path_clarity_should_reference_safe_demo_boundary = true', 'repository_landing_demo_path_clarity_should_explain_demo_review_path = true', 'repository_landing_demo_path_clarity_should_preserve_non_execution_boundary = true', 'repository_landing_demo_path_clarity_should_not_create_new_fixtures = true', 'repository_landing_demo_path_clarity_should_not_create_public_demo = true', 'repository_landing_demo_path_clarity_should_not_create_executable_demo = true', 'repository_landing_demo_path_clarity_should_not_modify_runtime_behavior = true', 'repository_landing_demo_path_clarity_should_not_modify_validator_behavior = true', 'repository_landing_demo_path_clarity_should_not_add_schema = true', 'safe_demo_fixture_set_creation_work_item_closed = true', 'safe_demo_fixture_set_status = accepted', 'safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review', 'safe_demo_fixture_set_is_static = true', 'safe_demo_fixture_set_is_mock = true', 'safe_demo_fixture_set_is_non_execution = true', 'safe_demo_fixture_set_is_reviewer_facing = true', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'additional_fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'sensitive_value_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN = ['repository landing and demo path clarity is created in this checkpoint', 'new fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06194, V06193, FIXTURE_DIR, REQUEST, DECISION, RESULT, TRACE, WALKTHROUGH, V06192, V06191, V06190, V06187, V06184, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required path: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.195 document missing required text: {phrase}")

    v06194 = V06194.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_review_decision_completed = true",
        "safe_demo_fixture_set_candidate_accepted = true",
        "safe_demo_fixture_set_creation_work_item_closed = true",
        "safe_demo_fixture_set_status = accepted",
        "request_fixture_accepted = true",
        "gate_decision_fixture_accepted = true",
        "non_execution_result_fixture_accepted = true",
        "evidence_trace_fixture_accepted = true",
        "reviewer_walkthrough_accepted = true",
        "selected_next_checkpoint = v0.6.195 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06194, f"v0.6.194 closeout missing required phrase: {phrase}")

    v06193 = V06193.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_candidate_completed = true",
        "fixture_set_created = true",
        "fixture_files_created = true",
        "request_fixture_created = true",
        "gate_decision_fixture_created = true",
        "non_execution_result_fixture_created = true",
        "evidence_trace_fixture_created = true",
        "reviewer_walkthrough_created = true",
    ]:
        require(phrase in v06193, f"v0.6.193 candidate missing required phrase: {phrase}")

    require("safe_demo_fixture_set_creation_readiness_review_completed = true" in V06192.read_text(encoding="utf-8"), "v0.6.192 readiness review must remain recorded")
    require("selected_next_work_item = safe_demo_fixture_set_creation" in V06191.read_text(encoding="utf-8"), "v0.6.191 selection must remain recorded")
    require("safe_demo_fixture_set_planning_work_item_closed = true" in V06190.read_text(encoding="utf-8"), "v0.6.190 fixture planning closeout must remain recorded")
    require("safe_demo_artifact_planning_work_item_closed = true" in V06187.read_text(encoding="utf-8"), "v0.6.187 artifact planning closeout must remain recorded")
    require("safe_demo_scenario_definition_work_item_closed = true" in V06184.read_text(encoding="utf-8"), "v0.6.184 scenario definition closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN:
        require(phrase not in lower_doc, f"v0.6.195 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.195 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
