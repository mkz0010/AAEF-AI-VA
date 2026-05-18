# ADR-0375: Accept Safe Mock Demo Public Artifact Promotion Candidate

Status: accepted  
Date: 2026-05-18  
Version: v0.6.300

## Context

v0.6.299 created a documentation-only Safe Mock Demo Public Artifact Promotion Candidate.

## Decision

Accept the v0.6.299 candidate for future safe mock demo public artifact promotion.

## Decision record

~~~text
safe_mock_demo_public_artifact_promotion_candidate_review_completed = true
safe_mock_demo_public_artifact_promotion_candidate_accepted = true
safe_mock_demo_public_artifact_promotion_candidate_id = safe_mock_demo_public_artifact_promotion_candidate_v06299
safe_mock_demo_public_artifact_promotion_candidate_review_result = accepted_for_future_public_artifact_promotion
safe_mock_demo_public_artifact_promotion_candidate_status = accepted_for_future_public_artifact_promotion
future_safe_mock_demo_public_artifact_promotion_accepted = true
future_public_artifact_candidate_set_accepted = true
future_public_artifact_readme_entry_accepted = true
future_public_artifact_demo_path_summary_accepted = true
future_public_artifact_command_example_accepted = true
future_public_artifact_expected_statuses_accepted = true
future_public_artifact_boundary_wording_accepted = true
future_public_artifact_private_artifact_exclusion_accepted = true
future_public_artifact_publication_blockers_accepted = true
reviewed_safe_mock_demo_public_artifact_promotion_candidate_id = safe_mock_demo_public_artifact_promotion_candidate_v06299
reviewed_next_work_selection_id = next_work_selection_v06298
reviewed_safe_mock_demo_pre_public_boundary_review_id = safe_mock_demo_pre_public_boundary_review_v06296
safe_mock_demo_public_artifact_promotion_candidate_created = true
safe_mock_demo_public_artifact_promotion_candidate_selected = true
safe_mock_demo_public_artifact_candidate_set_accepted = true
safe_mock_demo_public_artifact_candidate_readme_entry_accepted = true
safe_mock_demo_public_artifact_candidate_demo_path_summary_accepted = true
safe_mock_demo_public_artifact_candidate_command_example_accepted = true
safe_mock_demo_public_artifact_candidate_expected_statuses_accepted = true
safe_mock_demo_public_artifact_candidate_boundary_wording_accepted = true
safe_mock_demo_public_artifact_candidate_private_artifact_exclusion_accepted = true
safe_mock_demo_public_artifact_candidate_publication_blockers_accepted = true
safe_mock_demo_status = runnable_private_artifact_demo_available
safe_mock_demo_is_live_scanner_execution = false
safe_mock_demo_private_artifacts_remain_private = true
safe_mock_demo_public_artifact_promotion_applied = false
safe_mock_demo_public_artifact_promotion_created = false
safe_mock_demo_public_artifact_promotion_approved = false
safe_mock_demo_public_positioning_approved_for_publication = false
publication_approval_selected = false
publication_approval = false
public_announcement = deferred
private_generated_outputs_moved_public = false
local_only_demo_execution_boundary_candidate_selected = false
local_only_demo_execution_boundary_candidate_created = false
local_only_runnable_demo_path_selected = false
real_scanner_execution_path_selected = false
real_scanner_execution_status = blocked
runtime_demo_ready = false
runtime_demo_readiness_claim = false
scanner_readiness_claim = false
production_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
runtime_readiness_status = not_detected_execution_blocked
target_lab_gate_status = target_defined_execution_blocked
runtime_destination_binding_status = bound_execution_blocked
bounded_execution_transition_status = candidate_recorded_execution_blocked
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
recommended_next_work_item = safe_mock_demo_public_artifact_promotion
safe_mock_demo_public_artifact_promotion_recommended = true
safe_mock_demo_public_artifact_promotion_candidate_review_and_decision_recommended = false
next_work_selection_recommended = false
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

The project should next perform the safe mock demo public artifact promotion step. Publication approval, public announcement, local-only execution boundary work, runtime readiness, scanner readiness, and real execution remain deferred.

## Boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- public artifact promotion candidate review is not publication approval
- public artifact promotion candidate review is not public artifact promotion
- public artifact promotion candidate review is not runtime demo readiness
- public artifact promotion candidate review is not scanner readiness
- No private generated outputs are moved public in v0.6.300.

## Structural token coverage

- safe_mock_demo_public_artifact_promotion_candidate_review_and_decision
- safe_mock_demo_public_artifact_promotion_candidate_review_completed
- safe_mock_demo_public_artifact_promotion_candidate_accepted
- safe_mock_demo_public_artifact_promotion_candidate_v06299
- safe_mock_demo_public_artifact_promotion_candidate
- safe_mock_demo_public_artifact_promotion
- next_work_selection_v06298
- safe_mock_demo_pre_public_boundary_review_v06296
- safe_mock_demo_initial_path
- safe mock demo
- safe mock demo public artifact promotion candidate
- safe mock demo public artifact promotion
- safe mock demo public positioning
- safe mock demo private artifact boundary
- safe mock demo command example
- safe mock demo expected statuses
- safe mock demo is not live scanner execution
- private-not-in-git
- allowed-action: completed
- denied-action: blocked
- human-approval-required: requires_human_approval
- local-only runnable demo
- real scanner execution remains blocked
- runtime readiness status: not_detected_execution_blocked
- target lab gate status: target_defined_execution_blocked
- binding gate status: bound_execution_blocked
- transition gate status: candidate_recorded_execution_blocked
- execution authorized: False
- real execution permitted: False
- public artifact promotion candidate review is not publication approval
- public artifact promotion candidate review is not public artifact promotion
- public artifact promotion candidate review is not runtime demo readiness
- public artifact promotion candidate review is not scanner readiness
- public artifact promotion candidate review is not production readiness
- No private generated outputs are moved public in v0.6.300.
- readme_front_page_rewritten = false
- repository_metadata_changed = false
