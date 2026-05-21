from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/447-v06372-mock-dry-run-status-terminology-public-output-cleanup-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0447-add-v06372-mock-dry-run-status-terminology-public-output-cleanup-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0447-add-v06372-mock-dry-run-status-terminology-public-output-cleanup-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
RUNNER = ROOT / "prototypes/tool-gateway/runner.py"
PUBLIC_ARTIFACT = ROOT / "docs/public-artifacts/safe-mock-demo-public-artifact.md"

REQUIRED = ['v0.6.372 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate Review and Decision', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_review_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_decision = accepted', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_accepted = true', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_status = accepted_pending_closeout_review', 'mock_dry_run_status_terminology_public_output_cleanup_runner_console_output_reviewed = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_artifact_status_lines_reviewed = true', 'mock_dry_run_status_terminology_public_output_cleanup_readme_status_wording_reviewed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_accepted = true', 'mock_dry_run_status_terminology_public_output_cleanup_external_process_executed_display_accepted = true', 'mock_dry_run_status_terminology_public_output_cleanup_network_activity_performed_display_accepted = true', 'mock_dry_run_status_terminology_public_output_cleanup_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_generated_output_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_runtime_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_gateway_core_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_raw_result_json_status_changed = false', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'v06372_gateway_core_behavior_changed = false', 'v06372_tool_gateway_behavior_changed = false', 'v06372_runtime_behavior_changed = false', 'v06372_scanner_behavior_changed = false', 'v06372_schema_changed = false', 'v06372_generated_outputs_changed = false', 'v06372_public_artifacts_changed = false', 'v06372_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_closeout_review', 'mock_dry_run_status_terminology_public_output_cleanup_closeout_review_recommended = true', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Candidate acceptance is not production readiness.', 'Candidate acceptance is not scanner readiness.', 'Candidate acceptance is not execution authorization.', 'Candidate acceptance is not real execution permission.', 'Candidate acceptance is not external target authorization.', 'Candidate acceptance is not customer demo approval.', 'Candidate acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.372.', 'v0.6.373 Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review']
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

def test_v06372_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Review result: accepted pending closeout review", EXPECTED_ALLOWED, EXPECTED_MULTILINE])
    assert_tokens(ADR, ["ADR-0447", "Status: accepted", "Accept the v0.6.371 display cleanup candidate"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.372", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_closeout_review"])

def test_v06372_runner_and_public_display() -> None:
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output
    public_text = read(PUBLIC_ARTIFACT)
    assert "allowed-action: completed" not in public_text
    assert EXPECTED_MULTILINE in public_text

def test_v06372_index_files() -> None:
    assert_tokens(README, ["v0.6.372 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate Review and Decision", "mock_dry_run_status_terminology_public_output_cleanup_candidate_decision = accepted", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_closeout_review"])
    assert "allowed-action: completed" not in read(README)
    assert_tokens(CHANGELOG, ["v0.6.372 - Mock/Dry-Run Status Terminology Public Output Cleanup Candidate Review and Decision", "raw/reviewer separation"])
    assert_tokens(ROADMAP, ["After v0.6.372", "v0.6.373 Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review"])

def test_v06372_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06372_mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision.py"])

def main() -> None:
    test_v06372_primary_files()
    test_v06372_runner_and_public_display()
    test_v06372_index_files()
    test_v06372_registered_in_run_all()
    print("v0.6.372 mock/dry-run status terminology public output cleanup candidate review and decision checks passed")

if __name__ == "__main__":
    main()
