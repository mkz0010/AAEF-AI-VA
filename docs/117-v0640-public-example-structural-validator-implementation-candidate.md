# v0.6.40 Public Example Structural Validator Implementation Candidate

Version: v0.6.40 candidate  
Status: read-only structural validator implementation candidate; does not authorize runtime execution

## Purpose

This checkpoint implements a read-only structural validator candidate for the sanitized public sample artifact set.

v0.6.38 planned public example structural validation. v0.6.39 reviewed readiness to implement a read-only, public-example-scoped validator. v0.6.40 adds that implementation candidate.

The validator scope is limited to:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

This checkpoint is read-only structural validator implementation only.

This checkpoint does not create runnable configuration, create Docker Compose files, pull images, start containers, bind ports, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The validator implementation boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- The validator is read-only.
- The validator is public-example scoped.
- The validator checks structure and boundary posture.
- The validator does not run diagnostic tools.
- The validator does not authorize runtime execution.
- The validator does not authorize scanner execution.
- The validator does not authorize customer-target operation.
- The validator does not authorize delivery.
- Validator success does not imply production readiness.
- Validator success does not imply diagnostic accuracy.
- Validator success does not imply implementation conformance.
- Validator success does not imply audit sufficiency.
- Validator success does not imply legal sufficiency.
- Validator success does not imply compliance certification.
- Validator success does not imply external-framework equivalence.
- Customer-target operation remains blocked.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Implementation proposition

~~~text
A read-only public example structural validator may validate public `.example.` artifact presence, naming, linkage, non-proof visibility, AAEF five-questions mapping visibility, publication hygiene posture, and runtime/scanning/customer/delivery boundary flags without treating validation success as diagnostic correctness, production readiness, implementation conformance, audit sufficiency, legal sufficiency, compliance, or delivery authorization.
~~~

This proposition authorizes only read-only public example structural validation implementation.

This proposition authorizes only read-only public example structural validation implementation.

