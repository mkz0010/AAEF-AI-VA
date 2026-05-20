# ADR-0445: Prepare Mock/Dry-Run Status Terminology Public Output Cleanup

Status: accepted
Date: 2026-05-20
Version: v0.6.370

## Context

The private reviewer evidence trace path now provides a safe place to represent raw/reviewer status separation. The remaining visible risk is public or runner-facing raw `completed` wording.

## Decision

Define readiness for a mock/dry-run status terminology public output cleanup candidate.

## Decision record

~~~text
mock_dry_run_status_terminology_public_output_cleanup_readiness_review_completed = true\nmock_dry_run_status_terminology_public_output_cleanup_scope_defined = true\nmock_dry_run_status_terminology_public_output_cleanup_ready_for_candidate = true\nmock_dry_run_status_terminology_public_output_cleanup_target_runner_console_output = true\nmock_dry_run_status_terminology_public_output_cleanup_target_public_artifact_status_lines = true\nmock_dry_run_status_terminology_public_output_cleanup_target_readme_status_wording = true\nmock_dry_run_status_terminology_public_output_cleanup_raw_completed_status_preserved_for_compatibility = true\nmock_dry_run_status_terminology_public_output_cleanup_reviewer_status_value = mock_dry_run_completed_no_real_execution\nmock_dry_run_status_terminology_public_output_cleanup_public_display_must_not_show_bare_completed = true\nmock_dry_run_status_terminology_public_output_cleanup_raw_and_reviewer_status_separation_required = true\nprivate_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_closed = true\nauthorization_expiry_current_time_gateway_core_integrated = true\nrequest_decision_constraint_diff_gateway_core_integrated = true\nexternal_discovery_fail_closed_gateway_core_integrated = true\ncontrolled_executor_validation_gateway_core_integrated = false\nv06370_gateway_core_behavior_changed = false\nv06370_tool_gateway_behavior_changed = false\nv06370_runtime_behavior_changed = false\nv06370_scanner_behavior_changed = false\nv06370_schema_changed = false\nv06370_generated_outputs_changed = false\nv06370_public_artifacts_changed = false\nv06370_private_generated_outputs_moved_public = false\npublication_approval = false\npublic_announcement = deferred\ncustomer_demo_approval = false\nexecution_authorized = false\nreal_execution_permitted = false\nexternal_target_authorization = false\nruntime_demo_ready = false\nscanner_readiness_claim = false\nproduction_readiness_claim = false\nrecommended_next_work_item = mock_dry_run_status_terminology_public_output_cleanup_candidate\nModel output is not authority.\nAI rationale is not authorization.\nA gate decision is not AI self-approval.\nEvidence supports reconstruction; it does not prove legal truth.\nvalidator success is structural only\npublication remains deferred\nReadiness review is not production readiness.\nReadiness review is not scanner readiness.\nReadiness review is not execution authorization.\nReadiness review is not real execution permission.\nReadiness review is not external target authorization.\nReadiness review is not customer demo approval.\nReadiness review is not commercial offer approval.\nNo private generated outputs are moved public in v0.6.370.\nv0.6.371 Mock/Dry-Run Status Terminology Public Output Cleanup Candidate
~~~

## Boundaries

This readiness review does not change schemas, generated outputs, runtime behavior, scanner behavior, public artifacts, execution authorization, external target authorization, production readiness, scanner readiness, or commercial offer approval.\n