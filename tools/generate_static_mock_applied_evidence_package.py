from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

DEFAULT_OUTPUT_DIR = Path("private-not-in-git/applied-evidence-runs/static-mock-demo")
GENERATOR_VERSION = "v0.6.29-static-mock-private-generation"

NON_AUTHORIZATION_STATEMENT = (
    "This static/mock generated artifact is review-only. It does not authorize "
    "execution, scanning, container activity, credential injection, customer-target "
    "operation, delivery, certification, legal approval, or audit opinion."
)

NON_PROOF_CLAIMS = [
    "vulnerability detection accuracy",
    "production readiness",
    "implementation conformance",
    "audit sufficiency",
    "legal sufficiency",
    "compliance certification",
    "external-framework equivalence",
    "customer-target authorization",
    "delivery authorization",
    "safety guarantee",
]

RUNTIME_BOUNDARY: dict[str, bool] = {
    "static_mock_generation_started": True,
    "static_mock_package_generated_private": True,
    "static_mock_generation_authorized_for_public": False,
    "public_sample_generated": False,
    "structural_validator_implemented": False,
    "structural_validator_checks_execute": False,
    "tool_backed_diagnostic_capture_started": False,
    "local_lab_diagnostic_system_built": False,
    "fixture_live_evidence": False,
    "validator_authorizes_execution": False,
    "validator_authorizes_scanning": False,
    "validator_authorizes_docker": False,
    "validator_authorizes_delivery": False,
    "docker_compose_file_created": False,
    "docker_compose_executed": False,
    "docker_image_pulled": False,
    "container_started": False,
    "port_bound": False,
    "docker_execution_authorized": False,
    "execution_authorized": False,
    "real_execution_permitted": False,
    "network_activity_allowed": False,
    "scan_execution_allowed": False,
    "credential_injection_permitted": False,
    "customer_target": False,
    "external_network_target": False,
    "delivery_authorized": False,
    "customer_deliverable": False,
}

