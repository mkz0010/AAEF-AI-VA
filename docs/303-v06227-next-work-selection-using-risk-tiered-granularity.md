# v0.6.227 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.226 using risk-tiered granularity.

v0.6.226 accepted the Minimum Flow Scenario Matrix for future evidence linkage planning.

v0.6.227 selects the next concrete work item after the accepted scenario matrix.

This checkpoint does not create the evidence linkage table, create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create execution result records, create non-execution result records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, move private generated outputs into the public repository, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.226.

v0.6.226 accepted the Minimum Flow Scenario Matrix for future evidence linkage planning only.

The following boundaries remain in force:

- evidence linkage table is not created in this checkpoint
- minimum flow package is not created in this checkpoint
- fixtures are not created or modified in this checkpoint
- evidence linkage records are not created in this checkpoint
- `tool_action_request` records are not created in this checkpoint
- `gate_decision` records are not created in this checkpoint
- dispatch or non-dispatch evidence records are not created in this checkpoint
- execution result records are not created in this checkpoint
- non-execution result records are not created in this checkpoint
- reviewer walkthrough content is not created in this checkpoint
- AAEF five questions mapping content is not created in this checkpoint
- AAEF handback summary is not created in this checkpoint
- private generated outputs are not moved public in this checkpoint
- public exposure cleanup is not applied in this checkpoint
- README front page is not rewritten in this checkpoint
- Tool Gateway behavior is not changed in this checkpoint
- adapter behavior is not changed in this checkpoint
- execution statuses are not renamed in this checkpoint
- schemas are not changed in this checkpoint
- validator behavior is not changed in this checkpoint
- fixture semantics are not changed in this checkpoint
- runtime behavior is not changed in this checkpoint
- scanner behavior is not changed in this checkpoint
- runtime demo remains necessary but deferred
- publication remains deferred
- no scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence is claimed

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = evidence_linkage_table
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.228 Evidence Linkage Table Candidate
- selected_followup_checkpoint = v0.6.229 Evidence Linkage Table Review and Decision

## Why this work item is selected

The accepted Minimum Flow Scenario Matrix defines the four required scenarios:

- SCN-001 permitted safe diagnostic
- SCN-002 denied out-of-scope request
- SCN-003 held / requires human approval
- SCN-004 expired-not-executed

The next safe step is to plan an evidence linkage table that connects each scenario to the accepted minimum flow:

- model_output
- tool_action_request
- gate_decision
- dispatch_decision / non_dispatch_decision
- execution_result / non_execution_result
- evidence_event
- reviewer_walkthrough
- AAEF five questions mapping

This must happen before creating any package fixture, evidence record, request record, decision record, dispatch record, reviewer walkthrough, AAEF five questions mapping, or handback summary.

## Why the risk tier is high

This work is high-risk because linkage wording can overstate evidence maturity.

The evidence linkage table could incorrectly imply that:

- planned IDs are already implemented records
- private generated outputs are public-safe
- mock flow is live scanner execution
- static fixture is runtime behavior
- runtime scaffold is runtime readiness
- validator success is evidence sufficiency
- evidence events prove legal truth
- scenario coverage means diagnostic completeness
- reviewer walkthrough means audit sufficiency

The linkage table must distinguish:

- existing record
- planned record
- public-safe record
- public-safe-after-sanitization record
- private-not-in-git-only record
- patent-sensitive-private-only record
- not-suitable-for-public-repository record

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.228 creates the Evidence Linkage Table Candidate.
2. v0.6.229 reviews the Evidence Linkage Table Candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before the linkage table is treated as accepted.

## Required v0.6.228 candidate scope

The v0.6.228 candidate should create a candidate evidence linkage table for the four accepted scenarios:

- SCN-001 permitted safe diagnostic
- SCN-002 denied out-of-scope request
- SCN-003 held / requires human approval
- SCN-004 expired-not-executed

For each scenario, the candidate should define planned link fields:

- scenario_id
- model_output_id
- tool_action_request_id
- gate_decision_id
- dispatch_decision_id or non_dispatch_decision_id
- execution_result_id or non_execution_result_id
- evidence_event_id
- reviewer_walkthrough_id
- five_questions_mapping_id

The candidate should also define per-link metadata fields:

- link_status
- source_status
- source_classification
- public_surface_classification
- maturity_boundary
- evidence_boundary_note
- required_followup

The candidate must not create actual fixture records, evidence linkage records, request records, decision records, dispatch records, result records, walkthrough records, mapping records, or handback records.

## Required v0.6.228 link status model

The candidate should distinguish the following link statuses:

- existing_public_safe
- existing_public_safe_after_sanitization
- existing_private_not_in_git_only
- planned_public_safe
- planned_public_safe_after_sanitization
- planned_private_only
- patent_sensitive_excluded
- not_suitable_for_public_repository
- missing

The candidate should not use link status wording that implies evidence sufficiency, audit sufficiency, legal proof, runtime readiness, production readiness, scanner readiness, or diagnostic completeness.

## Required v0.6.228 scenario linkage expectations

### SCN-001 permitted safe diagnostic

The candidate should plan links for a permitted safe diagnostic path.

It must preserve:

- permitted means gate-permitted in the controlled example
- permitted does not mean autonomous scanning is generally safe
- permitted does not authorize third-party targets
- permitted does not imply production readiness
- mock/dry-run output wording must not imply real scanner execution

### SCN-002 denied out-of-scope request

The candidate should plan links for a denied and non-dispatched path.

It must preserve:

- denied means non-dispatch within the reviewed path
- denied does not prove all possible bypasses are impossible
- denied evidence supports reconstruction of the specific path only
- non-dispatch must be visible to the reviewer

### SCN-003 held / requires human approval

The candidate should plan links for a held path where autonomous dispatch does not occur.

It must preserve:

- held means no autonomous dispatch
- held does not mean human risk acceptance has occurred
- held does not mean customer PoC approval
- held does not mean delivery approval
- human approval records must be explicit if later introduced

### SCN-004 expired-not-executed

The candidate should plan links for an expired or not-executed path.

It must preserve:

- expired or stale authorization means no dispatch
- missing preflight evidence means no dispatch
- runtime scaffold is not runtime execution
- execution-blocked scaffold is not runtime readiness
- validator success is structural only

## Required v0.6.228 public/private boundary review

The candidate linkage table should mark whether each link can be built from material that is:

- public-safe
- public-safe-after-sanitization
- private-not-in-git-only
- patent-sensitive-private-only
- not suitable for public repository use

The candidate must not move files or publish private material in v0.6.228.

## Required v0.6.228 evidence-boundary review

The candidate linkage table must retain these statements:

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

## Required v0.6.228 output posture

The candidate evidence linkage table should be a planning artifact.

It should not:

- create JSON evidence package files
- create scenario fixture files
- create request / decision / dispatch / result records
- create reviewer walkthrough content
- create AAEF five questions mapping content
- move generated outputs public
- change Tool Gateway behavior
- claim runtime demo readiness
- claim scanner readiness
- claim production readiness
- approve publication

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.227

v0.6.227 does not:

- create the evidence linkage table
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

This direction-selection checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This checkpoint is accepted when:

- the selected next work item is explicitly recorded
- the selected risk tier is recorded as high
- the two-checkpoint split is recorded
- v0.6.228 is identified as the candidate checkpoint
- v0.6.229 is identified as the review and decision checkpoint
- the v0.6.228 required candidate scope is recorded
- link status model is required
- scenario linkage expectations are recorded
- public/private boundary review is required
- evidence-boundary review is required
- public exposure cleanup remains deferred, not rejected
- mock/dry-run completed status terminology cleanup remains deferred, not rejected
- the checkpoint states that no evidence linkage table is created in v0.6.227
- the checkpoint states that no fixtures, runtime behavior, Gateway behavior, public cleanup, or README rewrite is applied in v0.6.227
- runtime demo remains necessary but deferred
- publication remains deferred
