# v0.6.1 Capability Inventory and Maturity Map

Version: v0.6.1 candidate  
Status: capability inventory and maturity mapping; does not authorize runtime execution

## Purpose

This checkpoint inventories current AAEF-AI-VA capabilities before the project
chooses whether to build a local assessment lab, improve evaluation criteria,
harden runtime gates, prepare controlled demos, or plan commercial PoC boundaries.

The goal is to know what already exists, what maturity level it has reached, what
evidence supports that conclusion, and what should happen next.

This checkpoint is inventory and planning only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Maturity model

This checkpoint uses the v0.6.0 maturity model:

| Level | Name | Meaning |
| --- | --- | --- |
| L0 | Concept recorded | A concept or boundary is documented |
| L1 | Static example | Static examples exist |
| L2 | Local validation | Local tests validate behavior or documents |
| L3 | Dry-run behavior | Behavior is simulated without real execution |
| L4 | Local-only controlled behavior | Behavior is constrained to owned localhost/lab scope |
| L5 | Reviewed PoC candidate | Human-reviewed and contract/scope-aware PoC candidate |
| L6 | Commercial deployment candidate | Requires separate commercial, legal, security, and operational review |

Current public claims should remain at or below the supported maturity level.

The project must not imply L5 or L6 readiness while the evidence only supports
L0-L4.

## Current maturity summary

| Area | Current maturity | Summary |
| --- | --- | --- |
| Public repository and release governance | L2 | Documented and locally validated governance checkpoints |
| Licensing and commercial-use boundary | L2 | Public boundary documents and local tests exist |
| Reviewer navigation and FAQ | L2 | Public reviewer paths, FAQ, and objections handling are validated |
| Tool Gateway behavior | L3 | Local scenarios simulate allowed, denied, and human-review-required outcomes |
| Human review and approval gates | L2 | Local validation and generated private outputs exist |
| Evidence linkage and reconstruction | L2 | Evidence chain and reconstruction reports are locally validated |
| Finding and report promotion flow | L2 | Finding review, report promotion, report review, packet review, and delivery gates are locally validated |
| Runtime readiness boundary | L2 | Runtime readiness and transition gates validate that execution remains blocked |
| Preflight scaffolding | L2 | Preflight models, examples, validation rules, and negative examples are locally validated |
| Local target lab profile | L2 | Localhost-only boundary profile is validated, but lab execution is not enabled |
| Controlled local execution | L0-L2 | Planning and blocking gates exist; controlled execution is not enabled |
| Local assessment lab | L0 | Decisioning is planned; the lab is not built |
| Commercial PoC readiness | L0 | Boundary planning exists; no commercial PoC readiness is claimed |
| Production deployment | Not demonstrated | No production deployment capability is claimed |

## Capability inventory

