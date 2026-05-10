from __future__ import annotations

from datetime import datetime, timezone

from authorization_expiry_current_time import evaluate_authorization_expiry


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    fixed_now = datetime(2026, 5, 10, 12, 0, 0, tzinfo=timezone.utc)

    not_expired = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:01Z"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(not_expired.allowed_to_continue is True, "not expired authorization must continue existing checks")
    require(not_expired.status == "continue_existing_checks", "not expired status must continue")
    require(not_expired.reason == "authorization_not_expired", "not expired reason mismatch")
    require(not_expired.expired is False, "not expired flag mismatch")
    require(not_expired.comparison == "current_time_before_or_equal_expiry", "not expired comparison mismatch")

    equal_boundary = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:00+00:00"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(equal_boundary.allowed_to_continue is True, "expiry equal to current time must be deterministic and not expired")
    require(equal_boundary.reason == "authorization_not_expired", "equal boundary reason mismatch")

    expired = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T11:59:59Z"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(expired.allowed_to_continue is False, "expired authorization must fail closed")
    require(expired.status == "blocked", "expired status must be blocked")
    require(expired.reason == "authorization_expired", "expired reason mismatch")
    require(expired.expired is True, "expired flag mismatch")
    require(expired.comparison == "current_time_after_expiry", "expired comparison mismatch")

    malformed = evaluate_authorization_expiry(
        {"expires_at": "not-a-time"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(malformed.allowed_to_continue is False, "malformed expiry must fail closed")
    require(malformed.status == "blocked", "malformed status must be blocked")
    require(malformed.reason.startswith("malformed_expiry:"), "malformed reason mismatch")

    missing_required = evaluate_authorization_expiry(
        {"scope": "demo"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(missing_required.allowed_to_continue is False, "missing required expiry must fail closed")
    require(missing_required.reason == "missing_required_expiry", "missing required reason mismatch")

    missing_optional = evaluate_authorization_expiry(
        {"scope": "demo"},
        current_time=fixed_now,
        expiry_required=False,
    )
    require(missing_optional.allowed_to_continue is True, "missing optional expiry should continue existing checks")
    require(missing_optional.reason == "expiry_not_present_not_required", "missing optional reason mismatch")

    timezone_aware_offset = evaluate_authorization_expiry(
        {"valid_until": "2026-05-10T21:00:01+09:00"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(timezone_aware_offset.allowed_to_continue is True, "timezone-aware offset expiry should compare deterministically")
    require(timezone_aware_offset.expiry_field == "valid_until", "valid_until field should be reported")

    timezone_naive_expiry = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:01"},
        current_time=fixed_now,
        expiry_required=True,
    )
    require(timezone_naive_expiry.allowed_to_continue is False, "timezone-naive expiry must fail closed")
    require(timezone_naive_expiry.reason.startswith("malformed_expiry:"), "timezone-naive expiry reason mismatch")

    timezone_naive_now = evaluate_authorization_expiry(
        {"expires_at": "2026-05-10T12:00:01Z"},
        current_time=datetime(2026, 5, 10, 12, 0, 0),
        expiry_required=True,
    )
    require(timezone_naive_now.allowed_to_continue is False, "timezone-naive current_time must fail closed")
    require(timezone_naive_now.reason.startswith("ambiguous_current_time:"), "timezone-naive current_time reason mismatch")

    evidence = expired.as_evidence()
    require("allowed_to_continue" in evidence, "evidence must include allowed_to_continue")
    require("status" in evidence, "evidence must include status")
    require("reason" in evidence, "evidence must include reason")
    forbidden_evidence_terms = ["secret", "credential", "token", "scanner_output", "customer"]
    evidence_text = str(evidence).lower()
    for term in forbidden_evidence_terms:
        require(term not in evidence_text, f"evidence should not include sensitive term: {term}")

    print("Authorization expiry current-time helper tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
