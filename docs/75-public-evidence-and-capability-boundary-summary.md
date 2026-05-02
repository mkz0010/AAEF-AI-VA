# Public Evidence and Capability Boundary Summary

Version: v0.5.9 candidate  
Status: public evidence and capability explanation; does not authorize runtime execution

## Purpose

This document explains what AAEF-AI-VA currently demonstrates and what it does not
yet demonstrate.

The public repository is both a reference implementation and a product-introduction
surface. That means public readers need a clear answer to a simple question:

> What has this repository actually shown?

This checkpoint answers that question conservatively.

It separates:

- demonstrated capabilities,
- evidence-backed public claims,
- intentionally blocked capabilities,
- non-demonstrated capabilities,
- future capability candidates,
- unsupported claims to avoid.

This checkpoint is an evidence and capability explanation only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Summary statement

AAEF-AI-VA currently demonstrates a safety-first control boundary pattern for
AI-assisted vulnerability assessment workflows.

It demonstrates local validation of control gates, review gates, evidence linkage,
report promotion, delivery authorization, publication hygiene, licensing boundaries,
security policy boundaries, repository governance, release governance, and reviewer
navigation.

It does not demonstrate live scanning.

It does not demonstrate customer-target operation.

It does not demonstrate production deployment.

It does not demonstrate certification, legal approval, audit opinion, or compliance
equivalence.

## What is demonstrated

The repository currently demonstrates:

| Demonstrated area | Public evidence |
| --- | --- |
| Tool Gateway behavior | `tools/test_tool_gateway_runner.py`, `tools/test_tool_gateway_adapters.py` |
| Controlled executor policy | `tools/test_controlled_executor_policy.py` |
| Real execution readiness blocking | `tools/test_real_execution_readiness_gate.py` |
| Operator readiness review | `tools/test_operator_readiness_review.py` |
| Human approval gate | `tools/test_human_approval_gate.py` |
| Evidence chain linkage | `tools/test_evidence_chain_linkage.py` |
| Evidence reconstruction reporting | `tools/test_evidence_reconstruction_report.py` |
| Sanitizer redaction policy | `tools/test_sanitizer_redaction_policy.py` |
| Finding candidate modeling | `tools/test_finding_candidate_model.py` |
| Finding review gate | `tools/test_finding_review_gate.py` |
| Report finding promotion | `tools/test_report_finding_promotion_gate.py` |
| Report review gate | `tools/test_report_review_gate.py` |
| Report packet review gate | `tools/test_report_packet_review_gate.py` |
| Delivery authorization gate | `tools/test_delivery_authorization_gate.py` |
| Lifecycle integration checkpoint | `tools/test_lifecycle_integration_checkpoint.py` |
| Runtime readiness blocking | `tools/test_runtime_readiness_gate.py` |
| Local target lab profile boundary | `tools/test_local_target_lab_profile.py` |
| Runtime destination binding boundary | `tools/test_runtime_destination_binding.py` |
| Bounded execution transition candidate | `tools/test_bounded_execution_transition_candidate.py` |
| Local execution plan review | `tools/test_local_execution_plan_review.py` |
| Runtime safety policy | `tools/test_runtime_safety_policy.py` |
| Runtime enforcement design | `tools/test_runtime_enforcement_design.py` |
| Execution authorization gate scaffold | `tools/test_execution_authorization_gate.py` |
| Preflight validation scaffold | `tools/test_preflight_validation.py` |
| Preflight evidence examples and validation rules | `tools/test_preflight_evidence_examples.py`, `tools/test_preflight_evidence_validation_rules.py`, `tools/test_preflight_evidence_negative_examples.py` |
| Licensing and commercial-use boundary | `tools/test_licensing_and_commercial_use_boundary.py` |
| Public repository readiness | `tools/test_public_repository_readiness_checkpoint.py` |
| Publication hygiene and private artifact exclusion | `tools/test_publication_hygiene_private_artifact_exclusion.py` |
| Security policy and vulnerability disclosure | `tools/test_public_security_policy_vulnerability_disclosure.py` |
| GitHub Actions CI scaffold | `tools/test_github_actions_ci_scaffold.py` |
| README public wording and compatibility | `tools/test_readme_public_english_wording.py`, `tools/test_readme_compatibility_phrase_registry.py` |
| Commercial adoption preparation | `tools/test_commercial_adoption_preparation_checkpoint.py` |
| Licensing, trademark, authorship, and commercial-use protection | `tools/test_licensing_trademark_authorship_protection.py` |
| Dependency and repository governance readiness | `tools/test_dependency_repository_governance_readiness.py` |
| Repository ruleset and branch protection planning | `tools/test_github_repository_ruleset_branch_protection_planning.py` |
| Release governance and maintainer operations | `tools/test_release_governance_maintainer_operations_checklist.py` |
| Public trust and reviewer navigation | `tools/test_public_trust_reviewer_navigation.py` |
| Public front page and repository landing polish | `tools/test_public_front_page_landing_polish.py` |

## What is evidence-backed

The following public claims are evidence-backed by repository files and local tests:

- AI output is treated as a request, not execution authority.
- Runtime execution remains disabled.
- Scan execution remains blocked.
- Credential injection remains blocked.
- Customer-target operation remains blocked.
- Generated local artifacts are directed under `private-not-in-git/`.
- Human review and approval gates are represented.
- Evidence linkage and reconstruction are represented.
- Finding review and report promotion gates are represented.
- Delivery authorization is represented.
- Publication hygiene is represented.
- Security disclosure guidance is represented.
- Licensing and commercial-use boundaries are represented.
- Repository governance and release governance are represented.
- Reviewer navigation and front-page explanation are represented.