| Capability | Maturity | Supporting artifacts | Current interpretation |
| --- | --- | --- | --- |
| Scope registry | L2 | `tools/test_scope_registry.py` | Local validation of scope registry behavior |
| Tool Gateway runner | L3 | `tools/test_tool_gateway_runner.py` | Simulated allowed, denied, and human-review-required outcomes |
| Tool Gateway adapters | L2 | `tools/test_tool_gateway_adapters.py` | Adapter behavior is locally validated |
| Controlled executor policy | L2 | `tools/test_controlled_executor_policy.py` | Policy behavior is validated without production execution |
| Real execution readiness gate | L2 | `tools/test_real_execution_readiness_gate.py` | Execution readiness remains blocked |
| Operator readiness review | L2 | `tools/test_operator_readiness_review.py` | Operator review output is generated under `private-not-in-git/` |
| Human approval gate | L2 | `tools/test_human_approval_gate.py` | Human approval records and gate results are locally validated |
| Evidence chain linkage | L2 | `tools/test_evidence_chain_linkage.py` | Action/evidence correlation is locally validated |
| Evidence reconstruction report | L2 | `tools/test_evidence_reconstruction_report.py` | Reconstruction reports are locally generated and validated |
| Sanitizer redaction policy | L2 | `tools/test_sanitizer_redaction_policy.py` | Redaction behavior is locally validated |
| Finding candidate model | L2 | `tools/test_finding_candidate_model.py` | Candidate creation remains review-gated |
| Finding review gate | L2 | `tools/test_finding_review_gate.py` | Finding review gates are locally validated |
| Report finding promotion gate | L2 | `tools/test_report_finding_promotion_gate.py` | Promotion from candidate to report finding is locally validated |
| Report review gate | L2 | `tools/test_report_review_gate.py` | Report review gate is locally validated |
| Report packet review gate | L2 | `tools/test_report_packet_review_gate.py` | Packet review gate is locally validated |
| Delivery authorization gate | L2 | `tools/test_delivery_authorization_gate.py` | Delivery authorization is locally validated |
| Lifecycle integration checkpoint | L2 | `tools/test_lifecycle_integration_checkpoint.py` | End-to-end lifecycle checkpoint is locally validated |
| Runtime readiness gate | L2 | `tools/test_runtime_readiness_gate.py` | Runtime detection remains blocked |
| Local target lab profile | L2 | `tools/test_local_target_lab_profile.py` | Localhost-only profile boundary is validated |
| Runtime destination binding | L2 | `tools/test_runtime_destination_binding.py` | Destination binding is recorded while execution remains blocked |
| Bounded execution transition candidate | L2 | `tools/test_bounded_execution_transition_candidate.py` | Transition candidate is recorded while real execution remains blocked |
| Local execution plan review | L2 | `tools/test_local_execution_plan_review.py` | Local execution planning is recorded while execution remains blocked |
| Runtime safety policy | L2 | `tools/test_runtime_safety_policy.py` | Safety policy is recorded while execution remains blocked |
| Runtime enforcement design | L2 | `tools/test_runtime_enforcement_design.py` | Enforcement design is recorded while implementation remains blocked |
| Execution authorization gate scaffold | L2 | `tools/test_execution_authorization_gate.py` | Authorization gate scaffold is validated while execution remains blocked |
| Preflight validation scaffold | L2 | `tools/test_preflight_validation.py` | Preflight validation remains unsatisfied by default |
| Runtime transition checkpoint | L2 | `tools/test_runtime_transition_checkpoint.py` | Preflight implementation readiness is tracked while runtime execution remains blocked |
| Preflight check implementation scaffold | L2 | `tools/test_preflight_check_implementation.py` | Concrete checks are not yet implemented; execution remains blocked |
| Preflight evidence record model | L2 | `tools/test_preflight_evidence_record_model.py` | Evidence records are modeled while live records remain ungenerated |
| Preflight evidence examples | L2 | `tools/test_preflight_evidence_examples.py` | Example records are generated; live evidence remains ungenerated |
| Preflight evidence validation rules | L2 | `tools/test_preflight_evidence_validation_rules.py` | Generated examples are validated; live evidence remains out of scope |
| Negative preflight evidence examples | L2 | `tools/test_preflight_evidence_negative_examples.py` | Negative examples preserve fail-closed behavior |
| Licensing and commercial-use boundary | L2 | `tools/test_licensing_and_commercial_use_boundary.py` | AGPL and commercial-use boundaries are validated |
| Publication hygiene and private artifact exclusion | L2 | `tools/test_publication_hygiene_private_artifact_exclusion.py` | Private artifact boundaries are validated |
| Security policy and vulnerability disclosure | L2 | `tools/test_public_security_policy_vulnerability_disclosure.py` | Security disclosure guidance is validated |
| GitHub Actions CI scaffold | L2 | `tools/test_github_actions_ci_scaffold.py` | CI scaffold is validated |
| README compatibility phrase registry | L2 | `tools/test_readme_compatibility_phrase_registry.py` | Compatibility-sensitive public wording is protected |
| Licensing, trademark, authorship protection | L2 | `tools/test_licensing_trademark_authorship_protection.py` | Authorship, project-name, and commercial-use boundaries are validated |
| Dependency and repository governance readiness | L2 | `tools/test_dependency_repository_governance_readiness.py` | Governance readiness is documented and validated |
| Ruleset and branch protection planning | L2 | `tools/test_github_repository_ruleset_branch_protection_planning.py` | Protection planning exists; settings are not configured |
| Release governance and maintainer operations | L2 | `tools/test_release_governance_maintainer_operations_checklist.py` | Release operations are documented and validated |
| Public trust and reviewer navigation | L2 | `tools/test_public_trust_reviewer_navigation.py` | Reviewer navigation is documented and validated |
| Front page and repository landing polish | L2 | `tools/test_public_front_page_landing_polish.py` | Landing-page expectations are documented and validated |
| Evidence and capability boundary summary | L2 | `tools/test_public_evidence_capability_boundary_summary.py` | Demonstrated and non-demonstrated capabilities are documented |
| Public FAQ and reviewer objections | L2 | `tools/test_public_faq_reviewer_objections.py` | Likely objections are answered and validated |
| v0.6.0 work ordering | L2 | `tools/test_v060_implementation_evaluation_work_ordering.py` | v0.6.x sequencing is documented and validated |

