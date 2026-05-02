from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
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


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def require_keys(data: dict[str, Any], keys: list[str], label: str) -> None:
    missing = [key for key in keys if key not in data]
    if missing:
        raise PolicyError(f"{label} is missing required keys: {missing}")


def validate_request_decision_binding(
    request: dict[str, Any],
    decision: dict[str, Any],
) -> None:
    require_keys(request, BINDING_FIELDS, "tool_action_request")
    require_keys(
        decision,
        BINDING_FIELDS + ["decision", "expires_at", "decided_at", "constraints", "evidence_required"],
        "authorization_decision",
    )

    for field in BINDING_FIELDS:
        if request.get(field) != decision.get(field):
            raise PolicyError(
                f"Authorization binding mismatch for {field}: "
                f"request={request.get(field)!r}, decision={decision.get(field)!r}"
            )

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


def load_default_vault_metadata() -> dict[str, Any]:
    path = Path("prototypes/tool-gateway/mock_vault/metadata.json")
    if not path.exists():
        return {"credential_refs": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def _get_credential_metadata(vault_metadata: dict[str, Any], credential_ref: str) -> dict[str, Any]:
    refs = vault_metadata.get("credential_refs", {})
    if credential_ref not in refs:
        raise PolicyError(f"credential_ref is not registered in mock Vault metadata: {credential_ref}")
    metadata = refs[credential_ref]
    if not isinstance(metadata, dict):
        raise PolicyError(f"credential_ref metadata must be an object: {credential_ref}")
    return metadata


def validate_credential_ref_against_vault_metadata(
    decision: dict[str, Any],
    vault_metadata: dict[str, Any] | None = None,
) -> None:
    credential_ref = decision.get("credential_ref")
    if not credential_ref:
        return

    if decision.get("decision") != "allow":
        return

    metadata_root = vault_metadata if vault_metadata is not None else load_default_vault_metadata()
    metadata = _get_credential_metadata(metadata_root, credential_ref)

    if metadata.get("revoked") is True:
        raise PolicyError(f"credential_ref is revoked: {credential_ref}")

    expires_at = metadata.get("expires_at")
    if not expires_at:
        raise PolicyError(f"credential_ref metadata missing expires_at: {credential_ref}")
    if parse_zulu(expires_at) <= now_utc():
        raise PolicyError(f"credential_ref is expired: {credential_ref}")

    for field in ["target_id", "scope_id"]:
        expected = metadata.get(field)
        actual = decision.get(field)
        if expected != actual:
            raise PolicyError(
                f"credential_ref metadata mismatch for {field}: "
                f"metadata={expected!r}, decision={actual!r}"
            )

    allowed_tools = metadata.get("allowed_tools", [])
    if decision.get("tool") not in allowed_tools:
        raise PolicyError(
            f"credential_ref does not allow tool {decision.get('tool')!r}: {credential_ref}"
        )

    allowed_operations = metadata.get("allowed_operations", [])
    if decision.get("operation") not in allowed_operations:
        raise PolicyError(
            f"credential_ref does not allow operation {decision.get('operation')!r}: {credential_ref}"
        )
