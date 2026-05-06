# v0.6.26 Reviewer Walkthrough and Five Questions Mapping

Version: v0.6.26 candidate  
Status: reviewer walkthrough and mapping planning only; does not authorize runtime execution

## Purpose

This checkpoint defines the reviewer walkthrough and AAEF five questions mapping for
AAEF-AI-VA applied evidence work.

v0.6.23 defined the applied evidence package structure. v0.6.24 defined the four
minimum scenarios. v0.6.25 defined the static applied evidence fixture plan. v0.6.26
defines how those planned fixtures should be explained to reviewers before fixture
generation, applied evidence package generation, local-lab diagnostic execution,
scanner execution, or delivery authorization begins.

This checkpoint is reviewer walkthrough and mapping planning only.

This checkpoint does not generate fixture files, generate applied evidence packages,
create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The public walkthrough boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Reviewer walkthrough planning is not fixture generation.
- Reviewer walkthrough planning is not evidence package generation.
- Reviewer walkthrough planning is not scanner execution.
- Static/mock walkthrough examples are not proof of diagnostic accuracy.
- Dispatch and non-dispatch remain separated from gate decision.
- Non-execution evidence is first-class evidence.
- Real local-lab execution remains blocked by this checkpoint.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.

Model output is not authority.

## Walkthrough proposition

~~~text
A reviewer should be able to read the applied evidence package and answer the five
AAEF questions for each scenario without trusting AI output as authority and without
treating static/mock evidence as proof of diagnostic accuracy.
~~~

This proposition is intentionally non-executing.

## Reviewer walkthrough artifact plan

A future reviewer walkthrough should be represented as:

~~~text
applied-evidence-package/
  reviewer_walkthrough.md
  aaef_five_questions_mapping.md
  non_proof_statement.md
  scenarios/
    permitted-safe-diagnostic/
      review_summary.example.md
    denied-out-of-scope-request/
      review_summary.example.md
    human-approval-required/
      review_summary.example.md
    not-executed-expired/
      review_summary.example.md
~~~

This checkpoint does not create those files.

## Walkthrough reader model

The walkthrough should support these readers:

| Reader | What they need |
| --- | --- |
| AAEF reviewer | Request-to-evidence trace and five questions mapping |
| Security architect | Boundary between AI request, gate, dispatch, and execution |
| Risk owner | Whether execution was allowed, blocked, held, or not executed |
| Operator | What action, if any, occurred and what remains blocked |
| Legal/compliance reviewer | Non-proof statements and no certification / no legal sufficiency boundaries |

The walkthrough should be understandable without reading source code.

## Common walkthrough sequence

Each scenario walkthrough should use the same sequence:

1. State the scenario id.
2. State what the AI requested.
3. State why the request is not authority.
4. State what the gate decided.
5. State whether dispatch occurred.
6. State whether execution occurred.
7. State what evidence artifact proves the outcome.
8. Answer the five AAEF questions.
9. State what the scenario does not prove.

JSON files alone are not enough.

## AAEF five questions

The walkthrough must answer:

| AAEF question | Required answer source |
| --- | --- |
| Who or what acted? | `tool_action_request`, gateway identity, `dispatch_decision` |
| On whose behalf? | principal context and operator context in `tool_action_request` |
| With what authority? | `gate_decision`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision`, execution boundary, result artifact |
| What evidence proves what happened? | `evidence_event`, result artifact, `review_summary` |

These questions should be answered for all four scenarios.

## Artifact-to-question mapping

The future mapping should connect each artifact to reviewer questions:

| Artifact | Reviewer use |
| --- | --- |
| `tool_action_request.example.json` | Shows AI-generated intent and actor/principal context |
| `gate_decision.example.json` | Shows authority decision and policy/rule basis |
| `dispatch_decision.example.json` | Shows whether Tool Gateway dispatched or blocked |
| `execution_result.example.json` | Shows permitted execution result in safe/static context |
| `non_execution_result.example.json` | Shows denied, held, expired, or not-executed outcome |
| `evidence_event.example.json` | Links request, decision, dispatch, and result |
| `review_summary.example.md` | Human-readable scenario explanation |
| `non_proof_statement.example.md` | Boundaries of what is not proven |

The mapping should not imply audit or legal sufficiency.

## Scenario walkthrough: permitted-safe-diagnostic

Scenario id:

~~~text
permitted-safe-diagnostic
~~~

Reviewer explanation:

- AI requested a safe local-lab diagnostic action.
- The request was not authority.
- The gate evaluated scope, policy, target boundary, and risk posture.
- The gate permitted the request.
- The Tool Gateway dispatch decision recorded dispatch in the safe/static model.
- The result artifact recorded the permitted outcome.
- The evidence event linked the chain.
- The review summary explained why the action was allowed.

Expected reviewer conclusion:

~~~text
The scenario demonstrates traceability for a permitted local-lab-style request. It
does not prove scanner accuracy, production readiness, customer authorization, audit
sufficiency, or legal sufficiency.
~~~

## Scenario walkthrough: denied-out-of-scope-request

Scenario id:

~~~text
denied-out-of-scope-request
~~~

Reviewer explanation:

- AI requested an out-of-scope diagnostic action.
- The request was not authority.
- The gate evaluated the request against scope and target boundary.
- The gate denied the request.
- The Tool Gateway dispatch decision recorded non-dispatch.
- The non-execution result recorded the denial reason.
- The evidence event linked the denied request to non-execution evidence.
- The review summary explained why no action occurred.

Expected reviewer conclusion:

~~~text
The scenario demonstrates scope enforcement and evidenced non-execution. It does not
prove vulnerability detection accuracy, customer authorization, or external target
testing readiness.
~~~

## Scenario walkthrough: human-approval-required

Scenario id:

~~~text
human-approval-required
~~~

Reviewer explanation:

- AI requested an action that required human approval.
- The request was not authority.
- The gate evaluated uncertainty, impact, and approval requirements.
- The gate held the request for human approval.
- The Tool Gateway dispatch decision recorded non-dispatch.
- The non-execution result recorded that approval was required.
- The evidence event linked the held request to non-execution evidence.
- The review summary explained what approval would be needed.

Expected reviewer conclusion:

~~~text
The scenario demonstrates that human approval can remain a gate before execution. It
does not prove approval was granted or that runtime execution is ready.
~~~

## Scenario walkthrough: not-executed-expired

Scenario id:

~~~text
not-executed-expired
~~~

Reviewer explanation:

- AI request existed but was no longer executable.
- The request was not authority.
- The gate or lifecycle boundary recorded expiry or not-dispatched status.
- The Tool Gateway dispatch decision recorded non-dispatch.
- The non-execution result recorded expiry or not-execution reason.
- The evidence event linked the expired request to non-execution evidence.
- The review summary explained why no action occurred.

Expected reviewer conclusion:

~~~text
The scenario demonstrates that no-action outcomes are reviewable and evidenced. It
does not imply runtime execution readiness.
~~~

## Scenario outcome explanation matrix

| Scenario | Reviewer should see | Reviewer should not infer |
| --- | --- | --- |
| `permitted-safe-diagnostic` | permitted traceability in safe/static model | scanner accuracy or customer authorization |
| `denied-out-of-scope-request` | scope denial and non-dispatch evidence | external target testing readiness |
| `human-approval-required` | approval gate and held non-execution | human approval already granted |
| `not-executed-expired` | expiry / not-executed evidence | runtime execution readiness |

Non-execution evidence is first-class evidence.

## Five questions mapping by scenario

Every scenario should include a compact mapping table:

| Scenario | Who/what acted? | On whose behalf? | With what authority? | Allowed at execution? | Evidence |
| --- | --- | --- | --- | --- | --- |
| `permitted-safe-diagnostic` | AI request + gateway dispatch | test operator / local lab principal | gate decision permitted | yes, in safe/static or future authorized local-lab model | evidence event + execution result |
| `denied-out-of-scope-request` | AI request + gate denial | test operator / local lab principal | gate decision denied | no; dispatch not attempted | evidence event + non-execution result |
| `human-approval-required` | AI request + gate hold | test operator / local lab principal | human approval required | no; held until approval | evidence event + non-execution result |
| `not-executed-expired` | AI request + lifecycle/gate non-dispatch | test operator / local lab principal | expired / not-dispatched | no; request no longer executable | evidence event + non-execution result |

The mapping is reviewer guidance, not certification.

## Non-proof walkthrough requirements

Each walkthrough should include a non-proof section.

The non-proof section should state that the scenario does not prove:

- vulnerability detection accuracy,
- production readiness,
- implementation conformance,
- audit sufficiency,
- legal sufficiency,
- compliance certification,
- external-framework equivalence,
- customer-target authorization,
- delivery authorization,
- safety guarantee.

Non-proof statements should be visible to reviewers, not buried in JSON only.

## Reviewer acceptance checklist

A reviewer should be able to confirm:

- scenario id is clear,
- request id is linked,
- decision id is linked,
- dispatch decision id is linked,
- result id is linked,
- evidence event id is linked,
- decision result matches dispatch posture,
- dispatch posture matches result artifact,
- non-execution result is present where no execution occurred,
- five AAEF questions are answered,
- non-proof statement is present,
- no customer target is implied,
- no delivery authorization is implied.

This checklist is not an audit opinion.

## Future walkthrough generation readiness

Reviewer walkthrough generation should not begin until:

- this walkthrough planning is accepted,
- static applied evidence fixture planning is accepted,
- scenario artifact naming is accepted,
- identifier linkage rules are accepted,
- non-proof statement requirements are accepted,
- public/private artifact placement is confirmed.

Walkthrough generation should describe static/mock evidence, not live diagnostic evidence.

## Future structural validator planning hooks

A future structural validator should be able to check:

- reviewer walkthrough exists,
- every scenario has a review summary,
- five AAEF questions are answered,
- non-proof section exists,
- scenario ids match fixture ids,
- artifact references are linkable,
- no proof overclaims are present,
- no customer-target implication is present,
- no delivery authorization implication is present.

Validator success must not imply semantic correctness, evidence sufficiency,
assessment sufficiency, production readiness, audit sufficiency, legal sufficiency,
implementation conformance, certification, compliance, or external-framework
equivalence.

## Relationship to v0.6.25

v0.6.25 defined the static fixture artifact plan.

v0.6.26 defines the reviewer walkthrough and AAEF five questions mapping that should
make those future fixture artifacts understandable to reviewers.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.27 Applied Evidence Structural Validator Planning
~~~

Rationale:

- v0.6.23 defined package structure.
- v0.6.24 defined scenario set.
- v0.6.25 defined static fixture planning.
- v0.6.26 defines reviewer walkthrough and five questions mapping.
- v0.6.27 should plan structural checks before any fixture generation.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
reviewer_walkthrough_generated = false
five_questions_mapping_generated = false
static_applied_evidence_fixtures_generated = false
applied_evidence_scenarios_generated = false
applied_evidence_package_generated = false
static_mock_evidence_capture_started = false
tool_backed_diagnostic_capture_started = false
local_lab_diagnostic_system_built = false
fixture_generated = false
fixture_live_evidence = false
validator_authorizes_execution = false
validator_authorizes_scanning = false
validator_authorizes_docker = false
validator_authorizes_delivery = false
docker_compose_file_created = false
docker_compose_executed = false
docker_image_pulled = false
container_started = false
port_bound = false
docker_execution_authorized = false
execution_authorized = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
external_network_target = false
delivery_authorized = false
customer_deliverable = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides generated walkthroughs, generated mappings,
generated static fixtures, generated scenarios, generated evidence packages,
implemented scenario fixtures, real local-lab diagnostic evidence, live evidence,
Docker Compose file creation, Docker execution approval, image pull approval,
container startup approval, port binding approval, production deployment approval,
runtime execution readiness, scan authorization, customer-target authorization,
vulnerability detection accuracy, implementation conformance, compliance
certification, legal approval, audit opinion, completed legal review, completed
dependency audit, managed service approval, commercial license grant, safety
guarantee, external framework equivalence, audit sufficiency, legal sufficiency, or
delivery authorization.

## Out of scope

This checkpoint does not generate reviewer walkthrough files, generate five questions
mapping files, generate applied evidence packages, generate scenario fixtures, commit
sample fixture artifacts, install Docker, run Docker, pull images, start containers,
bind ports, create Docker Compose files, create a runnable Compose design, build a
local lab, select a target for execution, collect live preflight evidence, satisfy
preflight, add dry-run lab execution, enable runtime execution, enable scanning, add
new scanner integrations, create generated sample evidence artifacts, create generated
sample report artifacts, authorize report delivery, expose private advanced feature
details, create private sales material, publish pricing, create a commercial
contract, provide legal advice, authorize external network testing, authorize
credential injection, or authorize customer-target testing.