## Implemented validator

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/validate_public_example_structure.py` | Read-only public example structural validator |
| `tools/test_v0640_public_example_structural_validator_implementation_candidate.py` | Local validation test |
| `docs/117-v0640-public-example-structural-validator-implementation-candidate.md` | Checkpoint documentation |
| `planning/decisions/ADR-0111-add-v0640-public-example-structural-validator-implementation-candidate.md` | Decision record |
| `planning/issues/0110-add-v0640-public-example-structural-validator-implementation-candidate.md` | Completed planning issue |

## Validator scope

The validator reads only public example artifacts under:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

The validator does not read private run directories.

The validator does not read private generated artifacts.

The validator does not mutate public examples.

The validator does not mutate public examples.

## Validator checks

The validator performs read-only checks for:

- public example root presence,
- package-level required artifact presence,
- scenario directory presence,
- scenario-level required artifact presence,
- `.example.` naming except for `README.md`,
- four-scenario coverage,
- representative identifier linkage,
- scenario posture consistency,
- non-proof statement visibility,
- AAEF five-questions mapping visibility,
- publication hygiene status,
- publication review status,
- runtime/scanning/customer/delivery boundary flags,
- absence of public overclaim phrases.

The checks are structural and boundary-oriented, not semantic assurance.

## Expected successful output

A successful validation produces a summary equivalent to:

~~~text
public_example_structural_validation_status = passed
scenario_count = 4
hygiene_status = passed
publication_review_status = reviewed_retain_limited_public_example
blocker_categories = []
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
delivery_authorized = false
~~~

The output is local validation output, not certification, legal approval, audit opinion, compliance evidence, or customer deliverable material.

The output is local validation output, not certification, legal approval, audit opinion, compliance evidence, or customer deliverable material.

## Fail-closed behavior

The validator fails closed if:

- the public example root is missing,
- required package artifacts are missing,
- required scenario artifacts are missing,
- JSON is malformed,
- expected identifiers do not link,
- scenarios are missing,
- scenario posture is contradictory,
- non-proof statements are missing,
- AAEF five questions mapping is missing,
- publication hygiene is missing,
- publication hygiene is not `passed`,
- publication review record is missing,
- publication review status is not `reviewed_retain_limited_public_example`,
- runtime/scanning/customer/delivery boundary flags are not false,
- private path leakage appears,
- sensitive material indicators appear,
- customer-target implications appear,
- overclaim language appears.

Fail-closed behavior is implemented as a validation failure.

Fail-closed behavior is implemented as a validation failure.

## Validator output fields

The validator reports:

- `public_example_structural_validation_status`,
- `scenario_count`,
- `hygiene_status`,
- `publication_review_status`,
- `blocker_categories`,
- `runtime_boundary`,
- `checked_root`,
- `package_artifact_presence`,
- `scenario_reviews`.

The output is intended for local review.

## Validation limitations

The validator does not prove:

- vulnerability detection accuracy,
- diagnostic completeness,
- production readiness,
- implementation conformance,
- audit sufficiency,
- legal sufficiency,
- compliance certification,
- external-framework equivalence,
- customer-target authorization,
- report delivery authorization,
- managed service readiness,
- safety guarantee.

These limitations remain visible and intentional.

## AAEF-side reporting note

AAEF-side reporting may state:

- a read-only public example structural validator exists,
- validator scope is limited to public `.example.` artifacts,
- validation is structural and boundary-oriented,
- validator success does not prove diagnostic accuracy,
- runtime/scanner/customer-target/delivery authorization remains false.

AAEF-side reporting should not claim diagnostic accuracy, implementation conformance, audit sufficiency, legal sufficiency, compliance certification, external-framework equivalence, production readiness, or customer deliverable status.

## Relationship to diagnostic execution

This checkpoint does not move toward tool-backed diagnostic execution.

| Track | v0.6.40 status |
| --- | --- |
| Sanitized public sample candidate | generated |
| Publication review record | generated |
| Public sample close-readiness | reviewed |
| Public example structural validation planning | completed |
| Public example validator implementation readiness | reviewed |
| Public example structural validator implementation | implemented |
| Public example structural validator execution | local validation only |
| Runtime execution | not authorized |
| Scanner execution | not authorized |
| Customer-target operation | blocked |
| Delivery authorization | blocked |
| Tool-backed local-lab diagnostic execution | deferred |

The next safe step is public example structural validator review and close-readiness, not live diagnostic execution.

The next safe step is public example structural validator review and close-readiness, not live diagnostic execution.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.41 Public Example Structural Validator Review and Close-Readiness
~~~

Rationale:

- v0.6.40 implements a read-only validator candidate.
- A later checkpoint should review validator behavior and decide whether the public example validation track is close-ready.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution authorization model:

~~~text
public_example_structural_validator_implementation_candidate_completed = true
public_example_structural_validator_implemented = true
public_example_structural_validator_checks_execute = true
public_example_structural_validator_read_only = true
public_example_structural_validator_public_example_scoped = true
public_example_structural_validator_authorizes_execution = false
public_example_structural_validation_planning_completed = true
public_example_structural_validator_implementation_readiness_review_completed = true
sanitized_public_sample_track_close_ready = true
retain_limited_public_example = true
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = true
publication_review_record_generated = true
private_artifact_copied_to_public = false
structural_validator_implemented = true
structural_validator_checks_execute = true
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

Avoid language implying that v0.6.40 provides real local-lab diagnostic evidence, provides live evidence, runs scanners, creates Docker Compose files, approves Docker execution, pulls images, starts containers, binds ports, approves production deployment, authorizes runtime execution, authorizes scanning, permits credential injection, authorizes customer targets, proves vulnerability detection accuracy, provides implementation conformance, provides compliance certification, provides legal approval, provides audit opinion, completes legal review, completes dependency audit, approves managed service use, grants commercial license rights, guarantees safety, establishes external-framework equivalence, provides audit sufficiency, provides legal sufficiency, or authorizes delivery.

## Out of scope

This checkpoint does not install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add new scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
