# v0.6.10 Safe Docker Lab Roadmap and Local Target Candidate Planning

Version: v0.6.10 candidate  
Status: safe Docker lab roadmap and local target candidate planning; does not authorize runtime execution

## Purpose

This checkpoint defines a safe Docker lab roadmap and local target candidate plan for
AAEF-AI-VA.

v0.6.8 defined a non-executing reviewer walkthrough. v0.6.9 defined evidence
reconstruction and sample report demonstration planning. The next design step is to
identify how a future local lab may be planned without jumping directly into
execution.

This checkpoint is roadmap and candidate planning only.

This checkpoint does not authorize Docker execution, runtime execution, scanning,
credential injection, customer-target operation, production deployment,
certification, legal approval, or audit opinion.

## Public-safe design boundary

The public roadmap must stay within public-safe AAEF-AI-VA principles:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Local target candidates must be scoped, authorized, and evidenced before any later advancement.
- Docker lab candidates must remain localhost-only or documentation-only until a later explicit checkpoint changes scope.
- Runtime execution remains blocked.
- Scan execution remains blocked.
- External network testing remains blocked.
- Customer-target operation remains blocked.
- Report delivery remains separately gated.

The roadmap must not expose private advanced feature details, protected private
review materials, market-comparison materials, or confidential commercial strategy.

## Roadmap proposition

The roadmap proposition is:

~~~text
A future safe Docker lab may provide local-only, intentionally vulnerable targets for
demonstrating gated AI-assisted vulnerability-assessment workflows, but this checkpoint
only plans candidates and guardrails. It does not run containers, run scanners, or
authorize execution.
~~~

The roadmap is intentionally non-executing.

It explains how local lab work could be staged safely before any bounded execution
work is considered.

## Candidate local targets

Candidate targets may include intentionally vulnerable local applications:

| Candidate | Candidate use | Current status |
| --- | --- | --- |
| DVWA | Classic web vulnerability training target | Candidate only |
| OWASP Juice Shop | Modern web application training target | Candidate only |
| WebGoat | Web application training target | Candidate only |
| Synthetic local API | Future synthetic API target | Candidate only |
| Static fixture target | Non-running fixture-based target | Candidate only |

Candidate only means:

- not installed,
- not run,
- not scanned,
- not integrated,
- not treated as authorized execution.

## Candidate acceptance criteria

A local target candidate should not advance unless it satisfies:

| Criterion | Required posture |
| --- | --- |
| Ownership | Operator-controlled local environment only |
| Network boundary | Localhost-only or isolated Docker network only |
| External network | Disabled or explicitly unnecessary |
| Customer data | Not present |
| Secrets | Not present |
| Credentials | Synthetic only |
| Reset behavior | Documented reset or teardown path |
| Licensing | Reviewable before inclusion |
| Resource profile | Reasonable for local workstation use |
| Safety posture | Intentionally vulnerable lab target, not a real system |
| Evidence posture | Demonstration evidence only |
| Public claim posture | No production, compliance, audit, or safety guarantee claims |

Failure to meet these criteria should keep the candidate blocked.

## Candidate exclusion criteria

A target candidate should be excluded or deferred if it:

- requires external network testing,
- requires customer data,
- requires real credentials,
- requires sensitive secrets,
- requires privileged host access beyond the lab design,
- creates uncontrolled outbound traffic,
- has unclear licensing,
- cannot be reset cleanly,
- cannot be bounded to local-only operation,
- encourages unsafe use against third-party systems,
- creates public claims that exceed demonstration scope.

Exclusion is a safety feature.

## Phased safe Docker lab roadmap

The safe Docker lab roadmap should proceed in phases:

| Phase | Name | Scope |
| --- | --- | --- |
| L0 | Candidate planning | Identify local candidates and guardrails |
| L1 | Static lab profile | Record candidate profiles without execution |
| L2 | Compose design review | Review non-running Docker Compose design |
| L3 | Preflight model review | Define preflight evidence for local-only use |
| L4 | Dry-run planning | Plan request and gate records without starting containers |
| L5 | Bounded local execution proposal | Propose narrow local-only execution for later review |
| L6 | Bounded local execution implementation | Deferred until separate explicit checkpoint |
| L7 | Demonstration packet | Deferred until evidence and report boundaries are validated |

This checkpoint covers L0 only.

It may describe later phases, but it does not authorize them.

## Required preflight evidence for future advancement

Before any future local lab execution is considered, preflight evidence should include:

| Evidence | Purpose |
| --- | --- |
| `local_target_profile` | Confirms target candidate and local-only mode |
| `target_ownership_statement` | Confirms operator-controlled lab |
| `network_isolation_statement` | Confirms local-only or isolated Docker network boundary |
| `external_network_block_statement` | Confirms external network testing is not allowed |
| `synthetic_data_statement` | Confirms no customer data or secrets |
| `credential_policy` | Confirms synthetic credentials only |
| `reset_teardown_plan` | Confirms cleanup and reset path |
| `resource_limit_plan` | Confirms bounded CPU, memory, storage, and time expectations |
| `tool_action_taxonomy_mapping` | Confirms allowed and denied local actions |
| `human_review_checkpoint` | Confirms review before advancement |
| `non_proof_statement` | Confirms what the lab does not prove |

Preflight evidence planning is not execution authorization.

## Human review expectations

Human review should be required before:

- adding a new local target candidate,
- approving a non-running Docker Compose design,
- changing network boundaries,
- changing credential assumptions,
- changing resource limits,
- changing allowed action categories,
- moving from static planning to dry-run planning,
- moving from dry-run planning to bounded local execution proposal,
- treating any output as report evidence,
- publishing any lab-related public claim.

Human review remains a gate.

## Network boundary requirements

Future safe Docker lab work should preserve:

- localhost-only access,
- no customer target,
- no third-party target,
- no external network testing,
- no uncontrolled outbound traffic,
- no public internet scanning,
- no credential injection into real systems,
- no raw sensitive artifact capture from real systems.

If a later lab design requires network access for dependency installation, image pull,
or update behavior, that should be documented separately from assessment activity.

## Tool interaction boundary

A future lab may eventually demonstrate candidate tool requests, but this checkpoint
does not authorize tools to run.

Tool-related planning should preserve:

- AI may propose `tool_action_request`,
- Tool Gateway evaluates request boundaries,
- authorization remains false unless later explicit work changes scope,
- preflight remains unsatisfied in this checkpoint,
- scan execution remains blocked,
- real execution remains blocked,
- expected evidence may be described,
- generated artifacts remain private until a public-safe artifact decision is made.

## Generated artifact boundary

Future lab-generated outputs should remain under private output paths unless a
separate public-safe decision is made.

Allowed private candidate paths may include:

~~~text
private-not-in-git/local-lab-roadmaps/
private-not-in-git/local-target-candidates/
private-not-in-git/docker-lab-design-reviews/
private-not-in-git/local-lab-preflight-reviews/
private-not-in-git/local-lab-dry-run-plans/
~~~

Public repository content should contain planning, not generated private lab outputs.

## Synthetic data requirement

Any future local lab demonstration should use synthetic, non-customer, non-secret,
non-live data.

Synthetic lab data should avoid:

- real customer names,
- real target hostnames,
- real customer IP addresses,
- real credentials,
- real tokens,
- real assessment output from customer systems,
- raw sensitive artifacts from real systems,
- customer deliverable content,
- private advanced feature details.

## What this roadmap does not prove

The safe Docker lab roadmap does not prove:

- Docker lab execution works,
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
- audit sufficiency exists,
- delivery authorization exists,
- safety is guaranteed.

This non-proof statement should remain visible in future lab planning.

## Relationship to v0.6.5

v0.6.5 defined the documentation-only local lab profile and action taxonomy.

v0.6.10 uses that boundary to keep Docker lab work at candidate planning level.

## Relationship to v0.6.6

v0.6.6 defined:

~~~text
AI generates tool_action_request.
Gates decide execution.
~~~

A future Docker lab may help demonstrate that proposition, but this checkpoint does
not execute requests.

## Relationship to v0.6.7

v0.6.7 defined observation normalization and Diagnostic Fidelity Risk.

Any future lab observation should preserve approved diagnostic context boundaries,
normalization loss records, and sufficiency criteria.

## Relationship to v0.6.8 and v0.6.9

v0.6.8 and v0.6.9 defined reviewer walkthrough, evidence reconstruction, and sample
report demonstration planning.

v0.6.10 prepares a future local target roadmap that may eventually support those
demonstrations without changing their non-execution boundary.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning
~~~

Rationale:

- v0.6.10 defines the safe Docker lab roadmap and candidate criteria.
- The next step should define a concrete local lab candidate profile and preflight
  evidence planning without running Docker or scanners.
- Bounded local execution should remain deferred until candidate profiles, preflight
  evidence, network boundaries, and review gates are documented.

## Public claim boundary

Allowed public language:

- "safe Docker lab roadmap",
- "local target candidate planning",
- "intentionally vulnerable local targets",
- "candidate only",
- "localhost-only or isolated Docker network planning",
- "preflight evidence planning",
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
docker_execution_authorized = false
container_started = false
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
delivery_authorized = false
customer_deliverable = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- Docker execution approval,
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
- audit sufficiency,
- delivery authorization.

## Required local checks

Before tagging v0.6.10, verify:

1. README links to this checkpoint.
2. Public-safe design boundary is recorded.
3. Roadmap proposition is recorded.
4. Candidate local targets are recorded.
5. Candidate acceptance criteria are recorded.
6. Candidate exclusion criteria are recorded.
7. Phased safe Docker lab roadmap is recorded.
8. Required preflight evidence is recorded.
9. Human review expectations are recorded.
10. Network boundary requirements are recorded.
11. Tool interaction boundary is recorded.
12. Generated artifact boundary is recorded.
13. Synthetic data requirement is recorded.
14. Non-proof statement is recorded.
15. Runtime, scanning, Docker execution, and delivery boundaries remain disabled.
16. Claims to avoid are recorded.
17. `tools/run_all_local_checks.py` includes the v0.6.10 safe Docker lab roadmap test.

## Out of scope

This checkpoint does not:

- install Docker,
- run Docker,
- pull images,
- start containers,
- create Docker Compose files,
- build a local lab,
- add static demo fixtures,
- add dry-run lab execution,
- enable runtime execution,
- enable scanning,
- add new scanner integrations,
- create generated sample evidence artifacts,
- create generated sample report artifacts,
- authorize report delivery,
- expose private advanced feature details,
- create private sales material,
- publish pricing,
- create a commercial contract,
- provide legal advice,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
