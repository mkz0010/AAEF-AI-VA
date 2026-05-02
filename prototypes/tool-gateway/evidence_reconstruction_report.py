from __future__ import annotations

from typing import Any

from evidence_chain import validate_evidence_chain_bundle


class EvidenceReconstructionReportError(ValueError):
    pass


def build_evidence_reconstruction_report(
    chain: dict[str, Any],
    bundle: dict[str, Any],
) -> dict[str, Any]:
    validate_evidence_chain_bundle(bundle)

    operator_review = bundle["operator_readiness_review"]
    approval_record = bundle["human_approval_record"]
    approval_gate = bundle["human_approval_gate_result"]
    result = bundle["tool_execution_result"]
    evidence = bundle["evidence_record"]

    if chain.get("reconstruction_supported") is not True:
        raise EvidenceReconstructionReportError("evidence chain does not support reconstruction")

    if chain.get("real_execution_permitted") is not False:
        raise EvidenceReconstructionReportError("current MVP reconstruction requires real_execution_permitted=false")

    if chain.get("secret_exposed_to_ai") is not False:
        raise EvidenceReconstructionReportError("current MVP reconstruction requires secret_exposed_to_ai=false")

    blockers = list(operator_review.get("blockers", []))
    next_actions = list(operator_review.get("next_actions", []))

    if approval_gate.get("real_execution_permitted") is not False:
        raise EvidenceReconstructionReportError("approval gate must not permit real execution in current MVP")

    conclusion = "real_execution_not_permitted"
    if approval_record.get("approval_decision") == "approved":
        conclusion = "human_approval_recorded_but_real_execution_not_permitted"
    elif approval_record.get("approval_decision") == "rejected":
        conclusion = "human_rejection_recorded"
    elif approval_record.get("approval_decision") == "needs_more_info":
        conclusion = "more_information_required"
    elif approval_record.get("approval_decision") == "keep_blocked":
        conclusion = "kept_blocked_after_review"

    safety_assertions = {
        "model_output_was_not_execution_authority": True,
        "real_execution_permitted": False,
        "external_process_executed": False,
        "network_activity_performed": False,
        "secret_exposed_to_ai": False,
        "evidence_required": approval_record.get("evidence_required") is True,
        "adapter_output_embedded_in_public_result": False,
        "reconstruction_supported": True,
    }

    key_findings = [
        "The action was processed through the Tool Gateway control path.",
        "The request, authorization decision, execution result, and evidence record are linked.",
        "The operator readiness review was linked to the human approval record.",
        "The human approval gate result is linked to the approval record.",
        "Real execution remains unavailable in the current MVP.",
        "Secrets were not exposed to AI according to generated result and evidence flags.",
    ]

    if blockers:
        key_findings.append("The readiness gate reported blockers that require remediation before future real execution can be considered.")

    report = {
        "report_id": f"recon-{chain['chain_id']}",
        "report_type": "evidence_reconstruction_report",
        "report_status": "complete",
        "conclusion": conclusion,
        "chain_id": chain["chain_id"],
        "chain_status": chain["chain_status"],
        "target_id": chain["target_id"],
        "scope_id": chain["scope_id"],
        "tool": chain["tool"],
        "operation": chain["operation"],
        "tool_action_request_id": chain["tool_action_request_id"],
        "authorization_decision_id": chain["authorization_decision_id"],
        "tool_execution_id": chain["tool_execution_id"],
        "evidence_id": chain["evidence_id"],
        "command_plan_id": chain["command_plan_id"],
        "approval_record_id": chain["approval_record_id"],
        "approval_decision": chain["approval_decision"],
        "approval_gate_status": approval_gate["gate_status"],
        "operator_review_status": operator_review["review_status"],
        "operator_decision_recommendation": operator_review["decision_recommendation"],
        "tool_execution_status": result["execution_status"],
        "evidence_human_review_status": evidence["human_review_status"],
        "real_execution_permitted": False,
        "secret_exposed_to_ai": False,
        "safety_assertions": safety_assertions,
        "readiness_blockers": blockers,
        "readiness_next_actions": next_actions,
        "reconstruction_narrative": {
            "request": "A tool action request was created for the approved target alias and scope.",
            "authorization": "The authorization decision was bound to the request fields and used by Tool Gateway.",
            "tool_gateway": "Tool Gateway produced a schema-bound tool execution result and evidence record.",
            "readiness": "The real execution readiness gate evaluated the command plan and returned blockers.",
            "operator_review": "The operator readiness review converted blockers into reviewable next actions.",
            "human_approval": "A human approval record captured the operator decision without enabling real execution.",
            "approval_gate": "The human approval gate validated binding and kept real execution disabled.",
            "final": "The chain supports reconstruction while preserving the current MVP no-real-execution boundary.",
        },
        "key_findings": key_findings,
        "chain_nodes": chain["nodes"],
        "chain_links": chain["links"],
        "review_questions": [
            "Was the request bound to a valid authorization decision?",
            "Was the target resolved through the scope registry?",
            "Was credential_ref used without exposing raw credentials to AI?",
            "Was adapter output kept out of public generated results?",
            "Did the readiness gate identify real execution blockers?",
            "Was a human decision recorded and bound to the reviewed command plan?",
            "Is real execution still blocked in the MVP?",
        ],
    }

    return report


