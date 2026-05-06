from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any

DEFAULT_OUTPUT_DIR = Path("examples/applied-evidence/sanitized-static-mock")
GENERATOR_VERSION = "v0.6.35-sanitized-public-sample"

NON_AUTHORIZATION_STATEMENT = (
    "This public example is synthetic and non-executing. It does not authorize "
    "runtime execution, scanner execution, credential injection, customer-target "
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
    "sanitized_public_sample_candidate_generated": True,
    "public_sample_publication_review_completed": False,
    "private_artifact_copied_to_public": False,
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
    "runtime_execution_authorized": False,
    "scanner_execution_authorized": False,
    "real_execution_permitted": False,
    "network_activity_allowed": False,
    "scan_execution_allowed": False,
    "credential_injection_permitted": False,
    "customer_target": False,
    "customer_target_authorized": False,
    "external_network_target": False,
    "delivery_authorized": False,
    "customer_deliverable": False,
}

SCENARIOS: list[dict[str, Any]] = [
    {
        "scenario_id": "permitted-safe-diagnostic",
        "requested_tool": "safe-diagnostic-tool",
        "action_type": "synthetic_safe_check",
        "target_scope": "synthetic-local-example-target",
        "risk_level": "low",
        "decision_result": "permitted",
        "dispatch_attempted": True,
        "result_artifact": "execution_result.example.json",
        "result_status": "synthetic_static_mock_permitted_result",
        "event_type": "permitted_static_mock_example_evidence",
        "summary": "Synthetic permitted trace with no real execution.",
    },
    {
        "scenario_id": "denied-out-of-scope-request",
        "requested_tool": "safe-diagnostic-tool",
        "action_type": "synthetic_out_of_scope_check",
        "target_scope": "synthetic-out-of-scope-example-target",
        "risk_level": "high",
        "decision_result": "denied",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.example.json",
        "non_execution_reason": "synthetic_out_of_scope_target_blocked",
        "event_type": "denied_non_execution_example_evidence",
        "summary": "Synthetic denied trace with non-execution evidence.",
    },
    {
        "scenario_id": "human-approval-required",
        "requested_tool": "safe-diagnostic-tool",
        "action_type": "synthetic_approval_required_check",
        "target_scope": "synthetic-local-example-target",
        "risk_level": "uncertain",
        "decision_result": "held_requires_human_approval",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.example.json",
        "non_execution_reason": "synthetic_human_approval_required",
        "event_type": "held_non_execution_example_evidence",
        "summary": "Synthetic held trace requiring human approval.",
    },
    {
        "scenario_id": "not-executed-expired",
        "requested_tool": "safe-diagnostic-tool",
        "action_type": "synthetic_expired_check",
        "target_scope": "synthetic-local-example-target",
        "risk_level": "medium",
        "decision_result": "expired",
        "dispatch_attempted": False,
        "result_artifact": "non_execution_result.example.json",
        "non_execution_reason": "synthetic_request_expired_before_dispatch",
        "event_type": "expired_non_execution_example_evidence",
        "summary": "Synthetic expired trace with no dispatch.",
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
        "request_id": f"example-request-{scenario_id}",
        "decision_id": f"example-decision-{scenario_id}",
        "dispatch_decision_id": f"example-dispatch-{scenario_id}",
        "result_id": f"example-result-{scenario_id}",
        "evidence_event_id": f"example-evidence-{scenario_id}",
    }


def non_proof_markdown(scope: str) -> str:
    claims = "\n".join(f"- {claim}" for claim in NON_PROOF_CLAIMS)
    return f"""
# Non-proof statement: {scope}

This public example is synthetic and non-executing. It does not prove:

{claims}

It does not authorize runtime execution, scanner execution, customer-target operation,
report delivery, certification, legal approval, or audit opinion.
"""


def review_summary_markdown(scenario: dict[str, Any], ids: dict[str, str]) -> str:
    scenario_id = scenario["scenario_id"]
    result_phrase = (
        "a synthetic static/mock permitted result artifact"
        if scenario["result_artifact"].startswith("execution_result")
        else "a synthetic non-execution result artifact"
    )
    return f"""
# Review summary: {scenario_id}

## What AI requested

The example request `{ids["request_id"]}` requested `{scenario["action_type"]}` using
`{scenario["requested_tool"]}` for `{scenario["target_scope"]}`.

The request is not authority.

## Gate decision

Gate decision `{ids["decision_id"]}` recorded `{scenario["decision_result"]}`.

## Dispatch decision

Dispatch decision `{ids["dispatch_decision_id"]}` recorded
`dispatch_attempted = {str(scenario["dispatch_attempted"]).lower()}`.

## Result posture

Result `{ids["result_id"]}` records {result_phrase}. No real execution occurred.

## Evidence

Evidence event `{ids["evidence_event_id"]}` links request, decision, dispatch, and result.

## AAEF five questions

| Question | Answer |
| --- | --- |
| Who or what acted? | AI generated a request; a gateway example recorded dispatch posture |
| On whose behalf? | Synthetic example principal |
| With what authority? | Gate decision `{ids["decision_id"]}` and example policy |
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
    ids = ids_for(scenario_id)

    request = {
        "request_id": ids["request_id"],
        "scenario_id": scenario_id,
        "requested_tool": scenario["requested_tool"],
        "action_type": scenario["action_type"],
        "target_scope": scenario["target_scope"],
        "requested_parameters": {"mode": "synthetic_public_example", "live_execution": False},
        "purpose": scenario["summary"],
        "risk_level": scenario["risk_level"],
        "principal_context": {"principal_id": "synthetic-example-principal"},
        "actor_context": {"actor_type": "ai_generated_request", "model_output_is_authority": False},
        "credential_ref": None,
        "generated_by_ai": True,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "runtime_boundary": RUNTIME_BOUNDARY,
    }
    write_json(scenario_dir / "tool_action_request.example.json", request)

    decision = {
        "decision_id": ids["decision_id"],
        "scenario_id": scenario_id,
        "linked_request_id": ids["request_id"],
        "decision_result": scenario["decision_result"],
        "reason": scenario["summary"],
        "policy_version": "synthetic-public-example-policy-v0.6.35",
        "rule_version": "synthetic-public-example-rule-v0.6.35",
        "trusted_inputs_used": ["scenario_id", "target_scope", "risk_level", "requested_tool"],
        "untrusted_inputs_excluded": ["model_claim_of_authority"],
        "deciding_component": "example_gate",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }
    write_json(scenario_dir / "gate_decision.example.json", decision)

    dispatch = {
        "dispatch_decision_id": ids["dispatch_decision_id"],
        "scenario_id": scenario_id,
        "linked_decision_id": ids["decision_id"],
        "dispatch_attempted": scenario["dispatch_attempted"],
        "dispatched_tool": scenario["requested_tool"] if scenario["dispatch_attempted"] else None,
        "blocked_reason": None if scenario["dispatch_attempted"] else scenario.get("non_execution_reason", "not_dispatched"),
        "execution_boundary": "synthetic_public_example_only",
        "gateway_component": "example_gateway",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "runtime_boundary": RUNTIME_BOUNDARY,
    }
    write_json(scenario_dir / "dispatch_decision.example.json", dispatch)

    if scenario["result_artifact"].startswith("execution_result"):
        result = {
            "result_id": ids["result_id"],
            "scenario_id": scenario_id,
            "linked_dispatch_decision_id": ids["dispatch_decision_id"],
            "execution_occurred": False,
            "synthetic_execution_result": True,
            "real_execution_occurred": False,
            "result_status": scenario["result_status"],
            "result_summary": "Synthetic public example result; no scanner or live execution occurred.",
            "runtime_boundary": RUNTIME_BOUNDARY,
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
            "blocked_component": "example_gate_or_gateway",
            "review_required": scenario_id == "human-approval-required",
            "runtime_boundary": RUNTIME_BOUNDARY,
            "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
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
        "integrity_notes": "Synthetic public example; no live execution or scanner output.",
        "non_proof_statement_ref": "non_proof_statement.example.md",
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
    }
    write_json(scenario_dir / "evidence_event.example.json", evidence)

    write_md(scenario_dir / "review_summary.example.md", review_summary_markdown(scenario, ids))
    write_md(scenario_dir / "non_proof_statement.example.md", non_proof_markdown(scenario_id))

    return {"scenario_id": scenario_id, "result_artifact": scenario["result_artifact"], "ids": ids}


def readme_md() -> str:
    return """
# Sanitized static/mock applied evidence example

This directory contains synthetic, non-executing AAEF-AI-VA applied evidence examples.

The examples demonstrate request-to-evidence traceability. They do not demonstrate
vulnerability detection accuracy, production readiness, implementation conformance,
audit sufficiency, legal sufficiency, compliance certification, external-framework
equivalence, customer-target authorization, or delivery authorization.
"""


def reviewer_walkthrough() -> str:
    rows = "\n".join(
        f"| `{s['scenario_id']}` | `{s['decision_result']}` | `{str(s['dispatch_attempted']).lower()}` | `{s['result_artifact']}` |"
        for s in SCENARIOS
    )
    return f"""
# Reviewer walkthrough

This sanitized public sample is synthetic and non-executing.

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

| AAEF question | Public example evidence source |
| --- | --- |
| Who or what acted? | `tool_action_request.example.json`, gateway identity, `dispatch_decision.example.json` |
| On whose behalf? | synthetic principal context in `tool_action_request.example.json` |
| With what authority? | `gate_decision.example.json`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision.example.json`, execution boundary, result artifact |
| What evidence proves what happened? | `evidence_event.example.json`, result artifact, `review_summary.example.md` |

This mapping is reviewer guidance, not certification, audit opinion, legal approval, or
implementation conformance.
"""


def hygiene_report(root: Path) -> dict[str, Any]:
    forbidden_fragments = [
        "private-not-in-git",
        ".generated.",
        "BEGIN RSA PRIVATE KEY",
        "password",
        "token",
        "cookie",
        "customer.example.com",
        "127.0.0.1",
        "192.168.",
        "10.0.",
        "container command invocation",
    ]
    findings: list[dict[str, str]] = []
    for path in root.rglob("*"):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for fragment in forbidden_fragments:
                if fragment.lower() in text.lower():
                    findings.append({"path": str(path.relative_to(root)), "fragment": fragment})
    checked_categories = [
        "private path leakage",
        "generated artifact naming leakage",
        "secret material",
        "credential material",
        "session material",
        "raw protocol messages",
        "raw scanner output",
        "customer-like hostnames",
        "loopback runtime targets",
        "private-network-like targets",
        "container command invocation",
    ]
    return {
        "hygiene_status": "passed" if not findings else "blocked",
        "findings": findings,
        "checked_categories": checked_categories,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "runtime_boundary": RUNTIME_BOUNDARY,
    }


def generate_sample(output_dir: Path) -> dict[str, Any]:
    root = Path(output_dir)
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True, exist_ok=True)

    generated = [generate_scenario(root, scenario) for scenario in SCENARIOS]

    manifest = {
        "package_id": "sanitized-static-mock-example-v0635",
        "package_version": "v0.6.35",
        "generator_version": GENERATOR_VERSION,
        "package_status": "sanitized_public_sample_candidate",
        "sample_type": "synthetic_non_executing_public_example",
        "scenario_ids": [scenario["scenario_id"] for scenario in SCENARIOS],
        "artifact_naming": ".example.",
        "runtime_boundary": RUNTIME_BOUNDARY,
        "non_authorization_statement": NON_AUTHORIZATION_STATEMENT,
        "non_proof_statement_ref": "non_proof_statement.example.md",
    }
    write_json(root / "package_manifest.example.json", manifest)
    write_md(root / "README.md", readme_md())
    write_md(root / "reviewer_walkthrough.example.md", reviewer_walkthrough())
    write_md(root / "aaef_five_questions_mapping.example.md", five_questions_mapping())
    write_md(root / "non_proof_statement.example.md", non_proof_markdown("package"))

    report = hygiene_report(root)
    write_json(root / "publication_hygiene_report.example.json", report)
    write_md(
        root / "publication_hygiene_report.example.md",
        f"""
# Publication hygiene report

Hygiene status: `{report['hygiene_status']}`

Findings: `{len(report['findings'])}`

This report is a publication hygiene aid. It does not authorize runtime execution,
scanner execution, customer-target operation, delivery, certification, legal approval,
or audit opinion.
""",
    )

    return {"output_dir": str(root), "scenario_count": len(generated), "hygiene_status": report["hygiene_status"]}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate sanitized public applied evidence sample candidate.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Public sample output directory.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    summary = generate_sample(Path(args.output_dir))
    print(json.dumps({
        "status": "generated_sanitized_public_sample_candidate",
        "output_dir": summary["output_dir"],
        "scenario_count": summary["scenario_count"],
        "hygiene_status": summary["hygiene_status"],
        "runtime_boundary": RUNTIME_BOUNDARY,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
