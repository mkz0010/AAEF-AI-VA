# v0.6.29 Static/Mock Applied Evidence Package Private Generation Candidate

Version: v0.6.29 candidate  
Status: private static/mock generation candidate; does not authorize runtime execution

## Purpose

This checkpoint generates the first private-first static/mock AAEF applied evidence
package for AAEF-AI-VA.

v0.6.28 reviewed readiness for static/mock applied evidence package generation.
v0.6.29 adds a bounded generator that writes a static/mock evidence package under
`private-not-in-git/`, validates the generated structure locally, and keeps generated
artifacts out of the public repository unless a later public-safe promotion decision
is made.

This checkpoint is private static/mock generation only.

This checkpoint does not create public samples, create runnable configuration, create
Docker Compose files, pull images, start containers, bind ports, authorize Docker
execution, authorize runtime execution, run scanners, inject credentials, authorize
customer-target operation, create customer deliverables, provide certification,
provide legal approval, or provide audit opinion.

## Public-safe design boundary

The generation boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Generated outputs are private-first.
- Static/mock generation is not live diagnostic execution.
- Static/mock evidence is not proof of diagnostic accuracy.
- Generated private artifacts are not public samples.
- Generated private artifacts are not customer deliverables.
- Non-execution evidence is first-class evidence.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.

Model output is not authority.

## Generation proposition

~~~text
A private-first static/mock applied evidence package may be generated when it covers
the four minimum scenarios, preserves request-to-evidence linkage, includes non-proof
statements, answers the AAEF five questions, and does not run scanners, access
customer targets, inject credentials, authorize delivery, or imply runtime execution
readiness.
~~~

This proposition authorizes only private static/mock artifact generation under
`private-not-in-git/`.

## Implemented generator

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/generate_static_mock_applied_evidence_package.py` | Private-first static/mock package generator |
| `tools/test_v0629_static_mock_applied_evidence_package_private_generation_candidate.py` | Generator and generated-output boundary test |
| `docs/106-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` | Checkpoint documentation |
| `planning/decisions/ADR-0100-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` | Decision record |
| `planning/issues/0099-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` | Completed planning issue |

## Generated private output root

Default generated output root:

~~~text
private-not-in-git/applied-evidence-runs/static-mock-demo/
~~~

Generated outputs are not intended to be committed.

## Generated package structure

The generated private package includes:

~~~text
private-not-in-git/applied-evidence-runs/static-mock-demo/
  package_manifest.generated.json
  package_summary.generated.json
  reviewer_walkthrough.generated.md
  aaef_five_questions_mapping.generated.md
  non_proof_statement.generated.md
  scenarios/
    permitted-safe-diagnostic/
      tool_action_request.generated.json
      gate_decision.generated.json
      dispatch_decision.generated.json
      execution_result.generated.json
      evidence_event.generated.json
      review_summary.generated.md
      non_proof_statement.generated.md
    denied-out-of-scope-request/
      tool_action_request.generated.json
      gate_decision.generated.json
      dispatch_decision.generated.json
      non_execution_result.generated.json
      evidence_event.generated.json
      review_summary.generated.md
      non_proof_statement.generated.md
    human-approval-required/
      tool_action_request.generated.json
      gate_decision.generated.json
      dispatch_decision.generated.json
      non_execution_result.generated.json
      evidence_event.generated.json
      review_summary.generated.md
      non_proof_statement.generated.md
    not-executed-expired/
      tool_action_request.generated.json
      gate_decision.generated.json
      dispatch_decision.generated.json
      non_execution_result.generated.json
      evidence_event.generated.json
      review_summary.generated.md
      non_proof_statement.generated.md
~~~

## Scenario coverage

The generated package covers:

| Scenario | Result artifact | Runtime posture |
| --- | --- | --- |
| `permitted-safe-diagnostic` | `execution_result.generated.json` | static/mock only; no real execution |
| `denied-out-of-scope-request` | `non_execution_result.generated.json` | denied; no dispatch |
| `human-approval-required` | `non_execution_result.generated.json` | held; no dispatch |
| `not-executed-expired` | `non_execution_result.generated.json` | expired / not executed; no dispatch |

Only the static/mock generator runs. No scanner runs.

## Linkage model

The generated artifacts preserve these links:

| Linkage check | Expected relationship |
| --- | --- |
| request to gate | `gate_decision.linked_request_id` equals `tool_action_request.request_id` |
| gate to dispatch | `dispatch_decision.linked_decision_id` equals `gate_decision.decision_id` |
| dispatch to result | result `linked_dispatch_decision_id` equals `dispatch_decision.dispatch_decision_id` |
| result to evidence | `evidence_event.linked_result_id` equals result `result_id` |
| evidence to request | `evidence_event.linked_request_id` equals `tool_action_request.request_id` |
| evidence to decision | `evidence_event.linked_decision_id` equals `gate_decision.decision_id` |
| evidence to dispatch | `evidence_event.linked_dispatch_decision_id` equals `dispatch_decision.dispatch_decision_id` |

The v0.6.29 test validates representative linkage.

## AAEF five questions mapping

The generated package includes `aaef_five_questions_mapping.generated.md`.

It maps:

| AAEF question | Generated evidence source |
| --- | --- |
| Who or what acted? | `tool_action_request`, gateway identity, `dispatch_decision` |
| On whose behalf? | principal context and operator context in `tool_action_request` |
| With what authority? | `gate_decision`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision`, execution boundary, result artifact |
| What evidence proves what happened? | `evidence_event`, result artifact, `review_summary` |

