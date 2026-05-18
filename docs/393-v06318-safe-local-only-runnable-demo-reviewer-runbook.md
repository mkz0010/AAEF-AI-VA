# v0.6.318 Safe Local-Only Runnable Demo Reviewer Runbook

Status: runbook checkpoint  
Scope: AAEF-AI-VA safe local-only runnable demo reviewer runbook  
Previous checkpoint: v0.6.317 Safe Local-Only Runnable Demo Readiness Review  
Runbook result: safe local-only runnable demo reviewer runbook created  
Application status: runbook only; no runtime application, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed

## Purpose

This checkpoint creates a concise reviewer runbook for the safe local-only runnable demo.

The runbook explains what a local reviewer can run, what they should expect to see, and what boundaries remain closed. It is designed to make the v0.6.317 local reviewer walkthrough repeatable without changing the execution boundary.

This checkpoint does not approve publication, does not approve customer demonstrations, does not authorize execution, does not permit real scanner execution, does not apply runtime enforcement, and does not change gateway/runtime behavior.

No private generated outputs are moved public in v0.6.318.

## Runbook identity

~~~text
safe_local_only_runnable_demo_reviewer_runbook_created = true
safe_local_only_runnable_demo_reviewer_runbook_id = safe_local_only_runnable_demo_reviewer_runbook_v06318
safe_local_only_runnable_demo_reviewer_runbook_status = created_not_reviewed
safe_local_only_runnable_demo_reviewer_runbook_scope = local_reviewer_walkthrough_only
~~~

## Reviewer runbook

| runbook step | command or review action | expected visible result |
| --- | --- | --- |
| repository status | `git status --short` | no unrelated working-tree changes before demo review |
| mock gateway demo | `py tools/run_tool_gateway_example.py all` | `allowed-action: completed`, `denied-action: blocked`, `human-approval-required: requires_human_approval` |
| generated output validation | `py tools/validate_generated_outputs.py` | generated output validation passed |
| local target lab profile | `py tools/test_local_target_lab_profile.py` | `target lab gate status: target_defined_execution_blocked`, `target mode: localhost_only` |
| runtime destination binding | `py tools/test_runtime_destination_binding.py` | `binding gate status: bound_execution_blocked`, `target mode: localhost_only` |
| execution authorization gate | `py tools/test_execution_authorization_gate.py` | `execution authorized: False`, `real execution permitted: False` |
| preflight validation | `py tools/test_preflight_validation.py` | `preflight satisfied: False`, `execution authorized: False`, `real execution permitted: False` |
| runtime transition checkpoint | `py tools/test_runtime_transition_checkpoint.py` | `ready for preflight implementation: True`, `ready for runtime execution: False` |
| private artifact review | inspect printed `private-not-in-git` paths only | generated artifacts remain private |

## Runbook assertions

~~~text
safe local-only runnable demo reviewer runbook repository status check is defined
safe local-only runnable demo reviewer runbook mock gateway demo step is defined
safe local-only runnable demo reviewer runbook local target lab profile step is defined
safe local-only runnable demo reviewer runbook runtime destination binding step is defined
safe local-only runnable demo reviewer runbook execution authorization gate step is defined
safe local-only runnable demo reviewer runbook preflight validation step is defined
safe local-only runnable demo reviewer runbook private artifact review step is defined
~~~

## Reviewer script sequence

A local reviewer may use this sequence:

~~~bash
cd /e/AAEF-AI-VA
git status --short
py tools/run_tool_gateway_example.py all
py tools/validate_generated_outputs.py
py tools/test_local_target_lab_profile.py
py tools/test_runtime_destination_binding.py
py tools/test_execution_authorization_gate.py
py tools/test_preflight_validation.py
py tools/test_runtime_transition_checkpoint.py
~~~

The sequence is a mock-first localhost-only reviewer walkthrough. It is not a live scanner execution path and does not authorize execution.

## Expected reviewer-visible signals

The reviewer should see:

- `allowed-action: completed`
- `denied-action: blocked`
- `human-approval-required: requires_human_approval`
- `target lab gate status: target_defined_execution_blocked`
- `target mode: localhost_only`
- `binding gate status: bound_execution_blocked`
- `authorization gate status: authorization_scaffold_recorded_execution_blocked`
- `execution authorized: False`
- `preflight gate status: preflight_scaffold_recorded_execution_blocked`
- `preflight satisfied: False`
- `ready for runtime execution: False`
- `real execution permitted: False`
- `private-not-in-git` generated artifact paths

## Stop conditions

The runbook must stop and remain blocked if any of the following appear:

- non-localhost target
- public internet target
- private LAN target
- customer or third-party target
- production target
- external discovery
- credential use
- missing target lab profile
- missing runtime destination binding
- missing execution authorization gate
- missing preflight validation evidence
- AI-only justification
- request to move private generated outputs public

## Still not approved

The following remain false:

~~~text
safe_local_only_runnable_demo_public_ready = false
safe_local_only_runnable_demo_publication_ready = false
safe_local_only_runnable_demo_external_poc_ready = false
safe_local_only_runnable_demo_customer_demo_ready = false
runtime_demo_ready = false
scanner_readiness_claim = false
production_readiness_claim = false
~~~

## Preserved deferrals

