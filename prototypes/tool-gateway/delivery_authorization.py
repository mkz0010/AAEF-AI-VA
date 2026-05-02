from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from report_packet_review import validate_delivery_authorization_candidate


class DeliveryAuthorizationError(ValueError):
    pass


VALID_DELIVERY_AUTHORIZATION_DECISIONS = {
    "authorized_for_delivery_package",
    "needs_revision",
    "rejected",
}


REQUIRED_AUTHORIZATION_FIELDS = [
    "delivery_authorization_id",
    "authorization_type",
    "delivery_authorization_candidate_id",
    "report_packet_candidate_id",
    "packet_review_id",
    "report_finding_id",
    "report_review_id",
    "tool",
    "operation",
    "target_id",
    "scope_id",
    "authorization_decision",
    "authorized_by",
    "authorized_at",
    "authorization_scope",
    "delivery_package_allowed",
    "delivery_dispatched",
    "customer_delivery_performed",
    "customer_delivery_ready",
    "report_ready",
    "secret_exposed_to_ai",
    "evidence_required",
    "authorization_notes",
    "conditions",
]


BINDING_FIELDS = [
    "delivery_authorization_candidate_id",
    "report_packet_candidate_id",
    "packet_review_id",
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


def build_delivery_authorization_record(
    delivery_candidate: dict[str, Any],
    packet_candidate: dict[str, Any],
    packet_review_record: dict[str, Any],
    *,
    authorization_decision: str = "needs_revision",
    authorized_by: str = "demo-delivery-authorizer-001",
) -> dict[str, Any]:
    validate_delivery_authorization_candidate(delivery_candidate, packet_candidate, packet_review_record)

    if authorization_decision not in VALID_DELIVERY_AUTHORIZATION_DECISIONS:
        raise DeliveryAuthorizationError(f"unsupported delivery authorization decision: {authorization_decision}")

    if authorization_decision == "authorized_for_delivery_package":
        delivery_package_allowed = True
        authorization_notes = (
            "Delivery authorization candidate was authorized for delivery package generation. "
            "No customer delivery or dispatch is performed in the current MVP."
        )
    elif authorization_decision == "rejected":
        delivery_package_allowed = False
        authorization_notes = "Delivery authorization candidate was rejected."
    else:
        delivery_package_allowed = False
        authorization_notes = "Delivery authorization candidate requires revision before package generation."

    record = {
        "delivery_authorization_id": f"delivery-authorization-{delivery_candidate['delivery_authorization_candidate_id']}",
        "authorization_type": "delivery_authorization_review",
        "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
        "report_packet_candidate_id": delivery_candidate["report_packet_candidate_id"],
        "packet_review_id": delivery_candidate["packet_review_id"],
        "report_finding_id": delivery_candidate["report_finding_id"],
        "report_review_id": delivery_candidate["report_review_id"],
        "tool": delivery_candidate["tool"],
        "operation": delivery_candidate["operation"],
        "target_id": delivery_candidate["target_id"],
        "scope_id": delivery_candidate["scope_id"],
        "authorization_decision": authorization_decision,
        "authorized_by": authorized_by,
        "authorized_at": "2026-05-02T00:00:00Z",
        "authorization_scope": {
            "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
            "report_packet_candidate_id": delivery_candidate["report_packet_candidate_id"],
            "packet_review_id": delivery_candidate["packet_review_id"],
            "report_finding_id": delivery_candidate["report_finding_id"],
            "report_review_id": delivery_candidate["report_review_id"],
            "tool": delivery_candidate["tool"],
            "operation": delivery_candidate["operation"],
            "target_id": delivery_candidate["target_id"],
            "scope_id": delivery_candidate["scope_id"],
        },
        "delivery_package_allowed": delivery_package_allowed,
        "delivery_dispatched": False,
        "customer_delivery_performed": False,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "authorization_notes": authorization_notes,
        "conditions": [
            "This authorization record allows package generation only when approved.",
            "It does not dispatch, transmit, or deliver anything to a customer.",
            "Customer delivery remains disabled in the current MVP.",
            "A future delivery dispatch/export control must be defined before any real delivery.",
            "Raw adapter output must not be embedded in the delivery authorization record.",
        ],
    }

    validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review_record, record)
    return record


