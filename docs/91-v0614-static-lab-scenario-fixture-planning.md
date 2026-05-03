# v0.6.14 Static Lab Scenario Fixture Planning

Version: v0.6.14 candidate  
Status: static lab scenario fixture planning; does not authorize runtime execution

## Purpose

This checkpoint defines static lab scenario fixture planning for AAEF-AI-VA.

v0.6.10 through v0.6.13 created a staged path for safe Docker lab planning without
execution. This checkpoint defines how future static scenario fixtures can connect
candidate profile, static design sketch, AI request, gate decision, expected evidence,
reviewer walkthrough, and non-proof boundaries.

This checkpoint is static scenario fixture planning only.

This checkpoint does not authorize Docker Compose file creation, Docker execution,
image pull, container startup, port binding, runtime execution, scanning, credential
injection, customer-target operation, production deployment, certification, legal
approval, or audit opinion.

## Public-safe design boundary

The public planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Static fixtures are not runtime records.
- Static fixtures are not live evidence records.
- Static fixtures are not customer deliverables.
- Static fixtures must use synthetic, non-customer, non-secret data.
- No Docker Compose file is created by this checkpoint.
- No Docker image is pulled by this checkpoint.
- No container is started by this checkpoint.
- No port is opened by this checkpoint.
- No scanner is run by this checkpoint.
- Docker execution remains blocked.
- Runtime execution remains blocked.
- Scan execution remains blocked.
- External network testing remains blocked.
- Customer-target operation remains blocked.
- Report delivery remains separately gated.

The planning must not expose private advanced feature details, protected private
review materials, market-comparison materials, or confidential commercial strategy.

## Planning proposition

~~~text
A future static lab scenario fixture set can show the reviewable relationship between
candidate profile, static sketch, approved diagnostic context, AI-generated request,
gate decision, expected evidence, reviewer questions, and non-proof boundaries before
any runnable configuration or execution path exists.
~~~

This proposition is intentionally non-executing.

It creates a reviewable scenario layer before implementation.

## Static fixture set model

A future static fixture set should include:

| Fixture | Purpose |
| --- | --- |
| `fixture_manifest` | Lists fixture nodes and scenario metadata |
| `candidate_profile_fixture` | References local lab candidate profile planning |
| `static_sketch_fixture` | References static Compose design sketch planning |
| `diagnostic_context_fixture` | Describes approved synthetic diagnostic context |
| `ai_request_fixture` | Shows non-authoritative `tool_action_request` |
| `gate_decision_fixture` | Shows gate decision and reason |
| `expected_evidence_fixture` | Shows expected evidence categories |
| `reviewer_question_fixture` | Shows reviewer questions |
| `non_proof_fixture` | Shows what is not demonstrated |
| `scenario_trace_fixture` | Links nodes into a reviewable trace |

These fixtures are planning concepts at this checkpoint.

They are not generated artifacts yet.

## Fixture manifest model

A fixture manifest should include:

| Field | Purpose |
| --- | --- |
| `scenario_fixture_id` | Stable fixture-set identifier |
| `scenario_name` | Human-readable scenario name |
| `scenario_status` | Static planning status |
| `candidate_profile_ref` | Link to candidate profile planning |
| `static_sketch_ref` | Link to static sketch planning |
| `fixture_nodes` | Ordered fixture nodes |
| `synthetic_data_statement` | Confirms synthetic-only data |
| `execution_boundary_statement` | Confirms no execution |
| `reviewer_walkthrough_ref` | Link to walkthrough planning |
| `non_proof_statement_ref` | Link to non-proof boundary |
| `advancement_state` | Whether fixture may advance |

A fixture manifest is not an execution manifest.

## Fixture node status model

Fixture nodes should use conservative status values:

| Status | Meaning |
| --- | --- |
| `not_created` | Fixture node does not exist |
| `planned` | Fixture node is planned |
| `draft_for_review` | Fixture node draft may be reviewed |
| `requires_human_review` | Human review required |
| `blocked_missing_linkage` | Required linkage is missing |
| `blocked_by_runtime_implication` | Runtime implication blocks advancement |
| `blocked_by_sensitive_content` | Sensitive content concern blocks advancement |
| `accepted_for_static_review` | Accepted for static review only |
| `not_approved_for_execution` | Execution remains blocked |

This checkpoint should keep fixture status at static-review-only values.

## Candidate-to-sketch linkage

The fixture set should link candidate profile and static sketch without selecting a
target for execution.

The linkage should show:

- candidate profile reference,
- static sketch reference,
- local-only or isolated network intent,
- candidate-only status,
- non-runnable sketch status,
- synthetic data posture,
- credential exclusion posture,
- human review requirement,
- execution-blocked state.

Candidate-to-sketch linkage is not target selection.

## Diagnostic context fixture boundary

The diagnostic context fixture may describe approved synthetic context.

Allowed planning-level content includes:

- synthetic target label,
- candidate profile summary,
- static sketch summary,
- local-only assumption,
- missing information,
- uncertainty notes,
- expected evidence categories,
- human review recommendation.

The fixture must not include real customer data, real secrets, real tokens, raw live
scan output, or private advanced feature details.

## AI request fixture boundary

The AI request fixture may show a non-authoritative `tool_action_request`.

It should include:

- requested action category,
- candidate target reference,
- rationale,
- expected evidence,
- uncertainty,
- safety notes,
- human review recommendation.

The AI request fixture does not authorize execution.

## Gate decision fixture boundary

