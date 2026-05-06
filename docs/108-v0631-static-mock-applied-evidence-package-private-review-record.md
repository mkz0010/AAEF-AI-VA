# v0.6.31 Static/Mock Applied Evidence Package Private Review Record

Version: v0.6.31 candidate  
Status: private review-record generation; does not authorize runtime execution

## Purpose

This checkpoint generates a private review record for the static/mock applied evidence
package generated in v0.6.29.

v0.6.29 generated the private package. v0.6.30 planned the review and promotion gate.
v0.6.31 adds a bounded private review-record generator that reviews the generated
private package and writes private review outputs under `private-not-in-git/`.

This checkpoint is private review-record generation only.

This checkpoint does not promote public samples, generate public sample artifacts,
implement structural validators, execute structural validator checks, create runnable
configuration, create Docker Compose files, pull images, start containers, bind ports,
authorize Docker execution, authorize runtime execution, run scanners, inject
credentials, authorize customer-target operation, create customer deliverables,
provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The private review-record boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Private review records are not public samples.
- Private review records are not customer deliverables.
- Private review records do not authorize promotion.
- Static/mock evidence is not live diagnostic evidence.
- Static/mock evidence is not proof of diagnostic accuracy.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Private review proposition

~~~text
A private static/mock applied evidence package can be reviewed privately by recording
whether the expected scenarios, artifacts, linkages, non-proof statements, and runtime
boundaries are present, while keeping public sample promotion, scanner execution,
customer-target operation, and delivery authorization blocked.
~~~

This proposition authorizes only private review-record generation under
`private-not-in-git/`.

## Implemented private review generator

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/generate_static_mock_applied_evidence_private_review_record.py` | Private review-record generator |
| `tools/test_v0631_static_mock_applied_evidence_private_review_record.py` | Generator and private review output test |
| `docs/108-v0631-static-mock-applied-evidence-package-private-review-record.md` | Checkpoint documentation |
| `planning/decisions/ADR-0102-add-v0631-static-mock-applied-evidence-private-review-record.md` | Decision record |
| `planning/issues/0101-add-v0631-static-mock-applied-evidence-private-review-record.md` | Completed planning issue |

## Review input

Default review input:

~~~text
private-not-in-git/applied-evidence-runs/static-mock-demo/
~~~

The input package is expected to contain the v0.6.29 private static/mock generated
package.

If the package is missing, the review generator should fail closed rather than assume success.

If the package is missing, the review generator should fail closed rather than assume
success.

## Review output

Default review output:

~~~text
private-not-in-git/applied-evidence-review-records/static-mock-demo/
~~~

Generated private review outputs:

~~~text
private-review-record.generated.json
private-review-record.generated.md
promotion-gate-result.generated.json
promotion-gate-result.generated.md
~~~

Generated review outputs are not intended to be committed.

## Review criteria

The private review generator checks or records:

- package manifest presence,
- package summary presence,
- reviewer walkthrough presence,
- AAEF five questions mapping presence,
- package non-proof statement presence,
- four scenario directories,
- scenario-level request artifact presence,
- scenario-level gate decision artifact presence,
- scenario-level dispatch decision artifact presence,
- scenario-level result artifact presence,
- scenario-level evidence event artifact presence,
- scenario-level review summary presence,
- scenario-level non-proof statement presence,
- representative identifier linkage,
- runtime boundary flags,
- customer-target boundary flags,
- delivery authorization boundary flags.

The review is structural and boundary-oriented, not semantic assurance.

## Review status model

The private review record uses these statuses:

| Status | Meaning |
| --- | --- |
| `reviewed_keep_private` | Private package reviewed; remains private |
| `review_blocked_missing_input` | Required input package or artifact missing |
| `review_blocked_boundary_issue` | Runtime, customer, delivery, or overclaim boundary issue detected |
| `review_requires_human_attention` | Review uncertainty requires human attention |

The default safe successful status is `reviewed_keep_private`.

## Promotion gate result

The promotion gate result remains conservative:

~~~text
promotion_status = keep_private
public_sample_promotion_authorized = false
delivery_authorized = false
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
~~~

This result does not authorize public sample publication.

## Blocker categories

The private review generator records blocker categories such as:

- `missing_private_package`,
- `missing_package_manifest`,
- `missing_package_summary`,
- `missing_reviewer_walkthrough`,
- `missing_five_questions_mapping`,
- `missing_non_proof_statement`,
- `scenario_missing`,
- `artifact_missing`,
- `identifier_linkage_broken`,
- `runtime_boundary_issue`,
- `customer_target_boundary_issue`,
- `delivery_boundary_issue`,
- `public_promotion_boundary_issue`,
- `human_review_required`.

Any blocker keeps the package private.

## AAEF-side reporting result

The private review record can support AAEF-side reporting by providing:

- review id,
- reviewed package path,
- scenario coverage summary,
- artifact coverage summary,
- linkage summary,
- non-proof summary,
- promotion gate result,
- runtime/scanning/customer/delivery boundary summary,
- human-review recommendation.

Do not expose private generated package contents if the review remains private.

## Relationship to v0.6.30

v0.6.30 planned how to review the private package and how to decide whether public
sample promotion should even be considered.

v0.6.31 creates the private review record that captures the first review result while
keeping the package private.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.32 Static/Mock Applied Evidence Package Public Sample Promotion Decision Record
~~~

Rationale:

- v0.6.31 records private review status.
- A later decision can determine whether to plan a sanitized public sample.
- Public sample work should remain separate from private review record generation.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
private_package_review_record_generated = true
promotion_gate_result_generated = true
public_sample_promotion_authorized = false
public_sample_generated = false
public_artifact_generated = false
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

Avoid language implying that v0.6.31 promotes public samples, generates public sample
artifacts, provides real local-lab diagnostic evidence, provides live evidence, runs
scanners, creates Docker Compose files, approves Docker execution, pulls images,
starts containers, binds ports, approves production deployment, authorizes runtime
execution, authorizes scanning, permits credential injection, authorizes customer
targets, proves vulnerability detection accuracy, provides implementation conformance,
provides compliance certification, provides legal approval, provides audit opinion,
completes legal review, completes dependency audit, approves managed service use,
grants commercial license rights, guarantees safety, establishes external-framework
equivalence, provides audit sufficiency, provides legal sufficiency, approves public
samples, or authorizes delivery.

## Out of scope

This checkpoint does not promote public samples, generate public sample artifacts,
implement structural validators, execute structural validator checks, install Docker,
run Docker, pull images, start containers, bind ports, create Docker Compose files,
create a runnable Compose design, build a local lab, select a target for execution,
collect live preflight evidence, satisfy preflight, add dry-run lab execution, enable
runtime execution, enable scanning, add new scanner integrations, authorize report
delivery, expose private advanced feature details, create private sales material,
publish pricing, create a commercial contract, provide legal advice, authorize
external network testing, authorize credential injection, or authorize customer-target
testing.
