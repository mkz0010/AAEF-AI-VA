from __future__ import annotations

from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/205-v06129-authorization-expiry-current-time-check-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0199-add-v06129-authorization-expiry-current-time-check-candidate.md"
ISSUE = ROOT / "planning/issues/0198-add-v06129-authorization-expiry-current-time-check-candidate.md"
HELPER = ROOT / "tools/authorization_expiry_current_time.py"
HELPER_TEST = ROOT / "tools/test_authorization_expiry_current_time_check.py"
V06128_DOC = ROOT / "docs/204-v06128-authorization-expiry-current-time-check-readiness.md"
V06127_DOC = ROOT / "docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 2 of 3 for a High-risk gate-semantics work item.', 'This checkpoint implements the authorization expiry current-time check candidate.', 'The review and decision are deferred to v0.6.130.', 'Candidate implementation summary', 'Candidate helper', 'Candidate behavior', 'Fail-closed behavior', 'Deterministic current-time source', 'Evidence-safe result model', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.130 Authorization Expiry Current-Time Check Review and Decision']
FLAGS = ['authorization_expiry_current_time_check_candidate_completed = true', 'authorization_expiry_current_time_check_candidate_is_high_risk = true', 'authorization_expiry_current_time_check_candidate_checkpoint_2_of_3 = true', 'authorization_expiry_current_time_check_readiness_completed = true', 'authorization_expiry_current_time_check_review_decision_deferred_to_v06130 = true', 'authorization_expiry_current_time_helper_added = true', 'authorization_expiry_current_time_helper_tests_added = true', 'authorization_expiry_candidate_deterministic_current_time_supported = true', 'authorization_expiry_candidate_fail_closed_on_expired = true', 'authorization_expiry_candidate_fail_closed_on_malformed_expiry = true', 'authorization_expiry_candidate_fail_closed_on_missing_required_expiry = true', 'authorization_expiry_candidate_fail_closed_on_timezone_naive_expiry = true', 'authorization_expiry_candidate_fail_closed_on_timezone_naive_current_time = true', 'authorization_expiry_candidate_allows_not_expired_to_continue_existing_checks = true', 'authorization_expiry_candidate_equal_boundary_treated_as_not_expired = true', 'authorization_expiry_candidate_evidence_safe_result_model_added = true', 'authorization_expiry_behavior_modified = true', 'authorization_validation_logic_modified = true', 'authorization_gate_runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.130 Authorization Expiry Current-Time Check Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06128_DOC, V06127_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.129 document missing required text: {phrase}")

    for phrase in [
        "def evaluate_authorization_expiry(",
        "class AuthorizationExpiryDecision",
        "def as_evidence(",
        "current_time",
        "expiry_required",
        "authorization_expired",
        "missing_required_expiry",
        "malformed_expiry",
        "ambiguous_current_time",
        "current_time_before_or_equal_expiry",
        "current_time_after_expiry",
    ]:
        require(phrase in helper_text, f"helper missing required implementation phrase: {phrase}")

    for phrase in [
        "not expired authorization must continue existing checks",
        "expiry equal to current time must be deterministic and not expired",
        "expired authorization must fail closed",
        "malformed expiry must fail closed",
        "missing required expiry must fail closed",
        "timezone-naive expiry must fail closed",
        "timezone-naive current_time must fail closed",
        "evidence should not include sensitive term",
    ]:
        require(phrase in helper_test_text, f"helper test missing required case phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from authorization_expiry_current_time import evaluate_authorization_expiry

    fixed_now = datetime(2026, 5, 10, 12, 0, 0, tzinfo=timezone.utc)
    expired = evaluate_authorization_expiry({"expires_at": "2026-05-10T11:59:59Z"}, current_time=fixed_now, expiry_required=True)
    require(expired.allowed_to_continue is False, "expired helper result must fail closed")
    require(expired.reason == "authorization_expired", "expired helper reason mismatch")

    valid = evaluate_authorization_expiry({"expires_at": "2026-05-10T12:00:00Z"}, current_time=fixed_now, expiry_required=True)
    require(valid.allowed_to_continue is True, "equal boundary helper result must continue existing checks")

    malformed = evaluate_authorization_expiry({"expires_at": "not-a-time"}, current_time=fixed_now, expiry_required=True)
    require(malformed.allowed_to_continue is False, "malformed helper result must fail closed")

    missing = evaluate_authorization_expiry({}, current_time=fixed_now, expiry_required=True)
    require(missing.allowed_to_continue is False, "missing required expiry helper result must fail closed")

    v06128 = V06128_DOC.read_text(encoding="utf-8")
    for phrase in [
        "authorization_expiry_current_time_check_readiness_completed = true",
        "authorization_expiry_current_time_check_candidate_deferred_to_v06129 = true",
        "expired_authorization -> blocked / not authorized",
        "malformed_expiry -> blocked / not authorized",
        "missing_required_expiry -> blocked / not authorized",
        "ambiguous_current_time -> blocked / not authorized",
    ]:
        require(phrase in v06128, f"v0.6.128 readiness missing required phrase: {phrase}")

    v06127 = V06127_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = authorization_expiry_current_time_check" in v06127, "v0.6.127 selection must remain recorded")
    require("selected_next_work_item_risk_tier = high" in v06127, "v0.6.127 high-risk selection must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.129 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.129 authorization expiry current-time check candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
