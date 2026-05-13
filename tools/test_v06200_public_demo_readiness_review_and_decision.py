from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
READINESS = ROOT / "docs/public-demo-readiness-review.md"
DOC = ROOT / "docs/276-v06200-public-demo-readiness-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0270-add-v06200-public-demo-readiness-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0269-add-v06200-public-demo-readiness-review-and-decision.md"
V06199 = ROOT / "docs/275-v06199-public-demo-readiness-review-candidate.md"
V06198 = ROOT / "docs/274-v06198-next-work-selection-using-risk-tiered-granularity.md"
V06197 = ROOT / "docs/273-v06197-repository-landing-demo-path-clarity-review-and-decision.md"
V06196 = ROOT / "docs/272-v06196-repository-landing-demo-path-clarity-candidate.md"
CLARITY = ROOT / "docs/repository-landing-demo-path-clarity.md"
V06194 = ROOT / "docs/270-v06194-safe-demo-fixture-set-review-and-decision.md"
V06193 = ROOT / "docs/269-v06193-safe-demo-fixture-set-candidate.md"
FIXTURE_DIR = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review"
FIXTURES = [
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

REQUIRED_DOC = ['Status: decision', 'This checkpoint is checkpoint 2 of 2 for the Medium-risk Public Demo Readiness Review work item.', 'This checkpoint reviews and accepts the Public Demo Readiness Review candidate added in v0.6.199.', 'The Public Demo Readiness Review work item is closed.', 'Candidate accepted.', 'Do not call the current repository state a Public Demo yet.', 'Accepted public phrase', 'Static Fixture Review Path', 'public_demo_label_ready = false', 'public_demo_label_should_be_avoided_now = true', 'Wording review', 'Repository visibility review', 'Fixture boundary review', 'Runtime boundary review', 'Decision record', 'Work item closeout', 'v0.6.199 Public Demo Readiness Review Candidate', 'v0.6.200 Public Demo Readiness Review and Decision', 'v0.6.201 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_READINESS = ['# Public Demo Readiness Review', 'Status: draft_candidate', 'Do not call the current repository state a Public Demo yet.', 'Static Fixture Review Path', 'public_demo_label_ready = false', 'public_demo_label_should_be_avoided_now = true', 'static_fixture_review_path_publicly_explainable = true', 'This is not a scanner, not an executable demo, not a public demo, not PoC readiness, and not authorization to test third-party systems.', 'v0.6.200 Public Demo Readiness Review and Decision']
FLAGS = ['public_demo_readiness_review_decision_completed = true', 'public_demo_readiness_review_decision_is_medium_risk = true', 'public_demo_readiness_review_decision_checkpoint_2_of_2 = true', 'public_demo_readiness_review_candidate_reviewed = true', 'public_demo_readiness_review_candidate_accepted = true', 'public_demo_readiness_review_work_item_closed = true', 'public_demo_readiness_review_status = accepted', 'public_demo_readiness_review_is_documentation_only = true', 'public_demo_readiness_recommendation_accepted = true', 'public_demo_label_ready = false', 'public_demo_label_should_be_avoided_now = true', 'recommended_public_phrase = static_fixture_review_path', 'static_fixture_review_path_publicly_explainable = true', 'accepted_fixture_set_is_reviewable = true', 'accepted_fixture_set_is_not_public_demo = true', 'accepted_fixture_set_is_not_executable_demo = true', 'accepted_fixture_set_is_not_scanner_demo = true', 'accepted_fixture_set_is_not_poc_readiness = true', 'accepted_fixture_set_is_not_delivery_authorization = true', 'accepted_fixture_set_is_not_third_party_testing_authorization = true', 'public_demo_creation_deferred = true', 'public_announcement_deferred = true', 'public_demo_readiness_wording_review_accepted = true', 'public_demo_readiness_repository_visibility_review_accepted = true', 'public_demo_readiness_fixture_boundary_review_accepted = true', 'public_demo_readiness_runtime_boundary_review_accepted = true', 'repository_landing_demo_path_clarity_work_item_closed = true', 'repository_landing_demo_path_clarity_status = accepted', 'safe_demo_fixture_review_path_readme_entry_accepted = true', 'safe_demo_fixture_set_creation_work_item_closed = true', 'safe_demo_fixture_set_status = accepted', 'safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review', 'safe_demo_fixture_set_is_static = true', 'safe_demo_fixture_set_is_mock = true', 'safe_demo_fixture_set_is_non_execution = true', 'safe_demo_fixture_set_is_reviewer_facing = true', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'additional_fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'sensitive_value_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.201 Next Work Selection Using Risk-Tiered Granularity']
FORBIDDEN = ['public demo label ready = true', 'public demo label is ready', 'public demo is ready', 'public demo is created in this checkpoint', 'new fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'sensitive value injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'audit opinion provided', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [READINESS, DOC, ADR, ISSUE, V06199, V06198, V06197, V06196, CLARITY, V06194, V06193, FIXTURE_DIR, *FIXTURES, V06190, V06187, V06184, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required path: {path.relative_to(ROOT)}")

    readiness_text = READINESS.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_READINESS:
        require(phrase in readiness_text, f"public demo readiness review missing required text: {phrase}")

    for phrase in REQUIRED_DOC + FLAGS:
        require(phrase in doc_text, f"v0.6.200 document missing required text: {phrase}")

    v06199 = V06199.read_text(encoding="utf-8")
    for phrase in [
        "public_demo_readiness_review_candidate_completed = true",
        "public_demo_readiness_review_created = true",
        "public_demo_readiness_review_status = draft_candidate",
        "public_demo_label_ready = false",
        "public_demo_label_should_be_avoided_now = true",
        "recommended_public_phrase = static_fixture_review_path",
        "static_fixture_review_path_publicly_explainable = true",
        "selected_next_checkpoint = v0.6.200 Public Demo Readiness Review and Decision",
    ]:
        require(phrase in v06199, f"v0.6.199 candidate missing required phrase: {phrase}")

    v06198 = V06198.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06198_completed = true",
        "selected_next_work_item = public_demo_readiness_review",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
    ]:
        require(phrase in v06198, f"v0.6.198 selection missing required phrase: {phrase}")

    v06197 = V06197.read_text(encoding="utf-8")
    for phrase in [
        "repository_landing_demo_path_clarity_review_decision_completed = true",
        "repository_landing_demo_path_clarity_candidate_accepted = true",
        "repository_landing_demo_path_clarity_work_item_closed = true",
        "repository_landing_demo_path_clarity_status = accepted",
    ]:
        require(phrase in v06197, f"v0.6.197 closeout missing required phrase: {phrase}")

    require("repository_landing_demo_path_clarity_candidate_completed = true" in V06196.read_text(encoding="utf-8"), "v0.6.196 candidate must remain recorded")
    require("not a public demo" in CLARITY.read_text(encoding="utf-8"), "clarity document must preserve public demo boundary")
    require("safe_demo_fixture_set_creation_work_item_closed = true" in V06194.read_text(encoding="utf-8"), "v0.6.194 fixture set closeout must remain recorded")
    require("safe_demo_fixture_set_candidate_completed = true" in V06193.read_text(encoding="utf-8"), "v0.6.193 fixture set candidate must remain recorded")
    require("safe_demo_fixture_set_planning_work_item_closed = true" in V06190.read_text(encoding="utf-8"), "v0.6.190 fixture planning closeout must remain recorded")
    require("safe_demo_artifact_planning_work_item_closed = true" in V06187.read_text(encoding="utf-8"), "v0.6.187 artifact planning closeout must remain recorded")
    require("safe_demo_scenario_definition_work_item_closed = true" in V06184.read_text(encoding="utf-8"), "v0.6.184 scenario definition closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (readiness_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.200 Public Demo Readiness Review and Decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
