from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

EXTERNAL_DISCOVERY_REQUEST_ALIASES: tuple[str, ...] = (
    "external_discovery",
    "requested_external_discovery",
)

EXTERNAL_DISCOVERY_DECISION_ALIASES: tuple[str, ...] = (
    "external_discovery_allowed",
    "allow_external_discovery",
    "authorized_external_discovery",
)

TARGET_MODE_ALIASES: tuple[str, ...] = (
    "target_mode",
    "target_boundary",
    "boundary_mode",
)

DESTINATION_BINDING_ALIASES: tuple[str, ...] = (
    "runtime_destination_binding",
    "destination_binding",
    "destination_binding_id",
)

SCOPE_SUPPORT_ALIASES: tuple[str, ...] = (
    "external_discovery_in_scope",
    "scope_supports_external_discovery",
    "external_discovery_scope_allowed",
)

LOCALHOST_ONLY_MODES: tuple[str, ...] = (
    "localhost_only",
    "loopback_only",
    "local_only",
)

LOCAL_LAB_ONLY_MODES: tuple[str, ...] = (
    "local_lab_only",
    "local-lab-only",
    "local_lab",
    "local-lab",
)

EXTERNAL_COMPATIBLE_MODES: tuple[str, ...] = (
    "external_allowed",
    "external_permitted",
    "scoped_external",
    "authorized_external",
)


@dataclass(frozen=True)
class ExternalDiscoveryBlock:
    category: str
    reason: str
    field: str | None = None

    def as_evidence(self) -> dict[str, str | None]:
        return {
            "category": self.category,
            "reason": self.reason,
            "field": self.field,
        }


@dataclass(frozen=True)
class ExternalDiscoveryDecision:
    allowed_to_continue: bool
    status: str
    reason: str
    external_discovery_requested: bool | None
    block_categories: tuple[str, ...]
    blocks: tuple[ExternalDiscoveryBlock, ...]
    matched_constraints: tuple[str, ...]
    checked_fields: tuple[str, ...]

    def as_evidence(self) -> dict[str, Any]:
        return {
            "allowed_to_continue": self.allowed_to_continue,
            "status": self.status,
            "reason": self.reason,
            "external_discovery_requested": self.external_discovery_requested,
            "block_categories": list(self.block_categories),
            "blocks": [block.as_evidence() for block in self.blocks],
            "matched_constraints": list(self.matched_constraints),
            "checked_fields": list(self.checked_fields),
        }


def _safe_mapping(value: Any, name: str) -> Mapping[str, Any] | ExternalDiscoveryBlock:
    if value is None:
        return ExternalDiscoveryBlock(
            category=f"missing_{name}",
            reason=f"{name}_missing",
            field=name,
        )
    if not isinstance(value, Mapping):
        return ExternalDiscoveryBlock(
            category=f"malformed_{name}",
            reason=f"{name}_not_mapping",
            field=name,
        )
    return value


def _find_value(data: Mapping[str, Any], aliases: tuple[str, ...]) -> tuple[bool, Any, str | None]:
    for alias in aliases:
        if alias in data:
            return True, data[alias], alias
    return False, None, None


def _parse_optional_bool(value: Any, *, field: str) -> tuple[bool | None, ExternalDiscoveryBlock | None]:
    if value is None:
        return None, None
    if isinstance(value, bool):
        return value, None
    return None, ExternalDiscoveryBlock(
        category="malformed_external_discovery_flag",
        reason="external_discovery_flag_must_be_boolean",
        field=field,
    )


def _parse_required_bool(value: Any, *, field: str) -> tuple[bool | None, ExternalDiscoveryBlock | None]:
    if isinstance(value, bool):
        return value, None
    return None, ExternalDiscoveryBlock(
        category="ambiguous_external_discovery_comparison",
        reason="external_discovery_allowance_must_be_boolean",
        field=field,
    )


