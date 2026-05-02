from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from finding_candidate import build_finding_candidate_from_sanitized_artifact
from finding_review import build_finding_review_record
from report_promotion import (
    build_report_finding,
    evaluate_report_finding_promotion_gate,
    format_report_finding_markdown,
)
from sanitizer import sanitize_raw_artifact


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    review_decision = sys.argv[1] if len(sys.argv) > 1 else "confirmed"

    raw = {
        "adapter": "zap",
        "mock_raw_output": True,
        "request": "GET /account HTTP/1.1\nHost: demo.local\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789; theme=dark\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321; HttpOnly\n\ncsrf_token=tok_1234567890abcdef internal_ip=192.168.10.5",
        "finding_observation": "Potential issue was observed in sanitized demo artifact. password=hunter2",
    }

    out_dir = ROOT / "private-not-in-git" / "report-findings" / "demo"
    raw_path = out_dir / "raw-artifact.demo.json"
    sanitized_path = out_dir / "sanitized-artifact.generated.json"
    candidate_path = out_dir / "finding-candidate.generated.json"
    review_path = out_dir / "finding-review.generated.json"
    gate_path = out_dir / "report-finding-promotion-gate.generated.json"
    report_finding_path = out_dir / "report-finding.generated.json"
    md_path = out_dir / "report-finding.generated.md"

    write_json(raw_path, raw)
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/report-findings/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/report-findings/demo/sanitized-artifact.generated.json",
    )
    write_json(sanitized_path, sanitized)

    candidate = build_finding_candidate_from_sanitized_artifact(
        sanitized,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id="evidence-demo-001",
    )
    write_json(candidate_path, candidate)

    review = build_finding_review_record(candidate, review_decision=review_decision)
    write_json(review_path, review)

    gate = evaluate_report_finding_promotion_gate(candidate, review)
    write_json(gate_path, gate)

    if gate["report_finding_created"]:
        report_finding = build_report_finding(candidate, review)
        write_json(report_finding_path, report_finding)
        write_text(md_path, format_report_finding_markdown(report_finding, gate))
        print(f"report finding: {report_finding_path}")
        print(f"report finding md: {md_path}")

    print(f"finding candidate: {candidate_path}")
    print(f"finding review:    {review_path}")
    print(f"promotion gate:    {gate_path}")
    print(f"promotion status:  {gate['gate_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
