# v0.6.30 Static/Mock Applied Evidence Package Review and Promotion Gate Planning

Version: v0.6.30 candidate  
Status: review and promotion gate planning only; does not authorize runtime execution

## Purpose

This checkpoint defines how the private-first static/mock applied evidence package
generated in v0.6.29 should be reviewed before any public sanitized sample promotion
is considered.

v0.6.29 generated a private static/mock applied evidence package under
`private-not-in-git/applied-evidence-runs/static-mock-demo/`. v0.6.30 does not
promote that package to public materials. Instead, it defines the review gate,
promotion criteria, blocker categories, rollback posture, and AAEF-side reporting
boundary.

This checkpoint is review and promotion gate planning only.

This checkpoint does not promote public samples, generate public sample artifacts,
implement structural validators, execute structural validator checks, create runnable
configuration, create Docker Compose files, pull images, start containers, bind ports,
authorize Docker execution, authorize runtime execution, run scanners, inject
credentials, authorize customer-target operation, create customer deliverables,
provide certification, provide legal approval, or provide audit opinion.

## Public-safe design boundary

The review and promotion gate boundary is:

- AI output is treated as a request, not authority.
- AI may generate `tool_action_request`.
- Gates decide execution.
- Private generated artifacts are not public samples.
- Public sample promotion requires a separate gate.
- Static/mock evidence is not live diagnostic evidence.
- Static/mock evidence is not proof of diagnostic accuracy.
- Structural validator planning is not validator implementation.
- Public sample promotion is not delivery authorization.
- Customer-target operation remains blocked.
- Real local-lab diagnostic execution remains deferred.

Model output is not authority.

## Promotion gate proposition

~~~text
A private static/mock applied evidence package should not be promoted to public
sample material unless a review gate confirms that it is synthetic, non-executing,
non-customer, non-secret-bearing, non-patent-sensitive, non-overclaiming, and clear
about what it does not prove.
~~~

This proposition is intentionally non-executing.

## Review input package

The review input is the v0.6.29 private generated package:

~~~text
private-not-in-git/applied-evidence-runs/static-mock-demo/
~~~

Expected private package artifacts include:

- `package_manifest.generated.json`,
- `package_summary.generated.json`,
- `reviewer_walkthrough.generated.md`,
- `aaef_five_questions_mapping.generated.md`,
- `non_proof_statement.generated.md`,
- scenario-level generated request artifacts,
- scenario-level generated gate decision artifacts,
- scenario-level generated dispatch decision artifacts,
- scenario-level generated result artifacts,
- scenario-level generated evidence event artifacts,
- scenario-level generated review summaries,
- scenario-level generated non-proof statements.

This review input is private-first and not intended to be committed.

## Review objectives

The review should determine whether the private generated package is:

- complete enough for internal AAEF-side review,
- structurally coherent,
- internally linked,
- non-executing,
- synthetic,
- non-customer,
- non-secret-bearing,
- free of public overclaims,
- clear about non-proof boundaries,
- understandable to reviewers,
- not implying delivery authorization.

The review is not an audit opinion.

## Private package review criteria

Before any promotion discussion, the private package should pass these checks:

| Review area | Required result |
| --- | --- |
| Package location | remains under `private-not-in-git/` |
| Scenario coverage | four minimum scenarios present |
| Chain coverage | request, gate, dispatch, result, evidence, review present |
| Non-execution evidence | denied, held, and expired scenarios have non-execution results |
| Identifier linkage | request / decision / dispatch / result / evidence links are coherent |
| Non-proof visibility | package and scenario non-proof statements are visible |
| AAEF five questions | mapping exists and answers all five questions |
| Runtime boundary | scanner, Docker, real execution, credential injection are blocked |
| Customer boundary | no customer target or third-party target implication |
| Delivery boundary | no delivery authorization implication |

Any uncertainty should block public promotion.

## Promotion gate criteria

Public sanitized sample promotion should remain blocked unless all criteria are true:

- all content is synthetic,
- no real target names exist,
- no customer data exists,
- no credentials or secrets exist,
- no live scanner output exists,
- no Docker/runtime execution artifacts exist,
- no private patent-sensitive details exist,
- no confidential commercial strategy exists,
- no third-party target implication exists,
- no delivery authorization implication exists,
- non-proof statements are visible,
- AAEF five questions mapping is visible,
- reviewer walkthrough is readable,
- overclaim prevention passes,
- human review approves promotion.

Public sample promotion is not delivery authorization.

## Promotion blocker categories

Promotion should be blocked if any of these are present:

