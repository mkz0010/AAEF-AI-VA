# v0.6.358 Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate

Status: implementation candidate checkpoint
Scope: AAEF-AI-VA Gateway core request/decision constraint-diff integration
Previous checkpoint: v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision
Implementation result: candidate implemented pending review
Application status: mock Tool Gateway behavior changed for explicit request/decision constraint-map mismatches only; no runtime execution, real scanner execution, external target authorization, scanner readiness, publication approval, or commercial offer approval

## Purpose

This checkpoint creates a narrow Gateway core integration candidate for request/decision constraint-diff enforcement.

The candidate adds a pre-dispatch check to the mock Gateway core path so that explicit request-side constraints and explicit decision-side constraints are compared before dispatch. If both sides provide constraint maps and the maps differ, the action is blocked before dispatch.

The candidate preserves legacy paths where explicit constraint maps are missing from one or both sides.

No private generated outputs are moved public in v0.6.358.

## Candidate record

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

## What changed

- Added Gateway-core request/decision constraint-diff integration candidate helpers to `prototypes/tool-gateway/gateway.py`.
- Installed wrappers for Gateway functions that accept request/decision-style parameters.
- Added a v0.6.358 test for direct mismatch block behavior, missing-map legacy preservation, wrapper installation, and repository checkpoint records.
- Preserved authorization expiry current-time Gateway core integration from v0.6.356/v0.6.357.
- Left external discovery fail-closed behavior, controlled executor connection, public mock/dry-run status cleanup, and gateway validation evidence modeling for follow-up checkpoints.

## Candidate boundaries

This checkpoint changes mock Gateway core behavior for explicit request/decision constraint-map mismatches only. It does not authorize execution, permit real execution, authorize external targets, run scanners, change scanner behavior, approve public demo readiness, approve customer demo readiness, approve publication, approve commercial offers, rewrite Git history, recreate the repository, or move private generated outputs public.

## Claim boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- publication remains deferred
- Request/decision constraint diff Gateway core integration candidate is not execution authorization
- Request/decision constraint diff Gateway core integration candidate is not real execution permission
- Request/decision constraint diff Gateway core integration candidate is not external target authorization
- Request/decision constraint diff Gateway core integration candidate is not scanner readiness
- Request/decision constraint diff Gateway core integration candidate is not production readiness

No production readiness, scanner readiness, external PoC readiness, customer PoC approval, paid engagement approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostically complete claim, automated risk acceptance, commercial offer approval, or external-framework equivalence claim is made.

## Next checkpoint

~~~text
v0.6.359 Request/Decision Constraint Diff Gateway Core Integration Candidate Review and Decision
~~~
