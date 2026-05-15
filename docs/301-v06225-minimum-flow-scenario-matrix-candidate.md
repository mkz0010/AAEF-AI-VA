# v0.6.225 Minimum Flow Scenario Matrix Candidate

Status: Candidate only

## Purpose

This checkpoint creates the Minimum Flow Scenario Matrix Candidate selected by v0.6.224.

v0.6.224 selected `minimum_flow_scenario_matrix` as the next high-risk work item after the accepted Existing Element Inventory.

This checkpoint records a candidate scenario matrix for the accepted AAEF Applied Evidence Minimum Flow.

This checkpoint does not accept the matrix, create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, move private generated outputs into the public repository, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Source decision

v0.6.224 selected the next work item:

- selected_next_work_item = minimum_flow_scenario_matrix
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.225 Minimum Flow Scenario Matrix Candidate
- selected_followup_checkpoint = v0.6.226 Minimum Flow Scenario Matrix Review and Decision

## Candidate status fields

- minimum_flow_scenario_matrix_candidate_recorded = true
- minimum_flow_scenario_matrix_accepted = false
- minimum_flow_package_created = false
- fixtures_created = false
- fixtures_modified = false
- evidence_linkage_records_created = false
- tool_action_request_records_created = false
- gate_decision_records_created = false
- dispatch_evidence_records_created = false
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

## Matrix purpose

The scenario matrix converts the accepted Existing Element Inventory into a scenario-level planning view.

The matrix answers:

- which scenario should be represented
- which minimum flow steps are needed
- which accepted inventory rows can inform the scenario
- which material is public-safe, sanitization-dependent, private-only, or patent-sensitive
- which gaps remain before package creation
- which maturity and evidence-boundary statements must be preserved

The matrix is not an evidence package.

The matrix is not a runtime demo.

The matrix is not a scanner-readiness claim.

## Scenario matrix classification model

Each scenario row uses these fields:

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
| required_followup | Work required if the matrix is accepted |
| maturity_boundary | What this scenario can and cannot imply |
| evidence_boundary_note | What the scenario evidence does and does not support |
| public_private_boundary_note | Public/private/patent-sensitive treatment |

## Minimum flow steps covered

The matrix candidate uses the accepted minimum flow:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

## Candidate scenario matrix

| scenario_id | scenario_name | scenario_purpose | minimum_flow_steps | accepted_inventory_rows_used | source_classification | public_surface_classification | current_coverage | required_followup | maturity_boundary | evidence_boundary_note | public_private_boundary_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCN-001 | permitted safe diagnostic | Show a low-risk diagnostic request permitted by a gate under controlled scope | model_output; tool_action_request; gate_decision; dispatch_decision; execution_result; evidence_event; reviewer_walkthrough | INV-001; INV-002; INV-003; INV-004; INV-005; INV-006; INV-016; INV-017 | mock flow; generated private run output; public sanitized example; validator or structural check | public-safe-after-sanitization | partially present | Create public-safe candidate records later and review mock/dry-run status wording before publication | Permitted mock flow does not imply live scanner execution, customer authorization, or production readiness | Evidence supports reconstruction of a controlled example only | Use sanitized/static records only; do not publish private generated outputs directly |
| SCN-002 | denied out-of-scope request | Show that an out-of-scope request is denied and not dispatched | model_output; tool_action_request; gate_decision; non_dispatch_decision; non_execution_result; evidence_event; reviewer_walkthrough | INV-001; INV-002; INV-003; INV-004; INV-006; INV-007; INV-008; INV-009; INV-017 | mock flow; generated private run output; documentation-only record; validator or structural check | public-safe-after-sanitization | partially present | Create explicit non-dispatch linkage and scenario-specific reviewer explanation later | Denied scenario does not prove legal truth or complete enforcement coverage | Evidence supports review of a non-dispatch path; it does not prove all bypasses are impossible | Public material may use sanitized non-dispatch examples and existing walkthrough text |
| SCN-003 | held / requires human approval | Show that a high-impact or uncertain request is held and not autonomously dispatched | model_output; tool_action_request; gate_decision; non_dispatch_decision; non_execution_result; evidence_event; reviewer_walkthrough | INV-001; INV-002; INV-010; INV-007; INV-008; INV-009; INV-015; INV-017 | mock flow; generated private run output; documentation-only record; validator or structural check | public-safe-after-sanitization | partially present | Create held-scenario wording and no-autonomous-dispatch reviewer note later | Held scenario does not mean human risk acceptance, customer delivery approval, or paid engagement approval | Evidence supports reconstruction that autonomous dispatch was held | Public record must avoid implying human approval was granted unless separately evidenced |
| SCN-004 | expired-not-executed | Show that stale, expired, missing, or blocked authorization/preflight conditions prevent dispatch | model_output; tool_action_request; gate_decision; non_dispatch_decision; non_execution_result; evidence_event; reviewer_walkthrough | INV-011; INV-012; INV-013; INV-014; INV-017 | runtime scaffold; validator or structural check; documentation-only record | public-safe-after-sanitization | planned | Create dedicated expired/not-executed public-safe fixture or sanitized record later if accepted | Expired/not-executed scaffold does not imply runtime execution or scanner readiness | Evidence should support reconstruction that dispatch did not occur because authorization/preflight was not valid | Avoid publishing private runtime scaffold outputs; use sanitized/static representation only |