def format_evidence_reconstruction_report_markdown(report: dict[str, Any]) -> str:
    lines: list[str] = []

    lines.append("# Evidence Reconstruction Report")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Report ID: `{report['report_id']}`")
    lines.append(f"- Conclusion: `{report['conclusion']}`")
    lines.append(f"- Chain status: `{report['chain_status']}`")
    lines.append(f"- Target ID: `{report['target_id']}`")
    lines.append(f"- Scope ID: `{report['scope_id']}`")
    lines.append(f"- Tool: `{report['tool']}`")
    lines.append(f"- Operation: `{report['operation']}`")
    lines.append(f"- Tool execution status: `{report['tool_execution_status']}`")
    lines.append(f"- Operator review status: `{report['operator_review_status']}`")
    lines.append(f"- Human approval decision: `{report['approval_decision']}`")
    lines.append(f"- Approval gate status: `{report['approval_gate_status']}`")
    lines.append(f"- Real execution permitted: `{report['real_execution_permitted']}`")
    lines.append(f"- Secret exposed to AI: `{report['secret_exposed_to_ai']}`")
    lines.append("")

    lines.append("## Key IDs")
    lines.append("")
    for key in [
        "tool_action_request_id",
        "authorization_decision_id",
        "tool_execution_id",
        "evidence_id",
        "command_plan_id",
        "approval_record_id",
        "chain_id",
    ]:
        lines.append(f"- {key}: `{report[key]}`")
    lines.append("")

    lines.append("## Safety Assertions")
    lines.append("")
    for key, value in report["safety_assertions"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")

    lines.append("## Readiness Blockers")
    lines.append("")
    if report["readiness_blockers"]:
        for blocker in report["readiness_blockers"]:
            lines.append(f"- `{blocker}`")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Next Actions")
    lines.append("")
    if report["readiness_next_actions"]:
        for item in report["readiness_next_actions"]:
            lines.append(f"- `{item['blocker']}` / `{item['category']}`: {item['next_action']}")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Reconstruction Narrative")
    lines.append("")
    for key, text in report["reconstruction_narrative"].items():
        lines.append(f"### {key}")
        lines.append("")
        lines.append(text)
        lines.append("")

    lines.append("## Chain Nodes")
    lines.append("")
    for node in report["chain_nodes"]:
        lines.append(f"- `{node['node_type']}` / `{node['node_id']}` / `{node['status']}`")
    lines.append("")

    lines.append("## Chain Links")
    lines.append("")
    for source, target in report["chain_links"]:
        lines.append(f"- `{source}` -> `{target}`")
    lines.append("")

    lines.append("## Review Questions")
    lines.append("")
    for question in report["review_questions"]:
        lines.append(f"- [ ] {question}")
    lines.append("")

    return "\n".join(lines)
