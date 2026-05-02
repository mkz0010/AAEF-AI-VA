from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from delivery_authorization import (
    build_delivery_authorization_record,
    build_delivery_package,
    evaluate_delivery_authorization_gate,
)
from evidence_chain import build_evidence_chain
from evidence_reconstruction_report import build_evidence_reconstruction_report
from finding_candidate import build_finding_candidate_from_sanitized_artifact
from finding_review import build_finding_review_record, evaluate_finding_review_gate
from gateway import run_mock_tool_gateway
from human_approval import build_human_approval_record, evaluate_human_approval_gate
from lifecycle_checkpoint import (
    build_lifecycle_checkpoint_summary,
    format_lifecycle_checkpoint_markdown,
    validate_lifecycle_checkpoint_summary,
)
from models import load_json
from operator_readiness_review import summarize_readiness_for_operator
from policy import load_default_vault_metadata
from real_execution_gate import evaluate_real_execution_readiness
from report_packet_review import (
    build_delivery_authorization_candidate,
    build_report_packet_review_record,
    evaluate_report_packet_review_gate,
)
from report_promotion import build_report_finding, evaluate_report_finding_promotion_gate
from report_review import (
    build_report_packet_candidate,
    build_report_review_record,
    evaluate_report_review_gate,
)
from sanitizer import sanitize_raw_artifact


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_demo_bundle() -> dict:
    example_dir = TGW / "examples"
    request = load_json(example_dir / "allowed-action.tool-action-request.json")
    authz = load_json(example_dir / "allowed-action.authorization-decision.json")

    result, evidence = run_mock_tool_gateway(request, authz, vault_metadata=load_default_vault_metadata())

    adapter = get_adapter("zap")
    command_plan = adapter.build_command_plan(request, authz, "mock-vault")
    readiness_result = evaluate_real_execution_readiness(command_plan)
    operator_review = summarize_readiness_for_operator(readiness_result)
    human_approval = build_human_approval_record(operator_review, approval_decision="keep_blocked")
    human_approval_gate = evaluate_human_approval_gate(operator_review, human_approval)

    chain_bundle = {
        "tool_action_request": request,
        "authorization_decision": authz,
        "tool_execution_result": result,
        "evidence_record": evidence,
        "operator_readiness_review": operator_review,
        "human_approval_record": human_approval,
        "human_approval_gate_result": human_approval_gate,
    }
    evidence_chain = build_evidence_chain(chain_bundle)
    reconstruction_report = build_evidence_reconstruction_report(evidence_chain, chain_bundle)

    raw_artifact = {
        "adapter": "zap",
        "mock_raw_output": True,
        "request": "GET /account HTTP/1.1\nHost: demo.local\nAuthorization: Bearer abcdefghijklmnopqrstuvwxyz\nCookie: sessionid=abc123456789; theme=dark\n",
        "response": "HTTP/1.1 200 OK\nSet-Cookie: sessionid=def987654321; HttpOnly\n\ncsrf_token=tok_1234567890abcdef internal_ip=192.168.10.5",
        "finding_observation": "Potential issue was observed in sanitized demo artifact. password=hunter2",
    }
    sanitized_artifact = sanitize_raw_artifact(
        raw_artifact,
        raw_artifact_ref="private-not-in-git/lifecycle-checkpoints/demo/raw-artifact.demo.json",
        sanitized_artifact_ref="private-not-in-git/lifecycle-checkpoints/demo/sanitized-artifact.generated.json",
    )
    finding_candidate = build_finding_candidate_from_sanitized_artifact(
        sanitized_artifact,
        tool="zap",
        operation="authenticated_crawl",
        target_id="webapp-demo-001",
        scope_id="scope-demo-001",
        evidence_id=evidence["evidence_id"],
    )
    finding_review = build_finding_review_record(finding_candidate, review_decision="confirmed")
    finding_review_gate = evaluate_finding_review_gate(finding_candidate, finding_review)

    report_finding = build_report_finding(finding_candidate, finding_review)
    promotion_gate = evaluate_report_finding_promotion_gate(finding_candidate, finding_review)

    report_review = build_report_review_record(
        report_finding,
        finding_candidate,
        finding_review,
        review_decision="approved_for_report_packet",
    )
    report_review_gate = evaluate_report_review_gate(report_finding, finding_candidate, finding_review, report_review)

    packet_candidate = build_report_packet_candidate(report_finding, report_review)
    packet_review = build_report_packet_review_record(
        packet_candidate,
        report_finding,
        report_review,
        review_decision="approved_for_delivery_authorization",
    )
    packet_review_gate = evaluate_report_packet_review_gate(packet_candidate, report_finding, report_review, packet_review)

    delivery_candidate = build_delivery_authorization_candidate(packet_candidate, packet_review)
    delivery_authorization = build_delivery_authorization_record(
        delivery_candidate,
        packet_candidate,
        packet_review,
        authorization_decision="authorized_for_delivery_package",
    )
    delivery_gate = evaluate_delivery_authorization_gate(delivery_candidate, packet_candidate, packet_review, delivery_authorization)
    delivery_package = build_delivery_package(delivery_candidate, delivery_authorization)

    return {
        "readiness_result": readiness_result,
        "operator_review": operator_review,
        "human_approval_gate_result": human_approval_gate,
        "evidence_chain": evidence_chain,
        "reconstruction_report": reconstruction_report,
        "sanitized_artifact": sanitized_artifact,
        "finding_candidate": finding_candidate,
        "finding_review_gate_result": finding_review_gate,
        "report_finding_promotion_gate_result": promotion_gate,
        "report_review_gate_result": report_review_gate,
        "report_packet_review_gate_result": packet_review_gate,
        "delivery_authorization_gate_result": delivery_gate,
        "delivery_package": delivery_package,
    }


def main() -> int:
    bundle = build_demo_bundle()
    summary = build_lifecycle_checkpoint_summary(bundle)
    validate_lifecycle_checkpoint_summary(summary)

    out_dir = ROOT / "private-not-in-git" / "lifecycle-checkpoints" / "demo"
    summary_path = out_dir / "lifecycle-checkpoint.generated.json"
    markdown_path = out_dir / "lifecycle-checkpoint.generated.md"

    write_json(summary_path, summary)
    write_text(markdown_path, format_lifecycle_checkpoint_markdown(summary))

    print(f"lifecycle checkpoint json: {summary_path}")
    print(f"lifecycle checkpoint md:   {markdown_path}")
    print(f"lifecycle checkpoint status: {summary['checkpoint_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
