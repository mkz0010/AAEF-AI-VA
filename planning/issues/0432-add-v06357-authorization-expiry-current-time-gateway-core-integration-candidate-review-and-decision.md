# 0432 - Add v0.6.357 Authorization Expiry Current-Time Gateway Core Integration Candidate Review and Decision

Status: completed by v0.6.357
Version: v0.6.357
Type: candidate review and decision / Gateway core safety integration

## Objective

Review the v0.6.356 authorization expiry current-time Gateway core integration candidate and decide whether to accept it for the current mock Gateway core path.

## Acceptance criteria

- `authorization_expiry_current_time_gateway_core_integration_candidate_review_completed = true` is recorded.
- `authorization_expiry_current_time_gateway_core_integration_candidate_decision = accepted_for_mock_gateway_core_path` is recorded.
- `authorization_expiry_current_time_gateway_core_integration_candidate_accepted = true` is recorded.
- `authorization_expiry_current_time_gateway_core_integrated = true` is recorded.
- `authorization_expiry_current_time_expired_decision_blocks_before_dispatch = true` is recorded.
- `normal_fixture_runner_compatibility_preserved = true` is recorded.
- `generated_output_schema_compatibility_preserved = true` is recorded.
- `tool_gateway_runner_compatibility_preserved = true` is recorded.
- `missing_expiry_legacy_path_preserved_for_now = true` is recorded.
- `request_decision_constraint_diff_gateway_core_integrated = false` is recorded.
- `external_discovery_fail_closed_gateway_core_integrated = false` is recorded.
- `controlled_executor_validation_gateway_core_integrated = false` is recorded.
- `v06357_gateway_core_behavior_changed = false` is recorded.
- `v06357_tool_gateway_behavior_changed = false` is recorded.
- `v06357_runtime_behavior_changed = false` is recorded.
- `v06357_scanner_behavior_changed = false` is recorded.
- `execution_authorized = false` is recorded.
- `real_execution_permitted = false` is recorded.
- `external_target_authorization = false` is recorded.
- `recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_implementation_candidate` is recorded.
- No runtime demo readiness, scanner readiness, production readiness, external target authorization, publication approval, public announcement, customer demo approval, commercial offer approval, legal compliance, audit opinion, certification, diagnostic completeness, or external-framework equivalence claim is made.

## Exact next-work token

~~~text
recommended_next_work_item = request_decision_constraint_diff_gateway_core_integration_implementation_candidate
~~~

## Next

Proceed to v0.6.358 Request/Decision Constraint Diff Gateway Core Integration Implementation Candidate after v0.6.357 is merged and tagged.
