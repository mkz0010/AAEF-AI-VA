# v0.6.12 Non-running Docker Compose Design Review Planning

Version: v0.6.12 candidate  
Status: non-running Docker Compose design review planning; does not authorize runtime execution

## Purpose

This checkpoint defines non-running Docker Compose design review planning for
AAEF-AI-VA.

v0.6.10 defined a safe Docker lab roadmap. v0.6.11 defined candidate profile and
preflight evidence planning. This checkpoint defines how a future Docker Compose
design should be reviewed before any Compose file is created, images are pulled,
containers are started, or scanners are run.

This checkpoint is non-running design review planning only.

This checkpoint does not authorize Docker execution, image pull, container startup,
runtime execution, scanning, credential injection, customer-target operation,
production deployment, certification, legal approval, or audit opinion.

## Public-safe design boundary

The public planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Docker Compose design review is a planning record, not a running lab.
- No Docker Compose file is created by this checkpoint.
- No Docker image is pulled by this checkpoint.
- No container is started by this checkpoint.
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

The planning proposition is:

~~~text
A future Docker Compose design should be reviewed as a non-running design artifact
before any file creation, image pull, container startup, scanner execution, or
bounded local execution proposal is considered.
~~~

This proposition is intentionally non-executing.

It creates a review layer between candidate profiles and any later Docker design
artifact.

## Non-running Compose design review model

A non-running Docker Compose design review should include:

| Field | Purpose |
| --- | --- |
| `compose_design_review_id` | Stable review identifier |
| `candidate_profile_ref` | Candidate profile under review |
| `design_status` | Planning-only design status |
| `compose_file_created` | Whether a Compose file exists |
| `image_pull_required` | Whether image retrieval would be required in future |
| `container_start_required` | Whether container startup would be required in future |
| `network_boundary` | Proposed local network boundary |
| `port_exposure_plan` | Proposed port exposure and binding |
| `service_inventory` | Proposed services without creating runtime config |
| `image_provenance_review` | Image source and trust review posture |
| `environment_variable_review` | Environment variable and secret posture |
| `volume_persistence_review` | Volume and persistence posture |
| `reset_teardown_review` | Reset and cleanup posture |
| `resource_limit_review` | CPU, memory, storage, and time posture |
| `external_network_review` | Outbound and external target posture |
| `tool_interaction_review` | Future tool interaction posture |
| `preflight_evidence_required` | Evidence required before any advancement |
| `human_review_required` | Human review requirement |
| `advancement_state` | Whether design may advance |
| `non_proof_statement_ref` | Reference to non-proof boundary |

A Compose design review is not a Compose file.

A Compose design review is not an execution plan.

## Candidate design posture

Candidate design posture values should remain conservative:

| Posture | Meaning |
| --- | --- |
| `not_created` | No Compose file exists |
| `concept_only` | Design concept only |
| `draft_for_review` | Draft may be reviewed before file creation |
| `requires_human_review` | Human review required |
| `blocked_missing_evidence` | Required evidence is missing |
| `blocked_by_network_boundary` | Network design concern blocks advancement |
| `blocked_by_secret_or_credential_risk` | Secret or credential concern blocks advancement |
| `accepted_for_non_running_design_review` | Accepted for design review only |
| `not_approved_for_execution` | Execution remains blocked |

This checkpoint should keep design status at planning-only or review-only values.

## Network boundary review

Network boundary review should verify:

- localhost-only or isolated Docker network expectation,
- no customer target,
- no third-party target,
- no public internet scanning,
- no external network testing,
- no uncontrolled outbound traffic,
- no inbound exposure beyond explicitly reviewed local bindings,
- no production network dependency,
- no dependency on real customer infrastructure.

Any network ambiguity should block advancement.

## Port exposure review

Port exposure review should verify:

| Review point | Required posture |
| --- | --- |
| Host binding | Localhost-only unless separately reviewed |
| Published ports | Explicitly documented |
| Admin interfaces | Not exposed beyond local review boundary |
| Default credentials | Synthetic only and documented as lab-only |
| Conflicting services | Identified before future execution |
| Firewall assumptions | Not assumed without evidence |
| Browser access | Local-only assumption |
| Public exposure | Not permitted |

