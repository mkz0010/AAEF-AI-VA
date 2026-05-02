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
from report_promotion import (
    ReportPromotionError,
    build_report_finding,
    evaluate_report_finding_promotion_gate,
    format_report_finding_markdown,
    validate_report_finding,
)
from sanitizer import sanitize_raw_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_promotion_error(fn, message: str) -> None:
    try:
        fn()
    except ReportPromotionError:
        return
    raise AssertionError(message)


def build_demo_candidate() -> dict:
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
    return build_finding_candidate_from_sanitized_artifact(
        sanitized,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id="evidence-demo-001",
    )


def main() -> int:
    candidate = build_demo_candidate()

    confirmed_review = build_finding_review_record(candidate, review_decision="confirmed")
    gate = evaluate_report_finding_promotion_gate(candidate, confirmed_review)

    assert_true(gate["gate_status"] == "promoted_to_report_finding_review", "confirmed review should promote")
    assert_true(gate["report_finding_created"] is True, "confirmed review should create report finding")
    assert_true(gate["requires_report_review"] is True, "report review should be required")
    assert_true(gate["customer_delivery_ready"] is False, "customer delivery should not be ready")
    assert_true(gate["report_ready"] is False, "report finding should not be report-ready")
    assert_true(gate["secret_exposed_to_ai"] is False, "secret exposure should remain false")

    report_finding = build_report_finding(candidate, confirmed_review)
    assert_true(report_finding["report_finding_status"] == "report_review_required", "report finding status mismatch")
    assert_true(report_finding["requires_report_review"] is True, "report finding must require review")
    assert_true(report_finding["customer_delivery_ready"] is False, "report finding must not be delivery-ready")
    assert_true(report_finding["report_ready"] is False, "report finding must not be report-ready")
    assert_true(report_finding["secret_exposed_to_ai"] is False, "report finding must not expose secret")
    validate_report_finding(report_finding, candidate, confirmed_review)

    for decision in ["rejected", "needs_more_info", "duplicate", "false_positive"]:
        review = build_finding_review_record(candidate, review_decision=decision)
        gate = evaluate_report_finding_promotion_gate(candidate, review)
        assert_true(gate["gate_status"] == "not_promoted", f"{decision} should not promote")
        assert_true(gate["report_finding_created"] is False, f"{decision} should not create report finding")
        expect_promotion_error(
            lambda review=review: build_report_finding(candidate, review),
            f"{decision} build_report_finding should fail",
        )

    bad_report = copy.deepcopy(report_finding)
    bad_report["report_ready"] = True
    expect_promotion_error(
        lambda: validate_report_finding(bad_report, candidate, confirmed_review),
        "report_ready true should fail closed",
    )

    bad_report = copy.deepcopy(report_finding)
    bad_report["customer_delivery_ready"] = True
    expect_promotion_error(
        lambda: validate_report_finding(bad_report, candidate, confirmed_review),
        "customer_delivery_ready true should fail closed",
    )

    bad_report = copy.deepcopy(report_finding)
    bad_report["target_id"] = "other-target"
    expect_promotion_error(
        lambda: validate_report_finding(bad_report, candidate, confirmed_review),
        "target mismatch should fail closed",
    )

    bad_report = copy.deepcopy(report_finding)
    bad_report["summary"] = "Leaked Authorization: Bearer abcdefghijklmnopqrstuvwxyz"
    expect_promotion_error(
        lambda: validate_report_finding(bad_report, candidate, confirmed_review),
        "forbidden literal should fail closed",
    )

    markdown = format_report_finding_markdown(report_finding, gate)
    assert_true("# Report Finding" in markdown, "report finding markdown title missing")
    assert_true("Customer delivery ready" in markdown, "delivery readiness should appear in markdown")
    assert_true("Report ready" in markdown, "report readiness should appear in markdown")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_report_finding_promotion_demo.py")], check=True)

    generated_report = ROOT / "private-not-in-git" / "report-findings" / "demo" / "report-finding.generated.json"
    generated_gate = ROOT / "private-not-in-git" / "report-findings" / "demo" / "report-finding-promotion-gate.generated.json"
    generated_md = ROOT / "private-not-in-git" / "report-findings" / "demo" / "report-finding.generated.md"

    assert_true(generated_report.exists(), "generated report finding missing")
    assert_true(generated_gate.exists(), "generated promotion gate missing")
    assert_true(generated_md.exists(), "generated report finding markdown missing")

    generated = json.loads(generated_report.read_text(encoding="utf-8"))
    assert_true(generated["report_ready"] is False, "generated report finding should not be report-ready")

    print("Report finding promotion gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
