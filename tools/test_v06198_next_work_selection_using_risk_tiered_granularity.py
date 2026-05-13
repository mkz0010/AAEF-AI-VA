from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/274-v06198-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0268-add-v06198-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0267-add-v06198-next-work-selection-using-risk-tiered-granularity.md"
V06197 = ROOT / "docs/273-v06197-repository-landing-demo-path-clarity-review-and-decision.md"
V06196 = ROOT / "docs/272-v06196-repository-landing-demo-path-clarity-candidate.md"
CLARITY = ROOT / "docs/repository-landing-demo-path-clarity.md"
V06195 = ROOT / "docs/271-v06195-next-work-selection-using-risk-tiered-granularity.md"
V06194 = ROOT / "docs/270-v06194-safe-demo-fixture-set-review-and-decision.md"
V06193 = ROOT / "docs/269-v06193-safe-demo-fixture-set-candidate.md"
FIXTURE_DIR = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review"
FIXTURE_FILES = [
    FIXTURE_DIR / "request.fixture.json",
    FIXTURE_DIR / "gate-decision.fixture.json",
    FIXTURE_DIR / "non-execution-result.fixture.json",
    FIXTURE_DIR / "evidence-trace.fixture.json",
    FIXTURE_DIR / "reviewer-walkthrough.md",
]
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
V06184 = ROOT / "docs/260-v06184-safe-demo-scenario-definition-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Public Demo Readiness Review.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.199 Public Demo Readiness Review Candidate.', 'The follow-up checkpoint is v0.6.200 Public Demo Readiness Review and Decision.', 'This checkpoint does not create the Public Demo Readiness Review candidate.', 'This checkpoint does not create new fixture files.', 'This checkpoint does not create public samples.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not create an executable demo.', 'This checkpoint does not start runtime or scanner work.', 'This checkpoint does not authorize customer PoC intake.', 'This checkpoint does not modify runtime behavior.', 'This checkpoint does not modify validator behavior.', 'This checkpoint does not add a JSON Schema.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Expected Public Demo Readiness Review scope', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06198_completed = true', 'next_work_selection_v06198_is_documentation_only = true', 'next_work_selection_v06198_uses_v06120_granularity_policy = true', 'next_work_selection_v06198_uses_v06197_landing_demo_path_clarity_closeout = true', 'v06198_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = public_demo_readiness_review', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_review', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.199 Public Demo Readiness Review Candidate', 'selected_followup_checkpoint = v0.6.200 Public Demo Readiness Review and Decision', 'public_demo_readiness_review_selected = true', 'public_demo_readiness_review_candidate_created = false', 'public_demo_readiness_review_decision_completed = false', 'public_demo_readiness_review_should_evaluate_wording = true', 'public_demo_readiness_review_should_evaluate_public_demo_label = true', 'public_demo_readiness_review_should_evaluate_repository_visibility = true', 'public_demo_readiness_review_should_preserve_fixture_only_boundary = true', 'public_demo_readiness_review_should_preserve_non_execution_boundary = true', 'public_demo_readiness_review_should_not_create_public_demo = true', 'public_demo_readiness_review_should_not_create_executable_demo = true', 'public_demo_readiness_review_should_not_create_new_fixtures = true', 'public_demo_readiness_review_should_not_modify_runtime_behavior = true', 'public_demo_readiness_review_should_not_modify_validator_behavior = true', 'public_demo_readiness_review_should_not_add_schema = true', 'repository_landing_demo_path_clarity_work_item_closed = true', 'repository_landing_demo_path_clarity_status = accepted', 'safe_demo_fixture_review_path_readme_entry_accepted = true', 'safe_demo_fixture_set_creation_work_item_closed = true', 'safe_demo_fixture_set_status = accepted', 'safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review', 'safe_demo_fixture_set_is_static = true', 'safe_demo_fixture_set_is_mock = true', 'safe_demo_fixture_set_is_non_execution = true', 'safe_demo_fixture_set_is_reviewer_facing = true', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'additional_fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'sensitive_value_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN = ['public demo readiness review is created in this checkpoint', 'new fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'sensitive value injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'audit opinion provided', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06197, V06196, CLARITY, V06195, V06194, V06193, FIXTURE_DIR, *FIXTURE_FILES, V06190, V06187, V06184, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required path: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.198 document missing required text: {phrase}")

    v06197 = V06197.read_text(encoding="utf-8")
    for phrase in [
        "repository_landing_demo_path_clarity_review_decision_completed = true",
        "repository_landing_demo_path_clarity_candidate_accepted = true",
        "repository_landing_demo_path_clarity_work_item_closed = true",
        "repository_landing_demo_path_clarity_status = accepted",
        "safe_demo_fixture_review_path_readme_entry_accepted = true",
        "selected_next_checkpoint = v0.6.198 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06197, f"v0.6.197 closeout missing required phrase: {phrase}")

    v06196 = V06196.read_text(encoding="utf-8")
    for phrase in [
        "repository_landing_demo_path_clarity_candidate_completed = true",
        "repository_landing_demo_path_clarity_created = true",
        "repository_landing_demo_path_clarity_readme_entry_added = true",
    ]:
        require(phrase in v06196, f"v0.6.196 candidate missing required phrase: {phrase}")

    clarity = CLARITY.read_text(encoding="utf-8")
    for phrase in [
        "docs/examples/safe-demo/blocked-tool-action-request-review/",
        "not a scanner",
        "not an executable demo",
        "not a public demo",
        "not PoC readiness",
        "not authorization to test third-party systems",
    ]:
        require(phrase in clarity, f"clarity document missing required phrase: {phrase}")

    require("selected_next_work_item = repository_landing_demo_path_clarity" in V06195.read_text(encoding="utf-8"), "v0.6.195 selection must remain recorded")
    require("safe_demo_fixture_set_creation_work_item_closed = true" in V06194.read_text(encoding="utf-8"), "v0.6.194 fixture set closeout must remain recorded")
    require("safe_demo_fixture_set_candidate_completed = true" in V06193.read_text(encoding="utf-8"), "v0.6.193 fixture set candidate must remain recorded")
    require("safe_demo_fixture_set_planning_work_item_closed = true" in V06190.read_text(encoding="utf-8"), "v0.6.190 fixture planning closeout must remain recorded")
    require("safe_demo_artifact_planning_work_item_closed = true" in V06187.read_text(encoding="utf-8"), "v0.6.187 artifact planning closeout must remain recorded")
    require("safe_demo_scenario_definition_work_item_closed = true" in V06184.read_text(encoding="utf-8"), "v0.6.184 scenario definition closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN:
        require(phrase not in lower_doc, f"v0.6.198 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.198 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
