from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from delivery_authorization import (
    DeliveryAuthorizationError,
    build_delivery_authorization_record,
    build_delivery_package,
    evaluate_delivery_authorization_gate,
    format_delivery_authorization_markdown,
    validate_delivery_authorization_record,
    validate_delivery_package,
)
from finding_candidate import build_finding_candidate_from_sanitized_artifact
from finding_review import build_finding_review_record
from report_packet_review import build_delivery_authorization_candidate, build_report_packet_review_record
from report_promotion import build_report_finding
from report_review import build_report_packet_candidate, build_report_review_record
from sanitizer import sanitize_raw_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_delivery_authorization_error(fn, message: str) -> None:
    try:
        fn()
    except DeliveryAuthorizationError:
        return
    raise AssertionError(message)


def build_demo_delivery_candidate() -> tuple[dict, dict, dict]:
    raw = {
        "request": "GET /demo HTTP/1.1\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321\n\ncsrf_token=tok_1234567890abcdef 192.168.10.5",
        "body": "password=hunter2",
    }
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/raw-artifacts/zap/demo.json",
        sanitized_artifact_ref="private-not-in-git/sanitized-artifacts/zap/demo.json",
    )
    candidate = build_finding_candidate_from_sanitized_artifact(
        sanitized,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id="evidence-demo-001",
    )
    finding_review = build_finding_review_record(candidate, review_decision="confirmed")
    report_finding = build_report_finding(candidate, finding_review)
    report_review = build_report_review_record(
        report_finding,
        candidate,
        finding_review,
        review_decision="approved_for_report_packet",
    )
    packet_candidate = build_report_packet_candidate(report_finding, report_review)
    packet_review = build_report_packet_review_record(
        packet_candidate,
        report_finding,
        report_review,
        review_decision="approved_for_delivery_authorization",
    )
    delivery_candidate = build_delivery_authorization_candidate(packet_candidate, packet_review)
    return delivery_candidate, packet_candidate, packet_review


def main() -> int:
    delivery_candidate, packet_candidate, packet_review = build_demo_delivery_candidate()

    authorized = build_delivery_authorization_record(
        delivery_candidate,
        packet_candidate,
        packet_review,
        authorization_decision="authorized_for_delivery_package",
    )
    gate = evaluate_delivery_authorization_gate(delivery_candidate, packet_candidate, packet_review, authorized)

    assert_true(gate["gate_status"] == "authorized_for_delivery_package", "authorized gate status mismatch")
    assert_true(gate["delivery_package_created"] is True, "authorized gate should create delivery package")
    assert_true(gate["delivery_dispatched"] is False, "delivery must not be dispatched")
    assert_true(gate["customer_delivery_performed"] is False, "customer delivery must not be performed")
    assert_true(gate["customer_delivery_ready"] is False, "customer delivery must not be ready")
    assert_true(gate["report_ready"] is False, "report must not be ready")
    assert_true(gate["requires_export_control_review"] is True, "export control review should be required")

    package = build_delivery_package(delivery_candidate, authorized)
    assert_true(package["delivery_package_status"] == "package_generated_delivery_disabled", "delivery package status mismatch")
    assert_true(package["package_generated"] is True, "delivery package should be generated")
    assert_true(package["delivery_dispatched"] is False, "delivery package must not dispatch")
    assert_true(package["customer_delivery_ready"] is False, "delivery package must not be customer-delivery-ready")
    assert_true(package["requires_export_control_review"] is True, "delivery package should require export control review")
    validate_delivery_package(package, delivery_candidate, authorized)

    for decision, expected_status in [
        ("needs_revision", "needs_revision"),
        ("rejected", "rejected"),
    ]:
        record = build_delivery_authorization_record(
            delivery_candidate,
            packet_candidate,
            packet_review,
            authorization_decision=decision,
        )
        gate = evaluate_delivery_authorization_gate(delivery_candidate, packet_candidate, packet_review, record)
        assert_true(gate["gate_status"] == expected_status, f"{decision} gate status mismatch")
        assert_true(gate["delivery_package_created"] is False, f"{decision} should not create package")
        assert_true(gate["customer_delivery_ready"] is False, f"{decision} should not be delivery-ready")
        assert_true(gate["report_ready"] is False, f"{decision} should not be report-ready")
        expect_delivery_authorization_error(
            lambda record=record: build_delivery_package(delivery_candidate, record),
            f"{decision} should not build package",
        )

    bad = copy.deepcopy(authorized)
    bad["target_id"] = "other-target"
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "target mismatch should fail closed",
    )

    bad = copy.deepcopy(authorized)
    bad["authorization_scope"]["operation"] = "other-operation"
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "authorization scope mismatch should fail closed",
    )

    bad = copy.deepcopy(authorized)
    bad["delivery_dispatched"] = True
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "delivery_dispatched true should fail closed",
    )

    bad = copy.deepcopy(authorized)
    bad["customer_delivery_ready"] = True
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "customer_delivery_ready true should fail closed",
    )

    bad = copy.deepcopy(authorized)
    bad["report_ready"] = True
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "report_ready true should fail closed",
    )

    bad = copy.deepcopy(authorized)
    bad["authorization_notes"] = "Leaked Authorization: Bearer abcdefghijklmnopqrstuvwxyz"
    expect_delivery_authorization_error(
        lambda: validate_delivery_authorization_record(delivery_candidate, packet_candidate, packet_review, bad),
        "forbidden literal should fail closed",
    )

    markdown = format_delivery_authorization_markdown(authorized, gate)
    assert_true("# Delivery Authorization" in markdown, "delivery authorization markdown title missing")
    assert_true("Delivery package created" in markdown, "package created flag missing")
    assert_true("Customer delivery ready" in markdown, "delivery readiness missing")
    assert_true("Delivery dispatched" in markdown, "dispatch flag missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_delivery_authorization_demo.py")], check=True)

    generated_auth = ROOT / "private-not-in-git" / "delivery-authorizations" / "demo" / "delivery-authorization.generated.json"
    generated_gate = ROOT / "private-not-in-git" / "delivery-authorizations" / "demo" / "delivery-authorization-gate-result.generated.json"
    generated_package = ROOT / "private-not-in-git" / "delivery-authorizations" / "demo" / "delivery-package.generated.json"
    generated_md = ROOT / "private-not-in-git" / "delivery-authorizations" / "demo" / "delivery-authorization.generated.md"

    assert_true(generated_auth.exists(), "generated delivery authorization missing")
    assert_true(generated_gate.exists(), "generated delivery authorization gate missing")
    assert_true(generated_package.exists(), "generated delivery package missing")
    assert_true(generated_md.exists(), "generated delivery authorization markdown missing")

    generated = json.loads(generated_gate.read_text(encoding="utf-8"))
    assert_true(generated["customer_delivery_ready"] is False, "generated gate should not be delivery-ready")
    assert_true(generated["delivery_dispatched"] is False, "generated gate should not dispatch delivery")
    assert_true(generated["report_ready"] is False, "generated gate should not be report-ready")

    print("Delivery authorization gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
