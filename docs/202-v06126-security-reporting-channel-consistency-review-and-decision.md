# v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint reviews the SECURITY.md reporting-channel consistency candidate prepared in v0.6.125.

This is checkpoint 2 of 2 for a Medium-risk public-facing documentation change.

This checkpoint reviews and accepts the SECURITY.md reporting-channel consistency candidate from v0.6.125.

The SECURITY.md reporting-channel consistency work item is closed.

## Review conclusion

Candidate accepted.

No sensitive public issue path confusion found.

No third-party testing authorization confusion found.

No commercial contact confusion found.

No overclaim found.

No external submission effect.

No runtime effect.

No validator effect.

No schema effect.

No public sample effect.

The SECURITY.md reporting-channel consistency wording is accepted as public-facing documentation-only wording.

## Decision record

~~~text
security_reporting_channel_consistency_review_decision_completed = true
security_reporting_channel_consistency_review_decision_is_medium_risk = true
security_reporting_channel_consistency_review_decision_checkpoint_2_of_2 = true
security_reporting_channel_consistency_candidate_reviewed = true
security_reporting_channel_consistency_candidate_accepted = true
security_reporting_channel_consistency_work_item_closed = true
security_reporting_channel_consistency_public_facing = true
security_reporting_channel_consistency_documentation_only = true
security_reporting_channel_consistency_no_sensitive_public_issue_path_confusion_found = true
security_reporting_channel_consistency_no_third_party_testing_authorization_confusion_found = true
security_reporting_channel_consistency_no_commercial_contact_confusion_found = true
security_reporting_channel_consistency_no_overclaim_found = true
security_reporting_channel_consistency_no_external_submission_effect = true
security_reporting_channel_consistency_no_runtime_effect = true
security_reporting_channel_consistency_no_validator_effect = true
security_reporting_channel_consistency_no_schema_effect = true
security_reporting_channel_consistency_no_public_sample_effect = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
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
selected_next_direction = next_work_selection_using_risk_tiered_granularity
selected_next_checkpoint = v0.6.127 Next Work Selection Using Risk-Tiered Granularity
~~~

## Reviewed SECURITY.md section

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

## Review checklist

| Check | Result |
| --- | --- |
| Sensitive reports use private vulnerability reporting when available | pass |
| Public issues are limited to non-sensitive coordination | pass |
| Public issues exclude exploit details, secrets, credentials, customer material, and scanner output | pass |
| Repository security reports are scoped to AAEF-AI-VA repository concerns | pass |
| Third-party testing authorization confusion avoided | pass |
| Live third-party vulnerability details are excluded from public issues | pass |
| Commercial/NDA discussions are separated from vulnerability reporting | pass |
| Production vulnerability scanner claim avoided | pass |
| Managed vulnerability disclosure program claim avoided | pass |
| Bug bounty program claim avoided | pass |
| Emergency response service claim avoided | pass |
| Certification claim avoided | pass |
| Legal compliance claim avoided | pass |
| Audit opinion claim avoided | pass |
| Authorization service claim avoided | pass |

## Relationship to v0.6.125

v0.6.125 prepared the SECURITY.md reporting-channel consistency candidate as checkpoint 1 of 2.

This v0.6.126 checkpoint reviews and accepts the candidate as checkpoint 2 of 2.

The Medium-risk SECURITY.md reporting-channel consistency work item is now closed.

## Relationship to v0.6.124

v0.6.124 selected SECURITY.md reporting-channel consistency as a Medium-risk work item and assigned two checkpoints:

~~~text
v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate
v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision
~~~

This checkpoint completes that planned two-checkpoint split.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

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

## Next direction

The next checkpoint should select the next work item using the v0.6.120 risk-tiered checkpoint granularity policy.

Likely next checkpoint:

~~~text
v0.6.127 Next Work Selection Using Risk-Tiered Granularity
~~~

That checkpoint should be a Low-risk one-checkpoint direction-selection record unless a specific risk requires a larger split.
