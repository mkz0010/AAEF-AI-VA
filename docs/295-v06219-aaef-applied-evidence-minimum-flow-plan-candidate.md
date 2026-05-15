# v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate

Status: Candidate only

## Purpose

This checkpoint creates a candidate plan for the AAEF Applied Evidence Minimum Flow after the v0.6.218 intake and priority reconciliation.

v0.6.218 selected `aaef_applied_evidence_minimum_flow_plan` as the immediate next high-risk work item after AAEF main feedback.

This checkpoint is a plan candidate only. It does not create the minimum flow package, create or modify fixtures, create reviewer walkthrough content, create an AAEF handback summary, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Source decision

v0.6.218 selected the next work item:

- selected_next_work_item = aaef_applied_evidence_minimum_flow_plan
- selected_next_work_item_risk_tier = high
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate
- selected_followup_checkpoint = v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

The accepted Public Exposure Hygiene Plan remains valid, but public exposure cleanup remains deferred, not rejected.

The previously selected mock/dry-run completed status terminology cleanup remains deferred, not rejected.

## Candidate plan status

This candidate plan is:

- candidate only
- not accepted
- not applied
- not a minimum flow package
- not a fixture implementation
- not a reviewer walkthrough
- not an AAEF handback summary
- not runtime-ready
- not scanner-ready
- subject to v0.6.220 review and decision

## Central proposition

The candidate plan centers on the AAEF proposition:

> Model output is not authority.

In AAEF-AI-VA terms:

> AI generates `tool_action_request`, but execution is decided by gates.

The minimum flow should show how AI-generated diagnostic intent becomes a request, how a gate decides it, whether dispatch occurs or does not occur, and how a structured record supports reviewer reconstruction.

## Candidate minimum flow

The minimum flow to plan is:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

The plan should identify which existing files, generated records, fixtures, tests, or docs already represent each step and which gaps require narrow follow-up work.

## Existing element inventory plan

v0.6.219 should not invent a new architecture before inventorying existing elements.

The future minimum flow package should inventory at least the following existing elements:

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

The inventory should classify each element as one of:

- static fixture
- mock flow
- generated private run output
- public sanitized example
- documentation-only record
- runtime scaffold
- validator or structural check

The inventory should not imply live scanner execution or production readiness.

## Four-scenario matrix plan

The future minimum flow package should cover at least four scenarios.

| Scenario | Purpose | Expected package treatment |
| --- | --- | --- |
| permitted safe diagnostic | A low-risk request is permitted under gate control | permitted request, dispatch decision, mock execution result, evidence event, reviewer summary |
| denied out-of-scope request | An out-of-scope request is denied | denied gate decision, non-dispatch evidence, blocked reason, reviewer summary |
| held / requires human approval | A high-impact or uncertain request is held | held decision, no autonomous dispatch, human approval boundary, reviewer summary |
| expired-not-executed | An expired or non-executed request is evidenced as non-dispatched | expired or non-executed gate result, no dispatch, evidence event, reviewer summary |

The plan must clarify whether each scenario is currently represented by an existing mock flow, static fixture, runtime scaffold, or documentation-only material.

## Evidence linkage table plan

The future minimum flow package should include an evidence linkage table.

The table should link:

- scenario_id
- model_output_id
- tool_action_request_id
- gate_decision_id
- dispatch_decision_id or non_dispatch_decision_id
- execution_result_id or non_execution_result_id
- evidence_event_id
- reviewer_walkthrough_id
- five_questions_mapping_id

The table must distinguish existing records from planned records.

The table must not imply real execution when the underlying record is mock, static fixture, documentation-only, or execution-blocked scaffold material.

## tool_action_request record plan

The future package should define or identify a `tool_action_request` fixture or record with at least:

- request_id
- requested_tool
- action_type
- target_scope
- requested_parameters
- purpose
- rationale
- risk_level
- actor
- principal_context
- credential_ref, if applicable
- generated_by_ai
- timestamp

The record should state:

- AI output is a request, not authority
- AI statements that an action is permitted are not authorization decisions
- credential values must be represented as references, not raw secrets

## gate_decision record plan

The future package should define or identify a gate decision record with at least:

- decision_id
- linked_request_id
- decision_result
- reason
- policy_or_rule_version
- trusted_inputs_used
- untrusted_inputs_excluded
- deciding_component
- timestamp

The plan should cover decision results including:

- permitted
- denied
- held
- requires_human_approval
- not_dispatched
- expired

The record should state:

- gate decision is not AI self-approval
- prompt content, page content, and AI rationale are not sufficient trusted authority by themselves
- trusted and untrusted inputs must be distinguishable

## dispatch / non-dispatch evidence plan

The future package should define or identify dispatch / non-dispatch evidence with at least:

- linked_decision_id
- dispatch_attempted
- dispatched_tool, if any
- blocked_reason, if not dispatched
- execution_boundary
- gateway_component
- timestamp

The plan should ensure that evidence can show:

- denied action was not executed
- held action was not autonomously dispatched
- expired action was not dispatched
- AI did not bypass the gate by changing tool or payload within the reviewed path

## Evidence event package plan

The future evidence event package should connect:

- AI output / proposal
- tool_action_request
- gate_decision
- dispatch / non-dispatch
- execution_result / non_execution_result
- evidence_event
- reviewer_summary

The package should use review-supporting terminology.

It must not describe evidence as legal proof, audit sufficiency, compliance sufficiency, certification evidence, diagnostic completeness, or production readiness evidence.

