from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE_DIR = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review"
REQUEST = FIXTURE_DIR / "request.fixture.json"
DECISION = FIXTURE_DIR / "gate-decision.fixture.json"
RESULT = FIXTURE_DIR / "non-execution-result.fixture.json"
TRACE = FIXTURE_DIR / "evidence-trace.fixture.json"
WALKTHROUGH = FIXTURE_DIR / "reviewer-walkthrough.md"
DOC = ROOT / "docs/269-v06193-safe-demo-fixture-set-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0263-add-v06193-safe-demo-fixture-set-candidate.md"
ISSUE = ROOT / "planning/issues/0262-add-v06193-safe-demo-fixture-set-candidate.md"
V06192 = ROOT / "docs/268-v06192-safe-demo-fixture-set-creation-readiness-review.md"
V06191 = ROOT / "docs/267-v06191-next-work-selection-using-risk-tiered-granularity.md"
V06190 = ROOT / "docs/266-v06190-safe-demo-fixture-set-planning-review-and-decision.md"
V06181 = ROOT / "docs/257-v06181-commercial-inquiry-response-boundary-deferral-decision.md"
V06172 = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06119 = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: candidate', 'This checkpoint is checkpoint 2 of 3 for the High-risk Safe Demo Fixture Set Creation work item.', 'This checkpoint creates only static, mock, non-execution fixture candidates within the v0.6.192 readiness scope.', 'The review and decision are deferred to v0.6.194.', 'This checkpoint creates fixture files.', 'This checkpoint does not create public samples.', 'This checkpoint does not create a safe demo.', 'This checkpoint does not create a public demo.', 'This checkpoint does not create an executable demo.', 'Fixture path', 'Fixture files created', 'Request fixture', 'Gate decision fixture', 'Non-execution result fixture', 'Evidence trace fixture', 'Reviewer walkthrough', 'Static fixture consistency', 'Publication boundary', 'Candidate record', 'What did not happen', 'Next checkpoint']
FLAGS = ['safe_demo_fixture_set_candidate_completed = true', 'safe_demo_fixture_set_candidate_is_high_risk = true', 'safe_demo_fixture_set_candidate_checkpoint_2_of_3 = true', 'safe_demo_fixture_set_creation_readiness_review_completed = true', 'safe_demo_fixture_set_creation_readiness_accepted = true', 'safe_demo_fixture_set_review_decision_deferred_to_v06194 = true', 'safe_demo_fixture_set_candidate_created = true', 'safe_demo_fixture_set_status = draft_candidate', 'safe_demo_fixture_set_claim_safe = true', 'safe_demo_fixture_set_is_static = true', 'safe_demo_fixture_set_is_mock = true', 'safe_demo_fixture_set_is_non_execution = true', 'safe_demo_fixture_set_is_reviewer_facing = true', 'safe_demo_fixture_set_supports_accepted_fixture_plan = true', 'safe_demo_fixture_set_supports_accepted_artifact_plan = true', 'safe_demo_fixture_set_supports_accepted_scenario = true', 'safe_demo_fixture_set_path = docs/examples/safe-demo/blocked-tool-action-request-review', 'safe_demo_fixture_set_allowed_file_types_respected = true', 'fixture_set_created = true', 'fixture_files_created = true', 'request_fixture_created = true', 'gate_decision_fixture_created = true', 'non_execution_result_fixture_created = true', 'evidence_trace_fixture_created = true', 'reviewer_walkthrough_created = true', 'request_fixture_static_mock_non_execution = true', 'gate_decision_fixture_blocks_execution = true', 'non_execution_result_fixture_records_no_execution = true', 'evidence_trace_fixture_links_request_decision_result = true', 'reviewer_walkthrough_is_static_documentation = true', 'fixture_identifier_consistency_checked = true', 'fixture_publication_boundary_preserved = true', 'safe_demo_fixture_set_planning_status = accepted', 'safe_demo_artifact_planning_status = accepted', 'safe_demo_scenario_definition_status = accepted', 'safe_demo_scenario_story = blocked_tool_action_request_review', 'safe_demo_scenario_focus = request_gate_evidence_trace', 'safe_demo_scenario_outcome = blocked_or_non_execution_evidence_trace', 'commercial_inquiry_response_boundary_deferred = true', 'commercial_inquiry_response_template_deferred = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'aaef_ai_va_interim_inquiry_route_continues = true', 'aaef_ai_va_interim_inquiry_route = hexroot0010@gmail.com', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'public_samples_created = false', 'safe_demo_created = false', 'public_demo_created = false', 'executable_demo_created = false', 'runtime_scanner_readiness_created = false', 'real_scanner_execution_selected = false', 'runtime_execution_selected = false', 'customer_poc_intake_selected = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.194 Safe Demo Fixture Set Review and Decision']
FORBIDDEN_VALUES = ['http://', 'https://', 'localhost', '127.0.0.1', '0.0.0.0', '192.168.', '10.0.', '172.16.', 'password', 'secret', 'token', 'api_key', 'apikey', 'credential', 'customer', 'client', 'scan command', 'nmap ', 'zap ', 'nuclei ', 'burp ', 'sqlmap', 'exploit', 'payload']
FORBIDDEN_DOC_PHRASES = ['safe demo is created in this checkpoint', 'public demo is created in this checkpoint', 'executable demo is created in this checkpoint', 'runtime work is started in this checkpoint', 'scanner work is started in this checkpoint', 'real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main contact publication completed', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> int:
    for path in [FIXTURE_DIR, REQUEST, DECISION, RESULT, TRACE, WALKTHROUGH, DOC, ADR, ISSUE, V06192, V06191, V06190, V06181, V06172, V06119]:
        require(path.exists(), f"missing required path: {path.relative_to(ROOT)}")

    for path in [REQUEST, DECISION, RESULT, TRACE]:
        require(path.suffix == ".json", f"fixture must be json: {path.relative_to(ROOT)}")
    require(WALKTHROUGH.suffix == ".md", "walkthrough must be markdown")

    request = load_json(REQUEST)
    decision = load_json(DECISION)
    result = load_json(RESULT)
    trace = load_json(TRACE)
    walkthrough = WALKTHROUGH.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.193 document missing required text: {phrase}")

    require(request["fixture_kind"] == "tool_action_request", "request fixture kind mismatch")
    require(request["request_id"] == "demo-request-0001", "request id mismatch")
    require(request["execution_mode"] == "fixture_only_non_execution", "request execution mode must be fixture-only")
    require(request["authority_boundary"]["model_output_is_authority"] is False, "model output must not be authority")
    require(request["authority_boundary"]["requires_gate_decision"] is True, "gate decision must be required")
    require(request["authority_boundary"]["execution_permitted_by_request"] is False, "request must not permit execution")

    require(decision["fixture_kind"] == "gate_decision", "decision fixture kind mismatch")
    require(decision["request_id"] == request["request_id"], "decision must reference request")
    require(decision["decision"] == "blocked", "decision must be blocked")
    require(decision["execution_permitted"] is False, "decision must not permit execution")
    require(decision["execution_occurred"] is False, "decision must record no execution")
    require(decision["authority_boundary"]["dispatch_allowed"] is False, "dispatch must not be allowed")

    require(result["fixture_kind"] == "non_execution_result", "result fixture kind mismatch")
    require(result["request_id"] == request["request_id"], "result must reference request")
    require(result["decision_id"] == decision["decision_id"], "result must reference decision")
    require(result["execution_permitted"] is False, "result must not permit execution")
    require(result["execution_occurred"] is False, "result must record no execution")
    require(result["result_status"] == "non_executed_blocked", "result status mismatch")

    require(trace["fixture_kind"] == "evidence_trace", "trace fixture kind mismatch")
    ids = [step["artifact_id"] for step in trace["chain"]]
    require(request["request_id"] in ids, "trace must include request")
    require(decision["decision_id"] in ids, "trace must include decision")
    require(result["result_id"] in ids, "trace must include result")
    require(trace["review_conclusion"]["model_output_became_authority"] is False, "trace must say model output did not become authority")
    require(trace["review_conclusion"]["gate_decision_controlled_execution"] is True, "trace must say gate controlled execution")
    require(trace["review_conclusion"]["execution_permitted"] is False, "trace must say execution not permitted")
    require(trace["review_conclusion"]["execution_occurred"] is False, "trace must say execution did not occur")

    require("AI output did not become authority." in walkthrough, "walkthrough missing expected conclusion")
    require("not authorization to test third-party systems" in walkthrough, "walkthrough must preserve third-party testing boundary")

    fixture_combined = "\n".join(
        [
            REQUEST.read_text(encoding="utf-8"),
            DECISION.read_text(encoding="utf-8"),
            RESULT.read_text(encoding="utf-8"),
            TRACE.read_text(encoding="utf-8"),
            walkthrough,
        ]
    )
    fixture_lower = fixture_combined.lower()
    for phrase in FORBIDDEN_VALUES:
        require(phrase not in fixture_lower, f"forbidden value found in fixture set: {phrase}")

    combined_lower = (fixture_combined + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_DOC_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06192 = V06192.read_text(encoding="utf-8")
    for phrase in [
        "safe_demo_fixture_set_creation_readiness_review_completed = true",
        "safe_demo_fixture_set_creation_readiness_accepted = true",
        "safe_demo_fixture_set_candidate_allowed_next = true",
        "selected_next_checkpoint = v0.6.193 Safe Demo Fixture Set Candidate",
    ]:
        require(phrase in v06192, f"v0.6.192 readiness review missing required phrase: {phrase}")

    require("selected_next_work_item = safe_demo_fixture_set_creation" in V06191.read_text(encoding="utf-8"), "v0.6.191 selection must remain recorded")
    require("safe_demo_fixture_set_planning_work_item_closed = true" in V06190.read_text(encoding="utf-8"), "v0.6.190 fixture planning closeout must remain recorded")
    require("commercial_inquiry_response_boundary_deferred = true" in V06181.read_text(encoding="utf-8"), "v0.6.181 commercial inquiry deferral must remain recorded")
    require("aaef_main_contact_reflection_deferred = true" in V06172.read_text(encoding="utf-8"), "v0.6.172 AAEF main contact deferral must remain recorded")
    require("aaef_main_handback_sequence_paused = true" in V06119.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    print("v0.6.193 Safe Demo Fixture Set candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
