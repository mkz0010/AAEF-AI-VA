# v0.6.157 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-11

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.156 closed the Reviewer Walkthrough work item.

## Decision

The selected next work item is External Review Package Integration.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.158 External Review Package Integration Candidate.

This checkpoint does not create the External Review Package.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06157_completed = true
next_work_selection_v06157_is_documentation_only = true
next_work_selection_v06157_uses_v06120_granularity_policy = true
next_work_selection_v06157_uses_v06156_completed_work_item = true
v06157_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = external_review_package_integration
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.158 External Review Package Integration Candidate
external_review_package_integration_selected = true
reviewer_walkthrough_work_item_closed = true
control_matrix_work_item_closed = true
safe_poc_boundary_template_work_item_closed = true
technical_due_diligence_summary_work_item_closed = true
enterprise_review_guide_work_item_closed = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
external_review_package_created = false
external_review_package_modified = false
reviewer_walkthrough_created = false
reviewer_walkthrough_modified = false
control_matrix_created = false
control_matrix_modified = false
safe_poc_boundary_template_created = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_created = false
technical_due_diligence_summary_modified = false
enterprise_review_guide_created = false
enterprise_review_guide_modified = false
customer_poc_authorized = false
commercial_contract_created = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
runtime_behavior_modified = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
certification_claim_occurs = false
legal_compliance_claim_occurs = false
audit_opinion_claim_occurs = false
production_readiness_claim_occurs = false
external_framework_equivalence_claim_occurs = false
diagnostic_completeness_claim_occurs = false
third_party_testing_authorization_claim_occurs = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
~~~

## Candidate work items reviewed

| Candidate | Risk tier | Selected | Reason |
| --- | --- | --- | --- |
| External Review Package Integration | Medium | yes | Enterprise Review Guide, Technical Due Diligence Summary, Safe PoC Boundary Template, Control Matrix, and Reviewer Walkthrough are now accepted. A package-level integration artifact can give external reviewers a single entry point without creating customer PoC approval, delivery approval, or production-readiness claims. |
| Public-facing navigation polish only | Low or Medium | no | Useful, but too narrow. The current state needs an explicit integration boundary that explains the package and its limits, not just link polishing. |
| Buyer-facing review packet boundary | Medium | no | Useful, but should be handled inside the broader external review package integration so buyer-facing interpretation remains tied to non-authorizing boundaries. |
| AAEF main handback reconsideration | Medium or High | no | The v0.6.119 handback sequence remains paused. A public-safe AAEF main handback should wait until applied-implementation lessons are consolidated into narrow evidence/interface lessons. |
| Runtime execution preparation | High or Critical | no | Runtime/scanner/customer-target activity remains outside the current safe direction and would require a larger risk split. |

## Selected work item

~~~text
selected_next_work_item = external_review_package_integration
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to create a claim-safe integration artifact for the external review package.

The package integration should connect README positioning, Enterprise Review Guide, Technical Due Diligence Summary, Safe PoC Boundary Template, Control Matrix, Reviewer Walkthrough, relevant test families, versioned decision records, conservative claim boundaries, and non-authorizing interpretation limits.

It should not create runtime approval, customer PoC approval, customer delivery approval, legal/compliance claims, audit claims, certification claims, production readiness claims, diagnostic-completeness claims, or external-framework equivalence claims.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, an integrated external review package can be perceived as a customer packet, due-diligence packet, commercial evaluation packet, audit package, certification package, production readiness package, or PoC authorization package if poorly scoped.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, customer PoC authorization, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, customer delivery artifact, or AAEF main handback submission.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will create an external-review-facing integration artifact that may influence how buyers, technical reviewers, sponsors, maintainers, and possible commercial reviewers interpret the repository.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.158 External Review Package Integration Candidate
v0.6.159 External Review Package Integration Review and Decision
~~~

v0.6.158 should create the candidate integration artifact and tests. The artifact should remain claim-safe, non-authorizing, and aligned with the Enterprise Review Guide, Technical Due Diligence Summary, Safe PoC Boundary Template, Control Matrix, and Reviewer Walkthrough.

v0.6.159 should review the integration artifact, confirm claim boundaries, and decide whether to close the work item.

## Expected External Review Package Integration scope

The External Review Package Integration candidate should likely include:

* intended reader,
* package purpose,
* non-authorizing notice,
* document inventory,
* recommended entry points,
* reviewer paths,
* evidence/test-family index,
* boundary and non-goal summary,
* package-level claim-boundary summary,
* questions the package can answer,
* questions the package cannot answer,
* when to use the Safe PoC Boundary Template,
* when not to request a PoC,
* what remains outside the public package,
* explicit non-goals.

The artifact should help a reviewer navigate the external review package, not operate a scanner, approve testing, approve delivery, or create a commercial contract.

## Claim boundaries for the selected work

The External Review Package Integration candidate must not claim:

~~~text
certification
legal compliance
audit opinion
audit sufficiency
production readiness
production scanner status
diagnostic completeness
authorization for third-party testing
customer PoC approval
commercial contract creation
customer delivery approval
equivalence with external frameworks
AAEF Core/Profile/Practical Package promotion
~~~

The integration artifact may help reviewers navigate the current AAEF-AI-VA documentation and evidence-boundary package.

## What did not happen

No External Review Package is created in this checkpoint.

No Reviewer Walkthrough is created or modified.

No Control Matrix is created or modified.

No Safe PoC Boundary Template is created or modified.

No Technical Due Diligence Summary is created or modified.

No Enterprise Review Guide is created or modified.

No customer PoC approval occurs.

No commercial contract creation occurs.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime behavior is modified.

No runtime execution approval occurs.

No scanner execution approval occurs.

No Docker execution approval occurs.

No credential injection approval occurs.

No customer target approval occurs.

No delivery approval occurs.

No certification claim occurs.

No legal compliance claim occurs.

No audit opinion claim occurs.

No production readiness claim occurs.

No external-framework equivalence claim occurs.

No diagnostic completeness claim occurs.

No third-party testing authorization claim occurs.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.156

v0.6.156 closed the Medium-risk Reviewer Walkthrough work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.153

v0.6.153 closed the Medium-risk Control Matrix work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.150

v0.6.150 closed the Medium-risk Safe PoC Boundary Template work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.147

v0.6.147 closed the Medium-risk Technical Due Diligence Summary work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.144

v0.6.144 closed the Medium-risk Enterprise Review Guide work item.

This checkpoint does not modify that completed work.

## Relationship to v0.6.120

v0.6.120 adopted risk-tiered checkpoint granularity.

This v0.6.157 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.158 External Review Package Integration Candidate
~~~

That checkpoint may create the candidate integration artifact and tests within the boundaries defined here.
