# ADR-0384: Accept Safe Local-Only Runnable Demo Path Candidate

Status: accepted  
Date: 2026-05-18  
Version: v0.6.309

## Context

v0.6.308 created a documentation-only Safe Local-Only Runnable Demo Path Candidate.

## Decision

Accept the v0.6.308 candidate as a safe local-only runnable demo path candidate.

## Decision record

~~~text
safe_local_only_runnable_demo_path_candidate_review_completed = true
safe_local_only_runnable_demo_path_candidate_accepted = true
safe_local_only_runnable_demo_path_candidate_id = safe_local_only_runnable_demo_path_candidate_v06308
safe_local_only_runnable_demo_path_candidate_review_result = accepted_as_safe_local_only_runnable_demo_path_candidate
safe_local_only_runnable_demo_path_candidate_status = accepted_as_safe_local_only_runnable_demo_path_candidate
reviewed_safe_local_only_runnable_demo_path_candidate_created = true
reviewed_safe_local_only_runnable_demo_path_candidate_status = candidate_not_applied
reviewed_safe_local_only_runnable_demo_path_candidate_scope = documentation_only_candidate_for_safe_local_only_runnable_demo_path
safe_local_only_demo_execution_boundary_review_completed = true
safe_local_only_demo_execution_boundary_accepted = true
safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306
safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied
safe_local_only_demo_execution_boundary_target_mode = localhost_only
safe_local_only_demo_execution_boundary_runtime_applied = false
safe_local_only_demo_execution_boundary_applied = false
safe_local_only_runnable_demo_path_candidate_prerequisites_accepted = true
safe_local_only_runnable_demo_path_candidate_entrypoint_accepted = true
safe_local_only_runnable_demo_path_candidate_target_lab_profile_accepted = true
safe_local_only_runnable_demo_path_candidate_runtime_destination_binding_accepted = true
safe_local_only_runnable_demo_path_candidate_preflight_sequence_accepted = true
safe_local_only_runnable_demo_path_candidate_preflight_evidence_accepted = true
safe_local_only_runnable_demo_path_candidate_execution_authorization_gate_accepted = true
safe_local_only_runnable_demo_path_candidate_human_approval_gate_accepted = true
safe_local_only_runnable_demo_path_candidate_mock_first_execution_accepted = true
safe_local_only_runnable_demo_path_candidate_local_tool_invocation_accepted = true
safe_local_only_runnable_demo_path_candidate_evidence_output_accepted = true
safe_local_only_runnable_demo_path_candidate_review_walkthrough_accepted = true
safe_local_only_runnable_demo_path_candidate_stop_conditions_accepted = true
safe_local_only_runnable_demo_path_candidate_cleanup_boundary_accepted = true
safe_local_only_runnable_demo_path_candidate_expected_outputs_accepted = true
safe_local_only_runnable_demo_path_candidate_demo_command_sequence_accepted = true
safe_local_only_runnable_demo_path_candidate_excludes_external_targets = true
safe_local_only_runnable_demo_path_candidate_excludes_public_internet_targets = true
safe_local_only_runnable_demo_path_candidate_excludes_private_lan_targets = true
safe_local_only_runnable_demo_path_candidate_excludes_customer_or_third_party_targets = true
safe_local_only_runnable_demo_path_candidate_excludes_production_targets = true
safe_local_only_runnable_demo_path_candidate_excludes_credential_use = true
safe_local_only_runnable_demo_path_candidate_excludes_unreviewed_live_scanner_execution = true
safe_local_only_runnable_demo_path_candidate_excludes_public_movement_of_private_outputs = true
safe_local_only_runnable_demo_path_defined = false
safe_local_only_runnable_demo_path_applied = false
safe_local_only_runnable_demo_path_created = false
safe_local_only_runnable_demo_path_review_completed = false
safe_local_only_runnable_demo_path_accepted = false
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
recommended_next_work_item = safe_local_only_runnable_demo_path
safe_local_only_runnable_demo_path_recommended = true
safe_local_only_runnable_demo_path_candidate_review_and_decision_recommended = false
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

The project should next define the Safe Local-Only Runnable Demo Path. Runtime application, runnable path creation, runtime readiness, scanner readiness, execution authorization, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- safe local-only runnable demo path candidate review is not execution authorization
- safe local-only runnable demo path candidate review is not runnable demo creation
- safe local-only runnable demo path candidate review is not runtime-applied enforcement
- safe local-only runnable demo path candidate review is not external target authorization
- No private generated outputs are moved public in v0.6.309.

## Structural token coverage

- safe_local_only_runnable_demo_path_candidate_review_and_decision
- safe_local_only_runnable_demo_path_candidate_review_completed
- safe_local_only_runnable_demo_path_candidate_accepted
- safe_local_only_runnable_demo_path_candidate_v06308
- safe_local_only_runnable_demo_path_candidate
- safe_local_only_runnable_demo_path
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
- safe local-only runnable demo path candidate
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
- safe local-only runnable demo path candidate review is not execution authorization
- safe local-only runnable demo path candidate review is not runnable demo creation
- safe local-only runnable demo path candidate review is not runtime-applied enforcement
- safe local-only runnable demo path candidate review is not runtime demo readiness
- safe local-only runnable demo path candidate review is not scanner readiness
- safe local-only runnable demo path candidate review is not production readiness
- safe local-only runnable demo path candidate review is not external target authorization
- No private generated outputs are moved public in v0.6.309.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
