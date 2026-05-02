# v0.6.0 Implementation and Evaluation Work Ordering

Version: v0.6.0 candidate  
Status: implementation and evaluation sequencing; does not authorize runtime execution

## Purpose

This checkpoint organizes the next phase of AAEF-AI-VA before choosing a specific
implementation path.

A local assessment lab may become valuable, but it should not be started before the
project clarifies:

- what capabilities are already demonstrated,
- what needs to be evaluated,
- what should remain blocked,
- what can be implemented safely,
- what belongs only in a local model environment,
- what would be required before commercial PoC use,
- what must not be implied by public documentation.

This checkpoint is planning and sequencing only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Current baseline

The current public repository has reached v0.5.10 and includes:

- public FAQ and reviewer objection handling,
- public evidence and capability boundary summary,
- public front page and repository landing polish,
- public trust and reviewer navigation,
- release governance and maintainer operations checklist,
- repository ruleset and branch protection planning,
- dependency and repository governance readiness,
- licensing, trademark, authorship, and commercial-use protection,
- README compatibility phrase registry,
- commercial adoption preparation.

The current implementation already demonstrates local validation, control gates,
review gates, evidence linkage, report promotion, delivery authorization, runtime
readiness blocking, preflight scaffolding, governance checks, and public claim
boundaries.

The current implementation does not demonstrate live scanning, customer-target
operation, production deployment, managed-service operation, compliance
certification, legal approval, audit opinion, or external framework equivalence.

## Core sequencing rule

The v0.6.x sequencing rule is:

~~~text
Plan before implementation.
Evaluate before demonstration.
Gate before execution.
Local-only before customer-facing.
Evidence before claims.
Human review before delivery.
Commercial boundary before commercial PoC.
~~~

This means the next phase should not jump directly to a working scanner or a
customer-facing service.

## Workstream map

v0.6.x should be organized into the following workstreams:

| Workstream | Purpose | Starts before local model? |
| --- | --- | --- |
| Capability inventory | Record what exists and what is missing | Yes |
| Evaluation criteria | Define how future work will be judged | Yes |
| Safety boundary review | Preserve runtime and scan prohibitions | Yes |
| Local lab decisioning | Decide whether and how a local model environment should exist | Yes |
| Local assessment lab | Build localhost-only model environment if approved | Not necessarily |
| Runtime gate hardening | Improve gates before execution is enabled | Yes |
| Demo scenario planning | Define safe demos without public overclaims | Yes |
| Evidence/report UX | Improve explainability of generated evidence and review records | Yes |
| Commercial PoC readiness | Define what would be needed before paid pilots | Later |
| Runtime enablement | Consider narrow execution only after gates and scope mature | Later |

## Recommended order

The recommended order is:

1. v0.6.0 implementation and evaluation work ordering.
2. v0.6.1 capability inventory and maturity map.
3. v0.6.2 evaluation criteria and acceptance model.
4. v0.6.3 safety boundary and non-goal review.
5. v0.6.4 local assessment lab decision record.
6. v0.6.5 demo scenario and reviewer walkthrough planning.
7. v0.6.6 runtime gate hardening plan.
8. v0.6.7 evidence and report UX improvement plan.
9. v0.6.8 controlled local lab profile expansion, only if approved.
10. v0.6.9 commercial PoC readiness boundary, only after evidence and scope are clear.

This order may change, but the first three steps should happen before building a
larger local model environment.

## Why not start with the local lab immediately?

A local lab is valuable, but it can pull the project toward tool execution too early.

Starting with ordering and evaluation prevents these mistakes:

- building a demo before defining what it proves,
- enabling local commands before defining safety gates,
- creating a model environment that looks like scan authorization,
- producing artifacts that imply production readiness,
- spending effort on infrastructure before capability gaps are clear,
- confusing local-only demo value with customer-ready service value.

## Decision gates

Before starting each workstream, use these decision gates:

