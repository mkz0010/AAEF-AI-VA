# ADR-0438: Define Gateway Validation Result Evidence Trace Modeling Candidate

Status: proposed modeling candidate
Date: 2026-05-19
Version: v0.6.363

## Context

v0.6.362 documented that the current mock Gateway core path has accepted candidates for authorization expiry current-time, request/decision constraint diff, and external discovery fail-closed.

The remaining evidence gap is that these Gateway validation outcomes are not yet represented as a structured reviewer-facing evidence trace field.

## Decision

Define a candidate Gateway validation result evidence trace model without applying it to schemas, generated outputs, runtime behavior, or public artifacts.

## Decision record

~~~text
gateway_validation_result_evidence_trace_modeling_candidate_created = true
gateway_validation_result_evidence_trace_modeling_candidate_id = gateway_validation_result_evidence_trace_modeling_candidate_v06363
gateway_validation_result_evidence_trace_modeling_candidate_status = candidate_defined_pending_review
gateway_validation_result_evidence_trace_model_defined = true
gateway_validation_result_evidence_trace_model_runtime_applied = false
gateway_validation_result_evidence_record_schema_changed = false
gateway_validation_result_generated_outputs_changed = false
gateway_validation_result_existing_generated_output_compatibility_preserved = true
gateway_validation_result_model_scope = reviewer_facing_gateway_validation_trace_field_candidate
gateway_validation_result_model_gate_set_includes_authorization_expiry_current_time = true
gateway_validation_result_model_gate_set_includes_request_decision_constraint_diff = true
gateway_validation_result_model_gate_set_includes_external_discovery_fail_closed = true
gateway_validation_result_model_gate_set_includes_non_dispatch_legacy_path_preservation = true
gateway_validation_result_model_gate_set_includes_existing_policy_error_path_preservation = true
gateway_validation_result_model_external_process_executed_field_required = true
gateway_validation_result_model_network_activity_performed_field_required = true
gateway_validation_result_model_limitations_field_required = true
gateway_validation_result_model_producer_identity_future_work = true
gateway_validation_result_model_hash_or_signature_future_work = true
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
v06363_gateway_core_behavior_changed = false
v06363_tool_gateway_behavior_changed = false
v06363_runtime_behavior_changed = false
v06363_scanner_behavior_changed = false
v06363_schema_changed = false
v06363_fixtures_created = false
v06363_actual_records_created = false
v06363_private_generated_outputs_moved_public = false
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
recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision
gateway_validation_result_evidence_trace_modeling_candidate_review_and_decision_recommended = true
gateway_validation_result_evidence_trace_modeling_candidate_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Gateway validation result evidence trace modeling is not production readiness.
Gateway validation result evidence trace modeling is not scanner readiness.
Gateway validation result evidence trace modeling is not execution authorization.
Gateway validation result evidence trace modeling is not real execution permission.
Gateway validation result evidence trace modeling is not external target authorization.
Gateway validation result evidence trace modeling is not customer demo approval.
Gateway validation result evidence trace modeling is not commercial offer approval.
No private generated outputs are moved public in v0.6.363.
~~~

## Consequences

The project can review the model before deciding whether to apply it to evidence-record schemas, generated outputs, or reviewer-facing artifacts.

This preserves current generated-output compatibility while making the evidence trace direction explicit.

## Boundaries

- This is model definition only, not production readiness.
- This is not scanner readiness.
- This is not execution authorization.
- This is not external target authorization.
- This is not commercial offer approval.