## Reviewer walkthrough plan

The future reviewer walkthrough should be readable without requiring the reviewer to reverse-engineer JSON files.

Each scenario walkthrough should explain:

1. what the AI requested
2. what `tool_action_request` was created
3. what the gate evaluated
4. which trusted inputs were used
5. which untrusted inputs were excluded
6. why the result was permitted, denied, held, or not executed
7. whether dispatch occurred
8. which evidence event supports reconstruction
9. how the scenario answers AAEF's five questions
10. what the evidence does not prove

## AAEF five questions mapping plan

The future package should map AAEF-AI-VA evidence to AAEF's five questions.

| AAEF question | AAEF-AI-VA evidence direction |
| --- | --- |
| Who or what acted? | AI request identity, gateway identity, tool identity |
| On whose behalf? | principal context, operator context |
| With what authority? | gate decision, policy version, authorization scope |
| Was the action allowed at execution time? | dispatch decision, non-dispatch decision, backend verification where applicable |
| What evidence supports reconstruction? | linked evidence package, reviewer summary, evidence event chain |

The plan should use `supports reconstruction` rather than `proves what happened`.

## Evidence trust boundary and non-proof boundary plan

The future package should include a boundary note stating:

- model output is not evidence authority
- AI rationale is not authorization
- agent runtime self-report alone is not sufficient evidence
- evidence writer, gateway, and policy decision components should be separated from model runtime where practical
- compromised gateway reduces trust
- compromised evidence writer reduces trust
- compromised evidence store reduces trust
- validator success is structural only
- validator success does not imply semantic correctness
- validator success does not imply evidence sufficiency
- validator success does not imply audit sufficiency
- validator success does not imply legal sufficiency
- validator success does not imply production readiness
- validator success does not imply runtime readiness

## Handback summary plan

The future AAEF main handback summary should include:

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
11. public/private/patent-sensitive boundary notes
12. abstract lessons for AAEF Core
13. abstract lessons for Profile or Practical Package
14. possible lessons for `AI Agent Action Risk Review`

The handback should avoid AAEF-AI-VA technical details that are commercial, NDA-dependent, customer-specific, or patent-sensitive.

## Public/private/patent-sensitive boundary plan

Public repository material may include:

- safe local lab scope
- static fixtures
- mock gateway
- sanitized evidence examples
- structural validators
- reviewer walkthrough
- non-execution evidence examples
- AAEF five questions mapping
- abstract gate/evidence concepts

Public repository material must not include:

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

## Candidate sequencing

If this plan is accepted in v0.6.220, later work should proceed in narrow checkpoints.

Candidate sequencing:

1. existing element inventory candidate
2. existing element inventory review and decision
3. minimum flow scenario matrix candidate
4. minimum flow scenario matrix review and decision
5. evidence linkage table candidate
6. evidence linkage table review and decision
7. tool_action_request / gate_decision / dispatch evidence package candidate
8. tool_action_request / gate_decision / dispatch evidence package review and decision
9. reviewer walkthrough and AAEF five questions mapping candidate
10. reviewer walkthrough and AAEF five questions mapping review and decision
11. evidence trust boundary and non-proof boundary cleanup candidate
12. evidence trust boundary and non-proof boundary cleanup review and decision
13. AAEF main handback summary candidate
14. AAEF main handback summary review and decision
15. return to public exposure hygiene or Gateway core safety integration next work selection

## Candidate definition of done for future work

Future minimum flow checkpoints should not be treated as done unless they include:

- explicit scenario scope
- exact files created, changed, or intentionally left unchanged
- clear static fixture / mock / runtime scaffold classification
- linked IDs across request, decision, dispatch/non-dispatch, result, evidence, and walkthrough records
- AAEF five questions mapping
- evidence trust boundary note
- non-proof boundary note
- no hidden runtime demo approval
- no hidden scanner readiness claim
- no hidden customer or external target authorization
- no patent-sensitive public detail
- local validation or structural tests where practical

## Relationship to deferred work

The Public Exposure Hygiene Plan remains valid.

Public exposure cleanup remains deferred, not rejected.

The previously selected mock/dry-run completed status terminology cleanup remains deferred, not rejected.

This plan candidate does not decide which deferred work resumes after the minimum flow work. That should be selected by a later risk-tiered checkpoint.

## Explicit non-goals for v0.6.219

v0.6.219 does not:

- accept the plan
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

This plan candidate does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This candidate checkpoint is accepted when:

- the AAEF Applied Evidence Minimum Flow Plan Candidate is recorded
- the central proposition is recorded
- the minimum flow is recorded
- existing element inventory planning is recorded
- four-scenario matrix planning is recorded
- evidence linkage table planning is recorded
- tool_action_request record planning is recorded
- gate_decision record planning is recorded
- dispatch / non-dispatch evidence planning is recorded
- evidence event package planning is recorded
- reviewer walkthrough planning is recorded
- AAEF five questions mapping planning is recorded
- evidence trust boundary and non-proof boundary planning is recorded
- handback summary planning is recorded
- public/private/patent-sensitive boundary planning is recorded
- candidate sequencing is recorded
- v0.6.220 is identified as the review and decision checkpoint
- no minimum flow package, fixtures, Gateway behavior, runtime behavior, public cleanup, or README rewrite is applied in v0.6.219
- runtime demo remains necessary but deferred
- publication remains deferred
