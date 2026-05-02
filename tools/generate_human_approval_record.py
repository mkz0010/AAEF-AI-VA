from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from human_approval import build_human_approval_record, evaluate_human_approval_gate, format_human_approval_markdown
from models import load_json
from operator_readiness_review import summarize_readiness_for_operator
from real_execution_gate import evaluate_real_execution_readiness


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def main() -> int:
    decision = sys.argv[1] if len(sys.argv) > 1 else "keep_blocked"

    example_dir = TGW / "examples"
    request = load_json(example_dir / "allowed-action.tool-action-request.json")
    authz_decision = load_json(example_dir / "allowed-action.authorization-decision.json")

    adapter = get_adapter("zap")
    command_plan = adapter.build_command_plan(request, authz_decision, "mock-vault")
    readiness_result = evaluate_real_execution_readiness(command_plan)
    operator_summary = summarize_readiness_for_operator(readiness_result)

    approval_record = build_human_approval_record(operator_summary, approval_decision=decision)
    gate_result = evaluate_human_approval_gate(operator_summary, approval_record)

    out_dir = ROOT / "private-not-in-git" / "human-approvals" / "demo"
    record_path = out_dir / "human-approval-record.generated.json"
    gate_path = out_dir / "human-approval-gate-result.generated.json"
    md_path = out_dir / "human-approval-record.generated.md"

    write_json(record_path, approval_record)
    write_json(gate_path, gate_result)
    write_text(md_path, format_human_approval_markdown(approval_record, gate_result))

    print(f"human approval record: {record_path}")
    print(f"human approval gate:   {gate_path}")
    print(f"human approval md:     {md_path}")
    print(f"human approval status: {gate_result['gate_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
