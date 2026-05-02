from __future__ import annotations

from typing import Any


class EvidenceChainError(ValueError):
    pass


REQUIRED_OBJECTS = [
    "tool_action_request",
    "authorization_decision",
    "tool_execution_result",
    "evidence_record",
    "operator_readiness_review",
    "human_approval_record",
    "human_approval_gate_result",
]


CONSISTENCY_FIELDS = ["target_id", "scope_id", "tool", "operation"]


def _require_object(bundle: dict[str, Any], key: str) -> dict[str, Any]:
    value = bundle.get(key)
    if not isinstance(value, dict):
        raise EvidenceChainError(f"missing or invalid chain object: {key}")
    return value


def _check_equal(label: str, left: Any, right: Any) -> None:
    if left != right:
        raise EvidenceChainError(f"chain mismatch for {label}: {left!r} != {right!r}")


def validate_evidence_chain_bundle(bundle: dict[str, Any]) -> None:
    for key in REQUIRED_OBJECTS:
        _require_object(bundle, key)

    request = bundle["tool_action_request"]
    authz = bundle["authorization_decision"]
    result = bundle["tool_execution_result"]
    evidence = bundle["evidence_record"]
    operator_review = bundle["operator_readiness_review"]
    approval = bundle["human_approval_record"]
    approval_gate = bundle["human_approval_gate_result"]

    request_id = request["tool_action_request_id"]
    authz_id = authz["authorization_decision_id"]
    execution_id = result["tool_execution_id"]
    evidence_id = evidence["evidence_id"]
    approval_record_id = approval["approval_record_id"]

    _check_equal("request/authz tool_action_request_id", request_id, authz["tool_action_request_id"])
    _check_equal("request/result tool_action_request_id", request_id, result["tool_action_request_id"])
    _check_equal("request/evidence tool_action_request_id", request_id, evidence["tool_action_request_id"])

    _check_equal("authz/result authorization_decision_id", authz_id, result["authorization_decision_id"])
    _check_equal("authz/evidence authorization_decision_id", authz_id, evidence["authorization_decision_id"])

    _check_equal("result/evidence tool_execution_id", execution_id, evidence["tool_execution_id"])

    for field in CONSISTENCY_FIELDS:
        request_value = request.get(field)
        _check_equal(f"request/authz {field}", request_value, authz.get(field))
        _check_equal(f"request/result {field}", request_value, result.get(field))
        _check_equal(f"request/evidence {field}", request_value, evidence.get(field))
        _check_equal(f"operator/approval {field}", operator_review.get(field), approval.get(field))
        _check_equal(f"approval/gate {field}", approval.get(field), approval_gate.get(field))

    _check_equal(
        "operator/approval command_plan_id",
        operator_review.get("command_plan_id"),
        approval.get("command_plan_id"),
    )
    _check_equal(
        "approval/gate approval_record_id",
        approval_record_id,
        approval_gate.get("approval_record_id"),
    )
    _check_equal(
        "approval/gate command_plan_id",
        approval.get("command_plan_id"),
        approval_gate.get("command_plan_id"),
    )

    if result.get("secret_exposed_to_ai") is not False:
        raise EvidenceChainError("tool_execution_result must keep secret_exposed_to_ai=false")

    if evidence.get("secret_exposed_to_ai") is not False:
        raise EvidenceChainError("evidence_record must keep secret_exposed_to_ai=false")

    if approval.get("evidence_required") is not True:
        raise EvidenceChainError("human approval record must require evidence")

    if approval_gate.get("real_execution_permitted") is not False:
        raise EvidenceChainError("human approval gate must not permit real execution in current MVP")


