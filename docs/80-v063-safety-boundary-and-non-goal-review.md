# v0.6.3 Safety Boundary and Non-Goal Review

Version: v0.6.3 candidate  
Status: safety boundary and non-goal review; does not authorize runtime execution

## Purpose

This checkpoint reconfirms the safety boundaries and non-goals for AAEF-AI-VA
before the project proceeds toward local assessment lab decisioning, demo
walkthroughs, runtime gate hardening, evidence/report UX work, or commercial PoC
readiness.

v0.6.0 established work ordering. v0.6.1 inventoried capabilities and maturity.
v0.6.2 defined evaluation criteria and acceptance gates. v0.6.3 now restates what
must remain blocked unless a later explicit decision changes the boundary.

This checkpoint is boundary review only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Core safety statement

AAEF-AI-VA remains a safety-first reference implementation for AI-assisted
vulnerability assessment control boundaries.

AI output is not authority to perform assessment actions.

Model output may propose or request an assessment-related action, but action
execution must remain gated by authorization, scope, preflight evidence, Tool Gateway
behavior, human review, and delivery authorization.

## Hard non-goals

The following are hard non-goals for the current public repository:

| Non-goal | Current status |
| --- | --- |
| Production vulnerability scanner | Not provided |
| Autonomous vulnerability scanner | Not provided |
| Live scanning | Not authorized |
| External network testing | Not authorized |
| Customer-target operation | Not authorized |
| Credential injection against real systems | Not authorized |
| Production deployment | Not demonstrated |
| Managed security service operation | Not demonstrated |
| Multi-tenant SaaS operation | Not demonstrated |
| Compliance certification | Not provided |
| Legal approval | Not provided |
| Audit opinion | Not provided |
| External framework equivalence | Not claimed |
| Commercial license grant | Not granted by repository |

These non-goals must remain visible in future planning, demos, and public
communication.

## Intentionally blocked capabilities

The following capabilities remain intentionally blocked:

~~~text
runtime execution
network activity
scan execution
credential injection
raw artifact capture
customer-target operation
external network testing
production deployment
managed-service operation
multi-tenant SaaS operation
~~~

These blocks are not defects. They are part of the current safety posture.

## Safety boundary inventory

| Boundary | Required current state | Reason |
| --- | --- | --- |
| Runtime execution | Blocked | Prevents AI request from becoming action authority |
| Network activity | Blocked | Prevents uncontrolled external effects |
| Scan execution | Blocked | Prevents unauthorized assessment activity |
| Credential injection | Blocked | Prevents unsafe use of credentials |
| Raw artifact capture | Blocked | Prevents accidental sensitive artifact capture |
| Customer-target operation | Blocked | Requires separate scope, authorization, and agreement |
| External network target | Blocked | Prevents third-party testing implication |
| Production deployment | Not demonstrated | Requires separate engineering and operational review |
| Commercial PoC operation | Future work | Requires separate commercial and safety boundary review |
| Public claims | Conservative | Prevents unsupported readiness claims |

## Non-goal preservation rules

Future work must preserve these rules:

1. Do not describe the repository as a live scanner.
2. Do not describe dry-run behavior as scan execution.
3. Do not describe local validation as production readiness.
4. Do not describe generated private outputs as customer evidence.
5. Do not describe human review gates as legal approval.
6. Do not describe delivery authorization examples as customer delivery approval.
7. Do not describe AGPL-3.0 public use as a separate commercial license.
8. Do not describe public documentation as managed-service readiness.
9. Do not describe framework mapping as certification or equivalence.
10. Do not describe local-only planning as customer-target authorization.

## Fail-closed requirements

The project should fail closed when:

- scope is missing,
- target binding is missing,
- target mode is external or customer-like,
- authorization is missing,
- preflight evidence is missing,
- human review is required but absent,
- credential material is requested,
- raw artifact capture is requested,
- scan execution is requested without an explicit future authorization model,
- delivery authorization is missing,
- public claims exceed demonstrated maturity.

Fail-closed behavior should produce evidence or review records where possible.

## Local lab constraints

A future local assessment lab must remain constrained by these conditions:

- local-only or localhost-only target mode,
- owned lab target only,
- no third-party target,
- no customer target,
- no external network testing,
- no real credential injection,
- no raw sensitive artifact capture,
- generated outputs under `private-not-in-git/`,
- explicit allowed and denied action taxonomy,
- explicit preflight evidence requirements,
- explicit human review requirements,
- explicit statement of what the lab does not prove.

A local lab decision record must exist before building or expanding the lab.

## Demo constraints

A future demo must:

- state its purpose,
- state what it proves,
- state what it does not prove,
- map to capability inventory,
- map to evaluation criteria,
- avoid live scan implication,
- avoid customer-target implication,
- avoid production-readiness implication,
- keep generated outputs under `private-not-in-git/` where applicable,
- preserve human review and delivery authorization boundaries,
- preserve public claim safety.

A demo must not be presented as production deployment, certification, legal approval,
audit opinion, safety guarantee, or customer authorization.

## Runtime gate hardening constraints

Runtime gate hardening may improve detection, review, evidence, and blocking logic.

Runtime gate hardening must not be treated as runtime enablement.

Allowed hardening direction:

- clearer target binding checks,
- clearer preflight requirements,
- clearer deny reasons,
- clearer evidence records,
- clearer human review outcomes,
- clearer unsafe action categories,
- clearer private artifact handling,
- stronger regression tests.

Not allowed without later explicit authorization:

- enabling live scan execution,
- enabling external network activity,
- enabling credential injection,
- enabling customer-target operation,
- enabling production service behavior.

## Commercial PoC constraints

Commercial PoC readiness remains future work.

Before commercial PoC planning can advance, the project must have:

- commercial scope boundary,
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

Commercial PoC readiness must not be inferred from this checkpoint.

## Unsafe implication checklist

Review future changes for unsafe implications:

| If a change says... | Check that it does not imply... |
| --- | --- |
| local lab | customer target |
| dry-run | live scan |
| validation | certification |
| review gate | legal approval |
| delivery gate | customer delivery authorization |
| evidence | audit sufficiency |
| commercial inquiry | commercial license grant |
| framework mapping | external framework equivalence |
| runtime gate | runtime execution enabled |
| local target | external network target |

## Compatibility note

Negative guidance may name unsafe implications so reviewers know what not to infer. Validation should reject concrete positive claims that say this checkpoint or repository enables runtime behavior, not the mere presence of short unsafe terms when they appear in an unsafe implication checklist or claims-to-avoid guidance.

## Compatibility note

The unsafe implication checklist intentionally names short unsafe phrases so reviewers know what not to infer. Validation should reject concrete positive claims that say this checkpoint or repository enables runtime behavior, not checklist entries that explain unsafe implications to avoid. These phrases are allowed in negative guidance. Validation should reject concrete positive claims that say this checkpoint or repository enables runtime behavior, not checklist entries that explain unsafe implications to avoid.

## Advancement conditions

The project may advance only when:

1. the changed capability is named,
2. the maturity movement is stated,
3. evidence exists,
4. safety boundaries remain intact,
5. public claims remain conservative,
6. private outputs remain private,
7. human review remains preserved where required,
8. commercial implications are separated from public use,
9. all local checks pass,
10. the next decision becomes clearer.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.4 Local Assessment Lab Decision Record
~~~

Rationale:

- v0.6.0 defined work ordering.
- v0.6.1 inventoried capabilities.
- v0.6.2 defined evaluation criteria.
- v0.6.3 reconfirms safety boundaries and non-goals.
- v0.6.4 can now decide whether the local lab path should be no-lab, documentation-only, static fixture, dry-run, localhost-only controlled lab, or deferred commercial PoC lab.

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

Before tagging v0.6.3, verify:

1. README links to this checkpoint.
2. Core safety statement is recorded.
3. Hard non-goals are recorded.
4. Intentionally blocked capabilities are recorded.
5. Safety boundary inventory is recorded.
6. Non-goal preservation rules are recorded.
7. Fail-closed requirements are recorded.
8. Local lab constraints are recorded.
9. Demo constraints are recorded.
10. Runtime gate hardening constraints are recorded.
11. Commercial PoC constraints are recorded.
12. Unsafe implication checklist is recorded.
13. Advancement conditions are recorded.
14. Runtime and scanning boundaries remain disabled.
15. Claims to avoid are recorded.
16. `tools/run_all_local_checks.py` includes the v0.6.3 safety boundary/non-goal review test.

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
