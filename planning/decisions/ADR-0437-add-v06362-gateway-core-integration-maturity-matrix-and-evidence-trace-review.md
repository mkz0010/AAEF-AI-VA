# ADR-0437: Add Gateway Core Integration Maturity Matrix and Evidence Trace Review

Status: accepted
Date: 2026-05-19
Version: v0.6.362

## Context

v0.6.357, v0.6.359, and v0.6.361 accepted the current mock Gateway core candidates for authorization expiry current-time, request/decision constraint diff, and external discovery fail-closed behavior.

After those three acceptances, the next risk is external-reader confusion: helper-only controls, accepted mock Gateway core candidates, and future runtime/scanner work must be clearly separated.

## Decision

Add a Gateway core integration maturity matrix and evidence trace gap review.

## Decision record

~~~text
gateway_core_integration_maturity_matrix_review_completed = true
gateway_core_integration_maturity_matrix_review_id = gateway_core_integration_maturity_matrix_review_v06362
gateway_core_authorization_expiry_current_time_status = gateway_core_integrated_and_accepted
gateway_core_request_decision_constraint_diff_status = gateway_core_integrated_and_accepted
gateway_core_external_discovery_fail_closed_status = gateway_core_integrated_and_accepted
gateway_core_controlled_executor_validation_status = separate_helper_not_gateway_core_integrated
gateway_core_common_target_scope_tool_operation_binding_status = partial_not_common_gateway_core_integrated
gateway_core_mock_dry_run_status_terminology_status = helper_exists_public_output_cleanup_required
gateway_core_evidence_trace_status = minimal_reconstruction_trace_gateway_validation_result_modeling_required
authorization_expiry_current_time_gateway_core_integrated = true
authorization_expiry_current_time_gateway_core_candidate_accepted = true
request_decision_constraint_diff_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_candidate_accepted = true
external_discovery_fail_closed_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_candidate_accepted = true
controlled_executor_validation_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
gateway_validation_result_evidence_trace_modeling_required = true
mock_dry_run_status_terminology_public_output_cleanup_required = true
implementation_maturity_matrix_added = true
evidence_trace_gap_review_added = true
readme_front_page_simplification_still_required = true
v06362_gateway_core_behavior_changed = false
v06362_tool_gateway_behavior_changed = false
v06362_runtime_behavior_changed = false
v06362_scanner_behavior_changed = false
v06362_schema_changed = false
v06362_fixtures_created = false
v06362_actual_records_created = false
v06362_private_generated_outputs_moved_public = false
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
recommended_next_work_item = gateway_validation_result_evidence_trace_modeling_candidate
gateway_validation_result_evidence_trace_modeling_candidate_recommended = true
gateway_core_integration_maturity_matrix_and_evidence_trace_review_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Maturity matrix visibility is not production readiness.
Maturity matrix visibility is not scanner readiness.
Maturity matrix visibility is not execution authorization.
Maturity matrix visibility is not real execution permission.
Maturity matrix visibility is not external target authorization.
Maturity matrix visibility is not customer demo approval.
Maturity matrix visibility is not commercial offer approval.
No private generated outputs are moved public in v0.6.362.
~~~

## Consequences

The project now has a visible maturity distinction between accepted mock Gateway core candidates and remaining helper-only or not-yet-integrated controls.

The next recommended checkpoint is gateway validation result evidence trace modeling.

## Boundaries

- This is a visibility and review checkpoint, not production readiness.
- This is not scanner readiness.
- This is not execution authorization.
- This is not external target authorization.
- This is not commercial offer approval.