## Scenario step coverage candidate

| scenario_id | model_output | tool_action_request | gate_decision | dispatch / non-dispatch | result | evidence_event | reviewer_walkthrough | coverage conclusion |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCN-001 | partially present | partially present | partially present | partially present | partially present | partially present | planned | Candidate can be built later with sanitized/static permitted path material. |
| SCN-002 | partially present | partially present | partially present | partially present | partially present | partially present | present | Candidate can be built later with explicit non-dispatch linkage. |
| SCN-003 | partially present | partially present | partially present | partially present | partially present | partially present | planned | Candidate can be built later with human-approval boundary wording. |
| SCN-004 | planned | planned | partially present | partially present | partially present | planned | planned | Candidate requires dedicated expired/not-executed representation later. |

## Linkage planning candidate

The future linkage table should include the following planned identifiers.

| scenario_id | model_output_id | tool_action_request_id | gate_decision_id | dispatch_or_non_dispatch_id | result_id | evidence_event_id | reviewer_walkthrough_id | five_questions_mapping_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SCN-001 | planned | planned | planned | planned | planned | planned | planned | planned |
| SCN-002 | planned | planned | planned | planned | planned | planned | planned | planned |
| SCN-003 | planned | planned | planned | planned | planned | planned | planned | planned |
| SCN-004 | planned | planned | planned | planned | planned | planned | planned | planned |

No evidence linkage records are created in v0.6.225.

No request, decision, dispatch, result, evidence, walkthrough, or five-questions mapping records are created in v0.6.225.

## Scenario-specific maturity notes

### SCN-001 permitted safe diagnostic

SCN-001 may use the existing allowed-action mock flow as planning input.

It must preserve these statements:

- permitted means gate-permitted in the controlled example
- permitted does not mean autonomous scanning is generally safe
- permitted does not authorize third-party targets
- permitted does not imply production readiness
- mock/dry-run output wording must not imply real scanner execution

### SCN-002 denied out-of-scope request

SCN-002 may use existing denied-action and blocked-review materials as planning input.

It must preserve these statements:

- denied means non-dispatch within the reviewed path
- denied does not prove all possible bypasses are impossible
- denied evidence supports reconstruction of the specific path only
- non-dispatch must be visible to the reviewer

### SCN-003 held / requires human approval

SCN-003 may use existing human-approval-required material as planning input.

It must preserve these statements:

- held means no autonomous dispatch
- held does not mean human risk acceptance has occurred
- held does not mean customer PoC approval
- held does not mean delivery approval
- human approval records must be explicit if later introduced

### SCN-004 expired-not-executed

SCN-004 may use authorization expiry, runtime readiness, execution-blocked, and preflight scaffold material as planning input.

It must preserve these statements:

- expired or stale authorization means no dispatch
- missing preflight evidence means no dispatch
- runtime scaffold is not runtime execution
- execution-blocked scaffold is not runtime readiness
- validator success is structural only

## AAEF five questions planning candidate

The future five-questions mapping should be scenario-specific.

| AAEF question | Scenario matrix treatment |
| --- | --- |
| Who or what acted? | Each scenario should identify AI request identity, gateway identity, and tool identity where applicable. |
| On whose behalf? | Each scenario should identify principal context and operator context where available. |
| With what authority? | Each scenario should identify gate decision, policy/rule version, and authorization scope. |
| Was it allowed at execution time? | Each scenario should identify dispatch or non-dispatch decision without overclaiming runtime readiness. |
| What evidence supports reconstruction? | Each scenario should identify the linked evidence event and reviewer walkthrough, using supports reconstruction rather than proves what happened. |

No AAEF five questions mapping content is created in v0.6.225.

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

## Public/private/patent-sensitive boundary notes retained

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

## Matrix risks

The scenario matrix candidate identifies these risks:

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

## Candidate follow-up if accepted

If this candidate is accepted in v0.6.226, the next likely work item is:

- evidence_linkage_table

The evidence linkage table should use the accepted scenario matrix to define planned links across request, decision, dispatch/non-dispatch, result, evidence, walkthrough, and five-questions mapping records.

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.225

v0.6.225 does not:

- accept the minimum flow scenario matrix
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

- the Minimum Flow Scenario Matrix Candidate is recorded
- scenario matrix classification model is recorded
- minimum flow steps are covered
- candidate scenario matrix is recorded
- scenario step coverage candidate is recorded
- linkage planning candidate is recorded
- scenario-specific maturity notes are recorded
- AAEF five questions planning candidate is recorded
- evidence-boundary notes are retained
- public/private/patent-sensitive boundary notes are retained
- matrix risks are recorded
- v0.6.226 is identified as the review and decision checkpoint
- the checkpoint states that no matrix is accepted in v0.6.225
- the checkpoint states that no minimum flow package, fixtures, evidence linkage records, Gateway behavior, runtime behavior, public cleanup, or README rewrite is applied in v0.6.225
- runtime demo remains necessary but deferred
- publication remains deferred
