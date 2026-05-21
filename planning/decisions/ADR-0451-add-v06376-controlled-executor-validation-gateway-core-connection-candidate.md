# ADR-0451: Connect Controlled Executor Validation to Gateway Core Candidate

Status: proposed
Date: 2026-05-21
Version: v0.6.376

## Decision

Add a narrow Gateway-core connection candidate that validates command-plan context before allowed mock/dry-run result generation and fails closed on explicit policy failure flags.

## Decision record

~~~text
controlled_executor_validation_gateway_core_connection_candidate_created = true
controlled_executor_validation_gateway_core_connection_candidate_status = implemented_pending_review
controlled_executor_validation_gateway_core_integrated = true
controlled_executor_validation_gateway_core_call_added = true
controlled_executor_validation_command_plan_validation_required = true
controlled_executor_validation_gate_expected_fail_closed = true
controlled_executor_validation_policy_failure_blocks_before_result_generation = true
controlled_executor_validation_external_process_executed_flag_checked = true
controlled_executor_validation_network_activity_performed_flag_checked = true
controlled_executor_validation_real_execution_mode_checked = true
controlled_executor_validation_no_real_execution_boundary_preserved = true
controlled_executor_validation_raw_result_status_compatibility_preserved = true
controlled_executor_validation_reviewer_status_compatibility_preserved = true
controlled_executor_validation_gateway_core_connection_mode = fallback_gateway_context_command_plan
controlled_executor_validation_explicit_command_plan_assignment_found = false
controlled_executor_validation_fallback_gateway_context_command_plan_used = true
authorization_expiry_current_time_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_integrated = true
common_target_scope_tool_operation_binding_gateway_core_integrated = false
v06376_gateway_core_behavior_changed = true
v06376_tool_gateway_behavior_changed = true
v06376_runtime_behavior_changed = false
v06376_scanner_behavior_changed = false
v06376_schema_changed = false
v06376_generated_outputs_changed = false
v06376_public_artifacts_changed = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = controlled_executor_validation_gateway_core_connection_candidate_review_and_decision
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Connection candidate is not production readiness.
Connection candidate is not scanner readiness.
Connection candidate is not execution authorization.
Connection candidate is not real execution permission.
Connection candidate is not external target authorization.
Connection candidate is not customer demo approval.
Connection candidate is not commercial offer approval.
No private generated outputs are moved public in v0.6.376.
v0.6.377 Controlled Executor Validation Gateway Core Connection Candidate Review and Decision
~~~
