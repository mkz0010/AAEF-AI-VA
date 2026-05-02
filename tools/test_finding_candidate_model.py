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

from finding_candidate import (
    FindingCandidateError,
    build_finding_candidate_from_sanitized_artifact,
    validate_finding_candidate,
)
from sanitizer import sanitize_raw_artifact


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_candidate_error(candidate: dict, message: str) -> None:
    try:
        validate_finding_candidate(candidate)
    except FindingCandidateError:
        return
    raise AssertionError(message)


def build_demo_sanitized_artifact() -> dict:
    raw = {
        "request": "GET /demo HTTP/1.1\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321\n\ncsrf_token=tok_1234567890abcdef 192.168.10.5",
        "body": "password=hunter2",
    }
    return sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/raw-artifacts/zap/demo.json",
        sanitized_artifact_ref="private-not-in-git/sanitized-artifacts/zap/demo.json",
    )


def main() -> int:
    sanitized = build_demo_sanitized_artifact()
    candidate = build_finding_candidate_from_sanitized_artifact(
        sanitized,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id="evidence-demo-001",
    )

    assert_true(candidate["finding_candidate_status"] == "candidate_requires_human_review", "candidate should require review")
    assert_true(candidate["ai_visible_allowed"] is True, "candidate should be AI-visible after sanitizer")
    assert_true(candidate["secret_exposed_to_ai"] is False, "candidate should not expose secret")
    assert_true(candidate["requires_human_review"] is True, "candidate should require human review")
    assert_true(candidate["report_ready"] is False, "candidate should not be report-ready")
    assert_true(candidate["initial_severity"] == "informational", "candidate severity should be conservative")
    assert_true(candidate["initial_confidence"] == "low", "candidate confidence should be conservative")
    assert_true("raw_artifact_ref" not in candidate, "candidate must not embed raw artifact ref")
    assert_true(candidate["redaction_summary"], "candidate should include redaction summary metadata")

    validate_finding_candidate(candidate)

    serialized = json.dumps(candidate, ensure_ascii=False)
    assert_true("Authorization: Bearer" not in serialized, "candidate should not include auth header")
    assert_true("Cookie:" not in serialized, "candidate should not include cookie header")
    assert_true("password=hunter2" not in serialized, "candidate should not include password")
    assert_true("192.168.10.5" not in serialized, "candidate should not include private IP")

    bad = copy.deepcopy(candidate)
    bad["report_ready"] = True
    expect_candidate_error(bad, "report_ready true should fail closed")

    bad = copy.deepcopy(candidate)
    bad["requires_human_review"] = False
    expect_candidate_error(bad, "requires_human_review false should fail closed")

    bad = copy.deepcopy(candidate)
    bad["secret_exposed_to_ai"] = True
    expect_candidate_error(bad, "secret_exposed_to_ai true should fail closed")

    bad = copy.deepcopy(candidate)
    bad["source_sanitized_artifact_ref"] = "tracked/sanitized.json"
    expect_candidate_error(bad, "tracked sanitized path should fail closed")

    bad = copy.deepcopy(candidate)
    bad["raw_artifact_ref"] = "private-not-in-git/raw-artifacts/zap/demo.json"
    expect_candidate_error(bad, "raw artifact ref embedded in candidate should fail closed")

    bad = copy.deepcopy(candidate)
    bad["summary"] = "Leaked Authorization: Bearer abcdefghijklmnopqrstuvwxyz"
    expect_candidate_error(bad, "forbidden literal should fail closed")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_finding_candidate_demo.py")], check=True)

    generated = ROOT / "private-not-in-git" / "finding-candidates" / "demo" / "finding-candidate.generated.json"
    assert_true(generated.exists(), "generated finding candidate missing")

    generated_data = json.loads(generated.read_text(encoding="utf-8"))
    assert_true(generated_data["finding_candidate_status"] == "candidate_requires_human_review", "generated candidate status mismatch")
    assert_true(generated_data["report_ready"] is False, "generated candidate should not be report-ready")

    print("Finding candidate model tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
