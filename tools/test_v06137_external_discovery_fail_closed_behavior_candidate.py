from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/213-v06137-external-discovery-fail-closed-behavior-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0207-add-v06137-external-discovery-fail-closed-behavior-candidate.md"
ISSUE = ROOT / "planning/issues/0206-add-v06137-external-discovery-fail-closed-behavior-candidate.md"
HELPER = ROOT / "tools/external_discovery_fail_closed.py"
HELPER_TEST = ROOT / "tools/test_external_discovery_fail_closed_behavior.py"
V06136_DOC = ROOT / "docs/212-v06136-external-discovery-fail-closed-behavior-readiness.md"
V06135_DOC = ROOT / "docs/211-v06135-next-work-selection-using-risk-tiered-granularity.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 2 of 3 for a High-risk gate-semantics work item.', 'This checkpoint implements the external_discovery=true fail-closed behavior candidate.', 'The review and decision are deferred to v0.6.138.', 'Candidate implementation summary', 'Candidate helper', 'Candidate behavior', 'Fail-closed behavior', 'Evidence-safe result model', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.138 External Discovery Fail-Closed Behavior Review and Decision']
FLAGS = ['external_discovery_fail_closed_behavior_candidate_completed = true', 'external_discovery_fail_closed_behavior_candidate_is_high_risk = true', 'external_discovery_fail_closed_behavior_candidate_checkpoint_2_of_3 = true', 'external_discovery_fail_closed_behavior_readiness_completed = true', 'external_discovery_fail_closed_behavior_review_decision_deferred_to_v06138 = true', 'external_discovery_fail_closed_helper_added = true', 'external_discovery_fail_closed_helper_tests_added = true', 'external_discovery_candidate_deterministic_comparison_supported = true', 'external_discovery_candidate_fail_closed_without_decision_allowance = true', 'external_discovery_candidate_fail_closed_decision_allowance_false = true', 'external_discovery_candidate_fail_closed_localhost_only_boundary = true', 'external_discovery_candidate_fail_closed_local_lab_only_boundary = true', 'external_discovery_candidate_fail_closed_missing_destination_binding = true', 'external_discovery_candidate_fail_closed_malformed_destination_binding = true', 'external_discovery_candidate_fail_closed_missing_scope_support = true', 'external_discovery_candidate_fail_closed_ambiguous_target_boundary = true', 'external_discovery_candidate_fail_closed_expired_or_invalid_authorization = true', 'external_discovery_candidate_fail_closed_malformed_external_discovery_flag = true', 'external_discovery_candidate_allows_external_false_to_continue_existing_checks = true', 'external_discovery_candidate_allows_explicitly_allowed_boundary_compatible_external = true', 'external_discovery_candidate_evidence_safe_result_model_added = true', 'external_discovery_fail_closed_added = true', 'external_discovery_behavior_modified = true', 'external_discovery_helper_added = true', 'external_discovery_gate_runtime_behavior_modified = false', 'target_boundary_behavior_modified = true', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.138 External Discovery Fail-Closed Behavior Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06136_DOC, V06135_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.137 document missing required text: {phrase}")

    for phrase in [
        "def evaluate_external_discovery_fail_closed(",
        "class ExternalDiscoveryDecision",
        "class ExternalDiscoveryBlock",
        "def as_evidence(",
        "external_discovery_requested_without_decision_allowance",
        "external_discovery_requested_against_localhost_only_boundary",
        "external_discovery_requested_against_local_lab_only_boundary",
        "external_discovery_requested_without_runtime_destination_binding",
        "external_discovery_requested_with_malformed_destination_binding",
        "external_discovery_requested_without_scope_support",
        "external_discovery_requested_with_ambiguous_target_boundary",
        "external_discovery_requested_with_expired_or_invalid_authorization",
        "malformed_external_discovery_flag",
        "ambiguous_external_discovery_comparison",
    ]:
        require(phrase in helper_text, f"helper missing required implementation phrase: {phrase}")

    for phrase in [
        "external_discovery=false must continue existing checks",
        "external_discovery missing and not required must continue existing checks",
        "explicitly allowed boundary-compatible external discovery must continue existing checks",
        "external_discovery_requested_without_decision_allowance",
        "external_discovery_requested_against_localhost_only_boundary",
        "external_discovery_requested_against_local_lab_only_boundary",
        "external_discovery_requested_without_runtime_destination_binding",
        "external_discovery_requested_with_malformed_destination_binding",
        "external_discovery_requested_without_scope_support",
        "external_discovery_requested_with_ambiguous_target_boundary",
        "external_discovery_requested_with_expired_or_invalid_authorization",
        "malformed_external_discovery_flag",
        "evidence should not include sensitive material",
    ]:
        require(phrase in helper_test_text, f"helper test missing required case phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from external_discovery_fail_closed import evaluate_external_discovery_fail_closed

    request = {
        "external_discovery": True,
        "runtime_destination_binding": "binding-scoped-external",
        "scope_supports_external_discovery": True,
    }
    decision = {
        "external_discovery_allowed": True,
        "scope_supports_external_discovery": True,
    }
    boundary = {
        "target_mode": "scoped_external",
        "runtime_destination_binding": "binding-scoped-external",
        "scope_supports_external_discovery": True,
    }

    allowed = evaluate_external_discovery_fail_closed(request, decision, target_boundary=boundary)
    require(allowed.allowed_to_continue is True, "allowed external discovery helper result must continue existing checks")

    no_decision = evaluate_external_discovery_fail_closed(request, {}, target_boundary=boundary)
    require(no_decision.allowed_to_continue is False, "missing decision allowance helper result must fail closed")
    require("external_discovery_requested_without_decision_allowance" in no_decision.block_categories, "missing decision allowance category must be recorded")

    localhost = evaluate_external_discovery_fail_closed(request, decision, target_boundary={**boundary, "target_mode": "localhost_only"})
    require(localhost.allowed_to_continue is False, "localhost_only helper result must fail closed")
    require("external_discovery_requested_against_localhost_only_boundary" in localhost.block_categories, "localhost category must be recorded")

    invalid_auth = evaluate_external_discovery_fail_closed(request, decision, target_boundary=boundary, authorization_result={"allowed_to_continue": False, "status": "blocked"})
    require(invalid_auth.allowed_to_continue is False, "invalid authorization helper result must fail closed")
    require("external_discovery_requested_with_expired_or_invalid_authorization" in invalid_auth.block_categories, "invalid auth category must be recorded")

    malformed_flag = evaluate_external_discovery_fail_closed({"external_discovery": "true"}, decision, target_boundary=boundary)
    require(malformed_flag.allowed_to_continue is False, "malformed external_discovery flag must fail closed")
    require("malformed_external_discovery_flag" in malformed_flag.block_categories, "malformed flag category must be recorded")

    evidence = allowed.as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["binding-scoped-external", "secret", "password", "token", "scanner_output", "customer", "third-party-target.example"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")

    v06136 = V06136_DOC.read_text(encoding="utf-8")
    for phrase in [
        "external_discovery_fail_closed_behavior_readiness_completed = true",
        "external_discovery_fail_closed_behavior_candidate_deferred_to_v06137 = true",
        "external_discovery_requested_without_decision_allowance -> blocked / not authorized",
        "external_discovery_requested_against_localhost_only_boundary -> blocked / not authorized",
        "external_discovery_requested_with_ambiguous_target_boundary -> blocked / not authorized",
        "malformed_external_discovery_flag -> blocked / not authorized",
    ]:
        require(phrase in v06136, f"v0.6.136 readiness missing required phrase: {phrase}")

    v06135 = V06135_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = external_discovery_fail_closed_behavior" in v06135, "v0.6.135 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06135, "v0.6.135 high-risk selection must remain recorded")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "runtime execution is authorized by this candidate",
        "scanner execution is authorized by this candidate",
        "credential injection is permitted by this candidate",
        "this candidate opens an aaef main issue",
        "this candidate submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.137 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.137 external discovery fail-closed behavior candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
