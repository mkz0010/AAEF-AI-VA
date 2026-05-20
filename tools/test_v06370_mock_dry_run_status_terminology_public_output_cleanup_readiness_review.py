from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/445-v06370-mock-dry-run-status-terminology-public-output-cleanup-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0445-add-v06370-mock-dry-run-status-terminology-public-output-cleanup-readiness-review.md"
ISSUE = ROOT / "planning/issues/0445-add-v06370-mock-dry-run-status-terminology-public-output-cleanup-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.370 Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review', 'mock_dry_run_status_terminology_public_output_cleanup_readiness_review_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_scope_defined = true', 'mock_dry_run_status_terminology_public_output_cleanup_ready_for_candidate = true', 'mock_dry_run_status_terminology_public_output_cleanup_target_runner_console_output = true', 'mock_dry_run_status_terminology_public_output_cleanup_target_public_artifact_status_lines = true', 'mock_dry_run_status_terminology_public_output_cleanup_target_readme_status_wording = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true', 'mock_dry_run_status_terminology_public_output_cleanup_reviewer_status_value = mock_dry_run_completed_no_real_execution', 'mock_dry_run_status_terminology_public_output_cleanup_public_display_must_not_show_bare_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_required = true', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_closed = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'v06370_gateway_core_behavior_changed = false', 'v06370_tool_gateway_behavior_changed = false', 'v06370_runtime_behavior_changed = false', 'v06370_scanner_behavior_changed = false', 'v06370_schema_changed = false', 'v06370_generated_outputs_changed = false', 'v06370_public_artifacts_changed = false', 'v06370_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Readiness review is not production readiness.', 'Readiness review is not scanner readiness.', 'Readiness review is not execution authorization.', 'Readiness review is not real execution permission.', 'Readiness review is not external target authorization.', 'Readiness review is not customer demo approval.', 'Readiness review is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.370.', 'v0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06370_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["| Target area | v0.6.370 readiness decision |", "raw_execution_status: completed", "reviewer_status: mock_dry_run_completed_no_real_execution", "v0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate"])
    assert_tokens(ADR, ["ADR-0445", "Status: accepted", "Prepare Mock/Dry-Run Status Terminology Public Output Cleanup"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.370", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate"])

def test_v06370_index_files() -> None:
    assert_tokens(README, ["v0.6.370 Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review", "mock_dry_run_status_terminology_public_output_cleanup_readiness_review_completed = true", "mock_dry_run_status_terminology_public_output_cleanup_public_display_must_not_show_bare_completed = true", "v06370_schema_changed = false", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate"])
    assert_tokens(CHANGELOG, ["v0.6.370 - Mock/Dry-Run Status Terminology Public Output Cleanup Readiness Review", "mock_dry_run_completed_no_real_execution"])
    assert_tokens(ROADMAP, ["After v0.6.370", "v0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate", "raw status compatibility is preserved"])

def test_v06370_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06370_mock_dry_run_status_terminology_public_output_cleanup_readiness_review.py"])

def test_v06370_no_unsupported_claims() -> None:
    forbidden = ["production-ready scanner", "runtime-enforced scanner", "external-target-ready demo", "customer-ready PoC", "certified / audit-ready system", "compliance-sufficient control", "diagnostically complete"]
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for phrase in forbidden:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains forbidden phrase: {phrase}"

def main() -> None:
    test_v06370_primary_files()
    test_v06370_index_files()
    test_v06370_registered_in_run_all()
    test_v06370_no_unsupported_claims()
    print("v0.6.370 mock/dry-run status terminology public output cleanup readiness review checks passed")

if __name__ == "__main__":
    main()