| Gate | Question |
| --- | --- |
| Capability gate | What capability or boundary is being improved? |
| Evidence gate | What artifact will prove the improvement? |
| Safety gate | Does this preserve runtime and scan prohibitions? |
| Scope gate | Is this local-only, public documentation, or commercial PoC preparation? |
| Claim gate | What public claim becomes safer or clearer after this work? |
| Rework gate | Does this decision reduce or increase future rework? |
| Commercial gate | Does this create a commercial implication that needs boundary language? |

## Priority rules

Use these priority rules:

1. Prefer work that clarifies multiple future paths.
2. Prefer tests and boundaries before new functionality.
3. Prefer localhost-only assumptions before any target-like behavior.
4. Prefer mock and dry-run behavior before real execution.
5. Prefer evidence readability before demo polish.
6. Prefer commercial boundaries before sales materials.
7. Prefer public trust clarity before private outreach.
8. Avoid enabling anything that can be mistaken for customer-target operation.

## Capability maturity levels

Use these maturity levels for future work:

| Level | Name | Meaning |
| --- | --- | --- |
| L0 | Concept recorded | A concept or boundary is documented |
| L1 | Static example | Static examples exist |
| L2 | Local validation | Local tests validate behavior or documents |
| L3 | Dry-run behavior | Behavior is simulated without real execution |
| L4 | Local-only controlled behavior | Behavior is constrained to owned localhost/lab scope |
| L5 | Reviewed PoC candidate | Human-reviewed and contract/scope-aware PoC candidate |
| L6 | Commercial deployment candidate | Requires separate commercial, legal, security, and operational review |

The project should not imply L5 or L6 readiness while operating at L0-L4.

## Local lab decision options

The local lab decision should choose one of these options:

| Option | Meaning |
| --- | --- |
| No local lab yet | Continue with evaluation and gate hardening first |
| Documentation-only local lab | Define profile and boundaries only |
| Static fixture local lab | Add examples without execution |
| Dry-run local lab | Simulate requests/results without external effects |
| Localhost-only controlled lab | Use owned local targets only after explicit gating |
| Deferred commercial PoC lab | Do not build until a commercial partner or target use case exists |

The default recommended option is documentation-only or dry-run until evaluation
criteria are mature.

## Minimum safe path before any local execution

Before any local execution expands, complete:

1. capability inventory and maturity map,
2. evaluation criteria and acceptance model,
3. safety boundary and non-goal review,
4. local lab decision record,
5. local-only target profile,
6. allowed and denied action taxonomy,
7. preflight gate evidence requirements,
8. human review requirements,
9. generated artifact private-output policy,
10. public claim boundary review.

## Commercial PoC readiness path

Commercial PoC readiness should not be the immediate next step.

Before commercial PoC work, define:

- what paid PoC would prove,
- what it would not prove,
- what environment is allowed,
- what target scope is allowed,
- who authorizes actions,
- how evidence is reviewed,
- how outputs are delivered,
- what license or commercial agreement is needed,
- what support boundary applies,
- what public claims remain prohibited.

## Public claim boundary

v0.6.x should continue using evidence-backed language.

Allowed public language:

- "planned work ordering",
- "capability inventory",
- "evaluation criteria",
- "local-only lab decisioning",
- "runtime execution remains blocked",
- "commercial PoC readiness is future work",
- "evidence-backed capability boundary."

Avoid public language that implies:

- live scanning,
- customer-target authorization,
- production deployment,
- managed service readiness,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- commercial license grant.

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

Before tagging v0.6.0, verify:

1. README links to this checkpoint.
2. Current baseline is recorded.
3. Core sequencing rule is recorded.
4. Workstream map is recorded.
5. Recommended order is recorded.
6. Local lab decision options are recorded.
7. Capability maturity levels are recorded.
8. Decision gates are recorded.
9. Commercial PoC readiness path is recorded.
10. Runtime and scanning boundaries remain disabled.
11. Claims to avoid are recorded.
12. `tools/run_all_local_checks.py` includes the v0.6.0 work-ordering test.

## Out of scope

This checkpoint does not:

- build a local lab,
- enable runtime execution,
- enable scanning,
- create private sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- configure GitHub branch protection,
- configure GitHub rulesets,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
