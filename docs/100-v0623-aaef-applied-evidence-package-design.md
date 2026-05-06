# v0.6.23 AAEF Applied Evidence Package Design

Version: v0.6.23 candidate  
Status: package design only; does not authorize runtime execution

## Purpose

This checkpoint defines the AAEF applied evidence package design for AAEF-AI-VA.

v0.6.22 accepted the AAEF-side request and reordered the next work around a small,
safe, reviewable applied evidence record. v0.6.23 defines the package structure for
that record before any package generation, fixture generation, local-lab diagnostic
execution, scanner execution, or delivery authorization begins.

This checkpoint is package design only.

This checkpoint does not generate applied evidence packages, generate fixture files,
create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## Short answer: when actual evidence capture begins

There are two different starts.

| Evidence phase | Earliest safe start | Meaning |
| --- | --- | --- |
| Static / mock applied evidence capture | after v0.6.23 through v0.6.27 are in place | Generate or commit sanitized/static evidence examples that prove traceability, not scanner accuracy |
| Private generated applied evidence package | after package design, scenario planning, fixture planning, walkthrough mapping, and structural validator planning | Generate private package runs under `private-not-in-git/` for the four minimum scenarios |
| Real local-lab diagnostic system evidence capture | later gated local-lab phase, likely after the applied evidence package and structural validator are stable | Run bounded, non-destructive tool activity only against a local authorized lab target |
| Customer or third-party evidence capture | not in this roadmap stage | Requires separate authorization, scope, contracts, legal/commercial review, and delivery gates |

The project should start evidence capture with static/mock applied evidence, not with
live diagnostic execution.

Actual tool-backed diagnostic evidence should wait until the package structure,
scenario definitions, reviewer walkthrough, structural validator, local lab target
boundary, preflight checks, and execution authorization gates are all reviewable.

## Public-safe design boundary

The public package design boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Dispatch and non-dispatch are separated from gate decision.
- Non-execution evidence is first-class evidence.
- Evidence package design is not evidence package generation.
- Static/mock evidence examples are not proof of diagnostic accuracy.
- Validator success is not semantic correctness or evidence sufficiency.
- Real local-lab execution remains blocked by this checkpoint.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.

Model output is not authority.

## Design proposition

~~~text
An AAEF-AI-VA applied evidence package should make it possible for a reviewer to
trace AI-generated diagnostic intent from request, to gate decision, to dispatch or
non-dispatch, to execution or non-execution result, to evidence event, to review
summary, without treating AI output as authority.
~~~

This proposition is intentionally non-executing.

## Evidence package top-level structure

A future evidence package should be shaped like this:

~~~text
applied-evidence-package/
  package_manifest.json
  scenarios/
    permitted-safe-diagnostic/
      tool_action_request.json
      gate_decision.json
      dispatch_decision.json
      execution_result.json
      evidence_event.json
      review_summary.md
    denied-out-of-scope-request/
      tool_action_request.json
      gate_decision.json
      dispatch_decision.json
      non_execution_result.json
      evidence_event.json
      review_summary.md
    human-approval-required/
      tool_action_request.json
      gate_decision.json
      dispatch_decision.json
      non_execution_result.json
      evidence_event.json
      review_summary.md
    not-executed-expired/
      tool_action_request.json
      gate_decision.json
      dispatch_decision.json
      non_execution_result.json
      evidence_event.json
      review_summary.md
  package_summary.json
  reviewer_walkthrough.md
  aaef_five_questions_mapping.md
  non_proof_statement.md
~~~

This is a design shape, not a generated package.

## Package manifest design

A future `package_manifest.json` should include:

| Field | Purpose |
| --- | --- |
| `package_id` | Stable package identifier |
| `package_version` | Package version |
| `package_status` | Static/mock/generated/private status |
| `scope_boundary` | Local-lab-only and non-customer boundary |
| `scenario_ids` | Scenario list |
| `artifact_types` | Required artifact types |
| `evidence_chain_order` | Expected chain order |
| `non_authorization_statement` | AI output and validator output are not authority |
| `non_proof_statement_ref` | Link to what the package does not prove |
| `public_private_boundary` | Public vs private artifact posture |

