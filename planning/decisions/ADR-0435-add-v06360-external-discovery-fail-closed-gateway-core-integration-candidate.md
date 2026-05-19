# ADR-0435: Add External Discovery Fail-Closed Check to Gateway Core Candidate

Status: proposed implementation candidate
Date: 2026-05-19
Version: v0.6.360

## Context

v0.6.359 accepted the request/decision constraint-diff Gateway core integration candidate. The next P0 integration item is external discovery fail-closed enforcement.

## Decision

Add a narrow implementation candidate to the mock Gateway core so explicit `external_discovery=true` in request-side or decision-side constraint maps is blocked before dispatch.

## Decision record

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

## Boundaries

This is a mock Gateway core integration candidate, not execution authorization, real execution permission, external target authorization, scanner readiness, publication approval, or commercial offer approval.