def validate_delivery_authorization_record(
    delivery_candidate: dict[str, Any],
    packet_candidate: dict[str, Any],
    packet_review_record: dict[str, Any],
    authorization_record: dict[str, Any],
) -> None:
    validate_delivery_authorization_candidate(delivery_candidate, packet_candidate, packet_review_record)

    missing = [field for field in REQUIRED_AUTHORIZATION_FIELDS if field not in authorization_record]
    if missing:
        raise DeliveryAuthorizationError(f"delivery authorization record missing required fields: {missing}")

    if authorization_record["authorization_decision"] not in VALID_DELIVERY_AUTHORIZATION_DECISIONS:
        raise DeliveryAuthorizationError(
            f"unsupported delivery authorization decision: {authorization_record['authorization_decision']}"
        )

    for field in BINDING_FIELDS:
        if authorization_record.get(field) != delivery_candidate.get(field):
            raise DeliveryAuthorizationError(f"delivery authorization binding mismatch for field: {field}")
        if authorization_record.get("authorization_scope", {}).get(field) != authorization_record.get(field):
            raise DeliveryAuthorizationError(f"delivery authorization scope mismatch for field: {field}")

    if authorization_record.get("delivery_dispatched") is not False:
        raise DeliveryAuthorizationError("delivery authorization must not dispatch delivery in current MVP")

    if authorization_record.get("customer_delivery_performed") is not False:
        raise DeliveryAuthorizationError("delivery authorization must not perform customer delivery in current MVP")

    if authorization_record.get("customer_delivery_ready") is not False:
        raise DeliveryAuthorizationError("delivery authorization must not make customer_delivery_ready true")

    if authorization_record.get("report_ready") is not False:
        raise DeliveryAuthorizationError("delivery authorization must keep report_ready=false in current MVP")

    if authorization_record.get("secret_exposed_to_ai") is not False:
        raise DeliveryAuthorizationError("delivery authorization must keep secret_exposed_to_ai=false")

    if authorization_record.get("evidence_required") is not True:
        raise DeliveryAuthorizationError("delivery authorization must require evidence")

    if not isinstance(authorization_record.get("conditions"), list):
        raise DeliveryAuthorizationError("conditions must be a list")

    if authorization_record["authorization_decision"] == "authorized_for_delivery_package":
        if authorization_record.get("delivery_package_allowed") is not True:
            raise DeliveryAuthorizationError("authorized delivery should allow delivery package generation")
    else:
        if authorization_record.get("delivery_package_allowed") is not False:
            raise DeliveryAuthorizationError("non-authorized delivery must not allow delivery package generation")

    authorized_at = _parse_zulu(authorization_record["authorized_at"])
    if authorized_at > _now_utc():
        if authorization_record["authorized_at"] != "2026-05-02T00:00:00Z":
            raise DeliveryAuthorizationError("authorized_at must not be an arbitrary future timestamp")

    serialized = str(authorization_record)
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
            raise DeliveryAuthorizationError(f"delivery authorization contains forbidden literal: {literal}")


def build_delivery_package(
    delivery_candidate: dict[str, Any],
    authorization_record: dict[str, Any],
) -> dict[str, Any]:
    if authorization_record.get("authorization_decision") != "authorized_for_delivery_package":
        raise DeliveryAuthorizationError("delivery package requires authorized_for_delivery_package decision")

    if authorization_record.get("delivery_package_allowed") is not True:
        raise DeliveryAuthorizationError("delivery package is not allowed by authorization record")

    package = {
        "delivery_package_id": f"delivery-package-{authorization_record['delivery_authorization_id']}",
        "delivery_package_status": "package_generated_delivery_disabled",
        "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
        "delivery_authorization_id": authorization_record["delivery_authorization_id"],
        "report_packet_candidate_id": delivery_candidate["report_packet_candidate_id"],
        "packet_review_id": delivery_candidate["packet_review_id"],
        "report_finding_id": delivery_candidate["report_finding_id"],
        "report_review_id": delivery_candidate["report_review_id"],
        "tool": delivery_candidate["tool"],
        "operation": delivery_candidate["operation"],
        "target_id": delivery_candidate["target_id"],
        "scope_id": delivery_candidate["scope_id"],
        "included_report_finding_ids": delivery_candidate["included_report_finding_ids"],
        "package_generated": True,
        "delivery_dispatched": False,
        "customer_delivery_performed": False,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "requires_export_control_review": True,
        "conditions": [
            "This delivery package is generated for review workflow validation only.",
            "It is not customer-delivery-ready.",
            "It has not been dispatched or transmitted to a customer.",
            "A future export/delivery control is required before real customer delivery.",
        ],
    }

    validate_delivery_package(package, delivery_candidate, authorization_record)
    return package


