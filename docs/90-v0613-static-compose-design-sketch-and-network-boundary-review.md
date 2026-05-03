# v0.6.13 Static Compose Design Sketch and Network Boundary Review

Version: v0.6.13 candidate  
Status: static Compose design sketch and network boundary review; does not authorize runtime execution

## Purpose

This checkpoint defines a static Compose design sketch and network boundary review for AAEF-AI-VA.

v0.6.12 defined non-running Docker Compose design review planning. This checkpoint adds a narrower static design sketch layer that can describe future service roles, network boundary intent, and review questions without creating a runnable Compose file.

This checkpoint is static design sketch and network boundary review only.

This checkpoint does not authorize Docker Compose file creation, Docker execution, image pull, container startup, runtime execution, scanning, credential injection, customer-target operation, production deployment, certification, legal approval, or audit opinion.

## Public-safe design boundary

The public planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- A static Compose design sketch is not a Docker Compose file.
- A static Compose design sketch is not runnable configuration.
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

The planning must not expose private advanced feature details, protected private review materials, market-comparison materials, or confidential commercial strategy.

## Planning proposition

~~~text
A future lab design may first be represented as a non-runnable static design sketch
that records intended service roles, local network boundaries, port binding intent,
and review questions before any Compose file, image pull, container startup, or
tool execution is considered.
~~~

This proposition is intentionally non-executing.

It creates a reviewable boundary between design intent and runnable configuration.

## Static sketch prohibition

The static sketch must not contain runnable Docker Compose syntax.

The static sketch should not include:

- a `services:` YAML block,
- a `networks:` YAML block,
- a `volumes:` YAML block,
- an image reference intended for execution,
- a bind mount path intended for execution,
- executable Docker commands,
- container startup commands,
- scanner commands,
- real credentials,
- real secrets.

The sketch should use descriptive fields, not runnable configuration.

## Static sketch model

A static Compose design sketch should include:

| Field | Purpose |
| --- | --- |
| `static_sketch_id` | Stable sketch identifier |
| `candidate_profile_ref` | Candidate profile under review |
| `compose_design_review_ref` | Links to v0.6.12 design review |
| `sketch_status` | Static sketch status |
| `runnable_configuration_present` | Whether runnable configuration is present |
| `service_role_inventory` | Proposed service roles, not service definitions |
| `network_boundary_intent` | Intended local network boundary |
| `port_binding_intent` | Intended local port binding posture |
| `outbound_network_intent` | Intended outbound network posture |
| `environment_secret_posture` | Environment and secret posture |
| `volume_persistence_intent` | Volume and persistence posture |
| `reset_teardown_intent` | Reset and cleanup posture |
| `resource_limit_intent` | Resource expectation posture |
| `tool_interaction_intent` | Future tool interaction posture |
| `preflight_evidence_required` | Required evidence before advancement |
| `human_review_required` | Human review requirement |
| `advancement_state` | Whether sketch may advance |
| `non_proof_statement_ref` | Reference to non-proof boundary |

A static sketch is not a Compose file.

A static sketch is not an execution plan.

## Sketch status model

Sketch status values should remain conservative:

- `not_created`
- `concept_only`
- `static_sketch_recorded`
- `requires_human_review`
- `blocked_runnable_syntax_present`
- `blocked_by_network_boundary`
- `blocked_by_port_binding`
- `blocked_by_secret_or_credential_risk`
- `accepted_for_static_review`
- `not_approved_for_execution`

This checkpoint should keep sketch status at static-review-only values.

## Service role inventory

Service role inventory may describe future roles without defining runnable services.

Allowed planning-level role descriptions include:

- `local_target_candidate`
- `local_browser_or_client`
- `tool_gateway_control_plane`
- `evidence_review_workspace`
- `static_fixture_source`

Service role inventory must not provide runnable service definitions.

## Network boundary review

Network boundary review should verify:

- local-only intent,
- isolated lab-network intent,
- no customer target,
- no third-party target,
- no public internet scanning,
- no external network testing,
- no uncontrolled outbound traffic,
- no inbound exposure beyond explicit local intent,
- no production network dependency,
- no dependency on real customer infrastructure.

Any network ambiguity should block advancement.

## Port binding intent review

Port binding intent review should verify:

| Review point | Required posture |
| --- | --- |
| Host binding intent | Localhost-only intent |
| Published port intent | Documented as future planning only |
| Administrative interface intent | Local-only and review-bound |
| Default credential posture | Synthetic only and lab-only |
| Browser access intent | Local-only intent |
| Public exposure posture | Not permitted |
| Conflict review | Required before future execution |
| Firewall assumption posture | Not assumed without evidence |

Port binding intent is not permission to bind ports.

## Outbound network posture

Outbound network posture should distinguish image retrieval planning, dependency setup planning, assessment traffic planning, public internet scanning, and customer-target traffic.

Outbound behavior must remain blocked unless later explicit work changes scope.

## Environment and secret posture

Environment and secret posture should verify no real credentials, no real secrets, no customer tokens, no production API keys, no private keys, no sensitive environment file committed to the repository, synthetic placeholders only, lab-only placeholder names only, and secret values excluded from public materials.

