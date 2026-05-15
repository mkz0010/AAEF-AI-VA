# v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation

Status: Accepted intake and priority reconciliation checkpoint

## Purpose

This checkpoint records AAEF main feedback and reconciles the next AAEF-AI-VA priority after v0.6.217.

v0.6.217 accepted the Public Exposure Hygiene Plan for cleanup planning. That plan remains valid and is not rejected.

After v0.6.217, AAEF main confirmed that AAEF-AI-VA should prioritize a minimum applied evidence flow before continuing public exposure cleanup or Gateway implementation work.

The purpose of this checkpoint is to select an AAEF Applied Evidence Minimum Flow workstream that reorganizes existing AAEF-AI-VA elements into a reviewable package answering AAEF's five questions.

This checkpoint does not implement new runtime behavior, add scanner behavior, move public materials, rewrite README, create a runtime demo, or apply public cleanup.

## Source inputs

This checkpoint reconciles three active inputs.

### 1. v0.6.217 Public Exposure Hygiene Plan

v0.6.217 accepted the Public Exposure Hygiene Plan for cleanup planning only.

That plan remains valid.

### 2. v0.6.214 Gateway Core Safety Integration work selection

v0.6.214 selected `mock_dry_run_completed_status_terminology_cleanup` as the first high-risk Gateway Core Safety Integration implementation item.

That work remains deferred, not rejected.

### 3. AAEF main applied evidence direction

AAEF main instructed AAEF-AI-VA to prioritize showing the AAEF applied implementation minimum flow before adding new diagnostic capability.

The center of the requested flow is:

- model_output
- tool_action_request
- gate_decision
- dispatch_decision / non_dispatch_decision
- execution_result / non_execution_result
- evidence_event
- reviewer_walkthrough

The AAEF main emphasis is:

- AI generates `tool_action_request`, but execution is decided by gates.
- Model output is not authority.
- Evidence should support reconstruction, not claim legal proof, audit sufficiency, compliance sufficiency, or production readiness.
- Existing Tool Gateway runner, mock flow, evidence chain linkage, and reconstruction report should be reorganized before adding new features.

## Current repository context

AAEF-AI-VA already contains relevant elements that can be reorganized.

Examples include:

- Tool Gateway runner
- allowed / denied / human-approval-required mock flows
- evidence chain linkage
- evidence reconstruction report
- static fixture and safe demo material
- reviewer walkthrough material
- runtime readiness and preflight scaffold material
- non-execution and execution-blocked records

The next work should not begin by adding diagnostic precision or scanner capability.

The next work should begin by inventorying existing elements and mapping them to the AAEF applied evidence minimum flow.

## Reconciliation decision

The immediate next work order is changed.

Public Exposure Hygiene Plan remains accepted but is deferred behind the AAEF Applied Evidence Minimum Flow planning track.

Gateway terminology cleanup remains deferred, not rejected.

New near-term order:

1. v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation
2. v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate
3. v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision
4. Later checkpoint: minimum flow evidence package / fixture candidate
5. Later checkpoint: minimum flow evidence package / fixture review and decision
6. Later checkpoint: reviewer walkthrough and AAEF five questions mapping candidate
7. Later checkpoint: reviewer walkthrough and AAEF five questions mapping review and decision
8. Later checkpoint: AAEF main handback summary candidate
9. Later checkpoint: AAEF main handback summary review and decision

## Selected next work item

The selected next work item is recorded as follows:

- selected_next_work_item = aaef_applied_evidence_minimum_flow_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate
- selected_followup_checkpoint = v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

## Deferred work items

The following work items remain deferred, not rejected:

- deferred_work_item = public_exposure_cleanup_work
- deferred_reason = aaef_main_applied_evidence_minimum_flow_priority
- deferred_return_condition = aaef_applied_evidence_minimum_flow_plan_reviewed_and_decided

- deferred_work_item = mock_dry_run_completed_status_terminology_cleanup
- deferred_reason = aaef_main_applied_evidence_minimum_flow_priority
- deferred_return_condition = aaef_applied_evidence_minimum_flow_plan_reviewed_and_decided

## Required v0.6.219 planning focus

The v0.6.219 plan candidate should prioritize reorganization and mapping, not new runtime execution.

It should cover:

1. existing element inventory
2. four-scenario matrix
3. evidence linkage table
4. AAEF five questions mapping
5. evidence trust boundary and non-proof boundary
6. reviewer walkthrough gap analysis
7. handback summary structure
8. public/private/patent-sensitive boundary confirmation

## Minimum flow to plan

The minimum flow is:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

The plan should identify which existing files, fixtures, generated examples, or docs already represent each step, and which gaps require narrow follow-up work.

## Scenario matrix required

The plan should cover at least four scenarios:

| Scenario | Purpose |
| --- | --- |
| permitted safe diagnostic | A low-risk request is permitted under gate control |
| denied out-of-scope request | An out-of-scope request is denied |
| held / requires human approval | A high-impact or uncertain request is held |
| expired-not-executed | An expired or non-executed request is evidenced as non-dispatched |

The plan should identify whether each scenario is currently supported by existing mock flow, static fixture, runtime scaffold, or documentation-only material.

## Evidence linkage table required

The plan should define a table that links:

- model_output
- tool_action_request
- gate_decision
- dispatch_decision / non_dispatch_decision
- execution_result / non_execution_result
- evidence_event
- reviewer_walkthrough

The table should distinguish existing records from planned records and should avoid implying runtime execution where only mock or static fixture material exists.

## AAEF five questions mapping required

The plan should map AAEF-AI-VA evidence to AAEF's five questions.

| AAEF question | AAEF-AI-VA evidence direction |
| --- | --- |
| Who or what acted? | AI request, gateway identity, tool identity |
| On whose behalf? | principal context, operator context |
| With what authority? | gate decision, policy version |
| Was the action allowed at execution time? | dispatch decision, non-dispatch decision, backend verification where applicable |
| What evidence supports reconstruction? | linked evidence package, reviewer summary |

The plan should use `supports reconstruction` rather than `proves what happened`.

## Evidence trust boundary required

The plan should include a boundary note that states:

- model output is not evidence authority
- agent runtime self-report alone is not sufficient
- evidence writer, gateway, and policy decision components should be separated from model runtime where practical
- compromised gateway, evidence writer, or evidence store reduces evidence trust
- validator success is structural only
- validator success does not imply semantic correctness, evidence sufficiency, audit sufficiency, legal sufficiency, production readiness, or runtime readiness

## Handback summary requirement

The future handback summary should include:

1. latest commit / branch / tag
2. added or changed files
3. local validation result
4. `tools/run_all_local_checks.py` result
5. scenario list
6. evidence package structure
7. `tool_action_request -> gate_decision -> dispatch/non-dispatch -> evidence_event` correspondence
8. reviewer walkthrough location
9. AAEF five questions mapping location
10. evidence trust boundary notes
11. public-private-patent-sensitive boundary notes
12. abstract lessons that may return to AAEF Core, Profile, Practical Package, or AI Agent Action Risk Review

## Public/private/patent-sensitive boundary retained

Public repository work may include:

- safe local lab scope
- static fixtures
- mock gateway
- sanitized evidence examples
- structural validators
- reviewer walkthrough
- non-execution evidence examples
- AAEF five questions mapping
- abstract gate/evidence concepts

Public repository work must not include:

- real target details
- third-party scanning details
- live exploitation details
- raw credentials or secrets
- client or production environment details
- browser-state reconstruction technical details
- DOM / HAR / screenshot / accessibility / event / storage / console integration detail
- patent-sensitive diagnostic reconstruction detail
- pricing strategy
- customer lists
- NDA-dependent commercial material

Patent-sensitive material, if any, must remain outside public repository material and should be kept under `private-not-in-git/patent-prep/` when needed.

## Explicit non-goals for v0.6.218

v0.6.218 does not:

- create the minimum flow package
- create new fixtures
- modify existing fixtures
- create reviewer walkthrough content
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

This intake and priority reconciliation checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This checkpoint is accepted when:

- AAEF main feedback is recorded
- the current v0.6.217 public exposure hygiene plan is preserved
- AAEF applied evidence minimum flow planning is selected as the immediate next priority
- v0.6.219 is identified as the plan candidate checkpoint
- v0.6.220 is identified as the plan review and decision checkpoint
- public exposure cleanup is deferred, not rejected
- mock/dry-run completed status terminology cleanup is deferred, not rejected
- the checkpoint states that no fixtures, runtime behavior, Gateway behavior, public cleanup, or README rewrite is applied in v0.6.218
- runtime demo remains necessary but deferred
- publication remains deferred
