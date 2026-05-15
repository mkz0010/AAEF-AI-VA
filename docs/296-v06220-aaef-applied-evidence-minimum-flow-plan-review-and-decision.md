# v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision

Status: Accepted for minimum flow planning; not applied

## Purpose

This checkpoint reviews the v0.6.219 `AAEF Applied Evidence Minimum Flow Plan Candidate`.

The decision is narrow: the candidate plan is accepted as the AAEF Applied Evidence Minimum Flow Plan for future minimum flow work.

This checkpoint does not create the minimum flow package, create or modify fixtures, create evidence linkage records, create `tool_action_request` records, create `gate_decision` records, create dispatch or non-dispatch evidence records, create reviewer walkthrough content, create AAEF five questions mapping content, create an AAEF handback summary, rewrite README, apply public cleanup, change Gateway behavior, change runtime behavior, or approve publication.

## Reviewed source

Reviewed candidate:

- v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate

Source intake:

- v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation

AAEF main direction:

- Reorganize existing Tool Gateway runner, mock flow, evidence chain linkage, reconstruction report, and reviewer materials into a minimum applied evidence package before adding new diagnostic capability.
- Show `model_output -> tool_action_request -> gate_decision -> dispatch/non-dispatch -> evidence_event -> reviewer_walkthrough`.
- Preserve evidence trust boundary and non-proof boundary.

## Decision

The v0.6.219 candidate plan is accepted as the AAEF Applied Evidence Minimum Flow Plan for future minimum flow planning.

Decision fields:

- aaef_applied_evidence_minimum_flow_plan_accepted = true
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

## Accepted central proposition

The accepted plan centers on the AAEF proposition:

> Model output is not authority.

In AAEF-AI-VA terms:

> AI generates `tool_action_request`, but execution is decided by gates.

The accepted minimum flow must show how AI-generated diagnostic intent becomes a request, how a gate decides it, whether dispatch occurs or does not occur, and how a structured record supports reviewer reconstruction.

## Accepted minimum flow

The accepted minimum flow is:

1. model_output
2. tool_action_request
3. gate_decision
4. dispatch_decision / non_dispatch_decision
5. execution_result / non_execution_result
6. evidence_event
7. reviewer_walkthrough

Future work must identify which existing files, generated records, fixtures, tests, or docs already represent each step and which gaps require narrow follow-up work.

## Accepted existing element inventory requirement

Future minimum flow work must start by inventorying existing elements before creating new structures.

The inventory should include at least:

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

The inventory must classify each element as one of:

- static fixture
- mock flow
- generated private run output
- public sanitized example
- documentation-only record
- runtime scaffold
- validator or structural check

The inventory must not imply live scanner execution or production readiness.

## Accepted four-scenario matrix requirement

Future minimum flow work must cover at least four scenarios.

| Scenario | Purpose | Expected package treatment |
| --- | --- | --- |
| permitted safe diagnostic | A low-risk request is permitted under gate control | permitted request, dispatch decision, mock execution result, evidence event, reviewer summary |
| denied out-of-scope request | An out-of-scope request is denied | denied gate decision, non-dispatch evidence, blocked reason, reviewer summary |
| held / requires human approval | A high-impact or uncertain request is held | held decision, no autonomous dispatch, human approval boundary, reviewer summary |
| expired-not-executed | An expired or non-executed request is evidenced as non-dispatched | expired or non-executed gate result, no dispatch, evidence event, reviewer summary |

Future work must clarify whether each scenario is currently represented by an existing mock flow, static fixture, runtime scaffold, or documentation-only material.

## Accepted evidence linkage table requirement

Future minimum flow work must include an evidence linkage table.

The table must link:

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

## Accepted tool_action_request record requirement

Future minimum flow work must define or identify a `tool_action_request` fixture or record with at least:

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

The record must state:

- AI output is a request, not authority
- AI statements that an action is permitted are not authorization decisions
- credential values must be represented as references, not raw secrets

## Accepted gate_decision record requirement

Future minimum flow work must define or identify a gate decision record with at least:

- decision_id
- linked_request_id
- decision_result
- reason
- policy_or_rule_version
- trusted_inputs_used
- untrusted_inputs_excluded
- deciding_component
- timestamp

The plan accepts decision results including:

- permitted
- denied
- held
- requires_human_approval
- not_dispatched
- expired

The record must state:

- gate decision is not AI self-approval
- prompt content, page content, and AI rationale are not sufficient trusted authority by themselves
- trusted and untrusted inputs must be distinguishable

## Accepted dispatch / non-dispatch evidence requirement

Future minimum flow work must define or identify dispatch / non-dispatch evidence with at least:

- linked_decision_id
- dispatch_attempted
- dispatched_tool, if any
- blocked_reason, if not dispatched
- execution_boundary
- gateway_component
- timestamp

Future work must ensure that evidence can show:

- denied action was not executed
- held action was not autonomously dispatched
- expired action was not dispatched
- AI did not bypass the gate by changing tool or payload within the reviewed path

## Accepted evidence event package requirement

Future evidence event packages must connect:

- AI output / proposal
- tool_action_request
- gate_decision
- dispatch / non-dispatch
- execution_result / non_execution_result
- evidence_event
- reviewer_summary

The package must use review-supporting terminology.

It must not describe evidence as legal proof, audit sufficiency, compliance sufficiency, certification evidence, diagnostic completeness, or production readiness evidence.

## Accepted reviewer walkthrough requirement

Future reviewer walkthrough material must be readable without requiring the reviewer to reverse-engineer JSON files.

Each scenario walkthrough must explain:

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

## Accepted AAEF five questions mapping requirement

Future minimum flow work must map AAEF-AI-VA evidence to AAEF's five questions.

| AAEF question | AAEF-AI-VA evidence direction |
| --- | --- |
| Who or what acted? | AI request identity, gateway identity, tool identity |
| On whose behalf? | principal context, operator context |
| With what authority? | gate decision, policy version, authorization scope |
| Was the action allowed at execution time? | dispatch decision, non-dispatch decision, backend verification where applicable |
| What evidence supports reconstruction? | linked evidence package, reviewer summary, evidence event chain |

The mapping must use `supports reconstruction` rather than `proves what happened`.

## Accepted evidence trust boundary and non-proof boundary requirement

Future minimum flow material must include a boundary note stating:

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

## Accepted handback summary requirement

Future AAEF main handback summary should include:

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

The handback must avoid AAEF-AI-VA technical details that are commercial, NDA-dependent, customer-specific, or patent-sensitive.

## Accepted public/private/patent-sensitive boundary

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

## Accepted sequencing

Future work should proceed in narrow checkpoints.

Accepted sequencing:

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

## Accepted definition of done for future work

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

This checkpoint does not decide which deferred work resumes after the minimum flow work. That should be selected by a later risk-tiered checkpoint.

## Next recommended checkpoint

The recommended next checkpoint is:

- v0.6.221 Next Work Selection Using Risk-Tiered Granularity

That checkpoint should select the first concrete work item under the accepted AAEF Applied Evidence Minimum Flow Plan.

The expected first work item is existing element inventory, but the final selection should be recorded in v0.6.221.

## Explicit non-goals for v0.6.220

v0.6.220 does not:

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

This review-and-decision checkpoint does not approve public announcement, social-post instruction, executable demo, scanner readiness, external PoC readiness, production readiness, certification, legal compliance, audit opinion, diagnostic completeness, or external-framework equivalence.

## Acceptance criteria

This review-and-decision checkpoint is accepted when:

- the v0.6.219 candidate plan is reviewed
- the plan is accepted for minimum flow planning
- the central proposition is accepted
- the minimum flow is accepted
- existing element inventory requirement is accepted
- four-scenario matrix requirement is accepted
- evidence linkage table requirement is accepted
- tool_action_request record requirement is accepted
- gate_decision record requirement is accepted
- dispatch / non-dispatch evidence requirement is accepted
- evidence event package requirement is accepted
- reviewer walkthrough requirement is accepted
- AAEF five questions mapping requirement is accepted
- evidence trust boundary and non-proof boundary requirement is accepted
- handback summary requirement is accepted
- public/private/patent-sensitive boundary is accepted
- sequencing is accepted
- v0.6.221 is identified as the next recommended checkpoint
- no minimum flow package, fixtures, Gateway behavior, runtime behavior, public cleanup, or README rewrite is applied in v0.6.220
- runtime demo remains necessary but deferred
- publication remains deferred
