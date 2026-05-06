# v0.6.27 Applied Evidence Structural Validator Planning

Version: v0.6.27 candidate  
Status: structural validator planning only; does not authorize runtime execution

## Purpose

This checkpoint defines applied evidence structural validator planning for AAEF-AI-VA.

v0.6.23 defined the applied evidence package structure. v0.6.24 defined the scenario
set. v0.6.25 defined static fixture planning. v0.6.26 defined reviewer walkthrough
and AAEF five questions mapping. v0.6.27 defines the structural validator checks that
should exist before future fixture generation or static/mock applied evidence package
generation begins.

This checkpoint is structural validator planning only.

This checkpoint does not implement a structural validator, generate fixture files,
generate applied evidence packages, create runnable configuration, create Docker
Compose files, pull images, start containers, bind ports, authorize Docker execution,
authorize runtime execution, run scanners, inject credentials, authorize
customer-target operation, create customer deliverables, provide certification,
provide legal approval, or provide audit opinion.

## Public-safe design boundary

The public structural validator planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Structural validator planning is not validator implementation.
- Structural validation is not semantic correctness.
- Structural validation is not evidence sufficiency.
- Structural validation is not audit sufficiency.
- Structural validation is not legal sufficiency.
- Structural validation is not production readiness.
- Structural validation is not implementation conformance.
- Structural validation is not certification.
- Structural validation is not external-framework equivalence.
- Static/mock evidence is not proof of diagnostic accuracy.
- Real local-lab execution remains blocked by this checkpoint.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.

Model output is not authority.

## Structural validation proposition

~~~text
A future structural validator should verify that an applied evidence package is
complete, internally linked, scenario-consistent, non-authorizing, and explicit about
what it does not prove, while avoiding claims about diagnostic accuracy, audit
sufficiency, legal sufficiency, implementation conformance, production readiness, or
certification.
~~~

This proposition is intentionally non-executing.

## Validator input boundary

A future structural validator should accept static/mock applied evidence package
artifacts only.

Allowed planned inputs:

- `package_manifest.json`,
- scenario directories,
- `tool_action_request.example.json`,
- `gate_decision.example.json`,
- `dispatch_decision.example.json`,
- `execution_result.example.json`,
- `non_execution_result.example.json`,
- `evidence_event.example.json`,
- `review_summary.example.md`,
- `non_proof_statement.example.md`,
- `reviewer_walkthrough.md`,
- `aaef_five_questions_mapping.md`,
- package-level `non_proof_statement.md`.

Disallowed inputs:

- live scan output,
- raw customer artifacts,
- real credentials,
- real secrets,
- external network responses,
- runtime process output,
- customer deliverables,
- runnable Docker Compose files,
- executable scanner commands,
- customer target identifiers.

Input boundary violations should fail closed.

## Validator output boundary

A future structural validator should emit review-only validation results.

Allowed planned outputs:

- validation status,
- scenario id,
- artifact presence status,
- required field status,
- linkage status,
- scenario consistency status,
- contradiction status,
- non-proof status,
- reviewer walkthrough status,
- failure categories,
- blocking failures,
- human review recommendation,
- non-authorization statement.

Disallowed outputs:

- execution authorization,
- scanner authorization,
- Docker authorization,
- delivery authorization,
- customer-ready report,
- production-readiness claim,
- implementation conformance claim,
- compliance claim,
- legal approval,
- audit opinion,
- external-framework equivalence claim.

Validator output must not authorize execution.

## Required artifact presence checks

A future structural validator should check that each scenario contains the required
artifact set.

Required artifact checks:

| Scenario posture | Required artifacts |
| --- | --- |
| permitted execution-style scenario | `tool_action_request.example.json`, `gate_decision.example.json`, `dispatch_decision.example.json`, `execution_result.example.json`, `evidence_event.example.json`, `review_summary.example.md`, `non_proof_statement.example.md` |
| denied / held / not-executed scenario | `tool_action_request.example.json`, `gate_decision.example.json`, `dispatch_decision.example.json`, `non_execution_result.example.json`, `evidence_event.example.json`, `review_summary.example.md`, `non_proof_statement.example.md` |

Artifact absence should be blocking.

## Required field checks

A future structural validator should check required fields for each artifact type.

Required field checks should include:

