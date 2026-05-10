from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0200-add-v06130-authorization-expiry-current-time-check-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0199-add-v06130-authorization-expiry-current-time-check-review-and-decision.md"
HELPER = ROOT / "tools/authorization_expiry_current_time.py"
HELPER_TEST = ROOT / "tools/test_authorization_expiry_current_time_check.py"
V06129_DOC = ROOT / "docs/205-v06129-authorization-expiry-current-time-check-candidate.md"
V06128_DOC = ROOT / "docs/204-v06128-authorization-expiry-current-time-check-readiness.md"
V06127_DOC = ROOT / "docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 3 of 3 for a High-risk gate-semantics work item.', 'This checkpoint reviews and accepts the authorization expiry current-time check candidate from v0.6.129.', 'The authorization expiry current-time check work item is closed.', 'Review conclusion', 'Candidate accepted', 'Deterministic current-time source confirmed', 'Fail-closed behavior confirmed', 'Evidence-safe result model confirmed', 'No runtime execution authorization effect', 'No scanner execution authorization effect', 'No Docker execution authorization effect', 'No credential injection authorization effect', 'No customer target authorization effect', 'No delivery authorization effect', 'Reviewed candidate behavior', 'Reviewed helper and tests', 'Review checklist', 'What did not happen', 'Next direction', 'v0.6.131 Next Work Selection Using Risk-Tiered Granularity']
FLAGS = ['authorization_expiry_current_time_check_review_decision_completed = true', 'authorization_expiry_current_time_check_review_decision_is_high_risk = true', 'authorization_expiry_current_time_check_review_decision_checkpoint_3_of_3 = true', 'authorization_expiry_current_time_check_candidate_reviewed = true', 'authorization_expiry_current_time_check_candidate_accepted = true', 'authorization_expiry_current_time_check_work_item_closed = true', 'authorization_expiry_current_time_helper_reviewed = true', 'authorization_expiry_current_time_helper_tests_reviewed = true', 'authorization_expiry_current_time_deterministic_current_time_confirmed = true', 'authorization_expiry_current_time_fail_closed_expired_confirmed = true', 'authorization_expiry_current_time_fail_closed_malformed_confirmed = true', 'authorization_expiry_current_time_fail_closed_missing_required_confirmed = true', 'authorization_expiry_current_time_fail_closed_timezone_naive_expiry_confirmed = true', 'authorization_expiry_current_time_fail_closed_timezone_naive_current_time_confirmed = true', 'authorization_expiry_current_time_not_expired_continue_existing_checks_confirmed = true', 'authorization_expiry_current_time_equal_boundary_continue_existing_checks_confirmed = true', 'authorization_expiry_current_time_evidence_safe_result_confirmed = true', 'authorization_expiry_behavior_modified = true', 'authorization_validation_logic_modified = true', 'authorization_gate_runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.131 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_HELPER_PHRASES = ['def evaluate_authorization_expiry(', 'class AuthorizationExpiryDecision', 'def as_evidence(', 'current_time', 'expiry_required', 'authorization_expired', 'missing_required_expiry', 'malformed_expiry', 'ambiguous_current_time', 'current_time_before_or_equal_expiry', 'current_time_after_expiry']
REQUIRED_HELPER_TEST_PHRASES = ['not expired authorization must continue existing checks', 'expiry equal to current time must be deterministic and not expired', 'expired authorization must fail closed', 'malformed expiry must fail closed', 'missing required expiry must fail closed', 'timezone-naive expiry must fail closed', 'timezone-naive current_time must fail closed', 'evidence should not include sensitive term']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06129_DOC, V06128_DOC, V06127_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.130 document missing required text: {phrase}")

    for phrase in REQUIRED_HELPER_PHRASES:
        require(phrase in helper_text, f"helper missing reviewed phrase: {phrase}")

    for phrase in REQUIRED_HELPER_TEST_PHRASES:
        require(phrase in helper_test_text, f"helper test missing reviewed phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from authorization_expiry_current_time import evaluate_authorization_expiry

    fixed_now = datetime(2026, 5, 10, 12, 0, 0, tzinfo=timezone.utc)

    cases = [
        ("expired", {"expires_at": "2026-05-10T11:59:59Z"}, False, "authorization_expired"),
        ("malformed", {"expires_at": "not-a-time"}, False, "malformed_expiry:"),
        ("missing_required", {}, False, "missing_required_expiry"),
        ("equal_boundary", {"expires_at": "2026-05-10T12:00:00Z"}, True, "authorization_not_expired"),
        ("not_expired", {"expires_at": "2026-05-10T12:00:01Z"}, True, "authorization_not_expired"),
    ]

    for name, authorization, expected_allowed, expected_reason in cases:
        result = evaluate_authorization_expiry(authorization, current_time=fixed_now, expiry_required=True)
        require(result.allowed_to_continue is expected_allowed, f"{name} allowed_to_continue mismatch")
        if expected_reason.endswith(":"):
            require(result.reason.startswith(expected_reason), f"{name} reason mismatch: {result.reason}")
        else:
            require(result.reason == expected_reason, f"{name} reason mismatch: {result.reason}")

    timezone_naive_expiry = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:01"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(timezone_naive_expiry.allowed_to_continue is False, "timezone-naive expiry must fail closed")

    timezone_naive_now = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:01Z"},
        current_time=datetime(2026, 5, 10, 12, 0, 0),
        expiry_required=True,
    )
    require(timezone_naive_now.allowed_to_continue is False, "timezone-naive current_time must fail closed")

    evidence = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T11:59:59Z"},
        current_time=fixed_now,
        expiry_required=True,
    ).as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["secret", "credential", "token", "scanner_output", "customer", "private artifact"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive term: {term}")

    v06129 = V06129_DOC.read_text(encoding="utf-8")
    for phrase in [
        "authorization_expiry_current_time_check_candidate_completed = true",
        "authorization_expiry_current_time_check_candidate_checkpoint_2_of_3 = true",
        "authorization_expiry_current_time_helper_added = true",
        "authorization_expiry_current_time_helper_tests_added = true",
        "selected_next_checkpoint = v0.6.130 Authorization Expiry Current-Time Check Review and Decision",
    ]:
        require(phrase in v06129, f"v0.6.129 candidate missing required phrase: {phrase}")

    v06128 = V06128_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_readiness_completed = true" in v06128, "v0.6.128 readiness must remain recorded")

    v06127 = V06127_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = authorization_expiry_current_time_check" in v06127, "v0.6.127 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06127, "v0.6.127 high-risk selection must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.130 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.130 authorization expiry current-time check review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
