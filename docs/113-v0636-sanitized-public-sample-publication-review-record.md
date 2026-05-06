# v0.6.36 Sanitized Public Sample Publication Review Record

Version: v0.6.36 candidate  
Status: sanitized public sample publication review recording; does not authorize runtime execution

## Purpose

This checkpoint records a publication review for the sanitized public sample candidate
created in v0.6.35.

v0.6.35 generated synthetic, non-executing `.example.` artifacts under:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

v0.6.36 adds a bounded generator that reviews those public example artifacts and
writes publication review records into the same public example directory.

This checkpoint is sanitized public sample publication review recording only.

This checkpoint does not implement structural validators, execute structural validator
checks, create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The publication review boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Publication review is not runtime execution.
- Publication review is not diagnostic validation.
- Publication review is not delivery authorization.
- The sample remains a limited public example.
- Public example artifacts remain synthetic.
- Public example artifacts remain non-executing.
- Static/mock examples are not live diagnostic evidence.
- Static/mock examples are not proof of diagnostic accuracy.
- Customer-target operation remains blocked.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Review proposition

~~~text
A sanitized public sample candidate can be retained as a limited public example only
when publication review confirms synthetic content, `.example.` naming, four-scenario
coverage, non-proof visibility, AAEF five-questions visibility, hygiene posture, and
unchanged runtime, scanner, customer-target, and delivery boundaries.
~~~

This proposition authorizes only publication review recording for the sanitized public
example.

This proposition authorizes only publication review recording for the sanitized public example.

## Implemented publication review generator

This checkpoint adds:

| File | Purpose |
| --- | --- |
| `tools/generate_sanitized_public_sample_publication_review_record.py` | Publication review record generator |
| `tools/test_v0636_sanitized_public_sample_publication_review_record.py` | Publication review validation test |
| `docs/113-v0636-sanitized-public-sample-publication-review-record.md` | Checkpoint documentation |
| `planning/decisions/ADR-0107-add-v0636-sanitized-public-sample-publication-review-record.md` | Decision record |
| `planning/issues/0106-add-v0636-sanitized-public-sample-publication-review-record.md` | Completed planning issue |

## Review input

The review input is the v0.6.35 sanitized public sample candidate:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Expected package-level inputs:

- `README.md`,
- `package_manifest.example.json`,
- `reviewer_walkthrough.example.md`,
- `aaef_five_questions_mapping.example.md`,
- `non_proof_statement.example.md`,
- `publication_hygiene_report.example.json`,
- `publication_hygiene_report.example.md`.

Expected scenario inputs are `.example.` request, gate, dispatch, result, evidence,
review summary, and non-proof statement artifacts for the four minimum scenarios.

## Review output

The generator writes:

~~~text
examples/applied-evidence/sanitized-static-mock/
  publication_review_record.example.json
  publication_review_record.example.md
~~~

The generated review record is a public example review artifact, not a customer
deliverable.

The generated review record is a public example review artifact, not a customer deliverable.

## Review criteria

The publication review checks or records:

- package manifest exists,
- reviewer walkthrough exists,
- AAEF five questions mapping exists,
- non-proof statement exists,
- publication hygiene report exists,
- four scenario directories exist,
- expected `.example.` artifacts exist,
- representative linkage is coherent,
- non-proof statements are visible,
- publication hygiene status is `passed`,
- runtime execution remains unauthorized,
- scanner execution remains unauthorized,
- customer-target operation remains blocked,
- delivery authorization remains false.

The review is publication-oriented, not diagnostic assurance.

## Publication review status

The expected successful status is:

~~~text
publication_review_status = reviewed_retain_limited_public_example
publication_limit = limited_synthetic_non_executing_example
public_sample_publication_review_completed = true
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
delivery_authorized = false
~~~

This status does not elevate the example into production guidance, implementation
conformance, audit evidence, legal advice, or customer deliverable material.

This status does not elevate the example into production guidance, implementation conformance, audit evidence, legal advice, or customer deliverable material.

## Blocker categories

The publication review records blocker categories such as:

- `example_root_missing`,
- `package_manifest_missing`,
- `reviewer_walkthrough_missing`,
- `five_questions_mapping_missing`,
- `package_non_proof_statement_missing`,
- `publication_hygiene_report_missing`,
- `scenario_missing`,
- `artifact_missing`,
- `non_example_artifact_name_detected`,
- `identifier_linkage_broken`,
- `non_proof_statement_missing`,
- `hygiene_status_not_passed`,
- `runtime_boundary_issue`,
- `scanner_boundary_issue`,
- `customer_target_boundary_issue`,
- `delivery_boundary_issue`,
- `human_review_recommended`.

Any blocker should prevent treating the sample as reviewed.

## AAEF-side reporting note

AAEF-side reporting may state:

- sanitized public sample candidate exists,
- publication review record exists,
- publication review status is limited-public-example retention if checks pass,
- sample artifacts are synthetic,
- sample artifacts are non-executing,
- non-proof statements are visible,
- AAEF five questions mapping is visible,
- runtime/scanner/customer-target/delivery authorization remains false.

AAEF-side reporting should not claim diagnostic accuracy, implementation conformance,
audit sufficiency, legal sufficiency, compliance certification, external-framework
equivalence, or production readiness.

## Relationship to diagnostic execution

This checkpoint does not move toward tool-backed diagnostic execution.

| Track | v0.6.36 status |
| --- | --- |
| Sanitized public sample candidate | generated in v0.6.35 |
| Publication review record | generated by v0.6.36 |
| Runtime execution | not authorized |
| Scanner execution | not authorized |
| Customer-target operation | blocked |
| Delivery authorization | blocked |
| Structural validator implementation | not implemented |
| Tool-backed local-lab diagnostic execution | deferred |

The next safe step is structural validation planning for public examples or a public
sample close-readiness review, not live diagnostic execution.

The next safe step is structural validation planning for public examples or a public sample close-readiness review, not live diagnostic execution.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.37 Sanitized Public Sample Close-Readiness Review
~~~

Rationale:

- v0.6.35 generated a public sample candidate.
- v0.6.36 records publication review.
- A close-readiness review can decide whether this public sample track is complete
  enough before returning to structural validator implementation or local-lab
  diagnostic planning.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = true
publication_review_record_generated = true
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

Avoid language implying that v0.6.36 provides real local-lab diagnostic evidence,
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

This checkpoint does not implement structural validators, execute structural validator
checks, install Docker, run Docker, pull images, start containers, bind ports, create
Docker Compose files, create a runnable Compose design, build a local lab, select a
target for execution, collect live preflight evidence, satisfy preflight, add dry-run
lab execution, enable runtime execution, enable scanning, add new scanner integrations,
authorize report delivery, expose private advanced feature details, create private
sales material, publish pricing, create a commercial contract, provide legal advice,
authorize external network testing, authorize credential injection, or authorize
customer-target testing.
