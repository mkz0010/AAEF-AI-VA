from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD_ISSUE_PATH = ROOT / "planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanout-review.md"
NEW_ISSUE_PATH = ROOT / "planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanup-review.md"
DOC = ROOT / "docs/449-v06374-mock-dry-run-status-terminology-public-output-cleanup-issue-filename-normalization.md"
ADR = ROOT / "planning/decisions/ADR-0449-add-v06374-mock-dry-run-status-terminology-public-output-cleanup-issue-filename-normalization.md"
ISSUE = ROOT / "planning/issues/0449-add-v06374-mock-dry-run-status-terminology-public-output-cleanup-issue-filename-normalization.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.374 Mock/Dry-Run Status Terminology Public Output Cleanup Issue Filename Normalization', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_completed = true', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_scope = filename_only', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_old_path = planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanout-review.md', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_new_path = planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanup-review.md', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_cleanout_removed_from_current_tree = true', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_cleanup_present_in_current_tree = true', 'mock_dry_run_status_terminology_public_output_cleanup_track_already_closed = true', 'mock_dry_run_status_terminology_public_output_cleanup_status = closed_as_display_cleanup', 'mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true', 'mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true', 'controlled_executor_validation_gateway_core_connection_next_priority = true', 'v06374_gateway_core_behavior_changed = false', 'v06374_tool_gateway_behavior_changed = false', 'v06374_runtime_behavior_changed = false', 'v06374_scanner_behavior_changed = false', 'v06374_schema_changed = false', 'v06374_generated_outputs_changed = false', 'v06374_public_artifacts_changed = false', 'v06374_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review', 'controlled_executor_validation_gateway_core_connection_readiness_review_recommended = true', 'mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Filename normalization is not production readiness.', 'Filename normalization is not scanner readiness.', 'Filename normalization is not execution authorization.', 'Filename normalization is not real execution permission.', 'Filename normalization is not external target authorization.', 'Filename normalization is not customer demo approval.', 'Filename normalization is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.374.', 'v0.6.375 Controlled Executor Validation Gateway Core Connection Readiness Review']
EXPECTED_ALLOWED = "allowed-action: raw_execution_status=completed; reviewer_status=mock_dry_run_completed_no_real_execution; external_process_executed=false; network_activity_performed=false"

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def git_ls_files() -> str:
    completed = subprocess.run(["git", "ls-files"], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return completed.stdout

def run_command(args: list[str]) -> str:
    completed = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return completed.stdout + completed.stderr

def test_v06374_filename_normalized() -> None:
    assert not OLD_ISSUE_PATH.exists(), f"old typo path still exists: {OLD_ISSUE_PATH.relative_to(ROOT)}"
    assert NEW_ISSUE_PATH.exists(), f"new normalized path missing: {NEW_ISSUE_PATH.relative_to(ROOT)}"
    tracked = git_ls_files()
    assert OLD_ISSUE_PATH.relative_to(ROOT).as_posix() not in tracked
    assert NEW_ISSUE_PATH.relative_to(ROOT).as_posix() in tracked

def test_v06374_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Result: issue filename typo normalized from `cleanout` to `cleanup`", EXPECTED_ALLOWED])
    assert_tokens(ADR, ["ADR-0449", "Status: accepted", "cleanout` instead of `cleanup`"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.374", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review"])

def test_v06374_runner_display_still_clean() -> None:
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output

def test_v06374_index_files() -> None:
    assert_tokens(README, ["v0.6.374 Mock/Dry-Run Status Terminology Public Output Cleanup Issue Filename Normalization", "mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_completed = true", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review"])
    assert_tokens(CHANGELOG, ["v0.6.374 - Mock/Dry-Run Status Terminology Public Output Cleanup Issue Filename Normalization", "cleanout` to `cleanup`"])
    assert_tokens(ROADMAP, ["After v0.6.374", "v0.6.375 Controlled Executor Validation Gateway Core Connection Readiness Review"])

def test_v06374_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06374_mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization.py"])

def main() -> None:
    test_v06374_filename_normalized()
    test_v06374_primary_files()
    test_v06374_runner_display_still_clean()
    test_v06374_index_files()
    test_v06374_registered_in_run_all()
    print("v0.6.374 mock/dry-run status terminology cleanup issue filename normalization checks passed")

if __name__ == "__main__":
    main()
