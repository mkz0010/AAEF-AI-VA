from __future__ import annotations
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/455-v06380-controlled-executor-validation-explicit-command-plan-exposure-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0455-add-v06380-controlled-executor-validation-explicit-command-plan-exposure-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0455-add-v06380-controlled-executor-validation-explicit-command-plan-exposure-candidate-review-and-decision.md"
V06379_DOC = ROOT / "docs/454-v06379-controlled-executor-validation-explicit-command-plan-exposure-candidate.md"
V06378_DOC = ROOT / "docs/453-v06378-controlled-executor-validation-explicit-command-plan-exposure-readiness-review.md"
GATEWAY = ROOT / "prototypes/tool-gateway/gateway.py"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
REQUIRED = ['v0.6.380 Controlled Executor Validation Explicit Command Plan Exposure Candidate Review and Decision', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_review_completed = true', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_decision = accepted', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_accepted = true', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_status = accepted_pending_evidence_trace_review', 'controlled_executor_validation_explicit_command_plan_object_exposed = true', 'controlled_executor_validation_explicit_command_plan_builder_present = true', 'controlled_executor_validation_explicit_command_plan_feeds_controlled_executor_validation = true', 'controlled_executor_validation_explicit_command_plan_exposure_connection_mode = explicit_gateway_core_command_plan', 'controlled_executor_validation_gateway_core_connection_mode = explicit_gateway_core_command_plan', 'controlled_executor_validation_fallback_gateway_context_command_plan_preserved_for_compatibility = true', 'controlled_executor_validation_fallback_mode_replaced_as_primary_validation_source = true', 'controlled_executor_validation_explicit_command_plan_source_recorded = true', 'controlled_executor_validation_explicit_command_plan_preserves_no_real_execution_defaults = true', 'controlled_executor_validation_explicit_command_plan_raw_completed_compatibility_preserved = true', 'controlled_executor_validation_explicit_command_plan_reviewer_status_compatibility_preserved = true', 'controlled_executor_validation_result_and_command_plan_evidence_trace_next_priority = true', 'controlled_executor_validation_result_should_be_evidence_trace_ready = true', 'controlled_executor_validation_command_plan_should_be_evidence_trace_ready = true', 'controlled_executor_validation_gateway_core_integrated = true', 'controlled_executor_validation_gate_expected_fail_closed = true', 'controlled_executor_validation_policy_failure_blocks_before_result_generation = true', 'controlled_executor_validation_external_process_executed_flag_checked = true', 'controlled_executor_validation_network_activity_performed_flag_checked = true', 'controlled_executor_validation_real_execution_mode_checked = true', 'controlled_executor_validation_no_real_execution_boundary_preserved = true', 'authorization_expiry_current_time_gateway_core_integrated = true', 'request_decision_constraint_diff_gateway_core_integrated = true', 'external_discovery_fail_closed_gateway_core_integrated = true', 'common_target_scope_tool_operation_binding_gateway_core_integrated = false', 'common_target_scope_tool_operation_binding_gateway_core_integration_deferred = true', 'readme_front_page_simplification_still_required = true', 'v06380_gateway_core_behavior_changed = false', 'v06380_tool_gateway_behavior_changed = false', 'v06380_runtime_behavior_changed = false', 'v06380_scanner_behavior_changed = false', 'v06380_schema_changed = false', 'v06380_generated_outputs_changed = false', 'v06380_public_artifacts_changed = false', 'v06380_private_generated_outputs_moved_public = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = controlled_executor_validation_result_and_command_plan_evidence_trace_readiness_review', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Candidate acceptance is not production readiness.', 'Candidate acceptance is not scanner readiness.', 'Candidate acceptance is not execution authorization.', 'Candidate acceptance is not real execution permission.', 'Candidate acceptance is not external target authorization.', 'Candidate acceptance is not customer demo approval.', 'Candidate acceptance is not commercial offer approval.', 'No private generated outputs are moved public in v0.6.380.', 'v0.6.381 Controlled Executor Validation Result and Command Plan Evidence Trace Readiness Review']
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
def test_v06380_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ['Review result: accepted; validation result and command-plan evidence trace remains the next improvement target', EXPECTED_ALLOWED])
    assert_tokens(ADR, ['ADR-0455', 'Status: accepted'])
    assert_tokens(ISSUE, ['Status: completed by v0.6.380', 'recommended_next_work_item = controlled_executor_validation_result_and_command_plan_evidence_trace_readiness_review'])
def test_v06380_grounded_in_v06379_candidate() -> None:
    assert_tokens(V06379_DOC, ['controlled_executor_validation_explicit_command_plan_object_exposed = true', 'controlled_executor_validation_explicit_command_plan_feeds_controlled_executor_validation = true'])
    assert_tokens(V06378_DOC, ['controlled_executor_validation_explicit_command_plan_exposure_ready_for_candidate = true'])
    gateway_text = read(GATEWAY)
    assert 'def _build_explicit_controlled_executor_validation_command_plan' in gateway_text
    assert 'command_plan = _build_explicit_controlled_executor_validation_command_plan(' in gateway_text
    assert 'controlled_executor_validation = _validate_controlled_executor_command_plan(command_plan)' in gateway_text
def test_v06380_runner_display() -> None:
    output = run_command([sys.executable, 'tools/run_tool_gateway_example.py', 'all'])
    assert EXPECTED_ALLOWED in output
    assert 'allowed-action: completed' not in output
def test_v06380_index_files() -> None:
    assert_tokens(README, ['v0.6.380 Controlled Executor Validation Explicit Command Plan Exposure Candidate Review and Decision', 'controlled_executor_validation_explicit_command_plan_exposure_candidate_decision = accepted', 'recommended_next_work_item = controlled_executor_validation_result_and_command_plan_evidence_trace_readiness_review'])
    assert_tokens(CHANGELOG, ['v0.6.380 - Controlled Executor Validation Explicit Command Plan Exposure Candidate Review and Decision'])
    assert_tokens(ROADMAP, ['After v0.6.380', 'v0.6.381 Controlled Executor Validation Result and Command Plan Evidence Trace Readiness Review'])
def test_v06380_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ['tools/test_v06380_controlled_executor_validation_explicit_command_plan_exposure_candidate_review_and_decision.py'])
def main() -> None:
    test_v06380_primary_files()
    test_v06380_grounded_in_v06379_candidate()
    test_v06380_runner_display()
    test_v06380_index_files()
    test_v06380_registered_in_run_all()
    print('v0.6.380 controlled executor validation explicit command plan exposure candidate review and decision checks passed')
if __name__ == '__main__':
    main()