| Artifact | Required fields |
| --- | --- |
| `tool_action_request.example.json` | `request_id`, `scenario_id`, `requested_tool`, `action_type`, `target_scope`, `risk_level`, `principal_context`, `actor_context`, `generated_by_ai`, `non_authorization_statement` |
| `gate_decision.example.json` | `decision_id`, `scenario_id`, `linked_request_id`, `decision_result`, `reason`, `policy_version`, `rule_version`, `trusted_inputs_used`, `untrusted_inputs_excluded`, `deciding_component` |
| `dispatch_decision.example.json` | `dispatch_decision_id`, `scenario_id`, `linked_decision_id`, `dispatch_attempted`, `execution_boundary`, `gateway_component` |
| `execution_result.example.json` | `result_id`, `scenario_id`, `linked_dispatch_decision_id`, `execution_occurred`, `result_status`, `runtime_boundary` |
| `non_execution_result.example.json` | `result_id`, `scenario_id`, `linked_dispatch_decision_id`, `execution_occurred`, `non_execution_reason`, `blocked_component` |
| `evidence_event.example.json` | `evidence_event_id`, `scenario_id`, `linked_request_id`, `linked_decision_id`, `linked_dispatch_decision_id`, `linked_result_id`, `event_type`, `non_proof_statement_ref` |
| `review_summary.example.md` | scenario id, request summary, gate summary, dispatch summary, result summary, five questions mapping, non-proof section |
| `non_proof_statement.example.md` | non-proof boundaries |

Missing required fields should be blocking.

## Identifier linkage checks

A future structural validator should check stable identifier linkage:

| Linkage check | Expected relationship |
| --- | --- |
| request to gate | `gate_decision.linked_request_id` equals `tool_action_request.request_id` |
| gate to dispatch | `dispatch_decision.linked_decision_id` equals `gate_decision.decision_id` |
| dispatch to result | result `linked_dispatch_decision_id` equals `dispatch_decision.dispatch_decision_id` |
| result to evidence | `evidence_event.linked_result_id` equals result `result_id` |
| evidence to request | `evidence_event.linked_request_id` equals `tool_action_request.request_id` |
| evidence to decision | `evidence_event.linked_decision_id` equals `gate_decision.decision_id` |
| evidence to dispatch | `evidence_event.linked_dispatch_decision_id` equals `dispatch_decision.dispatch_decision_id` |

Broken identifier linkage should be blocking.

## Scenario consistency checks

A future structural validator should check scenario consistency:

| Scenario id | Expected consistency |
| --- | --- |
| `permitted-safe-diagnostic` | gate result is permitted, dispatch attempted is true in static/mock model, execution result artifact exists |
| `denied-out-of-scope-request` | gate result is denied, dispatch attempted is false, non-execution result artifact exists |
| `human-approval-required` | gate result is held / requires human approval, dispatch attempted is false, non-execution result artifact exists |
| `not-executed-expired` | gate result is expired / not dispatched, dispatch attempted is false, non-execution result artifact exists |

Scenario mismatch should be blocking.

## Contradiction checks

A future structural validator should block contradictions such as:

- denied gate decision with `dispatch_attempted = true`,
- held / requires-human-approval gate decision with `dispatch_attempted = true`,
- expired request with `dispatch_attempted = true`,
- non-execution scenario with `execution_occurred = true`,
- permitted scenario without execution or non-execution result explanation,
- dispatch decision without matching gate decision,
- evidence event without matching result,
- review summary claiming customer delivery,
- non-proof statement missing while evidence claims are present.

Contradiction checks are structural checks, not semantic assurance.

## Non-execution evidence checks

A future structural validator should ensure that non-execution outcomes are not
treated as missing evidence.

For denied, held, expired, or not-dispatched scenarios, the validator should require:

- `non_execution_result.example.json`,
- non-execution reason,
- blocked component,
- evidence event,
- review summary explanation,
- non-proof statement.

Non-execution evidence is first-class evidence.

## Reviewer walkthrough coverage checks

A future structural validator should check reviewer-facing coverage:

- package-level `reviewer_walkthrough.md` exists,
- package-level `aaef_five_questions_mapping.md` exists,
- every scenario has `review_summary.example.md`,
- every scenario review summary answers the five AAEF questions,
- every scenario review summary contains a non-proof section,
- every scenario review summary avoids customer delivery implication,
- every scenario review summary avoids audit/legal sufficiency claims.

Reviewer coverage checks should be blocking before public sample release.

## Non-proof statement checks

A future structural validator should require non-proof statements that reject claims of:

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

Missing non-proof statements should be blocking.

## Overclaim prevention checks

A future structural validator should block text or metadata that claims:

- production ready,
- certified compliant,
- legal approval,
- audit opinion,
- audit sufficiency,
- legal sufficiency,
- implementation conformance,
- external framework equivalence,
- customer deliverable,
- delivery authorized,
- scanner accuracy proven,
- real diagnostic evidence captured,
- customer-target operation authorized.

