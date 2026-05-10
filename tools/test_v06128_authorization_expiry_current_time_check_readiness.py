from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/204-v06128-authorization-expiry-current-time-check-readiness.md"
ADR = ROOT / "planning/decisions/ADR-0198-add-v06128-authorization-expiry-current-time-check-readiness.md"
ISSUE = ROOT / "planning/issues/0197-add-v06128-authorization-expiry-current-time-check-readiness.md"
V06127_DOC = ROOT / "docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md"
V06126_DOC = ROOT / "docs/202-v06126-security-reporting-channel-consistency-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: readiness', 'This is checkpoint 1 of 3 for a High-risk gate-semantics work item.', 'This checkpoint prepares authorization expiry current-time check readiness.', 'The candidate implementation is deferred to v0.6.129.', 'The review and decision are deferred to v0.6.130.', 'This checkpoint does not implement the authorization expiry current-time check.', 'This checkpoint does not modify authorization behavior.', 'This checkpoint does not modify runtime behavior.', 'Readiness target discovery', 'Expected candidate behavior', 'Expected tests to add or update', 'Fail-closed boundary', 'Current-time source boundary', 'Non-goals', 'What did not happen', 'Next checkpoint', 'v0.6.129 Authorization Expiry Current-Time Check Candidate']
FLAGS = ['authorization_expiry_current_time_check_readiness_completed = true', 'authorization_expiry_current_time_check_readiness_is_high_risk = true', 'authorization_expiry_current_time_check_readiness_checkpoint_1_of_3 = true', 'authorization_expiry_current_time_check_candidate_deferred_to_v06129 = true', 'authorization_expiry_current_time_check_review_decision_deferred_to_v06130 = true', 'authorization_expiry_current_time_check_readiness_documentation_only = true', 'authorization_expiry_current_time_check_readiness_identifies_target_discovery = true', 'authorization_expiry_current_time_check_readiness_identifies_expected_behavior = true', 'authorization_expiry_current_time_check_readiness_identifies_tests_to_add_or_update = true', 'authorization_expiry_current_time_check_readiness_identifies_fail_closed_boundary = true', 'authorization_expiry_current_time_check_readiness_identifies_non_goals = true', 'authorization_expiry_now_check_added = false', 'authorization_expiry_behavior_modified = false', 'authorization_validation_logic_modified = false', 'authorization_gate_runtime_behavior_modified = false', 'current_time_source_implemented = false', 'expired_authorization_fail_closed_behavior_implemented = false', 'candidate_implementation_started = false', 'review_decision_completed = false', 'security_reporting_channel_consistency_work_item_closed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.129 Authorization Expiry Current-Time Check Candidate']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06127_DOC, V06126_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.128 document missing required text: {phrase}")

    for phrase in [
        "expired_authorization -> blocked / not authorized",
        "malformed_expiry -> blocked / not authorized",
        "missing_required_expiry -> blocked / not authorized",
        "ambiguous_current_time -> blocked / not authorized",
        "v0.6.129 Authorization Expiry Current-Time Check Candidate",
    ]:
        require(phrase in doc_text, f"v0.6.128 readiness missing fail-closed or next-checkpoint phrase: {phrase}")

    v06127 = V06127_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = authorization_expiry_current_time_check",
        "selected_next_work_item_risk_tier = high",
        "selected_next_work_item_checkpoint_count = 3",
        "selected_next_checkpoint = v0.6.128 Authorization Expiry Current-Time Check Readiness",
        "authorization_expiry_now_check_added = false",
        "authorization_expiry_behavior_modified = false",
    ]:
        require(phrase in v06127, f"v0.6.127 selection missing required phrase: {phrase}")

    v06126 = V06126_DOC.read_text(encoding="utf-8")
    require("security_reporting_channel_consistency_work_item_closed = true" in v06126, "v0.6.126 SECURITY work item must be closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checkpoint implements the authorization expiry current-time check",
        "this checkpoint modifies authorization behavior",
        "this checkpoint modifies runtime behavior",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.128 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.128 authorization expiry current-time check readiness tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