def validate_delivery_package(
    delivery_package: dict[str, Any],
    delivery_candidate: dict[str, Any],
    authorization_record: dict[str, Any],
) -> None:
    if delivery_package.get("delivery_authorization_candidate_id") != delivery_candidate.get("delivery_authorization_candidate_id"):
        raise DeliveryAuthorizationError("delivery package candidate binding mismatch")

    if delivery_package.get("delivery_authorization_id") != authorization_record.get("delivery_authorization_id"):
        raise DeliveryAuthorizationError("delivery package authorization binding mismatch")

    if delivery_package.get("package_generated") is not True:
        raise DeliveryAuthorizationError("delivery package must record package_generated=true")

    if delivery_package.get("delivery_dispatched") is not False:
        raise DeliveryAuthorizationError("delivery package must not be dispatched in current MVP")

    if delivery_package.get("customer_delivery_performed") is not False:
        raise DeliveryAuthorizationError("delivery package must not perform customer delivery in current MVP")

    if delivery_package.get("customer_delivery_ready") is not False:
        raise DeliveryAuthorizationError("delivery package must not be customer-delivery-ready")

    if delivery_package.get("report_ready") is not False:
        raise DeliveryAuthorizationError("delivery package must keep report_ready=false")

    if delivery_package.get("secret_exposed_to_ai") is not False:
        raise DeliveryAuthorizationError("delivery package must keep secret_exposed_to_ai=false")

    if delivery_package.get("evidence_required") is not True:
        raise DeliveryAuthorizationError("delivery package must require evidence")

    if delivery_package.get("requires_export_control_review") is not True:
        raise DeliveryAuthorizationError("delivery package must require future export control review")


def evaluate_delivery_authorization_gate(
    delivery_candidate: dict[str, Any],
    packet_candidate: dict[str, Any],
    packet_review_record: dict[str, Any],
    authorization_record: dict[str, Any],
) -> dict[str, Any]:
    validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review_record, authorization_record)

    decision = authorization_record["authorization_decision"]

    if decision == "authorized_for_delivery_package":
        package = build_delivery_package(delivery_candidate, authorization_record)
        return {
            "gate_type": "delivery_authorization_gate",
            "gate_status": "authorized_for_delivery_package",
            "decision_recommendation": "generate_delivery_package_for_review",
            "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
            "delivery_authorization_id": authorization_record["delivery_authorization_id"],
            "delivery_package_id": package["delivery_package_id"],
            "delivery_package_created": True,
            "delivery_dispatched": False,
            "customer_delivery_performed": False,
            "customer_delivery_ready": False,
            "report_ready": False,
            "secret_exposed_to_ai": False,
            "evidence_required": True,
            "requires_export_control_review": True,
            "blockers": [],
        }

    if decision == "rejected":
        status = "rejected"
        recommendation = "do_not_generate_delivery_package"
        blockers = ["delivery_authorization_rejected"]
    else:
        status = "needs_revision"
        recommendation = "revise_delivery_authorization_candidate"
        blockers = ["delivery_authorization_candidate_needs_revision"]

    return {
        "gate_type": "delivery_authorization_gate",
        "gate_status": status,
        "decision_recommendation": recommendation,
        "delivery_authorization_candidate_id": delivery_candidate["delivery_authorization_candidate_id"],
        "delivery_authorization_id": authorization_record["delivery_authorization_id"],
        "delivery_package_created": False,
        "delivery_dispatched": False,
        "customer_delivery_performed": False,
        "customer_delivery_ready": False,
        "report_ready": False,
        "secret_exposed_to_ai": False,
        "evidence_required": True,
        "requires_export_control_review": True,
        "blockers": blockers,
    }


def format_delivery_authorization_markdown(
    authorization_record: dict[str, Any],
    gate_result: dict[str, Any],
) -> str:
    lines: list[str] = []
    lines.append("# Delivery Authorization")
    lines.append("")
    lines.append(f"- Delivery authorization ID: `{authorization_record['delivery_authorization_id']}`")
    lines.append(f"- Delivery authorization candidate ID: `{authorization_record['delivery_authorization_candidate_id']}`")
    lines.append(f"- Authorization decision: `{authorization_record['authorization_decision']}`")
    lines.append(f"- Gate status: `{gate_result['gate_status']}`")
    lines.append(f"- Decision recommendation: `{gate_result['decision_recommendation']}`")
    lines.append(f"- Delivery package created: `{gate_result['delivery_package_created']}`")
    lines.append(f"- Delivery dispatched: `{gate_result['delivery_dispatched']}`")
    lines.append(f"- Customer delivery performed: `{gate_result['customer_delivery_performed']}`")
    lines.append(f"- Customer delivery ready: `{gate_result['customer_delivery_ready']}`")
    lines.append(f"- Report ready: `{gate_result['report_ready']}`")
    lines.append(f"- Secret exposed to AI: `{gate_result['secret_exposed_to_ai']}`")
    lines.append(f"- Requires export control review: `{gate_result['requires_export_control_review']}`")
    lines.append("")
    lines.append("## Conditions")
    lines.append("")
    for condition in authorization_record["conditions"]:
        lines.append(f"- {condition}")
    lines.append("")
    lines.append("## Authorization Notes")
    lines.append("")
    lines.append(authorization_record["authorization_notes"])
    lines.append("")
    return "\n".join(lines)