~~~text
safe_local_only_runnable_demo_reviewer_runbook_review_completed = false
safe_local_only_runnable_demo_reviewer_runbook_accepted = false
safe_local_only_demo_execution_boundary_runtime_applied = false
safe_local_only_demo_execution_boundary_applied = false
publication_approval = false
public_announcement = deferred
runtime_demo_ready = false
scanner_readiness_claim = false
execution_authorized = false
real_execution_permitted = false
external_target_authorization = false
preflight_satisfied = false
concrete_checks_implemented = false
live_evidence_records_generated = false
runtime_enforcement_implemented = false
private_generated_outputs_moved_public = false
~~~

## Runtime and scanner boundary remains blocked

~~~text
real_scanner_execution_status = blocked
runtime readiness status: not_detected_execution_blocked
target lab gate status: target_defined_execution_blocked
binding gate status: bound_execution_blocked
transition gate status: candidate_recorded_execution_blocked
execution authorized: False
real execution permitted: False
~~~

## Decision fields

~~~text
safe_local_only_runnable_demo_reviewer_runbook_created = true
safe_local_only_runnable_demo_reviewer_runbook_id = safe_local_only_runnable_demo_reviewer_runbook_v06318
safe_local_only_runnable_demo_reviewer_runbook_status = created_not_reviewed
safe_local_only_runnable_demo_reviewer_runbook_scope = local_reviewer_walkthrough_only
safe_local_only_runnable_demo_reviewer_runbook_review_completed = false
safe_local_only_runnable_demo_reviewer_runbook_accepted = false
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
runbook_prerequisite_clean_checkout_required = true
runbook_prerequisite_python_available_required = true
runbook_prerequisite_no_network_targets_required = true
runbook_prerequisite_local_only_review_required = true
runbook_step_repository_status_check_defined = true
runbook_step_mock_gateway_demo_defined = true
runbook_step_generated_output_validation_defined = true
runbook_step_local_target_lab_profile_defined = true
runbook_step_runtime_destination_binding_defined = true
runbook_step_execution_authorization_gate_defined = true
runbook_step_preflight_validation_defined = true
runbook_step_runtime_transition_checkpoint_defined = true
runbook_step_private_artifact_review_defined = true
runbook_step_stop_condition_review_defined = true
runbook_expected_allowed_action_status_defined = true
runbook_expected_denied_action_status_defined = true
runbook_expected_human_approval_required_status_defined = true
runbook_expected_target_mode_localhost_only_defined = true
runbook_expected_execution_authorized_false_defined = true
runbook_expected_real_execution_permitted_false_defined = true
runbook_expected_preflight_satisfied_false_defined = true
runbook_expected_runtime_execution_ready_false_defined = true
runbook_expected_private_not_in_git_paths_defined = true
runbook_stop_condition_non_localhost_defined = true
runbook_stop_condition_external_discovery_defined = true
runbook_stop_condition_credentials_defined = true
runbook_stop_condition_missing_gate_defined = true
runbook_stop_condition_ai_only_justification_defined = true
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
recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook_review_and_decision
safe_local_only_runnable_demo_reviewer_runbook_review_and_decision_recommended = true
safe_local_only_runnable_demo_reviewer_runbook_recommended = false
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

## Explicit non-application boundary

This checkpoint creates a reviewer runbook only. It does not apply runtime enforcement, approve publication, create a public announcement, create runtime demo readiness, create scanner readiness, authorize execution, permit real execution, authorize external targets, change gateway behavior, change adapter behavior, change schema behavior, change runtime behavior, change scanner behavior, create fixtures, create actual records, rewrite the README front page, or change repository metadata.

## Claim boundaries

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- validator success is structural only
- publication remains deferred
- safe local-only runnable demo reviewer runbook is not execution authorization
- safe local-only runnable demo reviewer runbook is not runtime-applied enforcement
- safe local-only runnable demo reviewer runbook is not runtime demo readiness
- safe local-only runnable demo reviewer runbook is not scanner readiness
- safe local-only runnable demo reviewer runbook is not production readiness
- safe local-only runnable demo reviewer runbook is not external target authorization
- safe mock demo is not live scanner execution
- real scanner execution remains blocked
- verification report creation is deferred
- implementation changes are deferred

No production readiness, scanner readiness, external PoC readiness, customer PoC approval, paid engagement approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Structural token coverage

- safe_local_only_runnable_demo_reviewer_runbook
- safe_local_only_runnable_demo_reviewer_runbook_v06318
- safe_local_only_runnable_demo_reviewer_runbook_review_and_decision
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
- safe local-only runnable demo reviewer runbook is not execution authorization
- safe local-only runnable demo reviewer runbook is not runtime-applied enforcement
- safe local-only runnable demo reviewer runbook is not runtime demo readiness
- safe local-only runnable demo reviewer runbook is not scanner readiness
- safe local-only runnable demo reviewer runbook is not production readiness
- safe local-only runnable demo reviewer runbook is not external target authorization
- No private generated outputs are moved public in v0.6.318.
- readme_front_page_rewritten = false
- repository_metadata_changed = false

## Next checkpoint

~~~text
v0.6.319 Safe Local-Only Runnable Demo Reviewer Runbook Review and Decision
~~~
