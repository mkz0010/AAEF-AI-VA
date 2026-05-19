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

# AAEF-AI-VA v0.6.358 request/decision constraint diff Gateway core integration candidate
# v0.6.358 constraint diff existing PolicyError path preservation fix
# v0.6.358 constraint diff dispatch-decision scope fix
# Candidate scope: block explicit request/decision constraint-map mismatches before dispatch.

_AAEF_V06358_REQUEST_CONSTRAINT_KEYS = (
    "requested_constraints",
    "constraints",
    "request_constraints",
    "constraint_set",
)

_AAEF_V06358_DECISION_CONSTRAINT_KEYS = (
    "approved_constraints",
    "constraints",
    "decision_constraints",
    "authorized_constraints",
    "constraint_set",
)


def _aaef_v06358_jsonable(value):
    if isinstance(value, dict):
        return {str(key): _aaef_v06358_jsonable(item) for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))}
    if isinstance(value, list):
        return [_aaef_v06358_jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [_aaef_v06358_jsonable(item) for item in value]
    return value


def _aaef_v06358_normalize_constraint_map(value):
    if not isinstance(value, dict):
        return None
    normalized = _aaef_v06358_jsonable(value)
    return normalized if normalized else None


def _aaef_v06358_find_constraint_map(value, keys):
    if not isinstance(value, dict):
        return None

    for key in keys:
        normalized = _aaef_v06358_normalize_constraint_map(value.get(key))
        if normalized:
            return normalized

    for nested_key in ("tool_action_request", "request", "authorization_decision", "decision", "authorization"):
        nested = value.get(nested_key)
        if isinstance(nested, dict):
            for key in keys:
                normalized = _aaef_v06358_normalize_constraint_map(nested.get(key))
                if normalized:
                    return normalized

    return None


def _aaef_v06358_constraint_diff(request_constraints, decision_constraints):
    request_keys = set(request_constraints)
    decision_keys = set(decision_constraints)
    missing_in_decision = sorted(request_keys - decision_keys)
    extra_in_decision = sorted(decision_keys - request_keys)
    mismatched_keys = sorted(
        key
        for key in request_keys & decision_keys
        if request_constraints.get(key) != decision_constraints.get(key)
    )
    return {
        "missing_in_decision": missing_in_decision,
        "extra_in_decision": extra_in_decision,
        "mismatched_keys": mismatched_keys,
    }


def _aaef_v06358_decision_allows_dispatch(decision):
    """Return False for explicit non-dispatch decisions.

    Constraint-diff must not replace existing denied or human-approval paths,
    because those paths already produce schema-compatible result/evidence records.
    """
    if not isinstance(decision, dict):
        return True

    status_values = []
    for key in (
        "status",
        "decision",
        "decision_status",
        "authorization_status",
        "approval_status",
        "dispatch_status",
        "execution_status",
    ):
        value = decision.get(key)
        if isinstance(value, str):
            status_values.append(value.lower())

    authorization = decision.get("authorization")
    if isinstance(authorization, dict):
        for key in (
            "status",
            "decision",
            "decision_status",
            "authorization_status",
            "approval_status",
        ):
            value = authorization.get(key)
            if isinstance(value, str):
                status_values.append(value.lower())

    explicit_non_dispatch_terms = (
        "blocked",
        "denied",
        "deny",
        "rejected",
        "reject",
        "requires_human_approval",
        "human_approval_required",
        "pending_human_approval",
        "needs_human_approval",
        "paused_before_dispatch",
    )
    if any(any(term in value for term in explicit_non_dispatch_terms) for value in status_values):
        return False

    return True


def _aaef_v06358_should_defer_to_existing_policy_error_path(request_constraints, decision_constraints):
    """Preserve existing fail-closed PolicyError paths.

    Some constraints, such as destructive_tests=true, are already enforced by
    the existing mock Gateway runner tests as PolicyError cases. The v0.6.358
    constraint-diff candidate must not convert those legacy fail-closed paths
    into custom blocked result/evidence records.
    """
    for constraint_map in (request_constraints, decision_constraints):
        if not isinstance(constraint_map, dict):
            continue
        destructive = constraint_map.get("destructive_tests")
        if destructive is True:
            return True
        if isinstance(destructive, str) and destructive.lower() == "true":
            return True
    return False

def _aaef_v06358_request_decision_constraint_diff_gate(request, decision):
    if not _aaef_v06358_decision_allows_dispatch(decision):
        return {
            "allowed_to_continue": True,
            "status": "not_applicable_decision_not_dispatch_authorized_legacy_path_preserved",
            "reason": "decision_does_not_authorize_dispatch",
        }

    request_constraints = _aaef_v06358_find_constraint_map(
        request,
        _AAEF_V06358_REQUEST_CONSTRAINT_KEYS,
    )
    decision_constraints = _aaef_v06358_find_constraint_map(
        decision,
        _AAEF_V06358_DECISION_CONSTRAINT_KEYS,
    )

    if not request_constraints or not decision_constraints:
        return {
            "allowed_to_continue": True,
            "status": "not_applicable_missing_constraint_maps_legacy_path_preserved",
            "reason": "explicit_request_decision_constraint_maps_not_present",
        }

    if _aaef_v06358_should_defer_to_existing_policy_error_path(
        request_constraints,
        decision_constraints,
    ):
        return {
            "allowed_to_continue": True,
            "status": "not_applicable_existing_policy_error_path_preserved",
            "reason": "existing_policy_error_path_preserved_for_high_risk_constraint",
        }

    diff = _aaef_v06358_constraint_diff(request_constraints, decision_constraints)
    has_diff = any(diff.values())
    if has_diff:
        return {
            "allowed_to_continue": False,
            "status": "blocked_before_dispatch",
            "reason": "request_decision_constraint_diff_detected",
            "diff": diff,
            "request_constraints": request_constraints,
            "decision_constraints": decision_constraints,
        }

    return {
        "allowed_to_continue": True,
        "status": "passed",
        "reason": "request_decision_constraints_match",
        "request_constraints": request_constraints,
        "decision_constraints": decision_constraints,
    }


def _aaef_v06358_id_from(value, keys):
    if isinstance(value, dict):
        for key in keys:
            item = value.get(key)
            if isinstance(item, str) and item:
                return item
    return None


def _aaef_v06358_blocked_before_dispatch_result_for_constraint_diff(request, decision, gate):
    return {
        "status": "blocked",
        "execution_status": "blocked",
        "dispatch_status": "blocked_before_dispatch",
        "blocked_reason": gate.get("reason", "request_decision_constraint_diff_failed"),
        "tool_action_request_id": _aaef_v06358_id_from(request, ("tool_action_request_id", "request_id", "id")),
        "authorization_decision_id": _aaef_v06358_id_from(decision, ("authorization_decision_id", "decision_id", "id")),
        "gateway_validation": {"request_decision_constraint_diff": gate},
        "external_process_executed": False,
        "network_activity_performed": False,
        "result": {
            "message": "Blocked before dispatch because request/decision constraint-diff validation failed.",
        },
    }


def _aaef_v06358_blocked_evidence_for_constraint_diff(request, decision, gate):
    return {
        "evidence_type": "gateway_validation_trace",
        "status": "blocked_before_dispatch",
        "blocked_reason": gate.get("reason", "request_decision_constraint_diff_failed"),
        "gateway_validation": {"request_decision_constraint_diff": gate},
        "tool_action_request_id": _aaef_v06358_id_from(request, ("tool_action_request_id", "request_id", "id")),
        "authorization_decision_id": _aaef_v06358_id_from(decision, ("authorization_decision_id", "decision_id", "id")),
        "external_process_executed": False,
        "network_activity_performed": False,
        "limitations": [
            "mock Gateway validation result only",
            "not scanner output",
            "not execution authorization",
            "not legal proof",
        ],
    }


def _aaef_v06358_shape_blocked_gateway_return(original, request, decision, gate, blocked_result):
    original_name = getattr(original, "__name__", "")
    if original_name == "run_mock_tool_gateway":
        return (blocked_result, _aaef_v06358_blocked_evidence_for_constraint_diff(request, decision, gate))
    return blocked_result


def _aaef_v06358_extract_request_decision(signature, args, kwargs):
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


_AAEF_V06358_GATEWAY_FUNCTION_INVENTORY = []
_AAEF_V06358_WRAPPED_GATEWAY_FUNCTIONS = []


def _aaef_v06358_install_gateway_wrappers():
    import functools
    import inspect

    global _AAEF_V06358_GATEWAY_FUNCTION_INVENTORY
    global _AAEF_V06358_WRAPPED_GATEWAY_FUNCTIONS

    inventory = []
    wrapped = []

    for name, fn in list(globals().items()):
        if name.startswith("_aaef_"):
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

        if getattr(fn, "_aaef_v06358_wrapped", False):
            wrapped.append(name)
            continue

        def _make_wrapper(original, original_signature):
            @functools.wraps(original)
            def _wrapped(*args, **kwargs):
                request, decision = _aaef_v06358_extract_request_decision(original_signature, args, kwargs)
                if request is not None and decision is not None:
                    gate = _aaef_v06358_request_decision_constraint_diff_gate(request, decision)
                    if not gate.get("allowed_to_continue", True):
                        blocked_result = _aaef_v06358_blocked_before_dispatch_result_for_constraint_diff(request, decision, gate)
                        return _aaef_v06358_shape_blocked_gateway_return(original, request, decision, gate, blocked_result)
                return original(*args, **kwargs)

            _wrapped._aaef_v06358_wrapped = True
            return _wrapped

        globals()[name] = _make_wrapper(fn, signature)
        wrapped.append(name)

    _AAEF_V06358_GATEWAY_FUNCTION_INVENTORY = inventory
    _AAEF_V06358_WRAPPED_GATEWAY_FUNCTIONS = wrapped


_aaef_v06358_install_gateway_wrappers()

# AAEF-AI-VA v0.6.360 external discovery fail-closed Gateway core integration candidate
# Candidate scope: block explicit external_discovery=true before dispatch while preserving legacy non-dispatch and PolicyError paths.

_AAEF_V06360_REQUEST_CONSTRAINT_KEYS = ("requested_constraints", "constraints", "request_constraints", "constraint_set")
_AAEF_V06360_DECISION_CONSTRAINT_KEYS = ("approved_constraints", "constraints", "decision_constraints", "authorized_constraints", "constraint_set")


def _aaef_v06360_jsonable(value):
    if isinstance(value, dict):
        return {str(k): _aaef_v06360_jsonable(v) for k, v in sorted(value.items(), key=lambda p: str(p[0]))}
    if isinstance(value, (list, tuple)):
        return [_aaef_v06360_jsonable(v) for v in value]
    return value


def _aaef_v06360_find_constraint_map(value, keys):
    if not isinstance(value, dict):
        return None
    for key in keys:
        item = value.get(key)
        if isinstance(item, dict) and item:
            return _aaef_v06360_jsonable(item)
    for nested_key in ("tool_action_request", "request", "authorization_decision", "decision", "authorization"):
        nested = value.get(nested_key)
        if isinstance(nested, dict):
            for key in keys:
                item = nested.get(key)
                if isinstance(item, dict) and item:
                    return _aaef_v06360_jsonable(item)
    return None


def _aaef_v06360_decision_allows_dispatch(decision):
    if not isinstance(decision, dict):
        return True
    values = []
    for key in ("status", "decision", "decision_status", "authorization_status", "approval_status", "dispatch_status", "execution_status"):
        value = decision.get(key)
        if isinstance(value, str):
            values.append(value.lower())
    auth = decision.get("authorization")
    if isinstance(auth, dict):
        for key in ("status", "decision", "decision_status", "authorization_status", "approval_status"):
            value = auth.get(key)
            if isinstance(value, str):
                values.append(value.lower())
    non_dispatch = ("blocked", "denied", "deny", "rejected", "reject", "requires_human_approval", "human_approval_required", "pending_human_approval", "needs_human_approval", "paused_before_dispatch")
    return not any(any(term in value for term in non_dispatch) for value in values)


def _aaef_v06360_should_defer_to_existing_policy_error_path(request_constraints, decision_constraints):
    for constraint_map in (request_constraints, decision_constraints):
        if not isinstance(constraint_map, dict):
            continue
        destructive = constraint_map.get("destructive_tests")
        if destructive is True:
            return True
        if isinstance(destructive, str) and destructive.lower() == "true":
            return True
    return False


def _aaef_v06360_boolish_true(value):
    return value is True or value == 1 or (isinstance(value, str) and value.strip().lower() in ("true", "yes", "1", "enabled"))


def _aaef_v06360_external_discovery_value(constraint_map):
    if not isinstance(constraint_map, dict):
        return None
    if "external_discovery" in constraint_map:
        return constraint_map.get("external_discovery")
    if "allow_external_discovery" in constraint_map:
        return constraint_map.get("allow_external_discovery")
    return None


def _aaef_v06360_external_discovery_fail_closed_gate(request, decision):
    if not _aaef_v06360_decision_allows_dispatch(decision):
        return {"allowed_to_continue": True, "status": "not_applicable_decision_not_dispatch_authorized_legacy_path_preserved", "reason": "decision_does_not_authorize_dispatch"}

    request_constraints = _aaef_v06360_find_constraint_map(request, _AAEF_V06360_REQUEST_CONSTRAINT_KEYS)
    decision_constraints = _aaef_v06360_find_constraint_map(decision, _AAEF_V06360_DECISION_CONSTRAINT_KEYS)

    if _aaef_v06360_should_defer_to_existing_policy_error_path(request_constraints, decision_constraints):
        return {"allowed_to_continue": True, "status": "not_applicable_existing_policy_error_path_preserved", "reason": "existing_policy_error_path_preserved_for_high_risk_constraint"}

    request_external = _aaef_v06360_external_discovery_value(request_constraints)
    decision_external = _aaef_v06360_external_discovery_value(decision_constraints)

    if request_external is None and decision_external is None:
        return {"allowed_to_continue": True, "status": "not_applicable_external_discovery_not_declared_legacy_path_preserved", "reason": "external_discovery_not_explicitly_declared"}

    if _aaef_v06360_boolish_true(request_external) or _aaef_v06360_boolish_true(decision_external):
        return {"allowed_to_continue": False, "status": "blocked_before_dispatch", "reason": "external_discovery_true_fail_closed", "request_external_discovery": request_external, "decision_external_discovery": decision_external, "request_constraints": request_constraints, "decision_constraints": decision_constraints}

    return {"allowed_to_continue": True, "status": "passed", "reason": "external_discovery_not_enabled", "request_external_discovery": request_external, "decision_external_discovery": decision_external, "request_constraints": request_constraints, "decision_constraints": decision_constraints}


def _aaef_v06360_id_from(value, keys):
    if isinstance(value, dict):
        for key in keys:
            item = value.get(key)
            if isinstance(item, str) and item:
                return item
    return None


def _aaef_v06360_blocked_before_dispatch_result_for_external_discovery(request, decision, gate):
    return {"status": "blocked", "execution_status": "blocked", "dispatch_status": "blocked_before_dispatch", "blocked_reason": gate.get("reason", "external_discovery_fail_closed"), "tool_action_request_id": _aaef_v06360_id_from(request, ("tool_action_request_id", "request_id", "id")), "authorization_decision_id": _aaef_v06360_id_from(decision, ("authorization_decision_id", "decision_id", "id")), "gateway_validation": {"external_discovery_fail_closed": gate}, "external_process_executed": False, "network_activity_performed": False, "result": {"message": "Blocked before dispatch because external discovery fail-closed validation failed."}}


def _aaef_v06360_blocked_evidence_for_external_discovery(request, decision, gate):
    return {"evidence_type": "gateway_validation_trace", "status": "blocked_before_dispatch", "blocked_reason": gate.get("reason", "external_discovery_fail_closed"), "gateway_validation": {"external_discovery_fail_closed": gate}, "tool_action_request_id": _aaef_v06360_id_from(request, ("tool_action_request_id", "request_id", "id")), "authorization_decision_id": _aaef_v06360_id_from(decision, ("authorization_decision_id", "decision_id", "id")), "external_process_executed": False, "network_activity_performed": False, "limitations": ["mock Gateway validation result only", "not scanner output", "not execution authorization", "not legal proof"]}


def _aaef_v06360_shape_blocked_gateway_return(original, request, decision, gate, blocked_result):
    if getattr(original, "__name__", "") == "run_mock_tool_gateway":
        return (blocked_result, _aaef_v06360_blocked_evidence_for_external_discovery(request, decision, gate))
    return blocked_result


def _aaef_v06360_extract_request_decision(signature, args, kwargs):
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


_AAEF_V06360_GATEWAY_FUNCTION_INVENTORY = []
_AAEF_V06360_WRAPPED_GATEWAY_FUNCTIONS = []


def _aaef_v06360_install_gateway_wrappers():
    import functools
    import inspect
    global _AAEF_V06360_GATEWAY_FUNCTION_INVENTORY, _AAEF_V06360_WRAPPED_GATEWAY_FUNCTIONS
    inventory = []
    wrapped = []
    for name, fn in list(globals().items()):
        if name.startswith("_aaef_") or not callable(fn):
            continue
        try:
            signature = inspect.signature(fn)
        except (TypeError, ValueError):
            continue
        params = [p.lower() for p in signature.parameters]
        inventory.append({"name": name, "parameters": params})
        if not (any("request" in p for p in params) and any("decision" in p or "authorization" in p for p in params)):
            continue
        if getattr(fn, "_aaef_v06360_wrapped", False):
            wrapped.append(name)
            continue
        def _make_wrapper(original, original_signature):
            @functools.wraps(original)
            def _wrapped(*args, **kwargs):
                request, decision = _aaef_v06360_extract_request_decision(original_signature, args, kwargs)
                if request is not None and decision is not None:
                    gate = _aaef_v06360_external_discovery_fail_closed_gate(request, decision)
                    if not gate.get("allowed_to_continue", True):
                        blocked_result = _aaef_v06360_blocked_before_dispatch_result_for_external_discovery(request, decision, gate)
                        return _aaef_v06360_shape_blocked_gateway_return(original, request, decision, gate, blocked_result)
                return original(*args, **kwargs)
            _wrapped._aaef_v06360_wrapped = True
            return _wrapped
        globals()[name] = _make_wrapper(fn, signature)
        wrapped.append(name)
    _AAEF_V06360_GATEWAY_FUNCTION_INVENTORY = inventory
    _AAEF_V06360_WRAPPED_GATEWAY_FUNCTIONS = wrapped


_aaef_v06360_install_gateway_wrappers()

