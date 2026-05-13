from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLARITY = ROOT / "docs/repository-landing-demo-path-clarity.md"
DOC = ROOT / "docs/272-v06196-repository-landing-demo-path-clarity-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0266-add-v06196-repository-landing-demo-path-clarity-candidate.md"
ISSUE = ROOT / "planning/issues/0265-add-v06196-repository-landing-demo-path-clarity-candidate.md"
README = ROOT / "README.md"
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
V06192 = ROOT / "docs/268-v06192-safe-demo-fixture-set-creation-readiness-review.md"
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06120 = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_COMMON = ['docs/examples/safe-demo/blocked-tool-action-request-review/', 'request.fixture.json', 'gate-decision.fixture.json', 'non-execution-result.fixture.json', 'evidence-trace.fixture.json', 'reviewer-walkthrough.md', 'AI output did not become authority.', 'The gate decision controlled execution.', 'Execution was not permitted.', 'Execution did not occur.', 'not a scanner', 'not an executable demo', 'not a public demo', 'not PoC readiness', 'not authorization to test third-party systems', 'docs/270-v06194-safe-demo-fixture-set-review-and-decision.md']
FLAGS = ['repository_landing_demo_path_clarity_candidate_completed = true', 'repository_landing_demo_path_clarity_candidate_is_medium_risk = true', 'repository_landing_demo_path_clarity_candidate_checkpoint_1_of_2 = true', 'repository_landing_demo_path_clarity_review_decision_deferred_to_v06197 = true', 'repository_landing_demo_path_clarity_created = true', 'repository_landing_demo_path_clarity_status = draft_candidate', 'repository_landing_demo_path_clarity_is_documentation_only = true', 'repository_landing_demo_path_clarity_readme_entry_added = true', 'repository_landing_demo_path_clarity_references_accepted_fixture_set = true', 'repository_landing_demo_path_clarity_references_v06194_review_decision = true', 'repository_landing_demo_path_clarity_explains_demo_review_path = true', 'repository_landing_demo_path_clarity_preserves_non_execution_boundary = true', 'safe_demo_fixture_set_creation_work_item_closed = true', 'safe_demo_fixture_set_status = accepted', 'safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review', 'safe_demo_fixture_set_is_static = true', 'safe_demo_fixture_set_is_mock = true', 'safe_demo_fixture_set_is_non_execution = true', 'safe_demo_fixture_set_is_reviewer_facing = true', 'commercial_inquiry_response_boundary_deferred = true', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'additional_fixture_files_created = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'sensitive_value_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.197 Repository Landing and Demo Path Clarity Review and Decision']
FORBIDDEN = ['repository landing and demo path clarity is accepted in this checkpoint', 'repository landing and demo path clarity work item is closed', 'new fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'sensitive value injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'audit opinion provided', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [CLARITY, DOC, ADR, ISSUE, README, V06195, V06194, V06193, FIXTURE_DIR, *FIXTURE_FILES, V06192, V06190, V06181, V06172, V06120, V06119]:
        require(path.exists(), f"missing required path: {path.relative_to(ROOT)}")

    clarity_text = CLARITY.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")

    for phrase in REQUIRED_COMMON:
        require(phrase in clarity_text, f"clarity document missing required text: {phrase}")
        require(phrase in readme_text, f"README missing landing/demo path clarity text: {phrase}")

    for phrase in FLAGS:
        require(phrase in doc_text, f"v0.6.196 document missing flag: {phrase}")

    for phrase in [
        "Status: candidate",
        "This checkpoint is checkpoint 1 of 2 for the Medium-risk Repository Landing and Demo Path Clarity work item.",
        "This checkpoint creates the Repository Landing and Demo Path Clarity candidate.",
        "The review and decision are deferred to v0.6.197.",
        "This checkpoint updates README landing navigation.",
        "This checkpoint does not create new fixture files.",
        "This checkpoint does not create public samples.",
        "This checkpoint does not create a safe demo.",
        "This checkpoint does not create a public demo.",
        "This checkpoint does not create an executable demo.",
        "Candidate artifact",
        "README landing entry",
        "Accepted fixture set reference",
        "Review path",
        "Boundary statements",
        "Candidate record",
        "What did not happen",
        "Next checkpoint",
    ]:
        require(phrase in doc_text, f"v0.6.196 document missing required text: {phrase}")

    v06195 = V06195.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06195_completed = true",
        "selected_next_work_item = repository_landing_demo_path_clarity",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.196 Repository Landing and Demo Path Clarity Candidate",
        "selected_followup_checkpoint = v0.6.197 Repository Landing and Demo Path Clarity Review and Decision",
    ]:
        require(phrase in v06195, f"v0.6.195 selection missing required phrase: {phrase}")

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
    ]:
        require(phrase in v06194, f"v0.6.194 closeout missing required phrase: {phrase}")

    require("safe_demo_fixture_set_candidate_completed = true" in V06193.read_text(encoding="utf-8"), "v0.6.193 candidate must remain recorded")
    require("safe_demo_fixture_set_creation_readiness_review_completed = true" in V06192.read_text(encoding="utf-8"), "v0.6.192 readiness review must remain recorded")
    require("safe_demo_fixture_set_planning_work_item_closed = true" in V06190.read_text(encoding="utf-8"), "v0.6.190 fixture planning closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("risk_tiered_granularity_adopted = true" in V06120.read_text(encoding="utf-8"), "v0.6.120 policy must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (clarity_text + "\n" + doc_text + "\n" + readme_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.196 Repository Landing and Demo Path Clarity candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
