from __future__ import annotations

from datetime import datetime
from typing import Any


class PolicyError(ValueError):
    """Raised when a Tool Gateway policy or binding check fails."""


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
    """Validate that an authorization decision is bound to the request.

    This does not make model output authoritative. It only checks that the
    Authorization Gateway decision is for the same requested action.
    """
    require_keys(request, BINDING_FIELDS, "tool_action_request")
    require_keys(decision, BINDING_FIELDS + ["decision", "expires_at", "decided_at"], "authorization_decision")

    for field in BINDING_FIELDS:
        if request.get(field) != decision.get(field):
            raise PolicyError(
                f"Authorization binding mismatch for {field}: "
                f"request={request.get(field)!r}, decision={decision.get(field)!r}"
            )

    # Stable MVP check: ensure expiry is after decision time without making
    # examples fail as real time passes.
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


def _credential_entries(vault_metadata: dict[str, Any]) -> list[dict[str, Any]]:
    entries = vault_metadata.get("credential_refs")
    if not isinstance(entries, list):
        raise PolicyError("mock Vault metadata must contain credential_refs list")
    return entries


def find_credential_metadata(
    credential_ref: str,
    vault_metadata: dict[str, Any],
) -> dict[str, Any]:
    for entry in _credential_entries(vault_metadata):
        if entry.get("credential_ref") == credential_ref:
            return entry
    raise PolicyError(f"credential_ref not found in mock Vault metadata: {credential_ref}")


def validate_credential_ref_against_vault_metadata(
    decision: dict[str, Any],
    vault_metadata: dict[str, Any] | None,
) -> dict[str, Any] | None:
    """Validate credential_ref against mock Vault metadata.

    This makes credential_ref a constrained reference rather than a free-form
    string. It still does not expose or resolve the raw secret.
    """
    if not should_resolve_credential(decision):
        return None

    credential_ref = decision.get("credential_ref")
    if not isinstance(credential_ref, str) or not credential_ref:
        raise PolicyError("credential_ref must be a non-empty string when credential resolution is required")

    if vault_metadata is None:
        raise PolicyError("credential_ref requires mock Vault metadata for allowed execution")

    entry = find_credential_metadata(credential_ref, vault_metadata)

    if entry.get("revoked") is True:
        raise PolicyError(f"credential_ref is revoked: {credential_ref}")

    if entry.get("target_id") != decision.get("target_id"):
        raise PolicyError(
            f"credential_ref target mismatch: "
            f"vault={entry.get('target_id')!r}, decision={decision.get('target_id')!r}"
        )

    if entry.get("scope_id") != decision.get("scope_id"):
        raise PolicyError(
            f"credential_ref scope mismatch: "
            f"vault={entry.get('scope_id')!r}, decision={decision.get('scope_id')!r}"
        )

    allowed_tools = entry.get("allowed_tools", [])
    if decision.get("tool") not in allowed_tools:
        raise PolicyError(
            f"credential_ref tool not allowed: tool={decision.get('tool')!r}, allowed={allowed_tools!r}"
        )

    allowed_operations = entry.get("allowed_operations", [])
    if decision.get("operation") not in allowed_operations:
        raise PolicyError(
            f"credential_ref operation not allowed: "
            f"operation={decision.get('operation')!r}, allowed={allowed_operations!r}"
        )

    expires_at = entry.get("expires_at")
    if not isinstance(expires_at, str):
        raise PolicyError(f"credential_ref metadata missing expires_at: {credential_ref}")

    if parse_zulu(expires_at) <= parse_zulu(decision["decided_at"]):
        raise PolicyError(f"credential_ref is expired at decision time: {credential_ref}")

    return entry