def build_evidence_chain(bundle: dict[str, Any]) -> dict[str, Any]:
    validate_evidence_chain_bundle(bundle)

    request = bundle["tool_action_request"]
    authz = bundle["authorization_decision"]
    result = bundle["tool_execution_result"]
    evidence = bundle["evidence_record"]
    operator_review = bundle["operator_readiness_review"]
    approval = bundle["human_approval_record"]
    approval_gate = bundle["human_approval_gate_result"]

    chain_id = f"chain-{evidence['evidence_id']}-{approval['approval_record_id']}"

    if approval_gate["approval_decision"] == "approved":
        chain_status = "approval_recorded_execution_still_blocked"
    elif approval_gate["approval_decision"] == "keep_blocked":
        chain_status = "reviewed_and_blocked"
    elif approval_gate["approval_decision"] == "needs_more_info":
        chain_status = "reviewed_needs_more_information"
    else:
        chain_status = "reviewed_and_rejected"

    nodes = [
        {
            "node_type": "tool_action_request",
            "node_id": request["tool_action_request_id"],
            "status": "requested",
        },
        {
            "node_type": "authorization_decision",
            "node_id": authz["authorization_decision_id"],
            "status": authz["decision"],
        },
        {
            "node_type": "tool_execution_result",
            "node_id": result["tool_execution_id"],
            "status": result["execution_status"],
        },
        {
            "node_type": "evidence_record",
            "node_id": evidence["evidence_id"],
            "status": evidence["human_review_status"],
        },
        {
            "node_type": "operator_readiness_review",
            "node_id": operator_review["command_plan_id"],
            "status": operator_review["review_status"],
        },
        {
            "node_type": "human_approval_record",
            "node_id": approval["approval_record_id"],
            "status": approval["approval_decision"],
        },
        {
            "node_type": "human_approval_gate_result",
            "node_id": approval_gate["approval_record_id"],
            "status": approval_gate["gate_status"],
        },
    ]

    links = [
        ["tool_action_request", "authorization_decision"],
        ["authorization_decision", "tool_execution_result"],
        ["tool_execution_result", "evidence_record"],
        ["evidence_record", "operator_readiness_review"],
        ["operator_readiness_review", "human_approval_record"],
        ["human_approval_record", "human_approval_gate_result"],
    ]

    return {
        "chain_id": chain_id,
        "chain_type": "ai_vulnerability_assessment_execution_review_chain",
        "chain_status": chain_status,
        "target_id": request["target_id"],
        "scope_id": request["scope_id"],
        "tool": request["tool"],
        "operation": request["operation"],
        "tool_action_request_id": request["tool_action_request_id"],
        "authorization_decision_id": authz["authorization_decision_id"],
        "tool_execution_id": result["tool_execution_id"],
        "evidence_id": evidence["evidence_id"],
        "command_plan_id": operator_review["command_plan_id"],
        "approval_record_id": approval["approval_record_id"],
        "approval_decision": approval["approval_decision"],
        "real_execution_permitted": False,
        "secret_exposed_to_ai": False,
        "nodes": nodes,
        "links": links,
        "reconstruction_supported": True,
        "notes": (
            "Current MVP evidence chain supports reconstruction of request, authorization, "
            "execution result, evidence, operator review, human approval, and approval gate. "
            "It does not permit real execution."
        ),
    }


def format_evidence_chain_markdown(chain: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Evidence Chain Review")
    lines.append("")
    lines.append(f"- Chain ID: `{chain['chain_id']}`")
    lines.append(f"- Chain status: `{chain['chain_status']}`")
    lines.append(f"- Target ID: `{chain['target_id']}`")
    lines.append(f"- Scope ID: `{chain['scope_id']}`")
    lines.append(f"- Tool: `{chain['tool']}`")
    lines.append(f"- Operation: `{chain['operation']}`")
    lines.append(f"- Real execution permitted: `{chain['real_execution_permitted']}`")
    lines.append(f"- Secret exposed to AI: `{chain['secret_exposed_to_ai']}`")
    lines.append(f"- Reconstruction supported: `{chain['reconstruction_supported']}`")
    lines.append("")
    lines.append("## Nodes")
    lines.append("")
    for node in chain["nodes"]:
        lines.append(f"- `{node['node_type']}` / `{node['node_id']}` / `{node['status']}`")
    lines.append("")
    lines.append("## Links")
    lines.append("")
    for source, target in chain["links"]:
        lines.append(f"- `{source}` -> `{target}`")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(chain["notes"])
    lines.append("")
    return "\n".join(lines)