Overclaim prevention protects the public claim boundary.

## Failure category planning

Planned blocking failure categories include:

- `missing_required_artifact`,
- `missing_required_field`,
- `broken_identifier_linkage`,
- `scenario_consistency_failure`,
- `dispatch_result_contradiction`,
- `missing_non_execution_evidence`,
- `missing_reviewer_walkthrough`,
- `missing_five_questions_mapping`,
- `missing_non_proof_statement`,
- `overclaim_detected`,
- `runtime_implication_detected`,
- `customer_target_implication_detected`,
- `delivery_authorization_implication_detected`,
- `validator_uncertainty`.

Every unsafe or uncertain failure should be blocking.

## Validator review result planning

A future structural validator result should include:

| Field | Purpose |
| --- | --- |
| `validator_name` | Structural validator identity |
| `validator_version` | Validator version |
| `package_ref` | Package reviewed |
| `scenario_results` | Per-scenario structural results |
| `artifact_presence_status` | Artifact presence status |
| `identifier_linkage_status` | ID linkage status |
| `scenario_consistency_status` | Scenario consistency status |
| `reviewer_walkthrough_status` | Reviewer coverage status |
| `non_proof_status` | Non-proof status |
| `failure_categories` | Blocking failure categories |
| `blocking_failures` | Blocking failure detail |
| `non_authorization_statement` | Validator is not authority |

The result is review-only and non-authorizing.

## Future implementation sequence

Future implementation should proceed in this order:

1. accept structural validator planning,
2. implement read-only package loading,
3. implement artifact presence checks,
4. implement required field checks,
5. implement identifier linkage checks,
6. implement scenario consistency checks,
7. implement contradiction checks,
8. implement non-execution evidence checks,
9. implement reviewer walkthrough coverage checks,
10. implement non-proof statement checks,
11. implement overclaim prevention checks,
12. add negative tests for every blocking category,
13. only then generate static/mock applied evidence package samples.

Static/mock evidence generation should not precede structural validation planning.

## Readiness for static/mock evidence generation

Static/mock evidence generation can be considered after:

- structural validator planning is accepted,
- fixture planning is accepted,
- reviewer walkthrough mapping is accepted,
- artifact names and identifier linkage are stable,
- non-proof boundaries are visible,
- generation target is private or sanitized/public-safe,
- overclaim prevention is planned.

The earliest safe next step is not live diagnostic execution.

## Relationship to v0.6.26

v0.6.26 defined reviewer walkthrough and AAEF five questions mapping.

v0.6.27 defines structural validation planning so future generated static/mock
evidence packages can be checked for completeness and internal consistency before
they are used as AAEF-side applied evidence material.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.28 Static/Mock Applied Evidence Package Generation Readiness Review
~~~

Rationale:

- v0.6.23 defined package structure.
- v0.6.24 defined scenario set.
- v0.6.25 defined fixture planning.
- v0.6.26 defined reviewer walkthrough mapping.
- v0.6.27 defines structural validator planning.
- v0.6.28 should review whether static/mock package generation is safe to start.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
structural_validator_implemented = false
structural_validator_checks_execute = false
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

Do not claim that this checkpoint provides implemented structural validators,
executing validator checks, generated walkthroughs, generated mappings, generated
static fixtures, generated scenarios, generated evidence packages, implemented
scenario fixtures, real local-lab diagnostic evidence, live evidence, Docker Compose
file creation, Docker execution approval, image pull approval, container startup
approval, port binding approval, production deployment approval, runtime execution
readiness, scan authorization, customer-target authorization, vulnerability detection
accuracy, implementation conformance, compliance certification, legal approval, audit
opinion, completed legal review, completed dependency audit, managed service
approval, commercial license grant, safety guarantee, external framework equivalence,
audit sufficiency, legal sufficiency, or delivery authorization.

## Out of scope

This checkpoint does not implement structural validators, execute structural
validator checks, generate reviewer walkthrough files, generate five questions mapping
files, generate applied evidence packages, generate scenario fixtures, commit sample
fixture artifacts, install Docker, run Docker, pull images, start containers, bind
ports, create Docker Compose files, create a runnable Compose design, build a local
lab, select a target for execution, collect live preflight evidence, satisfy
preflight, add dry-run lab execution, enable runtime execution, enable scanning, add
new scanner integrations, create generated sample evidence artifacts, create generated
sample report artifacts, authorize report delivery, expose private advanced feature
details, create private sales material, publish pricing, create a commercial
contract, provide legal advice, authorize external network testing, authorize
credential injection, or authorize customer-target testing.
