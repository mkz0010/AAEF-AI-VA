# v0.6.4 Local Assessment Lab Decision Record

Version: v0.6.4 candidate  
Status: local assessment lab decision record; does not authorize runtime execution

## Purpose

This checkpoint records the local assessment lab decision for AAEF-AI-VA.

Earlier v0.6.x checkpoints established:

- implementation and evaluation work ordering,
- capability inventory and maturity mapping,
- evaluation criteria and acceptance gates,
- safety boundary and non-goal review.

This checkpoint now decides whether the project should proceed toward a local
assessment lab and, if so, which maturity level is allowed next.

This checkpoint is a decision record only.

This checkpoint does not build a local lab.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Decision summary

Decision:

~~~text
Proceed with a documentation-only local lab profile and dry-run planning.
Do not build localhost-only controlled execution yet.
Do not enable runtime execution.
Do not enable scan execution.
Do not enable credential injection.
Do not authorize customer-target operation.
~~~

Selected option:

~~~text
Documentation-only local lab, with dry-run planning allowed as future work.
~~~

Rejected for now:

~~~text
No local lab yet
Static fixture local lab as the immediate next step
Dry-run local lab as the immediate next step
Localhost-only controlled lab
Deferred commercial PoC lab
~~~

The project should not jump directly to a working local scanner, live test harness,
or customer-like model environment.

## Compatibility note

The project should not jump directly to a working local scanner, live test harness, or customer-like model environment.

The same meaning may also appear in wrapped Markdown prose, but this exact line is retained for validation compatibility.

## Rationale

A local assessment lab is valuable, but the project should first preserve a clear
distinction between:

- documentation-only lab planning,
- static fixtures,
- dry-run behavior,
- localhost-only controlled behavior,
- commercial PoC readiness,
- production deployment.

The current evidence supports planning and validation. It does not yet support
localhost-only controlled execution.

This decision reduces the risk of:

- treating a demo as scan authorization,
- treating local validation as runtime readiness,
- creating a lab that appears customer-target capable,
- enabling tools before allowed and denied action taxonomy is explicit,
- producing artifacts that imply production readiness,
- weakening public claim boundaries.

## Decision options considered

| Option | Decision | Reason |
| --- | --- | --- |
| No local lab yet | Not selected | Too conservative; the project needs a model path to guide future work |
| Documentation-only local lab | Selected | Safest next step; clarifies target, scope, evidence, and non-goals |
| Static fixture local lab | Deferred | Useful later, but should follow the lab profile and action taxonomy |
| Dry-run local lab | Deferred | Useful later, but should follow profile, taxonomy, and demo planning |
| Localhost-only controlled lab | Rejected for now | Too close to execution before concrete preflight checks and action taxonomy mature |
| Deferred commercial PoC lab | Rejected for now | Too early; commercial PoC readiness remains later work |

## Selected maturity level

The selected maturity level is:

~~~text
L0-L1: Concept recorded and documentation-only profile planning.
~~~

The decision does not advance the local lab to:

~~~text
L2 Local validation
L3 Dry-run behavior
L4 Local-only controlled behavior
L5 Reviewed PoC candidate
L6 Commercial deployment candidate
~~~

A future checkpoint may advance maturity, but only after evaluation criteria and
safety boundaries remain satisfied.

## Local lab profile scope

The documentation-only local lab profile should define:

- target mode,
- target ownership,
- network boundary,
- allowed action categories,
- denied action categories,
- preflight evidence requirements,
- human review requirements,
- generated output directory,
- artifact handling boundary,
- public claim boundary,
- what the lab does not prove.

The profile must remain local-only and non-executing at this stage.

## Local-only assumptions

Future local lab planning must assume:

| Assumption | Required value |
| --- | --- |
| Target mode | localhost-only or documentation-only |
| Target ownership | owned lab target only |
| Third-party target | not allowed |
| Customer target | not allowed |
| External network testing | not allowed |
| Runtime execution | not allowed |
| Scan execution | not allowed |
| Credential injection | not allowed |
| Raw sensitive artifact capture | not allowed |
| Generated outputs | under `private-not-in-git/` |
| Public claims | conservative and evidence-backed |

## Allowed artifacts for the next phase

The next phase may add:

