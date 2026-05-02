from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from models import load_json
from operator_readiness_review import format_operator_review_markdown, summarize_readiness_for_operator
from real_execution_gate import evaluate_real_execution_readiness


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    example_dir = TGW / "examples"
    request = load_json(example_dir / "allowed-action.tool-action-request.json")
    decision = load_json(example_dir / "allowed-action.authorization-decision.json")

    adapter = get_adapter("zap")
    command_plan = adapter.build_command_plan(request, decision, "mock-vault")
    readiness_result = evaluate_real_execution_readiness(command_plan)
    summary = summarize_readiness_for_operator(readiness_result)

    out_dir = ROOT / "private-not-in-git" / "operator-reviews" / "real-execution-readiness"
    json_path = out_dir / "operator-readiness-review.generated.json"
    md_path = out_dir / "operator-readiness-review.generated.md"

    write_json(json_path, summary)
    write_text(md_path, format_operator_review_markdown(summary))

    print(f"operator review json: {json_path}")
    print(f"operator review md:   {md_path}")
    print(f"operator review status: {summary['review_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
