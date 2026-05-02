from __future__ import annotations

import copy
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TGW = ROOT / "prototypes" / "tool-gateway"

if str(TGW) not in sys.path:
    sys.path.insert(0, str(TGW))

from adapters.registry import get_adapter
from human_approval import (
    HumanApprovalError,
    build_human_approval_record,
    evaluate_human_approval_gate,
    format_human_approval_markdown,
)
from models import load_json
from operator_readiness_review import summarize_readiness_for_operator
from real_execution_gate import evaluate_real_execution_readiness


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_approval_error(summary: dict, record: dict, message: str) -> None:
    try:
        evaluate_human_approval_gate(summary, record)
    except HumanApprovalError:
        return
    raise AssertionError(message)


def load_operator_summary() -> dict:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    decision = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
    adapter = get_adapter("zap")
    plan = adapter.build_command_plan(request, decision, "mock-vault")
    readiness = evaluate_real_execution_readiness(plan)
    return summarize_readiness_for_operator(readiness)


def main() -> int:
    summary = load_operator_summary()

    keep_blocked = build_human_approval_record(summary, approval_decision="keep_blocked")
    gate = evaluate_human_approval_gate(summary, keep_blocked)
    assert_true(gate["gate_status"] == "keep_blocked", "keep_blocked gate status mismatch")
    assert_true(gate["approval_satisfied"] is False, "keep_blocked should not satisfy approval")
    assert_true(gate["real_execution_permitted"] is False, "approval gate must not permit real execution")
    assert_true(gate["decision_recommendation"] == "do_not_execute", "keep_blocked recommendation mismatch")

    approved = build_human_approval_record(summary, approval_decision="approved")
    gate = evaluate_human_approval_gate(summary, approved)
    assert_true(gate["approval_satisfied"] is True, "approved decision should satisfy human approval")
    assert_true(gate["real_execution_permitted"] is False, "approved record must still not permit real execution in MVP")
    assert_true(
        gate["gate_status"] == "approval_recorded_but_real_execution_still_blocked",
        "approved MVP gate status mismatch",
    )

    rejected = build_human_approval_record(summary, approval_decision="rejected")
    gate = evaluate_human_approval_gate(summary, rejected)
    assert_true(gate["gate_status"] == "rejected", "rejected gate status mismatch")

    needs_more = build_human_approval_record(summary, approval_decision="needs_more_info")
    gate = evaluate_human_approval_gate(summary, needs_more)
    assert_true(gate["gate_status"] == "needs_more_info", "needs_more_info gate status mismatch")

    bad = copy.deepcopy(approved)
    bad["target_id"] = "other-target"
    expect_approval_error(summary, bad, "approval target mismatch should fail closed")

    bad = copy.deepcopy(approved)
    bad["approval_scope"]["operation"] = "other-operation"
    expect_approval_error(summary, bad, "approval scope mismatch should fail closed")

    bad = copy.deepcopy(approved)
    bad["real_execution_allowed"] = True
    expect_approval_error(summary, bad, "real_execution_allowed true should fail closed in MVP")

    bad = copy.deepcopy(approved)
    bad["evidence_required"] = False
    expect_approval_error(summary, bad, "evidence_required false should fail closed")

    bad = copy.deepcopy(approved)
    bad["expires_at"] = "2000-01-01T00:00:00Z"
    expect_approval_error(summary, bad, "expired approval should fail closed")

    markdown = format_human_approval_markdown(keep_blocked, evaluate_human_approval_gate(summary, keep_blocked))
    assert_true("# Human Approval Record" in markdown, "approval markdown title missing")
    assert_true("Real execution permitted" in markdown, "approval markdown execution field missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_human_approval_record.py")], check=True)

    generated_record = ROOT / "private-not-in-git" / "human-approvals" / "demo" / "human-approval-record.generated.json"
    generated_gate = ROOT / "private-not-in-git" / "human-approvals" / "demo" / "human-approval-gate-result.generated.json"
    generated_md = ROOT / "private-not-in-git" / "human-approvals" / "demo" / "human-approval-record.generated.md"

    assert_true(generated_record.exists(), "generated human approval record missing")
    assert_true(generated_gate.exists(), "generated human approval gate result missing")
    assert_true(generated_md.exists(), "generated human approval markdown missing")

    print("Human approval gate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
