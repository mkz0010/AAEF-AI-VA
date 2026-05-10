from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0208-add-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0207-add-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
HELPER = ROOT / "tools/external_discovery_fail_closed.py"
HELPER_TEST = ROOT / "tools/test_external_discovery_fail_closed_behavior.py"
V06137_DOC = ROOT / "docs/213-v06137-external-discovery-fail-closed-behavior-candidate.md"
V06136_DOC = ROOT / "docs/212-v06136-external-discovery-fail-closed-behavior-readiness.md"
V06135_DOC = ROOT / "docs/211-v06135-next-work-selection-using-risk-tiered-granularity.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 3 of 3 for a High-risk gate-semantics work item.', 'This checkpoint reviews and accepts the external_discovery=true fail-closed behavior candidate from v0.6.137.', 'The external_discovery=true fail-closed behavior work item is closed.', 'Review conclusion', 'Candidate accepted', 'Deterministic comparison confirmed', 'Fail-closed behavior confirmed', 'Evidence-safe result model confirmed', 'No runtime gate integration effect', 'No runtime execution authorization effect', 'No scanner execution authorization effect', 'No Docker execution authorization effect', 'No credential injection authorization effect', 'No customer target authorization effect', 'No delivery authorization effect', 'Reviewed candidate behavior', 'Reviewed helper and tests', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.139 Next Work Selection Using Risk-Tiered Granularity']
FLAGS = ['external_discovery_fail_closed_behavior_review_decision_completed = true', 'external_discovery_fail_closed_behavior_review_decision_is_high_risk = true', 'external_discovery_fail_closed_behavior_review_decision_checkpoint_3_of_3 = true', 'external_discovery_fail_closed_behavior_candidate_reviewed = true', 'external_discovery_fail_closed_behavior_candidate_accepted = true', 'external_discovery_fail_closed_behavior_work_item_closed = true', 'external_discovery_fail_closed_helper_reviewed = true', 'external_discovery_fail_closed_helper_tests_reviewed = true', 'external_discovery_deterministic_comparison_confirmed = true', 'external_discovery_fail_closed_without_decision_allowance_confirmed = true', 'external_discovery_fail_closed_decision_allowance_false_confirmed = true', 'external_discovery_fail_closed_localhost_only_boundary_confirmed = true', 'external_discovery_fail_closed_local_lab_only_boundary_confirmed = true', 'external_discovery_fail_closed_missing_destination_binding_confirmed = true', 'external_discovery_fail_closed_malformed_destination_binding_confirmed = true', 'external_discovery_fail_closed_missing_scope_support_confirmed = true', 'external_discovery_fail_closed_ambiguous_target_boundary_confirmed = true', 'external_discovery_fail_closed_expired_or_invalid_authorization_confirmed = true', 'external_discovery_fail_closed_malformed_external_discovery_flag_confirmed = true', 'external_discovery_false_continue_existing_checks_confirmed = true', 'external_discovery_missing_not_required_continue_existing_checks_confirmed = true', 'external_discovery_explicitly_allowed_boundary_compatible_continue_existing_checks_confirmed = true', 'external_discovery_evidence_safe_result_confirmed = true', 'external_discovery_fail_closed_added = true', 'external_discovery_behavior_modified = true', 'external_discovery_helper_added = true', 'external_discovery_gate_runtime_behavior_modified = false', 'target_boundary_behavior_modified = true', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.139 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_HELPER_PHRASES = ['def evaluate_external_discovery_fail_closed(', 'class ExternalDiscoveryDecision', 'class ExternalDiscoveryBlock', 'def as_evidence(', 'external_discovery_requested_without_decision_allowance', 'external_discovery_requested_against_localhost_only_boundary', 'external_discovery_requested_against_local_lab_only_boundary', 'external_discovery_requested_without_runtime_destination_binding', 'external_discovery_requested_with_malformed_destination_binding', 'external_discovery_requested_without_scope_support', 'external_discovery_requested_with_ambiguous_target_boundary', 'external_discovery_requested_with_expired_or_invalid_authorization', 'malformed_external_discovery_flag', 'ambiguous_external_discovery_comparison']
REQUIRED_HELPER_TEST_PHRASES = ['external_discovery=false must continue existing checks', 'external_discovery missing and not required must continue existing checks', 'explicitly allowed boundary-compatible external discovery must continue existing checks', 'external_discovery_requested_without_decision_allowance', 'external_discovery_requested_against_localhost_only_boundary', 'external_discovery_requested_against_local_lab_only_boundary', 'external_discovery_requested_without_runtime_destination_binding', 'external_discovery_requested_with_malformed_destination_binding', 'external_discovery_requested_without_scope_support', 'external_discovery_requested_with_ambiguous_target_boundary', 'external_discovery_requested_with_expired_or_invalid_authorization', 'malformed_external_discovery_flag', 'evidence should not include sensitive material']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06137_DOC, V06136_DOC, V06135_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.138 document missing required text: {phrase}")

    for phrase in REQUIRED_HELPER_PHRASES:
        require(phrase in helper_text, f"helper missing reviewed phrase: {phrase}")

    for phrase in REQUIRED_HELPER_TEST_PHRASES:
        require(phrase in helper_test_text, f"helper test missing reviewed phrase: {phrase}")

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
    require(allowed.allowed_to_continue is True, "explicitly allowed boundary-compatible external discovery must continue existing checks")

    external_false = evaluate_external_discovery_fail_closed({"external_discovery": False}, {}, target_boundary=None)
    require(external_false.allowed_to_continue is True, "external_discovery=false must continue existing checks")

    external_missing = evaluate_external_discovery_fail_closed({}, {}, target_boundary=None)
    require(external_missing.allowed_to_continue is True, "missing/not-required external_discovery must continue existing checks")

    fail_cases = [
        (
            "external_discovery_requested_without_decision_allowance",
            request,
            {},
            boundary,
            None,
        ),
        (
            "external_discovery_requested_without_decision_allowance",
            request,
            {**decision, "external_discovery_allowed": False},
            boundary,
            None,
        ),
        (
            "external_discovery_requested_against_localhost_only_boundary",
            request,
            decision,
            {**boundary, "target_mode": "localhost_only"},
            None,
        ),
        (
            "external_discovery_requested_against_local_lab_only_boundary",
            request,
            decision,
            {**boundary, "target_mode": "local_lab_only"},
            None,
        ),
        (
            "external_discovery_requested_without_runtime_destination_binding",
            {"external_discovery": True, "scope_supports_external_discovery": True},
            {"external_discovery_allowed": True, "scope_supports_external_discovery": True},
            {"target_mode": "scoped_external", "scope_supports_external_discovery": True},
            None,
        ),
        (
            "external_discovery_requested_with_malformed_destination_binding",
            request,
            decision,
            {**boundary, "runtime_destination_binding": ""},
            None,
        ),
        (
            "external_discovery_requested_without_scope_support",
            {"external_discovery": True, "runtime_destination_binding": "binding-scoped-external"},
            {"external_discovery_allowed": True},
            {"target_mode": "scoped_external", "runtime_destination_binding": "binding-scoped-external"},
            None,
        ),
        (
            "external_discovery_requested_with_ambiguous_target_boundary",
            request,
            decision,
            {"runtime_destination_binding": "binding-scoped-external", "scope_supports_external_discovery": True},
            None,
        ),
        (
            "external_discovery_requested_with_expired_or_invalid_authorization",
            request,
            decision,
            boundary,
            {"allowed_to_continue": False, "status": "blocked"},
        ),
    ]

    for category, req, dec, bnd, auth_result in fail_cases:
        result = evaluate_external_discovery_fail_closed(req, dec, target_boundary=bnd, authorization_result=auth_result)
        require(result.allowed_to_continue is False, f"{category} must fail closed")
        require(category in result.block_categories, f"{category} must be recorded")

    malformed = evaluate_external_discovery_fail_closed({"external_discovery": "true"}, decision, target_boundary=boundary)
    require(malformed.allowed_to_continue is False, "malformed external_discovery flag must fail closed")
    require("malformed_external_discovery_flag" in malformed.block_categories, "malformed flag category must be recorded")

    evidence = evaluate_external_discovery_fail_closed(
        {
            "external_discovery": True,
            "runtime_destination_binding": "binding-super-secret",
            "scope_supports_external_discovery": True,
        },
        decision,
        target_boundary={
            "target_mode": "scoped_external",
            "runtime_destination_binding": "binding-super-secret",
            "scope_supports_external_discovery": True,
        },
    ).as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["binding-scoped-external", "binding-super-secret", "secret", "password", "token", "scanner_output", "customer", "third-party-target.example"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")
    require("allowed_to_continue" in evidence, "evidence should include allowed_to_continue")
    require("checked_fields" in evidence, "evidence should include checked_fields")

    v06137 = V06137_DOC.read_text(encoding="utf-8")
    for phrase in [
        "external_discovery_fail_closed_behavior_candidate_completed = true",
        "external_discovery_fail_closed_behavior_candidate_checkpoint_2_of_3 = true",
        "external_discovery_fail_closed_helper_added = true",
        "external_discovery_fail_closed_helper_tests_added = true",
        "selected_next_checkpoint = v0.6.138 External Discovery Fail-Closed Behavior Review and Decision",
    ]:
        require(phrase in v06137, f"v0.6.137 candidate missing required phrase: {phrase}")

    v06136 = V06136_DOC.read_text(encoding="utf-8")
    require("external_discovery_fail_closed_behavior_readiness_completed = true" in v06136, "v0.6.136 readiness must remain recorded")

    v06135 = V06135_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = external_discovery_fail_closed_behavior" in v06135, "v0.6.135 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06135, "v0.6.135 high-risk selection must remain recorded")

    v06134 = V06134_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_work_item_closed = true" in v06134, "v0.6.134 constraint-diff work item must remain closed")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must remain closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "runtime execution is authorized by this review",
        "scanner execution is authorized by this review",
        "credential injection is permitted by this review",
        "this review opens an aaef main issue",
        "this review submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.138 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.138 external discovery fail-closed behavior review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
