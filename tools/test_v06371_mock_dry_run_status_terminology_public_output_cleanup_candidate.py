from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/446-v06371-mock-dry-run-status-terminology-public-output-cleanup-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0446-add-v06371-mock-dry-run-status-terminology-public-output-cleanup-candidate.md"
ISSUE = ROOT / "planning/issues/0446-add-v06371-mock-dry-run-status-terminology-public-output-cleanup-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
RUNNER = ROOT / "prototypes/tool-gateway/runner.py"
PUBLIC_ARTIFACT = ROOT / "docs/public-artifacts/safe-mock-demo-public-artifact.md"

REQUIRED = ['v0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate', 'mock_dry_run_status_terminology_public_output_cleanup_candidate_created = true', 'mock_dry_run_status_terminology_public_output_cleanup_runner_console_output_changed = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_artifact_status_lines_changed = true', 'mock_dry_run_status_terminology_public_output_cleanup_readme_status_wording_changed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true', 'mock_dry_run_status_terminology_public_output_cleanup_reviewer_status_value = mock_dry_run_completed_no_real_execution', 'mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true', 'mock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_applied = true', 'mock_dry_run_status_terminology_public_output_cleanup_external_process_executed_displayed = true', 'mock_dry_run_status_terminology_public_output_cleanup_network_activity_performed_displayed = true', 'mock_dry_run_status_terminology_public_output_cleanup_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_generated_output_schema_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_runtime_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_gateway_core_behavior_change_now = false', 'mock_dry_run_status_terminology_public_output_cleanup_raw_result_json_status_changed = false', 'private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_closed = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'v06371_gateway_core_behavior_changed = false', 'v06371_tool_gateway_behavior_changed = false', 'v06371_runtime_behavior_changed = false', 'v06371_scanner_behavior_changed = false', 'v06371_schema_changed = false', 'v06371_generated_outputs_changed = false', 'v06371_public_artifacts_changed = true', 'v06371_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Cleanup candidate is not production readiness.', 'Cleanup candidate is not scanner readiness.', 'Cleanup candidate is not execution authorization.', 'Cleanup candidate is not real execution permission.', 'Cleanup candidate is not external target authorization.', 'Cleanup candidate is not customer demo approval.', 'Cleanup candidate is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.371.', 'v0.6.372 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate Review and Decision']
EXPECTED_ALLOWED = "allowed-action: raw_execution_status=completed; reviewer_status=mock_dry_run_completed_no_real_execution; external_process_executed=false; network_activity_performed=false"

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

def test_v06371_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Expected allowed-action display", EXPECTED_ALLOWED])
    assert_tokens(ADR, ["ADR-0446", "Status: proposed"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.371", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision"])

def test_v06371_runner_console_output() -> None:
    assert "_format_mock_dry_run_status_line" in read(RUNNER)
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output
    assert "denied-action: blocked" in output
    assert "human-approval-required: requires_human_approval" in output

def test_v06371_public_artifact_and_readme_status_lines() -> None:
    public_text = read(PUBLIC_ARTIFACT)
    readme_text = read(README)
    assert "allowed-action: completed" not in public_text
    assert "allowed-action: completed" not in readme_text
    assert "reviewer_status: mock_dry_run_completed_no_real_execution" in public_text
    assert EXPECTED_ALLOWED in readme_text

def test_v06371_index_files() -> None:
    assert_tokens(README, ["v0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate", "mock_dry_run_status_terminology_public_output_cleanup_candidate_created = true", "recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision"])
    assert_tokens(CHANGELOG, ["v0.6.371 - Mock/Dry-Run Status Terminology Public Output Cleanup Candidate", "bare `allowed-action: completed`"])
    assert_tokens(ROADMAP, ["After v0.6.371", "v0.6.372 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate Review and Decision"])

def test_v06371_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06371_mock_dry_run_status_terminology_public_output_cleanup_candidate.py"])

def main() -> None:
    test_v06371_primary_files()
    test_v06371_runner_console_output()
    test_v06371_public_artifact_and_readme_status_lines()
    test_v06371_index_files()
    test_v06371_registered_in_run_all()
    print("v0.6.371 mock/dry-run status terminology public output cleanup candidate checks passed")

if __name__ == "__main__":
    main()
