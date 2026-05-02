from __future__ import annotations

from typing import Any

from models import make_evidence_id, make_execution_id, utc_now_iso
from policy import (
    decision_to_execution_status,
    should_resolve_credential,
    validate_credential_ref_against_vault_metadata,
    validate_request_decision_binding,
)


def run_mock_tool_gateway(
    request: dict[str, Any],
    decision: dict[str, Any],
    vault_metadata: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    \"\"\"Run the MVP Tool Gateway mock flow.

    This function does not execute real tools. It validates request/decision
    binding and emits mock execution/evidence objects.
    \"\"\"
    validate_request_decision_binding(request, decision)

    status = decision_to_execution_status(decision)
    credential_metadata = validate_credential_ref_against_vault_metadata(decision, vault_metadata)

    started_at = utc_now_iso()
    completed_at = started_at

    credential_ref = decision.get("credential_ref")
    credential_ref_used = credential_ref if status == "completed" else None
    credential_resolved_by = "mock-vault" if should_resolve_credential(decision) else None

    tool_execution_id = make_execution_id(request)

    if status == "completed":
        raw_artifact_ref = f"private-not-in-git/raw-artifacts/{decision['tool']}/{tool_execution_id}.json"
        sanitized_artifact_ref = f"private-not-in-git/prototype-runs/{tool_execution_id}/sanitized-result.json"
        sanitization_status = "completed"
        finding_candidate_ids = [f"finding-{tool_execution_id.removeprefix('exec-')}"]
        human_review_status = "pending"
        error_summary = None
    elif status == "blocked":
        raw_artifact_ref = None
        sanitized_artifact_ref = None
        sanitization_status = "not_required"
        finding_candidate_ids = []
        human_review_status = "not_required"
        error_summary = "Blocked by authorization decision before tool execution."
    else:
        raw_artifact_ref = None
        sanitized_artifact_ref = None
        sanitization_status = "not_required"
        finding_candidate_ids = []
        human_review_status = "pending"
        error_summary = "Execution paused because human approval is required."

    result = {
        "tool_execution_id": tool_execution_id,
        "tool_action_request_id": request["tool_action_request_id"],
        "authorization_decision_id": decision["authorization_decision_id"],
        "execution_status": status,
        "target_id": decision["target_id"],
        "scope_id": decision["scope_id"],
        "tool": decision["tool"],
        "operation": decision["operation"],
        "credential_ref_used": credential_ref_used,
        "credential_resolved_by": credential_resolved_by,
        "secret_exposed_to_ai": False,
        "raw_artifact_ref": raw_artifact_ref,
        "sanitized_artifact_ref": sanitized_artifact_ref,
        "started_at": started_at,
        "completed_at": completed_at,
        "error_summary": error_summary,
    }

    evidence = {
        "evidence_id": make_evidence_id(request),
        "tool_execution_id": tool_execution_id,
        "tool_action_request_id": request["tool_action_request_id"],
        "authorization_decision_id": decision["authorization_decision_id"],
        "target_id": decision["target_id"],
        "scope_id": decision["scope_id"],
        "tool": decision["tool"],
        "operation": decision["operation"],
        "credential_ref_used": credential_ref_used,
        "secret_exposed_to_ai": False,
        "raw_artifact_ref": raw_artifact_ref,
        "sanitized_artifact_ref": sanitized_artifact_ref,
        "sanitization_status": sanitization_status,
        "finding_candidate_ids": finding_candidate_ids,
        "human_review_status": human_review_status,
        "created_at": utc_now_iso(),
    }

    # Keep credential metadata out of schema-bound records, but access it here
    # so static checkers do not treat validation as unused.
    _ = credential_metadata

    return result, evidence