The sketch must not include secret values.

## Volume and persistence posture

Volume and persistence posture should verify no customer data volumes, no host-sensitive directory intent, no uncontrolled persistent artifacts, reset behavior planned, cleanup path planned, generated artifacts remain private unless separately reviewed, and logs and outputs do not become public by default.

## Reset and teardown posture

Reset and teardown posture should include reset intent, teardown intent, cleanup intent, state reset expectation, generated artifact cleanup expectation, operator confirmation expectation, and human review before repeatable demonstration claims.

Reset and teardown posture is not execution.

## Static sketch review questions

Reviewers should be able to ask:

- Is the sketch non-runnable?
- Does the sketch avoid runnable Compose syntax?
- What service roles are proposed?
- What local network boundary is intended?
- What port binding intent is described?
- What outbound network behavior is expected?
- What secrets or credentials are excluded?
- What volume or persistence behavior is expected?
- What reset and teardown expectations exist?
- What preflight evidence would be needed before advancement?
- Why does execution remain blocked?

## Preflight evidence expectations

Before any future static sketch advances, preflight evidence should include:

- `static_sketch_ref`
- `candidate_profile_ref`
- `compose_design_review_ref`
- `non_runnable_syntax_review`
- `network_boundary_evidence`
- `port_binding_intent_evidence`
- `outbound_network_evidence`
- `environment_secret_evidence`
- `volume_persistence_evidence`
- `reset_teardown_evidence`
- `resource_limit_evidence`
- `tool_interaction_boundary_evidence`
- `human_review_evidence`
- `non_proof_evidence`

Preflight evidence planning is not preflight satisfaction.

## Advancement gate model

Potential advancement states:

- `static_sketch_recorded`
- `static_sketch_incomplete`
- `preflight_evidence_planned`
- `preflight_evidence_requires_review`
- `blocked_runnable_syntax_present`
- `blocked_missing_evidence`
- `blocked_by_network_boundary`
- `blocked_by_port_binding`
- `blocked_by_secret_or_credential_risk`
- `accepted_for_static_review`
- `not_approved_for_execution`

This checkpoint does not introduce an execution-approved state.

## Human review requirements

Human review should be required for static sketch acceptance, runnable syntax review, service role interpretation, network boundary interpretation, port binding interpretation, outbound network posture, environment and secret posture, volume and persistence posture, reset and teardown posture, advancement to Compose file creation, advancement to dry-run planning, any later bounded local execution proposal, and any public claim about lab capability.

Human review remains a gate.

## Generated artifact boundary

Future static sketch and network boundary review outputs should remain under private output paths unless a separate public-safe decision is made.

Allowed private candidate paths may include:

~~~text
private-not-in-git/static-compose-sketches/
private-not-in-git/static-compose-network-reviews/
private-not-in-git/static-compose-preflight-evidence/
private-not-in-git/static-compose-advancement-gates/
~~~

Public repository content should contain planning, not generated private static sketch outputs.

## What this checkpoint does not prove

This checkpoint does not prove:

- Docker Compose files can be created,
- Docker images can be pulled,
- containers can be started,
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

## Relationship to v0.6.12

v0.6.12 defined non-running Docker Compose design review planning.

v0.6.13 keeps the next step static and non-runnable by defining sketch and network boundary review expectations before any usable Compose file is created.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.14 Static Lab Scenario Fixture Planning
~~~

Rationale:

- v0.6.13 defines static sketch and network boundary review.
- The next safe step can define static scenario fixtures that connect candidate profile, static sketch, AI request, gate decision, and evidence expectation.
- Bounded local execution should remain deferred until profile, preflight, design, network, fixture, and review gates are documented.

## Public claim boundary

Allowed public language:

- "static Compose design sketch",
- "non-runnable design sketch",
- "network boundary review",
- "port binding intent",
- "outbound network posture",
- "service role inventory",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies Docker execution, Compose file creation, image pull, container startup, live scanning, automated exploitation, autonomous testing, customer-target authorization, external network testing authorization, production deployment, managed service readiness, commercial PoC readiness, compliance certification, legal approval, audit opinion, external framework equivalence, commercial license grant, or private advanced feature details.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution authorization model:

~~~text
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

Do not claim that this checkpoint provides runnable Compose configuration, Docker Compose file creation, Docker execution approval, image pull approval, container startup approval, port binding approval, production deployment approval, runtime execution readiness, scan authorization, customer-target authorization, compliance certification, legal approval, audit opinion, completed legal review, completed dependency audit, managed service approval, commercial license grant, safety guarantee, external framework equivalence, audit sufficiency, or delivery authorization.

## Required local checks

Before tagging v0.6.13, verify README linkage, public-safe boundary, static sketch prohibition, static sketch model, sketch status model, service role inventory, network review, port binding review, outbound posture, environment and secret posture, volume posture, reset posture, preflight evidence expectations, advancement gate model, human review requirements, generated artifact boundary, false runtime markers, and `tools/run_all_local_checks.py` registration.

## Out of scope

This checkpoint does not install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add new scanner integrations, create generated sample evidence artifacts, create generated sample report artifacts, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