The gate decision fixture should show:

- scope binding result,
- target binding result,
- static sketch review result,
- action taxonomy result,
- preflight evidence result,
- human review requirement,
- execution authorization result,
- reason execution remains blocked.

The gate decision fixture should keep execution authorization false.

## Expected evidence fixture boundary

Expected evidence may include:

- candidate profile evidence,
- static sketch evidence,
- non-runnable syntax evidence,
- network boundary evidence,
- port binding intent evidence,
- synthetic data evidence,
- credential exclusion evidence,
- expected review evidence,
- non-proof evidence.

Expected evidence is not live evidence.

## Scenario trace model

A scenario trace should link:

~~~text
candidate_profile_fixture
  -> static_sketch_fixture
  -> diagnostic_context_fixture
  -> ai_request_fixture
  -> gate_decision_fixture
  -> expected_evidence_fixture
  -> reviewer_question_fixture
  -> non_proof_fixture
~~~

The trace is a review aid.

The trace is not proof of live execution.

## Reviewer walkthrough linkage

The static fixture set should support reviewer questions:

- Which candidate profile is referenced?
- Which static sketch is referenced?
- What synthetic context was approved?
- What did AI request?
- Which gate evaluated the request?
- Why did execution remain blocked?
- What evidence would be expected?
- What information is missing?
- What human review is required?
- What does the fixture not prove?

These questions support review without claiming lab readiness.

## Fixture validation expectations

Future fixture validation should confirm:

- required fixture nodes are present,
- fixture IDs are stable,
- references are internally consistent,
- synthetic data statement is present,
- non-execution boundary is present,
- no runnable Compose syntax is present,
- no image pull instruction is present,
- no container startup instruction is present,
- no scanner command is present,
- no real credentials are present,
- no customer data is present,
- execution markers remain false,
- non-proof statement is present.

Validation should not convert fixtures into execution artifacts.

## Generated artifact boundary

Future static fixture outputs should remain under private output paths unless a
separate public-safe decision is made.

Allowed private candidate paths may include:

~~~text
private-not-in-git/static-lab-scenario-fixtures/
private-not-in-git/static-lab-scenario-traces/
private-not-in-git/static-lab-fixture-reviews/
private-not-in-git/static-lab-fixture-advancement-gates/
~~~

Public repository content should contain planning, not generated private fixture
outputs.

## What this checkpoint does not prove

This checkpoint does not prove:

- static fixtures have been generated,
- Docker Compose files can be created,
- Docker images can be pulled,
- containers can be started,
- ports can be bound,
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

## Relationship to v0.6.13

v0.6.13 defined static Compose design sketch and network boundary review.

v0.6.14 defines how future static scenario fixtures can reference that sketch without
creating runnable configuration or execution paths.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.15 Static Fixture Schema and Validator Planning
~~~

Rationale:

- v0.6.14 defines fixture planning.
- The next safe step is to define static fixture schema and validator planning before
  generating or committing sample fixture artifacts.
- Bounded local execution should remain deferred until profile, preflight, design,
  network, fixture, schema, validator, and review gates are documented.

## Public claim boundary

Allowed public language:

- "static lab scenario fixture planning",
- "non-executing fixture set",
- "fixture manifest",
- "scenario trace",
- "AI request fixture",
- "gate decision fixture",
- "expected evidence fixture",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies Docker execution, Compose file creation, image pull,
container startup, port binding, live scanning, automated exploitation, autonomous
testing, customer-target authorization, external network testing authorization,
production deployment, managed service readiness, commercial PoC readiness,
compliance certification, legal approval, audit opinion, external framework
equivalence, commercial license grant, or private advanced feature details.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
fixture_generated = false
fixture_live_evidence = false
static_sketch_runnable = false
docker_compose_file_created = false
docker_compose_executed = false
docker_image_pulled = false
container_started = false
port_bound = false
docker_execution_authorized = false
candidate_selected_for_execution = false
preflight_evidence_collected = false
preflight_satisfied = false
execution_authorized = false
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

Do not claim that this checkpoint provides generated fixtures, live evidence,
runnable Compose configuration, Docker Compose file creation, Docker execution
approval, image pull approval, container startup approval, port binding approval,
production deployment approval, runtime execution readiness, scan authorization,
customer-target authorization, compliance certification, legal approval, audit
opinion, completed legal review, completed dependency audit, managed service
approval, commercial license grant, safety guarantee, external framework equivalence,
audit sufficiency, or delivery authorization.

## Required local checks

Before tagging v0.6.14, verify README linkage, public-safe boundary, fixture set
model, fixture manifest model, node status model, candidate-to-sketch linkage,
diagnostic context boundary, AI request boundary, gate decision boundary, expected
evidence boundary, scenario trace model, reviewer linkage, fixture validation
expectations, generated artifact boundary, false runtime markers, and
`tools/run_all_local_checks.py` registration.

## Out of scope

This checkpoint does not generate fixture files, commit sample fixture artifacts,
install Docker, run Docker, pull images, start containers, bind ports, create Docker
Compose files, create a runnable Compose design, build a local lab, select a target
for execution, collect live preflight evidence, satisfy preflight, add dry-run lab
execution, enable runtime execution, enable scanning, add new scanner integrations,
create generated sample evidence artifacts, create generated sample report artifacts,
authorize report delivery, expose private advanced feature details, create private
sales material, publish pricing, create a commercial contract, provide legal advice,
authorize external network testing, authorize credential injection, or authorize
customer-target testing.
