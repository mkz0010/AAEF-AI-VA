# v0.6.228 Evidence Linkage Table Candidate

Status: Candidate only

## Purpose

This checkpoint creates the Evidence Linkage Table Candidate selected by v0.6.227.

v0.6.227 selected `evidence_linkage_table` as the next high-risk work item after the accepted Minimum Flow Scenario Matrix.

This checkpoint records a candidate linkage table for the accepted AAEF Applied Evidence Minimum Flow scenarios.

This checkpoint does not accept the linkage table, create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create execution result records, create non-execution result records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, move private generated outputs into the public repository, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Source decision

v0.6.227 selected the next work item:

- selected_next_work_item = evidence_linkage_table
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.228 Evidence Linkage Table Candidate
- selected_followup_checkpoint = v0.6.229 Evidence Linkage Table Review and Decision

## Candidate status fields

- evidence_linkage_table_candidate_recorded = true
- evidence_linkage_table_accepted = false
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
- runtime_behavior_changed = false
- scanner_behavior_changed = false
- runtime_demo_ready = false
- publication_approval = false

## Linkage table purpose

The linkage table candidate converts the accepted Minimum Flow Scenario Matrix into planned evidence links.

The table answers:

- which scenario is represented
- which minimum flow IDs must be linked
- whether each link is existing, planned, private-only, public-safe, sanitization-dependent, patent-sensitive, or missing
- which maturity boundary applies to the link
- which evidence-boundary statement must be preserved
- what follow-up work is required before package creation

The linkage table is not an evidence package.

The linkage table is not runtime execution.

The linkage table is not scanner readiness.

## Required execution / non-execution result link token

The linkage table uses `result_or_non_result_id` as the compact row field name, and it corresponds to `execution_result_id or non_execution_result_id` in the accepted minimum flow terminology.

## Linkage classification model

Each candidate row uses these fields:

| Field | Meaning |
| --- | --- |
| linkage_id | Stable candidate identifier for the linkage row |
| scenario_id | Accepted scenario identifier |
| scenario_name | Accepted scenario name |
| model_output_id | Planned or existing model output link |
| tool_action_request_id | Planned or existing tool action request link |
| gate_decision_id | Planned or existing gate decision link |
| dispatch_or_non_dispatch_id | Planned or existing dispatch / non-dispatch link |
| result_or_non_result_id | Planned or existing execution result / non-execution result link |
| evidence_event_id | Planned or existing evidence event link |
| reviewer_walkthrough_id | Planned or existing reviewer walkthrough link |
| five_questions_mapping_id | Planned or existing AAEF five questions mapping link |
| link_status | Link maturity and public-surface status |
| source_status | Whether the source is existing, planned, private-only, excluded, or missing |
| source_classification | static fixture, mock flow, generated private run output, public sanitized example, documentation-only record, runtime scaffold, validator or structural check |
| public_surface_classification | public-safe, public-safe-after-sanitization, private-not-in-git-only, patent-sensitive-private-only, or not-suitable-for-public-repository |
| maturity_boundary | What this link can and cannot imply |
| evidence_boundary_note | What the linked evidence supports and does not prove |
| required_followup | Work required if the linkage table is accepted |

## Link status model

The candidate uses the following link status model:

- existing_public_safe
- existing_public_safe_after_sanitization
- existing_private_not_in_git_only
- planned_public_safe
- planned_public_safe_after_sanitization
- planned_private_only
- patent_sensitive_excluded
- not_suitable_for_public_repository
- missing

The link status model must not imply evidence sufficiency, audit sufficiency, legal proof, runtime readiness, production readiness, scanner readiness, or diagnostic completeness.

## Candidate evidence linkage table

