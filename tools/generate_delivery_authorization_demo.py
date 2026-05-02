from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from delivery_authorization import (
    build_delivery_authorization_record,
    build_delivery_package,
    evaluate_delivery_authorization_gate,
    format_delivery_authorization_markdown,
)
from finding_candidate import build_finding_candidate_from_sanitized_artifact
from finding_review import build_finding_review_record
from report_packet_review import build_delivery_authorization_candidate, build_report_packet_review_record
from report_promotion import build_report_finding
from report_review import build_report_packet_candidate, build_report_review_record
from sanitizer import sanitize_raw_artifact


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    authorization_decision = sys.argv[1] if len(sys.argv) > 1 else "authorized_for_delivery_package"

    raw = {
        "adapter": "zap",
        "mock_raw_output": True,
        "request": "GET /account HTTP/1.1\nHost: demo.local\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789; theme=dark\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321; HttpOnly\n\ncsrf_token=tok_1234567890abcdef internal_ip=192.168.10.5",
        "finding_observation": "Potential issue was observed in sanitized demo artifact. password=hunter2",
    }

    out_dir = ROOT / "private-not-in-git" / "delivery-authorizations" / "demo"
    raw_path = out_dir / "raw-artifact.demo.json"
    sanitized_path = out_dir / "sanitized-artifact.generated.json"
    candidate_path = out_dir / "finding-candidate.generated.json"
    finding_review_path = out_dir / "finding-review.generated.json"
    report_finding_path = out_dir / "report-finding.generated.json"
    report_review_path = out_dir / "report-review.generated.json"
    packet_candidate_path = out_dir / "report-packet-candidate.generated.json"
    packet_review_path = out_dir / "report-packet-review.generated.json"
    delivery_candidate_path = out_dir / "delivery-authorization-candidate.generated.json"
    authorization_path = out_dir / "delivery-authorization.generated.json"
    gate_path = out_dir / "delivery-authorization-gate-result.generated.json"
    package_path = out_dir / "delivery-package.generated.json"
    md_path = out_dir / "delivery-authorization.generated.md"

    write_json(raw_path, raw)
    sanitized = sanitize_raw_artifact(
        raw,
        raw_artifact_ref="private-not-in-git/delivery-authorizations/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/delivery-authorizations/demo/sanitized-artifact.generated.json",
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
        review_decision="approved_for_report_packet",
    )
    write_json(report_review_path, report_review)

    packet_candidate = build_report_packet_candidate(report_finding, report_review)
    write_json(packet_candidate_path, packet_candidate)

    packet_review = build_report_packet_review_record(
        packet_candidate,
        report_finding,
        report_review,
        review_decision="approved_for_delivery_authorization",
    )
    write_json(packet_review_path, packet_review)

    delivery_candidate = build_delivery_authorization_candidate(packet_candidate, packet_review)
    write_json(delivery_candidate_path, delivery_candidate)

    authorization = build_delivery_authorization_record(
        delivery_candidate,
        packet_candidate,
        packet_review,
        authorization_decision=authorization_decision,
    )
    write_json(authorization_path, authorization)

    gate = evaluate_delivery_authorization_gate(delivery_candidate, packet_candidate, packet_review, authorization)
    write_json(gate_path, gate)
    write_text(md_path, format_delivery_authorization_markdown(authorization, gate))

    if gate["delivery_package_created"]:
        package = build_delivery_package(delivery_candidate, authorization)
        write_json(package_path, package)
        print(f"delivery package: {package_path}")

    print(f"delivery authorization candidate: {delivery_candidate_path}")
    print(f"delivery authorization:           {authorization_path}")
    print(f"delivery authorization gate:      {gate_path}")
    print(f"delivery authorization md:        {md_path}")
    print(f"delivery authorization gate status: {gate['gate_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