def _destination_binding_present_and_valid(*sources: Mapping[str, Any]) -> tuple[bool, ExternalDiscoveryBlock | None]:
    for source in sources:
        present, value, field = _find_value(source, DESTINATION_BINDING_ALIASES)
        if not present:
            continue
        if isinstance(value, str) and value.strip():
            return True, None
        if isinstance(value, Mapping) and value:
            return True, None
        return False, ExternalDiscoveryBlock(
            category="external_discovery_requested_with_malformed_destination_binding",
            reason="destination_binding_malformed",
            field=field,
        )
    return False, ExternalDiscoveryBlock(
        category="external_discovery_requested_without_runtime_destination_binding",
        reason="destination_binding_missing",
        field="runtime_destination_binding",
    )


def _scope_supports_external(*sources: Mapping[str, Any]) -> bool:
    for source in sources:
        for alias in SCOPE_SUPPORT_ALIASES:
            if source.get(alias) is True:
                return True
    return False


def _authorization_invalid(authorization_result: Mapping[str, Any] | None) -> bool:
    if authorization_result is None:
        return False
    allowed = authorization_result.get("allowed_to_continue")
    status = authorization_result.get("status")
    if allowed is False:
        return True
    if isinstance(status, str) and status.lower() in {"blocked", "denied", "expired", "invalid"}:
        return True
    return False


