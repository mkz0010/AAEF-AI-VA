# v0.6.11 Local Lab Candidate Profile and Preflight Evidence Planning

Version: v0.6.11 candidate  
Status: local lab candidate profile and preflight evidence planning; does not authorize runtime execution

## Purpose

This checkpoint defines local lab candidate profile and preflight evidence planning
for AAEF-AI-VA.

v0.6.10 defined a safe Docker lab roadmap and candidate criteria. This checkpoint
turns that roadmap into profile and evidence planning without starting containers,
running tools, or enabling scanning.

This checkpoint is candidate-profile and preflight-evidence planning only.

This checkpoint does not authorize Docker execution, container startup, runtime
execution, scanning, credential injection, customer-target operation, production
deployment, certification, legal approval, or audit opinion.

## Public-safe design boundary

The public planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Local lab candidates are profile records, not running targets.
- Preflight evidence is planned, not satisfied.
- Docker execution remains blocked.
- Container startup remains blocked.
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
A future local lab candidate should be represented as a reviewable profile with
explicit scope, network, data, credential, reset, resource, licensing, and evidence
expectations before any Docker, scanner, dry-run, or bounded local execution work
is considered.
~~~

This proposition is intentionally non-executing.

It creates a reviewable planning layer before implementation.

## Candidate profile model

A local lab candidate profile should include:

| Field | Purpose |
| --- | --- |
| `candidate_id` | Stable candidate identifier |
| `candidate_name` | Human-readable name |
| `candidate_type` | Training app, synthetic API, or static fixture target |
| `candidate_status` | Candidate-only status |
| `target_mode` | Localhost-only, isolated network, or static fixture |
| `ownership_statement` | Operator-controlled environment statement |
| `network_boundary` | Network scope and restrictions |
| `external_network_policy` | External network behavior |
| `data_policy` | Synthetic-only and no-customer-data posture |
| `credential_policy` | Synthetic credential posture |
| `secret_policy` | Secret exclusion posture |
| `reset_teardown_expectation` | Reset and cleanup expectation |
| `resource_expectation` | CPU, memory, storage, and time expectation |
| `licensing_review_status` | Licensing review posture |
| `tool_action_taxonomy_mapping` | Allowed and denied future action categories |
| `preflight_evidence_required` | Required evidence before advancement |
| `human_review_required` | Review requirement |
| `advancement_state` | Whether candidate can advance |
| `non_proof_statement_ref` | Reference to non-proof boundary |

A candidate profile is not an execution plan.

## Candidate profile examples

Candidate examples remain planning examples only:

| Candidate | Candidate type | Candidate status | Target mode |
| --- | --- | --- | --- |
| DVWA | Training web application | candidate_only | localhost_or_isolated_network_candidate |
| OWASP Juice Shop | Training web application | candidate_only | localhost_or_isolated_network_candidate |
| WebGoat | Training web application | candidate_only | localhost_or_isolated_network_candidate |
| Synthetic local API | Synthetic target | candidate_only | localhost_or_isolated_network_candidate |
| Static fixture target | Static fixture target | candidate_only | static_fixture_only |

These examples are not selected for execution.

These examples are not installed, started, scanned, integrated, or treated as
authorized execution.

## Candidate comparison criteria

Candidate comparison should consider:

| Criterion | Review question |
| --- | --- |
| Fit for demonstration | Does it help demonstrate request and gate boundaries? |
| Local-only suitability | Can it remain localhost-only or isolated? |
| Reset simplicity | Can state be reset safely? |
| Licensing clarity | Can licensing be reviewed before inclusion? |
| Resource predictability | Can local resource usage be bounded? |
| Credential safety | Can credentials remain synthetic? |
| Data safety | Can customer data be excluded? |
| Tool compatibility | Can future actions remain taxonomy-bound? |
| Evidence clarity | Can evidence expectations be demonstrated safely? |
| Public claim safety | Can public claims remain conservative? |

Candidate comparison is not candidate approval.

## Preflight evidence package model

A future preflight evidence package should include:

| Evidence | Purpose |
| --- | --- |
| `candidate_profile_ref` | Links to candidate profile |
| `local_ownership_evidence` | Shows operator-controlled local environment |
| `network_boundary_evidence` | Shows localhost-only or isolated network expectation |
| `external_network_block_evidence` | Shows external target testing remains blocked |
| `synthetic_data_evidence` | Shows no customer data |
| `synthetic_credential_evidence` | Shows no real credentials |
| `secret_exclusion_evidence` | Shows no secrets are required |
| `reset_teardown_evidence` | Shows reset and cleanup planning |
| `resource_limit_evidence` | Shows local resource bounds |
| `licensing_review_evidence` | Shows licensing review status |
| `action_taxonomy_evidence` | Shows allowed and denied action mapping |
| `human_review_evidence` | Shows review requirement |
| `non_proof_evidence` | Shows what is not demonstrated |

Preflight evidence planning is not preflight satisfaction.

## Preflight evidence status model

Preflight evidence should use conservative status values:

| Status | Meaning |
| --- | --- |
| `not_collected` | Evidence has not been collected |
| `planned` | Evidence is planned |
| `drafted_for_review` | Evidence draft exists for review |
| `requires_review` | Human review required |
| `accepted_for_planning` | Accepted for planning only |
| `rejected` | Evidence is insufficient |
| `not_applicable` | Not applicable with rationale |

This checkpoint should keep preflight satisfied as false.

## Advancement gate model

