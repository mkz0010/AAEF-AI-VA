# ADR-0432: Accept Authorization Expiry Current-Time Gateway Core Integration Candidate

Status: accepted
Date: 2026-05-19
Version: v0.6.357

## Context

v0.6.356 introduced a narrow authorization expiry current-time Gateway core integration candidate. It added pre-dispatch blocking behavior for expired authorization decisions while preserving normal fixture runner compatibility and generated output validation.

The candidate required legacy planning-test scope adjustments because older planning-only tests scanned rolling aggregate files for tokens that later checkpoints may legitimately contain.

## Decision

Accept the v0.6.356 authorization expiry current-time Gateway core integration candidate for the current mock Gateway core path.

## Decision record

~~~text
authorization_expiry_current_time_gateway_core_integration_candidate_review_completed = true
authorization_expiry_current_time_gateway_core_integration_candidate_review_id = authorization_expiry_current_time_gateway_core_integration_candidate_review_v06357
authorization_expiry_current_time_gateway_core_integration_candidate_decision = accepted_for_mock_gateway_core_path
authorization_expiry_current_time_gateway_core_integration_candidate_accepted = true
authorization_expiry_current_time_gateway_core_integration_candidate_status = accepted_pending_follow_on_controls
authorization_expiry_current_time_gateway_core_integrated = true
authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true
normal_fixture_runner_compatibility_preserved = true
generated_output_schema_compatibility_preserved = true
tool_gateway_runner_compatibility_preserved = true
run_tool_gateway_example_all_passed_before_v06356_commit = true
validate_generated_outputs_passed_before_v06356_commit = true
all_local_checks_passed_before_v06356_commit = true
missing_expiry_legacy_path_preserved_for_now = true
missing_expiry_fail_closed_not_yet_required = true
authorization_expiry_current_time_gateway_core_integration_follow_on_review_required = false
request_decision_constraint_diff_gateway_core_integrated = false
external_discovery_fail_closed_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
controlled_executor_validation_gateway_core_integrated = false
mock_dry_run_status_terminology_public_output_cleanup_required = true
evidence_gateway_validation_result_modeling_required = true
implementation_maturity_matrix_required = true
readme_front_page_simplification_still_required = true
legacy_planning_test_scope_adjustment_accepted = true
legacy_planning_test_scope_adjustment_reason = rolling_aggregate_files_can_contain_later_checkpoint_tokens
v06357_gateway_core_behavior_changed = false
v06357_tool_gateway_behavior_changed = false
v06357_runtime_behavior_changed = false
v06357_scanner_behavior_changed = false
v06357_schema_changed = false
v06357_fixtures_created = false
v06357_actual_records_created = false
v06357_private_generated_outputs_moved_public = false
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
recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_implementation_candidate
request_decision_constraint_diff_gateway_core_integration_implementation_candidate_recommended = true
authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision_recommended = false
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
No private generated outputs are moved public in v0.6.357.
~~~

## Consequences

The project can keep the v0.6.356 candidate and proceed to the next P0 integration item: request/decision constraint-diff Gateway core integration.

This acceptance remains scoped to the mock Gateway core path and does not imply runtime demo readiness, scanner readiness, production readiness, customer demo approval, execution authorization, real execution permission, external target authorization, publication approval, or commercial offer approval.

## Boundaries

- This is candidate acceptance, not production readiness.
- This is candidate acceptance, not scanner readiness.
- This is candidate acceptance, not execution authorization.
- This is candidate acceptance, not external target authorization.
- This is candidate acceptance, not commercial offer approval.
