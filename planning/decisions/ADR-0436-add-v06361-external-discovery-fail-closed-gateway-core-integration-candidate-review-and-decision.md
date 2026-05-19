# ADR-0436: Accept External Discovery Fail-Closed Gateway Core Integration Candidate

Status: accepted
Date: 2026-05-19
Version: v0.6.361

## Context

v0.6.360 introduced a narrow external discovery fail-closed Gateway core integration candidate. It added pre-dispatch blocking behavior for explicit `external_discovery=true` on dispatch-authorized paths while preserving normal fixture runner compatibility, generated output validation, existing non-dispatch decision paths, and existing destructive-tests PolicyError behavior.

## Decision

Accept the v0.6.360 external discovery fail-closed Gateway core integration candidate for the current mock Gateway core path.

## Decision record

~~~text
external_discovery_fail_closed_gateway_core_integration_candidate_review_completed = true
external_discovery_fail_closed_gateway_core_integration_candidate_review_id = external_discovery_fail_closed_gateway_core_integration_candidate_review_v06361
external_discovery_fail_closed_gateway_core_integration_candidate_decision = accepted_for_mock_gateway_core_path
external_discovery_fail_closed_gateway_core_integration_candidate_accepted = true
external_discovery_fail_closed_gateway_core_integration_candidate_status = accepted_pending_follow_on_controls
external_discovery_fail_closed_gateway_core_integrated = true
external_discovery_true_blocks_before_dispatch = true
external_discovery_false_allows_continue = true
external_discovery_missing_legacy_path_preserved_for_now = true
non_dispatch_decision_legacy_paths_preserved = true
destructive_tests_policy_error_path_preserved = true
normal_fixture_runner_compatibility_preserved = true
generated_output_schema_compatibility_preserved = true
tool_gateway_runner_compatibility_preserved = true
run_tool_gateway_example_all_passed_before_v06360_commit = true
validate_generated_outputs_passed_before_v06360_commit = true
test_tool_gateway_runner_passed_before_v06360_commit = true
all_local_checks_passed_before_v06360_commit = true
authorization_expiry_current_time_gateway_core_integrated = true
authorization_expiry_current_time_gateway_core_candidate_accepted = true
request_decision_constraint_diff_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_candidate_accepted = true
common_target_scope_tool_operation_binding_gateway_core_integrated = false
controlled_executor_validation_gateway_core_integrated = false
mock_dry_run_status_terminology_public_output_cleanup_required = true
evidence_gateway_validation_result_modeling_required = true
implementation_maturity_matrix_required = true
readme_front_page_simplification_still_required = true
v06361_gateway_core_behavior_changed = false
v06361_tool_gateway_behavior_changed = false
v06361_runtime_behavior_changed = false
v06361_scanner_behavior_changed = false
v06361_schema_changed = false
v06361_fixtures_created = false
v06361_actual_records_created = false
v06361_private_generated_outputs_moved_public = false
history_rewrite_performed = false
repo_recreated = false
commercial_offer_approval = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
safe_local_only_demo_execution_boundary_runtime_applied = false
minimal_runtime_wiring_changed = false
runtime_enforcement_implemented = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = gateway_core_integration_maturity_matrix_and_evidence_trace_review
gateway_core_integration_maturity_matrix_and_evidence_trace_review_recommended = true
external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Candidate acceptance is not production readiness.
Candidate acceptance is not scanner readiness.
Candidate acceptance is not execution authorization.
Candidate acceptance is not real execution permission.
Candidate acceptance is not external target authorization.
Candidate acceptance is not customer demo approval.
Candidate acceptance is not commercial offer approval.
No private generated outputs are moved public in v0.6.361.
~~~

## Consequences

The project can keep the v0.6.360 candidate and proceed to a visibility/evidence checkpoint covering Gateway-core integration maturity and evidence trace modeling.

This acceptance remains scoped to the mock Gateway core path and does not imply runtime demo readiness, scanner readiness, production readiness, customer demo approval, execution authorization, real execution permission, external target authorization, publication approval, or commercial offer approval.

## Boundaries

- This is candidate acceptance, not production readiness.
- This is candidate acceptance, not scanner readiness.
- This is candidate acceptance, not execution authorization.
- This is candidate acceptance, not external target authorization.
- This is candidate acceptance, not commercial offer approval.
