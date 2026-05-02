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
from evidence_chain import build_evidence_chain
from evidence_reconstruction_report import (
    EvidenceReconstructionReportError,
    build_evidence_reconstruction_report,
    format_evidence_reconstruction_report_markdown,
)
from gateway import run_mock_tool_gateway
from human_approval import build_human_approval_record, evaluate_human_approval_gate
from models import load_json
from operator_readiness_review import summarize_readiness_for_operator
from policy import load_default_vault_metadata
from real_execution_gate import evaluate_real_execution_readiness


EXAMPLE_DIR = TGW / "examples"


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def expect_report_error(chain: dict, bundle: dict, message: str) -> None:
    try:
        build_evidence_reconstruction_report(chain, bundle)
    except EvidenceReconstructionReportError:
        return
    raise AssertionError(message)


def build_demo_chain_and_bundle(approval_decision: str = "keep_blocked") -> tuple[dict, dict]:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    authz = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
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
    return chain, bundle


def main() -> int:
    chain, bundle = build_demo_chain_and_bundle()
    report = build_evidence_reconstruction_report(chain, bundle)

    assert_true(report["report_type"] == "evidence_reconstruction_report", "report type mismatch")
    assert_true(report["report_status"] == "complete", "report status mismatch")
    assert_true(report["conclusion"] == "kept_blocked_after_review", "default conclusion mismatch")
    assert_true(report["real_execution_permitted"] is False, "report must not permit real execution")
    assert_true(report["secret_exposed_to_ai"] is False, "report must not expose secret to AI")
    assert_true(report["safety_assertions"]["model_output_was_not_execution_authority"] is True, "authority assertion missing")
    assert_true(report["safety_assertions"]["real_execution_permitted"] is False, "real execution assertion mismatch")
    assert_true("command_plan_is_dry_run_only" in report["readiness_blockers"], "dry-run blocker missing")
    assert_true(len(report["chain_nodes"]) == 7, "report should include chain nodes")
    assert_true(len(report["review_questions"]) >= 5, "report should include review questions")

    approved_chain, approved_bundle = build_demo_chain_and_bundle("approved")
    approved_report = build_evidence_reconstruction_report(approved_chain, approved_bundle)
    assert_true(
        approved_report["conclusion"] == "human_approval_recorded_but_real_execution_not_permitted",
        "approved conclusion mismatch",
    )
    assert_true(approved_report["real_execution_permitted"] is False, "approved report must still block real execution")

    bad_chain = copy.deepcopy(chain)
    bad_chain["real_execution_permitted"] = True
    expect_report_error(bad_chain, bundle, "report should reject real_execution_permitted=true")

    bad_chain = copy.deepcopy(chain)
    bad_chain["secret_exposed_to_ai"] = True
    expect_report_error(bad_chain, bundle, "report should reject secret_exposed_to_ai=true")

    bad_bundle = copy.deepcopy(bundle)
    bad_bundle["human_approval_gate_result"]["real_execution_permitted"] = True
    try:
        build_evidence_reconstruction_report(chain, bad_bundle)
    except Exception:
        pass
    else:
        raise AssertionError("report should reject approval gate real_execution_permitted=true")

    markdown = format_evidence_reconstruction_report_markdown(report)
    assert_true("# Evidence Reconstruction Report" in markdown, "markdown title missing")
    assert_true("Safety Assertions" in markdown, "markdown safety assertions missing")
    assert_true("Reconstruction Narrative" in markdown, "markdown narrative missing")
    assert_true("Real execution permitted" in markdown, "markdown execution status missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_evidence_reconstruction_report.py")], check=True)

    generated_json = ROOT / "private-not-in-git" / "reconstruction-reports" / "demo" / "evidence-reconstruction-report.generated.json"
    generated_md = ROOT / "private-not-in-git" / "reconstruction-reports" / "demo" / "evidence-reconstruction-report.generated.md"

    assert_true(generated_json.exists(), "generated reconstruction report JSON missing")
    assert_true(generated_md.exists(), "generated reconstruction report Markdown missing")

    print("Evidence reconstruction report tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
