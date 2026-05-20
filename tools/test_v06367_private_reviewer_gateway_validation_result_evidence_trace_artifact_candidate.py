from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/442-v06367-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0442-add-v06367-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate.md"
ISSUE = ROOT / "planning/issues/0442-add-v06367-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
PRIVATE_DIR = ROOT / "private-not-in-git" / "gateway-validation-result-evidence-traces" / "v0.6.367" / "demo"
JSON_ARTIFACT = PRIVATE_DIR / "gateway-validation-result-evidence-trace.generated.json"
MD_ARTIFACT = PRIVATE_DIR / "gateway-validation-result-evidence-trace.generated.md"

REQUIRED = ['v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_created = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_status = candidate_implemented_pending_review', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_generated = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_path = private-not-in-git/gateway-validation-result-evidence-traces/v0.6.367/demo', 'private_reviewer_gateway_validation_result_evidence_trace_json_artifact_generated = true', 'private_reviewer_gateway_validation_result_evidence_trace_markdown_artifact_generated = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_private_only = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_publication_approved = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_schema_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_generated_outputs_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_runtime_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_public_artifact_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_preserves_generated_output_compatibility = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_raw_gate_result_preserved = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_reviewer_status_included = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_raw_and_reviewer_status_separated = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_external_process_executed_included = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_network_activity_performed_included = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_limitations_included = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_gate_results_include_authorization_expiry_current_time = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_gate_results_include_request_decision_constraint_diff = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_gate_results_include_external_discovery_fail_closed = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_gate_results_include_non_dispatch_legacy_path_preservation = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_gate_results_include_existing_policy_error_path_preservation = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_limitations_include_not_scanner_output = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_limitations_include_not_legal_proof = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_limitations_include_not_audit_opinion = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_limitations_include_not_execution_authorization = true', 'gateway_validation_result_evidence_trace_application_planning_candidate_accepted = true', 'gateway_validation_result_application_phase_1_private_reviewer_artifact = accepted_as_first_application_target', 'gateway_validation_result_application_phase_2_schema_field_decision = deferred', 'gateway_validation_result_application_phase_3_generated_output_application_decision = deferred', 'gateway_validation_result_application_phase_4_runtime_application_decision = deferred', 'gateway_validation_result_application_public_artifact_change_decision = deferred', 'gateway_validation_result_application_schema_change_now = false', 'gateway_validation_result_application_generated_output_change_now = false', 'gateway_validation_result_application_runtime_change_now = false', 'gateway_validation_result_application_public_artifact_change_now = false', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'v06367_gateway_core_behavior_changed = false', 'v06367_tool_gateway_behavior_changed = false', 'v06367_runtime_behavior_changed = false', 'v06367_scanner_behavior_changed = false', 'v06367_schema_changed = false', 'v06367_public_artifacts_changed = false', 'v06367_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_review_and_decision', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Private reviewer artifact candidate is not production readiness.', 'Private reviewer artifact candidate is not scanner readiness.', 'Private reviewer artifact candidate is not execution authorization.', 'Private reviewer artifact candidate is not real execution permission.', 'Private reviewer artifact candidate is not external target authorization.', 'Private reviewer artifact candidate is not customer demo approval.', 'Private reviewer artifact candidate is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.367.', 'v0.6.368 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def build_private_artifact() -> dict:
    return {
        "artifact_type": "private_reviewer_gateway_validation_result_evidence_trace",
        "artifact_version": "private-reviewer-gateway-validation-result-evidence-trace-v06367",
        "artifact_scope": "private_reviewer_only",
        "publication_approved": False,
        "source_checkpoint": "v0.6.367",
        "schema_changed": False,
        "generated_outputs_changed": False,
        "runtime_changed": False,
        "public_artifact_changed": False,
        "gateway_validation_result": {
            "model_version": "gateway-validation-result-candidate-v06363",
            "summary_status": "mock_dry_run_completed_no_real_execution",
            "raw_execution_status": "completed",
            "reviewer_execution_status": "mock_dry_run_completed_no_real_execution",
            "raw_and_reviewer_status_separated": True,
            "checked_before_dispatch": True,
            "external_process_executed": False,
            "network_activity_performed": False,
            "gate_results": [
                {"gate_id": "authorization_expiry_current_time", "gate_status": "passed", "allowed_to_continue": True},
                {"gate_id": "request_decision_constraint_diff", "gate_status": "passed", "allowed_to_continue": True},
                {"gate_id": "external_discovery_fail_closed", "gate_status": "passed", "allowed_to_continue": True},
                {"gate_id": "non_dispatch_legacy_path_preservation", "gate_status": "not_applicable_legacy_path_preserved", "allowed_to_continue": True},
                {"gate_id": "existing_policy_error_path_preservation", "gate_status": "policy_error_path_preserved", "allowed_to_continue": True},
            ],
            "limitations": [
                "private reviewer artifact candidate only",
                "not scanner output",
                "not legal proof",
                "not audit opinion",
                "not execution authorization",
                "not external target authorization",
                "not production readiness",
            ],
        },
    }

def write_private_artifacts() -> None:
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    artifact = build_private_artifact()
    JSON_ARTIFACT.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# Private Reviewer Gateway Validation Result Evidence Trace",
        "",
        "- checkpoint: v0.6.367",
        "- artifact_scope: private_reviewer_only",
        "- publication_approved: false",
        "- raw_execution_status: completed",
        "- reviewer_execution_status: mock_dry_run_completed_no_real_execution",
        "- raw_and_reviewer_status_separated: true",
        "- external_process_executed: false",
        "- network_activity_performed: false",
        "",
        "## Gate results",
    ]
    for gate in artifact["gateway_validation_result"]["gate_results"]:
        lines.append(f"- {gate['gate_id']}: {gate['gate_status']} / allowed_to_continue={str(gate['allowed_to_continue']).lower()}")
    lines.extend(["", "## Limitations"])
    for item in artifact["gateway_validation_result"]["limitations"]:
        lines.append(f"- {item}")
    MD_ARTIFACT.write_text("\n".join(lines) + "\n", encoding="utf-8")

