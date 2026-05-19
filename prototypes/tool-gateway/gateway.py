from __future__ import annotations

from typing import Any

from adapters.registry import get_adapter
from models import make_evidence_id, make_execution_id, utc_now_iso
from policy import (
    decision_to_execution_status,
    should_resolve_credential,
    validate_credential_ref_against_vault_metadata,
    validate_request_decision_binding,
)


def run_mock_tool_gateway(
    request: dict[str, Any],
    decision: dict[str, Any],
    vault_metadata: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    validate_request_decision_binding(request, decision)
    validate_credential_ref_against_vault_metadata(decision, vault_metadata=vault_metadata)

    status = decision_to_execution_status(decision)
    started_at = utc_now_iso()
    completed_at = started_at

    credential_ref = decision.get("credential_ref")
    credential_ref_used = credential_ref if status == "completed" else None
    credential_resolved_by = "mock-vault" if should_resolve_credential(decision) else None

    tool_execution_id = make_execution_id(request)

    if status == "completed":
        adapter = get_adapter(decision["tool"])
        # Adapter output is internal Tool Gateway information.
        # Do not include it in generated public tool_execution_result objects.
        adapter.execute(request, decision, credential_resolved_by)
        raw_artifact_ref = f"private-not-in-git/raw-artifacts/{decision['tool']}/{tool_execution_id}.json"
        sanitized_artifact_ref = f"private-not-in-git/prototype-runs/{tool_execution_id}/sanitized-result.json"
        sanitization_status = "completed"
        finding_candidate_ids = [f"finding-{tool_execution_id.removeprefix('exec-')}"]
        human_review_status = "pending"
        error_summary = None
    elif status == "blocked":
        raw_artifact_ref = None
        sanitized_artifact_ref = None
        sanitization_status = "not_required"
        finding_candidate_ids = []
        human_review_status = "not_required"
        error_summary = "Blocked by authorization decision before tool execution."
    else:
        raw_artifact_ref = None
        sanitized_artifact_ref = None
        sanitization_status = "not_required"
        finding_candidate_ids = []
        human_review_status = "pending"
        error_summary = "Execution paused because human approval is required."

    result = {
        "tool_execution_id": tool_execution_id,
        "tool_action_request_id": request["tool_action_request_id"],
        "authorization_decision_id": decision["authorization_decision_id"],
        "execution_status": status,
        "target_id": decision["target_id"],
        "scope_id": decision["scope_id"],
        "tool": decision["tool"],
        "operation": decision["operation"],
        "credential_ref_used": credential_ref_used,
        "credential_resolved_by": credential_resolved_by,
        "secret_exposed_to_ai": False,
        "raw_artifact_ref": raw_artifact_ref,
        "sanitized_artifact_ref": sanitized_artifact_ref,
        "started_at": started_at,
        "completed_at": completed_at,
        "error_summary": error_summary,
    }

    evidence = {
        "evidence_id": make_evidence_id(request),
        "tool_execution_id": tool_execution_id,
        "tool_action_request_id": request["tool_action_request_id"],
        "authorization_decision_id": decision["authorization_decision_id"],
        "target_id": decision["target_id"],
        "scope_id": decision["scope_id"],
        "tool": decision["tool"],
        "operation": decision["operation"],
        "credential_ref_used": credential_ref_used,
        "secret_exposed_to_ai": False,
        "raw_artifact_ref": raw_artifact_ref,
        "sanitized_artifact_ref": sanitized_artifact_ref,
        "sanitization_status": sanitization_status,
        "finding_candidate_ids": finding_candidate_ids,
        "human_review_status": human_review_status,
        "created_at": utc_now_iso(),
    }

    return result, evidence

# AAEF-AI-VA v0.6.356 authorization expiry current-time Gateway core integration candidate
# v0.6.356 authorization expiry scope fix: targeted authorization expiry only
# Candidate scope: block explicitly expired authorization decisions before dispatch in request/decision Gateway functions.

_AAEF_V06356_EXPIRY_KEYS = (
    "expires_at",
    "expires_at_utc",
    "authorization_expires_at",
    "authorization_expiry",
    "authorization_expiry_at",
    "valid_until",
    "valid_until_utc",
    "decision_expires_at",
)


def _aaef_v06356_parse_utc_datetime(value):
    from datetime import datetime, timezone

    if not isinstance(value, str) or not value.strip():
        return None
    candidate = value.strip()
    if candidate.endswith("Z"):
        candidate = candidate[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(candidate)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _aaef_v06356_find_authorization_expiry(value):
    """Return only an explicit authorization-decision expiry.

    This intentionally avoids recursively scanning the whole decision object.
    The first v0.6.356 candidate was too broad: it could pick up unrelated
    expires_at / valid_until fields inside fixture metadata and block normal
    allowed / denied / human-approval examples. This function only accepts:

    - expiry fields inside a dedicated authorization object;
    - explicit authorization_* expiry fields at the decision top level; or
    - explicit decision_expires_at at the decision top level.
    """
    if not isinstance(value, dict):
        return None

    authorization = value.get("authorization")
    if isinstance(authorization, dict):
        for key in _AAEF_V06356_EXPIRY_KEYS:
            item = authorization.get(key)
            if isinstance(item, str) and item.strip():
                return item

    authorization_decision = value.get("authorization_decision")
    if isinstance(authorization_decision, dict):
        for key in (
            "authorization_expires_at",
            "authorization_expiry",
            "authorization_expiry_at",
            "decision_expires_at",
        ):
            item = authorization_decision.get(key)
            if isinstance(item, str) and item.strip():
                return item

    for key in (
        "authorization_expires_at",
        "authorization_expiry",
        "authorization_expiry_at",
        "decision_expires_at",
    ):
        item = value.get(key)
        if isinstance(item, str) and item.strip():
            return item

    return None


def _aaef_v06356_authorization_expiry_current_time_gate(decision, current_time=None):
    from datetime import datetime, timezone

    expiry_raw = _aaef_v06356_find_authorization_expiry(decision)
    if not expiry_raw:
        return {
            "allowed_to_continue": True,
            "status": "not_applicable_missing_expiry_legacy_path_preserved",
            "reason": "authorization_expiry_not_present",
        }

    expiry_at = _aaef_v06356_parse_utc_datetime(expiry_raw)
    if expiry_at is None:
        return {
            "allowed_to_continue": False,
            "status": "blocked_before_dispatch",
            "reason": "authorization_expiry_unparseable",
            "authorization_expires_at": expiry_raw,
        }

    now = current_time or datetime.now(timezone.utc)
    now = now.astimezone(timezone.utc)
    if expiry_at <= now:
        return {
            "allowed_to_continue": False,
            "status": "blocked_before_dispatch",
            "reason": "authorization_expired_at_current_time",
            "authorization_expires_at": expiry_at.isoformat(),
            "current_time": now.isoformat(),
        }

    return {
        "allowed_to_continue": True,
        "status": "passed",
        "reason": "authorization_not_expired",
        "authorization_expires_at": expiry_at.isoformat(),
        "current_time": now.isoformat(),
    }


def _aaef_v06356_id_from(value, keys):
    if isinstance(value, dict):
        for key in keys:
            item = value.get(key)
            if isinstance(item, str) and item:
                return item
    return None


def _aaef_v06356_blocked_before_dispatch_result_for_authorization_expiry(request, decision, gate):
    return {
        "status": "blocked",
        "execution_status": "blocked",
        "dispatch_status": "blocked_before_dispatch",
        "blocked_reason": gate.get("reason", "authorization_expiry_current_time_failed"),
        "tool_action_request_id": _aaef_v06356_id_from(
            request,
            ("tool_action_request_id", "request_id", "id"),
        ),
        "authorization_decision_id": _aaef_v06356_id_from(
            decision,
            ("authorization_decision_id", "decision_id", "id"),
        ),
        "gateway_validation": {
            "authorization_current_time_expiry": gate,
        },
        "external_process_executed": False,
        "network_activity_performed": False,
        "result": {
            "message": "Blocked before dispatch because authorization expiry current-time validation failed.",
        },
    }


def _aaef_v06356_blocked_evidence_for_authorization_expiry(request, decision, gate):
    return {
        "evidence_type": "gateway_validation_trace",
        "status": "blocked_before_dispatch",
        "blocked_reason": gate.get("reason", "authorization_expiry_current_time_failed"),
        "gateway_validation": {
            "authorization_current_time_expiry": gate,
        },
        "tool_action_request_id": _aaef_v06356_id_from(
            request,
            ("tool_action_request_id", "request_id", "id"),
        ),
        "authorization_decision_id": _aaef_v06356_id_from(
            decision,
            ("authorization_decision_id", "decision_id", "id"),
        ),
        "external_process_executed": False,
        "network_activity_performed": False,
        "limitations": [
            "mock Gateway validation result only",
            "not scanner output",
            "not execution authorization",
            "not legal proof",
        ],
    }


def _aaef_v06356_shape_blocked_gateway_return(original, request, decision, gate, blocked_result):
    original_name = getattr(original, "__name__", "")
    if original_name == "run_mock_tool_gateway":
        return (
            blocked_result,
            _aaef_v06356_blocked_evidence_for_authorization_expiry(request, decision, gate),
        )
    return blocked_result

def _aaef_v06356_extract_request_decision(signature, args, kwargs):
    try:
        bound = signature.bind_partial(*args, **kwargs)
    except TypeError:
        return None, None
    request = None
    decision = None
    for name, value in bound.arguments.items():
        lowered = name.lower()
        if request is None and "request" in lowered:
            request = value
        if decision is None and ("decision" in lowered or "authorization" in lowered):
            decision = value
    return request, decision


_AAEF_V06356_GATEWAY_FUNCTION_INVENTORY = []
_AAEF_V06356_WRAPPED_GATEWAY_FUNCTIONS = []


def _aaef_v06356_install_gateway_wrappers():
    import functools
    import inspect

    global _AAEF_V06356_GATEWAY_FUNCTION_INVENTORY
    global _AAEF_V06356_WRAPPED_GATEWAY_FUNCTIONS

    inventory = []
    wrapped = []

    for name, fn in list(globals().items()):
        if name.startswith("_aaef_v06356_"):
            continue
        if not callable(fn):
            continue
        try:
            signature = inspect.signature(fn)
        except (TypeError, ValueError):
            continue

        params = [param_name.lower() for param_name in signature.parameters]
        inventory.append({"name": name, "parameters": params})

        has_request = any("request" in param for param in params)
        has_decision = any("decision" in param or "authorization" in param for param in params)
        if not (has_request and has_decision):
            continue

        if getattr(fn, "_aaef_v06356_wrapped", False):
            wrapped.append(name)
            continue

        def _make_wrapper(original, original_signature):
            @functools.wraps(original)
            def _wrapped(*args, **kwargs):
                request, decision = _aaef_v06356_extract_request_decision(
                    original_signature,
                    args,
                    kwargs,
                )
                if decision is not None:
                    gate = _aaef_v06356_authorization_expiry_current_time_gate(decision)
                    if not gate.get("allowed_to_continue", True):
                        blocked_result = _aaef_v06356_blocked_before_dispatch_result_for_authorization_expiry(
                            request,
                            decision,
                            gate,
                        )
                        return _aaef_v06356_shape_blocked_gateway_return(
                            original,
                            request,
                            decision,
                            gate,
                            blocked_result,
                        )
                return original(*args, **kwargs)

            _wrapped._aaef_v06356_wrapped = True
            return _wrapped

        globals()[name] = _make_wrapper(fn, signature)
        wrapped.append(name)

    _AAEF_V06356_GATEWAY_FUNCTION_INVENTORY = inventory
    _AAEF_V06356_WRAPPED_GATEWAY_FUNCTIONS = wrapped


_aaef_v06356_install_gateway_wrappers()

