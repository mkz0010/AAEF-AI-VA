from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/451-v06376-controlled-executor-validation-gateway-core-connection-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0451-add-v06376-controlled-executor-validation-gateway-core-connection-candidate.md"
ISSUE = ROOT / "planning/issues/0451-add-v06376-controlled-executor-validation-gateway-core-connection-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
GATEWAY = ROOT / "prototypes/tool-gateway/gateway.py"

REQUIRED = ['v0.6.376 Controlled Executor Validation Gateway Core Connection Candidate', 'controlled_executor_validation_gateway_core_connection_candidate_created = true', 'controlled_executor_validation_gateway_core_connection_candidate_status = implemented_pending_review', 'controlled_executor_validation_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_call_added = true', 'controlled_executor_validation_command_plan_validation_required = true', 'controlled_executor_validation_gate_expected_fail_closed = true', 'controlled_executor_validation_policy_failure_blocks_before_result_generation = true', 'controlled_executor_validation_external_process_executed_flag_checked = true', 'controlled_executor_validation_network_activity_performed_flag_checked = true', 'controlled_executor_validation_real_execution_mode_checked = true', 'controlled_executor_validation_no_real_execution_boundary_preserved = true', 'controlled_executor_validation_raw_result_status_compatibility_preserved = true', 'controlled_executor_validation_reviewer_status_compatibility_preserved = true', 'controlled_executor_validation_gateway_core_connection_mode = fallback_gateway_context_command_plan', 'controlled_executor_validation_explicit_command_plan_assignment_found = false', 'controlled_executor_validation_fallback_gateway_context_command_plan_used = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'v06376_gateway_core_behavior_changed = true', 'v06376_tool_gateway_behavior_changed = true', 'v06376_runtime_behavior_changed = false', 'v06376_scanner_behavior_changed = false', 'v06376_schema_changed = false', 'v06376_generated_outputs_changed = false', 'v06376_public_artifacts_changed = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate_review_and_decision', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Connection candidate is not production readiness.', 'Connection candidate is not scanner readiness.', 'Connection candidate is not execution authorization.', 'Connection candidate is not real execution permission.', 'Connection candidate is not external target authorization.', 'Connection candidate is not customer demo approval.', 'Connection candidate is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.376.', 'v0.6.377 Controlled Executor Validation Gateway Core Connection Candidate Review and Decision']
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

def test_v06376_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Candidate result: implemented pending review", EXPECTED_ALLOWED])
    assert_tokens(ADR, ["ADR-0451", "Status: proposed"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.376", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate_review_and_decision"])

def test_v06376_gateway_core_connection_present() -> None:
    gateway_text = read(GATEWAY)
    assert "def _validate_controlled_executor_command_plan" in gateway_text
    assert "def _fail_closed_for_controlled_executor_validation" in gateway_text
    assert "controlled_executor_validation = _validate_controlled_executor_command_plan(command_plan)" in gateway_text
    assert "_fail_closed_for_controlled_executor_validation(controlled_executor_validation)" in gateway_text

def test_v06376_runner_display() -> None:
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output

def test_v06376_index_files() -> None:
    assert_tokens(README, ["v0.6.376 Controlled Executor Validation Gateway Core Connection Candidate", "controlled_executor_validation_gateway_core_integrated = true", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate_review_and_decision"])
    assert_tokens(CHANGELOG, ["v0.6.376 - Controlled Executor Validation Gateway Core Connection Candidate"])
    assert_tokens(ROADMAP, ["After v0.6.376", "v0.6.377 Controlled Executor Validation Gateway Core Connection Candidate Review and Decision"])

def test_v06376_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06376_controlled_executor_validation_gateway_core_connection_candidate.py"])

def main() -> None:
    test_v06376_primary_files()
    test_v06376_gateway_core_connection_present()
    test_v06376_runner_display()
    test_v06376_index_files()
    test_v06376_registered_in_run_all()
    print("v0.6.376 controlled executor validation Gateway core connection candidate checks passed")

if __name__ == "__main__":
    main()