The mapping is reviewer guidance, not certification.

## Non-proof boundary

Generated package and scenario non-proof statements reject claims of:

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

Non-proof statements are generated as visible Markdown files.

## Private-first handling

Generated artifacts remain under `private-not-in-git/`.

The generator and tests should not require public sample promotion.

A later public-safe sample decision would need a separate review for synthetic-only
content, no secrets, no credentials, no live scan output, no third-party target
implication, no patent-sensitive private detail, non-proof visibility, overclaim
prevention, and human review.

Public-safe promotion is not delivery authorization.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
static_mock_generation_started = true
static_mock_package_generated_private = true
static_mock_generation_authorized_for_public = false
public_sample_generated = false
structural_validator_implemented = false
structural_validator_checks_execute = false
tool_backed_diagnostic_capture_started = false
local_lab_diagnostic_system_built = false
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
real_execution_permitted = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
external_network_target = false
delivery_authorized = false
customer_deliverable = false
~~~

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.30 Static/Mock Applied Evidence Package Review and Promotion Gate Planning
~~~

Rationale:

- v0.6.29 generates private static/mock artifacts.
- The next step should review the generated private package before considering public
  sanitized sample promotion.
- Real local-lab diagnostic execution should remain deferred.

## Claims to avoid

Avoid language implying that v0.6.29 provides public samples, real local-lab diagnostic
evidence, live evidence, scanner execution, Docker Compose file creation, Docker
execution approval, image pull approval, container startup approval, port binding
approval, production deployment approval, runtime execution readiness, scan
authorization, customer-target authorization, vulnerability detection accuracy,
implementation conformance, compliance certification, legal approval, audit opinion,
completed legal review, completed dependency audit, managed service approval,
commercial license grant, safety guarantee, external framework equivalence, audit
sufficiency, legal sufficiency, public sample approval, or delivery authorization.

## Out of scope

This checkpoint does not create public samples, implement structural validators,
execute structural validator checks, install Docker, run Docker, pull images, start
containers, bind ports, create Docker Compose files, create a runnable Compose design,
build a local lab, select a target for execution, collect live preflight evidence,
satisfy preflight, add dry-run lab execution, enable runtime execution, enable
scanning, add new scanner integrations, authorize report delivery, expose private
advanced feature details, create private sales material, publish pricing, create a
commercial contract, provide legal advice, authorize external network testing,
authorize credential injection, or authorize customer-target testing.
