# v0.6.33 Sanitized Public Sample Planning

Version: v0.6.33 candidate  
Status: sanitized public sample planning only; does not authorize runtime execution

## Purpose

This checkpoint plans how a future sanitized public sample may be prepared from the
static/mock applied evidence package lineage.

v0.6.29 generated a private static/mock applied evidence package. v0.6.31 generated a
private review record. v0.6.32 recorded the promotion decision: the private package
remains private, direct public sample generation remains unauthorized, and a later
sanitized public sample planning checkpoint may be considered.

v0.6.33 is that planning checkpoint. It does not generate public samples.

This checkpoint is sanitized public sample planning only.

This checkpoint does not generate public sample artifacts, copy private generated
artifacts into the public repository, implement structural validators, execute
structural validator checks, create runnable configuration, create Docker Compose
files, pull images, start containers, bind ports, authorize Docker execution,
authorize runtime execution, run scanners, inject credentials, authorize
customer-target operation, create customer deliverables, provide certification,
provide legal approval, or provide audit opinion.

## Public-safe design boundary

The sanitized public sample planning boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Public sample planning is not public sample generation.
- Public sample planning is not private artifact promotion.
- Private generated artifacts remain private unless a later checkpoint creates
  explicitly sanitized public examples.
- Sanitized public examples, if later generated, must be synthetic.
- Static/mock evidence is not live diagnostic evidence.
- Static/mock evidence is not proof of diagnostic accuracy.
- Customer-target operation remains blocked.
- Delivery authorization remains separately gated.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Planning proposition

~~~text
A sanitized public sample may be planned only if the public artifacts are synthetic,
reviewer-facing, non-executing, non-customer, non-secret-bearing, non-patent-sensitive,
and explicit about what they do not prove.
~~~

This proposition is intentionally non-executing.

## Public sample scope

A future sanitized public sample should be limited to demonstrating the AAEF control
chain, not diagnostic effectiveness.

Allowed public sample goals:

- show that AI output is a request,
- show that gates decide execution,
- show request-to-decision-to-dispatch-to-result-to-evidence linkage,
- show permitted, denied, held, and not-executed outcomes,
- show non-execution evidence as first-class evidence,
- show AAEF five questions mapping,
- show non-proof boundaries.

Disallowed public sample goals:

- proving scanner accuracy,
- proving vulnerability detection coverage,
- proving production readiness,
- proving implementation conformance,
- proving audit sufficiency,
- proving legal sufficiency,
- proving compliance,
- proving external-framework equivalence,
- authorizing customer-target testing,
- authorizing report delivery.

## Candidate public directory placement

A future sanitized public sample may use a public example directory such as:

~~~text
examples/applied-evidence/sanitized-static-mock/
~~~

This checkpoint does not create that directory.

The private source lineage remains:

~~~text
private-not-in-git/applied-evidence-runs/static-mock-demo/
private-not-in-git/applied-evidence-review-records/static-mock-demo/
~~~

Private paths should not be copied directly into the public tree.

## Sanitized artifact naming

Future sanitized public artifacts should use `.example.` naming rather than
`.generated.` naming.

Candidate names:

| Private/generated artifact | Future public sanitized name |
| --- | --- |
| `package_manifest.generated.json` | `package_manifest.example.json` |
| `tool_action_request.generated.json` | `tool_action_request.example.json` |
| `gate_decision.generated.json` | `gate_decision.example.json` |
| `dispatch_decision.generated.json` | `dispatch_decision.example.json` |
| `execution_result.generated.json` | `execution_result.example.json` |
| `non_execution_result.generated.json` | `non_execution_result.example.json` |
| `evidence_event.generated.json` | `evidence_event.example.json` |
| `review_summary.generated.md` | `review_summary.example.md` |
| `non_proof_statement.generated.md` | `non_proof_statement.example.md` |
| `reviewer_walkthrough.generated.md` | `reviewer_walkthrough.example.md` |
| `aaef_five_questions_mapping.generated.md` | `aaef_five_questions_mapping.example.md` |

Generated private filenames should not be exposed as if they were public evidence.

## Scenario coverage plan

A future sanitized public sample should preserve the four minimum scenarios:

| Scenario | Public sample posture |
| --- | --- |
| `permitted-safe-diagnostic` | static/mock permitted trace only |
| `denied-out-of-scope-request` | static/mock denied non-execution trace |
| `human-approval-required` | static/mock held non-execution trace |
| `not-executed-expired` | static/mock expired / not-executed trace |

The scenario set should remain synthetic and non-executing.

## Private-to-public transformation rules

A future transformation must:

- create new sanitized files rather than copying private outputs blindly,
- replace generated IDs with public example IDs,
- remove private output paths,
- remove private review paths,
- remove timestamps if they imply live operation,
- remove local filesystem paths,
- remove any raw output references,
- remove customer-like names,
- remove credential references unless synthetic and non-secret,
- remove tool-output details that imply scanner execution,
- keep non-proof statements visible,
- keep AAEF five questions mapping visible.

Transformation must be reviewable before publication.

