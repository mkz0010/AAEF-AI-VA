from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

FIELD_ALIASES: dict[str, tuple[str, ...]] = {
    "tool_action": ("tool_action", "action", "tool", "tool_name", "requested_tool_action", "authorized_tool_action"),
    "target": ("target", "target_id", "target_url", "destination", "requested_target", "authorized_target"),
    "destination_binding": ("destination_binding", "runtime_destination_binding", "destination_binding_id"),
    "target_mode": ("target_mode", "target_type", "target_boundary"),
    "scope_id": ("scope_id", "scope", "assessment_scope", "authorized_scope"),
    "credential_ref": ("credential_ref", "credential_reference", "allowed_credential_ref", "authorized_credential_ref"),
    "execution_mode": ("execution_mode", "mode", "run_mode", "authorized_execution_mode"),
    "external_discovery": ("external_discovery", "allow_external_discovery", "external_discovery_allowed"),
    "delivery_action": ("delivery_action", "reporting_action", "authorized_delivery_action"),
}

DIFF_CATEGORY_BY_FIELD: dict[str, str] = {
    "tool_action": "tool_action_mismatch",
    "target": "target_mismatch",
    "destination_binding": "destination_binding_mismatch",
    "target_mode": "target_mode_mismatch",
    "scope_id": "scope_mismatch",
    "credential_ref": "credential_ref_mismatch",
    "execution_mode": "execution_mode_mismatch",
    "external_discovery": "external_discovery_escalation",
    "delivery_action": "delivery_action_mismatch",
}

DEFAULT_REQUIRED_FIELDS: tuple[str, ...] = (
    "tool_action",
    "target",
    "target_mode",
    "scope_id",
    "execution_mode",
    "external_discovery",
)


@dataclass(frozen=True)
class ConstraintDiff:
    category: str
    field: str
    reason: str

    def as_evidence(self) -> dict[str, str]:
        return {
            "category": self.category,
            "field": self.field,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class RequestDecisionConstraintDiffResult:
    allowed_to_continue: bool
    status: str
    reason: str
    diff_categories: tuple[str, ...]
    diffs: tuple[ConstraintDiff, ...]
    matched_constraints: tuple[str, ...]
    compared_fields: tuple[str, ...]

    def as_evidence(self) -> dict[str, Any]:
        return {
            "allowed_to_continue": self.allowed_to_continue,
            "status": self.status,
            "reason": self.reason,
            "diff_categories": list(self.diff_categories),
            "diffs": [diff.as_evidence() for diff in self.diffs],
            "matched_constraints": list(self.matched_constraints),
            "compared_fields": list(self.compared_fields),
        }


def _safe_mapping(value: Any, name: str) -> Mapping[str, Any] | ConstraintDiff:
    if not isinstance(value, Mapping):
        if name == "request":
            category = "malformed_request_constraints"
        elif name == "decision":
            category = "malformed_decision_constraints"
        else:
            category = "ambiguous_constraint_comparison"
        return ConstraintDiff(
            category=category,
            field=name,
            reason=f"{name}_constraints_not_mapping",
        )
    return value


def _find_value(data: Mapping[str, Any], canonical_field: str) -> tuple[bool, Any]:
    aliases = FIELD_ALIASES.get(canonical_field, (canonical_field,))
    for alias in aliases:
        if alias in data:
            return True, data[alias]
    return False, None


def _normalize_scalar(value: Any) -> Any:
    if isinstance(value, str):
        return value.strip()
    return value


def _diff_for_field(field: str, reason: str) -> ConstraintDiff:
    return ConstraintDiff(
        category=DIFF_CATEGORY_BY_FIELD.get(field, "ambiguous_constraint_comparison"),
        field=field,
        reason=reason,
    )


def evaluate_request_decision_constraint_diff(
    request: Mapping[str, Any],
    decision: Mapping[str, Any],
    *,
    required_fields: Sequence[str] = DEFAULT_REQUIRED_FIELDS,
    optional_fields: Sequence[str] = ("destination_binding", "credential_ref", "delivery_action"),
) -> RequestDecisionConstraintDiffResult:
    # Compare evidence-safe, gate-relevant request constraints with the
    # authorization decision constraints. Raw values are deliberately not
    # copied into evidence output.
    request_mapping = _safe_mapping(request, "request")
    if isinstance(request_mapping, ConstraintDiff):
        return _blocked((request_mapping,), (), ())

    decision_mapping = _safe_mapping(decision, "decision")
    if isinstance(decision_mapping, ConstraintDiff):
        return _blocked((decision_mapping,), (), ())

    fields: tuple[str, ...] = tuple(dict.fromkeys([*required_fields, *optional_fields]))
    diffs: list[ConstraintDiff] = []
    matched: list[str] = []
    compared: list[str] = []

    for field in fields:
        request_has, request_value = _find_value(request_mapping, field)
        decision_has, decision_value = _find_value(decision_mapping, field)

        if field in required_fields:
            if not request_has:
                diffs.append(ConstraintDiff("missing_required_request_field", field, "required_request_constraint_missing"))
                compared.append(field)
                continue
            if not decision_has:
                diffs.append(ConstraintDiff("missing_required_decision_field", field, "required_decision_constraint_missing"))
                compared.append(field)
                continue

        if not request_has and not decision_has:
            continue

        if request_has != decision_has:
            if request_has:
                diffs.append(_diff_for_field(field, "request_constraint_present_without_decision_constraint"))
            else:
                diffs.append(_diff_for_field(field, "decision_constraint_present_without_request_constraint"))
            compared.append(field)
            continue

        compared.append(field)
        normalized_request = _normalize_scalar(request_value)
        normalized_decision = _normalize_scalar(decision_value)

        if field == "external_discovery":
            request_bool = bool(normalized_request)
            decision_bool = bool(normalized_decision)
            if request_bool and not decision_bool:
                diffs.append(ConstraintDiff("external_discovery_escalation", field, "request_enables_external_discovery_without_decision"))
            elif request_bool != decision_bool:
                diffs.append(_diff_for_field(field, "external_discovery_value_mismatch"))
            else:
                matched.append(field)
            continue

        if normalized_request != normalized_decision:
            diffs.append(_diff_for_field(field, "request_decision_value_mismatch"))
        else:
            matched.append(field)

    if diffs:
        return _blocked(tuple(diffs), tuple(matched), tuple(compared))

    return RequestDecisionConstraintDiffResult(
        allowed_to_continue=True,
        status="continue_existing_checks",
        reason="request_decision_constraints_match",
        diff_categories=(),
        diffs=(),
        matched_constraints=tuple(matched),
        compared_fields=tuple(compared),
    )


def _blocked(
    diffs: tuple[ConstraintDiff, ...],
    matched: tuple[str, ...],
    compared: tuple[str, ...],
) -> RequestDecisionConstraintDiffResult:
    categories = tuple(diff.category for diff in diffs)
    return RequestDecisionConstraintDiffResult(
        allowed_to_continue=False,
        status="blocked",
        reason="request_decision_constraint_diff_detected",
        diff_categories=categories,
        diffs=diffs,
        matched_constraints=matched,
        compared_fields=compared,
    )
