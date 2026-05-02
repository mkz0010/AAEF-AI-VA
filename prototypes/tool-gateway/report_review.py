from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from report_promotion import validate_report_finding


class ReportReviewError(ValueError):
    pass


VALID_REPORT_REVIEW_DECISIONS = {
    "approved_for_report_packet",
    "needs_revision",
    "rejected",
}


REQUIRED_REPORT_REVIEW_FIELDS = [
    "report_review_id",
    "review_type",
    "report_finding_id",
    "finding_candidate_id",
    "finding_review_id",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "review_decision",
    "reviewed_by",
    "reviewed_at",
    "review_scope",
    "report_packet_candidate_allowed",
    "customer_delivery_ready",
    "report_ready",
    "secret_exposed_to_ai",
    "evidence_required",
    "review_notes",
    "conditions",
]


BINDING_FIELDS = [
    "report_finding_id",
    "finding_candidate_id",
    "finding_review_id",
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


def build_report_review_record(
    report_finding: dict[str, Any],
    candidate: dict[str, Any],
    finding_review_record: dict[str, Any],
    *,
    review_decision: str = "needs_revision",
    reviewed_by: str = "demo-report-reviewer-001",
) -> dict[str, Any]:
    validate_report_finding(report_finding, candidate, finding_review_record)

    if review_decision not in VALID_REPORT_REVIEW_DECISIONS:
        raise ReportReviewError(f"unsupported report review decision: {review_decision}")

    if review_decision == "approved_for_report_packet":
        report_packet_candidate_allowed = True
        review_notes = "Report finding was approved for report packet candidate assembly. Customer delivery is still not allowed."
    elif review_decision == "rejected":
        report_packet_candidate_allowed = False
        review_notes = "Report finding was rejected during report review."
    else:
        report_packet_candidate_allowed = False
        review_notes = "Report finding requires revision before it can be considered for a report packet candidate."

    record = {
        "report_review_id": f"report-review-{report_finding['report_finding_id']}",
        "review_type": "report_finding_review",
        "report_finding_id": report_finding["report_finding_id"],
        "finding_candidate_id": report_finding["finding_candidate_id"],
        "finding_review_id": report_finding["finding_review_id"],
        "source_sanitized_artifact_ref": report_finding["source_sanitized_artifact_ref"],
        "tool": report_finding["tool"],
        "operation": report_finding["operation"],
        "target_id": report_finding["target_id"],
        "scope_id": report_finding["scope_id"],
        "review_decision": review_decision,
        "reviewed_by": reviewed_by,
        "reviewed_at": "2026-05-02T00:00:00Z",
        "review_scope": {
            "report_finding_id": report_finding["report_finding_id"],
            "finding_candidate_id": report_finding["finding_candidate_id"],
            "finding_review_id": report_finding["finding_review_id"],
            "source_sanitized_artifact_ref": report_finding["source_sanitized_artifact_ref"],
            "tool": report_finding["tool"],
            "operation": report_finding["operation"],
            "target_id": report_finding["target_id"],
            "scope_id": report_finding["scope_id"],
        },
        "report_packet_candidate_allowed": report_packet_candidate_allowed,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "review_notes": review_notes,
        "conditions": [
            "This report review record does not make the finding customer-delivery-ready.",
            "Approved report review allows only report packet candidate assembly.",
            "Customer delivery requires a separate report packet review gate.",
            "Raw adapter output must not be embedded in the report review record.",
        ],
    }

    validate_report_review_record(report_finding, candidate, finding_review_record, record)
    return record


def validate_report_review_record(
    report_finding: dict[str, Any],
    candidate: dict[str, Any],
    finding_review_record: dict[str, Any],
    report_review_record: dict[str, Any],
) -> None:
    validate_report_finding(report_finding, candidate, finding_review_record)

    missing = [field for field in REQUIRED_REPORT_REVIEW_FIELDS if field not in report_review_record]
    if missing:
        raise ReportReviewError(f"report review record missing required fields: {missing}")

    if report_review_record["review_decision"] not in VALID_REPORT_REVIEW_DECISIONS:
        raise ReportReviewError(f"unsupported report review decision: {report_review_record['review_decision']}")

    for field in BINDING_FIELDS:
        if report_review_record.get(field) != report_finding.get(field):
            raise ReportReviewError(f"report review binding mismatch for field: {field}")
        if report_review_record.get("review_scope", {}).get(field) != report_review_record.get(field):
            raise ReportReviewError(f"report review scope mismatch for field: {field}")

    if report_review_record.get("secret_exposed_to_ai") is not False:
        raise ReportReviewError("report review must keep secret_exposed_to_ai=false")

    if report_review_record.get("customer_delivery_ready") is not False:
        raise ReportReviewError("report review must not make customer_delivery_ready true")

    if report_review_record.get("report_ready") is not False:
        raise ReportReviewError("report review must keep report_ready=false in current MVP")

    if report_review_record.get("evidence_required") is not True:
        raise ReportReviewError("report review must require evidence")

    if not isinstance(report_review_record.get("conditions"), list):
        raise ReportReviewError("conditions must be a list")

    if report_review_record["review_decision"] == "approved_for_report_packet":
        if report_review_record.get("report_packet_candidate_allowed") is not True:
            raise ReportReviewError("approved report review should allow report packet candidate assembly")
    else:
        if report_review_record.get("report_packet_candidate_allowed") is not False:
            raise ReportReviewError("non-approved report review must not allow report packet candidate assembly")

    reviewed_at = _parse_zulu(report_review_record["reviewed_at"])
    if reviewed_at > _now_utc():
        if report_review_record["reviewed_at"] != "2026-05-02T00:00:00Z":
            raise ReportReviewError("reviewed_at must not be an arbitrary future timestamp")

    serialized = str(report_review_record)
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
            raise ReportReviewError(f"report review contains forbidden literal: {literal}")


def build_report_packet_candidate(
    report_finding: dict[str, Any],
    report_review_record: dict[str, Any],
) -> dict[str, Any]:
    if report_review_record.get("review_decision") != "approved_for_report_packet":
        raise ReportReviewError("report packet candidate requires approved_for_report_packet review decision")

    if report_review_record.get("report_packet_candidate_allowed") is not True:
        raise ReportReviewError("report packet candidate is not allowed by report review record")

    candidate = {
        "report_packet_candidate_id": f"report-packet-candidate-{report_review_record['report_review_id']}",
        "report_packet_candidate_status": "packet_review_required",
        "report_finding_id": report_finding["report_finding_id"],
        "report_review_id": report_review_record["report_review_id"],
        "tool": report_finding["tool"],
        "operation": report_finding["operation"],
        "target_id": report_finding["target_id"],
        "scope_id": report_finding["scope_id"],
        "included_report_finding_ids": [report_finding["report_finding_id"]],
        "requires_packet_review": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "conditions": [
            "This report packet candidate is not customer-delivery-ready.",
            "Customer delivery requires a separate report packet review gate.",
            "Report finding content must remain bound to sanitized artifacts and evidence.",
        ],
    }

    validate_report_packet_candidate(candidate, report_finding, report_review_record)
    return candidate


def validate_report_packet_candidate(
    packet_candidate: dict[str, Any],
    report_finding: dict[str, Any],
    report_review_record: dict[str, Any],
) -> None:
    if packet_candidate.get("report_finding_id") != report_finding.get("report_finding_id"):
        raise ReportReviewError("packet candidate report_finding_id mismatch")

    if packet_candidate.get("report_review_id") != report_review_record.get("report_review_id"):
        raise ReportReviewError("packet candidate report_review_id mismatch")

    if packet_candidate.get("requires_packet_review") is not True:
        raise ReportReviewError("packet candidate must require packet review")

    if packet_candidate.get("customer_delivery_ready") is not False:
        raise ReportReviewError("packet candidate must not be customer-delivery-ready")

    if packet_candidate.get("report_ready") is not False:
        raise ReportReviewError("packet candidate must keep report_ready=false")

    if packet_candidate.get("secret_exposed_to_ai") is not False:
        raise ReportReviewError("packet candidate must keep secret_exposed_to_ai=false")

    if packet_candidate.get("evidence_required") is not True:
        raise ReportReviewError("packet candidate must require evidence")


def evaluate_report_review_gate(
    report_finding: dict[str, Any],
    candidate: dict[str, Any],
    finding_review_record: dict[str, Any],
    report_review_record: dict[str, Any],
) -> dict[str, Any]:
    validate_report_review_record(report_finding, candidate, finding_review_record, report_review_record)

    decision = report_review_record["review_decision"]

    if decision == "approved_for_report_packet":
        packet_candidate = build_report_packet_candidate(report_finding, report_review_record)
        return {
            "gate_type": "report_review_gate",
            "gate_status": "approved_for_report_packet_candidate",
            "decision_recommendation": "assemble_report_packet_candidate",
            "report_finding_id": report_finding["report_finding_id"],
            "report_review_id": report_review_record["report_review_id"],
            "report_packet_candidate_id": packet_candidate["report_packet_candidate_id"],
            "report_packet_candidate_created": True,
            "requires_packet_review": True,
            "customer_delivery_ready": False,
            "report_ready": False,
            "secret_exposed_to_ai": False,
            "evidence_required": True,
            "blockers": [],
        }

    if decision == "rejected":
        status = "rejected"
        recommendation = "do_not_include_in_report_packet"
        blockers = ["report_review_rejected"]
    else:
        status = "needs_revision"
        recommendation = "revise_report_finding"
        blockers = ["report_finding_needs_revision"]

    return {
        "gate_type": "report_review_gate",
        "gate_status": status,
        "decision_recommendation": recommendation,
        "report_finding_id": report_finding["report_finding_id"],
        "report_review_id": report_review_record["report_review_id"],
        "report_packet_candidate_created": False,
        "requires_packet_review": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "blockers": blockers,
    }


def format_report_review_markdown(
    report_review_record: dict[str, Any],
    gate_result: dict[str, Any],
) -> str:
    lines: list[str] = []
    lines.append("# Report Review")
    lines.append("")
    lines.append(f"- Report review ID: `{report_review_record['report_review_id']}`")
    lines.append(f"- Report finding ID: `{report_review_record['report_finding_id']}`")
    lines.append(f"- Review decision: `{report_review_record['review_decision']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Report packet candidate created: `{gate_result['report_packet_candidate_created']}`")
    lines.append(f"- Requires packet review: `{gate_result['requires_packet_review']}`")
    lines.append(f"- Customer delivery ready: `{gate_result['customer_delivery_ready']}`")
    lines.append(f"- Report ready: `{gate_result['report_ready']}`")
    lines.append(f"- Secret exposed to AI: `{gate_result['secret_exposed_to_ai']}`")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    for condition in report_review_record["conditions"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Review Notes")
    lines.append("")
    lines.append(report_review_record["review_notes"])
    lines.append("")
    return "\n".join(lines)
