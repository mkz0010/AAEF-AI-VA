# v0.6.8 Demo Scenario and Reviewer Walkthrough Planning

Version: v0.6.8 candidate  
Status: demo scenario and reviewer walkthrough planning; does not authorize runtime execution

## Purpose

This checkpoint defines a public-safe demo scenario and reviewer walkthrough plan for
AAEF-AI-VA.

v0.6.6 defined the AI request decision boundary and tool selection criteria.
v0.6.7 defined observation normalization and Diagnostic Fidelity Risk.

This checkpoint now defines how to explain the model to reviewers without enabling
runtime execution or exposing private advanced feature details.

This checkpoint is planning only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Public-safe design boundary

The walkthrough must stay within public-safe AAEF-AI-VA principles:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Assessment actions must be scoped, authorized, and evidenced.
- Raw or sensitive artifacts must not be exposed to AI without approval and redaction.
- Runtime execution remains blocked.
- Scan execution remains blocked.
- Customer-target operation remains blocked.

The walkthrough must not disclose private advanced feature details, protected IP-review strategy,
protected IP-review drafting, protected IP-review analysis, competitor comparison, or confidential commercial
licensing strategy.

## Core walkthrough proposition

The walkthrough proposition is:

~~~text
AI receives an approved diagnostic context package.
AI generates a non-authoritative tool_action_request.
Gates evaluate scope, preflight, action taxonomy, evidence needs, and human review.
Execution remains blocked in this planning checkpoint.
Reviewers can inspect the request, gate decision, evidence expectations, and non-proof boundaries.
~~~

This proposition is intentionally non-executing.

It explains the control model without implying a working scanner, customer-target
operation, or production-ready service.

## Walkthrough audience

The walkthrough should be understandable to:

- security reviewers,
- vulnerability assessment leads,
- CISO or security managers,
- AI governance reviewers,
- compliance or assurance reviewers,
- implementation reviewers,
- potential commercial evaluators.

The walkthrough should avoid relying on private implementation details.

It should explain the public control model and evidence model.

## Demo scenario shape

The demo scenario is a documentation-only reviewer walkthrough.

It may use static illustrative records in future work, but this checkpoint does not
add those records.

The scenario should show:

1. a scope statement,
2. an approved diagnostic context package summary,
3. an AI-generated `tool_action_request`,
4. a gate decision,
5. expected evidence,
6. human review checkpoint,
7. result state,
8. what the walkthrough does not prove.

The scenario should remain non-executing.

## Reviewer walkthrough sequence

The reviewer walkthrough should proceed in this order:

| Step | Reviewer sees | Purpose |
| --- | --- | --- |
| 1 | Scope and target boundary summary | Confirm what is in scope and what remains excluded |
| 2 | Diagnostic context summary | Show what AI may use for request generation |
| 3 | Missing information and uncertainty | Show that AI does not guess missing context |
| 4 | AI-generated `tool_action_request` | Show request generation without authority |
| 5 | Gate evaluation summary | Show gate-controlled decision-making |
| 6 | Evidence expectation summary | Show what evidence would be needed |
| 7 | Human review checkpoint | Show where human review is required |
| 8 | Blocked or documentation-only outcome | Show execution remains blocked |
| 9 | Non-proof statement | Show what the walkthrough does not prove |
| 10 | Reviewer questions | Support structured review without overstating capability |

## Walkthrough artifacts

Future walkthrough artifacts may include:

| Artifact | Public-safe purpose |
| --- | --- |
| `demo_scope_summary` | Explain scope and exclusions |
| `demo_diagnostic_context_summary` | Explain AI-visible approved context |
| `demo_missing_information_summary` | Explain known gaps |
| `demo_tool_action_request` | Show non-authoritative request generation |
| `demo_gate_decision_summary` | Show gate outcome |
| `demo_expected_evidence_summary` | Show evidence expectations |
| `demo_human_review_checkpoint` | Show review requirement |
| `demo_non_proof_statement` | Show what is not demonstrated |
| `demo_reviewer_question_list` | Support reviewer assessment |
| `demo_walkthrough_record` | Link the walkthrough pieces together |

These are planning artifacts at this stage.

They are not runtime artifacts.

## AI-visible information in the walkthrough

The walkthrough may describe AI-visible information only at an abstract and approved
level.

Allowed examples:

- approved diagnostic context package summary,
- sanitized observation summary,
- extracted signal summary,
- missing information,
- confidence and uncertainty,
- safety notes,
- expected evidence categories,
- human review recommendation.

The walkthrough must not expose secrets, credentials, raw customer artifacts, private
advanced feature details, or unreviewed sensitive raw content.

## What AI may do in the walkthrough

AI may:

- interpret approved diagnostic context,
- identify missing information,
- state uncertainty,
- recommend an additional observation as a request,
- generate `tool_action_request`,
- provide a request rationale,
- state expected evidence,
- request human review,
- preserve the boundary that execution is gate-decided.

These actions are still request-generation activities.

They do not authorize execution.

## What gates should show in the walkthrough

Gate evaluation should show:

- scope binding check,
- target binding check,
- action taxonomy check,
- denied action check,
- preflight evidence check,
- diagnostic sufficiency check,
- human review requirement,
- evidence expectation,
- blocked or documentation-only outcome,
- reason for keeping execution blocked.

