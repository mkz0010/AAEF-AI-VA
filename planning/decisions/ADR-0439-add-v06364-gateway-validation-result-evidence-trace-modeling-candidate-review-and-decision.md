# ADR-0439: Accept Gateway Validation Result Evidence Trace Modeling Candidate

Status: accepted
Date: 2026-05-19
Version: v0.6.364

## Context

v0.6.363 defined a reviewer-facing candidate model for representing Gateway validation results in evidence traces while preserving existing generated output compatibility.

The project needs to decide whether to accept that model as the evidence-trace direction before applying it to schemas, generated outputs, runtime records, or reviewer artifacts.

## Decision

Accept the v0.6.363 Gateway validation result evidence trace model as the reviewer-facing evidence trace direction.

Application to schemas, generated outputs, runtime behavior, and public artifacts is deferred to a follow-up application-planning checkpoint.

## Decision record

~~~text
gateway_validation_result_evidence_trace_modeling_candidate_review_completed = true
gateway_validation_result_evidence_trace_modeling_candidate_review_id = gateway_validation_result_evidence_trace_modeling_candidate_review_v06364
gateway_validation_result_evidence_trace_modeling_candidate_decision = accepted_for_reviewer_facing_evidence_trace_direction
gateway_validation_result_evidence_trace_modeling_candidate_accepted = true
gateway_validation_result_evidence_trace_modeling_candidate_status = accepted_pending_application_planning
gateway_validation_result_evidence_trace_model_defined = true
gateway_validation_result_evidence_trace_model_runtime_applied = false
gateway_validation_result_evidence_record_schema_changed = false
gateway_validation_result_generated_outputs_changed = false
gateway_validation_result_existing_generated_output_compatibility_preserved = true
gateway_validation_result_model_scope = reviewer_facing_gateway_validation_trace_field_direction
gateway_validation_result_model_gate_set_includes_authorization_expiry_current_time = true
gateway_validation_result_model_gate_set_includes_request_decision_constraint_diff = true
gateway_validation_result_model_gate_set_includes_external_discovery_fail_closed = true
gateway_validation_result_model_gate_set_includes_non_dispatch_legacy_path_preservation = true
gateway_validation_result_model_gate_set_includes_existing_policy_error_path_preservation = true
gateway_validation_result_model_external_process_executed_field_required = true
gateway_validation_result_model_network_activity_performed_field_required = true
gateway_validation_result_model_limitations_field_required = true
gateway_validation_result_model_raw_and_reviewer_facing_status_separation_required = true
gateway_validation_result_model_schema_application_deferred = true
gateway_validation_result_model_generated_output_application_deferred = true
gateway_validation_result_model_runtime_application_deferred = true
gateway_validation_result_model_producer_identity_deferred = true
gateway_validation_result_model_hash_or_signature_deferred = true
authorization_expiry_current_time_gateway_core_integrated = true
authorization_expiry_current_time_gateway_core_candidate_accepted = true
request_decision_constraint_diff_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_candidate_accepted = true
external_discovery_fail_closed_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_candidate_accepted = true
controlled_executor_validation_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
mock_dry_run_status_terminology_public_output_cleanup_required = true
implementation_maturity_matrix_available = true
readme_front_page_simplification_still_required = true
v06364_gateway_core_behavior_changed = false
v06364_tool_gateway_behavior_changed = false
v06364_runtime_behavior_changed = false
v06364_scanner_behavior_changed = false
v06364_schema_changed = false
v06364_fixtures_created = false
v06364_actual_records_created = false
v06364_private_generated_outputs_moved_public = false
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
recommended_next_work_item = gateway_validation_result_evidence_trace_application_planning_candidate
gateway_validation_result_evidence_trace_application_planning_candidate_recommended = true
gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision_recommended = false
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
No private generated outputs are moved public in v0.6.364.
~~~

## Consequences

The project can now plan staged application of the Gateway validation result evidence trace model while preserving compatibility and claim boundaries.

## Boundaries

- This is candidate acceptance, not schema application.
- This is candidate acceptance, not generated-output application.
- This is candidate acceptance, not production readiness.
- This is candidate acceptance, not scanner readiness.
- This is candidate acceptance, not execution authorization.
- This is candidate acceptance, not external target authorization.
- This is candidate acceptance, not commercial offer approval.
