from __future__ import annotations

import json
from typing import Any

from finding_candidate import validate_finding_candidate
from finding_review import evaluate_finding_review_gate, validate_finding_review_record


class ReportPromotionError(ValueError):
    pass


REQUIRED_REPORT_FINDING_FIELDS = [
    "report_finding_id",
    "report_finding_status",
    "finding_candidate_id",
    "finding_review_id",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "title",
    "summary",
    "severity",
    "confidence",
    "promotion_basis",
    "requires_report_review",
    "customer_delivery_ready",
    "report_ready",
    "secret_exposed_to_ai",
    "evidence_required",
    "review_notes",
    "limitations",
]


BINDING_FIELDS = [
    "finding_candidate_id",
    "source_sanitized_artifact_ref",
    "tool",
    "operation",
    "target_id",
    "scope_id",
]


def build_report_finding(
    candidate: dict[str, Any],
    review_record: dict[str, Any],
) -> dict[str, Any]:
    validate_finding_candidate(candidate)
    validate_finding_review_record(candidate, review_record)
    review_gate = evaluate_finding_review_gate(candidate, review_record)

    if review_gate.get("eligible_for_report_promotion") is not True:
        raise ReportPromotionError("finding review is not eligible for report finding promotion")

    if review_record.get("review_decision") != "confirmed":
        raise ReportPromotionError("only confirmed finding reviews can be promoted")

    report_finding = {
        "report_finding_id": f"report-finding-{review_record['finding_review_id']}",
        "report_finding_status": "report_review_required",
        "finding_candidate_id": candidate["finding_candidate_id"],
        "finding_review_id": review_record["finding_review_id"],
        "source_sanitized_artifact_ref": candidate["source_sanitized_artifact_ref"],
        "tool": candidate["tool"],
        "operation": candidate["operation"],
        "target_id": candidate["target_id"],
        "scope_id": candidate["scope_id"],
        "title": candidate["title"],
        "summary": (
            "This report finding was promoted from a confirmed sanitized finding candidate. "
            "It still requires report review before customer delivery."
        ),
        "severity": candidate.get("initial_severity", "informational"),
        "confidence": candidate.get("initial_confidence", "low"),
        "promotion_basis": {
            "finding_candidate_id": candidate["finding_candidate_id"],
            "finding_review_id": review_record["finding_review_id"],
            "review_decision": review_record["review_decision"],
            "reviewed_by": review_record["reviewed_by"],
            "source_sanitized_artifact_ref": candidate["source_sanitized_artifact_ref"],
        },
        "requires_report_review": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "review_notes": review_record["review_notes"],
        "limitations": [
            "This report finding is not customer-delivery-ready.",
            "Severity and confidence remain conservative until report review.",
            "Raw adapter output is not embedded in this report finding.",
            "Human report review is required before customer-facing use.",
        ],
    }

    validate_report_finding(report_finding, candidate, review_record)
    return report_finding


def validate_report_finding(
    report_finding: dict[str, Any],
    candidate: dict[str, Any],
    review_record: dict[str, Any],
) -> None:
    validate_finding_candidate(candidate)
    validate_finding_review_record(candidate, review_record)

    missing = [field for field in REQUIRED_REPORT_FINDING_FIELDS if field not in report_finding]
    if missing:
        raise ReportPromotionError(f"report finding missing required fields: {missing}")

    for field in BINDING_FIELDS:
        if report_finding.get(field) != candidate.get(field):
            raise ReportPromotionError(f"report finding candidate binding mismatch: {field}")
        if report_finding.get(field) != review_record.get(field):
            raise ReportPromotionError(f"report finding review binding mismatch: {field}")

    if report_finding.get("finding_review_id") != review_record.get("finding_review_id"):
        raise ReportPromotionError("report finding must bind to finding_review_id")

    if report_finding.get("requires_report_review") is not True:
        raise ReportPromotionError("report finding must require report review")

    if report_finding.get("customer_delivery_ready") is not False:
        raise ReportPromotionError("report finding must not be customer-delivery-ready in current MVP")

    if report_finding.get("report_ready") is not False:
        raise ReportPromotionError("report finding must keep report_ready=false in current MVP")

    if report_finding.get("secret_exposed_to_ai") is not False:
        raise ReportPromotionError("report finding must keep secret_exposed_to_ai=false")

    if report_finding.get("evidence_required") is not True:
        raise ReportPromotionError("report finding must require evidence")

    if "raw_artifact_ref" in report_finding:
        raise ReportPromotionError("report finding must not embed raw_artifact_ref")

    serialized = json.dumps(report_finding, ensure_ascii=False)
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
            raise ReportPromotionError(f"report finding contains forbidden literal: {literal}")


