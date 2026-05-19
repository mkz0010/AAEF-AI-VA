# ADR-0433: Add Request/Decision Constraint Diff Check to Gateway Core Candidate

Status: proposed implementation candidate
Date: 2026-05-19
Version: v0.6.358

## Context

v0.6.357 accepted the v0.6.356 authorization expiry current-time Gateway core integration candidate. The next P0 integration item is request/decision constraint-diff enforcement.

## Decision

Add a narrow implementation candidate to the mock Gateway core so explicit request/decision constraint-map mismatches are blocked before dispatch.

## Decision record

~~~text
request_decision_constraint_diff_gateway_core_integration_candidate_created = true
request_decision_constraint_diff_gateway_core_integration_candidate_status = candidate_implemented_pending_review
request_decision_constraint_diff_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integration_scope = explicit_request_decision_constraint_map_diff_blocks_before_dispatch
request_decision_constraint_diff_helper_exists = true
request_decision_constraint_diff_helper_tested = true
request_decision_constraint_diff_mismatch_blocks_before_dispatch = true
request_decision_constraint_diff_missing_constraint_maps_legacy_path_preserved = true
authorization_expiry_current_time_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_integrated = false
controlled_executor_validation_gateway_core_integrated = false
gateway_core_behavior_changed = true
tool_gateway_behavior_changed = true
runtime_behavior_changed = false
scanner_behavior_changed = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
publication_approval = false
commercial_offer_approval = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision
request_decision_constraint_diff_gateway_core_integration_candidate_review_and_decision_recommended = true
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Request/decision constraint diff Gateway core integration candidate is not execution authorization
Request/decision constraint diff Gateway core integration candidate is not real execution permission
Request/decision constraint diff Gateway core integration candidate is not external target authorization
Request/decision constraint diff Gateway core integration candidate is not scanner readiness
Request/decision constraint diff Gateway core integration candidate is not production readiness
No private generated outputs are moved public in v0.6.358.
~~~

## Consequences

The mock Tool Gateway behavior changes for Gateway functions that receive explicit request and decision constraint maps that differ. Legacy paths without explicit constraint maps remain preserved in this candidate and should be reviewed later.

## Boundaries

- This is a mock Gateway core integration candidate.
- This does not authorize execution.
- This does not permit real execution.
- This does not authorize external targets.
- This does not approve scanner readiness.
- This does not approve publication.
- This does not approve commercial offers.
