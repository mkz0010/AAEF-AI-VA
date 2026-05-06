# v0.6.35 Sanitized Public Sample Generation Candidate

Version: v0.6.35 candidate  
Status: sanitized public sample candidate generation; does not authorize runtime execution

## Purpose

This checkpoint generates a sanitized public sample candidate for AAEF-AI-VA applied
evidence.

v0.6.33 planned sanitized public sample boundaries. v0.6.34 reviewed readiness for a
later generation candidate. v0.6.35 adds a bounded generator that creates synthetic,
non-executing `.example.` artifacts under:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

This checkpoint is sanitized public sample candidate generation only.

This checkpoint does not copy private generated artifacts into the public repository,
implement structural validators, execute structural validator checks, create runnable
configuration, create Docker Compose files, pull images, start containers, bind ports,
authorize Docker execution, authorize runtime execution, run scanners, inject
credentials, authorize customer-target operation, create customer deliverables,
provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The sanitized public sample candidate boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Public example artifacts are synthetic.
- Public example artifacts are non-executing.
- Public example artifacts use `.example.` naming.
- Private generated artifacts are not copied directly.
- Static/mock examples are not live diagnostic evidence.
- Static/mock examples are not proof of diagnostic accuracy.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Generation proposition

~~~text
A sanitized public sample candidate may be generated only as synthetic, non-executing
`.example.` artifacts that demonstrate request-to-evidence traceability and non-proof
boundaries without copying private generated artifacts or implying runtime,
scanner, customer-target, delivery, audit, legal, compliance, certification, or
production-readiness authorization.
~~~

This proposition authorizes only sanitized public sample candidate generation.

## Implemented generator

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/generate_sanitized_public_sample.py` | Sanitized public sample candidate generator |
| `tools/test_v0635_sanitized_public_sample_generation_candidate.py` | Public sample candidate validation test |
| `docs/112-v0635-sanitized-public-sample-generation-candidate.md` | Checkpoint documentation |
| `planning/decisions/ADR-0106-add-v0635-sanitized-public-sample-generation-candidate.md` | Decision record |
| `planning/issues/0105-add-v0635-sanitized-public-sample-generation-candidate.md` | Completed planning issue |

## Generated public sample candidate

The generator writes:

~~~text
examples/applied-evidence/sanitized-static-mock/
  README.md
  package_manifest.example.json
  reviewer_walkthrough.example.md
  aaef_five_questions_mapping.example.md
  non_proof_statement.example.md
  publication_hygiene_report.example.json
  publication_hygiene_report.example.md
  scenarios/
    permitted-safe-diagnostic/
      tool_action_request.example.json
      gate_decision.example.json
      dispatch_decision.example.json
      execution_result.example.json
      evidence_event.example.json
      review_summary.example.md
      non_proof_statement.example.md
    denied-out-of-scope-request/
      tool_action_request.example.json
      gate_decision.example.json
      dispatch_decision.example.json
      non_execution_result.example.json
      evidence_event.example.json
      review_summary.example.md
      non_proof_statement.example.md
    human-approval-required/
      tool_action_request.example.json
      gate_decision.example.json
      dispatch_decision.example.json
      non_execution_result.example.json
      evidence_event.example.json
      review_summary.example.md
      non_proof_statement.example.md
    not-executed-expired/
      tool_action_request.example.json
      gate_decision.example.json
      dispatch_decision.example.json
      non_execution_result.example.json
      evidence_event.example.json
      review_summary.example.md
      non_proof_statement.example.md
~~~

## Scenario coverage

The sample covers four scenarios:

| Scenario | Public sample posture |
| --- | --- |
| `permitted-safe-diagnostic` | synthetic permitted trace; no real execution |
| `denied-out-of-scope-request` | synthetic denied trace; non-execution evidence |
| `human-approval-required` | synthetic human-approval hold; non-execution evidence |
| `not-executed-expired` | synthetic expired request; non-execution evidence |

The sample demonstrates control-boundary evidence, not diagnostic accuracy.

## Publication hygiene

The generated sample includes a publication hygiene report.

The candidate must avoid:

- private path leakage,
- private generated artifact copying,
- secrets,
- credentials,
- tokens,
- cookies,
- raw HTTP messages,
- raw scanner output,
- customer names,
- real target hostnames,
- non-example IP addresses,
- local filesystem paths,
- patent-sensitive private details,
- public overclaims,
- runtime authorization language,
- delivery authorization language.

Hygiene uncertainty must fail closed.

## Non-proof boundary

Visible non-proof statements reject claims of:

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

Non-proof statements are included at package and scenario levels.

## Candidate status

The candidate status is:

~~~text
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = false
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
delivery_authorized = false
~~~

The sample is public-facing example material, not a customer deliverable.

## AAEF-side reporting note

AAEF-side reporting may state:

- sanitized public sample candidate exists,
- sample artifacts are synthetic,
- sample artifacts are non-executing,
- sample artifacts use `.example.` naming,
- non-proof statements are visible,
- runtime/scanner/customer-target/delivery authorization remains false.

AAEF-side reporting should not claim diagnostic accuracy, implementation conformance,
audit sufficiency, legal sufficiency, compliance certification, external-framework
equivalence, or production readiness.

## Relationship to diagnostic execution

This checkpoint does not move toward tool-backed diagnostic execution.

| Track | v0.6.35 status |
| --- | --- |
| Sanitized public sample candidate | generated |
| Runtime execution | not authorized |
| Scanner execution | not authorized |
| Customer-target operation | blocked |
| Delivery authorization | blocked |
| Structural validator implementation | not implemented |
| Tool-backed local-lab diagnostic execution | deferred |

The next safe step is publication review or structural validation planning for public
examples, not live diagnostic execution.

The next safe step is publication review or structural validation planning for public examples, not live diagnostic execution.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.36 Sanitized Public Sample Publication Review Record
~~~

Rationale:

- v0.6.35 creates a public sample candidate.
- A later checkpoint should record publication review results and any remaining
  limitations.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = false
private_artifact_copied_to_public = false
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
runtime_execution_authorized = false
scanner_execution_authorized = false
real_execution_permitted = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
customer_target_authorized = false
external_network_target = false
delivery_authorized = false
customer_deliverable = false
~~~

## Claims to avoid

Avoid language implying that v0.6.35 provides real local-lab diagnostic evidence,
provides live evidence, runs scanners, creates Docker Compose files, approves Docker
execution, pulls images, starts containers, binds ports, approves production
deployment, authorizes runtime execution, authorizes scanning, permits credential
injection, authorizes customer targets, proves vulnerability detection accuracy,
provides implementation conformance, provides compliance certification, provides legal
approval, provides audit opinion, completes legal review, completes dependency audit,
approves managed service use, grants commercial license rights, guarantees safety,
establishes external-framework equivalence, provides audit sufficiency, provides legal
sufficiency, or authorizes delivery.

## Out of scope

This checkpoint does not copy private generated artifacts into the public repository,
implement structural validators, execute structural validator checks, install Docker,
run Docker, pull images, start containers, bind ports, create Docker Compose files,
create a runnable Compose design, build a local lab, select a target for execution,
collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable
runtime execution, enable scanning, add new scanner integrations, authorize report
delivery, expose private advanced feature details, create private sales material,
publish pricing, create a commercial contract, provide legal advice, authorize
external network testing, authorize credential injection, or authorize customer-target
testing.