def evaluate_external_discovery_fail_closed(
    request: Mapping[str, Any],
    decision: Mapping[str, Any],
    *,
    target_boundary: Mapping[str, Any] | None = None,
    authorization_result: Mapping[str, Any] | None = None,
    require_destination_binding_when_external: bool = True,
) -> ExternalDiscoveryDecision:
    # Evaluate whether external_discovery=true is explicitly allowed and
    # compatible with a target boundary. Raw target values and raw payloads are
    # deliberately not copied into evidence output.
    request_mapping = _safe_mapping(request, "request")
    if isinstance(request_mapping, ExternalDiscoveryBlock):
        return _blocked((request_mapping,), None, (), ("request",))

    decision_mapping = _safe_mapping(decision, "decision")
    if isinstance(decision_mapping, ExternalDiscoveryBlock):
        return _blocked((decision_mapping,), None, (), ("decision",))

    target_boundary_mapping: Mapping[str, Any] | None
    if target_boundary is None:
        target_boundary_mapping = None
    else:
        checked_boundary = _safe_mapping(target_boundary, "target_boundary")
        if isinstance(checked_boundary, ExternalDiscoveryBlock):
            target_boundary_mapping = None
        else:
            target_boundary_mapping = checked_boundary

    checked_fields: list[str] = []
    matched: list[str] = []
    blocks: list[ExternalDiscoveryBlock] = []

    request_has_flag, request_flag, request_flag_field = _find_value(request_mapping, EXTERNAL_DISCOVERY_REQUEST_ALIASES)
    checked_fields.append(request_flag_field or "external_discovery")
    requested_external, parse_block = _parse_optional_bool(request_flag if request_has_flag else False, field=request_flag_field or "external_discovery")
    if parse_block is not None:
        return _blocked((parse_block,), None, tuple(matched), tuple(checked_fields))

    if requested_external is not True:
        matched.append("external_discovery_not_requested")
        return ExternalDiscoveryDecision(
            allowed_to_continue=True,
            status="continue_existing_checks",
            reason="external_discovery_not_requested",
            external_discovery_requested=False,
            block_categories=(),
            blocks=(),
            matched_constraints=tuple(matched),
            checked_fields=tuple(checked_fields),
        )

    decision_has_allowance, decision_allowance, decision_allowance_field = _find_value(decision_mapping, EXTERNAL_DISCOVERY_DECISION_ALIASES)
    checked_fields.append(decision_allowance_field or "external_discovery_allowed")
    if not decision_has_allowance:
        blocks.append(ExternalDiscoveryBlock(
            category="external_discovery_requested_without_decision_allowance",
            reason="decision_allowance_missing",
            field="external_discovery_allowed",
        ))
    else:
        allowed_by_decision, allowance_block = _parse_required_bool(decision_allowance, field=decision_allowance_field or "external_discovery_allowed")
        if allowance_block is not None:
            blocks.append(allowance_block)
        elif allowed_by_decision is not True:
            blocks.append(ExternalDiscoveryBlock(
                category="external_discovery_requested_without_decision_allowance",
                reason="decision_allowance_false",
                field=decision_allowance_field,
            ))
        else:
            matched.append("decision_allows_external_discovery")

    if target_boundary_mapping is None:
        blocks.append(ExternalDiscoveryBlock(
            category="external_discovery_requested_with_ambiguous_target_boundary",
            reason="target_boundary_missing_or_malformed",
            field="target_boundary",
        ))
    else:
        target_mode_present, target_mode_value, target_mode_field = _find_value(target_boundary_mapping, TARGET_MODE_ALIASES)
        checked_fields.append(target_mode_field or "target_mode")
        if not target_mode_present or not isinstance(target_mode_value, str) or not target_mode_value.strip():
            blocks.append(ExternalDiscoveryBlock(
                category="external_discovery_requested_with_ambiguous_target_boundary",
                reason="target_mode_missing_or_malformed",
                field=target_mode_field or "target_mode",
            ))
        else:
            normalized_mode = target_mode_value.strip().lower()
            if normalized_mode in LOCALHOST_ONLY_MODES:
                blocks.append(ExternalDiscoveryBlock(
                    category="external_discovery_requested_against_localhost_only_boundary",
                    reason="target_boundary_is_localhost_only",
                    field=target_mode_field,
                ))
            elif normalized_mode in LOCAL_LAB_ONLY_MODES:
                blocks.append(ExternalDiscoveryBlock(
                    category="external_discovery_requested_against_local_lab_only_boundary",
                    reason="target_boundary_is_local_lab_only",
                    field=target_mode_field,
                ))
            elif normalized_mode in EXTERNAL_COMPATIBLE_MODES:
                matched.append("target_boundary_external_compatible")
            else:
                blocks.append(ExternalDiscoveryBlock(
                    category="external_discovery_requested_with_ambiguous_target_boundary",
                    reason="target_boundary_not_explicitly_external_compatible",
                    field=target_mode_field,
                ))

    if require_destination_binding_when_external:
        sources: tuple[Mapping[str, Any], ...]
        if target_boundary_mapping is None:
            sources = (request_mapping, decision_mapping)
        else:
            sources = (target_boundary_mapping, request_mapping, decision_mapping)
        destination_present, destination_block = _destination_binding_present_and_valid(*sources)
        checked_fields.append("runtime_destination_binding")
        if not destination_present and destination_block is not None:
            blocks.append(destination_block)
        elif destination_present:
            matched.append("runtime_destination_binding_present")

    if not _scope_supports_external(request_mapping, decision_mapping, target_boundary_mapping or {}):
        blocks.append(ExternalDiscoveryBlock(
            category="external_discovery_requested_without_scope_support",
            reason="scope_support_for_external_discovery_missing",
            field="scope_supports_external_discovery",
        ))
        checked_fields.append("scope_supports_external_discovery")
    else:
        matched.append("scope_supports_external_discovery")
        checked_fields.append("scope_supports_external_discovery")

    if _authorization_invalid(authorization_result):
        blocks.append(ExternalDiscoveryBlock(
            category="external_discovery_requested_with_expired_or_invalid_authorization",
            reason="authorization_result_not_allowed",
            field="authorization_result",
        ))
        checked_fields.append("authorization_result")

    if blocks:
        return _blocked(tuple(blocks), True, tuple(matched), tuple(dict.fromkeys(checked_fields)))

    return ExternalDiscoveryDecision(
        allowed_to_continue=True,
        status="continue_existing_checks",
        reason="external_discovery_explicitly_allowed_and_boundary_compatible",
        external_discovery_requested=True,
        block_categories=(),
        blocks=(),
        matched_constraints=tuple(matched),
        checked_fields=tuple(dict.fromkeys(checked_fields)),
    )


def _blocked(
    blocks: tuple[ExternalDiscoveryBlock, ...],
    requested_external: bool | None,
    matched: tuple[str, ...],
    checked_fields: tuple[str, ...],
) -> ExternalDiscoveryDecision:
    categories = tuple(block.category for block in blocks)
    return ExternalDiscoveryDecision(
        allowed_to_continue=False,
        status="blocked",
        reason="external_discovery_fail_closed",
        external_discovery_requested=requested_external,
        block_categories=categories,
        blocks=blocks,
        matched_constraints=matched,
        checked_fields=checked_fields,
    )