The gate explanation should be readable without implying that the system is ready for
live execution.

## Outcome model for the walkthrough

The walkthrough may use these outcomes:

| Outcome | Meaning |
| --- | --- |
| `documentation_recorded` | A documentation-only step was recorded |
| `request_recorded` | A `tool_action_request` was recorded |
| `requires_more_observation` | Context was insufficient |
| `requires_human_review` | Review is required before any later advancement |
| `requires_preflight_evidence` | Preflight evidence is missing |
| `blocked_by_scope` | Scope or target boundary blocks advancement |
| `blocked_by_action_taxonomy` | Action is denied or unsupported |
| `execution_not_authorized` | Runtime execution remains blocked |

The walkthrough must not introduce an `executed` outcome.

## Non-proof statement

The walkthrough must explicitly state what it does not prove.

It does not prove:

- live scanning works,
- runtime execution is ready,
- customer-target operation is authorized,
- external network testing is authorized,
- credential injection is authorized,
- raw sensitive artifact capture is authorized,
- production deployment is ready,
- managed-service operation is ready,
- commercial PoC readiness exists,
- compliance certification exists,
- legal approval exists,
- audit opinion exists,
- safety is guaranteed.

This non-proof statement should be visible in any future demo package.

## Reviewer questions

The walkthrough should help reviewers ask:

- What context did AI receive?
- What context did AI not receive?
- What uncertainty did AI identify?
- What `tool_action_request` did AI generate?
- Which observations supported the request?
- Which gate evaluated the request?
- What evidence would be expected?
- Why did execution remain blocked?
- Where would human review be required?
- What does this walkthrough not prove?

These questions support review without claiming production readiness.

## Demo success criteria

A successful non-executing demo walkthrough should show:

- the core proposition clearly,
- the request and execution boundary clearly,
- the AI-visible context boundary clearly,
- the missing information boundary clearly,
- the gate decision clearly,
- the evidence expectation clearly,
- the human review checkpoint clearly,
- the non-proof statement clearly,
- no execution authorization,
- no scan execution,
- no customer-target implication,
- no private advanced feature disclosure.

## Private workstream separation

The public walkthrough must not include private advanced feature details.

If a future private workstream requires advanced implementation details, those details
must remain outside public repository content and be handled only in private,
non-git-tracked materials.

Public wording should stay at the level of general AAEF-AI-VA principles.

The public demo walkthrough is not a place for protected IP-review strategy, protected IP-review drafting,
protected IP-review analysis, competitor comparison, or confidential commercial licensing
strategy.

## Relationship to v0.6.6

v0.6.6 provides the request boundary:

~~~text
AI generates tool_action_request.
Gates decide execution.
~~~

The demo walkthrough should make that boundary observable to reviewers without
changing it.

## Relationship to v0.6.7

v0.6.7 provides the observation boundary:

~~~text
AI receives approved diagnostic context.
Normalization loss and missing information are recorded.
Information insufficiency should lead to additional observation or review, not guessing.
~~~

The demo walkthrough should make that observation boundary understandable to
reviewers without exposing unsafe raw content.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.9 Evidence Reconstruction and Sample Report Demonstration Planning
~~~

Rationale:

- v0.6.8 defines how reviewers should walk through a non-executing demo.
- The next step should define sample evidence and report demonstration planning.
- A sample report demonstration should still remain non-executing unless later work
  explicitly changes scope.
- Safe Docker or local lab execution should remain deferred until public-safe
  walkthrough and evidence demonstration boundaries are clear.

## Public claim boundary

Allowed public language:

- "non-executing demo walkthrough",
- "reviewer walkthrough planning",
- "AI-generated `tool_action_request`",
- "gate decision summary",
- "evidence expectation summary",
- "human review checkpoint",
- "non-proof statement",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies:

- live scanning,
- automated exploitation,
- autonomous testing,
- customer-target authorization,
- external network testing authorization,
- production deployment,
- managed service readiness,
- commercial PoC readiness,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- commercial license grant,
- private advanced feature details.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- completed legal review,
- completed dependency audit,
- managed service approval,
- commercial license grant,
- safety guarantee,
- external framework equivalence,
- audit sufficiency.

## Required local checks

Before tagging v0.6.8, verify:

1. README links to this checkpoint.
2. Public-safe design boundary is recorded.
3. Core walkthrough proposition is recorded.
4. Walkthrough audience is recorded.
5. Demo scenario shape is recorded.
6. Reviewer walkthrough sequence is recorded.
7. Walkthrough artifacts are recorded.
8. AI-visible information boundary is recorded.
9. What AI may do in the walkthrough is recorded.
10. What gates should show in the walkthrough is recorded.
11. Outcome model excludes execution.
12. Non-proof statement is recorded.
13. Reviewer questions are recorded.
14. Demo success criteria are recorded.
15. Private workstream separation is recorded.
16. Runtime and scanning boundaries remain disabled.
17. Claims to avoid are recorded.
18. `tools/run_all_local_checks.py` includes the v0.6.8 demo scenario test.

## Out of scope

This checkpoint does not:

- build a local lab,
- add static demo fixtures,
- add dry-run lab execution,
- enable runtime execution,
- enable scanning,
- add new scanner integrations,
- expose private advanced feature details,
- create private sales material,
- publish pricing,
- create a commercial contract,
- provide legal advice,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
