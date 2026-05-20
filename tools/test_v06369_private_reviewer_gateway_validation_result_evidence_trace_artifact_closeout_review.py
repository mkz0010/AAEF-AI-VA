from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/444-v06369-private-reviewer-gateway-validation-result-evidence-trace-artifact-closeout-review.md"
ADR = ROOT / "planning/decisions/ADR-0444-add-v06369-private-reviewer-gateway-validation-result-evidence-trace-artifact-closeout-review.md"
ISSUE = ROOT / "planning/issues/0444-add-v06369-private-reviewer-gateway-validation-result-evidence-trace-artifact-closeout-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.369 Private Reviewer Gateway Validation Result Evidence Trace Artifact Closeout Review', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review_completed = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_path_accepted = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_closed = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_status = closed_as_private_reviewer_artifact_path', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_path = private-not-in-git/gateway-validation-result-evidence-traces/v0.6.367/demo', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_private_only = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_publication_approved = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_schema_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_generated_outputs_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_runtime_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_public_artifact_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_raw_and_reviewer_status_separated = true', 'gateway_validation_result_application_phase_2_schema_field_decision = deferred', 'gateway_validation_result_application_phase_3_generated_output_application_decision = deferred', 'gateway_validation_result_application_phase_4_runtime_application_decision = deferred', 'gateway_validation_result_application_public_artifact_change_decision = deferred', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'mock_dry_run_status_terminology_public_output_cleanup_required = true', 'mock_dry_run_status_terminology_public_output_cleanup_next_priority = true', 'v06369_gateway_core_behavior_changed = false', 'v06369_tool_gateway_behavior_changed = false', 'v06369_runtime_behavior_changed = false', 'v06369_scanner_behavior_changed = false', 'v06369_schema_changed = false', 'v06369_generated_outputs_changed = false', 'v06369_public_artifacts_changed = false', 'v06369_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_readiness_review', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Closeout review is not production readiness.', 'Closeout review is not scanner readiness.', 'Closeout review is not execution authorization.', 'Closeout review is not real execution permission.', 'Closeout review is not external target authorization.', 'Closeout review is not customer demo approval.', 'Closeout review is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.369.', 'v0.6.370 Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06369_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["| Area | Closeout status |", "Private reviewer artifact path | accepted and closed", "v0.6.370 Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review"])
    assert_tokens(ADR, ["ADR-0444", "Status: accepted", "Close the private reviewer Gateway validation result evidence trace artifact path as accepted"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.369", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_readiness_review"])

def test_v06369_index_files() -> None:
    assert_tokens(README, ["v0.6.369 Private Reviewer Gateway Validation Result Evidence Trace Artifact Closeout Review", "private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review_completed = true", "mock_dry_run_status_terminology_public_output_cleanup_next_priority = true", "v06369_schema_changed = false", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_readiness_review"])
    assert_tokens(CHANGELOG, ["v0.6.369 - Private Reviewer Gateway Validation Result Evidence Trace Artifact Closeout Review", "mock/dry-run status terminology public output cleanup is the next priority"])
    assert_tokens(ROADMAP, ["After v0.6.369", "v0.6.370 Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review", "no evidence-record schema change in v0.6.369"])

def test_v06369_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06369_private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review.py"])

def test_v06369_no_unsupported_claims() -> None:
    forbidden = ["production-ready scanner", "runtime-enforced scanner", "external-target-ready demo", "customer-ready PoC", "certified / audit-ready system", "compliance-sufficient control", "diagnostically complete"]
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for phrase in forbidden:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains forbidden phrase: {phrase}"

def main() -> None:
    test_v06369_primary_files()
    test_v06369_index_files()
    test_v06369_registered_in_run_all()
    test_v06369_no_unsupported_claims()
    print("v0.6.369 private reviewer Gateway validation result evidence trace artifact closeout review checks passed")

if __name__ == "__main__":
    main()
