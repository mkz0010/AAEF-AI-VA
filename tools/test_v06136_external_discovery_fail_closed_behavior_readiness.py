from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/212-v06136-external-discovery-fail-closed-behavior-readiness.md"
ADR = ROOT / "planning/decisions/ADR-0206-add-v06136-external-discovery-fail-closed-behavior-readiness.md"
ISSUE = ROOT / "planning/issues/0205-add-v06136-external-discovery-fail-closed-behavior-readiness.md"
V06135_DOC = ROOT / "docs/211-v06135-next-work-selection-using-risk-tiered-granularity.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: readiness', 'This is checkpoint 1 of 3 for a High-risk gate-semantics work item.', 'This checkpoint prepares external_discovery=true fail-closed behavior readiness.', 'The candidate implementation is deferred to v0.6.137.', 'The review and decision are deferred to v0.6.138.', 'This checkpoint does not implement external_discovery fail-closed behavior.', 'This checkpoint does not modify external_discovery behavior.', 'This checkpoint does not modify runtime behavior.', 'Readiness target discovery', 'Current semantics to inspect', 'Target-boundary inputs', 'Expected candidate behavior', 'Fail-closed boundary', 'Expected tests to add or update', 'Evidence boundary', 'Non-goals', 'What did not happen', 'Next checkpoint', 'v0.6.137 External Discovery Fail-Closed Behavior Candidate']
FLAGS = ['external_discovery_fail_closed_behavior_readiness_completed = true', 'external_discovery_fail_closed_behavior_readiness_is_high_risk = true', 'external_discovery_fail_closed_behavior_readiness_checkpoint_1_of_3 = true', 'external_discovery_fail_closed_behavior_candidate_deferred_to_v06137 = true', 'external_discovery_fail_closed_behavior_review_decision_deferred_to_v06138 = true', 'external_discovery_fail_closed_behavior_readiness_documentation_only = true', 'external_discovery_fail_closed_behavior_readiness_identifies_target_discovery = true', 'external_discovery_fail_closed_behavior_readiness_identifies_current_semantics = true', 'external_discovery_fail_closed_behavior_readiness_identifies_target_boundary_inputs = true', 'external_discovery_fail_closed_behavior_readiness_identifies_expected_behavior = true', 'external_discovery_fail_closed_behavior_readiness_identifies_fail_closed_boundary = true', 'external_discovery_fail_closed_behavior_readiness_identifies_tests_to_add_or_update = true', 'external_discovery_fail_closed_behavior_readiness_identifies_evidence_boundary = true', 'external_discovery_fail_closed_behavior_readiness_identifies_non_goals = true', 'external_discovery_fail_closed_added = false', 'external_discovery_behavior_modified = false', 'external_discovery_helper_added = false', 'external_discovery_gate_runtime_behavior_modified = false', 'target_boundary_behavior_modified = false', 'candidate_implementation_started = false', 'review_decision_completed = false', 'request_decision_constraint_diff_enforcement_work_item_closed = true', 'authorization_expiry_current_time_check_work_item_closed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.137 External Discovery Fail-Closed Behavior Candidate']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06135_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.136 document missing required text: {phrase}")

    for phrase in [
        "external_discovery_requested_without_decision_allowance -> blocked / not authorized",
        "external_discovery_requested_against_localhost_only_boundary -> blocked / not authorized",
        "external_discovery_requested_against_local_lab_only_boundary -> blocked / not authorized",
        "external_discovery_requested_without_runtime_destination_binding -> blocked / not authorized",
        "external_discovery_requested_with_malformed_destination_binding -> blocked / not authorized",
        "external_discovery_requested_without_scope_support -> blocked / not authorized",
        "external_discovery_requested_with_ambiguous_target_boundary -> blocked / not authorized",
        "external_discovery_requested_with_expired_or_invalid_authorization -> blocked / not authorized",
        "malformed_external_discovery_flag -> blocked / not authorized",
        "ambiguous_external_discovery_comparison -> blocked / not authorized",
        "v0.6.137 External Discovery Fail-Closed Behavior Candidate",
    ]:
        require(phrase in doc_text, f"v0.6.136 readiness missing expected fail-closed phrase: {phrase}")

    v06135 = V06135_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = external_discovery_fail_closed_behavior",
        "selected_next_work_item_risk_tier = high",
        "selected_next_work_item_checkpoint_count = 3",
        "selected_next_checkpoint = v0.6.136 External Discovery Fail-Closed Behavior Readiness",
        "external_discovery_fail_closed_added = false",
        "external_discovery_behavior_modified = false",
    ]:
        require(phrase in v06135, f"v0.6.135 selection missing required phrase: {phrase}")

    v06134 = V06134_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_work_item_closed = true" in v06134, "v0.6.134 constraint-diff work item must be closed")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must be closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checkpoint implements external_discovery fail-closed behavior",
        "this checkpoint modifies external_discovery behavior",
        "this checkpoint modifies runtime behavior",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.136 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.136 external discovery fail-closed behavior readiness tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