def evaluate_report_finding_promotion_gate(
    candidate: dict[str, Any],
    review_record: dict[str, Any],
) -> dict[str, Any]:
    validate_finding_candidate(candidate)
    validate_finding_review_record(candidate, review_record)
    review_gate = evaluate_finding_review_gate(candidate, review_record)

    if review_gate.get("eligible_for_report_promotion") is not True:
        return {
            "gate_type": "report_finding_promotion_gate",
            "gate_status": "not_promoted",
            "decision_recommendation": "do_not_create_report_finding",
            "finding_candidate_id": candidate["finding_candidate_id"],
            "finding_review_id": review_record["finding_review_id"],
            "review_decision": review_record["review_decision"],
            "report_finding_created": False,
            "requires_report_review": True,
            "customer_delivery_ready": False,
            "report_ready": False,
            "secret_exposed_to_ai": False,
            "evidence_required": True,
            "blockers": ["finding_review_not_confirmed"],
        }

    report_finding = build_report_finding(candidate, review_record)

    return {
        "gate_type": "report_finding_promotion_gate",
        "gate_status": "promoted_to_report_finding_review",
        "decision_recommendation": "send_to_report_review",
        "finding_candidate_id": candidate["finding_candidate_id"],
        "finding_review_id": review_record["finding_review_id"],
        "review_decision": review_record["review_decision"],
        "report_finding_id": report_finding["report_finding_id"],
        "report_finding_created": True,
        "requires_report_review": True,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "blockers": [],
    }


def format_report_finding_markdown(
    report_finding: dict[str, Any],
    gate_result: dict[str, Any],
) -> str:
    lines: list[str] = []
    lines.append("# Report Finding")
    lines.append("")
    lines.append(f"- Report finding ID: `{report_finding['report_finding_id']}`")
    lines.append(f"- Status: `{report_finding['report_finding_status']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Finding candidate ID: `{report_finding['finding_candidate_id']}`")
    lines.append(f"- Finding review ID: `{report_finding['finding_review_id']}`")
    lines.append(f"- Tool: `{report_finding['tool']}`")
    lines.append(f"- Operation: `{report_finding['operation']}`")
    lines.append(f"- Target ID: `{report_finding['target_id']}`")
    lines.append(f"- Scope ID: `{report_finding['scope_id']}`")
    lines.append(f"- Severity: `{report_finding['severity']}`")
    lines.append(f"- Confidence: `{report_finding['confidence']}`")
    lines.append(f"- Requires report review: `{report_finding['requires_report_review']}`")
    lines.append(f"- Customer delivery ready: `{report_finding['customer_delivery_ready']}`")
    lines.append(f"- Report ready: `{report_finding['report_ready']}`")
    lines.append(f"- Secret exposed to AI: `{report_finding['secret_exposed_to_ai']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(report_finding["summary"])
    lines.append("")
    lines.append("## Limitations")
    lines.append("")
    for limitation in report_finding["limitations"]:
        lines.append(f"- {limitation}")
    lines.append("")
    lines.append("## Review Notes")
    lines.append("")
    lines.append(report_finding["review_notes"])
    lines.append("")
    return "\n".join(lines)
