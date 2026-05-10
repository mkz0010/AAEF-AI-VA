from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0204-add-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0203-add-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
HELPER = ROOT / "tools/request_decision_constraint_diff.py"
HELPER_TEST = ROOT / "tools/test_request_decision_constraint_diff_enforcement.py"
V06133_DOC = ROOT / "docs/209-v06133-request-decision-constraint-diff-enforcement-candidate.md"
V06132_DOC = ROOT / "docs/208-v06132-request-decision-constraint-diff-enforcement-readiness.md"
V06131_DOC = ROOT / "docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 3 of 3 for a High-risk gate-semantics work item.', 'This checkpoint reviews and accepts the request/decision constraint-diff enforcement candidate from v0.6.133.', 'The request/decision constraint-diff enforcement work item is closed.', 'Review conclusion', 'Candidate accepted', 'Deterministic comparison confirmed', 'Fail-closed behavior confirmed', 'Evidence-safe result model confirmed', 'No runtime gate integration effect', 'No runtime execution authorization effect', 'No scanner execution authorization effect', 'No Docker execution authorization effect', 'No credential injection authorization effect', 'No customer target authorization effect', 'No delivery authorization effect', 'Reviewed candidate behavior', 'Reviewed helper and tests', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.135 Next Work Selection Using Risk-Tiered Granularity']
FLAGS = ['request_decision_constraint_diff_enforcement_review_decision_completed = true', 'request_decision_constraint_diff_enforcement_review_decision_is_high_risk = true', 'request_decision_constraint_diff_enforcement_review_decision_checkpoint_3_of_3 = true', 'request_decision_constraint_diff_enforcement_candidate_reviewed = true', 'request_decision_constraint_diff_enforcement_candidate_accepted = true', 'request_decision_constraint_diff_enforcement_work_item_closed = true', 'constraint_diff_helper_reviewed = true', 'constraint_diff_helper_tests_reviewed = true', 'constraint_diff_deterministic_comparison_confirmed = true', 'constraint_diff_fail_closed_tool_action_mismatch_confirmed = true', 'constraint_diff_fail_closed_target_mismatch_confirmed = true', 'constraint_diff_fail_closed_destination_binding_mismatch_confirmed = true', 'constraint_diff_fail_closed_target_mode_mismatch_confirmed = true', 'constraint_diff_fail_closed_scope_mismatch_confirmed = true', 'constraint_diff_fail_closed_credential_ref_mismatch_confirmed = true', 'constraint_diff_fail_closed_execution_mode_mismatch_confirmed = true', 'constraint_diff_fail_closed_external_discovery_escalation_confirmed = true', 'constraint_diff_fail_closed_missing_required_request_field_confirmed = true', 'constraint_diff_fail_closed_missing_required_decision_field_confirmed = true', 'constraint_diff_fail_closed_malformed_request_constraints_confirmed = true', 'constraint_diff_fail_closed_malformed_decision_constraints_confirmed = true', 'constraint_diff_exact_match_continue_existing_checks_confirmed = true', 'constraint_diff_evidence_safe_result_confirmed = true', 'constraint_diff_enforcement_added = true', 'constraint_diff_behavior_modified = true', 'request_decision_comparison_logic_modified = true', 'authorization_gate_runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'authorization_expiry_now_check_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.135 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_HELPER_PHRASES = ['def evaluate_request_decision_constraint_diff(', 'class RequestDecisionConstraintDiffResult', 'class ConstraintDiff', 'def as_evidence(', 'tool_action_mismatch', 'target_mismatch', 'destination_binding_mismatch', 'target_mode_mismatch', 'scope_mismatch', 'credential_ref_mismatch', 'execution_mode_mismatch', 'external_discovery_escalation', 'missing_required_request_field', 'missing_required_decision_field', 'malformed_request_constraints', 'malformed_decision_constraints']
REQUIRED_HELPER_TEST_PHRASES = ['exact request/decision match must continue existing checks', 'tool_action_mismatch', 'target_mismatch', 'destination_binding_mismatch', 'target_mode_mismatch', 'scope_mismatch', 'credential_ref_mismatch', 'execution_mode_mismatch', 'external_discovery_escalation', 'missing_required_request_field', 'missing_required_decision_field', 'malformed_request_constraints', 'malformed_decision_constraints', 'evidence should not include sensitive material']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06133_DOC, V06132_DOC, V06131_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.134 document missing required text: {phrase}")

    for phrase in REQUIRED_HELPER_PHRASES:
        require(phrase in helper_text, f"helper missing reviewed phrase: {phrase}")

    for phrase in REQUIRED_HELPER_TEST_PHRASES:
        require(phrase in helper_test_text, f"helper test missing reviewed phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from request_decision_constraint_diff import evaluate_request_decision_constraint_diff

    request = {
        "tool_action": "zap-baseline",
        "target": "local-lab",
        "target_mode": "localhost_only",
        "scope_id": "scope-demo",
        "execution_mode": "dry_run",
        "external_discovery": False,
        "destination_binding": "binding-localhost",
        "credential_ref": "credential_ref:demo",
    }
    decision = {
        "authorized_tool_action": "zap-baseline",
        "authorized_target": "local-lab",
        "target_mode": "localhost_only",
        "authorized_scope": "scope-demo",
        "authorized_execution_mode": "dry_run",
        "external_discovery_allowed": False,
        "destination_binding": "binding-localhost",
        "authorized_credential_ref": "credential_ref:demo",
    }

    exact = evaluate_request_decision_constraint_diff(request, decision)
    require(exact.allowed_to_continue is True, "exact request/decision match must continue existing checks")

    diff_cases = [
        ("tool_action_mismatch", {"tool_action": "nmap-scan"}),
        ("target_mismatch", {"target": "external-target"}),
        ("destination_binding_mismatch", {"destination_binding": "binding-external"}),
        ("target_mode_mismatch", {"target_mode": "external"}),
        ("scope_mismatch", {"scope_id": "scope-other"}),
        ("credential_ref_mismatch", {"credential_ref": "credential_ref:other"}),
        ("execution_mode_mismatch", {"execution_mode": "live"}),
        ("external_discovery_escalation", {"external_discovery": True}),
    ]

    for category, update in diff_cases:
        changed = dict(request)
        changed.update(update)
        result = evaluate_request_decision_constraint_diff(changed, decision)
        require(result.allowed_to_continue is False, f"{category} must fail closed")
        require(category in result.diff_categories, f"{category} must be recorded")

    missing_request = dict(request)
    del missing_request["scope_id"]
    missing_request_result = evaluate_request_decision_constraint_diff(missing_request, decision)
    require(missing_request_result.allowed_to_continue is False, "missing required request field must fail closed")
    require("missing_required_request_field" in missing_request_result.diff_categories, "missing request category must be recorded")

    missing_decision = dict(decision)
    del missing_decision["authorized_scope"]
    missing_decision_result = evaluate_request_decision_constraint_diff(request, missing_decision)
    require(missing_decision_result.allowed_to_continue is False, "missing required decision field must fail closed")
    require("missing_required_decision_field" in missing_decision_result.diff_categories, "missing decision category must be recorded")

    malformed_request_result = evaluate_request_decision_constraint_diff("not-a-request", decision)
    require(malformed_request_result.allowed_to_continue is False, "malformed request must fail closed")
    require("malformed_request_constraints" in malformed_request_result.diff_categories, "malformed request category must be recorded")

    malformed_decision_result = evaluate_request_decision_constraint_diff(request, "not-a-decision")
    require(malformed_decision_result.allowed_to_continue is False, "malformed decision must fail closed")
    require("malformed_decision_constraints" in malformed_decision_result.diff_categories, "malformed decision category must be recorded")

    evidence = evaluate_request_decision_constraint_diff(
        {**request, "target": "external-target", "credential_ref": "credential_ref:super-secret"},
        decision,
    ).as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["external-target", "super-secret", "secret", "password", "token", "scanner_output", "customer"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")
    require("target_mismatch" in evidence_text, "evidence should include safe target diff category")
    require("credential_ref_mismatch" in evidence_text, "evidence should include safe credential_ref diff category")

    v06133 = V06133_DOC.read_text(encoding="utf-8")
    for phrase in [
        "request_decision_constraint_diff_enforcement_candidate_completed = true",
        "request_decision_constraint_diff_enforcement_candidate_checkpoint_2_of_3 = true",
        "constraint_diff_helper_added = true",
        "constraint_diff_helper_tests_added = true",
        "selected_next_checkpoint = v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision",
    ]:
        require(phrase in v06133, f"v0.6.133 candidate missing required phrase: {phrase}")

    v06132 = V06132_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_readiness_completed = true" in v06132, "v0.6.132 readiness must remain recorded")

    v06131 = V06131_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = request_decision_constraint_diff_enforcement" in v06131, "v0.6.131 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06131, "v0.6.131 high-risk selection must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.134 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.134 request/decision constraint-diff enforcement review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