- documentation-only local lab profile,
- local lab target profile template,
- allowed and denied action taxonomy draft,
- preflight evidence requirement draft,
- dry-run scenario plan,
- demo walkthrough plan,
- generated-output directory plan,
- review checklist,
- "what this lab does not prove" section,
- local validation for documentation consistency.

These artifacts may be committed if they are public-safe and do not contain secrets,
customer information, live target details, or sensitive vulnerability material.

## Prohibited behavior

This decision prohibits:

- live vulnerability scanning,
- external network testing,
- customer-target testing,
- real credential injection,
- raw sensitive artifact capture,
- production deployment,
- managed-service operation,
- multi-tenant SaaS operation,
- automatic delivery to customers,
- public claims of scan authorization,
- public claims of production readiness,
- public claims of compliance certification,
- public claims of legal approval,
- public claims of audit opinion.

## Entry criteria for future dry-run lab

Before a dry-run local lab is allowed, complete:

1. documentation-only local lab profile,
2. allowed and denied action taxonomy,
3. preflight evidence requirement model,
4. human review requirement model,
5. generated-output private artifact policy,
6. demo purpose statement,
7. demo non-proof statement,
8. local validation test,
9. public claim boundary review.

Dry-run behavior must not produce real external effects.

## Entry criteria for future localhost-only controlled behavior

Before localhost-only controlled behavior is considered, complete:

1. dry-run lab validation,
2. concrete preflight checks,
3. explicit local-only target binding,
4. explicit action authorization model,
5. explicit deny-by-default behavior,
6. explicit no-credential-injection policy,
7. explicit no-external-network policy,
8. explicit evidence retention policy,
9. explicit human review workflow,
10. explicit rollback and cleanup plan.

Even then, localhost-only controlled behavior must remain separate from customer
target operation and commercial PoC readiness.

## Exit criteria for this decision

This decision is successful if it makes the next step clearer without enabling
execution.

Exit criteria:

- the local lab path is selected conservatively,
- rejected options are explicit,
- allowed next artifacts are explicit,
- prohibited behavior is explicit,
- dry-run entry criteria are explicit,
- localhost-only controlled behavior entry criteria are explicit,
- runtime and scanning boundaries remain disabled,
- public claims remain conservative,
- all local checks pass.

## Impact on v0.6.x sequence

This decision updates the practical v0.6.x sequence:

~~~text
v0.6.4 Local Assessment Lab Decision Record
v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy
v0.6.6 Demo Scenario and Reviewer Walkthrough Planning
v0.6.7 Runtime Gate Hardening Plan
v0.6.8 Evidence and Report UX Improvement Plan
v0.6.9 Dry-Run Local Lab Decision, only if prior criteria are satisfied
~~~

The earlier idea of going directly to a controlled local lab remains deferred.

## Commercial implication

This decision improves future product explanation, but it does not create a
commercial PoC.

Commercial PoC readiness remains future work and requires:

- separate commercial scope,
- separate commercial agreement or licensing discussion,
- target authorization model,
- human review model,
- evidence retention model,
- data handling boundary,
- delivery authorization model,
- vulnerability disclosure boundary,
- support boundary,
- operational rollback plan,
- public claim boundary.

## Public claim boundary

Allowed public language:

- "local assessment lab decision record",
- "documentation-only local lab profile",
- "dry-run planning allowed as future work",
- "localhost-only controlled execution is deferred",
- "runtime execution remains blocked",
- "scan execution remains blocked",
- "customer-target operation remains blocked."

Avoid public language that implies:

- live scanning,
- customer-target authorization,
- production deployment,
- managed service readiness,
- commercial PoC readiness,
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

Before tagging v0.6.4, verify:

1. README links to this checkpoint.
2. Decision summary is recorded.
3. Selected and rejected options are recorded.
4. Selected maturity level is recorded.
5. Local lab profile scope is recorded.
6. Local-only assumptions are recorded.
7. Allowed artifacts are recorded.
8. Prohibited behavior is recorded.
9. Dry-run entry criteria are recorded.
10. Localhost-only controlled behavior entry criteria are recorded.
11. Exit criteria are recorded.
12. v0.6.x sequence impact is recorded.
13. Commercial implication is recorded.
14. Runtime and scanning boundaries remain disabled.
15. Claims to avoid are recorded.
16. `tools/run_all_local_checks.py` includes the v0.6.4 local assessment lab decision test.

## Out of scope

This checkpoint does not:

- build a local lab,
- add static lab fixtures,
- add dry-run lab execution,
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
