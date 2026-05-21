from __future__ import annotations
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/452-v06377-controlled-executor-validation-gateway-core-connection-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0452-add-v06377-controlled-executor-validation-gateway-core-connection-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0452-add-v06377-controlled-executor-validation-gateway-core-connection-candidate-review-and-decision.md"
V06376_DOC = ROOT / "docs/451-v06376-controlled-executor-validation-gateway-core-connection-candidate.md"
GATEWAY = ROOT / "prototypes/tool-gateway/gateway.py"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
REQUIRED = ['v0.6.377 Controlled Executor Validation Gateway Core Connection Candidate Review and Decision', 'controlled_executor_validation_gateway_core_connection_candidate_review_completed = true', 'controlled_executor_validation_gateway_core_connection_candidate_decision = accepted_with_fallback_mode', 'controlled_executor_validation_gateway_core_connection_candidate_accepted = true', 'controlled_executor_validation_gateway_core_connection_candidate_status = accepted_pending_explicit_command_plan_exposure_review', 'controlled_executor_validation_gateway_core_integrated = true', 'controlled_executor_validation_gateway_core_call_present = true', 'controlled_executor_validation_gateway_core_connection_mode = fallback_gateway_context_command_plan', 'controlled_executor_validation_explicit_command_plan_assignment_found = false', 'controlled_executor_validation_fallback_gateway_context_command_plan_used = true', 'controlled_executor_validation_fallback_gateway_context_command_plan_accepted = true', 'controlled_executor_validation_fallback_mode_limitation_recorded = true', 'controlled_executor_validation_explicit_command_plan_exposure_next_priority = true', 'controlled_executor_validation_gate_expected_fail_closed = true', 'controlled_executor_validation_policy_failure_blocks_before_result_generation = true', 'controlled_executor_validation_no_real_execution_boundary_preserved = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'v06377_gateway_core_behavior_changed = false', 'v06377_tool_gateway_behavior_changed = false', 'v06377_runtime_behavior_changed = false', 'v06377_scanner_behavior_changed = false', 'v06377_schema_changed = false', 'v06377_generated_outputs_changed = false', 'v06377_public_artifacts_changed = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_explicit_command_plan_exposure_readiness_review', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Candidate acceptance is not production readiness.', 'Candidate acceptance is not scanner readiness.', 'Candidate acceptance is not execution authorization.', 'Candidate acceptance is not real execution permission.', 'Candidate acceptance is not external target authorization.', 'Candidate acceptance is not customer demo approval.', 'Candidate acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.377.', 'v0.6.378 Controlled Executor Validation Explicit Command Plan Exposure Readiness Review']
EXPECTED_ALLOWED = "allowed-action: raw_execution_status=completed; reviewer_status=mock_dry_run_completed_no_real_execution; external_process_executed=false; network_activity_performed=false"
def read(path: Path) -> str:
    assert path.exists(), f'missing file: {path.relative_to(ROOT)}'
    return path.read_text(encoding='utf-8')
def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f'{path.relative_to(ROOT)} missing token: {token}'
def run_command(args: list[str]) -> str:
    p = subprocess.run(args, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return p.stdout + p.stderr
def test_v06377_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ['Review result: accepted with fallback mode', EXPECTED_ALLOWED])
    assert_tokens(ADR, ['ADR-0452', 'Status: accepted'])
    assert_tokens(ISSUE, ['Status: completed by v0.6.377', 'recommended_next_work_item = controlled_executor_validation_explicit_command_plan_exposure_readiness_review'])
def test_v06377_fallback_mode_is_grounded() -> None:
    assert_tokens(V06376_DOC, ['controlled_executor_validation_gateway_core_integrated = true', 'controlled_executor_validation_fallback_gateway_context_command_plan_used = true'])
    gateway_text = read(GATEWAY)
    assert 'def _validate_controlled_executor_command_plan' in gateway_text
    assert '_build_controlled_executor_validation_command_plan_from_gateway_context' in gateway_text
def test_v06377_runner_display() -> None:
    output = run_command([sys.executable, 'tools/run_tool_gateway_example.py', 'all'])
    assert EXPECTED_ALLOWED in output
    assert 'allowed-action: completed' not in output
def test_v06377_index_files() -> None:
    assert_tokens(README, ['v0.6.377 Controlled Executor Validation Gateway Core Connection Candidate Review and Decision', 'controlled_executor_validation_gateway_core_connection_candidate_decision = accepted_with_fallback_mode', 'recommended_next_work_item = controlled_executor_validation_explicit_command_plan_exposure_readiness_review'])
    assert_tokens(CHANGELOG, ['v0.6.377 - Controlled Executor Validation Gateway Core Connection Candidate Review and Decision', 'fallback mode'])
    assert_tokens(ROADMAP, ['After v0.6.377', 'v0.6.378 Controlled Executor Validation Explicit Command Plan Exposure Readiness Review'])
def test_v06377_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ['tools/test_v06377_controlled_executor_validation_gateway_core_connection_candidate_review_and_decision.py'])
def main() -> None:
    test_v06377_primary_files()
    test_v06377_fallback_mode_is_grounded()
    test_v06377_runner_display()
    test_v06377_index_files()
    test_v06377_registered_in_run_all()
    print('v0.6.377 controlled executor validation Gateway core connection candidate review and decision checks passed')
if __name__ == '__main__':
    main()
