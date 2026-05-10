from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/209-v06133-request-decision-constraint-diff-enforcement-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0203-add-v06133-request-decision-constraint-diff-enforcement-candidate.md"
ISSUE = ROOT / "planning/issues/0202-add-v06133-request-decision-constraint-diff-enforcement-candidate.md"
HELPER = ROOT / "tools/request_decision_constraint_diff.py"
HELPER_TEST = ROOT / "tools/test_request_decision_constraint_diff_enforcement.py"
V06132_DOC = ROOT / "docs/208-v06132-request-decision-constraint-diff-enforcement-readiness.md"
V06131_DOC = ROOT / "docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 2 of 3 for a High-risk gate-semantics work item.', 'This checkpoint implements the request/decision constraint-diff enforcement candidate.', 'The review and decision are deferred to v0.6.134.', 'Candidate implementation summary', 'Candidate helper', 'Candidate behavior', 'Fail-closed behavior', 'Evidence-safe result model', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision']
FLAGS = ['request_decision_constraint_diff_enforcement_candidate_completed = true', 'request_decision_constraint_diff_enforcement_candidate_is_high_risk = true', 'request_decision_constraint_diff_enforcement_candidate_checkpoint_2_of_3 = true', 'request_decision_constraint_diff_enforcement_readiness_completed = true', 'request_decision_constraint_diff_enforcement_review_decision_deferred_to_v06134 = true', 'constraint_diff_helper_added = true', 'constraint_diff_helper_tests_added = true', 'constraint_diff_candidate_deterministic_comparison_supported = true', 'constraint_diff_candidate_fail_closed_on_tool_action_mismatch = true', 'constraint_diff_candidate_fail_closed_on_target_mismatch = true', 'constraint_diff_candidate_fail_closed_on_destination_binding_mismatch = true', 'constraint_diff_candidate_fail_closed_on_target_mode_mismatch = true', 'constraint_diff_candidate_fail_closed_on_scope_mismatch = true', 'constraint_diff_candidate_fail_closed_on_credential_ref_mismatch = true', 'constraint_diff_candidate_fail_closed_on_execution_mode_mismatch = true', 'constraint_diff_candidate_fail_closed_on_external_discovery_escalation = true', 'constraint_diff_candidate_fail_closed_on_missing_required_request_field = true', 'constraint_diff_candidate_fail_closed_on_missing_required_decision_field = true', 'constraint_diff_candidate_fail_closed_on_malformed_request_constraints = true', 'constraint_diff_candidate_fail_closed_on_malformed_decision_constraints = true', 'constraint_diff_candidate_allows_exact_match_to_continue_existing_checks = true', 'constraint_diff_candidate_evidence_safe_result_model_added = true', 'constraint_diff_enforcement_added = true', 'constraint_diff_behavior_modified = true', 'request_decision_comparison_logic_modified = true', 'authorization_gate_runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'authorization_expiry_now_check_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06132_DOC, V06131_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.133 document missing required text: {phrase}")

    for phrase in [
        "def evaluate_request_decision_constraint_diff(",
        "class RequestDecisionConstraintDiffResult",
        "class ConstraintDiff",
        "def as_evidence(",
        "tool_action_mismatch",
        "target_mismatch",
        "destination_binding_mismatch",
        "target_mode_mismatch",
        "scope_mismatch",
        "credential_ref_mismatch",
        "execution_mode_mismatch",
        "external_discovery_escalation",
        "missing_required_request_field",
        "missing_required_decision_field",
        "malformed_request_constraints",
        "malformed_decision_constraints",
    ]:
        require(phrase in helper_text, f"helper missing required implementation phrase: {phrase}")

    for phrase in [
        "exact request/decision match must continue existing checks",
        "tool_action_mismatch",
        "target_mismatch",
        "destination_binding_mismatch",
        "target_mode_mismatch",
        "scope_mismatch",
        "credential_ref_mismatch",
        "execution_mode_mismatch",
        "external_discovery_escalation",
        "missing_required_request_field",
        "missing_required_decision_field",
        "malformed_request_constraints",
        "malformed_decision_constraints",
        "evidence should not include sensitive material",
    ]:
        require(phrase in helper_test_text, f"helper test missing required case phrase: {phrase}")

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
    }
    decision = {
        "authorized_tool_action": "zap-baseline",
        "authorized_target": "local-lab",
        "target_mode": "localhost_only",
        "authorized_scope": "scope-demo",
        "authorized_execution_mode": "dry_run",
        "external_discovery_allowed": False,
    }

    exact = evaluate_request_decision_constraint_diff(request, decision)
    require(exact.allowed_to_continue is True, "exact helper result must continue existing checks")

    changed = dict(request)
    changed["target"] = "external-target"
    mismatch = evaluate_request_decision_constraint_diff(changed, decision)
    require(mismatch.allowed_to_continue is False, "target mismatch helper result must fail closed")
    require("target_mismatch" in mismatch.diff_categories, "target mismatch category must be recorded")

    external = dict(request)
    external["external_discovery"] = True
    escalation = evaluate_request_decision_constraint_diff(external, decision)
    require(escalation.allowed_to_continue is False, "external discovery escalation must fail closed")
    require("external_discovery_escalation" in escalation.diff_categories, "external discovery escalation category must be recorded")

    evidence = mismatch.as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["secret", "password", "token", "scanner_output", "customer", "external-target"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")

    v06132 = V06132_DOC.read_text(encoding="utf-8")
    for phrase in [
        "request_decision_constraint_diff_enforcement_readiness_completed = true",
        "request_decision_constraint_diff_enforcement_candidate_deferred_to_v06133 = true",
        "tool_action_mismatch",
        "target_mismatch",
        "credential_ref_mismatch",
        "external_discovery_escalation",
        "ambiguous_constraint_comparison",
    ]:
        require(phrase in v06132, f"v0.6.132 readiness missing required phrase: {phrase}")

    v06131 = V06131_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = request_decision_constraint_diff_enforcement" in v06131, "v0.6.131 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06131, "v0.6.131 high-risk selection must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.133 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.133 request/decision constraint-diff enforcement candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