Port exposure planning is not permission to bind ports.

## Image provenance review

Image provenance review should verify:

- proposed image source is documented,
- image license review is planned,
- image update policy is planned,
- image digest or version pinning is considered,
- supply-chain risk is acknowledged,
- image pull is separated from assessment activity,
- no image is pulled by this checkpoint,
- no container is started by this checkpoint.

Image review is not image approval.

## Environment variable and secret review

Environment variable review should verify:

- no real credentials,
- no real secrets,
- no customer tokens,
- no production API keys,
- no private keys,
- no sensitive environment file committed to the repository,
- synthetic credentials only,
- lab-only placeholders only,
- secret values excluded from public materials.

Credential and secret safety must be explicit before any future advancement.

## Volume and persistence review

Volume and persistence review should verify:

- no customer data volumes,
- no host-sensitive directories mounted,
- no uncontrolled persistent artifacts,
- reset behavior documented,
- cleanup path documented,
- generated artifacts remain private unless separately reviewed,
- logs and outputs do not become public by default.

Persistence should be minimized and reviewable.

## Reset and teardown review

Reset and teardown planning should include:

- reset method,
- teardown method,
- cleanup of generated containers or resources if future execution is later authorized,
- cleanup of generated artifacts,
- state reset expectation,
- operator confirmation step,
- human review before repeatable demonstration claims.

Reset and teardown planning is not execution.

## Resource limit review

Resource limit review should include:

- CPU expectation,
- memory expectation,
- storage expectation,
- time limit expectation,
- log size expectation,
- scanner activity remains disabled,
- runaway behavior mitigation planning,
- operator interruption planning.

Resource review supports safety before execution exists.

## Image retrieval and assessment activity separation

If a future design requires image retrieval, dependency setup, or update behavior,
that activity must be separated from assessment activity.

The design review should distinguish:

| Activity | Status in this checkpoint |
| --- | --- |
| Image retrieval planning | Allowed as planning |
| Image retrieval execution | Not authorized |
| Container startup planning | Allowed as planning |
| Container startup execution | Not authorized |
| Tool request planning | Allowed as planning |
| Scanner execution | Not authorized |
| Assessment activity | Not authorized |
| Customer-target activity | Not authorized |

This separation prevents dependency setup from being confused with assessment execution.

## Preflight evidence expectations

Before any future Compose design advances, preflight evidence should include:

| Evidence | Purpose |
| --- | --- |
| `candidate_profile_ref` | Links design to candidate profile |
| `compose_design_review_ref` | Links to design review |
| `network_boundary_evidence` | Shows local-only or isolated network expectation |
| `port_exposure_evidence` | Shows host bindings and published ports |
| `image_provenance_evidence` | Shows image source and review posture |
| `image_pull_separation_evidence` | Shows image retrieval is separate from assessment activity |
| `environment_variable_evidence` | Shows no real secrets or customer tokens |
| `volume_persistence_evidence` | Shows volume and persistence posture |
| `reset_teardown_evidence` | Shows reset and cleanup planning |
| `resource_limit_evidence` | Shows resource bounds |
| `external_network_block_evidence` | Shows external target testing remains blocked |
| `tool_interaction_boundary_evidence` | Shows scanners remain disabled |
| `human_review_evidence` | Shows review requirement |
| `non_proof_evidence` | Shows what is not demonstrated |

Preflight evidence planning is not preflight satisfaction.

## Advancement gate model

A Compose design should only advance when gates permit it.

Potential advancement states:

| State | Meaning |
| --- | --- |
| `compose_design_recorded` | Design review record exists |
| `compose_design_incomplete` | Required design fields are missing |
| `preflight_evidence_planned` | Preflight evidence is planned |
| `preflight_evidence_requires_review` | Evidence requires review |
| `blocked_missing_evidence` | Missing evidence blocks advancement |
| `blocked_by_network_boundary` | Network concern blocks advancement |
| `blocked_by_port_exposure` | Port exposure concern blocks advancement |
| `blocked_by_secret_or_credential_risk` | Secret or credential concern blocks advancement |
| `blocked_by_image_provenance` | Image provenance concern blocks advancement |
| `accepted_for_non_running_review` | Accepted for non-running review only |
| `not_approved_for_execution` | Execution remains blocked |

This checkpoint does not introduce an execution-approved state.

## Human review requirements

Human review should be required for:

- Compose design review acceptance,
- network boundary interpretation,
- port exposure interpretation,
- image provenance posture,
- image pull separation posture,
- environment variable and secret posture,
- volume and persistence posture,
- reset and teardown posture,
- resource limit posture,
- tool interaction boundary,
- advancement to Compose file creation,
- advancement to dry-run planning,
- any later bounded local execution proposal,
- any public claim about lab capability.

Human review remains a gate.

## Generated artifact boundary

Future Compose design review outputs should remain under private output paths unless
a separate public-safe decision is made.

Allowed private candidate paths may include:

~~~text
private-not-in-git/docker-compose-design-reviews/
private-not-in-git/docker-compose-preflight-evidence/
private-not-in-git/docker-compose-network-reviews/
private-not-in-git/docker-compose-advancement-gates/
~~~

Public repository content should contain planning, not generated private Compose
design review outputs.

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

This non-proof statement should remain visible in future Compose design planning.

## Relationship to v0.6.10

v0.6.10 defined the safe Docker lab roadmap and local target candidate planning.

v0.6.12 keeps the next step non-running by defining design review expectations before
Compose files are created.

## Relationship to v0.6.11

v0.6.11 defined local lab candidate profiles and preflight evidence planning.

v0.6.12 links any future Compose design review back to candidate profiles and
preflight evidence expectations.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.13 Static Compose Design Sketch and Network Boundary Review
~~~

Rationale:

- v0.6.12 defines non-running Compose design review criteria.
- The next safe step can define a static, non-runnable design sketch and network
  boundary review without creating a usable Compose file, pulling images, or starting
  containers.
- Bounded local execution should remain deferred until profile, preflight, design,
  network, and review gates are documented.

## Public claim boundary

Allowed public language:

- "non-running Docker Compose design review",
- "Compose design planning",
- "image provenance review",
- "port exposure review",
- "network boundary review",
- "image retrieval and assessment activity separation",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies:

- Docker execution,
- Compose file creation,
- image pull,
- container startup,
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
docker_compose_file_created = false
docker_compose_executed = false
docker_image_pulled = false
container_started = false
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

Do not claim that this checkpoint provides:

- Docker Compose file creation,
- Docker execution approval,
- image pull approval,
- container startup approval,
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

Before tagging v0.6.12, verify:

1. README links to this checkpoint.
2. Public-safe design boundary is recorded.
3. Planning proposition is recorded.
4. Non-running Compose design review model is recorded.
5. Candidate design posture is recorded.
6. Network boundary review is recorded.
7. Port exposure review is recorded.
8. Image provenance review is recorded.
9. Environment variable and secret review is recorded.
10. Volume and persistence review is recorded.
11. Reset and teardown review is recorded.
12. Resource limit review is recorded.
13. Image retrieval and assessment activity separation is recorded.
14. Preflight evidence expectations are recorded.
15. Advancement gate model is recorded.
16. Human review requirements are recorded.
17. Generated artifact boundary is recorded.
18. Runtime, scanning, Compose, image pull, Docker execution, and delivery boundaries remain disabled.
19. Claims to avoid are recorded.
20. `tools/run_all_local_checks.py` includes the v0.6.12 non-running Docker Compose design review test.

## Out of scope

This checkpoint does not:

- install Docker,
- run Docker,
- pull images,
- start containers,
- create Docker Compose files,
- create a runnable Compose design,
- build a local lab,
- select a target for execution,
- collect live preflight evidence,
- satisfy preflight,
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