## Synthetic-only requirements

Future public sample artifacts must contain only:

- synthetic scenario IDs,
- synthetic request IDs,
- synthetic decision IDs,
- synthetic dispatch IDs,
- synthetic result IDs,
- synthetic evidence event IDs,
- synthetic local-lab principal references,
- synthetic tool names in non-executing context,
- synthetic policy versions,
- synthetic result summaries,
- synthetic non-execution reasons,
- synthetic reviewer explanations.

They must not contain customer data, production data, secrets, credentials, live scan
output, third-party target details, or operational runtime traces.

## Publication hygiene checks

Before a future public sample is generated or committed, publication hygiene should
check for:

- private path leakage,
- secrets,
- credentials,
- tokens,
- cookies,
- raw HTTP messages,
- raw scanner output,
- customer names,
- real target hostnames,
- IP addresses unless reserved/example-only,
- local filesystem paths,
- patent-sensitive private details,
- public overclaims,
- delivery authorization language,
- runtime authorization language.

Any uncertainty should block publication.

## Patent-sensitive detail exclusion

Future public sanitized samples must avoid patent-sensitive private details.

The public sample should stay at the abstract AAEF boundary:

- AI output as request,
- gate decision,
- dispatch / non-dispatch,
- evidence linkage,
- reviewer summary,
- non-proof statement.

Do not include private advanced feature details, claim drafts, prior-art analysis,
patent strategy, or implementation details that were intentionally kept private.

## Non-proof visibility

Every future public sample package should include visible non-proof statements.

Non-proof statements should reject claims of:

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

Non-proof statements should not be hidden in JSON only.

## Overclaim prevention

Future public sample text must avoid implying:

- public sample approval equals delivery authorization,
- static/mock evidence equals live diagnostic evidence,
- structural consistency equals semantic correctness,
- example artifacts equal production readiness,
- AAEF example coverage equals compliance,
- gate examples equal legal approval,
- reviewer walkthrough equals audit opinion,
- public sample equals managed service readiness.

Overclaim prevention is a blocker for publication.

## Human publication review

A future public sample generation candidate should require human publication review.

Human review should confirm:

- the sample is synthetic,
- the sample is non-executing,
- private paths are removed,
- private generated content is not copied blindly,
- non-proof statements are visible,
- AAEF five questions mapping is clear,
- no customer target is implied,
- no scanner execution is implied,
- no delivery authorization is implied,
- no patent-sensitive private detail is exposed.

Human publication review remains a gate.

## Future generation gate

A later public sample generation checkpoint should remain blocked unless:

- this planning checkpoint is accepted,
- publication hygiene checks are implemented or documented,
- sanitized artifact naming is accepted,
- public directory placement is accepted,
- human publication review is recorded,
- non-proof visibility is required,
- overclaim prevention is required,
- runtime/scanning/customer/delivery boundaries remain false.

Planning acceptance is not generation authorization.

## AAEF-side reporting note

AAEF-side reporting may state:

- sanitized public sample planning exists,
- public sample generation remains unauthorized,
- private package remains private,
- private review record remains private,
- future public sample generation would require a separate checkpoint,
- runtime/scanner/customer-target/delivery authorization remains false.

AAEF-side reporting should not expose private generated contents.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.34 Sanitized Public Sample Generation Readiness Review
~~~

Rationale:

- v0.6.33 plans sanitized public sample boundaries.
- The next safe step is a readiness review, not generation.
- Public sample generation should remain a later gated decision.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
sanitized_public_sample_planning_completed = true
sanitized_public_sample_generation_ready = false
public_sample_generation_authorized = false
public_sample_promotion_authorized = false
public_sample_generated = false
public_artifact_generated = false
private_package_review_record_generated = true
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

Avoid language implying that v0.6.33 generates public sample artifacts, promotes
private artifacts, provides real local-lab diagnostic evidence, provides live
evidence, runs scanners, creates Docker Compose files, approves Docker execution,
pulls images, starts containers, binds ports, approves production deployment,
authorizes runtime execution, authorizes scanning, permits credential injection,
authorizes customer targets, proves vulnerability detection accuracy, provides
implementation conformance, provides compliance certification, provides legal
approval, provides audit opinion, completes legal review, completes dependency audit,
approves managed service use, grants commercial license rights, guarantees safety,
establishes external-framework equivalence, provides audit sufficiency, provides legal
sufficiency, approves public samples, or authorizes delivery.

## Out of scope

This checkpoint does not generate public sample artifacts, copy private generated
artifacts into the public repository, implement structural validators, execute
structural validator checks, install Docker, run Docker, pull images, start
containers, bind ports, create Docker Compose files, create a runnable Compose design,
build a local lab, select a target for execution, collect live preflight evidence,
satisfy preflight, add dry-run lab execution, enable runtime execution, enable
scanning, add new scanner integrations, authorize report delivery, expose private
advanced feature details, create private sales material, publish pricing, create a
commercial contract, provide legal advice, authorize external network testing,
authorize credential injection, or authorize customer-target testing.
