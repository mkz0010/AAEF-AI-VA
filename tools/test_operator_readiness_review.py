from __future__ import annotations

import subprocess
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


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_allowed_zap_readiness_result() -> dict:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    decision = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
    adapter = get_adapter("zap")
    plan = adapter.build_command_plan(request, decision, "mock-vault")
    return evaluate_real_execution_readiness(plan)


def main() -> int:
    readiness = load_allowed_zap_readiness_result()
    summary = summarize_readiness_for_operator(readiness)

    assert_true(summary["review_type"] == "real_execution_readiness_operator_review", "review type mismatch")
    assert_true(summary["review_status"] == "blocked", "default review should be blocked")
    assert_true(summary["decision_recommendation"] == "do_not_execute", "default recommendation should be do_not_execute")
    assert_true(summary["operator_notes_required"] is True, "operator notes should be required when blocked")
    assert_true(summary["blocker_count"] >= 1, "default readiness should have blockers")
    assert_true("real_execution_disabled" in summary["blockers"], "real execution disabled blocker missing")
    assert_true("command_plan_is_dry_run_only" in summary["blockers"], "dry-run blocker missing")
    assert_true("execution_enablement" in summary["blocker_categories"], "execution enablement category missing")
    assert_true("execution_mode" in summary["blocker_categories"], "execution mode category missing")
    assert_true(any(item["next_action"] for item in summary["next_actions"]), "next actions should be populated")

    markdown = format_operator_review_markdown(summary)
    assert_true("# Operator Readiness Review" in markdown, "markdown title missing")
    assert_true("Decision recommendation" in markdown, "markdown recommendation missing")
    assert_true("real_execution_disabled" in markdown, "markdown blocker missing")
    assert_true("Operator Decision" in markdown, "operator decision checklist missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_operator_readiness_review.py")], check=True)
    generated_md = ROOT / "private-not-in-git" / "operator-reviews" / "real-execution-readiness" / "operator-readiness-review.generated.md"
    generated_json = ROOT / "private-not-in-git" / "operator-reviews" / "real-execution-readiness" / "operator-readiness-review.generated.json"

    assert_true(generated_md.exists(), "generated operator review markdown missing")
    assert_true(generated_json.exists(), "generated operator review json missing")

    print("Operator readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