def test_v06367_private_artifact_generation_and_shape() -> None:
    write_private_artifacts()
    artifact = json.loads(JSON_ARTIFACT.read_text(encoding="utf-8"))
    assert artifact["artifact_scope"] == "private_reviewer_only"
    assert artifact["publication_approved"] is False
    assert artifact["schema_changed"] is False
    assert artifact["generated_outputs_changed"] is False
    assert artifact["runtime_changed"] is False
    assert artifact["public_artifact_changed"] is False
    result = artifact["gateway_validation_result"]
    assert result["raw_execution_status"] == "completed"
    assert result["reviewer_execution_status"] == "mock_dry_run_completed_no_real_execution"
    assert result["raw_and_reviewer_status_separated"] is True
    assert result["external_process_executed"] is False
    assert result["network_activity_performed"] is False
    gates = {gate["gate_id"]: gate for gate in result["gate_results"]}
    for gate_id in ["authorization_expiry_current_time", "request_decision_constraint_diff", "external_discovery_fail_closed", "non_dispatch_legacy_path_preservation", "existing_policy_error_path_preservation"]:
        assert gate_id in gates
    limitations = set(result["limitations"])
    for item in ["private reviewer artifact candidate only", "not scanner output", "not legal proof", "not audit opinion", "not execution authorization", "not external target authorization", "not production readiness"]:
        assert item in limitations
    md = MD_ARTIFACT.read_text(encoding="utf-8")
    assert "mock_dry_run_completed_no_real_execution" in md
    assert "external_process_executed: false" in md
    assert "network_activity_performed: false" in md

def test_v06367_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["private-not-in-git/gateway-validation-result-evidence-traces/v0.6.367/demo", "gateway-validation-result-evidence-trace.generated.json", "v0.6.368 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision"])
    assert_tokens(ADR, ["ADR-0442", "Status: proposed artifact candidate"])
    assert_tokens(ISSUE, ["0442 - Add v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate", "Status: completed by v0.6.367"])

def test_v06367_index_files() -> None:
    assert_tokens(README, ["v0.6.367 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate", "private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_created = true", "private_reviewer_gateway_validation_result_evidence_trace_artifact_publication_approved = false", "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_review_and_decision"])
    assert_tokens(CHANGELOG, ["v0.6.367 - Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate", "private-not-in-git/gateway-validation-result-evidence-traces/v0.6.367/demo"])
    assert_tokens(ROADMAP, ["After v0.6.367", "v0.6.368 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision"])

def test_v06367_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06367_private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate.py"])

def test_v06367_no_unsupported_claims() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for phrase in ["production-ready scanner", "runtime-enforced scanner", "external-target-ready demo", "customer-ready PoC", "certified / audit-ready system", "compliance-sufficient control", "diagnostically complete", "diagnostically-complete"]:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06367_private_artifact_generation_and_shape()
    test_v06367_primary_files()
    test_v06367_index_files()
    test_v06367_registered_in_run_all()
    test_v06367_no_unsupported_claims()
    print("v0.6.367 private reviewer Gateway validation result evidence trace artifact candidate checks passed")

if __name__ == "__main__":
    main()