| linkage_id | scenario_id | scenario_name | model_output_id | tool_action_request_id | gate_decision_id | dispatch_or_non_dispatch_id | result_or_non_result_id | evidence_event_id | reviewer_walkthrough_id | five_questions_mapping_id | link_status | source_status | source_classification | public_surface_classification | maturity_boundary | evidence_boundary_note | required_followup |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LNK-001 | SCN-001 | permitted safe diagnostic | planned:SCN-001-MODEL-OUTPUT | planned:SCN-001-REQUEST | planned:SCN-001-GATE-DECISION | planned:SCN-001-DISPATCH | planned:SCN-001-EXECUTION-RESULT | planned:SCN-001-EVIDENCE-EVENT | planned:SCN-001-WALKTHROUGH | planned:SCN-001-FIVE-QUESTIONS | planned_public_safe_after_sanitization | planned | mock flow; generated private run output; public sanitized example | public-safe-after-sanitization | Permitted mock flow does not imply live scanner execution, third-party authorization, or production readiness. | Evidence supports reconstruction of a controlled permitted example only. | Create public-safe candidate records later and review mock/dry-run status wording. |
| LNK-002 | SCN-002 | denied out-of-scope request | planned:SCN-002-MODEL-OUTPUT | planned:SCN-002-REQUEST | planned:SCN-002-GATE-DECISION | planned:SCN-002-NON-DISPATCH | planned:SCN-002-NON-EXECUTION-RESULT | planned:SCN-002-EVIDENCE-EVENT | planned:SCN-002-WALKTHROUGH | planned:SCN-002-FIVE-QUESTIONS | planned_public_safe_after_sanitization | planned | mock flow; generated private run output; documentation-only record | public-safe-after-sanitization | Denied scenario records non-dispatch in the reviewed path; it does not prove all bypasses are impossible. | Evidence supports reconstruction of a specific denied path only. | Create explicit non-dispatch linkage and scenario-specific reviewer explanation later. |
| LNK-003 | SCN-003 | held / requires human approval | planned:SCN-003-MODEL-OUTPUT | planned:SCN-003-REQUEST | planned:SCN-003-GATE-DECISION | planned:SCN-003-NON-DISPATCH | planned:SCN-003-NON-EXECUTION-RESULT | planned:SCN-003-EVIDENCE-EVENT | planned:SCN-003-WALKTHROUGH | planned:SCN-003-FIVE-QUESTIONS | planned_public_safe_after_sanitization | planned | mock flow; generated private run output; documentation-only record | public-safe-after-sanitization | Held means no autonomous dispatch; it does not mean human risk acceptance, PoC approval, or delivery approval. | Evidence supports reconstruction that autonomous dispatch was held. | Create held-scenario wording and no-autonomous-dispatch reviewer note later. |
| LNK-004 | SCN-004 | expired-not-executed | planned:SCN-004-MODEL-OUTPUT | planned:SCN-004-REQUEST | planned:SCN-004-GATE-DECISION | planned:SCN-004-NON-DISPATCH | planned:SCN-004-NON-EXECUTION-RESULT | planned:SCN-004-EVIDENCE-EVENT | planned:SCN-004-WALKTHROUGH | planned:SCN-004-FIVE-QUESTIONS | planned_public_safe_after_sanitization | planned | runtime scaffold; validator or structural check; documentation-only record | public-safe-after-sanitization | Expired/not-executed scaffold does not imply runtime execution or scanner readiness. | Evidence should support reconstruction that dispatch did not occur because authorization/preflight was not valid. | Create dedicated expired/not-executed public-safe fixture or sanitized record later if accepted. |

## Minimum flow link coverage candidate

| scenario_id | model_output | tool_action_request | gate_decision | dispatch / non-dispatch | result / non-result | evidence_event | reviewer_walkthrough | five_questions_mapping | coverage conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCN-001 | planned | planned | planned | planned dispatch | planned execution result | planned | planned | planned | Linkage can be planned from permitted-path materials but package records are not created. |
| SCN-002 | planned | planned | planned | planned non-dispatch | planned non-execution result | planned | planned | planned | Linkage can be planned from denied/non-dispatch materials but package records are not created. |
| SCN-003 | planned | planned | planned | planned non-dispatch | planned non-execution result | planned | planned | planned | Linkage can be planned from held/human-approval materials but package records are not created. |
| SCN-004 | planned | planned | planned | planned non-dispatch | planned non-execution result | planned | planned | planned | Linkage requires dedicated expired/not-executed representation later. |

## Scenario linkage expectations

### SCN-001 permitted safe diagnostic

SCN-001 linkage must show a permitted safe diagnostic path.

It must preserve:

- permitted means gate-permitted in the controlled example
- permitted does not mean autonomous scanning is generally safe
- permitted does not authorize third-party targets
- permitted does not imply production readiness
- mock/dry-run output wording must not imply real scanner execution

### SCN-002 denied out-of-scope request

SCN-002 linkage must show a denied and non-dispatched path.

It must preserve:

- denied means non-dispatch within the reviewed path
- denied does not prove all possible bypasses are impossible
- denied evidence supports reconstruction of the specific path only
- non-dispatch must be visible to the reviewer

### SCN-003 held / requires human approval

SCN-003 linkage must show a held path where autonomous dispatch does not occur.

It must preserve:

- held means no autonomous dispatch
- held does not mean human risk acceptance has occurred
- held does not mean customer PoC approval
- held does not mean delivery approval
- human approval records must be explicit if later introduced

### SCN-004 expired-not-executed

SCN-004 linkage must show an expired or not-executed path.

It must preserve:

- expired or stale authorization means no dispatch
- missing preflight evidence means no dispatch
- runtime scaffold is not runtime execution
- execution-blocked scaffold is not runtime readiness
- validator success is structural only

## AAEF five questions linkage candidate

The future AAEF five-questions mapping should link from each scenario row.

| AAEF question | Linkage table treatment |
| --- | --- |
| Who or what acted? | Link to model_output_id, tool_action_request_id, gateway identity, and tool identity where applicable. |
| On whose behalf? | Link to principal context and operator context where available. |
| With what authority? | Link to gate_decision_id, policy/rule version, and authorization scope. |
| Was it allowed at execution time? | Link to dispatch_decision_id or non_dispatch_decision_id without overclaiming runtime readiness. |
| What evidence supports reconstruction? | Link to evidence_event_id and reviewer_walkthrough_id, using supports reconstruction rather than proves what happened. |

No AAEF five questions mapping content is created in v0.6.228.

## Public/private/patent-sensitive linkage notes

Public repository material may use:

- public-safe documentation records
- public-safe-after-sanitization static examples
- sanitized mock-flow summaries
- structural validator references
- reviewer-friendly explanations
- future AAEF five questions mapping after separate review

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

## Evidence-boundary notes retained

This checkpoint retains these boundary notes:

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

## Linkage risks

The evidence linkage table candidate identifies these risks:

- planned IDs can be mistaken for existing records
- a linkage table can be mistaken for an evidence package
- a permitted linkage row can be overread as scanner readiness
- a denied linkage row can be overread as proof that bypass is impossible
- a held linkage row can be overread as human risk acceptance
- an expired-not-executed linkage row can be overread as runtime enforcement readiness
- generated private run output can be mistaken for public-safe evidence
- mock flow can be mistaken for live scanner execution
- runtime scaffold can be mistaken for runtime readiness
- validator success can be mistaken for evidence sufficiency
- documentation-only material can be mistaken for implemented enforcement
- public samples may be overread as diagnostic completeness

## Candidate follow-up if accepted

If this candidate is accepted in v0.6.229, the next likely work item is:

- tool_action_request_gate_decision_dispatch_evidence_package

That future work should decide whether to create public-safe records or documentation packages for request, decision, dispatch/non-dispatch, result/non-result, evidence event, reviewer walkthrough, and AAEF five questions mapping.

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.228

v0.6.228 does not:

- accept the evidence linkage table
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

This candidate checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This candidate checkpoint is accepted when:

- the Evidence Linkage Table Candidate is recorded
- linkage classification model is recorded
- link status model is recorded
- candidate evidence linkage table is recorded
- minimum flow link coverage candidate is recorded
- scenario linkage expectations are recorded
- AAEF five questions linkage candidate is recorded
- public/private/patent-sensitive linkage notes are retained
- evidence-boundary notes are retained
- linkage risks are recorded
- v0.6.229 is identified as the review and decision checkpoint
- the checkpoint states that no linkage table is accepted in v0.6.228
- the checkpoint states that no minimum flow package, fixtures, evidence linkage records, Gateway behavior, runtime behavior, public cleanup, or README rewrite is applied in v0.6.228
- runtime demo remains necessary but deferred
- publication remains deferred
