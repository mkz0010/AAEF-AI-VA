from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Mapping

EXPIRY_FIELD_CANDIDATES: tuple[str, ...] = (
    "authorization_expires_at",
    "expires_at",
    "expires",
    "expiry",
    "expiration",
    "valid_until",
)


@dataclass(frozen=True)
class AuthorizationExpiryDecision:
    # Evidence-safe authorization expiry decision. This object deliberately
    # records decision facts without copying secrets, credentials, scanner
    # output, customer material, or private artifacts.
    allowed_to_continue: bool
    status: str
    reason: str
    expiry_field: str | None = None
    expiry_value_present: bool = False
    expired: bool | None = None
    comparison: str | None = None

    def as_evidence(self) -> dict[str, Any]:
        return {
            "allowed_to_continue": self.allowed_to_continue,
            "status": self.status,
            "reason": self.reason,
            "expiry_field": self.expiry_field,
            "expiry_value_present": self.expiry_value_present,
            "expired": self.expired,
            "comparison": self.comparison,
        }


def _parse_datetime(value: Any) -> datetime:
    if not isinstance(value, str):
        raise ValueError("timestamp must be an ISO-8601 string")

    normalized = value.strip()
    if not normalized:
        raise ValueError("timestamp must not be empty")

    if normalized.endswith("Z"):
        normalized = normalized[:-1] + "+00:00"

    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise ValueError("timestamp must be ISO-8601 parseable") from exc

    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("timestamp must be timezone-aware")

    return parsed.astimezone(timezone.utc)


def _find_expiry_value(authorization: Mapping[str, Any]) -> tuple[str | None, Any]:
    for field in EXPIRY_FIELD_CANDIDATES:
        if field in authorization:
            return field, authorization[field]
    return None, None


def evaluate_authorization_expiry(
    authorization: Mapping[str, Any],
    *,
    current_time: datetime | str,
    expiry_required: bool = False,
) -> AuthorizationExpiryDecision:
    # Evaluate authorization expiry against an explicit current-time value.
    # The function is intentionally deterministic: callers must supply
    # current_time. It does not read wall-clock time internally. Ambiguous
    # inputs fail closed.
    if not isinstance(authorization, Mapping):
        return AuthorizationExpiryDecision(
            allowed_to_continue=False,
            status="blocked",
            reason="authorization_not_mapping",
            expiry_value_present=False,
        )

    try:
        current = _parse_datetime(current_time) if isinstance(current_time, str) else current_time
        if not isinstance(current, datetime):
            raise ValueError("current_time must be datetime or ISO-8601 string")
        if current.tzinfo is None or current.utcoffset() is None:
            raise ValueError("current_time must be timezone-aware")
        current = current.astimezone(timezone.utc)
    except ValueError as exc:
        return AuthorizationExpiryDecision(
            allowed_to_continue=False,
            status="blocked",
            reason=f"ambiguous_current_time: {exc}",
            expiry_value_present=False,
        )

    field, raw_expiry = _find_expiry_value(authorization)
    if field is None:
        if expiry_required:
            return AuthorizationExpiryDecision(
                allowed_to_continue=False,
                status="blocked",
                reason="missing_required_expiry",
                expiry_field=None,
                expiry_value_present=False,
            )
        return AuthorizationExpiryDecision(
            allowed_to_continue=True,
            status="continue_existing_checks",
            reason="expiry_not_present_not_required",
            expiry_field=None,
            expiry_value_present=False,
            expired=None,
            comparison="not_applicable",
        )

    try:
        expiry = _parse_datetime(raw_expiry)
    except ValueError as exc:
        return AuthorizationExpiryDecision(
            allowed_to_continue=False,
            status="blocked",
            reason=f"malformed_expiry: {exc}",
            expiry_field=field,
            expiry_value_present=True,
            expired=None,
            comparison="parse_failed",
        )

    if current > expiry:
        return AuthorizationExpiryDecision(
            allowed_to_continue=False,
            status="blocked",
            reason="authorization_expired",
            expiry_field=field,
            expiry_value_present=True,
            expired=True,
            comparison="current_time_after_expiry",
        )

    return AuthorizationExpiryDecision(
        allowed_to_continue=True,
        status="continue_existing_checks",
        reason="authorization_not_expired",
        expiry_field=field,
        expiry_value_present=True,
        expired=False,
        comparison="current_time_before_or_equal_expiry",
    )
