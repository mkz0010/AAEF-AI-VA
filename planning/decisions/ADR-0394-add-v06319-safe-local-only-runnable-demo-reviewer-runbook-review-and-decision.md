# ADR-0394: Accept Safe Local-Only Runnable Demo Reviewer Runbook

Status: accepted  
Date: 2026-05-18  
Version: v0.6.319

## Context

v0.6.318 created a concise local reviewer runbook for the safe local-only runnable demo.

## Decision

Accept the v0.6.318 runbook as the local reviewer walkthrough runbook.

## Decision record

~~~text
safe_local_only_runnable_demo_reviewer_runbook_review_completed = true
safe_local_only_runnable_demo_reviewer_runbook_accepted = true
safe_local_only_runnable_demo_reviewer_runbook_id = safe_local_only_runnable_demo_reviewer_runbook_v06318
safe_local_only_runnable_demo_reviewer_runbook_review_result = accepted_as_local_reviewer_walkthrough_runbook
safe_local_only_runnable_demo_reviewer_runbook_status = accepted_not_public_demo_ready
reviewed_safe_local_only_runnable_demo_reviewer_runbook_created = true
reviewed_safe_local_only_runnable_demo_reviewer_runbook_scope = local_reviewer_walkthrough_only
safe_local_only_runnable_demo_readiness_review_completed = true
safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317
safe_local_only_runnable_demo_readiness_review_result = ready_as_mock_first_localhost_only_reviewer_demo
safe_local_only_runnable_demo_ready = true
safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo
safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough
safe_local_only_runnable_demo_public_ready = false
safe_local_only_runnable_demo_publication_ready = false
safe_local_only_runnable_demo_external_poc_ready = false
safe_local_only_runnable_demo_customer_demo_ready = false
safe_local_only_runnable_demo_path_creation_review_completed = true
safe_local_only_runnable_demo_path_creation_accepted = true
safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315
safe_local_only_runnable_demo_path_created = true
safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310
safe_local_only_runnable_demo_path_status = accepted_created_not_runtime_applied
safe_local_only_runnable_demo_path_applied = false
runbook_prerequisite_clean_checkout_accepted = true
runbook_prerequisite_python_available_accepted = true
runbook_prerequisite_no_network_targets_accepted = true
runbook_prerequisite_local_only_review_accepted = true
runbook_step_repository_status_check_accepted = true
runbook_step_mock_gateway_demo_accepted = true
runbook_step_generated_output_validation_accepted = true
runbook_step_local_target_lab_profile_accepted = true
runbook_step_runtime_destination_binding_accepted = true
runbook_step_execution_authorization_gate_accepted = true
runbook_step_preflight_validation_accepted = true
runbook_step_runtime_transition_checkpoint_accepted = true
runbook_step_private_artifact_review_accepted = true
runbook_step_stop_condition_review_accepted = true
runbook_expected_allowed_action_status_accepted = true
runbook_expected_denied_action_status_accepted = true
runbook_expected_human_approval_required_status_accepted = true
runbook_expected_target_mode_localhost_only_accepted = true
runbook_expected_execution_authorized_false_accepted = true
runbook_expected_real_execution_permitted_false_accepted = true
runbook_expected_preflight_satisfied_false_accepted = true
runbook_expected_runtime_execution_ready_false_accepted = true
runbook_expected_private_not_in_git_paths_accepted = true
runbook_stop_condition_non_localhost_accepted = true
runbook_stop_condition_external_discovery_accepted = true
runbook_stop_condition_credentials_accepted = true
runbook_stop_condition_missing_gate_accepted = true
runbook_stop_condition_ai_only_justification_accepted = true
runbook_mock_first = true
runbook_localhost_only = true
runbook_execution_blocked_by_default = true
runbook_private_not_in_git_outputs = true
runbook_no_private_outputs_moved_public = true
runbook_excludes_external_targets = true
runbook_excludes_public_internet_targets = true
runbook_excludes_private_lan_targets = true
runbook_excludes_customer_or_third_party_targets = true
runbook_excludes_production_targets = true
runbook_excludes_credential_use = true
runbook_excludes_unreviewed_live_scanner_execution = true
safe_local_only_demo_execution_boundary_review_completed = true
safe_local_only_demo_execution_boundary_accepted = true
safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306
safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied
safe_local_only_demo_execution_boundary_target_mode = localhost_only
safe_local_only_demo_execution_boundary_runtime_applied = false
safe_local_only_demo_execution_boundary_applied = false
safe_mock_demo_public_artifact_promotion_review_completed = true
safe_mock_demo_public_artifact_promotion_accepted = true
safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
publication_approval_selected = false
publication_approval = false
public_announcement = deferred
private_generated_outputs_moved_public = false
real_scanner_execution_path_selected = false
real_scanner_execution_status = blocked
runtime_demo_ready = false
runtime_demo_readiness_claim = false
scanner_readiness_claim = false
production_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_review
safe_local_only_runnable_demo_public_positioning_review_recommended = true
safe_local_only_runnable_demo_reviewer_runbook_review_and_decision_recommended = false
gateway_execution_path_behavior_modified = false
tool_gateway_behavior_changed = false
adapter_behavior_changed = false
schema_changed = false
runtime_behavior_changed = false
scanner_behavior_changed = false
fixtures_created = false
record_candidate_artifacts_created = false
actual_records_created = false
readme_front_page_rewritten = false
repository_metadata_changed = false
certification_claim = false
legal_compliance_claim = false
audit_opinion_claim = false
diagnostic_completeness_claim = false
external_framework_equivalence_claim = false
~~~

