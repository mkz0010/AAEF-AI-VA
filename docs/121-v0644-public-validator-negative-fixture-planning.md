# v0.6.44 Public Validator Negative Fixture Planning

Version: v0.6.44 candidate  
Status: negative fixture planning only; does not authorize runtime execution

## Purpose

This checkpoint plans negative fixtures for the read-only public example structural validator.

The validator was introduced at:

~~~text
tools/validate_public_example_structure.py
~~~

The existing positive control remains:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

This checkpoint is negative fixture planning only.

This checkpoint does not implement negative fixtures, modify validator behavior, create runnable configuration, create Docker Compose files, pull images, start containers, bind ports, authorize Docker execution, authorize runtime execution, run scanners, inject credentials, authorize customer-target operation, create customer deliverables, provide certification, provide legal advice, or provide audit opinion.

Model output is not authority.

## Planning classification

~~~text
AAEF category = Applied Implementation
AAEF Core = not promoted by default
AAEF Profile = not promoted by default
AAEF Practical Package = not promoted by default
public_validator_negative_fixture_planning = true
negative_fixtures_implemented = false
validator_behavior_modified = false
~~~

This is applied implementation hardening, not AAEF Core/Profile/Package promotion.

## Planning proposition

A public validator negative fixture set may be planned to demonstrate that the read-only public example structural validator fails closed for missing artifacts, malformed JSON, broken linkage, scenario contradictions, naming violations, non-proof omissions, hygiene failures, forbidden text leakage, overclaims, and runtime/scanning/customer/delivery boundary violations.

This proposition authorizes only negative fixture planning for the public validator.

## Public-safe planning boundary

- AI output is treated as a request, not authority.
- Gates decide execution.
- Negative fixture planning is not fixture implementation.
- Negative fixture planning is not validator modification.
- Negative fixture planning is not runtime execution.
- Negative fixture planning is not diagnostic validation.
- Future negative fixtures should be synthetic and public-safe.
- Future negative fixtures should not contain private generated artifacts, scanner output, credentials, or customer targets.
- Customer-target operation remains blocked.
- Real local-lab diagnostic execution remains deferred.

## Planning input

| Input | Expected state |
| --- | --- |
| Public example structural validator | implemented |
| Public validator review | completed |
| AAEF Applied Implementation handback | sufficient |
| Public example package | retained as limited synthetic non-executing example |
| Runtime execution | not authorized |
| Scanner execution | not authorized |
| Customer-target operation | blocked |
| Delivery authorization | blocked |

## Planned fixture root

A later checkpoint may add negative fixtures under a public-safe root such as:

~~~text
examples/applied-evidence/public-validator-negative-fixtures/
~~~

This path is a planned candidate. It is not created by v0.6.44.

## Planned negative fixture categories

| Category | Purpose |
| --- | --- |
| `missing-package-artifact` | required package artifact is absent |
| `missing-scenario-artifact` | required scenario artifact is absent |
| `missing-scenario-directory` | one of the four required scenarios is absent |
| `malformed-json` | required JSON artifact is syntactically invalid |
| `broken-linkage` | request, gate, dispatch, result, and evidence identifiers do not link |
| `scenario-posture-contradiction` | denied, held, or expired scenario implies execution |
| `non-example-name` | public artifact name does not use `.example.` except `README.md` |
| `missing-non-proof-statement` | package or scenario non-proof statement is absent |
| `missing-five-questions-mapping` | AAEF five-questions mapping is absent or incomplete |
| `hygiene-not-passed` | publication hygiene status is missing or not `passed` |
| `forbidden-text-leakage` | private path, generated-private artifact name, secret, credential, token, scanner output, or customer-like text appears |
| `overclaim-language` | public artifact implies diagnostic accuracy, production readiness, conformance, audit sufficiency, legal sufficiency, certification, equivalence, customer authorization, or delivery authorization |
| `boundary-flag-violation` | runtime/scanning/customer/delivery boundary flags are not false |

Each category should map to an expected fail-closed blocker.

## Planned expected blocker mapping

| Fixture category | Expected blocker examples |
| --- | --- |
| `missing-package-artifact` | `package_artifact_missing:*` |
| `missing-scenario-artifact` | `scenario_artifact_missing:*` |
| `missing-scenario-directory` | `scenario_missing:*` |
| `malformed-json` | `malformed_json:*` |
| `broken-linkage` | `identifier_linkage_broken:*` |
| `scenario-posture-contradiction` | `scenario_posture_contradiction:*` |
| `non-example-name` | `non_example_artifact_name_detected:*` |
| `missing-non-proof-statement` | `non_proof_statement_missing_or_incomplete:*` |
| `missing-five-questions-mapping` | `five_questions_mapping_missing:*` |
| `hygiene-not-passed` | `publication_hygiene_not_passed` |
| `forbidden-text-leakage` | `forbidden_fragment_detected:*` |
| `overclaim-language` | `overclaim_detected:*` |
| `boundary-flag-violation` | `runtime_boundary_flag_not_false:*` |

