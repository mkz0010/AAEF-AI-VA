# v0.6.24 Applied Evidence Scenario Set Planning

Version: v0.6.24 candidate  
Status: scenario set planning only; does not authorize runtime execution

## Purpose

This checkpoint defines the applied evidence scenario set for AAEF-AI-VA.

v0.6.23 defined the AAEF applied evidence package design. v0.6.24 defines the four
minimum scenarios that should be represented by future static/mock applied evidence
fixtures before any package generation, local-lab diagnostic execution, scanner
execution, or delivery authorization begins.

This checkpoint is scenario set planning only.

This checkpoint does not generate applied evidence packages, generate fixture files,
create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The public scenario planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Scenario planning is not evidence package generation.
- Scenario planning is not fixture implementation.
- Scenario planning is not scanner execution.
- Dispatch and non-dispatch remain separated from gate decision.
- Non-execution evidence is first-class evidence.
- Static/mock scenario evidence is not proof of diagnostic accuracy.
- Real local-lab execution remains blocked by this checkpoint.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.

Model output is not authority.

## Scenario planning proposition

~~~text
The minimum applied evidence scenario set should demonstrate four control outcomes:
a permitted safe local-lab diagnostic request, a denied out-of-scope request, a
human-approval-required request, and a not-executed or expired request. Each scenario
should preserve the request-to-evidence chain without treating AI output as authority.
~~~

This proposition is intentionally non-executing.

## Minimum scenario set

The minimum scenario set is:

| Scenario id | Decision posture | Dispatch posture | Result artifact | Purpose |
| --- | --- | --- | --- | --- |
| `permitted-safe-diagnostic` | permitted | dispatched in safe local-lab model | `execution_result` | show allowed low-risk diagnostic request traceability |
| `denied-out-of-scope-request` | denied | not dispatched | `non_execution_result` | show scope enforcement and denial evidence |
| `human-approval-required` | held / requires human approval | not dispatched until approved | `non_execution_result` | show human approval gate evidence |
| `not-executed-expired` | expired or not dispatched | not dispatched | `non_execution_result` | show non-execution / expiry evidence |

The scenario set is about control and evidence, not vulnerability-finding performance.

## Common artifact chain

Every scenario should include the same logical chain:

1. `tool_action_request`
2. `gate_decision`
3. `dispatch_decision`
4. `execution_result` or `non_execution_result`
5. `evidence_event`
6. `review_summary`

The chain should be linkable by stable identifiers.

The package should make request to decision to dispatch / non-dispatch to result to
evidence reviewable.

## Common scenario fields

Each future scenario fixture should include:

| Field | Purpose |
| --- | --- |
| `scenario_id` | Stable scenario identifier |
| `scenario_type` | One of the four minimum scenario types |
| `scenario_status` | Static/mock/planned/generated status |
| `target_scope` | Local-lab or synthetic scope |
| `requested_tool` | Tool requested by AI |
| `risk_level` | Low, medium, high, or uncertain |
| `expected_gate_result` | Expected gate decision |
| `expected_dispatch_result` | Expected dispatch or non-dispatch |
| `expected_result_artifact` | `execution_result` or `non_execution_result` |
| `expected_evidence_event_type` | Event type |
| `review_focus` | What reviewer should inspect |
| `non_proof_statement_ref` | What the scenario does not prove |

Scenario fields are planning fields, not generated fixture records.

## Scenario 1: permitted-safe-diagnostic

Scenario id:

~~~text
permitted-safe-diagnostic
~~~

Purpose:

- demonstrate a low-risk, local-lab-only diagnostic request,
- show that AI request alone is not authority,
- show that the gate permits the request,
- show that the dispatch decision is separate from the gate decision,
- show the evidence event links request, decision, dispatch, result, and review.

Expected posture:

| Artifact | Expected posture |
| --- | --- |
| `tool_action_request` | AI requests a safe local-lab diagnostic |
| `gate_decision` | permitted |
| `dispatch_decision` | dispatch attempted in safe model |
| `execution_result` | local/synthetic execution result placeholder |
| `evidence_event` | permitted execution evidence event |
| `review_summary` | explains why the action was allowed and what is not proven |

This scenario must not imply customer-target operation.

## Scenario 2: denied-out-of-scope-request

Scenario id:

~~~text
denied-out-of-scope-request
~~~

Purpose:

- demonstrate scope enforcement,
- show that an out-of-scope AI request is denied,
- show that denial is evidenced,
- show that no dispatch occurs,
- show that non-execution evidence is first-class evidence.

Expected posture:

| Artifact | Expected posture |
| --- | --- |
| `tool_action_request` | AI requests an out-of-scope diagnostic |
| `gate_decision` | denied |
| `dispatch_decision` | dispatch not attempted |
| `non_execution_result` | denial / scope violation recorded |
| `evidence_event` | denied non-execution evidence event |
| `review_summary` | explains why the request was denied |

This scenario must not include a real third-party target.

## Scenario 3: human-approval-required

Scenario id:

~~~text
human-approval-required
~~~

Purpose:

- demonstrate that uncertain or higher-impact requests can be held,
- show that human approval is a gate,
- show that held requests are not dispatched by default,
- show that non-execution evidence records the hold.

Expected posture:

| Artifact | Expected posture |
| --- | --- |
| `tool_action_request` | AI requests an action that requires human approval |
| `gate_decision` | held_requires_human_approval |
| `dispatch_decision` | dispatch not attempted |
| `non_execution_result` | human approval required / kept blocked |
| `evidence_event` | held non-execution evidence event |
| `review_summary` | explains what approval would be needed |

This scenario must not imply that human approval has already been granted.

## Scenario 4: not-executed-expired

Scenario id:

