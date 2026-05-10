# v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate

Status: candidate
Date: 2026-05-10

## Purpose

This checkpoint prepares SECURITY.md reporting-channel consistency after v0.6.124 selected it as the next Medium-risk work item.

This is checkpoint 1 of 2 for a Medium-risk public-facing documentation change.

This checkpoint prepares the SECURITY.md reporting-channel consistency candidate.

The review and decision are deferred to v0.6.126.

## Candidate summary

The candidate adds or confirms a SECURITY.md section titled:

~~~text
Reporting channel and scope clarification
~~~

The candidate clarifies that sensitive reports about this repository should use GitHub Security Advisories / private vulnerability reporting when that channel is available.

It also clarifies that public GitHub issues are only for non-sensitive coordination, and that this repository is not authorization to test third-party systems.

## Candidate SECURITY.md wording

~~~markdown
## Reporting channel and scope clarification

Use GitHub Security Advisories / private vulnerability reporting for sensitive reports about this repository when that channel is available.

If the private reporting channel is unavailable, open a public GitHub issue only for non-sensitive coordination and do not include exploit details, secrets, credentials, target-specific data, private customer material, scanner output, or other sensitive information.

Security reports for this repository should concern the AAEF-AI-VA implementation, documentation, examples, release process, or repository configuration.

This repository is not an authorization to test third-party systems. Do not use this repository, its examples, or its documentation as permission to scan, attack, probe, exploit, or otherwise test systems that you do not own or do not have explicit written authorization to assess.

Do not submit live third-party vulnerability details, customer target data, credentials, tokens, private scan output, exploit chains, or operationally sensitive diagnostics through public issues.

AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries. It is not a production vulnerability scanner, not a managed vulnerability disclosure program, not a bug bounty program, not an emergency response service, not a certification scheme, not a legal compliance claim, not an audit opinion, and not an authorization service.

For questions about commercial licensing, paid evaluation, or NDA-based adoption discussions, use the commercial contact path described in the repository documentation rather than the vulnerability reporting channel.
~~~

## Candidate record

~~~text
security_reporting_channel_consistency_candidate_completed = true
security_reporting_channel_consistency_candidate_is_medium_risk = true
security_reporting_channel_consistency_candidate_checkpoint_1_of_2 = true
security_reporting_channel_consistency_review_decision_deferred_to_v06126 = true
security_reporting_channel_consistency_candidate_added_security_section = true
security_reporting_channel_consistency_candidate_public_facing = true
security_reporting_channel_consistency_candidate_documentation_only = true
security_reporting_channel_consistency_candidate_not_final_review = true
security_reporting_channel_consistency_candidate_not_closeout = true
security_reporting_channel_consistency_private_reporting_when_available = true
security_reporting_channel_consistency_public_issue_non_sensitive_only = true
security_reporting_channel_consistency_no_third_party_testing_authorization = true
security_reporting_channel_consistency_no_public_secrets_or_scanner_output = true
security_reporting_channel_consistency_commercial_contact_separated = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
readme_current_latest_baseline_clarity_work_item_closed = true
authorization_expiry_now_check_added = false
constraint_diff_enforcement_added = false
external_discovery_fail_closed_added = false
mock_completed_status_renamed = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
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
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_checkpoint = v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision
~~~

## Boundary preserved

The SECURITY.md reporting-channel consistency candidate is documentation-only.

It does not modify runtime behavior, validator behavior, schemas, fixture metadata contracts, public samples, AAEF main handback state, or external submission state.

It preserves the boundary that AAEF-AI-VA is a safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.

It clarifies that AAEF-AI-VA is not a production vulnerability scanner, not a managed vulnerability disclosure program, not a bug bounty program, not an emergency response service, not a certification scheme, not a legal compliance claim, not an audit opinion, and not an authorization service.

It clarifies that the vulnerability reporting channel is for repository security issues, not commercial licensing, paid evaluation, NDA-based adoption discussions, third-party vulnerability submissions, or customer-target vulnerability disclosure.

## Relationship to v0.6.124

v0.6.124 selected SECURITY.md reporting-channel consistency as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate
v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision
~~~

This checkpoint is the candidate checkpoint.

## Relationship to v0.6.123

v0.6.123 closed the README current/latest baseline clarity work item.

This checkpoint does not reopen that work item.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

No review/decision closeout is completed for SECURITY.md reporting-channel consistency.

No authorization expiry now check is added.

No request/decision constraint-diff enforcement is added.

No external_discovery fail-closed behavior is added.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

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

No AAEF Core, Profile, or Practical Package promotion is decided.

## Next checkpoint

Proceed to:

~~~text
v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision
~~~

That checkpoint should review the candidate wording, confirm public-safe boundaries, and decide whether the Medium-risk SECURITY.md reporting-channel consistency work item is complete.
