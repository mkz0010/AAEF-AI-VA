from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/448-v06373-mock-dry-run-status-terminology-public-output-cleanup-closeout-review.md"
ADR = ROOT / "planning/decisions/ADR-0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanup-closeout-review.md"
ISSUE = ROOT / "planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanout-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
RUNNER = ROOT / "prototypes/tool-gateway/runner.py"
PUBLIC_ARTIFACT = ROOT / "docs/public-artifacts/safe-mock-demo-public-artifact.md"

REQUIRED = ['v0.6.373 Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review', 'mock_dry_run_status_terminology_public_output_cleanup_closeout_review_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_track_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_status = closed_as_display_cleanup', 'mock_dry_run_status_terminology_public_output_cleanup_readiness_review_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_accepted = true', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_decision = accepted', 'mock_dry_run_status_terminology_public_output_cleanup_runner_console_output_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_artifact_status_lines_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_readme_status_wording_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_external_process_executed_display_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_network_activity_performed_display_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_generated_output_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_runtime_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_gateway_core_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_raw_result_json_status_changed = false', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_connection_next_priority = true', 'common_target_scope_tool_operation_binding_gateway_core_integration_deferred = true', 'readme_front_page_simplification_still_required = true', 'v06373_gateway_core_behavior_changed = false', 'v06373_tool_gateway_behavior_changed = false', 'v06373_runtime_behavior_changed = false', 'v06373_scanner_behavior_changed = false', 'v06373_schema_changed = false', 'v06373_generated_outputs_changed = false', 'v06373_public_artifacts_changed = false', 'v06373_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review', 'controlled_executor_validation_gateway_core_connection_readiness_review_recommended = true', 'mock_dry_run_status_terminology_public_output_cleanup_closeout_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Closeout review is not production readiness.', 'Closeout review is not scanner readiness.', 'Closeout review is not execution authorization.', 'Closeout review is not real execution permission.', 'Closeout review is not external target authorization.', 'Closeout review is not customer demo approval.', 'Closeout review is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.373.', 'v0.6.374 Controlled Executor Validation Gateway Core Connection Readiness Review']
EXPECTED_ALLOWED = "allowed-action: raw_execution_status=completed; reviewer_status=mock_dry_run_completed_no_real_execution; external_process_executed=false; network_activity_performed=false"
EXPECTED_MULTILINE = 'allowed-action:\n  raw_execution_status: completed\n  reviewer_status: mock_dry_run_completed_no_real_execution\n  external_process_executed: false\n  network_activity_performed: false'

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def run_command(args: list[str]) -> str:
    completed = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return completed.stdout + completed.stderr

def test_v06373_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Closeout result: public/runner-facing mock/dry-run status terminology cleanup closed as display cleanup", EXPECTED_ALLOWED, EXPECTED_MULTILINE])
    assert_tokens(ADR, ["ADR-0448", "Status: accepted", "Close the mock/dry-run status terminology public-output cleanup track"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.373", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review"])

def test_v06373_runner_and_public_display() -> None:
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output
    public_text = read(PUBLIC_ARTIFACT)
    assert "allowed-action: completed" not in public_text
    assert EXPECTED_MULTILINE in public_text

def test_v06373_index_files() -> None:
    assert_tokens(README, ["v0.6.373 Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review", "mock_dry_run_status_terminology_public_output_cleanup_track_closed = true", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review"])
    assert "allowed-action: completed" not in read(README)
    assert_tokens(CHANGELOG, ["v0.6.373 - Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review", "cleanup track"])
    assert_tokens(ROADMAP, ["After v0.6.373", "v0.6.374 Controlled Executor Validation Gateway Core Connection Readiness Review"])

def test_v06373_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06373_mock_dry_run_status_terminology_public_output_cleanup_closeout_review.py"])

def main() -> None:
    test_v06373_primary_files()
    test_v06373_runner_and_public_display()
    test_v06373_index_files()
    test_v06373_registered_in_run_all()
    print("v0.6.373 mock/dry-run status terminology public output cleanup closeout review checks passed")

if __name__ == "__main__":
    main()
