# v0.6.226 Minimum Flow Scenario Matrix Review and Decision

Status: Accepted for evidence linkage planning; not applied

## Purpose

This checkpoint reviews the v0.6.225 `Minimum Flow Scenario Matrix Candidate`.

The decision is narrow: the candidate matrix is accepted as the Minimum Flow Scenario Matrix for future AAEF Applied Evidence Minimum Flow planning.

This checkpoint does not create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create execution result records, create non-execution result records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, move private generated outputs into the public repository, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Reviewed source

Reviewed candidate:

- v0.6.225 Minimum Flow Scenario Matrix Candidate

Source selection:

- v0.6.224 Next Work Selection Using Risk-Tiered Granularity

Accepted inventory context:

- v0.6.223 Existing Element Inventory Review and Decision

Accepted plan context:

- v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

## Decision

The v0.6.225 candidate matrix is accepted as the Minimum Flow Scenario Matrix for future evidence linkage planning.

Decision fields:

- minimum_flow_scenario_matrix_accepted = true
- minimum_flow_scenario_matrix_applied_to_package = false
- minimum_flow_package_created = false
- fixtures_created = false
- fixtures_modified = false
- evidence_linkage_records_created = false
- tool_action_request_records_created = false
- gate_decision_records_created = false
- dispatch_evidence_records_created = false
- execution_result_records_created = false
- non_execution_result_records_created = false
- reviewer_walkthrough_created = false
- aaef_five_questions_mapping_created = false
- aaef_handback_summary_created = false
- private_generated_outputs_moved_public = false
- public_exposure_cleanup_applied = false
- readme_front_page_rewritten = false
- gateway_core_safety_controls_implemented = false
- tool_gateway_behavior_changed = false
- adapter_behavior_changed = false
- execution_status_renamed = false
- schema_changed = false
- validator_behavior_changed = false
- fixture_semantics_changed = false
- runtime_behavior_changed = false
- scanner_behavior_changed = false
- runtime_demo_ready = false
- scanner_readiness_claim = false
- external_poc_readiness_claim = false
- publication_approval = false
- public_announcement = deferred
- social_post_publication = deferred
- commercial_terms_created = false
- production_readiness_claim = false
- certification_claim = false
- legal_compliance_claim = false
- audit_opinion_claim = false
- diagnostic_completeness_claim = false
- external_framework_equivalence_claim = false

## Accepted matrix classification model

The accepted scenario matrix uses these fields:

| Field | Meaning |
| --- | --- |
| scenario_id | Stable candidate identifier for the scenario |
| scenario_name | Human-readable scenario name |
| scenario_purpose | Why the scenario exists in the minimum flow |
| minimum_flow_steps | Minimum flow steps expected for the scenario |
| accepted_inventory_rows_used | Accepted inventory rows that may inform future package work |
| source_classification | static fixture, mock flow, generated private run output, public sanitized example, documentation-only record, runtime scaffold, validator or structural check |
| public_surface_classification | public-safe, public-safe-after-sanitization, private-not-in-git-only, patent-sensitive-private-only, or not-suitable-for-public-repository |
| current_coverage | present, partially present, planned, missing, unsafe_for_public_surface, or private_or_patent_sensitive_only |
| required_followup | Work required after matrix acceptance |
| maturity_boundary | What this scenario can and cannot imply |
| evidence_boundary_note | What the scenario evidence does and does not support |
| public_private_boundary_note | Public/private/patent-sensitive treatment |

## Accepted minimum flow steps

The accepted matrix covers the accepted minimum flow:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

The matrix is accepted as a planning matrix, not as proof that each flow step has an implemented public fixture or runtime record.

## Accepted scenarios

The accepted scenario matrix contains four scenarios:

| scenario_id | scenario_name | accepted purpose |
| --- | --- | --- |
| SCN-001 | permitted safe diagnostic | Show a low-risk diagnostic request permitted by a gate under controlled scope |
| SCN-002 | denied out-of-scope request | Show that an out-of-scope request is denied and not dispatched |
| SCN-003 | held / requires human approval | Show that a high-impact or uncertain request is held and not autonomously dispatched |
| SCN-004 | expired-not-executed | Show that stale, expired, missing, or blocked authorization/preflight conditions prevent dispatch |

## Accepted scenario coverage

