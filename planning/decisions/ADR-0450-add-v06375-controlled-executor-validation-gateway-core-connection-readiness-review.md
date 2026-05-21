# ADR-0450: Prepare Controlled Executor Validation Gateway Core Connection

Status: accepted
Date: 2026-05-21
Version: v0.6.375

## Context

The Gateway core path now integrates authorization expiry current-time checks, request/decision constraint-diff checks, and external discovery fail-closed checks. Controlled executor policy exists separately but is not yet connected into the Gateway core path.

## Decision

Define readiness for a controlled executor validation Gateway-core connection candidate. The candidate should validate command plans after construction and before result/evidence generation, fail closed on policy failure, and preserve no-real-execution boundaries.

## Decision record

~~~text
controlled_executor_validation_gateway_core_connection_readiness_review_completed = true
controlled_executor_validation_gateway_core_connection_scope_defined = true
controlled_executor_validation_gateway_core_connection_ready_for_candidate = true
controlled_executor_validation_gateway_core_connection_candidate_recommended = true
controlled_executor_policy_available = true
controlled_executor_policy_tests_available = true
controlled_executor_policy_tests_pass_required = true
controlled_executor_validation_current_gateway_core_integrated = false
controlled_executor_validation_gateway_core_target_position = after_command_plan_build_before_result_and_evidence_generation
controlled_executor_validation_gateway_core_candidate_should_be_display_and_evidence_safe = true
controlled_executor_validation_command_plan_validation_required = true
controlled_executor_validation_gate_expected_fail_closed = true
controlled_executor_validation_blocked_result_required_on_policy_failure = true
controlled_executor_validation_external_process_executed_flag_required = true
controlled_executor_validation_network_activity_performed_flag_required = true
controlled_executor_validation_no_real_execution_boundary_required = true
controlled_executor_validation_raw_result_status_compatibility_required = true
controlled_executor_validation_reviewer_status_compatibility_required = true
controlled_executor_validation_gateway_validation_result_evidence_trace_future_candidate = true
authorization_expiry_current_time_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_integrated = true
controlled_executor_validation_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integration_deferred = true
readme_front_page_simplification_still_required = true
v06375_gateway_core_behavior_changed = false
v06375_tool_gateway_behavior_changed = false
v06375_runtime_behavior_changed = false
v06375_scanner_behavior_changed = false
v06375_schema_changed = false
v06375_generated_outputs_changed = false
v06375_public_artifacts_changed = false
v06375_private_generated_outputs_moved_public = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate
controlled_executor_validation_gateway_core_connection_readiness_review_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Readiness review is not production readiness.
Readiness review is not scanner readiness.
Readiness review is not execution authorization.
Readiness review is not real execution permission.
Readiness review is not external target authorization.
Readiness review is not customer demo approval.
Readiness review is not commercial offer approval.
No private generated outputs are moved public in v0.6.375.
v0.6.376 Controlled Executor Validation Gateway Core Connection Candidate
~~~

## Consequences

The next checkpoint can implement a narrow Gateway-core connection candidate for controlled executor validation without authorizing real execution or changing schema behavior in this readiness review.

## Boundaries

This readiness review does not change schemas, generated output schema, Gateway core behavior, runtime behavior, scanner behavior, public artifact behavior, execution authorization, external target authorization, production readiness, scanner readiness, or commercial offer approval.
