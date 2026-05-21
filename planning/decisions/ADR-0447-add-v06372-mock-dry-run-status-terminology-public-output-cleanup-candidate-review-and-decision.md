# ADR-0447: Accept Mock/Dry-Run Status Terminology Public Output Cleanup Candidate

Status: accepted
Date: 2026-05-21
Version: v0.6.372

## Context

v0.6.371 implemented a display cleanup candidate that preserves raw `completed` compatibility while removing public/runner-facing bare `allowed-action: completed` display for allowed mock/dry-run actions.

## Decision

Accept the v0.6.371 display cleanup candidate and proceed to closeout review.

## Decision record

~~~text
mock_dry_run_status_terminology_public_output_cleanup_candidate_review_completed = true
mock_dry_run_status_terminology_public_output_cleanup_candidate_decision = accepted
mock_dry_run_status_terminology_public_output_cleanup_candidate_accepted = true
mock_dry_run_status_terminology_public_output_cleanup_candidate_status = accepted_pending_closeout_review
mock_dry_run_status_terminology_public_output_cleanup_runner_console_output_reviewed = true
mock_dry_run_status_terminology_public_output_cleanup_public_artifact_status_lines_reviewed = true
mock_dry_run_status_terminology_public_output_cleanup_readme_status_wording_reviewed = true
mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true
mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true
mock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_accepted = true
mock_dry_run_status_terminology_public_output_cleanup_external_process_executed_display_accepted = true
mock_dry_run_status_terminology_public_output_cleanup_network_activity_performed_display_accepted = true
mock_dry_run_status_terminology_public_output_cleanup_schema_change_now = false
mock_dry_run_status_terminology_public_output_cleanup_generated_output_schema_change_now = false
mock_dry_run_status_terminology_public_output_cleanup_runtime_behavior_change_now = false
mock_dry_run_status_terminology_public_output_cleanup_gateway_core_behavior_change_now = false
mock_dry_run_status_terminology_public_output_cleanup_raw_result_json_status_changed = false
authorization_expiry_current_time_gateway_core_integrated = true
request_decision_constraint_diff_gateway_core_integrated = true
external_discovery_fail_closed_gateway_core_integrated = true
controlled_executor_validation_gateway_core_integrated = false
common_target_scope_tool_operation_binding_gateway_core_integrated = false
v06372_gateway_core_behavior_changed = false
v06372_tool_gateway_behavior_changed = false
v06372_runtime_behavior_changed = false
v06372_scanner_behavior_changed = false
v06372_schema_changed = false
v06372_generated_outputs_changed = false
v06372_public_artifacts_changed = false
v06372_private_generated_outputs_moved_public = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_closeout_review
mock_dry_run_status_terminology_public_output_cleanup_closeout_review_recommended = true
mock_dry_run_status_terminology_public_output_cleanup_candidate_review_and_decision_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Candidate acceptance is not production readiness.
Candidate acceptance is not scanner readiness.
Candidate acceptance is not execution authorization.
Candidate acceptance is not real execution permission.
Candidate acceptance is not external target authorization.
Candidate acceptance is not customer demo approval.
Candidate acceptance is not commercial offer approval.
No private generated outputs are moved public in v0.6.372.
v0.6.373 Mock/Dry-Run Status Terminology Public Output Cleanup Closeout Review
~~~

## Consequences

Runner and public-facing status display now use raw/reviewer separation for allowed mock/dry-run actions, while raw result JSON and schema expectations remain compatible.

## Boundaries

This review does not change schemas, generated output schema, Gateway core behavior, runtime behavior, scanner behavior, execution authorization, external target authorization, production readiness, scanner readiness, or commercial offer approval.