A candidate should only advance when gates permit it.

Potential advancement states:

| State | Meaning |
| --- | --- |
| `candidate_recorded` | Candidate profile exists |
| `profile_incomplete` | Profile lacks required fields |
| `preflight_evidence_planned` | Preflight evidence is planned |
| `preflight_evidence_requires_review` | Evidence requires review |
| `blocked_missing_evidence` | Missing evidence blocks advancement |
| `blocked_by_network_boundary` | Network boundary concern blocks advancement |
| `blocked_by_credential_policy` | Credential concern blocks advancement |
| `blocked_by_licensing_review` | Licensing concern blocks advancement |
| `accepted_for_static_planning` | Accepted for planning only |
| `not_approved_for_execution` | Execution remains blocked |

This checkpoint does not introduce an execution-approved state.

## Candidate rejection criteria

A candidate should be rejected or deferred if it:

- cannot remain local-only or isolated,
- requires customer data,
- requires real credentials,
- requires real secrets,
- requires uncontrolled outbound traffic,
- requires external network testing,
- has unclear licensing,
- cannot be reset safely,
- cannot define resource expectations,
- cannot map future actions to allowed and denied categories,
- encourages unsafe use against third-party systems,
- creates public claims beyond demonstration planning.

Rejection protects the project boundary.

## Human review requirements

Human review should be required for:

- candidate profile acceptance,
- network boundary interpretation,
- credential policy interpretation,
- synthetic data assertion,
- licensing review status,
- action taxonomy mapping,
- preflight evidence package review,
- advancement to static planning,
- advancement to any future dry-run planning,
- any later bounded local execution proposal,
- any public claim about lab capability.

Human review remains a gate.

## Network and target boundary

Candidate profiles should preserve:

- localhost-only or isolated network expectation,
- no customer target,
- no third-party target,
- no public internet scanning,
- no external network testing,
- no uncontrolled outbound traffic,
- no real credential use,
- no raw sensitive artifact capture from real systems.

If a future design needs network access for image retrieval or dependency setup, that
must be separated from assessment activity and reviewed independently.

## Tool action taxonomy planning

Candidate profiles may map future action categories, but those mappings remain
non-executing.

Allowed planning-level categories may include:

- profile review,
- static configuration review,
- expected evidence review,
- preflight evidence review,
- denied action review,
- human review checkpoint,
- non-proof statement review.

Denied or deferred categories include:

- live scanning,
- external network testing,
- real credential injection,
- customer-target testing,
- automated exploitation,
- report delivery,
- production deployment.

## Generated artifact boundary

Future candidate profile and preflight evidence outputs should remain under private
output paths unless a separate public-safe decision is made.

Allowed private candidate paths may include:

~~~text
private-not-in-git/local-lab-candidate-profiles/
private-not-in-git/local-lab-preflight-evidence/
private-not-in-git/local-lab-profile-reviews/
private-not-in-git/local-lab-advancement-gates/
~~~

Public repository content should contain planning, not generated private candidate
profile outputs.

## Synthetic data requirement

Candidate profiles and future preflight evidence should use synthetic, non-customer,
non-secret, non-live data.

Synthetic planning data should avoid:

- real customer names,
- real target hostnames,
- real customer IP addresses,
- real credentials,
- real tokens,
- real assessment output from customer systems,
- raw sensitive artifacts from real systems,
- customer deliverable content,
- private advanced feature details.

## What this checkpoint does not prove

This checkpoint does not prove:

- Docker lab execution works,
- containers can be started,
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

This non-proof statement should remain visible in future profile and preflight
planning.

## Relationship to v0.6.10

v0.6.10 defined the safe Docker lab roadmap and candidate-only boundary.

v0.6.11 defines the candidate profile and preflight evidence planning layer that
should exist before any later static lab profile, dry-run, or bounded execution work.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.12 Non-running Docker Compose Design Review Planning
~~~

Rationale:

- v0.6.10 defined candidate roadmap and guardrails.
- v0.6.11 defines candidate profile and preflight evidence planning.
- The next safe step is reviewing a non-running Docker Compose design without
  pulling images, starting containers, running scanners, or authorizing execution.

## Public claim boundary

Allowed public language:

- "local lab candidate profile",
- "preflight evidence planning",
- "candidate only",
- "localhost-only or isolated network candidate",
- "synthetic data requirement",
- "human review gate",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies:

- Docker execution,
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
docker_execution_authorized = false
container_started = false
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

- Docker execution approval,
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

Before tagging v0.6.11, verify:

1. README links to this checkpoint.
2. Public-safe design boundary is recorded.
3. Planning proposition is recorded.
4. Candidate profile model is recorded.
5. Candidate profile examples are recorded.
6. Candidate comparison criteria are recorded.
7. Preflight evidence package model is recorded.
8. Preflight evidence status model is recorded.
9. Advancement gate model is recorded.
10. Candidate rejection criteria are recorded.
11. Human review requirements are recorded.
12. Network and target boundary is recorded.
13. Tool action taxonomy planning is recorded.
14. Generated artifact boundary is recorded.
15. Synthetic data requirement is recorded.
16. Runtime, scanning, Docker execution, and delivery boundaries remain disabled.
17. Claims to avoid are recorded.
18. `tools/run_all_local_checks.py` includes the v0.6.11 local lab candidate profile test.

## Out of scope

This checkpoint does not:

- install Docker,
- run Docker,
- pull images,
- start containers,
- create Docker Compose files,
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
