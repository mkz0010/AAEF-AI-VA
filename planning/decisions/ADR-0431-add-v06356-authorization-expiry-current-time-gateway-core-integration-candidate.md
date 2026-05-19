# ADR-0431: Add Authorization Expiry Current-Time Check to Gateway Core Candidate

Status: proposed implementation candidate
Date: 2026-05-19
Version: v0.6.356

## Context

v0.6.355 recorded that Gateway core safety integration was helper-ready but core-not-integrated. The first P0 integration item is authorization expiry current-time enforcement.

The first v0.6.356 apply attempt assumed an exact function name that is not present in the current `gateway.py`, so this candidate uses function-signature discovery instead of a hard-coded function name.

## Decision

Add a narrow implementation candidate to the mock Gateway core so expired authorization decisions are blocked before dispatch when the Gateway function receives request/decision-style inputs.

## Decision record

~~~text
authorization_expiry_current_time_gateway_core_integration_candidate_created = true
authorization_expiry_current_time_gateway_core_integration_candidate_id = authorization_expiry_current_time_gateway_core_integration_candidate_v06356
authorization_expiry_current_time_gateway_core_integration_candidate_status = candidate_implemented_pending_review
authorization_expiry_current_time_gateway_core_integrated = true
authorization_expiry_current_time_gateway_core_integration_scope = expired_authorization_blocks_before_dispatch
authorization_expiry_current_time_helper_exists = true
authorization_expiry_current_time_helper_tested = true
authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true
authorization_expiry_current_time_missing_expiry_legacy_path_preserved = true
request_decision_constraint_diff_gateway_core_integrated = false
external_discovery_fail_closed_gateway_core_integrated = false
controlled_executor_validation_gateway_core_integrated = false
gateway_core_behavior_changed = true
tool_gateway_behavior_changed = true
runtime_behavior_changed = false
scanner_behavior_changed = false
schema_changed = false
fixtures_created = false
private_generated_outputs_moved_public = false
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
recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision
authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision_recommended = true
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Authorization expiry current-time Gateway core integration candidate is not execution authorization
Authorization expiry current-time Gateway core integration candidate is not real execution permission
Authorization expiry current-time Gateway core integration candidate is not external target authorization
Authorization expiry current-time Gateway core integration candidate is not scanner readiness
Authorization expiry current-time Gateway core integration candidate is not production readiness
No private generated outputs are moved public in v0.6.356.
~~~

## Consequences

The mock Tool Gateway behavior changes for explicitly expired authorization decisions on wrapped request/decision Gateway functions. Legacy paths without expiry timestamps remain preserved in this candidate and should be reviewed in a follow-up checkpoint.

## Boundaries

- This is a mock Gateway core integration candidate.
- This does not authorize execution.
- This does not permit real execution.
- This does not authorize external targets.
- This does not approve scanner readiness.
- This does not approve publication.
- This does not approve commercial offers.