## What remains intentionally blocked

The following capabilities remain intentionally blocked:

~~~text
runtime execution
network activity
scan execution
credential injection
raw artifact capture
customer-target operation
external network testing
production deployment
managed-service operation
~~~

These blocks are part of the public safety posture.

They should not be described as missing polish. They are intentional boundaries.

## What is not demonstrated

The repository does not currently demonstrate:

- live vulnerability scanning,
- external network testing,
- customer-target testing,
- credential injection against real systems,
- production service deployment,
- multi-tenant SaaS operation,
- managed security service operation,
- legal dependency review completion,
- full software bill of materials completion,
- compliance certification,
- legal approval,
- audit opinion,
- equivalence with any external framework,
- customer-ready managed assessment platform operation.

## Capability boundary table

| Capability | Current status | Interpretation |
| --- | --- | --- |
| Local validation | Demonstrated | Local tests can be run by reviewers |
| GitHub Actions validation | Demonstrated | Public CI scaffold exists and is used |
| Tool Gateway behavior | Demonstrated locally | Reference behavior, not production service |
| Human approval gate | Demonstrated locally | Review boundary example, not legal approval |
| Evidence linkage | Demonstrated locally | Evidence pattern, not audit sufficiency |
| Report promotion | Demonstrated locally | Review pipeline example, not report certification |
| Delivery authorization | Demonstrated locally | Delivery gate example, not customer authorization |
| Runtime execution | Intentionally blocked | Not authorized |
| Live scanning | Intentionally blocked | Not authorized |
| External network testing | Intentionally blocked | Not authorized |
| Credential injection | Intentionally blocked | Not authorized |
| Customer-target operation | Intentionally blocked | Not authorized |
| Production deployment | Not demonstrated | Future work only |
| Managed service operation | Not demonstrated | Requires separate review and agreement |
| Commercial license | Not granted by repository | Requires separate written agreement |

## Reviewer interpretation guidance

Reviewers should interpret this repository as:

- a safety-first reference implementation,
- a control-boundary demonstration,
- a local validation corpus,
- a governance and release-readiness artifact,
- a commercial discussion starting point.

Reviewers should not interpret this repository as:

- a production scanner,
- an autonomous vulnerability scanner,
- permission to scan third-party systems,
- a customer-ready managed assessment platform,
- compliance certification,
- legal approval,
- audit opinion,
- a commercial license grant.

## Evidence artifacts and private outputs

Local tests generate example outputs under `private-not-in-git/`.

Those generated outputs demonstrate local pipeline behavior, but they are not public
customer evidence and they are not proof of production operation.

Expected boundary:

- generated local outputs stay under `private-not-in-git/`,
- private sales materials stay under `private-not-in-git/`,
- customer-specific material is not committed,
- secrets and credentials are not committed,
- sensitive vulnerability details are not committed.

## Public communication boundary

Public communication should use evidence-backed language.

Allowed public language:

- "demonstrates a control-boundary pattern",
- "shows local validation gates",
- "records runtime execution as disabled",
- "documents commercial-use boundaries",
- "provides reviewer navigation",
- "supports commercial licensing discussions."

Avoid unsupported public language:

- "production-ready scanner",
- "autonomous vulnerability scanner",
- "customer-ready managed assessment platform",
- "certified compliant",
- "legally approved",
- "audit-ready",
- "safe by default for customer targets",
- "authorized to scan third-party systems."

## Relationship to front page polish

This checkpoint builds on public front page polish.

Related checkpoint:

- `docs/74-public-front-page-and-repository-landing-polish-checkpoint.md`

The front page polish checkpoint explains how the repository should introduce
itself. This evidence and capability summary explains what the repository can
truthfully claim based on public artifacts and local validation.

## Relationship to public trust navigation

This checkpoint builds on public trust reviewer navigation.

Related checkpoint:

- `docs/73-public-trust-and-reviewer-navigation-checkpoint.md`

Reviewer navigation explains where to look. This summary explains what to conclude
from the visible artifacts.

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

## Compatibility note

Negative and claims-to-avoid sections may name unsafe claims so reviewers know what not to infer. Validation should reject unsafe positive claims, not the mere presence of terms such as `certified compliant` when they appear in unsupported-language or claims-to-avoid guidance.

The validation test normalizes not-demonstrated capability casing before comparison.

This avoids false failures for terms such as `multi-tenant SaaS operation`, where
the section text may be normalized for comparison while the source term preserves
standard capitalization.

## Required local checks

Before tagging v0.5.9, verify:

1. README links to this checkpoint.
2. Summary statement is recorded.
3. Demonstrated capabilities are recorded.
4. Evidence-backed public claims are recorded.
5. Intentionally blocked capabilities are recorded.
6. Non-demonstrated capabilities are recorded.
7. Capability boundary table is recorded.
8. Reviewer interpretation guidance is recorded.
9. Evidence artifacts and private outputs are addressed.
10. Public communication boundary is recorded.
11. Relationships to front page polish and public trust navigation are recorded.
12. Runtime and scanning boundaries remain disabled.
13. Claims to avoid are recorded.
14. `tools/run_all_local_checks.py` includes the public evidence and capability boundary summary test.

## Out of scope

This checkpoint does not:

- enable runtime execution,
- enable scanning,
- create commercial sales material,
- publish pricing,
- create a target customer list,
- create a commercial contract,
- provide legal advice,
- configure GitHub branch protection,
- configure GitHub rulesets,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
