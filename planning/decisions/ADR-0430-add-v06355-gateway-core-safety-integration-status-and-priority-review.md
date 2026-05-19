# ADR-0430: Prioritize Gateway Core Safety Integration

Status: accepted
Date: 2026-05-19
Version: v0.6.355

## Context

Emergency public-tree cleanup and public history exposure review are complete for the current tree. External review still identifies Gateway core safety integration as the primary technical risk.

Helper controls exist for authorization expiry current-time checking, request/decision constraint diff, external discovery fail-closed behavior, and mock/dry-run status terminology. However, the Gateway core execution path does not yet integrate the most important helper controls.

## Decision

Prioritize Gateway core safety integration as P0 work, beginning with a narrow authorization expiry current-time Gateway core integration implementation candidate.

## Decision record

~~~text
gateway_core_safety_integration_status_and_priority_review_completed = true
gateway_core_safety_integration_status = helper_ready_core_not_integrated
gateway_core_safety_integration_priority = p0
gateway_core_currently_enforces_request_decision_binding = true
gateway_core_currently_enforces_credential_ref_metadata_check = true
authorization_expiry_current_time_helper_exists = true
authorization_expiry_current_time_helper_tested = true
authorization_expiry_current_time_gateway_core_integrated = false
request_decision_constraint_diff_helper_exists = true
request_decision_constraint_diff_helper_tested = true
request_decision_constraint_diff_gateway_core_integrated = false
external_discovery_fail_closed_helper_exists = true
external_discovery_fail_closed_helper_tested = true
external_discovery_fail_closed_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
controlled_executor_validation_gateway_core_integrated = false
mock_dry_run_status_terminology_public_output_cleanup_required = true
evidence_gateway_validation_result_modeling_required = true
implementation_maturity_matrix_required = true
readme_front_page_simplification_still_required = true
p0_sequence_1 = authorization_expiry_current_time_gateway_core_integration
p0_sequence_2 = request_decision_constraint_diff_gateway_core_integration
p0_sequence_3 = external_discovery_fail_closed_gateway_core_integration
p0_sequence_4 = controlled_executor_validation_gateway_core_connection
p0_sequence_5 = public_mock_dry_run_status_cleanup
p0_sequence_6 = gateway_validation_evidence_trace_modeling
history_rewrite_performed = false
repo_recreated = false
git_history_exposure_may_remain = true
commercial_offer_approval = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
safe_local_only_demo_execution_boundary_runtime_applied = false
minimal_runtime_wiring_changed = false
tool_gateway_behavior_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
gateway_core_behavior_changed = false
gateway_core_integration_implemented = false
runtime_enforcement_implemented = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_implementation_candidate
authorization_expiry_current_time_gateway_core_integration_implementation_candidate_recommended = true
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Gateway core status review is not Gateway core integration
Gateway core status review is not runtime wiring
Gateway core status review is not runtime application
Gateway core status review is not execution authorization
Gateway core status review is not real execution permission
Gateway core status review is not external target authorization
Gateway core status review is not scanner readiness
Gateway core status review is not production readiness
No private generated outputs are moved public in v0.6.355.
~~~

## Consequences

The project should move from status review to a narrow implementation candidate. This ADR does not itself change Gateway core behavior, authorize execution, permit real execution, or approve external targets.

## Boundaries

- This is a priority review only.
- This does not change Gateway core behavior.
- This does not change runtime wiring.
- This does not approve execution.
- This does not approve publication.
- This does not approve commercial offers.