SCENARIOS: list[dict[str, Any]] = [
    {
        "scenario_id": "permitted-safe-diagnostic",
        "requested_tool": "browser",
        "action_type": "safe_login_check",
        "target_scope": "local_lab_synthetic_target",
        "risk_level": "low",
        "decision_result": "permitted",
        "dispatch_attempted": True,
        "result_artifact": "execution_result.generated.json",
        "result_status": "static_mock_permitted_result",
        "event_type": "permitted_static_mock_execution_evidence",
        "summary": "Permitted safe local-lab diagnostic request with static/mock result.",
    },
    {
        "scenario_id": "denied-out-of-scope-request",
        "requested_tool": "nmap",
        "action_type": "network_probe",
        "target_scope": "out_of_scope_synthetic_target",
        "risk_level": "high",
        "decision_result": "denied",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.generated.json",
        "non_execution_reason": "out_of_scope_target_blocked",
        "event_type": "denied_non_execution_evidence",
        "summary": "Denied out-of-scope request with non-execution evidence.",
    },
    {
        "scenario_id": "human-approval-required",
        "requested_tool": "zap",
        "action_type": "active_scan_candidate",
        "target_scope": "local_lab_synthetic_target",
        "risk_level": "uncertain",
        "decision_result": "held_requires_human_approval",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.generated.json",
        "non_execution_reason": "human_approval_required",
        "event_type": "held_non_execution_evidence",
        "summary": "Held request requiring human approval before dispatch.",
    },
    {
        "scenario_id": "not-executed-expired",
        "requested_tool": "nuclei",
        "action_type": "template_check_candidate",
        "target_scope": "local_lab_synthetic_target",
        "risk_level": "medium",
        "decision_result": "expired",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.generated.json",
        "non_execution_reason": "request_expired_before_dispatch",
        "event_type": "expired_non_execution_evidence",
        "summary": "Expired request with no dispatch and non-execution evidence.",
    },
]


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def write_md(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8", newline="\n")


def ids_for(scenario_id: str) -> dict[str, str]:
    return {
        "request_id": f"req-{scenario_id}",
        "decision_id": f"dec-{scenario_id}",
        "dispatch_decision_id": f"disp-{scenario_id}",
        "result_id": f"res-{scenario_id}",
        "evidence_event_id": f"ev-{scenario_id}",
    }


def non_proof_markdown(scope: str) -> str:
    claims = "\n".join(f"- {claim}" for claim in NON_PROOF_CLAIMS)
    return f"""
# Non-proof statement: {scope}

This static/mock generated artifact does not prove:

{claims}

It does not authorize execution, scanning, customer-target operation, report delivery,
certification, legal approval, or audit opinion.
"""


def review_summary_markdown(scenario: dict[str, Any], ids: dict[str, str]) -> str:
    scenario_id = scenario["scenario_id"]
    execution_phrase = (
        "a static/mock execution result artifact was generated without real tool execution"
        if scenario["result_artifact"].startswith("execution_result")
        else "a non-execution result artifact was generated"
    )
    return f"""
# Review summary: {scenario_id}

## What AI requested

The AI-generated request `{ids["request_id"]}` requested `{scenario["action_type"]}`
using `{scenario["requested_tool"]}` for `{scenario["target_scope"]}`.

The request is not authority.

## Gate decision

Gate decision `{ids["decision_id"]}` recorded `{scenario["decision_result"]}`.

## Dispatch decision

Dispatch decision `{ids["dispatch_decision_id"]}` recorded
`dispatch_attempted = {str(scenario["dispatch_attempted"]).lower()}`.

## Result posture

Result `{ids["result_id"]}` records that {execution_phrase}.

## Evidence

Evidence event `{ids["evidence_event_id"]}` links request, decision, dispatch, and result.

## AAEF five questions

| Question | Answer |
| --- | --- |
| Who or what acted? | AI generated a request; Tool Gateway recorded dispatch posture |
| On whose behalf? | Synthetic local-lab principal / test operator |
| With what authority? | Gate decision `{ids["decision_id"]}` and static/mock policy version |
| Was the action allowed at the point of execution? | See dispatch decision and result posture |
| What evidence proves what happened? | Evidence event `{ids["evidence_event_id"]}` and this review summary |

## Non-proof

This scenario does not prove vulnerability detection accuracy, production readiness,
implementation conformance, audit sufficiency, legal sufficiency, compliance
certification, external-framework equivalence, customer-target authorization, delivery
authorization, or safety guarantee.
"""


def generate_scenario(root: Path, scenario: dict[str, Any]) -> dict[str, Any]:
    scenario_id = scenario["scenario_id"]
    scenario_dir = root / "scenarios" / scenario_id
    scenario_dir.mkdir(parents=True, exist_ok=True)
    ids = ids_for(scenario_id)

    request = {
        "request_id": ids["request_id"],
        "scenario_id": scenario_id,
        "requested_tool": scenario["requested_tool"],
        "action_type": scenario["action_type"],
        "target_scope": scenario["target_scope"],
        "requested_parameters": {"mode": "static_mock", "live_execution": False},
        "purpose": scenario["summary"],
        "rationale": "Demonstrate AAEF request-to-evidence traceability.",
        "risk_level": scenario["risk_level"],
        "principal_context": {"principal_id": "synthetic-local-lab-principal"},
        "actor_context": {"actor_type": "ai_generated_request", "model_output_is_authority": False},
        "credential_ref": None,
        "generated_by_ai": True,
        "timestamp": "2026-05-06T00:00:00Z",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "runtime_boundary": RUNTIME_BOUNDARY,
    }
    write_json(scenario_dir / "tool_action_request.generated.json", request)

    decision = {
        "decision_id": ids["decision_id"],
        "scenario_id": scenario_id,
        "linked_request_id": ids["request_id"],
        "decision_result": scenario["decision_result"],
        "reason": scenario["summary"],
        "policy_version": "static-mock-policy-v0.6.29",
        "rule_version": "static-mock-rule-v0.6.29",
        "trusted_inputs_used": ["scenario_id", "target_scope", "risk_level", "requested_tool"],
        "untrusted_inputs_excluded": ["model_claim_of_authority"],
        "deciding_component": "static_mock_gate",
        "timestamp": "2026-05-06T00:00:01Z",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }
    write_json(scenario_dir / "gate_decision.generated.json", decision)

    dispatch = {
        "dispatch_decision_id": ids["dispatch_decision_id"],
        "scenario_id": scenario_id,
        "linked_decision_id": ids["decision_id"],
        "dispatch_attempted": scenario["dispatch_attempted"],
        "dispatched_tool": scenario["requested_tool"] if scenario["dispatch_attempted"] else None,
        "blocked_reason": None if scenario["dispatch_attempted"] else scenario.get("non_execution_reason", "not_dispatched"),
        "execution_boundary": "static_mock_private_only",
        "gateway_component": "static_mock_tool_gateway",
        "timestamp": "2026-05-06T00:00:02Z",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "runtime_boundary": RUNTIME_BOUNDARY,
    }
    write_json(scenario_dir / "dispatch_decision.generated.json", dispatch)

    if scenario["result_artifact"].startswith("execution_result"):
        result = {
            "result_id": ids["result_id"],
            "scenario_id": scenario_id,
            "linked_dispatch_decision_id": ids["dispatch_decision_id"],
            "execution_occurred": False,
            "static_mock_execution_result": True,
            "real_execution_occurred": False,
            "result_status": scenario["result_status"],
            "result_summary": "Static/mock permitted result artifact; no scanner or live execution occurred.",
            "sanitized_output_ref": None,
            "runtime_boundary": RUNTIME_BOUNDARY,
            "timestamp": "2026-05-06T00:00:03Z",
            "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        }
    else:
        result = {
            "result_id": ids["result_id"],
            "scenario_id": scenario_id,
            "linked_dispatch_decision_id": ids["dispatch_decision_id"],
            "execution_occurred": False,
            "real_execution_occurred": False,
            "non_execution_reason": scenario["non_execution_reason"],
            "blocked_component": "static_mock_gate_or_gateway",
            "review_required": scenario["scenario_id"] == "human-approval-required",
            "timestamp": "2026-05-06T00:00:03Z",
            "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
            "runtime_boundary": RUNTIME_BOUNDARY,
        }
    write_json(scenario_dir / scenario["result_artifact"], result)

    evidence = {
        "evidence_event_id": ids["evidence_event_id"],
        "scenario_id": scenario_id,
        "linked_request_id": ids["request_id"],
        "linked_decision_id": ids["decision_id"],
        "linked_dispatch_decision_id": ids["dispatch_decision_id"],
        "linked_result_id": ids["result_id"],
        "event_type": scenario["event_type"],
        "event_summary": scenario["summary"],
        "evidence_created_at": "2026-05-06T00:00:04Z",
        "integrity_notes": "Static/mock generated package; no live execution or scanner output.",
        "non_proof_statement_ref": "non_proof_statement.generated.md",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }
    write_json(scenario_dir / "evidence_event.generated.json", evidence)

    write_md(scenario_dir / "review_summary.generated.md", review_summary_markdown(scenario, ids))
    write_md(scenario_dir / "non_proof_statement.generated.md", non_proof_markdown(scenario_id))

    return {
        "scenario_id": scenario_id,
        "scenario_dir": str(scenario_dir),
        "result_artifact": scenario["result_artifact"],
        "ids": ids,
    }


def reviewer_walkthrough(scenarios: list[dict[str, Any]]) -> str:
    rows = "\n".join(
        f"| `{s['scenario_id']}` | `{s['decision_result']}` | `{str(s['dispatch_attempted']).lower()}` | `{s['result_artifact']}` |"
        for s in scenarios
    )
    return f"""
# Static/mock applied evidence reviewer walkthrough

This private generated package demonstrates AAEF request-to-evidence traceability in
a static/mock form. It does not run scanners or authorize execution.

| Scenario | Gate result | Dispatch attempted | Result artifact |
| --- | --- | --- | --- |
{rows}

Reviewer focus:

1. Confirm the request is not authority.
2. Confirm gate decision is separate from dispatch decision.
3. Confirm non-dispatch is evidenced for denied, held, and expired scenarios.
4. Confirm evidence event links request, decision, dispatch, and result.
5. Confirm non-proof statements remain visible.
"""


def five_questions_mapping() -> str:
    return """
# AAEF five questions mapping

| AAEF question | Generated evidence source |
| --- | --- |
| Who or what acted? | `tool_action_request.generated.json`, gateway identity, `dispatch_decision.generated.json` |
| On whose behalf? | principal context and operator context in `tool_action_request.generated.json` |
| With what authority? | `gate_decision.generated.json`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision.generated.json`, execution boundary, result artifact |
| What evidence proves what happened? | `evidence_event.generated.json`, result artifact, `review_summary.generated.md` |

This mapping is reviewer guidance, not certification, audit opinion, legal approval,
or implementation conformance.
"""


def generate_package(output_dir: Path) -> dict[str, Any]:
    root = Path(output_dir)
    root.mkdir(parents=True, exist_ok=True)

    generated = [generate_scenario(root, scenario) for scenario in SCENARIOS]

    manifest = {
        "package_id": "static-mock-demo-v0629",
        "package_version": "v0.6.29",
        "generator_version": GENERATOR_VERSION,
        "package_status": "private_static_mock_generated",
        "scope_boundary": "private-not-in-git only; no live execution; no customer target",
        "scenario_ids": [scenario["scenario_id"] for scenario in SCENARIOS],
        "artifact_types": [
            "tool_action_request",
            "gate_decision",
            "dispatch_decision",
            "execution_result_or_non_execution_result",
            "evidence_event",
            "review_summary",
            "non_proof_statement",
        ],
        "evidence_chain_order": [
            "tool_action_request",
            "gate_decision",
            "dispatch_decision",
            "execution_result_or_non_execution_result",
            "evidence_event",
            "review_summary",
        ],
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "non_proof_statement_ref": "non_proof_statement.generated.md",
        "public_private_boundary": "private generated artifact; not public sample; not customer deliverable",
    }
    write_json(root / "package_manifest.generated.json", manifest)

    summary = {
        "package_id": manifest["package_id"],
        "scenario_count": len(generated),
        "scenarios": generated,
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }
    write_json(root / "package_summary.generated.json", summary)

    write_md(root / "reviewer_walkthrough.generated.md", reviewer_walkthrough(SCENARIOS))
    write_md(root / "aaef_five_questions_mapping.generated.md", five_questions_mapping())
    write_md(root / "non_proof_statement.generated.md", non_proof_markdown("package"))

    return summary


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a private static/mock AAEF applied evidence package."
    )
    parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_OUTPUT_DIR),
        help="Private output directory. Default: private-not-in-git/applied-evidence-runs/static-mock-demo",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    output_dir = Path(args.output_dir)
    summary = generate_package(output_dir)
    print(json.dumps({
        "status": "generated_private_static_mock_package",
        "output_dir": str(output_dir),
        "scenario_count": summary["scenario_count"],
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
