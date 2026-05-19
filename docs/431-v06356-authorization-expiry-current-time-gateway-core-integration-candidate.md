# v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate

Status: implementation candidate checkpoint
Scope: AAEF-AI-VA Gateway core authorization expiry current-time integration
Previous checkpoint: v0.6.355 Gateway Core Safety Integration Status and Priority Review
Implementation result: candidate implemented pending review
Application status: mock Tool Gateway behavior changed for expired authorization decisions only; no runtime execution, real scanner execution, external target authorization, scanner readiness, publication approval, or commercial offer approval

## Purpose

This checkpoint creates a narrow Gateway core integration candidate for authorization expiry current-time enforcement.

The previous generated script assumed a function named `run_mock_tool_gateway()`. This fixed candidate does not assume that exact name. It locates Gateway functions in `prototypes/tool-gateway/gateway.py` whose signatures include request/decision-style parameters, then installs an authorization-expiry pre-dispatch wrapper for those functions.

No private generated outputs are moved public in v0.6.356.

## Candidate record

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

## What changed

- Added Gateway-core authorization expiry current-time integration candidate helpers to `prototypes/tool-gateway/gateway.py`.
- Installed wrappers for Gateway functions that accept request/decision-style parameters.
- Added a v0.6.356 test that verifies the integration marker, wrapper installation, direct expired-authorization block behavior, and repository checkpoint records.
- Preserved request/decision constraint-diff enforcement, external discovery fail-closed behavior, controlled executor connection, public mock/dry-run status cleanup, and gateway validation evidence modeling for later checkpoints.

## Candidate boundaries

This checkpoint changes mock Gateway core behavior for expired authorization decisions only. It does not authorize execution, permit real execution, authorize external targets, run scanners, change scanner behavior, approve public demo readiness, approve customer demo readiness, approve publication, approve commercial offers, rewrite Git history, recreate the repository, or move private generated outputs public.

The candidate is pending review. A follow-up review and decision checkpoint should confirm whether the implementation is accepted and whether missing-expiry legacy paths should later become fail-closed.

## Claim boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- publication remains deferred
- Authorization expiry current-time Gateway core integration candidate is not execution authorization
- Authorization expiry current-time Gateway core integration candidate is not real execution permission
- Authorization expiry current-time Gateway core integration candidate is not external target authorization
- Authorization expiry current-time Gateway core integration candidate is not scanner readiness
- Authorization expiry current-time Gateway core integration candidate is not production readiness

No production readiness, scanner readiness, external PoC readiness, customer PoC approval, paid engagement approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, commercial offer approval, or external-framework equivalence claim is made.

## Next checkpoint

~~~text
v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision
~~~
