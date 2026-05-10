# v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint implements the mock/dry-run `completed` status terminology cleanup candidate after v0.6.139 selected the work item.

This is checkpoint 1 of 2 for a Medium-risk terminology and evidence-interpretation work item.

This checkpoint implements the mock/dry-run `completed` status terminology cleanup candidate.

The review and decision are deferred to v0.6.141.

## Candidate implementation summary

This checkpoint adds a reviewer-facing terminology helper and tests for disambiguating mock/dry-run `completed` outputs.

The helper preserves the raw status string and does not modify runtime behavior, gate behavior, scanner behavior, Docker behavior, credential behavior, customer-target behavior, or delivery behavior.

The candidate terminology maps mock/dry-run or explicitly no-real-execution `completed` records to a reviewer-facing status:

~~~text
mock_dry_run_completed_no_real_execution
~~~

This is a terminology and evidence-interpretation layer only.

## Candidate helper

~~~text
tools/mock_dry_run_status_terminology.py
~~~

The helper exposes:

~~~text
classify_mock_dry_run_completed_status(record)
MockDryRunStatusTerminology.as_evidence()
~~~

## Candidate behavior

| Case | Candidate behavior |
| --- | --- |
| raw `completed` with `execution_mode=dry_run` | reviewer status `mock_dry_run_completed_no_real_execution`; raw status preserved |
| raw `completed` with mock marker | reviewer status `mock_dry_run_completed_no_real_execution`; raw status preserved |
| raw `completed` with explicit no-real-execution flag | reviewer status `mock_dry_run_completed_no_real_execution`; raw status preserved |
| raw `completed` with execution-blocked note | reviewer status `mock_dry_run_completed_no_real_execution`; raw status preserved |
| raw `completed` without context | reviewer status `completed_context_unclassified_requires_review`; raw status preserved |
| raw non-`completed` status | reviewer status remains unchanged |
| malformed status record | reviewer status `malformed_status_record_requires_review` |

## Raw status compatibility

This candidate does not rename the raw `completed` status.

It adds a reviewer-facing terminology layer so reviewers do not mistake mock/dry-run completion for real execution completion.

Compatibility decision:

~~~text
raw_status = completed
reviewer_status = mock_dry_run_completed_no_real_execution
raw_status_preserved = true
behavior_modified = false
~~~

## Evidence-safe result model

The helper returns a `MockDryRunStatusTerminology` object with:

~~~text
raw_status
reviewer_status
reviewer_label
reason
raw_status_preserved
behavior_modified
evidence_notes
~~~

The result intentionally avoids including raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, full raw request payloads, full raw authorization decision payloads, or live third-party target details.

## Candidate tests

This checkpoint adds:

~~~text
tools/test_mock_dry_run_completed_status_terminology.py
tools/test_v06140_mock_dry_run_completed_status_terminology_cleanup_candidate.py
~~~

The tests cover:

* dry-run `completed` reviewer status,
* mock `completed` reviewer status,
* explicit no-real-execution `completed` reviewer status,
* execution-blocked note `completed` reviewer status,
* ambiguous `completed` requiring context review,
* non-`completed` status preservation,
* malformed status record review requirement,
* evidence-safe output shape,
* v0.6.139 selection continuity,
* v0.6.141 review/decision deferral.

## Candidate record

~~~text
mock_dry_run_completed_status_terminology_cleanup_candidate_completed = true
mock_dry_run_completed_status_terminology_cleanup_candidate_is_medium_risk = true
mock_dry_run_completed_status_terminology_cleanup_candidate_checkpoint_1_of_2 = true
mock_dry_run_completed_status_terminology_cleanup_review_decision_deferred_to_v06141 = true
mock_dry_run_completed_status_terminology_helper_added = true
mock_dry_run_completed_status_terminology_helper_tests_added = true
mock_dry_run_completed_status_reviewer_label_added = true
mock_dry_run_completed_status_raw_status_preserved = true
mock_dry_run_completed_status_behavior_preserved = true
mock_dry_run_completed_status_no_real_execution_label_supported = true
mock_dry_run_completed_status_ambiguous_context_requires_review = true
mock_completed_status_renamed = false
mock_dry_run_status_behavior_modified = false
raw_completed_status_behavior_modified = false
runtime_status_contract_modified = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
review_decision_completed = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
external_discovery_fail_closed_added = false
constraint_diff_enforcement_added = false
authorization_expiry_now_check_added = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_checkpoint = v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision
~~~

## What changed

The following files are added:

~~~text
tools/mock_dry_run_status_terminology.py
tools/test_mock_dry_run_completed_status_terminology.py
tools/test_v06140_mock_dry_run_completed_status_terminology_cleanup_candidate.py
docs/216-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md
planning/decisions/ADR-0210-add-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md
planning/issues/0209-add-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md
~~~

The following files are updated for repository navigation and checks:

~~~text
README.md
CHANGELOG.md
ROADMAP.md
tools/run_all_local_checks.py
~~~

## What did not happen

No review/decision closeout is completed.

No raw mock/dry-run `completed` status is renamed.

No mock/dry-run status behavior is modified.

No runtime status contract is modified.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No external_discovery fail-closed behavior is added or modified.

No request/decision constraint-diff enforcement is added or modified.

No authorization expiry current-time check is added or modified.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.139

v0.6.139 selected mock/dry-run `completed` status terminology cleanup as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate
v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.138

v0.6.138 closed the external_discovery=true fail-closed behavior work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next checkpoint

Proceed to:

~~~text
v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision
~~~

That checkpoint should review the candidate terminology behavior, confirm raw status compatibility and non-execution boundaries, and decide whether to close the Medium-risk work item.
