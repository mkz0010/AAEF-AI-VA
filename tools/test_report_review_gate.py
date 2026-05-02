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

from finding_candidate import build_finding_candidate_from_sanitized_artifact
from finding_review import build_finding_review_record
from report_promotion import build_report_finding
from report_review import (
    ReportReviewError,
    build_report_packet_candidate,
    build_report_review_record,
    evaluate_report_review_gate,
    format_report_review_markdown,
    validate_report_packet_candidate,
    validate_report_review_record,
)
from sanitizer import sanitize_raw_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_report_review_error(fn, message: str) -> None:
    try:
        fn()
    except ReportReviewError:
        return
    raise AssertionError(message)


def build_demo_report_finding() -> tuple[dict, dict, dict]:
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
    return candidate, finding_review, report_finding


def main() -> int:
    candidate, finding_review, report_finding = build_demo_report_finding()

    approved_review = build_report_review_record(
        report_finding,
        candidate,
        finding_review,
        review_decision="approved_for_report_packet",
    )
    gate = evaluate_report_review_gate(report_finding, candidate, finding_review, approved_review)

    assert_true(gate["gate_status"] == "approved_for_report_packet_candidate", "approved gate status mismatch")
    assert_true(gate["report_packet_candidate_created"] is True, "approved review should create packet candidate")
    assert_true(gate["requires_packet_review"] is True, "packet review should be required")
    assert_true(gate["customer_delivery_ready"] is False, "customer delivery must not be ready")
    assert_true(gate["report_ready"] is False, "report must not be ready")
    assert_true(gate["secret_exposed_to_ai"] is False, "secret exposure must remain false")

    packet_candidate = build_report_packet_candidate(report_finding, approved_review)
    assert_true(packet_candidate["report_packet_candidate_status"] == "packet_review_required", "packet status mismatch")
    assert_true(packet_candidate["requires_packet_review"] is True, "packet candidate must require review")
    assert_true(packet_candidate["customer_delivery_ready"] is False, "packet candidate must not be delivery-ready")
    assert_true(packet_candidate["report_ready"] is False, "packet candidate must not be report-ready")
    validate_report_packet_candidate(packet_candidate, report_finding, approved_review)

    for decision, expected_status in [
        ("needs_revision", "needs_revision"),
        ("rejected", "rejected"),
    ]:
        review = build_report_review_record(report_finding, candidate, finding_review, review_decision=decision)
        gate = evaluate_report_review_gate(report_finding, candidate, finding_review, review)
        assert_true(gate["gate_status"] == expected_status, f"{decision} gate status mismatch")
        assert_true(gate["report_packet_candidate_created"] is False, f"{decision} should not create packet candidate")
        assert_true(gate["customer_delivery_ready"] is False, f"{decision} should not be delivery-ready")
        assert_true(gate["report_ready"] is False, f"{decision} should not be report-ready")
        expect_report_review_error(
            lambda review=review: build_report_packet_candidate(report_finding, review),
            f"{decision} should not build packet candidate",
        )

    bad = copy.deepcopy(approved_review)
    bad["target_id"] = "other-target"
    expect_report_review_error(
        lambda: validate_report_review_record(report_finding, candidate, finding_review, bad),
        "target mismatch should fail closed",
    )

    bad = copy.deepcopy(approved_review)
    bad["review_scope"]["operation"] = "other-operation"
    expect_report_review_error(
        lambda: validate_report_review_record(report_finding, candidate, finding_review, bad),
        "review scope mismatch should fail closed",
    )

    bad = copy.deepcopy(approved_review)
    bad["customer_delivery_ready"] = True
    expect_report_review_error(
        lambda: validate_report_review_record(report_finding, candidate, finding_review, bad),
        "customer_delivery_ready true should fail closed",
    )

    bad = copy.deepcopy(approved_review)
    bad["report_ready"] = True
    expect_report_review_error(
        lambda: validate_report_review_record(report_finding, candidate, finding_review, bad),
        "report_ready true should fail closed",
    )

    bad = copy.deepcopy(approved_review)
    bad["review_notes"] = "Leaked Authorization: Bearer abcdefghijklmnopqrstuvwxyz"
    expect_report_review_error(
        lambda: validate_report_review_record(report_finding, candidate, finding_review, bad),
        "forbidden literal should fail closed",
    )

    markdown = format_report_review_markdown(approved_review, gate)
    assert_true("# Report Review" in markdown, "report review markdown title missing")
    assert_true("Report packet candidate created" in markdown, "packet candidate flag missing")
    assert_true("Customer delivery ready" in markdown, "delivery readiness missing")
    assert_true("Report ready" in markdown, "report readiness missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_report_review_demo.py")], check=True)

    generated_review = ROOT / "private-not-in-git" / "report-reviews" / "demo" / "report-review.generated.json"
    generated_gate = ROOT / "private-not-in-git" / "report-reviews" / "demo" / "report-review-gate-result.generated.json"
    generated_packet = ROOT / "private-not-in-git" / "report-reviews" / "demo" / "report-packet-candidate.generated.json"
    generated_md = ROOT / "private-not-in-git" / "report-reviews" / "demo" / "report-review.generated.md"

    assert_true(generated_review.exists(), "generated report review missing")
    assert_true(generated_gate.exists(), "generated report review gate missing")
    assert_true(generated_packet.exists(), "generated report packet candidate missing")
    assert_true(generated_md.exists(), "generated report review markdown missing")

    generated = json.loads(generated_gate.read_text(encoding="utf-8"))
    assert_true(generated["customer_delivery_ready"] is False, "generated gate should not be delivery-ready")
    assert_true(generated["report_ready"] is False, "generated gate should not be report-ready")

    print("Report review gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
