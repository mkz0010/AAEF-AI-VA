# v0.6.221 Next Work Selection Using Risk-Tiered Granularity

Status: Accepted direction-selection checkpoint

## Purpose

This checkpoint records the next work selection after v0.6.220 using risk-tiered granularity.

v0.6.220 accepted the AAEF Applied Evidence Minimum Flow Plan for future minimum flow planning.

v0.6.221 selects the first concrete work item under that accepted plan.

This checkpoint does not create the existing element inventory, create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Baseline carried forward

The latest completed checkpoint before this document is v0.6.220.

v0.6.220 accepted the AAEF Applied Evidence Minimum Flow Plan for future minimum flow planning only.

The following boundaries remain in force:

- minimum flow package is not created in this checkpoint
- existing element inventory is not created in this checkpoint
- fixtures are not created or modified in this checkpoint
- evidence linkage records are not created in this checkpoint
- `tool_action_request` records are not created in this checkpoint
- `gate_decision` records are not created in this checkpoint
- dispatch or non-dispatch evidence records are not created in this checkpoint
- reviewer walkthrough content is not created in this checkpoint
- AAEF five questions mapping content is not created in this checkpoint
- AAEF handback summary is not created in this checkpoint
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

- selected_next_work_item = existing_element_inventory
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.222 Existing Element Inventory Candidate
- selected_followup_checkpoint = v0.6.223 Existing Element Inventory Review and Decision

## Why this work item is selected

The accepted AAEF Applied Evidence Minimum Flow Plan requires existing element inventory before creating new structures.

This is necessary because AAEF-AI-VA already contains relevant elements:

- Tool Gateway runner
- generated runner outputs
- allowed-action mock flow
- denied-action mock flow
- human-approval-required mock flow
- evidence chain linkage outputs
- evidence reconstruction report outputs
- sanitizer and finding review records where relevant
- runtime readiness and execution-blocked scaffold outputs
- preflight evidence model and validation scaffold outputs
- static fixture and safe demo materials
- reviewer walkthrough materials
- public sample and applied evidence documents

The next safe step is to inventory and classify these elements before creating or modifying fixtures.

## Why the risk tier is high

This work is high-risk because an inaccurate inventory can misstate project maturity.

Inventory wording could incorrectly imply that documentation-only, static fixture, mock flow, generated private run output, runtime scaffold, or structural validator material is equivalent to runtime execution, scanner readiness, production readiness, audit sufficiency, or diagnostic completeness.

The inventory must preserve the distinction between:

- static fixture
- mock flow
- generated private run output
- public sanitized example
- documentation-only record
- runtime scaffold
- validator or structural check

The inventory must also preserve public/private/patent-sensitive boundaries.

## Why the work is split into two checkpoints

The selected work item is split into two checkpoints:

1. v0.6.222 creates the Existing Element Inventory Candidate.
2. v0.6.223 reviews the Existing Element Inventory Candidate, accepts or rejects it, and records the decision.

This preserves a review boundary before the inventory is treated as accepted.

## Required v0.6.222 candidate scope

The v0.6.222 candidate should inventory existing elements that may support the accepted minimum flow:

- model_output
- tool_action_request
- gate_decision
- dispatch_decision / non_dispatch_decision
- execution_result / non_execution_result
- evidence_event
- reviewer_walkthrough

The candidate should identify candidate source locations without creating new minimum flow artifacts.

The candidate should classify each existing element using maturity/source categories:

- static fixture
- mock flow
- generated private run output
- public sanitized example
- documentation-only record
- runtime scaffold
- validator or structural check

The candidate should include a gap classification for each minimum flow step:

- present
- partially present
- planned
- missing
- unsafe_for_public_surface
- private_or_patent_sensitive_only

## Required v0.6.222 scenario coverage review

The v0.6.222 candidate should check existing coverage for at least four scenarios:

- permitted safe diagnostic
- denied out-of-scope request
- held / requires human approval
- expired-not-executed

The candidate should not create these scenario artifacts yet.

It should record whether each scenario is currently represented by existing material and what follow-up is needed.

## Required v0.6.222 evidence-boundary review

The v0.6.222 candidate must preserve these statements:

- model output is not authority
- AI rationale is not authorization
- evidence supports reconstruction; it does not prove legal truth
- validator success is structural only
- runtime scaffold is not runtime readiness
- mock flow is not live scanner execution
- generated private run output is not public-safe by default
- public sanitized examples must not expose secrets, customer data, third-party targets, or patent-sensitive implementation detail

## Required v0.6.222 public/private boundary review

The v0.6.222 candidate should mark whether candidate source material is:

- public-safe
- public-safe after sanitization
- private-not-in-git only
- patent-sensitive private only
- not suitable for public repository use

The candidate must not move files or publish private material in v0.6.222.

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress
- deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused

## Explicit non-goals for v0.6.221

v0.6.221 does not:

- create the existing element inventory
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
- v0.6.222 is identified as the candidate checkpoint
- v0.6.223 is identified as the review and decision checkpoint
- the v0.6.222 required candidate scope is recorded
- four-scenario coverage review is required
- evidence-boundary review is required
- public/private boundary review is required
- public exposure cleanup remains deferred, not rejected
- mock/dry-run completed status terminology cleanup remains deferred, not rejected
- the checkpoint states that no existing element inventory is created in v0.6.221
- the checkpoint states that no fixtures, runtime behavior, Gateway behavior, public cleanup, or README rewrite is applied in v0.6.221
- runtime demo remains necessary but deferred
- publication remains deferred
