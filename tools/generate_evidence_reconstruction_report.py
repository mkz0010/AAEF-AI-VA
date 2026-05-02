from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from evidence_chain import build_evidence_chain
from evidence_reconstruction_report import (
    build_evidence_reconstruction_report,
    format_evidence_reconstruction_report_markdown,
)
from gateway import run_mock_tool_gateway
from human_approval import build_human_approval_record, evaluate_human_approval_gate
from models import load_json
from operator_readiness_review import summarize_readiness_for_operator
from policy import load_default_vault_metadata
from real_execution_gate import evaluate_real_execution_readiness


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    approval_decision = sys.argv[1] if len(sys.argv) > 1 else "keep_blocked"

    example_dir = TGW / "examples"
    request = load_json(example_dir / "allowed-action.tool-action-request.json")
    authz = load_json(example_dir / "allowed-action.authorization-decision.json")

    result, evidence = run_mock_tool_gateway(request, authz, vault_metadata=load_default_vault_metadata())

    adapter = get_adapter("zap")
    command_plan = adapter.build_command_plan(request, authz, "mock-vault")
    readiness_result = evaluate_real_execution_readiness(command_plan)
    operator_review = summarize_readiness_for_operator(readiness_result)
    approval_record = build_human_approval_record(operator_review, approval_decision=approval_decision)
    approval_gate_result = evaluate_human_approval_gate(operator_review, approval_record)

    bundle = {
        "tool_action_request": request,
        "authorization_decision": authz,
        "tool_execution_result": result,
        "evidence_record": evidence,
        "operator_readiness_review": operator_review,
        "human_approval_record": approval_record,
        "human_approval_gate_result": approval_gate_result,
    }

    chain = build_evidence_chain(bundle)
    report = build_evidence_reconstruction_report(chain, bundle)

    out_dir = ROOT / "private-not-in-git" / "reconstruction-reports" / "demo"
    report_path = out_dir / "evidence-reconstruction-report.generated.json"
    markdown_path = out_dir / "evidence-reconstruction-report.generated.md"

    write_json(report_path, report)
    write_text(markdown_path, format_evidence_reconstruction_report_markdown(report))

    print(f"reconstruction report json: {report_path}")
    print(f"reconstruction report md:   {markdown_path}")
    print(f"reconstruction conclusion: {report['conclusion']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
