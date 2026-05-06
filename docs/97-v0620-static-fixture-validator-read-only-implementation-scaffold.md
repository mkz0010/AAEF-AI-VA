# v0.6.20 Static Fixture Validator Read-only Implementation Scaffold

Version: v0.6.20 candidate  
Status: read-only implementation scaffold; does not authorize runtime execution

## Purpose

This checkpoint adds the first read-only implementation scaffold for the future static fixture validator.

v0.6.19 defined implementation readiness review. v0.6.20 introduces a minimal `tools/validate_static_lab_fixtures.py` scaffold that can be compiled, imported, and run in a read-only mode while preserving the boundary that complete fixture schema validation, negative tests, positive fixture generation, and execution remain out of scope.

This checkpoint is read-only implementation scaffold only.

This checkpoint does not implement complete fixture schemas, implement complete fixture validators, implement negative tests, generate fixture files, create runnable configuration, create Docker Compose files, pull images, start containers, bind ports, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The public implementation boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- The scaffold is read-only.
- The scaffold emits review-only validation results.
- The scaffold does not authorize execution.
- The scaffold does not authorize scanning.
- The scaffold does not authorize Docker.
- The scaffold does not authorize delivery.
- The scaffold does not create fixture artifacts.
- The scaffold does not create or modify Docker Compose files.
- The scaffold does not pull images.
- The scaffold does not start containers.
- The scaffold does not bind ports.
- The scaffold does not access external targets.
- The scaffold does not inject credentials.
- Runtime execution remains blocked.
- Scan execution remains blocked.
- Customer-target operation remains blocked.
- Report delivery remains separately gated.

The implementation must not expose private advanced feature details, protected private review materials, market-comparison materials, or confidential commercial strategy.

## Implementation proposition

~~~text
The first validator implementation step should be a read-only scaffold that can load
only local fixture paths, emit review-only results, fail closed for missing inputs,
and never authorize execution, scanning, Docker activity, delivery, or customer-target
operation.
~~~

This proposition is intentionally non-executing.

## Implemented scaffold files

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/validate_static_lab_fixtures.py` | Minimal read-only static fixture validator scaffold |
| `tools/test_v0620_static_fixture_validator_read_only_implementation_scaffold.py` | Boundary and scaffold validation test |
| `docs/97-v0620-static-fixture-validator-read-only-implementation-scaffold.md` | Checkpoint documentation |
| `planning/decisions/ADR-0091-add-v0620-static-fixture-validator-read-only-implementation-scaffold.md` | Decision record |
| `planning/issues/0090-add-v0620-static-fixture-validator-read-only-implementation-scaffold.md` | Completed planning issue |

## Implemented scaffold behavior

The scaffold implements only:

- review-only result structures,
- planned failure category constants,
- explicit runtime-boundary markers,
- read-only fixture directory inspection,
- fail-closed missing-directory behavior,
- fail-closed non-directory behavior,
- local CLI argument parsing,
- JSON review result output to stdout.

The scaffold does not implement full fixture validation.

## Read-only behavior

The scaffold must remain read-only.

Read-only behavior means:

- it reads local paths only,
- it does not create fixture files,
- it does not modify fixture files,
- it does not generate sample fixtures,
- it does not write validation outputs to repository paths,
- it does not run external processes,
- it does not run Docker,
- it does not run scanners,
- it does not access external targets,
- it does not inject credentials.

Any future write behavior requires separate review.

## Review-only output model

The scaffold output is a review record.

It may include `validator_name`, `validator_version`, `validation_status`, `fixture_dir`, `failure_categories`, `blocking_failures`, `runtime_boundary`, and `non_authorization_statement`.

It must not include execution authorization, scanner authorization, Docker authorization, delivery authorization, customer-ready report, production-readiness claim, compliance claim, legal approval, or audit opinion.

Validator output must not authorize execution.

## Fail-closed behavior

The scaffold fails closed when the fixture directory is missing, the fixture directory path is not a directory, or the validator cannot safely inspect the path.

Fail-closed means the review result is blocking and non-authorizing.

## Runtime boundary markers

The scaffold and tests preserve these false markers:

~~~text
fixture_schema_complete = false
fixture_validator_complete = false
negative_tests_complete = false
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

## Relationship to v0.6.19

v0.6.19 defined implementation readiness review.

v0.6.20 implements only the first read-only validator scaffold after that readiness review, without implementing complete validation checks or generating fixture artifacts.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.21 Static Fixture Validator Required-node Check Planning
~~~

Rationale:

- v0.6.20 adds the minimal read-only scaffold.
- The next safe step is planning required-node checks before implementing full schema validation or positive fixture generation.
- Bounded local execution should remain deferred until static validator checks remain read-only, fail-closed, and non-authorizing.

## Public claim boundary

Allowed public language:

- "read-only validator scaffold",
- "review-only validation result",
- "fail-closed missing-directory behavior",
- "non-authorizing CLI boundary",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies complete fixture schemas, complete fixture validators, implemented negative tests, generated fixtures, live evidence, working complete validator, runnable configuration, Docker execution, Compose file creation, image pull, container startup, port binding, live scanning, automated exploitation, autonomous testing, customer-target authorization, external network testing authorization, production deployment, managed service readiness, commercial PoC readiness, compliance certification, legal approval, audit opinion, external framework equivalence, commercial license grant, or private advanced feature details.

## Claims to avoid

Do not claim that this checkpoint provides complete fixture schema validation, complete fixture validator implementation, negative test implementation, generated fixtures, live evidence, Docker Compose file creation, Docker execution approval, image pull approval, container startup approval, port binding approval, production deployment approval, runtime execution readiness, scan authorization, customer-target authorization, compliance certification, legal approval, audit opinion, completed legal review, completed dependency audit, managed service approval, commercial license grant, safety guarantee, external framework equivalence, audit sufficiency, or delivery authorization.

## Out of scope

This checkpoint does not implement complete fixture schemas, implement complete fixture validators, implement negative tests, generate fixture files, commit sample fixture artifacts, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add new scanner integrations, create generated sample evidence artifacts, create generated sample report artifacts, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
