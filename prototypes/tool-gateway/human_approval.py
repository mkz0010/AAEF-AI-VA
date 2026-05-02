from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class HumanApprovalError(ValueError):
    pass


VALID_APPROVAL_DECISIONS = {
    "approved",
    "rejected",
    "needs_more_info",
    "keep_blocked",
}


REQUIRED_APPROVAL_FIELDS = [
    "approval_record_id",
    "review_type",
    "command_plan_id",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "approval_decision",
    "approved_by",
    "approved_at",
    "expires_at",
    "approval_scope",
    "real_execution_allowed",
    "evidence_required",
    "conditions",
]


BINDING_FIELDS = [
    "command_plan_id",
    "tool",
    "operation",
    "target_id",
    "scope_id",
]


def _parse_zulu(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def validate_human_approval_record(record: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_APPROVAL_FIELDS if field not in record]
    if missing:
        raise HumanApprovalError(f"human approval record missing required fields: {missing}")

    if record["approval_decision"] not in VALID_APPROVAL_DECISIONS:
        raise HumanApprovalError(f"unsupported approval_decision: {record['approval_decision']}")

    if not isinstance(record.get("conditions"), list):
        raise HumanApprovalError("conditions must be a list")

    if record.get("evidence_required") is not True:
        raise HumanApprovalError("evidence_required must be true for approval records")

    if record.get("real_execution_allowed") is not False:
        raise HumanApprovalError("real_execution_allowed must remain false in current MVP")

    approved_at = _parse_zulu(record["approved_at"])
    expires_at = _parse_zulu(record["expires_at"])
    if expires_at <= approved_at:
        raise HumanApprovalError("expires_at must be after approved_at")

    if expires_at <= _now_utc():
        raise HumanApprovalError("approval record is expired")


def build_human_approval_record(
    operator_summary: dict[str, Any],
    approval_decision: str = "keep_blocked",
    approved_by: str = "demo-operator-001",
) -> dict[str, Any]:
    if approval_decision not in VALID_APPROVAL_DECISIONS:
        raise HumanApprovalError(f"unsupported approval_decision: {approval_decision}")

    # Use stable future timestamps for MVP examples.
    approved_at = "2026-05-02T00:00:00Z"
    expires_at = "2099-12-31T00:00:00Z"

    return {
        "approval_record_id": f"approval-{operator_summary.get('command_plan_id', 'unknown')}",
        "review_type": "human_approval_record",
        "command_plan_id": operator_summary.get("command_plan_id"),
        "tool": operator_summary.get("tool"),
        "operation": operator_summary.get("operation"),
        "target_id": operator_summary.get("target_id"),
        "scope_id": operator_summary.get("scope_id"),
        "approval_decision": approval_decision,
        "approved_by": approved_by,
        "approved_at": approved_at,
        "expires_at": expires_at,
        "approval_scope": {
            "command_plan_id": operator_summary.get("command_plan_id"),
            "tool": operator_summary.get("tool"),
            "operation": operator_summary.get("operation"),
            "target_id": operator_summary.get("target_id"),
            "scope_id": operator_summary.get("scope_id"),
        },
        "real_execution_allowed": False,
        "evidence_required": True,
        "conditions": [
            "This approval record does not permit real execution in the current MVP.",
            "Real execution remains blocked by readiness gate and dry-run command plan policy.",
            "Operator decision is recorded for review workflow validation only.",
        ],
        "operator_notes": "Generated MVP approval record for review workflow validation.",
    }


def evaluate_human_approval_gate(
    operator_summary: dict[str, Any],
    approval_record: dict[str, Any],
) -> dict[str, Any]:
    validate_human_approval_record(approval_record)

    mismatches: list[str] = []
    for field in BINDING_FIELDS:
        if operator_summary.get(field) != approval_record.get(field):
            mismatches.append(field)

    scope = approval_record.get("approval_scope", {})
    for field in BINDING_FIELDS:
        if approval_record.get(field) != scope.get(field):
            mismatches.append(f"approval_scope.{field}")

    if mismatches:
        raise HumanApprovalError(f"human approval record binding mismatch: {sorted(set(mismatches))}")

    decision = approval_record["approval_decision"]
    approval_satisfied = decision == "approved"

    if decision == "approved":
        gate_status = "approval_recorded_but_real_execution_still_blocked"
        recommendation = "continue_readiness_review"
    elif decision == "rejected":
        gate_status = "rejected"
        recommendation = "do_not_execute"
    elif decision == "needs_more_info":
        gate_status = "needs_more_info"
        recommendation = "request_additional_information"
    else:
        gate_status = "keep_blocked"
        recommendation = "do_not_execute"

    return {
        "gate_type": "human_approval_gate",
        "gate_status": gate_status,
        "approval_satisfied": approval_satisfied,
        "approval_decision": decision,
        "decision_recommendation": recommendation,
        "approved_by": approval_record["approved_by"],
        "approval_record_id": approval_record["approval_record_id"],
        "command_plan_id": approval_record["command_plan_id"],
        "tool": approval_record["tool"],
        "operation": approval_record["operation"],
        "target_id": approval_record["target_id"],
        "scope_id": approval_record["scope_id"],
        "real_execution_allowed_by_approval_record": approval_record["real_execution_allowed"],
        "real_execution_permitted": False,
        "evidence_required": approval_record["evidence_required"],
    }


def format_human_approval_markdown(record: dict[str, Any], gate_result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Human Approval Record")
    lines.append("")
    lines.append(f"- Approval record ID: `{record['approval_record_id']}`")
    lines.append(f"- Approval decision: `{record['approval_decision']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Real execution permitted: `{gate_result['real_execution_permitted']}`")
    lines.append(f"- Approved by: `{record['approved_by']}`")
    lines.append(f"- Approved at: `{record['approved_at']}`")
    lines.append(f"- Expires at: `{record['expires_at']}`")
    lines.append(f"- Tool: `{record['tool']}`")
    lines.append(f"- Operation: `{record['operation']}`")
    lines.append(f"- Target ID: `{record['target_id']}`")
    lines.append(f"- Scope ID: `{record['scope_id']}`")
    lines.append(f"- Command plan ID: `{record['command_plan_id']}`")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    for condition in record["conditions"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Operator Notes")
    lines.append("")
    lines.append(record.get("operator_notes", ""))
    lines.append("")
    return "\n".join(lines)
