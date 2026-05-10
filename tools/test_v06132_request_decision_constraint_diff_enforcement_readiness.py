from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/208-v06132-request-decision-constraint-diff-enforcement-readiness.md"
ADR = ROOT / "planning/decisions/ADR-0202-add-v06132-request-decision-constraint-diff-enforcement-readiness.md"
ISSUE = ROOT / "planning/issues/0201-add-v06132-request-decision-constraint-diff-enforcement-readiness.md"
V06131_DOC = ROOT / "docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: readiness', 'This is checkpoint 1 of 3 for a High-risk gate-semantics work item.', 'This checkpoint prepares request/decision constraint-diff enforcement readiness.', 'The candidate implementation is deferred to v0.6.133.', 'The review and decision are deferred to v0.6.134.', 'This checkpoint does not implement request/decision constraint-diff enforcement.', 'This checkpoint does not modify constraint-diff behavior.', 'This checkpoint does not modify runtime behavior.', 'Readiness target discovery', 'Comparison inputs', 'Expected candidate behavior', 'Diff categories', 'Fail-closed boundary', 'Expected tests to add or update', 'Evidence boundary', 'Non-goals', 'What did not happen', 'Next checkpoint', 'v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate']
FLAGS = ['request_decision_constraint_diff_enforcement_readiness_completed = true', 'request_decision_constraint_diff_enforcement_readiness_is_high_risk = true', 'request_decision_constraint_diff_enforcement_readiness_checkpoint_1_of_3 = true', 'request_decision_constraint_diff_enforcement_candidate_deferred_to_v06133 = true', 'request_decision_constraint_diff_enforcement_review_decision_deferred_to_v06134 = true', 'request_decision_constraint_diff_enforcement_readiness_documentation_only = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_target_discovery = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_comparison_inputs = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_diff_categories = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_fail_closed_boundary = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_tests_to_add_or_update = true', 'request_decision_constraint_diff_enforcement_readiness_identifies_non_goals = true', 'constraint_diff_enforcement_added = false', 'constraint_diff_behavior_modified = false', 'constraint_diff_helper_added = false', 'request_decision_comparison_logic_modified = false', 'authorization_gate_runtime_behavior_modified = false', 'candidate_implementation_started = false', 'review_decision_completed = false', 'authorization_expiry_current_time_check_work_item_closed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'authorization_expiry_now_check_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06131_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.132 document missing required text: {phrase}")

    for phrase in [
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
        "ambiguous_constraint_comparison",
        "request_outside_authorized_tool_action -> blocked / not authorized",
        "request_outside_authorized_target -> blocked / not authorized",
        "request_outside_authorized_scope -> blocked / not authorized",
        "request_outside_authorized_credential_ref -> blocked / not authorized",
        "request_escalates_external_discovery -> blocked / not authorized",
        "v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate",
    ]:
        require(phrase in doc_text, f"v0.6.132 readiness missing expected diff/fail-closed phrase: {phrase}")

    v06131 = V06131_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = request_decision_constraint_diff_enforcement",
        "selected_next_work_item_risk_tier = high",
        "selected_next_work_item_checkpoint_count = 3",
        "selected_next_checkpoint = v0.6.132 Request/Decision Constraint-Diff Enforcement Readiness",
        "constraint_diff_enforcement_added = false",
        "constraint_diff_behavior_modified = false",
    ]:
        require(phrase in v06131, f"v0.6.131 selection missing required phrase: {phrase}")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must be closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checkpoint implements request/decision constraint-diff enforcement",
        "this checkpoint modifies constraint-diff behavior",
        "this checkpoint modifies runtime behavior",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.132 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.132 request/decision constraint-diff enforcement readiness tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