## Consequences

The project should next review public positioning for the safe local-only runnable demo without converting it into public demo readiness. Publication, customer demonstration, runtime application, runtime readiness, scanner readiness, execution authorization, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe local-only runnable demo reviewer runbook review is not execution authorization
- safe local-only runnable demo reviewer runbook review is not runtime-applied enforcement
- safe local-only runnable demo reviewer runbook review is not external target authorization
- No private generated outputs are moved public in v0.6.319.

## Structural token coverage

- safe_local_only_runnable_demo_reviewer_runbook_review_and_decision
- safe_local_only_runnable_demo_reviewer_runbook_review_completed
- safe_local_only_runnable_demo_reviewer_runbook_accepted
- safe_local_only_runnable_demo_reviewer_runbook_v06318
- safe_local_only_runnable_demo_reviewer_runbook
- safe_local_only_runnable_demo_public_positioning_review
- safe_local_only_runnable_demo_readiness_review_v06317
- safe_local_only_runnable_demo_ready
- mock_first_localhost_only_reviewer_demo
- safe_local_only_runnable_demo_path_creation_v06315
- safe_local_only_runnable_demo_path
- safe_local_only_runnable_demo_path_v06310
- safe_local_only_demo_execution_boundary_v06306
- safe_local_only_demo_execution_boundary
- localhost_only
- loopback-only target boundary
- mock_first_no_live_scanner_default
- external target authorization remains false
- safe_mock_demo_public_artifact
- docs/public-artifacts/safe-mock-demo-public-artifact.md
- safe mock demo
- private-not-in-git
- allowed-action: completed
- denied-action: blocked
- human-approval-required: requires_human_approval
- real scanner execution remains blocked
- runtime readiness status: not_detected_execution_blocked
- target lab gate status: target_defined_execution_blocked
- binding gate status: bound_execution_blocked
- transition gate status: candidate_recorded_execution_blocked
- execution authorized: False
- real execution permitted: False
- safe local-only runnable demo reviewer runbook review is not execution authorization
- safe local-only runnable demo reviewer runbook review is not runtime-applied enforcement
- safe local-only runnable demo reviewer runbook review is not runtime demo readiness
- safe local-only runnable demo reviewer runbook review is not scanner readiness
- safe local-only runnable demo reviewer runbook review is not production readiness
- safe local-only runnable demo reviewer runbook review is not external target authorization
- No private generated outputs are moved public in v0.6.319.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
