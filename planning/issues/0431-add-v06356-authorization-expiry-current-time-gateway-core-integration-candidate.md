# 0431 - Add v0.6.356 Authorization Expiry Current-Time Gateway Core Integration Implementation Candidate

Status: completed by v0.6.356
Version: v0.6.356
Type: implementation candidate / Gateway core safety integration

## Objective

Create a narrow Gateway core integration candidate that blocks expired authorization decisions before dispatch.

## Acceptance criteria

- `authorization_expiry_current_time_gateway_core_integration_candidate_created = true` is recorded.
- `authorization_expiry_current_time_gateway_core_integration_candidate_status = candidate_implemented_pending_review` is recorded.
- `authorization_expiry_current_time_gateway_core_integrated = true` is recorded.
- `authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true` is recorded.
- `authorization_expiry_current_time_missing_expiry_legacy_path_preserved = true` is recorded.
- `request_decision_constraint_diff_gateway_core_integrated = false` is recorded.
- `external_discovery_fail_closed_gateway_core_integrated = false` is recorded.
- `controlled_executor_validation_gateway_core_integrated = false` is recorded.
- `gateway_core_behavior_changed = true` is recorded.
- `tool_gateway_behavior_changed = true` is recorded.
- `runtime_behavior_changed = false` is recorded.
- `scanner_behavior_changed = false` is recorded.
- `execution_authorized = false` is recorded.
- `real_execution_permitted = false` is recorded.
- `external_target_authorization = false` is recorded.
- `recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision` is recorded.
- No runtime demo readiness, scanner readiness, production readiness, external target authorization, publication approval, public announcement, customer demo approval, commercial offer approval, legal compliance, audit opinion, certification, diagnostic completeness, or external-framework equivalence claim is made.

## Exact next-work token

~~~text
recommended_next_work_item = authorization_expiry_current_time_gateway_core_integration_candidate_review_and_decision
~~~

## Next

Proceed to v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision after v0.6.356 is merged and tagged.
