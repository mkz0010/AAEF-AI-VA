# v0.6.38 Public Example Structural Validation Planning

Version: v0.6.38 candidate  
Status: structural validation planning only; does not authorize runtime execution

## Purpose

This checkpoint plans structural validation for the sanitized public sample artifact
set created by the v0.6.35 through v0.6.37 track.

The public sample track currently has:

~~~text
sanitized_public_sample_candidate_generated = true
public_sample_publication_review_completed = true
publication_review_record_generated = true
sanitized_public_sample_track_close_ready = true
retain_limited_public_example = true
~~~

The public sample is located at:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

v0.6.38 plans how a later validator should check that public `.example.` artifact set.

This checkpoint is structural validation planning only.

This checkpoint does not implement structural validators, execute structural validator
checks, create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The structural validation planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Structural validation planning is not validator implementation.
- Structural validation planning is not runtime execution.
- Structural validation planning is not diagnostic validation.
- Structural validation planning is not delivery authorization.
- Future validator success must not imply production readiness.
- Future validator success must not imply diagnostic accuracy.
- Future validator success must not imply implementation conformance.
- Future validator success must not imply audit sufficiency.
- Future validator success must not imply legal sufficiency.
- Future validator success must not imply compliance certification.
- Future validator success must not imply external-framework equivalence.
- Customer-target operation remains blocked.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Planning proposition

~~~text
A future public example structural validator may check artifact presence, naming,
scenario coverage, linkage, non-proof visibility, publication hygiene posture, and
runtime/scanning/customer/delivery boundary flags for the sanitized public sample
without treating structural validity as diagnostic correctness, production readiness,
implementation conformance, audit sufficiency, legal sufficiency, compliance, or
delivery authorization.
~~~

This proposition authorizes only structural validation planning for public examples.

This proposition authorizes only structural validation planning for public examples.

## Validation input scope

A future validator should focus on:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

Expected package-level artifacts:

- `README.md`,
- `package_manifest.example.json`,
- `reviewer_walkthrough.example.md`,
- `aaef_five_questions_mapping.example.md`,
- `non_proof_statement.example.md`,
- `publication_hygiene_report.example.json`,
- `publication_hygiene_report.example.md`,
- `publication_review_record.example.json`,
- `publication_review_record.example.md`.

Expected scenario directories:

- `permitted-safe-diagnostic`,
- `denied-out-of-scope-request`,
- `human-approval-required`,
- `not-executed-expired`.

## Planned validation objectives

The future validator should help reviewers answer:

- Is the public example artifact set complete?
- Does it use public `.example.` naming?
- Are all four minimum scenarios present?
- Are request, gate, dispatch, result, and evidence artifacts linked?
- Are non-execution scenarios represented as non-execution evidence?
- Are non-proof statements visible?
- Is AAEF five-questions mapping visible?
- Did publication hygiene pass?
- Are runtime/scanning/customer/delivery boundaries still false?
- Are overclaims absent from public example artifacts?

The validator should be structural and boundary-oriented, not semantic assurance.

## Planned required-artifact checks

A later validator should check package-level required artifacts:

| Artifact | Required |
| --- | --- |
| `README.md` | yes |
| `package_manifest.example.json` | yes |
| `reviewer_walkthrough.example.md` | yes |
| `aaef_five_questions_mapping.example.md` | yes |
| `non_proof_statement.example.md` | yes |
| `publication_hygiene_report.example.json` | yes |
| `publication_hygiene_report.example.md` | yes |
| `publication_review_record.example.json` | yes |
| `publication_review_record.example.md` | yes |

A missing required artifact should fail closed.

A missing required artifact should fail closed.

## Planned scenario checks

A later validator should require four scenarios:

| Scenario | Required result artifact |
| --- | --- |
| `permitted-safe-diagnostic` | `execution_result.example.json` |
| `denied-out-of-scope-request` | `non_execution_result.example.json` |
| `human-approval-required` | `non_execution_result.example.json` |
| `not-executed-expired` | `non_execution_result.example.json` |

Each scenario should include:

- `tool_action_request.example.json`,
- `gate_decision.example.json`,
- `dispatch_decision.example.json`,
- result artifact,
- `evidence_event.example.json`,
- `review_summary.example.md`,
- `non_proof_statement.example.md`.

## Planned naming checks

A later validator should require public artifacts to use `.example.` naming except for
directory names and `README.md`.

The validator should reject:

- `.generated.` public artifact names,
- private review artifact names,
- private run artifact names,
- raw runtime output names,
- customer-deliverable names,
- scanner-output names.

Public examples should remain examples, not generated private evidence.

## Planned linkage checks

A later validator should check representative linkage:

~~~text
gate_decision.linked_request_id == tool_action_request.request_id
dispatch_decision.linked_decision_id == gate_decision.decision_id
result.linked_dispatch_decision_id == dispatch_decision.dispatch_decision_id
evidence_event.linked_request_id == tool_action_request.request_id
evidence_event.linked_decision_id == gate_decision.decision_id
evidence_event.linked_dispatch_decision_id == dispatch_decision.dispatch_decision_id
evidence_event.linked_result_id == result.result_id
~~~

Identifier linkage checks are structural checks, not proof that an action was safe.

Identifier linkage checks are structural checks, not proof that an action was safe.

## Planned scenario posture checks

A later validator should check expected scenario posture:

| Scenario | Expected posture |
| --- | --- |
| `permitted-safe-diagnostic` | synthetic permitted trace; no real execution |
| `denied-out-of-scope-request` | denied and non-executed |
| `human-approval-required` | held and non-executed pending approval |
| `not-executed-expired` | expired and non-executed |

The validator should reject contradictions such as:

- denied scenario with execution result,
- held scenario with dispatch attempted,
- expired scenario with execution result,
- non-execution scenario without non-execution reason,
- result artifact claiming real execution,
- evidence artifact implying scanner output.

## Planned non-proof checks

A later validator should require non-proof statements at:

- package level,
- every scenario level,
- reviewer-facing summaries where appropriate.

Non-proof statements should reject claims of:

- vulnerability detection accuracy,
- diagnostic completeness,
- production readiness,
- implementation conformance,
- audit sufficiency,
- legal sufficiency,
- compliance certification,
- external-framework equivalence,
- customer-target authorization,
- delivery authorization,
- safety guarantee.

Non-proof visibility is a validation requirement.

## Planned AAEF five-questions checks

A later validator should require:

- `aaef_five_questions_mapping.example.md` exists,
- the mapping mentions all five AAEF questions,
- scenario review summaries reference the request, gate, dispatch, result, and evidence chain,
- evidence events link to the artifacts needed to reconstruct the scenario.

The five-questions mapping is reviewer guidance, not audit opinion.

## Planned publication hygiene checks

A later validator should check or consume the publication hygiene report.

Expected hygiene status:

~~~text
hygiene_status = passed
~~~

The validator should fail closed if the hygiene report is missing, malformed, or not
passed.

Publication hygiene should include checks for:

- private path leakage,
- private generated artifact leakage,
- secrets,
- credentials,
- tokens,
- cookies,
- raw protocol messages,
- raw scanner output,
- customer-like names,
- real target hostnames,
- non-example IP addresses,
- local filesystem paths,
- patent-sensitive private details,
- public overclaims,
- runtime authorization language,
- delivery authorization language.

## Planned runtime boundary checks

A later validator should require boundary flags to remain false:

~~~text
private_artifact_copied_to_public = false
runtime_execution_authorized = false
scanner_execution_authorized = false
scan_execution_allowed = false
credential_injection_permitted = false
customer_target = false
customer_target_authorized = false
delivery_authorized = false
customer_deliverable = false
structural_validator_implemented = false
structural_validator_checks_execute = false
tool_backed_diagnostic_capture_started = false
local_lab_diagnostic_system_built = false
~~~

If a future validator is implemented, `structural_validator_implemented` may become
true for the validator implementation checkpoint, but validator success must still not
authorize runtime execution, scanner execution, customer-target operation, or delivery.

## Planned failure categories

A later validator should use failure categories such as:

- `example_root_missing`,
- `package_artifact_missing`,
- `scenario_missing`,
- `scenario_artifact_missing`,
- `non_example_artifact_name_detected`,
- `private_generated_artifact_name_detected`,
- `identifier_linkage_broken`,
- `scenario_posture_contradiction`,
- `non_execution_evidence_missing`,
- `non_proof_statement_missing`,
- `five_questions_mapping_missing`,
- `publication_hygiene_missing`,
- `publication_hygiene_not_passed`,
- `private_path_leakage_detected`,
- `secret_or_credential_detected`,
- `customer_target_implication_detected`,
- `runtime_execution_implication_detected`,
- `scanner_execution_implication_detected`,
- `delivery_authorization_implication_detected`,
- `overclaim_detected`.

Any validation uncertainty should fail closed.

Any validation uncertainty should fail closed.

## Planned validator output

A later validator may output a local summary such as:

~~~text
public_example_structural_validation_status = passed
scenario_count = 4
hygiene_status = passed
blocker_categories = []
runtime_execution_authorized = false
scanner_execution_authorized = false
customer_target_authorized = false
delivery_authorized = false
~~~

This output should not be treated as diagnostic evidence.

## AAEF-side reporting note

AAEF-side reporting may state:

- public example structural validation planning exists,
- the public sample remains a limited synthetic non-executing example,
- future validation would be structural and boundary-oriented,
- future validator success would not prove diagnostic accuracy,
- runtime/scanner/customer-target/delivery authorization remains false.

AAEF-side reporting should not claim diagnostic accuracy, implementation conformance,
audit sufficiency, legal sufficiency, compliance certification, external-framework
equivalence, production readiness, or customer deliverable status.

## Relationship to diagnostic execution

This checkpoint does not move toward tool-backed diagnostic execution.

| Track | v0.6.38 status |
| --- | --- |
| Sanitized public sample candidate | generated |
| Publication review record | generated |
| Public sample close-readiness | reviewed |
| Public example structural validation | planned only |
| Runtime execution | not authorized |
| Scanner execution | not authorized |
| Customer-target operation | blocked |
| Delivery authorization | blocked |
| Structural validator implementation | not implemented |
| Tool-backed local-lab diagnostic execution | deferred |

The next safe step is public example structural validator implementation readiness
review or minimal validator implementation, not live diagnostic execution.

The next safe step is public example structural validator implementation readiness review or minimal validator implementation, not live diagnostic execution.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.39 Public Example Structural Validator Implementation Readiness Review
~~~

Rationale:

- v0.6.38 plans structural validation.
- The next safe step is readiness review before writing validator code.
- Validator implementation should remain read-only and public-example scoped.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
public_example_structural_validation_planning_completed = true
public_example_structural_validator_implementation_ready = false
public_example_structural_validator_implemented = false
public_example_structural_validator_checks_execute = false
sanitized_public_sample_track_close_ready = true
retain_limited_public_example = true
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

Avoid language implying that v0.6.38 implements structural validators, executes
structural validator checks, provides real local-lab diagnostic evidence, provides
live evidence, runs scanners, creates Docker Compose files, approves Docker execution,
pulls images, starts containers, binds ports, approves production deployment,
authorizes runtime execution, authorizes scanning, permits credential injection,
authorizes customer targets, proves vulnerability detection accuracy, provides
implementation conformance, provides compliance certification, provides legal
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
