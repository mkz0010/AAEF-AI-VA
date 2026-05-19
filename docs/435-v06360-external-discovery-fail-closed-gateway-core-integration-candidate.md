# v0.6.360 External Discovery Fail-Closed Gateway Core Integration Implementation Candidate

Status: implementation candidate checkpoint
Scope: AAEF-AI-VA Gateway core external discovery fail-closed integration
Previous checkpoint: v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision
Implementation result: candidate implemented pending review

## Purpose

This checkpoint creates a narrow Gateway core integration candidate for external discovery fail-closed enforcement.

The candidate adds a pre-dispatch check to the mock Gateway core path so that explicit `external_discovery=true` in request-side or decision-side constraint maps blocks before dispatch. Existing denied, blocked, human-approval, and destructive-tests PolicyError paths are preserved so existing schema-compatible outputs and fail-closed tests remain intact.

No private generated outputs are moved public in v0.6.360.

## Candidate record

~~~text
external_discovery_fail_closed_gateway_core_integration_candidate_created = true
external_discovery_fail_closed_gateway_core_integration_candidate_status = candidate_implemented_pending_review
external_discovery_fail_closed_gateway_core_integrated = true
external_discovery_true_blocks_before_dispatch = true
external_discovery_false_allows_continue = true
external_discovery_missing_legacy_path_preserved = true
non_dispatch_decision_legacy_paths_preserved = true
destructive_tests_policy_error_path_preserved = true
authorization_expiry_current_time_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integrated = true
controlled_executor_validation_gateway_core_integrated = false
gateway_core_behavior_changed = true
tool_gateway_behavior_changed = true
runtime_behavior_changed = false
scanner_behavior_changed = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
recommended_next_work_item = external_discovery_fail_closed_gateway_core_integration_candidate_review_and_decision
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
External discovery fail-closed Gateway core integration candidate is not execution authorization
External discovery fail-closed Gateway core integration candidate is not real execution permission
External discovery fail-closed Gateway core integration candidate is not external target authorization
External discovery fail-closed Gateway core integration candidate is not scanner readiness
External discovery fail-closed Gateway core integration candidate is not production readiness
No private generated outputs are moved public in v0.6.360.
v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision
~~~

## Decision boundary

This checkpoint changes mock Gateway core behavior for explicit `external_discovery=true` on dispatch-authorized request/decision paths only. It does not authorize execution, permit real execution, authorize external targets, approve scanner readiness, approve publication, or approve commercial offers.

## Claim boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- External discovery fail-closed Gateway core integration candidate is not execution authorization.
- External discovery fail-closed Gateway core integration candidate is not real execution permission.
- External discovery fail-closed Gateway core integration candidate is not external target authorization.
- External discovery fail-closed Gateway core integration candidate is not scanner readiness.
- External discovery fail-closed Gateway core integration candidate is not production readiness.

## Next checkpoint

~~~text
v0.6.361 External Discovery Fail-Closed Gateway Core Integration Candidate Review and Decision
~~~