| scenario_id | accepted coverage | accepted note |
| --- | --- | --- |
| SCN-001 | partially present | Candidate can be built later with sanitized/static permitted path material. |
| SCN-002 | partially present | Candidate can be built later with explicit non-dispatch linkage. |
| SCN-003 | partially present | Candidate can be built later with human-approval boundary wording. |
| SCN-004 | planned | Candidate requires dedicated expired/not-executed representation later. |

## Accepted scenario matrix rows

The accepted scenario matrix rows are the v0.6.225 candidate rows:

- SCN-001 permitted safe diagnostic
- SCN-002 denied out-of-scope request
- SCN-003 held / requires human approval
- SCN-004 expired-not-executed

The accepted matrix uses the v0.6.223 accepted inventory rows as planning inputs.

The accepted matrix does not move private generated outputs into the public repository.

The accepted matrix does not create public sanitized examples.

The accepted matrix does not create scenario fixture files.

## Accepted linkage planning requirement

The future evidence linkage table should define planned links for each scenario:

- scenario_id
- model_output_id
- tool_action_request_id
- gate_decision_id
- dispatch_decision_id or non_dispatch_decision_id
- execution_result_id or non_execution_result_id
- evidence_event_id
- reviewer_walkthrough_id
- five_questions_mapping_id

The accepted matrix records these linkage fields as planned.

No evidence linkage records are created in v0.6.226.

No request, decision, dispatch, result, evidence, walkthrough, or five-questions mapping records are created in v0.6.226.

## Accepted scenario-specific maturity notes

### SCN-001 permitted safe diagnostic

Accepted maturity boundary:

- permitted means gate-permitted in the controlled example
- permitted does not mean autonomous scanning is generally safe
- permitted does not authorize third-party targets
- permitted does not imply production readiness
- mock/dry-run output wording must not imply real scanner execution

### SCN-002 denied out-of-scope request

Accepted maturity boundary:

- denied means non-dispatch within the reviewed path
- denied does not prove all possible bypasses are impossible
- denied evidence supports reconstruction of the specific path only
- non-dispatch must be visible to the reviewer

### SCN-003 held / requires human approval

Accepted maturity boundary:

- held means no autonomous dispatch
- held does not mean human risk acceptance has occurred
- held does not mean customer PoC approval
- held does not mean delivery approval
- human approval records must be explicit if later introduced

### SCN-004 expired-not-executed

Accepted maturity boundary:

- expired or stale authorization means no dispatch
- missing preflight evidence means no dispatch
- runtime scaffold is not runtime execution
- execution-blocked scaffold is not runtime readiness
- validator success is structural only

## Accepted AAEF five questions planning requirement

Future AAEF five-questions mapping should be scenario-specific.

| AAEF question | Accepted matrix treatment |
| --- | --- |
| Who or what acted? | Each scenario should identify AI request identity, gateway identity, and tool identity where applicable. |
| On whose behalf? | Each scenario should identify principal context and operator context where available. |
| With what authority? | Each scenario should identify gate decision, policy/rule version, and authorization scope. |
| Was it allowed at execution time? | Each scenario should identify dispatch or non-dispatch decision without overclaiming runtime readiness. |
| What evidence supports reconstruction? | Each scenario should identify the linked evidence event and reviewer walkthrough, using supports reconstruction rather than proves what happened. |

No AAEF five questions mapping content is created in v0.6.226.

## Accepted evidence-boundary notes

This checkpoint accepts these boundary notes as future constraints:

- model output is not authority
- AI rationale is not authorization
- gate decision is not AI self-approval
- evidence supports reconstruction; it does not prove legal truth
- validator success is structural only
- runtime scaffold is not runtime readiness
- mock flow is not live scanner execution
- generated private run output is not public-safe by default
- public sanitized examples must not expose secrets, customer data, third-party targets, or patent-sensitive implementation detail
- compromised gateway reduces trust
- compromised evidence writer reduces trust
- compromised evidence store reduces trust

## Accepted public/private/patent-sensitive boundary notes

Public repository material may use:

- public-safe documentation records
- public-safe-after-sanitization static examples
- sanitized mock-flow summaries
- structural validator references
- reviewer-friendly explanations
- AAEF five questions mapping after separate review

Public repository material must not use:

- raw private generated output
- raw credentials or secrets
- customer data
- third-party target details
- live exploitation details
- patent-sensitive browser-state reconstruction detail
- DOM / HAR / screenshot / accessibility / event / storage / console integration detail
- pricing strategy
- customer lists
- NDA-dependent commercial material

Patent-sensitive material, if any, must remain outside public repository material and should be kept under `private-not-in-git/patent-prep/` when needed.

## Accepted matrix risks

The accepted matrix records these risks for future work:

- a permitted scenario can be overread as scanner readiness
- a denied scenario can be overread as proof that bypass is impossible
- a held scenario can be overread as human risk acceptance
- an expired-not-executed scenario can be overread as runtime enforcement readiness
- mock flow can be mistaken for live scanner execution
- generated private run output can be mistaken for public-safe evidence
- runtime scaffold can be mistaken for runtime readiness
- validator success can be mistaken for evidence sufficiency
- documentation-only material can be mistaken for implemented enforcement
- `completed` wording in mock/dry-run output may imply real execution
- public samples may be overread as diagnostic completeness

## Required follow-up

The accepted matrix makes the next likely work item:

- evidence_linkage_table

That work should use the accepted scenario matrix to define planned links across:

- request
- decision
- dispatch / non-dispatch
- result / non-result
- evidence event
- reviewer walkthrough
- AAEF five questions mapping

The evidence linkage table should remain a planning artifact unless separately approved to create records.

## Recommended next checkpoint

The recommended next checkpoint is:

- v0.6.227 Next Work Selection Using Risk-Tiered Granularity

That checkpoint should select the first work item after the accepted scenario matrix.

The expected work item is `evidence_linkage_table`, but final selection should be recorded in v0.6.227.

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.226

v0.6.226 does not:

- apply the matrix to create a minimum flow package
- create the minimum flow package
- create new fixtures
- modify existing fixtures
- create evidence linkage records
- create tool_action_request records
- create gate_decision records
- create dispatch or non-dispatch evidence records
- create execution result records
- create non-execution result records
- create reviewer walkthrough content
- create AAEF five questions mapping content
- create an AAEF handback summary
- move private generated outputs into the public repository
- publish private-not-in-git material
- expose patent-sensitive detail
- remove public contact routes
- move pricing materials
- move business-plan materials
- rewrite the README front page
- delete historical docs
- create a curated documentation index
- create a mock execution recording
- create a runtime demo
- create an executable demo
- implement Gateway core safety controls
- change Tool Gateway behavior
- change adapter behavior
- rename execution statuses
- change execution result schemas
- change evidence schemas
- change validator behavior
- change fixture semantics
- apply runtime changes
- approve scanner readiness
- authorize real scanner execution
- authorize external PoC intake
- publish a public announcement
- approve a social post
- create a release announcement
- create AAEF main publication material
- create an AAEF main issue, PR, command, or URL
- create commercial contract terms
- create paid engagement approval
- create external-specific material
- promote this project into AAEF Core, Profile, or Practical Package

## Runtime demo position retained

Runtime demo remains necessary but deferred.

The project should not advance to closed runtime demo readiness until Gateway core safety integration, public exposure hygiene, and AAEF applied evidence minimum flow have each been planned and reviewed.

## Publication boundary retained

Publication remains deferred.

This review-and-decision checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This review-and-decision checkpoint is accepted when:

- the v0.6.225 Minimum Flow Scenario Matrix Candidate is reviewed
- the matrix is accepted for future evidence linkage planning
- accepted matrix classification model is recorded
- accepted minimum flow steps are recorded
- accepted scenarios are recorded
- accepted scenario coverage is recorded
- accepted scenario matrix rows are recorded
- accepted linkage planning requirement is recorded
- accepted scenario-specific maturity notes are recorded
- accepted AAEF five questions planning requirement is recorded
- accepted evidence-boundary notes are recorded
- accepted public/private/patent-sensitive boundary notes are recorded
- accepted matrix risks are recorded
- v0.6.227 is identified as the next recommended checkpoint
- the checkpoint states that no minimum flow package, fixtures, evidence linkage records, Gateway behavior, runtime behavior, public cleanup, or README rewrite is applied in v0.6.226
- runtime demo remains necessary but deferred
- publication remains deferred