The package manifest is not execution authorization.

## Required artifact chain

Every scenario should preserve this chain:

1. `tool_action_request`
2. `gate_decision`
3. `dispatch_decision`
4. `execution_result` or `non_execution_result`
5. `evidence_event`
6. `review_summary`

The chain should be linkable by stable identifiers.

The package should make request to decision to dispatch / non-dispatch to result to
evidence reviewable.

## `tool_action_request` design

A future `tool_action_request` should include:

- `request_id`,
- `requested_tool`,
- `action_type`,
- `target_scope`,
- `requested_parameters`,
- `purpose`,
- `rationale`,
- `risk_level`,
- `principal_context`,
- `actor_context`,
- `credential_ref` if applicable,
- `generated_by_ai`,
- `timestamp`,
- `non_authorization_statement`.

The request is not authority.

## `gate_decision` design

A future `gate_decision` should include:

- `decision_id`,
- `linked_request_id`,
- `decision_result`,
- `reason`,
- `policy_version`,
- `rule_version`,
- `trusted_inputs_used`,
- `untrusted_inputs_excluded`,
- `deciding_component`,
- `timestamp`.

Supported decision results should include:

- `permitted`,
- `denied`,
- `held_requires_human_approval`,
- `not_dispatched`,
- `expired`,
- `revoked`.

Gate decision is the authorization boundary record, not the dispatch record.

## `dispatch_decision` design

A future `dispatch_decision` should include:

- `dispatch_decision_id`,
- `linked_decision_id`,
- `dispatch_attempted`,
- `dispatched_tool`,
- `blocked_reason`,
- `execution_boundary`,
- `gateway_component`,
- `timestamp`.

Dispatch and non-dispatch must be explicit.

## Execution and non-execution result design

A future `execution_result` should be used only for permitted local-lab actions.

A future `non_execution_result` should be used for denied, held, not-dispatched,
expired, or revoked actions.

A `non_execution_result` should include:

- `result_id`,
- `linked_dispatch_decision_id`,
- `execution_occurred`,
- `non_execution_reason`,
- `blocked_component`,
- `review_required`,
- `timestamp`.

Non-execution evidence is first-class evidence.

## Evidence event design

A future `evidence_event` should include:

- `evidence_event_id`,
- `scenario_id`,
- `linked_request_id`,
- `linked_decision_id`,
- `linked_dispatch_decision_id`,
- `linked_result_id`,
- `event_type`,
- `event_summary`,
- `evidence_created_at`,
- `integrity_notes`,
- `non_proof_statement_ref`.

The evidence event links the chain for review.

## Review summary design

A future `review_summary.md` should explain:

- what AI requested,
- what gate evaluated,
- why the result was permitted, denied, held, or not-executed,
- which evidence artifacts prove the path,
- how AAEF five questions are answered,
- what the scenario does not prove.

The review summary is a reviewer-facing explanation, not a customer deliverable.

## Minimum scenario package set

The minimum scenario package set should include:

| Scenario id | Result posture | Purpose |
| --- | --- | --- |
| `permitted-safe-diagnostic` | permitted / execution_result | Low-risk local-lab diagnostic request is permitted |
| `denied-out-of-scope-request` | denied / non_execution_result | Scope violation is denied and evidenced |
| `human-approval-required` | held / non_execution_result | High-impact or uncertain request is held |
| `not-executed-expired` | not executed or expired / non_execution_result | Non-execution is evidenced |

The purpose is control and evidence, not vulnerability-finding performance.

## Public and private artifact placement

Public repository may contain:

- package design,
- sanitized static sample package,
- reviewer walkthrough,
- non-execution evidence examples,
- AAEF five questions mapping,
- structural validator planning.

Private output paths may contain generated runs:

~~~text
private-not-in-git/applied-evidence-runs/
private-not-in-git/local-lab-runs/
private-not-in-git/applied-evidence-review-records/
~~~

Public repo must not contain raw credentials, real customer data, unauthorized targets,
live exploitation details, or patent-sensitive browser/dynamic-state reconstruction
details.

## Diagnostic system build timing

The diagnostic system should be built in layers:

| Layer | Action |
| --- | --- |
| Applied evidence package design | Do now |
| Scenario and fixture planning | Next |
| Static/mock evidence package generation | After design, scenario, fixture, walkthrough, and validator planning |
| Read-only structural validation | Before any tool-backed local execution |
| Local lab target bring-up | After package and validator boundaries are stable |
| Non-destructive local tool execution | Only after preflight, scope binding, destination binding, and execution authorization gates are explicit |
| Customer-target execution | Out of scope for this stage |

In practical project terms, the first meaningful evidence capture should be static or
mock evidence capture. The first tool-backed diagnostic system evidence capture should
come later, after the applied evidence package can already explain what happened.

## AAEF five questions package mapping

The package should answer:

| AAEF question | Evidence package artifact |
| --- | --- |
| Who or what acted? | `tool_action_request`, `dispatch_decision`, gateway identity |
| On whose behalf? | principal context and operator context in `tool_action_request` |
| With what authority? | `gate_decision`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision`, execution boundary, backend/gateway verification |
| What evidence proves what happened? | `evidence_event`, result artifact, `review_summary` |

## Structural validator relationship

The package design should be validator-friendly.

A future structural validator may check:

- required artifact presence,
- required field presence,
- request id linkage,
- decision id linkage,
- dispatch id linkage,
- result id linkage,
- evidence event link integrity,
- scenario type consistency,
- contradiction checks,
- non-proof statement presence.

Validator success must not imply semantic correctness, evidence sufficiency,
assessment sufficiency, production readiness, audit sufficiency, legal sufficiency,
implementation conformance, certification, compliance, or external-framework
equivalence.

## Recommended next checkpoints

Recommended order:

| Checkpoint | Purpose |
| --- | --- |
| v0.6.24 Applied Evidence Scenario Set Planning | Specify four scenarios in detail |
| v0.6.25 Static Applied Evidence Fixture Planning | Plan static artifacts for each scenario |
| v0.6.26 Reviewer Walkthrough and Five Questions Mapping | Add reviewer-facing explanation |
| v0.6.27 Applied Evidence Structural Validator Planning | Plan structural checks |
| v0.6.28 Static/Mock Applied Evidence Package Generation | Generate first private/static evidence package if boundaries are ready |
| v0.7.x Local Lab Diagnostic Execution Gate | Consider bounded, non-destructive local tool-backed evidence capture |

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
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

Do not claim that this checkpoint provides generated evidence packages, real local-lab
diagnostic evidence, implemented scenario fixtures, live evidence, Docker Compose file
creation, Docker execution approval, image pull approval, container startup approval,
port binding approval, production deployment approval, runtime execution readiness,
scan authorization, customer-target authorization, vulnerability detection accuracy,
implementation conformance, compliance certification, legal approval, audit opinion,
completed legal review, completed dependency audit, managed service approval,
commercial license grant, safety guarantee, external framework equivalence, audit
sufficiency, legal sufficiency, or delivery authorization.

## Out of scope

This checkpoint does not generate applied evidence packages, generate fixture files,
commit sample fixture artifacts, install Docker, run Docker, pull images, start
containers, bind ports, create Docker Compose files, create a runnable Compose design,
build a local lab, select a target for execution, collect live preflight evidence,
satisfy preflight, add dry-run lab execution, enable runtime execution, enable
scanning, add new scanner integrations, create generated sample evidence artifacts,
create generated sample report artifacts, authorize report delivery, expose private
advanced feature details, create private sales material, publish pricing, create a
commercial contract, provide legal advice, authorize external network testing,
authorize credential injection, or authorize customer-target testing.
