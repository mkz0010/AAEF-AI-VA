from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from report_review import validate_report_packet_candidate


class ReportPacketReviewError(ValueError):
    pass


VALID_PACKET_REVIEW_DECISIONS = {
    "approved_for_delivery_authorization",
    "needs_revision",
    "rejected",
}


REQUIRED_PACKET_REVIEW_FIELDS = [
    "packet_review_id",
    "review_type",
    "report_packet_candidate_id",
    "report_finding_id",
    "report_review_id",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "review_decision",
    "reviewed_by",
    "reviewed_at",
    "review_scope",
    "delivery_authorization_candidate_allowed",
    "customer_delivery_ready",
    "report_ready",
    "secret_exposed_to_ai",
    "evidence_required",
    "review_notes",
    "conditions",
]


BINDING_FIELDS = [
    "report_packet_candidate_id",
    "report_finding_id",
    "report_review_id",
    "tool",
    "operation",
    "target_id",
    "scope_id",
]


def _parse_zulu(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _now_utc() -> datetime:
    return datetime.now(timezone.utc)


def build_report_packet_review_record(
    packet_candidate: dict,
    report_finding: dict,
    report_review_record: dict,
    *,
    review_decision: str = "needs_revision",
    reviewed_by: str = "demo-packet-reviewer-001",
) -> dict:
    validate_report_packet_candidate(packet_candidate, report_finding, report_review_record)

    if review_decision not in VALID_PACKET_REVIEW_DECISIONS:
        raise ReportPacketReviewError(f"unsupported packet review decision: {review_decision}")

    if review_decision == "approved_for_delivery_authorization":
        delivery_authorization_candidate_allowed = True
        review_notes = (
            "Report packet candidate was approved for delivery authorization review. "
            "Customer delivery is still not allowed."
        )
    elif review_decision == "rejected":
        delivery_authorization_candidate_allowed = False
        review_notes = "Report packet candidate was rejected during packet review."
    else:
        delivery_authorization_candidate_allowed = False
        review_notes = "Report packet candidate requires revision before delivery authorization review."

    record = {
        "packet_review_id": f"packet-review-{packet_candidate['report_packet_candidate_id']}",
        "review_type": "report_packet_candidate_review",
        "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
        "report_finding_id": packet_candidate["report_finding_id"],
        "report_review_id": packet_candidate["report_review_id"],
        "tool": packet_candidate["tool"],
        "operation": packet_candidate["operation"],
        "target_id": packet_candidate["target_id"],
        "scope_id": packet_candidate["scope_id"],
        "review_decision": review_decision,
        "reviewed_by": reviewed_by,
        "reviewed_at": "2026-05-02T00:00:00Z",
        "review_scope": {
            "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
            "report_finding_id": packet_candidate["report_finding_id"],
            "report_review_id": packet_candidate["report_review_id"],
            "tool": packet_candidate["tool"],
            "operation": packet_candidate["operation"],
            "target_id": packet_candidate["target_id"],
            "scope_id": packet_candidate["scope_id"],
        },
        "delivery_authorization_candidate_allowed": delivery_authorization_candidate_allowed,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "review_notes": review_notes,
        "conditions": [
            "This packet review record does not make the packet customer-delivery-ready.",
            "Approved packet review allows only delivery authorization candidate assembly.",
            "Customer delivery requires a separate delivery authorization gate.",
            "Raw adapter output must not be embedded in the packet review record.",
        ],
    }

    validate_report_packet_review_record(packet_candidate, report_finding, report_review_record, record)
    return record


def validate_report_packet_review_record(
    packet_candidate: dict,
    report_finding: dict,
    report_review_record: dict,
    packet_review_record: dict,
) -> None:
    validate_report_packet_candidate(packet_candidate, report_finding, report_review_record)

    missing = [field for field in REQUIRED_PACKET_REVIEW_FIELDS if field not in packet_review_record]
    if missing:
        raise ReportPacketReviewError(f"packet review record missing required fields: {missing}")

    if packet_review_record["review_decision"] not in VALID_PACKET_REVIEW_DECISIONS:
        raise ReportPacketReviewError(f"unsupported packet review decision: {packet_review_record['review_decision']}")

    for field in BINDING_FIELDS:
        if packet_review_record.get(field) != packet_candidate.get(field):
            raise ReportPacketReviewError(f"packet review binding mismatch for field: {field}")
        if packet_review_record.get("review_scope", {}).get(field) != packet_review_record.get(field):
            raise ReportPacketReviewError(f"packet review scope mismatch for field: {field}")

    if packet_review_record.get("secret_exposed_to_ai") is not False:
        raise ReportPacketReviewError("packet review must keep secret_exposed_to_ai=false")

    if packet_review_record.get("customer_delivery_ready") is not False:
        raise ReportPacketReviewError("packet review must not make customer_delivery_ready true")

    if packet_review_record.get("report_ready") is not False:
        raise ReportPacketReviewError("packet review must keep report_ready=false in current MVP")

    if packet_review_record.get("evidence_required") is not True:
        raise ReportPacketReviewError("packet review must require evidence")

    if not isinstance(packet_review_record.get("conditions"), list):
        raise ReportPacketReviewError("conditions must be a list")

    if packet_review_record["review_decision"] == "approved_for_delivery_authorization":
        if packet_review_record.get("delivery_authorization_candidate_allowed") is not True:
            raise ReportPacketReviewError("approved packet review should allow delivery authorization candidate assembly")
    else:
        if packet_review_record.get("delivery_authorization_candidate_allowed") is not False:
            raise ReportPacketReviewError("non-approved packet review must not allow delivery authorization candidate assembly")

    reviewed_at = _parse_zulu(packet_review_record["reviewed_at"])
    if reviewed_at > _now_utc():
        if packet_review_record["reviewed_at"] != "2026-05-02T00:00:00Z":
            raise ReportPacketReviewError("reviewed_at must not be an arbitrary future timestamp")

    serialized = str(packet_review_record)
    forbidden_literals = [
        "Authorization: Bearer",
        "Cookie:",
        "Set-Cookie:",
        "password=",
        "csrf_token=",
        "sessionid=",
        "api_key=",
        "192.168.",
        "10.0.",
    ]
    for literal in forbidden_literals:
        if literal.lower() in serialized.lower():
            raise ReportPacketReviewError(f"packet review contains forbidden literal: {literal}")


def build_delivery_authorization_candidate(
    packet_candidate: dict,
    packet_review_record: dict,
) -> dict:
    if packet_review_record.get("review_decision") != "approved_for_delivery_authorization":
        raise ReportPacketReviewError("delivery authorization candidate requires approved packet review decision")

    if packet_review_record.get("delivery_authorization_candidate_allowed") is not True:
        raise ReportPacketReviewError("delivery authorization candidate is not allowed by packet review record")

    candidate = {
        "delivery_authorization_candidate_id": f"delivery-authorization-candidate-{packet_review_record['packet_review_id']}",
        "delivery_authorization_candidate_status": "delivery_authorization_review_required",
        "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
        "packet_review_id": packet_review_record["packet_review_id"],
        "report_finding_id": packet_candidate["report_finding_id"],
        "report_review_id": packet_candidate["report_review_id"],
        "tool": packet_candidate["tool"],
        "operation": packet_candidate["operation"],
        "target_id": packet_candidate["target_id"],
        "scope_id": packet_candidate["scope_id"],
        "included_report_finding_ids": packet_candidate["included_report_finding_ids"],
        "requires_delivery_authorization": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "conditions": [
            "This delivery authorization candidate is not customer-delivery-ready.",
            "Customer delivery requires a separate delivery authorization gate.",
            "Delivery authorization must validate scope, evidence, redaction, and reviewer approval.",
        ],
    }

    validate_delivery_authorization_candidate(candidate, packet_candidate, packet_review_record)
    return candidate


def validate_delivery_authorization_candidate(
    delivery_candidate: dict,
    packet_candidate: dict,
    packet_review_record: dict,
) -> None:
    if delivery_candidate.get("report_packet_candidate_id") != packet_candidate.get("report_packet_candidate_id"):
        raise ReportPacketReviewError("delivery candidate report_packet_candidate_id mismatch")

    if delivery_candidate.get("packet_review_id") != packet_review_record.get("packet_review_id"):
        raise ReportPacketReviewError("delivery candidate packet_review_id mismatch")

    if delivery_candidate.get("requires_delivery_authorization") is not True:
        raise ReportPacketReviewError("delivery candidate must require delivery authorization")

    if delivery_candidate.get("customer_delivery_ready") is not False:
        raise ReportPacketReviewError("delivery candidate must not be customer-delivery-ready")

    if delivery_candidate.get("report_ready") is not False:
        raise ReportPacketReviewError("delivery candidate must keep report_ready=false")

    if delivery_candidate.get("secret_exposed_to_ai") is not False:
        raise ReportPacketReviewError("delivery candidate must keep secret_exposed_to_ai=false")

    if delivery_candidate.get("evidence_required") is not True:
        raise ReportPacketReviewError("delivery candidate must require evidence")


def evaluate_report_packet_review_gate(
    packet_candidate: dict,
    report_finding: dict,
    report_review_record: dict,
    packet_review_record: dict,
) -> dict:
    validate_report_packet_review_record(packet_candidate, report_finding, report_review_record, packet_review_record)

    decision = packet_review_record["review_decision"]

    if decision == "approved_for_delivery_authorization":
        delivery_candidate = build_delivery_authorization_candidate(packet_candidate, packet_review_record)
        return {
            "gate_type": "report_packet_review_gate",
            "gate_status": "approved_for_delivery_authorization_candidate",
            "decision_recommendation": "send_to_delivery_authorization_gate",
            "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
            "packet_review_id": packet_review_record["packet_review_id"],
            "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
            "delivery_authorization_candidate_created": True,
            "requires_delivery_authorization": True,
            "customer_delivery_ready": False,
            "report_ready": False,
            "secret_exposed_to_ai": False,
            "evidence_required": True,
            "blockers": [],
        }

    if decision == "rejected":
        status = "rejected"
        recommendation = "do_not_send_to_delivery_authorization"
        blockers = ["packet_review_rejected"]
    else:
        status = "needs_revision"
        recommendation = "revise_report_packet_candidate"
        blockers = ["report_packet_candidate_needs_revision"]

    return {
        "gate_type": "report_packet_review_gate",
        "gate_status": status,
        "decision_recommendation": recommendation,
        "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
        "packet_review_id": packet_review_record["packet_review_id"],
        "delivery_authorization_candidate_created": False,
        "requires_delivery_authorization": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "blockers": blockers,
    }


def format_report_packet_review_markdown(
    packet_review_record: dict,
    gate_result: dict,
) -> str:
    lines: list[str] = []
    lines.append("# Report Packet Review")
    lines.append("")
    lines.append(f"- Packet review ID: `{packet_review_record['packet_review_id']}`")
    lines.append(f"- Report packet candidate ID: `{packet_review_record['report_packet_candidate_id']}`")
    lines.append(f"- Review decision: `{packet_review_record['review_decision']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Delivery authorization candidate created: `{gate_result['delivery_authorization_candidate_created']}`")
    lines.append(f"- Requires delivery authorization: `{gate_result['requires_delivery_authorization']}`")
    lines.append(f"- Customer delivery ready: `{gate_result['customer_delivery_ready']}`")
    lines.append(f"- Report ready: `{gate_result['report_ready']}`")
    lines.append(f"- Secret exposed to AI: `{gate_result['secret_exposed_to_ai']}`")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    for condition in packet_review_record["conditions"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Review Notes")
    lines.append("")
    lines.append(packet_review_record["review_notes"])
    lines.append("")
    return "\n".join(lines)
