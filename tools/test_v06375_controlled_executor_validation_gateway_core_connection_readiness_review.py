from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/450-v06375-controlled-executor-validation-gateway-core-connection-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0450-add-v06375-controlled-executor-validation-gateway-core-connection-readiness-review.md"
ISSUE = ROOT / "planning/issues/0450-add-v06375-controlled-executor-validation-gateway-core-connection-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
CONTROLLED_EXECUTOR_TEST = ROOT / "tools/test_controlled_executor_policy.py"
RUNNER = ROOT / "prototypes/tool-gateway/runner.py"
GATEWAY = ROOT / "prototypes/tool-gateway/gateway.py"

REQUIRED = ['v0.6.375 Controlled Executor Validation Gateway Core Connection Readiness Review', 'controlled_executor_validation_gateway_core_connection_readiness_review_completed = true', 'controlled_executor_validation_gateway_core_connection_scope_defined = true', 'controlled_executor_validation_gateway_core_connection_ready_for_candidate = true', 'controlled_executor_validation_gateway_core_connection_candidate_recommended = true', 'controlled_executor_policy_available = true', 'controlled_executor_policy_tests_available = true', 'controlled_executor_policy_tests_pass_required = true', 'controlled_executor_validation_current_gateway_core_integrated = false', 'controlled_executor_validation_gateway_core_target_position = after_command_plan_build_before_result_and_evidence_generation', 'controlled_executor_validation_gateway_core_candidate_should_be_display_and_evidence_safe = true', 'controlled_executor_validation_command_plan_validation_required = true', 'controlled_executor_validation_gate_expected_fail_closed = true', 'controlled_executor_validation_blocked_result_required_on_policy_failure = true', 'controlled_executor_validation_external_process_executed_flag_required = true', 'controlled_executor_validation_network_activity_performed_flag_required = true', 'controlled_executor_validation_no_real_execution_boundary_required = true', 'controlled_executor_validation_raw_result_status_compatibility_required = true', 'controlled_executor_validation_reviewer_status_compatibility_required = true', 'controlled_executor_validation_gateway_validation_result_evidence_trace_future_candidate = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integration_deferred = true', 'readme_front_page_simplification_still_required = true', 'v06375_gateway_core_behavior_changed = false', 'v06375_tool_gateway_behavior_changed = false', 'v06375_runtime_behavior_changed = false', 'v06375_scanner_behavior_changed = false', 'v06375_schema_changed = false', 'v06375_generated_outputs_changed = false', 'v06375_public_artifacts_changed = false', 'v06375_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate', 'controlled_executor_validation_gateway_core_connection_readiness_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Readiness review is not production readiness.', 'Readiness review is not scanner readiness.', 'Readiness review is not execution authorization.', 'Readiness review is not real execution permission.', 'Readiness review is not external target authorization.', 'Readiness review is not customer demo approval.', 'Readiness review is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.375.', 'v0.6.376 Controlled Executor Validation Gateway Core Connection Candidate']
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

def test_v06375_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["Readiness result: connection scope defined and ready for candidate", "after_command_plan_build_before_result_and_evidence_generation", EXPECTED_ALLOWED])
    assert_tokens(ADR, ["ADR-0450", "Status: accepted", "Prepare Controlled Executor Validation Gateway Core Connection"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.375", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate"])

def test_v06375_controlled_executor_policy_available_and_not_core_integrated() -> None:
    assert CONTROLLED_EXECUTOR_TEST.exists(), "controlled executor policy test must exist before connection candidate"
    gateway_text = read(GATEWAY)
    assert "run_mock_tool_gateway" in gateway_text
    assert "controlled_executor_validation_gateway_core_integrated = false" in read(DOC)

def test_v06375_runner_display_still_clean() -> None:
    output = run_command([sys.executable, "tools/run_tool_gateway_example.py", "all"])
    assert EXPECTED_ALLOWED in output
    assert "allowed-action: completed" not in output

def test_v06375_index_files() -> None:
    assert_tokens(README, ["v0.6.375 Controlled Executor Validation Gateway Core Connection Readiness Review", "controlled_executor_validation_gateway_core_connection_readiness_review_completed = true", "recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate"])
    assert_tokens(CHANGELOG, ["v0.6.375 - Controlled Executor Validation Gateway Core Connection Readiness Review", "after command plan construction and before result/evidence generation"])
    assert_tokens(ROADMAP, ["After v0.6.375", "v0.6.376 Controlled Executor Validation Gateway Core Connection Candidate"])

def test_v06375_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06375_controlled_executor_validation_gateway_core_connection_readiness_review.py"])

def main() -> None:
    test_v06375_primary_files()
    test_v06375_controlled_executor_policy_available_and_not_core_integrated()
    test_v06375_runner_display_still_clean()
    test_v06375_index_files()
    test_v06375_registered_in_run_all()
    print("v0.6.375 controlled executor validation Gateway core connection readiness review checks passed")

if __name__ == "__main__":
    main()
