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
from report_promotion import build_report_finding
from report_review import (
    build_report_packet_candidate,
    build_report_review_record,
    evaluate_report_review_gate,
    format_report_review_markdown,
)
from sanitizer import sanitize_raw_artifact


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    report_review_decision = sys.argv[1] if len(sys.argv) > 1 else "approved_for_report_packet"

    raw = {
        "adapter": "zap",
        "mock_raw_output": True,
        "request": "GET /account HTTP/1.1\nHost: demo.local\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789; theme=dark\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321; HttpOnly\n\ncsrf_token=tok_1234567890abcdef internal_ip=192.168.10.5",
        "finding_observation": "Potential issue was observed in sanitized demo artifact. password=hunter2",
    }

    out_dir = ROOT / "private-not-in-git" / "report-reviews" / "demo"
    raw_path = out_dir / "raw-artifact.demo.json"
    sanitized_path = out_dir / "sanitized-artifact.generated.json"
    candidate_path = out_dir / "finding-candidate.generated.json"
    finding_review_path = out_dir / "finding-review.generated.json"
    report_finding_path = out_dir / "report-finding.generated.json"
    report_review_path = out_dir / "report-review.generated.json"
    gate_path = out_dir / "report-review-gate-result.generated.json"
    packet_candidate_path = out_dir / "report-packet-candidate.generated.json"
    md_path = out_dir / "report-review.generated.md"

    write_json(raw_path, raw)
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/report-reviews/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/report-reviews/demo/sanitized-artifact.generated.json",
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

    finding_review = build_finding_review_record(candidate, review_decision="confirmed")
    write_json(finding_review_path, finding_review)

    report_finding = build_report_finding(candidate, finding_review)
    write_json(report_finding_path, report_finding)

    report_review = build_report_review_record(
        report_finding,
        candidate,
        finding_review,
        review_decision=report_review_decision,
    )
    write_json(report_review_path, report_review)

    gate = evaluate_report_review_gate(report_finding, candidate, finding_review, report_review)
    write_json(gate_path, gate)
    write_text(md_path, format_report_review_markdown(report_review, gate))

    if gate["report_packet_candidate_created"]:
        packet_candidate = build_report_packet_candidate(report_finding, report_review)
        write_json(packet_candidate_path, packet_candidate)
        print(f"report packet candidate: {packet_candidate_path}")

    print(f"report finding: {report_finding_path}")
    print(f"report review:  {report_review_path}")
    print(f"report gate:    {gate_path}")
    print(f"report review md: {md_path}")
    print(f"report review gate status: {gate['gate_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
