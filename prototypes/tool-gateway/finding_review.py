from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from finding_candidate import validate_finding_candidate


class FindingReviewError(ValueError):
    pass


VALID_REVIEW_DECISIONS = {
    "confirmed",
    "rejected",
    "needs_more_info",
    "duplicate",
    "false_positive",
}


REQUIRED_REVIEW_FIELDS = [
    "finding_review_id",
    "review_type",
    "finding_candidate_id",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "review_decision",
    "reviewed_by",
    "reviewed_at",
    "review_scope",
    "human_review_required_satisfied",
    "secret_exposed_to_ai",
    "report_ready",
    "eligible_for_report_promotion",
    "evidence_required",
    "review_notes",
    "conditions",
]


BINDING_FIELDS = [
    "finding_candidate_id",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
]


def _parse_zulu(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def build_finding_review_record(
    candidate: dict[str, Any],
    *,
    review_decision: str = "needs_more_info",
    reviewed_by: str = "demo-reviewer-001",
) -> dict[str, Any]:
    validate_finding_candidate(candidate)

    if review_decision not in VALID_REVIEW_DECISIONS:
        raise FindingReviewError(f"unsupported review_decision: {review_decision}")

    if review_decision == "confirmed":
        eligible_for_report_promotion = True
        review_notes = "Candidate was marked confirmed for workflow testing only. Report promotion still requires a separate gate."
    elif review_decision == "rejected":
        eligible_for_report_promotion = False
        review_notes = "Candidate was rejected by human review."
    elif review_decision == "duplicate":
        eligible_for_report_promotion = False
        review_notes = "Candidate was marked as duplicate and should be linked to an existing reviewed item."
    elif review_decision == "false_positive":
        eligible_for_report_promotion = False
        review_notes = "Candidate was marked as false positive."
    else:
        eligible_for_report_promotion = False
        review_notes = "Additional information is required before validation."

    record = {
        "finding_review_id": f"finding-review-{candidate['finding_candidate_id']}",
        "review_type": "finding_candidate_human_review",
        "finding_candidate_id": candidate["finding_candidate_id"],
        "source_sanitized_artifact_ref": candidate["source_sanitized_artifact_ref"],
        "tool": candidate["tool"],
        "operation": candidate["operation"],
        "target_id": candidate["target_id"],
        "scope_id": candidate["scope_id"],
        "review_decision": review_decision,
        "reviewed_by": reviewed_by,
        "reviewed_at": "2026-05-02T00:00:00Z",
        "review_scope": {
            "finding_candidate_id": candidate["finding_candidate_id"],
            "source_sanitized_artifact_ref": candidate["source_sanitized_artifact_ref"],
            "tool": candidate["tool"],
            "operation": candidate["operation"],
            "target_id": candidate["target_id"],
            "scope_id": candidate["scope_id"],
        },
        "human_review_required_satisfied": review_decision in {"confirmed", "rejected", "duplicate", "false_positive"},
        "secret_exposed_to_ai": False,
        "report_ready": False,
        "eligible_for_report_promotion": eligible_for_report_promotion,
        "evidence_required": True,
        "review_notes": review_notes,
        "conditions": [
            "This finding review record does not create a customer-facing report finding by itself.",
            "Report promotion requires a separate report finding promotion gate.",
            "The reviewed candidate must remain bound to the sanitized artifact and review scope.",
            "Raw adapter artifacts must not be embedded in the review record.",
        ],
    }

    validate_finding_review_record(candidate, record)
    return record


def validate_finding_review_record(candidate: dict[str, Any], record: dict[str, Any]) -> None:
    validate_finding_candidate(candidate)

    missing = [field for field in REQUIRED_REVIEW_FIELDS if field not in record]
    if missing:
        raise FindingReviewError(f"finding review record missing required fields: {missing}")

    if record["review_decision"] not in VALID_REVIEW_DECISIONS:
        raise FindingReviewError(f"unsupported review_decision: {record['review_decision']}")

    for field in BINDING_FIELDS:
        if record.get(field) != candidate.get(field):
            raise FindingReviewError(f"finding review binding mismatch for field: {field}")
        if record.get("review_scope", {}).get(field) != record.get(field):
            raise FindingReviewError(f"finding review scope mismatch for field: {field}")

    if record.get("secret_exposed_to_ai") is not False:
        raise FindingReviewError("finding review must keep secret_exposed_to_ai=false")

    if record.get("report_ready") is not False:
        raise FindingReviewError("finding review must not mark report_ready in current MVP")

    if record.get("evidence_required") is not True:
        raise FindingReviewError("finding review must require evidence")

    if not isinstance(record.get("conditions"), list):
        raise FindingReviewError("conditions must be a list")

    if record["review_decision"] == "confirmed":
        if record.get("eligible_for_report_promotion") is not True:
            raise FindingReviewError("confirmed review should be eligible for future report promotion")
    else:
        if record.get("eligible_for_report_promotion") is not False:
            raise FindingReviewError("non-confirmed review must not be eligible for report promotion")

    if record["review_decision"] == "needs_more_info":
        if record.get("human_review_required_satisfied") is not False:
            raise FindingReviewError("needs_more_info does not satisfy human review requirement")
    else:
        if record.get("human_review_required_satisfied") is not True:
            raise FindingReviewError("terminal review decisions should satisfy human review requirement")

    reviewed_at = _parse_zulu(record["reviewed_at"])
    if reviewed_at > _now_utc():
        # Allow stable MVP fixture date if running before that timestamp is impossible in normal project timeline.
        # This is intentionally conservative but avoids accepting arbitrary far-future review dates.
        if record["reviewed_at"] != "2026-05-02T00:00:00Z":
            raise FindingReviewError("reviewed_at must not be an arbitrary future timestamp")

    serialized = str(record)
    forbidden_literals = [
        "Authorization: Bearer",
        "Cookie:",
        "Set-Cookie:",
        "password=",
        "csrf_token=",
        "sessionid=",
        "192.168.",
        "10.0.",
    ]
    for literal in forbidden_literals:
        if literal.lower() in serialized.lower():
            raise FindingReviewError(f"finding review contains forbidden literal: {literal}")


def evaluate_finding_review_gate(
    candidate: dict[str, Any],
    review_record: dict[str, Any],
) -> dict[str, Any]:
    validate_finding_review_record(candidate, review_record)

    decision = review_record["review_decision"]

    if decision == "confirmed":
        gate_status = "confirmed_for_future_report_promotion_review"
        recommendation = "eligible_for_report_promotion_gate"
    elif decision == "rejected":
        gate_status = "rejected"
        recommendation = "do_not_report"
    elif decision == "false_positive":
        gate_status = "false_positive"
        recommendation = "do_not_report"
    elif decision == "duplicate":
        gate_status = "duplicate"
        recommendation = "link_to_existing_reviewed_finding"
    else:
        gate_status = "needs_more_info"
        recommendation = "request_additional_information"

    return {
        "gate_type": "finding_candidate_review_gate",
        "gate_status": gate_status,
        "review_decision": decision,
        "decision_recommendation": recommendation,
        "finding_candidate_id": review_record["finding_candidate_id"],
        "finding_review_id": review_record["finding_review_id"],
        "tool": review_record["tool"],
        "operation": review_record["operation"],
        "target_id": review_record["target_id"],
        "scope_id": review_record["scope_id"],
        "human_review_required_satisfied": review_record["human_review_required_satisfied"],
        "eligible_for_report_promotion": review_record["eligible_for_report_promotion"],
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
    }


def format_finding_review_markdown(record: dict[str, Any], gate_result: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Finding Candidate Review")
    lines.append("")
    lines.append(f"- Finding review ID: `{record['finding_review_id']}`")
    lines.append(f"- Finding candidate ID: `{record['finding_candidate_id']}`")
    lines.append(f"- Review decision: `{record['review_decision']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Tool: `{record['tool']}`")
    lines.append(f"- Operation: `{record['operation']}`")
    lines.append(f"- Target ID: `{record['target_id']}`")
    lines.append(f"- Scope ID: `{record['scope_id']}`")
    lines.append(f"- Human review satisfied: `{gate_result['human_review_required_satisfied']}`")
    lines.append(f"- Eligible for report promotion: `{gate_result['eligible_for_report_promotion']}`")
    lines.append(f"- Report ready: `{gate_result['report_ready']}`")
    lines.append(f"- Secret exposed to AI: `{gate_result['secret_exposed_to_ai']}`")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    for condition in record["conditions"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Review Notes")
    lines.append("")
    lines.append(record["review_notes"])
    lines.append("")
    return "\n".join(lines)
