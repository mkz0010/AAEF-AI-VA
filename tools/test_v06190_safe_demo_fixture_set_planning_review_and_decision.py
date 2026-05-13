from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/safe-demo-fixture-set-planning.md"
DOC = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0260-add-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0259-add-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
V06189 = ROOT / "docs/265-v06189-safe-demo-fixture-set-planning-candidate.md"
V06188 = ROOT / "docs/264-v06188-next-work-selection-using-risk-tiered-granularity.md"
V06187 = ROOT / "docs/263-v06187-safe-demo-artifact-planning-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06179 = ROOT / "docs/255-v06179-public-demo-positioning-review-and-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['safe_demo_fixture_set_planning_review_decision_completed = true', 'safe_demo_fixture_set_planning_review_decision_is_medium_risk = true', 'safe_demo_fixture_set_planning_review_decision_checkpoint_2_of_2 = true', 'safe_demo_fixture_set_planning_candidate_reviewed = true', 'safe_demo_fixture_set_planning_candidate_accepted = true', 'safe_demo_fixture_set_planning_work_item_closed = true', 'safe_demo_fixture_set_planning_status = accepted', 'fixture_inventory_accepted = true', 'fixture_file_boundary_accepted = true', 'request_fixture_boundary_accepted = true', 'gate_decision_fixture_boundary_accepted = true', 'non_execution_result_fixture_boundary_accepted = true', 'evidence_trace_fixture_boundary_accepted = true', 'reviewer_walkthrough_boundary_accepted = true', 'static_validation_expectations_accepted = true', 'file_naming_expectations_accepted = true', 'public_private_fixture_distinction_accepted = true', 'fixture_creation_sequence_accepted = true', 'fixture_files_created = false', 'public_samples_created = false', 'actual_fixture_creation_deferred = true', 'safe_demo_artifact_creation_deferred = true', 'executable_demo_creation_deferred = true', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.191 Next Work Selection Using Risk-Tiered Granularity']
PLAN_REQUIRED = ['# Safe Demo Fixture Set Planning', 'Status: draft_candidate', 'Fixture inventory', 'Fixture file boundary', 'Request fixture boundary', 'Gate decision fixture boundary', 'Non-execution result fixture boundary', 'Evidence trace fixture boundary', 'Reviewer walkthrough boundary', 'Static validation expectations', 'File naming expectations', 'Public and private fixture distinction', 'Future fixture creation sequence', 'Fixtures intentionally not created yet', 'v0.6.190 Safe Demo Fixture Set Planning Review and Decision']
REVIEW_REQUIRED = ['Status: decision', 'This checkpoint reviews the Safe Demo Fixture Set Planning candidate added in v0.6.189.', 'This is checkpoint 2 of 2 for a Medium-risk safe-demo fixture-set-planning work item.', 'This checkpoint reviews and accepts the Safe Demo Fixture Set Planning candidate.', 'The Safe Demo Fixture Set Planning work item is closed.', 'Candidate accepted.', 'docs/safe-demo-fixture-set-planning.md', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_fixture_set_planning_candidate_accepted = true', 'safe_demo_fixture_set_planning_work_item_closed = true', 'Review checklist', 'Work item closeout', 'v0.6.189 Safe Demo Fixture Set Planning Candidate', 'v0.6.190 Safe Demo Fixture Set Planning Review and Decision', 'v0.6.191 Next Work Selection Using Risk-Tiered Granularity']
FORBIDDEN = ['fixture files are created in this checkpoint', 'public samples are created in this checkpoint', 'safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'aaef main contact publication completed', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'audit opinion provided', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [PLAN, DOC, ADR, ISSUE, V06189, V06188, V06187, V06181, V06179, V06172, V06119]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    plan_text = PLAN.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in PLAN_REQUIRED:
        require(phrase in plan_text, f"safe demo fixture set planning missing required phrase: {phrase}")
    for phrase in REVIEW_REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.190 review/decision document missing required phrase: {phrase}")

    v06189 = V06189.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_planning_candidate_completed = true",
        "safe_demo_fixture_set_planning_created = true",
        "safe_demo_fixture_set_planning_status = draft_candidate",
        "safe_demo_fixture_set_planning_review_decision_deferred_to_v06190 = true",
        "fixture_inventory_defined = true",
        "request_fixture_boundary_defined = true",
        "gate_decision_fixture_boundary_defined = true",
        "non_execution_result_fixture_boundary_defined = true",
        "evidence_trace_fixture_boundary_defined = true",
        "selected_next_checkpoint = v0.6.190 Safe Demo Fixture Set Planning Review and Decision",
    ]:
        require(phrase in v06189, f"v0.6.189 candidate missing required phrase: {phrase}")

    v06188 = V06188.read_text(encoding="utf-8")
    for phrase in [
        "next_work_selection_using_risk_tiered_granularity_v06188_completed = true",
        "selected_next_work_item = safe_demo_fixture_set_planning",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
    ]:
        require(phrase in v06188, f"v0.6.188 selection missing required phrase: {phrase}")

    v06187 = V06187.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_artifact_planning_review_decision_completed = true",
        "safe_demo_artifact_planning_candidate_accepted = true",
        "safe_demo_artifact_planning_work_item_closed = true",
        "safe_demo_artifact_planning_status = accepted",
    ]:
        require(phrase in v06187, f"v0.6.187 closeout missing required phrase: {phrase}")

    v06181 = V06181.read_text(encoding="utf-8")
    for phrase in [
        "commercial_inquiry_response_boundary_deferral_decision_completed = true",
        "commercial_inquiry_response_boundary_deferred = true",
        "commercial_inquiry_response_template_deferred = true",
    ]:
        require(phrase in v06181, f"v0.6.181 deferral missing required phrase: {phrase}")

    require("public_demo_positioning_work_item_closed = true" in V06179.read_text(encoding="utf-8"), "v0.6.179 public demo positioning closeout must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    combined_lower = (plan_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    print("v0.6.190 Safe Demo Fixture Set Planning review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