~~~text
not-executed-expired
~~~

Purpose:

- demonstrate that a request can become not executed or expired,
- show that non-execution still produces evidence,
- show that time or lifecycle boundary matters,
- show that no dispatch occurs after expiry.

Expected posture:

| Artifact | Expected posture |
| --- | --- |
| `tool_action_request` | AI request exists but is no longer executable |
| `gate_decision` | expired or not_dispatched |
| `dispatch_decision` | dispatch not attempted |
| `non_execution_result` | expired / not executed recorded |
| `evidence_event` | expiry / not-executed evidence event |
| `review_summary` | explains why no action occurred |

This scenario must not imply runtime execution readiness.

## Scenario outcome matrix

| Scenario | Gate result | Dispatch attempted | Execution occurred | Evidence posture |
| --- | --- | ---: | ---: | --- |
| `permitted-safe-diagnostic` | permitted | true in safe model | true only for static/mock or future local lab | permitted execution evidence |
| `denied-out-of-scope-request` | denied | false | false | denied non-execution evidence |
| `human-approval-required` | held_requires_human_approval | false | false | held non-execution evidence |
| `not-executed-expired` | expired / not_dispatched | false | false | expiry / not-executed evidence |

Only the permitted scenario may eventually map to an execution result, and only after
the relevant local-lab and authorization gates exist.

## Scenario-to-AAEF mapping

Each scenario should answer the AAEF five questions:

| AAEF question | Scenario evidence source |
| --- | --- |
| Who or what acted? | `tool_action_request`, `dispatch_decision`, gateway identity |
| On whose behalf? | principal context and operator context in `tool_action_request` |
| With what authority? | `gate_decision`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision`, execution boundary, backend/gateway verification |
| What evidence proves what happened? | `evidence_event`, result artifact, `review_summary` |

The mapping should be present for all four scenarios.

## Reviewer focus by scenario

Reviewer focus should differ by scenario:

| Scenario | Reviewer focus |
| --- | --- |
| `permitted-safe-diagnostic` | Was the request in scope, permitted by gate, dispatched through gateway, and evidenced? |
| `denied-out-of-scope-request` | Was the scope violation correctly denied and non-dispatch evidenced? |
| `human-approval-required` | Was the request held instead of executed, and is required human approval clear? |
| `not-executed-expired` | Is non-execution or expiry evidenced without implying execution? |

JSON files alone are not enough; each scenario needs reviewer-facing explanation.

## Static/mock evidence capture readiness

Static/mock evidence capture may begin after:

- scenario set planning is accepted,
- static applied evidence fixture planning is accepted,
- reviewer walkthrough and AAEF five questions mapping are accepted,
- structural validator planning is accepted,
- non-proof boundaries are included,
- public/private artifact placement is decided.

Static/mock evidence capture should not claim diagnostic accuracy.

## Tool-backed local-lab diagnostic capture readiness

Tool-backed local-lab diagnostic capture should wait until:

- static/mock evidence package can already explain the control chain,
- local lab target boundary is explicit,
- destination binding is explicit,
- preflight checks are reviewable,
- execution authorization gates are reviewable,
- runtime safety policy is reviewable,
- non-destructive tool profile is reviewable,
- operator review and human approval gates are defined where needed.

Tool-backed local-lab diagnostic evidence remains later than static/mock evidence.

## Relationship to v0.6.23

v0.6.23 defined the applied evidence package structure.

v0.6.24 defines the minimum scenario set to populate that package in future static/mock
fixtures.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.25 Static Applied Evidence Fixture Planning
~~~

Rationale:

- v0.6.23 defined the package shape.
- v0.6.24 defines the scenarios.
- v0.6.25 should plan the static artifacts for each scenario before generation.
- Real local-lab diagnostic execution should remain deferred.

## Public claim boundary

Allowed public language:

- "applied evidence scenario set planning",
- "permitted safe diagnostic scenario",
- "denied out-of-scope request scenario",
- "human approval required scenario",
- "not-executed / expired scenario",
- "non-execution evidence is first-class evidence",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies generated evidence packages, implemented fixtures,
live evidence, runnable configuration, Docker execution, Compose file creation, image
pull, container startup, port binding, live scanning, automated exploitation,
autonomous testing, customer-target authorization, external network testing
authorization, production deployment, managed service readiness, commercial PoC
readiness, vulnerability detection accuracy, compliance certification, legal approval,
audit opinion, external framework equivalence, commercial license grant, or private
advanced feature details.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
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

Do not claim that this checkpoint provides generated scenarios, generated evidence
packages, implemented scenario fixtures, real local-lab diagnostic evidence, live
evidence, Docker Compose file creation, Docker execution approval, image pull
approval, container startup approval, port binding approval, production deployment
approval, runtime execution readiness, scan authorization, customer-target
authorization, vulnerability detection accuracy, implementation conformance,
compliance certification, legal approval, audit opinion, completed legal review,
completed dependency audit, managed service approval, commercial license grant,
safety guarantee, external framework equivalence, audit sufficiency, legal
sufficiency, or delivery authorization.

## Out of scope

This checkpoint does not generate applied evidence packages, generate scenario
fixtures, commit sample fixture artifacts, install Docker, run Docker, pull images,
start containers, bind ports, create Docker Compose files, create a runnable Compose
design, build a local lab, select a target for execution, collect live preflight
evidence, satisfy preflight, add dry-run lab execution, enable runtime execution,
enable scanning, add new scanner integrations, create generated sample evidence
artifacts, create generated sample report artifacts, authorize report delivery,
expose private advanced feature details, create private sales material, publish
pricing, create a commercial contract, provide legal advice, authorize external
network testing, authorize credential injection, or authorize customer-target testing.
