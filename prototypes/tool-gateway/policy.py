from __future__ import annotations

from datetime import datetime
from typing import Any


class PolicyError(ValueError):
    pass


BINDING_FIELDS = [
    "tool_action_request_id",
    "action_type",
    "target_id",
    "scope_id",
    "tool",
    "operation",
    "credential_ref",
]


def parse_zulu(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def require_keys(data: dict[str, Any], keys: list[str], label: str) -> None:
    missing = [key for key in keys if key not in data]
    if missing:
        raise PolicyError(f"{label} is missing required keys: {missing}")


def validate_request_decision_binding(
    request: dict[str, Any],
    decision: dict[str, Any],
) -> None:
    require_keys(request, BINDING_FIELDS, "tool_action_request")
    require_keys(decision, BINDING_FIELDS + ["decision", "expires_at", "decided_at"], "authorization_decision")

    for field in BINDING_FIELDS:
        if request.get(field) != decision.get(field):
            raise PolicyError(
                f"Authorization binding mismatch for {field}: "
                f"request={request.get(field)!r}, decision={decision.get(field)!r}"
            )

    # Stable MVP check: ensure expiry is after decision time without making examples fail as real time passes.
    decided_at = parse_zulu(decision["decided_at"])
    expires_at = parse_zulu(decision["expires_at"])
    if expires_at <= decided_at:
        raise PolicyError("authorization_decision expires_at must be after decided_at")

    constraints = decision.get("constraints", {})
    if constraints.get("destructive_tests") is True:
        raise PolicyError("destructive_tests must not be true for MVP mock runner")

    if decision.get("evidence_required") is not True:
        raise PolicyError("evidence_required must be true for MVP mock runner")


def decision_to_execution_status(decision: dict[str, Any]) -> str:
    value = decision["decision"]
    if value == "allow":
        return "completed"
    if value == "deny":
        return "blocked"
    if value == "require_human_approval":
        return "requires_human_approval"
    raise PolicyError(f"Unsupported decision value: {value}")


def should_resolve_credential(decision: dict[str, Any]) -> bool:
    return decision["decision"] == "allow" and bool(decision.get("credential_ref"))