## Capability gaps

The current gaps are:

| Gap | Current maturity | Needed before advancement |
| --- | --- | --- |
| Evaluation criteria and acceptance model | L0 | Define what future capabilities must prove |
| Capability scoring model | L0 | Define scoring dimensions without implying certification |
| Local assessment lab decision record | L0 | Decide whether lab is no-lab, documentation-only, static fixture, dry-run, or localhost-only |
| Allowed and denied action taxonomy | L0-L1 | Record action categories before any local execution expansion |
| Local-only target profile expansion | L2 | Clarify constraints before controlled lab use |
| Preflight concrete checks | L2 | Move from scaffold to concrete local-only checks while keeping execution blocked |
| Runtime enforcement implementation | L2 | Move from design to controlled local enforcement only after gates mature |
| Evidence/report UX improvement | L2 | Improve reviewer readability of generated private outputs |
| Demo scenario walkthrough | L0 | Define safe demo path before demo assets |
| Commercial PoC readiness boundary | L0 | Define paid pilot boundaries without claiming deployment readiness |

## Readiness by future path

| Future path | Readiness today | Reason |
| --- | --- | --- |
| Continue documentation and evaluation planning | Ready | Strong public governance and validation base exists |
| Build evaluation criteria | Ready | Capability inventory gives inputs for evaluation |
| Improve generated evidence UX | Ready | Existing private outputs and review gates can be made clearer |
| Build dry-run demo walkthrough | Conditionally ready | Requires evaluation criteria and demo boundary first |
| Build local assessment lab | Not yet | Requires local lab decision record and safety boundary review |
| Enable controlled local execution | Not yet | Requires concrete preflight checks, allowed/denied taxonomy, and local-only target constraints |
| Prepare commercial PoC | Not yet | Requires capability scoring, scope model, safety review, and commercial agreement boundaries |
| Production deployment | Not ready | Out of scope and not demonstrated |

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.2 Evaluation Criteria and Acceptance Model
~~~

Rationale:

- The capability inventory identifies what exists.
- Evaluation criteria define how future improvements will be judged.
- The local lab decision should be informed by evaluation criteria, not the other way around.
- Evaluation criteria reduce the risk of building a demo that does not prove the right thing.

## Local lab implication

The local assessment lab remains a candidate path, not the default immediate build.

Current recommendation:

~~~text
Do not build a localhost-only controlled lab yet.
First define evaluation criteria and acceptance model.
Then complete safety boundary and non-goal review.
Then create a local assessment lab decision record.
~~~

## Commercial PoC implication

Commercial PoC readiness remains later work.

Before commercial PoC readiness, complete:

- evaluation criteria and acceptance model,
- safety boundary and non-goal review,
- local lab decision record,
- demo scenario and reviewer walkthrough planning,
- evidence and report UX improvement,
- commercial scope and licensing boundary review.

## Public claim boundary

Allowed public language:

- "capability inventory",
- "maturity map",
- "local validation",
- "dry-run behavior where supported",
- "runtime execution remains blocked",
- "local lab remains a decision path",
- "commercial PoC readiness remains future work."

Avoid public language that implies:

- live scanning,
- customer-target authorization,
- production deployment,
- managed service readiness,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- commercial license grant.

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

Before tagging v0.6.1, verify:

1. README links to this checkpoint.
2. Maturity model is recorded.
3. Current maturity summary is recorded.
4. Capability inventory is recorded.
5. Capability gaps are recorded.
6. Readiness by future path is recorded.
7. Recommended next checkpoint is recorded.
8. Local lab implication is recorded.
9. Commercial PoC implication is recorded.
10. Runtime and scanning boundaries remain disabled.
11. Claims to avoid are recorded.
12. `tools/run_all_local_checks.py` includes the v0.6.1 capability inventory test.

## Out of scope

This checkpoint does not:

- build a local lab,
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
