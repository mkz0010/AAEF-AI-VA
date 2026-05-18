# ADR-0388: Create Safe Local-Only Runnable Demo Path Creation Candidate

Status: proposed candidate  
Date: 2026-05-18  
Version: v0.6.313

## Context

v0.6.312 reviewed readiness to prepare a Safe Local-Only Runnable Demo Path Creation Candidate.

## Decision

Create a documentation-only Safe Local-Only Runnable Demo Path Creation Candidate.

## Decision record

~~~text
safe_local_only_runnable_demo_path_creation_candidate_created = true
safe_local_only_runnable_demo_path_creation_candidate_id = safe_local_only_runnable_demo_path_creation_candidate_v06313
safe_local_only_runnable_demo_path_creation_candidate_status = candidate_not_applied
safe_local_only_runnable_demo_path_creation_candidate_scope = documentation_only_candidate_for_path_creation
safe_local_only_runnable_demo_path_creation_candidate_review_completed = false
safe_local_only_runnable_demo_path_creation_candidate_accepted = false
safe_local_only_runnable_demo_path_creation_readiness_review_completed = true
safe_local_only_runnable_demo_path_creation_readiness_review_id = safe_local_only_runnable_demo_path_creation_readiness_review_v06312
safe_local_only_runnable_demo_path_creation_readiness_review_result = ready_for_creation_candidate_not_created
safe_local_only_runnable_demo_path_review_completed = true
safe_local_only_runnable_demo_path_accepted = true
safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310
safe_local_only_runnable_demo_path_status = accepted_not_created
safe_local_only_demo_execution_boundary_review_completed = true
safe_local_only_demo_execution_boundary_accepted = true
safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306
safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied
safe_local_only_demo_execution_boundary_target_mode = localhost_only
safe_local_only_demo_execution_boundary_runtime_applied = false
safe_local_only_demo_execution_boundary_applied = false
creation_candidate_boundary_prerequisite_confirmed = true
creation_candidate_path_prerequisite_confirmed = true
creation_candidate_readiness_review_confirmed = true
creation_candidate_mock_gateway_demo_step_defined = true
creation_candidate_local_target_lab_profile_step_defined = true
creation_candidate_runtime_destination_binding_step_defined = true
creation_candidate_bounded_transition_step_defined = true
creation_candidate_local_execution_plan_review_step_defined = true
creation_candidate_runtime_safety_policy_step_defined = true
creation_candidate_runtime_enforcement_design_step_defined = true
creation_candidate_execution_authorization_gate_step_defined = true
creation_candidate_preflight_validation_step_defined = true
creation_candidate_preflight_evidence_reference_step_defined = true
creation_candidate_private_artifact_review_step_defined = true
creation_candidate_reviewer_walkthrough_step_defined = true
creation_candidate_expected_terminal_outputs_defined = true
creation_candidate_expected_json_outputs_defined = true
creation_candidate_expected_markdown_outputs_defined = true
creation_candidate_stop_conditions_defined = true
creation_candidate_cleanup_boundary_defined = true
creation_candidate_should_remain_mock_first = true
creation_candidate_should_remain_localhost_only = true
creation_candidate_should_keep_execution_blocked_by_default = true
creation_candidate_should_use_private_not_in_git_outputs = true
creation_candidate_should_not_move_private_outputs_public = true
creation_candidate_excludes_external_targets = true
creation_candidate_excludes_public_internet_targets = true
creation_candidate_excludes_private_lan_targets = true
creation_candidate_excludes_customer_or_third_party_targets = true
creation_candidate_excludes_production_targets = true
creation_candidate_excludes_credential_use = true
creation_candidate_excludes_unreviewed_live_scanner_execution = true
creation_candidate_excludes_public_movement_of_private_outputs = true
safe_local_only_runnable_demo_path_created = false
safe_local_only_runnable_demo_path_applied = false
safe_local_only_runnable_demo_ready = false
safe_local_only_runnable_demo_review_completed = false
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
local_only_demo_execution_boundary_candidate_selected = false
local_only_demo_execution_boundary_candidate_created = false
local_only_runnable_demo_path_selected = false
local_only_runnable_demo_path_created = false
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
recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate_review_and_decision
safe_local_only_runnable_demo_path_creation_candidate_review_and_decision_recommended = true
safe_local_only_runnable_demo_path_creation_candidate_recommended = false
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

The project should next review this creation candidate before any runnable demo path is created. Runnable path creation, runtime application, runtime readiness, scanner readiness, execution authorization, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe local-only runnable demo path creation candidate is not execution authorization
- safe local-only runnable demo path creation candidate is not runnable demo creation
- safe local-only runnable demo path creation candidate is not runtime-applied enforcement
- safe local-only runnable demo path creation candidate is not external target authorization
- No private generated outputs are moved public in v0.6.313.

## Structural token coverage

- safe_local_only_runnable_demo_path_creation_candidate
- safe_local_only_runnable_demo_path_creation_candidate_v06313
- safe_local_only_runnable_demo_path_creation_candidate_review_and_decision
- safe_local_only_runnable_demo_path_creation_readiness_review_v06312
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
- safe local-only demo execution boundary
- safe local-only runnable demo path
- safe mock demo is not live scanner execution
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
- safe local-only runnable demo path creation candidate is not execution authorization
- safe local-only runnable demo path creation candidate is not runnable demo creation
- safe local-only runnable demo path creation candidate is not runtime-applied enforcement
- safe local-only runnable demo path creation candidate is not runtime demo readiness
- safe local-only runnable demo path creation candidate is not scanner readiness
- safe local-only runnable demo path creation candidate is not production readiness
- safe local-only runnable demo path creation candidate is not external target authorization
- No private generated outputs are moved public in v0.6.313.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
