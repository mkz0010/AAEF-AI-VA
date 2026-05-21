# ADR-0452: Accept Controlled Executor Validation Gateway Core Connection Candidate with Fallback Mode

Status: accepted
Date: 2026-05-21
Version: v0.6.377

## Decision

Accept the v0.6.376 controlled executor validation Gateway-core connection candidate with fallback mode and make explicit command plan exposure the next review target.

## Decision record

~~~text
controlled_executor_validation_gateway_core_connection_candidate_review_completed = true
controlled_executor_validation_gateway_core_connection_candidate_decision = accepted_with_fallback_mode
controlled_executor_validation_gateway_core_connection_candidate_accepted = true
controlled_executor_validation_gateway_core_connection_candidate_status = accepted_pending_explicit_command_plan_exposure_review
controlled_executor_validation_gateway_core_integrated = true
controlled_executor_validation_gateway_core_call_present = true
controlled_executor_validation_gateway_core_connection_mode = fallback_gateway_context_command_plan
controlled_executor_validation_explicit_command_plan_assignment_found = false
controlled_executor_validation_fallback_gateway_context_command_plan_used = true
controlled_executor_validation_fallback_gateway_context_command_plan_accepted = true
controlled_executor_validation_fallback_mode_limitation_recorded = true
controlled_executor_validation_explicit_command_plan_exposure_next_priority = true
controlled_executor_validation_gate_expected_fail_closed = true
controlled_executor_validation_policy_failure_blocks_before_result_generation = true
controlled_executor_validation_no_real_execution_boundary_preserved = true
authorization_expiry_current_time_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_integrated = true
common_target_scope_tool_operation_binding_gateway_core_integrated = false
v06377_gateway_core_behavior_changed = false
v06377_tool_gateway_behavior_changed = false
v06377_runtime_behavior_changed = false
v06377_scanner_behavior_changed = false
v06377_schema_changed = false
v06377_generated_outputs_changed = false
v06377_public_artifacts_changed = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = controlled_executor_validation_explicit_command_plan_exposure_readiness_review
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
No private generated outputs are moved public in v0.6.377.
v0.6.378 Controlled Executor Validation Explicit Command Plan Exposure Readiness Review
~~~

## Boundaries

This review does not change schemas, generated output schema, Gateway core behavior, runtime behavior, scanner behavior, public artifact behavior, execution authorization, external target authorization, production readiness, scanner readiness, or commercial offer approval.
