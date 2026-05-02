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
from evidence_chain import EvidenceChainError, build_evidence_chain, format_evidence_chain_markdown
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


def expect_chain_error(bundle: dict, message: str) -> None:
    try:
        build_evidence_chain(bundle)
    except EvidenceChainError:
        return
    raise AssertionError(message)


def build_demo_bundle(approval_decision: str = "keep_blocked") -> dict:
    request = load_json(EXAMPLE_DIR / "allowed-action.tool-action-request.json")
    authz = load_json(EXAMPLE_DIR / "allowed-action.authorization-decision.json")
    result, evidence = run_mock_tool_gateway(request, authz, vault_metadata=load_default_vault_metadata())

    adapter = get_adapter("zap")
    command_plan = adapter.build_command_plan(request, authz, "mock-vault")
    readiness_result = evaluate_real_execution_readiness(command_plan)
    operator_review = summarize_readiness_for_operator(readiness_result)
    approval_record = build_human_approval_record(operator_review, approval_decision=approval_decision)
    approval_gate_result = evaluate_human_approval_gate(operator_review, approval_record)

    return {
        "tool_action_request": request,
        "authorization_decision": authz,
        "tool_execution_result": result,
        "evidence_record": evidence,
        "operator_readiness_review": operator_review,
        "human_approval_record": approval_record,
        "human_approval_gate_result": approval_gate_result,
    }


def main() -> int:
    bundle = build_demo_bundle()
    chain = build_evidence_chain(bundle)

    assert_true(chain["chain_type"] == "ai_vulnerability_assessment_execution_review_chain", "chain type mismatch")
    assert_true(chain["chain_status"] == "reviewed_and_blocked", "default chain should be reviewed_and_blocked")
    assert_true(chain["real_execution_permitted"] is False, "chain must not permit real execution")
    assert_true(chain["secret_exposed_to_ai"] is False, "chain must not expose secret to AI")
    assert_true(chain["reconstruction_supported"] is True, "chain should support reconstruction")
    assert_true(len(chain["nodes"]) == 7, "chain should contain seven nodes")
    assert_true(len(chain["links"]) == 6, "chain should contain six links")

    approved_bundle = build_demo_bundle("approved")
    approved_chain = build_evidence_chain(approved_bundle)
    assert_true(
        approved_chain["chain_status"] == "approval_recorded_execution_still_blocked",
        "approved MVP chain status mismatch",
    )
    assert_true(approved_chain["real_execution_permitted"] is False, "approved chain must still not permit real execution")

    bad = copy.deepcopy(bundle)
    bad["evidence_record"]["tool_execution_id"] = "other-exec"
    expect_chain_error(bad, "execution/evidence mismatch should fail closed")

    bad = copy.deepcopy(bundle)
    bad["human_approval_record"]["target_id"] = "other-target"
    expect_chain_error(bad, "approval target mismatch should fail closed")

    bad = copy.deepcopy(bundle)
    bad["human_approval_gate_result"]["real_execution_permitted"] = True
    expect_chain_error(bad, "real execution permitted in gate result should fail closed")

    bad = copy.deepcopy(bundle)
    bad["tool_execution_result"]["secret_exposed_to_ai"] = True
    expect_chain_error(bad, "secret exposure in result should fail closed")

    markdown = format_evidence_chain_markdown(chain)
    assert_true("# Evidence Chain Review" in markdown, "evidence chain markdown title missing")
    assert_true("tool_action_request" in markdown, "evidence chain markdown node missing")
    assert_true("human_approval_gate_result" in markdown, "evidence chain markdown approval gate missing")

    subprocess.run([sys.executable, str(ROOT / "tools" / "generate_evidence_chain_review.py")], check=True)

    generated_json = ROOT / "private-not-in-git" / "evidence-chains" / "demo" / "evidence-chain.generated.json"
    generated_md = ROOT / "private-not-in-git" / "evidence-chains" / "demo" / "evidence-chain.generated.md"

    assert_true(generated_json.exists(), "generated evidence chain JSON missing")
    assert_true(generated_md.exists(), "generated evidence chain Markdown missing")

    print("Evidence chain linkage tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
