# v0.6.224 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.223 using risk-tiered granularity.

v0.6.223 accepted the Existing Element Inventory for future AAEF Applied Evidence Minimum Flow planning.

v0.6.224 selects the next concrete work item after the accepted inventory.

This checkpoint does not create the minimum flow scenario matrix, create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, move private generated outputs into the public repository, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.223.

v0.6.223 accepted the Existing Element Inventory for future minimum flow planning only.

The following boundaries remain in force:

- minimum flow scenario matrix is not created in this checkpoint
- minimum flow package is not created in this checkpoint
- fixtures are not created or modified in this checkpoint
- evidence linkage records are not created in this checkpoint
- `tool_action_request` records are not created in this checkpoint
- `gate_decision` records are not created in this checkpoint
- dispatch or non-dispatch evidence records are not created in this checkpoint
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

- selected_next_work_item = minimum_flow_scenario_matrix
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.225 Minimum Flow Scenario Matrix Candidate
- selected_followup_checkpoint = v0.6.226 Minimum Flow Scenario Matrix Review and Decision

## Why this work item is selected

The accepted Existing Element Inventory identified partially present coverage for the minimum flow and the four required scenarios.

The next safe step is to convert the accepted inventory into a scenario matrix candidate that defines how the minimum flow should be represented across:

- permitted safe diagnostic
- denied out-of-scope request
- held / requires human approval
- expired-not-executed

This must happen before creating any new fixture, evidence linkage table, request/decision/dispatch record, reviewer walkthrough, AAEF five questions mapping, or handback summary.

## Why the risk tier is high

This work is high-risk because scenario wording can easily overstate maturity.

The scenario matrix could incorrectly imply that:

- mock flow is live scanner execution
- static fixture is runtime behavior
- generated private run output is public-safe
- runtime scaffold is runtime readiness
- validator success is evidence sufficiency
- documentation-only material is implemented enforcement
- non-dispatch records are proof of legal truth
- public samples demonstrate diagnostic completeness

The matrix must preserve the distinction between:

- static fixture
- mock flow
- generated private run output
- public sanitized example
- documentation-only record
- runtime scaffold
- validator or structural check

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.225 creates the Minimum Flow Scenario Matrix Candidate.
2. v0.6.226 reviews the Minimum Flow Scenario Matrix Candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before the scenario matrix is treated as accepted.

## Required v0.6.225 candidate scope

The v0.6.225 candidate should create a candidate matrix for the four required scenarios:

- permitted safe diagnostic
- denied out-of-scope request
- held / requires human approval
- expired-not-executed

For each scenario, the candidate should identify:

- scenario_id
- scenario_name
- scenario_purpose
- expected_minimum_flow_steps
- accepted_inventory_rows_used
- source_classification
- public_surface_classification
- current_coverage
- required_followup
- maturity_boundary
- evidence_boundary_note
- public/private/patent-sensitive boundary note

The candidate must not create actual fixture records, evidence linkage records, request records, decision records, dispatch records, walkthrough records, mapping records, or handback records.

## Required v0.6.225 minimum flow coverage

The candidate matrix should cover the accepted minimum flow steps:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

The candidate should identify which steps are already partially represented by accepted inventory rows and which steps require future public-safe fixture or documentation work.

## Required v0.6.225 scenario expectations

### permitted safe diagnostic

The candidate should define a safe permitted path where a low-risk diagnostic request is permitted under gate control.

It must avoid implying production scanner readiness.

It should identify whether existing allowed-action mock flow and generated outputs can inform later public-safe representation.

### denied out-of-scope request

The candidate should define a denial path where an out-of-scope request is denied and not dispatched.

It should identify existing denied-action mock flow, non-dispatch evidence, blocked reasons, evidence chain, reconstruction report, and reviewer walkthrough materials.

It must make non-dispatch clear.

### held / requires human approval

The candidate should define a held path where a high-impact or uncertain request requires human approval and is not autonomously dispatched.

It should identify existing human-approval-required mock flow and human approval gate outputs.

It must avoid implying that human review has accepted risk or approved customer delivery.

### expired-not-executed

The candidate should define an expired or non-executed path where a request is not dispatched because authorization or preflight conditions are stale, expired, missing, or blocked.

It should identify existing authorization expiry helper, runtime readiness scaffold, execution-blocked scaffold, and preflight evidence scaffold materials.

It must avoid implying runtime execution or scanner readiness.

## Required v0.6.225 linkage planning

For each scenario, the candidate matrix should plan links for:

- model_output_id
- tool_action_request_id
- gate_decision_id
- dispatch_decision_id or non_dispatch_decision_id
- execution_result_id or non_execution_result_id
- evidence_event_id
- reviewer_walkthrough_id
- five_questions_mapping_id

The candidate matrix must distinguish existing records from planned records.

## Required v0.6.225 evidence-boundary review

The candidate matrix must retain these statements:

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

## Required v0.6.225 public/private boundary review

The candidate matrix should mark whether each scenario can be built from material that is:

- public-safe
- public-safe-after-sanitization
- private-not-in-git-only
- patent-sensitive-private-only
- not suitable for public repository use

The candidate must not move files or publish private material in v0.6.225.

## Required v0.6.225 output posture

The candidate matrix should be a planning artifact.

It should not:

- create scenario fixture files
- create JSON evidence package files
- create sanitized public examples
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

## Explicit non-goals for v0.6.224

v0.6.224 does not:

- create the minimum flow scenario matrix
- create the minimum flow package
- create new fixtures
- modify existing fixtures
- create evidence linkage records
- create tool_action_request records
- create gate_decision records
- create dispatch or non-dispatch evidence records
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
- v0.6.225 is identified as the candidate checkpoint
- v0.6.226 is identified as the review and decision checkpoint
- the v0.6.225 required candidate scope is recorded
- minimum flow coverage is required
- four scenario expectations are recorded
- linkage planning is required
- evidence-boundary review is required
- public/private boundary review is required
- public exposure cleanup remains deferred, not rejected
- mock/dry-run completed status terminology cleanup remains deferred, not rejected
- the checkpoint states that no minimum flow scenario matrix is created in v0.6.224
- the checkpoint states that no fixtures, runtime behavior, Gateway behavior, public cleanup, or README rewrite is applied in v0.6.224
- runtime demo remains necessary but deferred
- publication remains deferred