The exact blocker strings may be refined by a future implementation checkpoint.

## Planned fixture behavior

A future negative fixture should be synthetic, public-safe, read-only, scoped to public example validation, and expected to trigger validator failure with at least one expected blocker category.

Negative fixtures should prove fail-closed behavior only in the structural validator sense.

## Planned fixture construction rules

A future fixture generator or fixture set should:

- copy only sanitized public example structure when needed,
- avoid private generated artifacts,
- keep fixture data synthetic,
- avoid network targets, real hostnames, customer-like identifiers, credentials, and secrets,
- include expected blocker metadata,
- include a non-authorization statement,
- keep runtime/scanning/customer/delivery flags false except in the specific boundary-violation fixture where the flag violation is the expected negative condition.

The boundary-violation fixture should remain a static file mutation, not a runtime action.

## Planned validation harness behavior

A future harness may run:

~~~text
tools/validate_public_example_structure.py --root <fixture-root> --json
~~~

The harness should assert non-zero exit for negative cases, parse blocker categories, compare them to expected blockers, and avoid mutating the positive control.

It must not run scanners, invoke Docker, bind ports, open network connections, read private run directories as fixture source, or authorize delivery.

## Public example positive control

The existing positive public example package remains the positive control:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Future negative fixture work should preserve this positive control.

Expected positive control result:

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

## AAEF handback relationship

AAEF main may receive the lesson that Applied Implementations can benefit from negative fixture planning for evidence validators.

AAEF main should not receive implementation-sensitive fixture-generation details, patent-sensitive diagnostic reconstruction details, commercial strategy, pricing strategy, customer lists, NDA-assumed material, raw scanner output, private generated artifacts, or credential material.

## Readiness assessment

~~~text
public_validator_negative_fixture_planning_completed = true
public_validator_negative_fixtures_ready_to_consider = true
negative_fixtures_implemented = false
negative_fixture_harness_implemented = false
validator_behavior_modified = false
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
delivery_authorized = false
~~~

The project is ready to consider a later negative fixture implementation readiness review.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

~~~text
public_validator_negative_fixture_planning_completed = true
public_validator_negative_fixtures_ready_to_consider = true
negative_fixtures_implemented = false
negative_fixture_harness_implemented = false
validator_behavior_modified = false
aaef_applied_implementation_handback_review_completed = true
aaef_applied_implementation_handback_sufficient_for_main = true
aaef_handback_category_applied_implementation = true
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
excluded_material_boundary_preserved = true
public_example_structural_validator_review_completed = true
public_example_structural_validation_track_close_ready = true
public_example_structural_validation_status = passed
public_example_structural_validator_implemented = true
public_example_structural_validator_checks_execute = true
public_example_structural_validator_read_only = true
public_example_structural_validator_public_example_scoped = true
public_example_structural_validator_authorizes_execution = false
sanitized_public_sample_track_close_ready = true
retain_limited_public_example = true
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = true
publication_review_record_generated = true
private_artifact_copied_to_public = false
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

Avoid language implying that v0.6.44 implements negative fixtures, modifies validator behavior, provides real local-lab diagnostic evidence, provides live evidence, runs scanners, creates Docker Compose files, approves Docker execution, pulls images, starts containers, binds ports, approves production deployment, authorizes runtime execution, authorizes scanning, permits credential injection, authorizes customer targets, proves vulnerability detection accuracy, provides implementation conformance, provides compliance certification, provides legal advice, provides audit opinion, establishes external-framework equivalence, provides audit sufficiency, provides legal sufficiency, or authorizes delivery.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.45 Public Validator Negative Fixture Implementation Readiness Review
~~~

Rationale:

- v0.6.44 plans negative fixture categories and behavior.
- A readiness review should come before adding fixture files or harness behavior.
- The future implementation should remain read-only, public-safe, and structural.
- Real local-lab diagnostic execution should remain deferred until separately authorized.

## Out of scope

This checkpoint does not implement negative fixtures, implement a negative fixture harness, modify validator behavior, install Docker, run Docker, pull images, start containers, bind ports, create Docker Compose files, create a runnable Compose design, build a local lab, select a target for execution, collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime execution, enable scanning, add new scanner integrations, authorize report delivery, expose private advanced feature details, create private sales material, publish pricing, create a commercial contract, provide legal advice, authorize external network testing, authorize credential injection, or authorize customer-target testing.