- `private_package_missing`,
- `scenario_missing`,
- `artifact_missing`,
- `identifier_linkage_broken`,
- `non_execution_evidence_missing`,
- `reviewer_walkthrough_missing`,
- `five_questions_mapping_missing`,
- `non_proof_statement_missing`,
- `secret_or_credential_detected`,
- `customer_target_implication_detected`,
- `third_party_target_implication_detected`,
- `live_scanner_output_detected`,
- `runtime_execution_implication_detected`,
- `docker_execution_implication_detected`,
- `delivery_authorization_implication_detected`,
- `audit_or_legal_sufficiency_claim_detected`,
- `certification_or_compliance_claim_detected`,
- `external_framework_equivalence_claim_detected`,
- `patent_sensitive_detail_detected`,
- `human_review_missing`.

Every blocker should keep the package private.

## Promotion outcomes

The promotion gate should allow only these outcomes:

| Outcome | Meaning |
| --- | --- |
| `keep_private` | Package remains private; no public sample work |
| `revise_private_package` | Package requires correction before another review |
| `approve_sanitized_public_sample_planning` | Planning for a sanitized public sample may begin |
| `reject_public_promotion` | Public promotion should not be pursued |

No outcome authorizes runtime execution, scanner execution, customer-target testing, or
report delivery.

## Public sample planning boundary

If public sample planning is later approved, that later checkpoint should:

- generate or copy only sanitized artifacts,
- use `.example.` naming or clearly public-safe sample naming,
- keep non-proof statements visible,
- avoid raw generated private content if not reviewed,
- avoid real target names,
- avoid private patent-sensitive details,
- avoid delivery language,
- avoid production-readiness language,
- run local publication hygiene checks.

Public sample planning should not include tool-backed local-lab execution.

## AAEF-side reporting boundary

After private package review, the AAEF side may receive:

- tag and commit,
- private package path existence,
- scenario list,
- artifact list,
- request-to-evidence chain summary,
- reviewer walkthrough path,
- AAEF five questions mapping path,
- non-proof statement path,
- local validation result,
- promotion gate status,
- explicit runtime/scanning/customer/delivery boundary note.

Do not expose private generated contents if the package remains private.

## Runtime and diagnostic execution separation

This checkpoint preserves three separate tracks:

| Track | Status |
| --- | --- |
| Private static/mock evidence package | generated in v0.6.29 |
| Public sanitized sample | not promoted by v0.6.30 |
| Tool-backed local-lab diagnostic execution | still deferred |

The earliest next step is review / promotion gate work, not live diagnostic execution.

## Structural validator relationship

A structural validator is still not implemented by this checkpoint.

A later validator implementation may support the promotion gate by checking:

- artifact presence,
- required fields,
- identifier linkage,
- scenario consistency,
- contradiction checks,
- non-execution evidence,
- reviewer walkthrough coverage,
- AAEF five questions mapping,
- non-proof statements,
- overclaim prevention.

Validator success must not imply semantic correctness, evidence sufficiency,
assessment sufficiency, production readiness, audit sufficiency, legal sufficiency,
implementation conformance, certification, compliance, or external-framework
equivalence.

## Rollback posture

If review identifies a blocker:

- keep generated package private,
- do not promote public samples,
- record blocker category,
- revise generator or generated package in a later checkpoint,
- rerun local checks,
- preserve non-execution and non-proof boundaries,
- do not use private package as customer deliverable.

Rollback is a safety control, not a failure.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.31 Static/Mock Applied Evidence Package Private Review Record
~~~

Rationale:

- v0.6.29 generated a private package.
- v0.6.30 plans the review and promotion gate.
- v0.6.31 can record a private review result for the generated package.
- Public sanitized sample promotion should remain a later gated decision.
- Real local-lab diagnostic execution should remain deferred.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
promotion_gate_planning_completed = true
public_sample_promotion_authorized = false
public_sample_generated = false
private_package_review_record_generated = false
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

## Claims to avoid

Avoid language implying that v0.6.30 provides public samples, real local-lab
diagnostic evidence, live evidence, scanner execution, Docker Compose file creation,
Docker execution approval, image pull approval, container startup approval, port
binding approval, production deployment approval, runtime execution readiness, scan
authorization, customer-target authorization, vulnerability detection accuracy,
implementation conformance, compliance certification, legal approval, audit opinion,
completed legal review, completed dependency audit, managed service approval,
commercial license grant, safety guarantee, external framework equivalence, audit
sufficiency, legal sufficiency, public sample approval, or delivery authorization.

## Out of scope

This checkpoint does not promote public samples, generate public sample artifacts,
generate a private review record, implement structural validators, execute structural
validator checks, install Docker, run Docker, pull images, start containers, bind
ports, create Docker Compose files, create a runnable Compose design, build a local
lab, select a target for execution, collect live preflight evidence, satisfy
preflight, add dry-run lab execution, enable runtime execution, enable scanning, add
new scanner integrations, authorize report delivery, expose private advanced feature
details, create private sales material, publish pricing, create a commercial
contract, provide legal advice, authorize external network testing, authorize
credential injection, or authorize customer-target testing.
