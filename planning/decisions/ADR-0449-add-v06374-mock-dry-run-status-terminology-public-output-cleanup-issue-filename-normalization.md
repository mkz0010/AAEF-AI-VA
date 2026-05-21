# ADR-0449: Normalize Mock/Dry-Run Status Terminology Cleanup Issue Filename

Status: accepted
Date: 2026-05-21
Version: v0.6.374

## Context

v0.6.373 closed the mock/dry-run status terminology public-output cleanup track. The committed planning issue filename used `cleanout` instead of `cleanup`.

## Decision

Rename the v0.6.373 planning issue file from `cleanout` to `cleanup` and proceed to controlled executor validation Gateway-core connection readiness review.

## Decision record

~~~text
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_completed = true
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_scope = filename_only
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_old_path = planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanout-review.md
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_new_path = planning/issues/0448-add-v06373-mock-dry-run-status-terminology-public-output-cleanup-review.md
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_cleanout_removed_from_current_tree = true
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_cleanup_present_in_current_tree = true
mock_dry_run_status_terminology_public_output_cleanup_track_already_closed = true
mock_dry_run_status_terminology_public_output_cleanup_status = closed_as_display_cleanup
mock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true
mock_dry_run_status_terminology_public_output_cleanup_public_display_bare_completed_removed = true
controlled_executor_validation_gateway_core_connection_next_priority = true
v06374_gateway_core_behavior_changed = false
v06374_tool_gateway_behavior_changed = false
v06374_runtime_behavior_changed = false
v06374_scanner_behavior_changed = false
v06374_schema_changed = false
v06374_generated_outputs_changed = false
v06374_public_artifacts_changed = false
v06374_private_generated_outputs_moved_public = false
publication_approval = false
public_announcement = deferred
customer_demo_approval = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
recommended_next_work_item = controlled_executor_validation_gateway_core_connection_readiness_review
controlled_executor_validation_gateway_core_connection_readiness_review_recommended = true
mock_dry_run_status_terminology_public_output_cleanup_issue_filename_normalization_recommended = false
Model output is not authority.
AI rationale is not authorization.
A gate decision is not AI self-approval.
Evidence supports reconstruction; it does not prove legal truth.
validator success is structural only
publication remains deferred
Filename normalization is not production readiness.
Filename normalization is not scanner readiness.
Filename normalization is not execution authorization.
Filename normalization is not real execution permission.
Filename normalization is not external target authorization.
Filename normalization is not customer demo approval.
Filename normalization is not commercial offer approval.
No private generated outputs are moved public in v0.6.374.
v0.6.375 Controlled Executor Validation Gateway Core Connection Readiness Review
~~~

## Consequences

The current public tree has consistent cleanup terminology for the v0.6.373 issue file.

## Boundaries

This filename normalization does not change schemas, generated output schema, Gateway core behavior, runtime behavior, scanner behavior, public artifact behavior, execution authorization, external target authorization, production readiness, scanner readiness, or commercial offer approval.
