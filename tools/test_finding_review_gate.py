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
from finding_review import (
    FindingReviewError,
    build_finding_review_record,
    evaluate_finding_review_gate,
    format_finding_review_markdown,
    validate_finding_review_record,
)
from sanitizer import sanitize_raw_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_review_error(candidate: dict, record: dict, message: str) -> None:
    try:
        validate_finding_review_record(candidate, record)
    except FindingReviewError:
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

    needs_more = build_finding_review_record(candidate, review_decision="needs_more_info")
    gate = evaluate_finding_review_gate(candidate, needs_more)
    assert_true(gate["gate_status"] == "needs_more_info", "needs_more_info gate status mismatch")
    assert_true(gate["human_review_required_satisfied"] is False, "needs_more_info should not satisfy human review")
    assert_true(gate["eligible_for_report_promotion"] is False, "needs_more_info should not be promotion eligible")
    assert_true(gate["report_ready"] is False, "finding review gate must not make report ready")

    confirmed = build_finding_review_record(candidate, review_decision="confirmed")
    gate = evaluate_finding_review_gate(candidate, confirmed)
    assert_true(
        gate["gate_status"] == "confirmed_for_future_report_promotion_review",
        "confirmed gate status mismatch",
    )
    assert_true(gate["human_review_required_satisfied"] is True, "confirmed should satisfy human review")
    assert_true(gate["eligible_for_report_promotion"] is True, "confirmed should be promotion eligible")
    assert_true(gate["report_ready"] is False, "confirmed review should still not be report-ready in MVP")

    for decision, expected_status in [
        ("rejected", "rejected"),
        ("duplicate", "duplicate"),
        ("false_positive", "false_positive"),
    ]:
        record = build_finding_review_record(candidate, review_decision=decision)
        gate = evaluate_finding_review_gate(candidate, record)
        assert_true(gate["gate_status"] == expected_status, f"{decision} gate status mismatch")
        assert_true(gate["eligible_for_report_promotion"] is False, f"{decision} should not be promotion eligible")
        assert_true(gate["report_ready"] is False, f"{decision} should not be report-ready")

    bad = copy.deepcopy(confirmed)
    bad["target_id"] = "other-target"
    expect_review_error(candidate, bad, "target mismatch should fail closed")

    bad = copy.deepcopy(confirmed)
    bad["review_scope"]["operation"] = "other-operation"
    expect_review_error(candidate, bad, "review scope mismatch should fail closed")

    bad = copy.deepcopy(confirmed)
    bad["report_ready"] = True
    expect_review_error(candidate, bad, "report_ready true should fail closed")

    bad = copy.deepcopy(confirmed)
    bad["secret_exposed_to_ai"] = True
    expect_review_error(candidate, bad, "secret_exposed_to_ai true should fail closed")

    bad = copy.deepcopy(confirmed)
    bad["evidence_required"] = False
    expect_review_error(candidate, bad, "evidence_required false should fail closed")

    bad = copy.deepcopy(confirmed)
    bad["review_notes"] = "Leaked Cookie: sessionid=abc123456789"
    expect_review_error(candidate, bad, "forbidden literal should fail closed")

    markdown = format_finding_review_markdown(needs_more, evaluate_finding_review_gate(candidate, needs_more))
    assert_true("# Finding Candidate Review" in markdown, "finding review markdown title missing")
    assert_true("Report ready" in markdown, "finding review markdown report readiness missing")
    assert_true("Secret exposed to AI" in markdown, "finding review markdown secret flag missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_finding_review_demo.py")], check=True)

    generated_review = ROOT / "private-not-in-git" / "finding-reviews" / "demo" / "finding-review.generated.json"
    generated_gate = ROOT / "private-not-in-git" / "finding-reviews" / "demo" / "finding-review-gate-result.generated.json"
    generated_md = ROOT / "private-not-in-git" / "finding-reviews" / "demo" / "finding-review.generated.md"

    assert_true(generated_review.exists(), "generated finding review missing")
    assert_true(generated_gate.exists(), "generated finding review gate missing")
    assert_true(generated_md.exists(), "generated finding review markdown missing")

    generated = json.loads(generated_gate.read_text(encoding="utf-8"))
    assert_true(generated["report_ready"] is False, "generated gate should not be report-ready")

    print("Finding review gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
