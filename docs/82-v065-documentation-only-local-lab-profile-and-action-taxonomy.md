# v0.6.5 Documentation-Only Local Lab Profile and Action Taxonomy

Version: v0.6.5 candidate  
Status: documentation-only local lab profile and action taxonomy; does not authorize runtime execution

## Purpose

This checkpoint defines the documentation-only local lab profile and action taxonomy
for AAEF-AI-VA.

v0.6.4 decided that the project may proceed with a documentation-only local lab
profile and dry-run planning, but must not build localhost-only controlled execution
yet.

This checkpoint turns that decision into a concrete profile and taxonomy.

This checkpoint is documentation-only.

This checkpoint does not build a local lab.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Decision carried forward

The v0.6.4 decision remains in force:

~~~text
Proceed with a documentation-only local lab profile and dry-run planning.
Do not build localhost-only controlled execution yet.
Do not enable runtime execution.
Do not enable scan execution.
Do not enable credential injection.
Do not authorize customer-target operation.
~~~

This checkpoint defines the profile and taxonomy needed before any dry-run lab
planning can advance.

## Documentation-only local lab profile

The local lab profile is documentation-only and non-executing.

| Field | Required value |
| --- | --- |
| `profile_id` | `documentation_only_local_lab_v0_6_5` |
| `profile_type` | `documentation_only` |
| `target_mode` | `localhost_only_or_documentation_only` |
| `target_ownership` | `owned_lab_target_only` |
| `third_party_target_allowed` | `false` |
| `customer_target_allowed` | `false` |
| `external_network_testing_allowed` | `false` |
| `runtime_execution_allowed` | `false` |
| `scan_execution_allowed` | `false` |
| `credential_injection_allowed` | `false` |
| `raw_sensitive_artifact_capture_allowed` | `false` |
| `generated_output_root` | `private-not-in-git/` |
| `human_review_required` | `true` |
| `delivery_authorization_required` | `true` |
| `public_claim_mode` | `conservative_evidence_backed` |

This profile is not an execution profile.

This profile is not a scanner configuration.

This profile is not a customer-target authorization record.

## Local-only assumptions

Future dry-run or fixture work must preserve these assumptions:

- target is documentation-only or localhost-only,
- target is owned by the operator,
- target is not a third-party system,
- target is not a customer system,
- external network testing is not allowed,
- runtime execution remains blocked,
- scan execution remains blocked,
- credential injection remains blocked,
- raw sensitive artifact capture remains blocked,
- generated outputs remain under `private-not-in-git/`,
- public claims remain conservative and evidence-backed.

## Allowed action taxonomy

The following action categories may be documented, modeled, or used in future dry-run
planning.

They do not authorize execution.

| Action category | Current status | Description |
| --- | --- | --- |
| `document_scope` | allowed_for_documentation | Record scope assumptions and exclusions |
| `record_target_profile` | allowed_for_documentation | Record local/documentation-only target metadata |
| `record_allowed_action` | allowed_for_documentation | Record an allowed action category without executing it |
| `record_denied_action` | allowed_for_documentation | Record a denied action category and denial reason |
| `record_preflight_requirement` | allowed_for_documentation | Record required preflight evidence |
| `record_human_review_requirement` | allowed_for_documentation | Record required review checkpoints |
| `generate_static_fixture` | allowed_for_static_fixture_planning | Plan future static examples without execution |
| `simulate_dry_run_request` | allowed_for_future_dry_run_planning | Plan a dry-run request shape without running tools |
| `record_expected_evidence` | allowed_for_documentation | Record expected evidence fields |
| `record_expected_denial` | allowed_for_documentation | Record expected fail-closed outcomes |
| `record_demo_non_proof` | allowed_for_documentation | Record what a demo or lab does not prove |
| `record_private_output_policy` | allowed_for_documentation | Record generated output boundary |

Allowed means documentation-allowed only at this stage.

Allowed does not mean execution-authorized.

## Denied action taxonomy

The following action categories are denied in the current public repository:

| Action category | Required decision | Reason |
| --- | --- | --- |
| `run_live_scan` | deny | Live scanning is not authorized |
| `test_external_network` | deny | External network testing is not authorized |
| `test_customer_target` | deny | Customer-target operation is not authorized |
| `inject_real_credentials` | deny | Credential injection against real systems is not authorized |
| `capture_raw_sensitive_artifact` | deny | Raw sensitive artifact capture is not authorized |
| `invoke_external_process` | deny | External process execution is not authorized |
| `perform_network_activity` | deny | Network activity is not authorized |
| `bypass_preflight` | deny | Preflight evidence remains required before any future execution path |
| `bypass_human_review` | deny | Human review remains required where assessment actions or findings are involved |
| `auto_promote_finding` | deny | Finding promotion requires review |
| `auto_deliver_report` | deny | Delivery authorization remains required |
| `claim_production_readiness` | deny | Production readiness is not demonstrated |
| `claim_compliance_certification` | deny | Compliance certification is not provided |
| `claim_legal_approval` | deny | Legal approval is not provided |
| `claim_audit_opinion` | deny | Audit opinion is not provided |
| `claim_commercial_license_grant` | deny | Commercial license is not granted by the repository |

Denied actions should fail closed in later fixture, dry-run, or validation work.

## Preflight evidence requirements

Before any future dry-run lab behavior is considered, the following evidence
requirements must be documented:

| Evidence requirement | Purpose |
| --- | --- |
| `scope_statement` | Confirms the lab scope and exclusions |
| `target_profile` | Confirms documentation-only or localhost-only target mode |
| `target_ownership_statement` | Confirms owned lab target only |
| `network_boundary_statement` | Confirms no external network testing |
| `allowed_action_taxonomy` | Confirms which documentation or dry-run actions are permitted |
| `denied_action_taxonomy` | Confirms which actions fail closed |
| `credential_policy` | Confirms no real credential injection |
| `artifact_policy` | Confirms no raw sensitive artifact capture |
| `human_review_requirement` | Confirms review obligations |
| `generated_output_policy` | Confirms outputs stay under `private-not-in-git/` |
| `non_proof_statement` | Confirms what the lab does not prove |
| `public_claim_boundary` | Confirms conservative public language |

Preflight evidence requirements are documentation requirements at this stage.

They are not execution authorization.

## Human review requirements

Future local lab planning must preserve these human review checkpoints:

| Review checkpoint | Required before |
| --- | --- |
| Scope review | Any dry-run scenario is accepted |
| Target profile review | Any target-like object is used in a fixture or dry-run |
| Action taxonomy review | Any action category is added or changed |
| Preflight evidence review | Any dry-run behavior is proposed |
| Finding review | Any finding candidate is promoted |
| Report review | Any report packet is prepared |
| Delivery authorization review | Any output is considered deliverable |
| Public claim review | Any public text describes lab capability |

Human review is part of the control model, not a cosmetic approval step.

## Generated output policy

Generated local outputs must remain under:

~~~text
private-not-in-git/
~~~

Allowed generated-output subpaths for future work may include:

~~~text
private-not-in-git/local-lab-profiles/
private-not-in-git/local-lab-taxonomy/
private-not-in-git/local-lab-dry-run-plans/
private-not-in-git/local-lab-review-records/
private-not-in-git/local-lab-non-proof-statements/
~~~

Generated outputs must not include:

- real customer data,
- real third-party target details,
- secrets,
- credentials,
- access tokens,
- raw sensitive vulnerability artifacts,
- live scan output,
- customer deliverables.

## What this lab does not prove

The documentation-only local lab profile does not prove:

- live scanning works,
- customer-target operation is authorized,
- external network testing is safe,
- credential injection is safe,
- runtime execution is ready,
- production deployment is ready,
- managed-service operation is ready,
- compliance certification exists,
- legal approval exists,
- audit opinion exists,
- commercial PoC readiness exists,
- commercial license is granted.

This exact boundary is required for future demo and dry-run planning.

## Dry-run planning readiness

This checkpoint makes dry-run planning more feasible, but does not authorize dry-run behavior yet.

This exact line is retained for validation compatibility when similar Markdown prose is line-wrapped.


This checkpoint makes dry-run planning more feasible, but does not authorize dry-run
behavior yet.

Before dry-run behavior is added, complete:

1. static local lab profile artifact,
2. static allowed and denied action taxonomy artifact,
3. preflight evidence requirement artifact,
4. human review requirement artifact,
5. dry-run request and response schema,
6. dry-run non-proof statement,
7. local validation for dry-run fixture behavior,
8. safety boundary review update,
9. public claim boundary review.

## Localhost-only controlled behavior remains deferred

Localhost-only controlled behavior remains deferred.

Before localhost-only controlled behavior is considered, complete:

- dry-run lab validation,
- concrete preflight checks,
- explicit local-only target binding,
- explicit action authorization model,
- explicit deny-by-default behavior,
- explicit no-credential-injection policy,
- explicit no-external-network policy,
- explicit evidence retention policy,
- explicit human review workflow,
- explicit rollback and cleanup plan.

This checkpoint does not satisfy those requirements by itself.

## Acceptance criteria for this checkpoint

This checkpoint is accepted if:

- the documentation-only profile is defined,
- local-only assumptions are defined,
- allowed action categories are defined,
- denied action categories are defined,
- preflight evidence requirements are defined,
- human review requirements are defined,
- generated output policy is defined,
- what this lab does not prove is defined,
- dry-run planning readiness is bounded,
- localhost-only controlled behavior remains deferred,
- runtime and scanning boundaries remain disabled,
- all local checks pass.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.6 Demo Scenario and Reviewer Walkthrough Planning
~~~

Rationale:

- v0.6.5 defines the documentation-only lab profile and action taxonomy.
- A reviewer walkthrough can explain the intended model without enabling execution.
- Dry-run behavior should still wait until profile, taxonomy, and demo boundaries are clear.
- Runtime gate hardening remains valuable but should use the profile and taxonomy defined here.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- completed legal review,
- completed dependency audit,
- managed service approval,
- commercial license grant,
- safety guarantee,
- external framework equivalence,
- audit sufficiency.

## Required local checks

Before tagging v0.6.5, verify:

1. README links to this checkpoint.
2. Decision carried forward is recorded.
3. Documentation-only local lab profile is recorded.
4. Local-only assumptions are recorded.
5. Allowed action taxonomy is recorded.
6. Denied action taxonomy is recorded.
7. Preflight evidence requirements are recorded.
8. Human review requirements are recorded.
9. Generated output policy is recorded.
10. What this lab does not prove is recorded.
11. Dry-run planning readiness is recorded.
12. Localhost-only controlled behavior remains deferred.
13. Acceptance criteria are recorded.
14. Runtime and scanning boundaries remain disabled.
15. Claims to avoid are recorded.
16. `tools/run_all_local_checks.py` includes the v0.6.5 documentation-only local lab test.

## Out of scope

This checkpoint does not:

- build a local lab,
- add static lab fixtures,
- add dry-run lab execution,
- enable runtime execution,
- enable scanning,
- create private sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- configure GitHub branch protection,
- configure GitHub rulesets,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
