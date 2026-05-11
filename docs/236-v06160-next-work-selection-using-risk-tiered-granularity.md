# v0.6.160 Next Work Selection Using Risk-Tiered Granularity

Status: decision
Date: 2026-05-11

## Purpose

This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.

This checkpoint is intentionally completed as one Low-risk checkpoint.

It selects the next AAEF-AI-VA work item after v0.6.159 closed the External Review Package Integration work item.

## Decision

The selected next work item is Public Review Entry Point Polish.

The selected next work item risk tier is Medium risk.

The selected checkpoint count is 2 checkpoints.

The next checkpoint is v0.6.161 Public Review Entry Point Polish Candidate.

This checkpoint does not modify the README public entry point.

This checkpoint does not modify runtime behavior.

This checkpoint does not reopen the AAEF main handback sequence.

## Risk-tiered selection record

~~~text
next_work_selection_using_risk_tiered_granularity_v06160_completed = true
next_work_selection_v06160_is_documentation_only = true
next_work_selection_v06160_uses_v06120_granularity_policy = true
next_work_selection_v06160_uses_v06159_completed_work_item = true
v06160_completed_as_low_risk_one_checkpoint = true
selected_next_work_item = public_review_entry_point_polish
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
selected_next_checkpoint = v0.6.161 Public Review Entry Point Polish Candidate
public_review_entry_point_polish_selected = true
external_review_package_integration_work_item_closed = true
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
public_review_entry_point_created = false
public_review_entry_point_modified = false
readme_public_entry_modified = false
external_review_package_modified = false
reviewer_walkthrough_modified = false
control_matrix_modified = false
safe_poc_boundary_template_modified = false
technical_due_diligence_summary_modified = false
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
| Public Review Entry Point Polish | Medium | yes | External Review Package Integration is now accepted. The public entry points should make the review package discoverable and clearly non-authorizing without implying customer PoC approval, commercial agreement, production readiness, or runtime capability. |
| Buyer-facing commercial inquiry boundary | Medium | no | Useful soon, but commercial inquiry language should follow public review entry clarity so commercial readers first encounter the non-authorizing package boundary. |
| AAEF main handback reconsideration | Medium or High | no | The v0.6.119 handback sequence remains paused. A public-safe AAEF main handback should wait until applied-implementation lessons are consolidated into narrow evidence/interface lessons. |
| Customer PoC package | High | no | A customer PoC package would be closer to commercial or target-specific activity and should not precede public review entry clarity. |
| Runtime execution preparation | High or Critical | no | Runtime/scanner/customer-target activity remains outside the current safe direction and would require a larger risk split. |

## Selected work item

~~~text
selected_next_work_item = public_review_entry_point_polish
selected_next_work_item_risk_tier = medium
selected_next_work_item_checkpoint_count = 2
selected_next_work_item_first_checkpoint = candidate_implementation
selected_next_work_item_second_checkpoint = review_and_decision
~~~

The purpose of the selected work item is to make the public review package easier to discover from the repository front page and related public-facing navigation points.

The work should connect README positioning, External Review Package, Reviewer Walkthrough, Control Matrix, Technical Due Diligence Summary, Enterprise Review Guide, Safe PoC Boundary Template, non-authorizing interpretation limits, and conservative claim boundaries.

It should not create runtime approval, customer PoC approval, customer delivery approval, legal/compliance claims, audit claims, certification claims, production readiness claims, diagnostic-completeness claims, or external-framework equivalence claims.

## Why this is Medium risk

The selected work item is documentation-oriented and should not modify runtime code, gate behavior, validators, schemas, public samples, scanners, Docker execution, credential handling, customer targets, or delivery authorization.

However, front-page and public-entry wording can strongly influence external interpretation. Poor wording could make the repository look like a production scanner, customer PoC package, commercial offer, audit/certification package, or deployment-ready system.

Therefore, it is Medium risk and should use two checkpoints.

## Why not High or Critical risk

This work item should not change enforcement behavior, fail-closed logic, runtime execution, scanner execution, Docker/lab execution, credential injection, customer target handling, delivery authorization, customer PoC authorization, or external submission.

It does not create a live PoC, contract, authorization record, runtime gate integration, scanner runbook, customer delivery artifact, or AAEF main handback submission.

Therefore, the High-risk three-checkpoint pattern and Critical-risk four-to-five-checkpoint pattern are not required unless later scope expands.

## Why not Low risk

This work item is not only a direction-selection note.

It will likely modify public-facing repository navigation and README wording, which may influence how external reviewers, buyers, sponsors, maintainers, and commercial readers interpret the project.

Therefore, it should not be completed in one checkpoint.

## Planned checkpoint split

The selected work item should use the Medium-risk two-checkpoint pattern:

~~~text
v0.6.161 Public Review Entry Point Polish Candidate
v0.6.162 Public Review Entry Point Polish Review and Decision
~~~

v0.6.161 should create the candidate navigation/README polish and tests. The changes should remain claim-safe, non-authorizing, and aligned with the External Review Package, Reviewer Walkthrough, Control Matrix, Technical Due Diligence Summary, Enterprise Review Guide, and Safe PoC Boundary Template.

v0.6.162 should review the public entry point changes, confirm claim boundaries, and decide whether to close the work item.

## Expected Public Review Entry Point Polish scope

The candidate should likely include:

* a clear public-review entry path in README,
* an explicit pointer to `docs/external-review-package.md`,
* a brief explanation of who should read the package,
* a public-facing non-authorizing notice,
* links to key reviewer artifacts,
* a safe order for external review,
* a statement that customer PoC, commercial terms, runtime/scanner execution, and delivery require separate authorization,
* claim-boundary language preventing certification, audit, legal compliance, production readiness, diagnostic-completeness, and external-framework equivalence interpretations,
* tests verifying the public-entry language and absence of forbidden claims.

The work should help reviewers find the package, not operate a scanner, approve testing, approve delivery, or create a commercial contract.

## Claim boundaries for the selected work

The Public Review Entry Point Polish candidate must not claim:

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

The polish may help reviewers navigate the current AAEF-AI-VA public review package and evidence-boundary materials.

## What did not happen

No public review entry point is created or modified in this checkpoint.

No README public entry is modified in this checkpoint.

No External Review Package is modified.

No Reviewer Walkthrough is modified.

No Control Matrix is modified.

No Safe PoC Boundary Template is modified.

No Technical Due Diligence Summary is modified.

No Enterprise Review Guide is modified.

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

## Relationship to v0.6.159

v0.6.159 closed the Medium-risk External Review Package Integration work item.

This checkpoint selects the next work item after that closeout.

## Relationship to v0.6.156

v0.6.156 closed the Medium-risk Reviewer Walkthrough work item.

This checkpoint does not modify that completed work.

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

This v0.6.160 checkpoint applies that policy by completing a Low-risk direction-selection decision in one checkpoint and assigning the selected follow-up work to Medium risk with two checkpoints.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## Next direction

Proceed to:

~~~text
v0.6.161 Public Review Entry Point Polish Candidate
~~~

That checkpoint may create the candidate public review entry point polish and tests within the boundaries defined here.
