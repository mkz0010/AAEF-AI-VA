# v0.6.22 AAEF Applied Evidence Work Intake and Current-state Review

Version: v0.6.22 candidate  
Status: intake, inventory, and work-ordering; does not authorize runtime execution

## Purpose

This checkpoint responds to an AAEF-side request for AAEF-AI-VA to prioritize a
small, safe, reviewable applied evidence record over building a stronger vulnerability
scanning AI.

This checkpoint is intake, inventory, and work-ordering only.

This checkpoint does not implement required-node checks, generate fixture files,
create runnable configuration, create Docker Compose files, pull images, start
containers, bind ports, authorize Docker execution, authorize runtime execution, run
scanners, inject credentials, authorize customer-target operation, create customer
deliverables, provide certification, provide legal approval, or provide audit opinion.

## AAEF-side request summary

The AAEF-side request asks AAEF-AI-VA to show how AAEF applies to an AI-assisted
vulnerability assessment workflow.

The requested emphasis is not diagnostic strength.

The requested emphasis is an AAEF applied evidence record.

The applied evidence record should show:

- AI does not directly execute diagnostic actions.
- AI may generate `tool_action_request`, but gates decide execution.
- Gate / Tool Gateway / authorization boundary decides whether execution is permitted.
- Permitted, denied, held, and not-executed outcomes are recorded.
- Execution and non-execution evidence are both preserved.
- A reviewer can later trace why execution occurred or did not occur.

Model output is not authority.

AI output is treated as a request, not authority.

## Current repository state captured

Captured before this checkpoint was written:

| Item | Captured value |
| --- | --- |
| Current branch before feature work | `main` |
| Latest tag / version | `v0.6.21` |
| Latest commit | `ba97047 (HEAD -> main, tag: v0.6.21, origin/main) Add v0.6.21 static fixture validator required-node check planning` |
| Working tree status before checkpoint | `clean` |

The expected starting point for this checkpoint is `v0.6.21` at commit `ba97047`.

## Repository inventory summary

Representative current repository inventory:

| Artifact group | Count | Representative files |
| --- | ---: | --- |
| docs | 99 | see list below |
| planning decisions / ADRs | 92 | see list below |
| planning issues | 91 | see list below |
| validator scripts | 4 | see list below |
| test scripts | 77 | see list below |
| Tool Gateway related files | 48 | see list below |
| local-lab / runtime / preflight related files | 41 | see list below |

### Representative docs

- `docs/00-project-charter.md`
- `docs/01-business-plan.md`
- `docs/02-service-concept.md`
- `docs/03-architecture.md`
- `docs/04-aaef-control-model.md`
- `docs/05-ai-data-handling-policy.md`
- `docs/06-credential-ref-model.md`
- `docs/07-tool-gateway-design.md`
- `docs/08-evidence-store-design.md`
- `docs/09-legal-and-nda-considerations.md`
- `docs/10-exit-strategy.md`
- `docs/11-mvp-scope.md`
- `docs/12-credential-ref-flow.md`
- `docs/13-tool-gateway-mvp-design.md`
- `docs/14-mvp-schemas.md`
- `docs/15-tool-gateway-prototype-examples.md`
- `docs/16-tool-gateway-mock-runner.md`
- `docs/17-tool-gateway-negative-tests.md`
- `docs/18-mock-vault-credential-ref-validation.md`
- `docs/19-v0110-stability-checkpoint.md`

### Representative ADRs

- `planning/decisions/ADR-0001-local-first-management.md`
- `planning/decisions/ADR-0002-no-raw-customer-data-in-git.md`
- `planning/decisions/ADR-0003-use-existing-llm-api-for-mvp.md`
- `planning/decisions/ADR-0004-credential-ref-secretless-ai-execution.md`
- `planning/decisions/ADR-0005-define-initial-mvp-scope.md`
- `planning/decisions/ADR-0006-credential-ref-lifecycle.md`
- `planning/decisions/ADR-0007-tool-gateway-as-trusted-control-boundary.md`
- `planning/decisions/ADR-0008-mvp-schema-contracts.md`
- `planning/decisions/ADR-0009-use-example-contract-flows-before-tool-execution-code.md`
- `planning/decisions/ADR-0010-use-standard-library-mock-runner-before-real-tools.md`
- `planning/decisions/ADR-0011-add-fail-closed-negative-tests-for-tool-gateway.md`
- `planning/decisions/ADR-0012-validate-credential-ref-against-vault-metadata.md`
- `planning/decisions/ADR-0013-record-v0110-as-stable-local-checkpoint.md`
- `planning/decisions/ADR-0014-add-tool-gateway-adapter-stubs-before-real-tool-integration.md`

### Representative planning issues

- `planning/issues/0001-define-mvp-scope.md`
- `planning/issues/0002-design-credential-ref-flow.md`
- `planning/issues/0003-draft-ai-use-addendum.md`
- `planning/issues/0004-design-tool-gateway-mvp.md`
- `planning/issues/0005-define-mvp-schema-contracts.md`
- `planning/issues/0006-build-tool-gateway-prototype-scaffold.md`
- `planning/issues/0007-build-tool-gateway-mock-runner.md`
- `planning/issues/0008-add-tool-gateway-negative-tests.md`
- `planning/issues/0009-add-mock-vault-credential-ref-validation.md`
- `planning/issues/0010-fix-tool-gateway-gateway-syntax.md`
- `planning/issues/0011-fix-remaining-python-escaped-docstrings.md`
- `planning/issues/0012-document-v0110-stability-checkpoint.md`
- `planning/issues/0013-add-tool-gateway-adapter-stubs.md`
- `planning/issues/0014-validate-generated-tool-gateway-outputs.md`

## Existing validators and checks

Representative validator scripts:

- `tools/validate_generated_outputs.py`
- `tools/validate_mvp_examples.py`
- `tools/validate_mvp_schemas.py`
- `tools/validate_static_lab_fixtures.py`

Representative test scripts:

- `tools/test_bounded_execution_transition_candidate.py`
- `tools/test_commercial_adoption_preparation_checkpoint.py`
- `tools/test_controlled_executor_policy.py`
- `tools/test_delivery_authorization_gate.py`
- `tools/test_dependency_repository_governance_readiness.py`
- `tools/test_evidence_chain_linkage.py`
- `tools/test_evidence_reconstruction_report.py`
- `tools/test_execution_authorization_gate.py`
- `tools/test_finding_candidate_model.py`
- `tools/test_finding_review_gate.py`
- `tools/test_first_publication_repository_settings_checklist.py`
- `tools/test_github_actions_ci_scaffold.py`
- `tools/test_github_release_publication_checkpoint.py`
- `tools/test_github_repository_ruleset_branch_protection_planning.py`
- `tools/test_human_approval_gate.py`
- `tools/test_licensing_and_commercial_use_boundary.py`
- `tools/test_licensing_trademark_authorship_protection.py`
- `tools/test_lifecycle_integration_checkpoint.py`
- `tools/test_local_execution_plan_review.py`
- `tools/test_local_target_lab_profile.py`
- `tools/test_operator_readiness_review.py`
- `tools/test_preflight_check_implementation.py`
- `tools/test_preflight_evidence_examples.py`
- `tools/test_preflight_evidence_negative_examples.py`

`tools/run_all_local_checks.py` currently registers the local checks through the v0.6.21
static fixture validator required-node check planning test.

Representative tail of local-check registration context:

~~~text
    run([sys.executable, "tools/test_v0610_safe_docker_lab_roadmap_local_target_candidate_planning.py"])
    run([sys.executable, "tools/test_v0611_local_lab_candidate_profile_preflight_evidence_planning.py"])
    run([sys.executable, "tools/test_v0612_non_running_docker_compose_design_review_planning.py"])
    run([sys.executable, "tools/test_v0613_static_compose_design_sketch_network_boundary_review.py"])
    run([sys.executable, "tools/test_v0614_static_lab_scenario_fixture_planning.py"])
    run([sys.executable, "tools/test_v0615_static_fixture_schema_validator_planning.py"])
    run([sys.executable, "tools/test_v0616_static_fixture_schema_draft_negative_test_planning.py"])
    run([sys.executable, "tools/test_v0617_static_fixture_validator_scaffold_planning.py"])
    run([sys.executable, "tools/test_v0618_static_fixture_validator_minimal_scaffold_design.py"])
    run([sys.executable, "tools/test_v0619_static_fixture_validator_implementation_readiness_review.py"])
    run([sys.executable, "tools/test_v0620_static_fixture_validator_read_only_implementation_scaffold.py"])
    run([sys.executable, "tools/test_v0621_static_fixture_validator_required_node_check_planning.py"])
    print("All local checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
~~~

## Existing Tool Gateway and local-lab related files

Representative Tool Gateway related files:

- `prototypes/tool-gateway/README.md`
- `prototypes/tool-gateway/adapters/__init__.py`
- `prototypes/tool-gateway/adapters/base.py`
- `prototypes/tool-gateway/adapters/browser_adapter.py`
- `prototypes/tool-gateway/adapters/command_plan.py`
- `prototypes/tool-gateway/adapters/nmap_adapter.py`
- `prototypes/tool-gateway/adapters/nuclei_adapter.py`
- `prototypes/tool-gateway/adapters/registry.py`
- `prototypes/tool-gateway/adapters/zap_adapter.py`
- `prototypes/tool-gateway/bounded_execution_transition.py`
- `prototypes/tool-gateway/controlled_executor.py`
- `prototypes/tool-gateway/delivery_authorization.py`
- `prototypes/tool-gateway/evidence_chain.py`
- `prototypes/tool-gateway/evidence_reconstruction_report.py`
- `prototypes/tool-gateway/examples/README.md`
- `prototypes/tool-gateway/execution_authorization.py`
- `prototypes/tool-gateway/finding_candidate.py`
- `prototypes/tool-gateway/finding_review.py`
- `prototypes/tool-gateway/gateway.py`
- `prototypes/tool-gateway/human_approval.py`
- `prototypes/tool-gateway/lifecycle_checkpoint.py`
- `prototypes/tool-gateway/local_execution_plan.py`
- `prototypes/tool-gateway/local_target_lab.py`
- `prototypes/tool-gateway/mock_vault/README.md`

Representative local-lab / runtime / preflight related files:

- `docs/39-controlled-local-runtime-readiness.md`
- `docs/40-local-target-lab-profile.md`
- `docs/41-scope-registry-runtime-destination-binding.md`
- `docs/45-runtime-enforcement-design-scaffold.md`
- `docs/47-preflight-validation-scaffold.md`
- `docs/48-runtime-transition-checkpoint.md`
- `docs/49-preflight-check-implementation-scaffold.md`
- `docs/50-preflight-evidence-record-model.md`
- `docs/51-generated-preflight-evidence-record-examples.md`
- `docs/52-preflight-evidence-validation-rules.md`
- `docs/53-negative-preflight-evidence-examples.md`
- `docs/81-v064-local-assessment-lab-decision-record.md`
- `docs/82-v065-documentation-only-local-lab-profile-and-action-taxonomy.md`
- `docs/88-v0611-local-lab-candidate-profile-and-preflight-evidence-planning.md`
- `tools/generate_local_target_lab_profile_demo.py`
- `tools/generate_preflight_check_implementation_demo.py`
- `tools/generate_preflight_evidence_examples_demo.py`
- `tools/generate_preflight_evidence_negative_examples_demo.py`
- `tools/generate_preflight_evidence_record_model_demo.py`
- `tools/generate_preflight_evidence_validation_rules_demo.py`
- `tools/generate_preflight_validation_demo.py`
- `tools/generate_runtime_destination_binding_demo.py`
- `tools/generate_runtime_enforcement_design_demo.py`
- `tools/generate_runtime_readiness_demo.py`

## Public and private boundary

Public repository materials may include:

- safe local lab scope,
- static fixtures,
- sanitized evidence examples,
- mock gateway behavior,
- structural validators,
- reviewer walkthrough,
- non-execution evidence examples,
- AAEF five questions mapping.

Private or excluded materials include:

- third-party target details,
- real exploitation details,
- raw credentials or secrets,
- unauthorized live scanning,
- client or production environment details,
- private patent strategy,
- private commercial negotiation strategy,
- patent-sensitive browser/dynamic-state reconstruction details.

Patent-sensitive browser/dynamic-state reconstruction details remain outside public
repository materials.

If private handling is needed, keep only the existence of private work visible and
manage details under `private-not-in-git/patent-prep/`.

## Safe local lab scope boundary

The applied evidence work must preserve:

- local lab only,
- no third-party target,
- no unauthorized scanning,
- no live exploitation,
- no autonomous execution authority for AI,
- no raw credential exposure to AI,
- no production-readiness claim,
- no implementation conformance claim,
- no certification, compliance, audit, or legal sufficiency claim.

AAEF-AI-VA should be treated as a safe reference implementation / local demonstration
path, not as a production-ready scanner.

## Required applied evidence chain

The next applied evidence package should make this trace reviewable:

1. `tool_action_request`
2. `gate_decision`
3. `dispatch_decision`
4. `execution_result` or `non_execution_result`
5. `evidence_event`
6. `review_summary`

Dispatch and non-dispatch must be separated from gate decision.

Non-execution evidence is first-class evidence.

The purpose is not to prove vulnerability detection accuracy.

The purpose is to show how AI-generated diagnostic intent is controlled and evidenced.

## Required `tool_action_request` posture

A future request record should include at least:

- request id,
- requested tool,
- action type,
- target scope,
- requested parameters,
- purpose / rationale,
- risk level,
- principal / actor context,
- credential reference if applicable,
- generated-by-AI flag,
- timestamp.

The request remains non-authoritative.

## Required `gate_decision` posture

A future gate decision record should include at least:

- decision id,
- linked request id,
- decision result,
- reason,
- policy / rule version,
- trusted inputs used,
- untrusted inputs excluded,
- deciding component,
- timestamp.

Decision results should include permitted, denied, held / requires human approval,
not dispatched, expired if applicable, and revoked if applicable.

## Required dispatch / non-dispatch posture

A future dispatch / non-dispatch record should include at least:

- linked decision id,
- dispatch attempted / not attempted,
- dispatched tool if any,
- blocked reason if not dispatched,
- execution boundary,
- timestamp,
- gateway component.

This record must preserve non-dispatch evidence.

## Minimum scenario set

The minimum scenario set should be:

| Scenario | Purpose |
| --- | --- |
| permitted safe diagnostic | permitted low-risk diagnostic request is dispatched in the safe local-lab model |
| denied out-of-scope request | out-of-scope request is denied |
| human approval required | high-impact or uncertain request is held |
| not-executed / expired | non-execution is evidenced |

The value is control and evidence, not vulnerability-finding performance.

## Reviewer walkthrough requirement

A reviewer walkthrough should explain for each scenario:

- what AI requested,
- what the gate evaluated,
- why the result was permitted, denied, held, or not-executed,
- which evidence artifacts trace the path,
- how the AAEF five questions are answered,
- what is not proven.

JSON and fixtures alone are not enough for external readers.

## AAEF five questions mapping requirement

The applied evidence package should include this mapping:

| AAEF question | AAEF-AI-VA evidence |
| --- | --- |
| Who or what acted? | AI request / gateway / tool identity |
| On whose behalf? | principal context / operator context |
| With what authority? | gate decision / policy version |
| Was the action allowed at the point of execution? | dispatch decision / backend verification |
| What evidence proves what happened? | linked evidence event package |

## Structural validator posture

A structural validator is useful but should not be treated as assurance.

It may check:

- required fields,
- request id linkage,
- decision id linkage,
- scenario type consistency,
- contradictions such as denied with execution result,
- contradictions such as held with dispatch,
- evidence event link integrity,
- fixture completeness.

Validator success must not be described as semantic correctness, evidence sufficiency,
assessment sufficiency, production readiness, audit sufficiency, or legal sufficiency.

## Optimal work ordering from here

The optimal order after this checkpoint is:

| Step | Proposed checkpoint | Purpose |
| --- | --- | --- |
| 1 | v0.6.23 AAEF Applied Evidence Package Design | Define evidence package structure and scenario artifact model |
| 2 | v0.6.24 Applied Evidence Scenario Set Planning | Define the four minimum scenarios in public-safe form |
| 3 | v0.6.25 Static Applied Evidence Fixture Planning | Plan static fixtures for request / gate / dispatch / result / evidence / review |
| 4 | v0.6.26 Reviewer Walkthrough and Five Questions Mapping | Add reader-facing walkthrough and AAEF mapping |
| 5 | v0.6.27 Applied Evidence Structural Validator Planning | Plan structural checks without overclaiming |
| 6 | later | Revisit required-node minimal implementation if it directly supports applied evidence |

The previously natural v0.6.22 required-node minimal implementation should be deferred
until the applied evidence package design is anchored.

The next work should prioritize evidence-package planning before additional validator
implementation.

## Completion signal expected by AAEF side

When the applied evidence work reaches a meaningful checkpoint, the AAEF side should
receive:

1. latest commit / branch / tag state,
2. changed files,
3. local validation result,
4. `tools/run_all_local_checks.py` result,
5. scenarios created,
6. evidence package structure,
7. request to decision to dispatch / non-dispatch to evidence mapping,
8. reviewer walkthrough location,
9. AAEF five questions mapping location,
10. existence-only note for private or patent-sensitive content if any.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
required_node_checks_implemented = false
applied_evidence_package_generated = false
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

## Claims to avoid

Do not claim that this checkpoint provides implemented required-node checks, generated
fixture files, complete fixture schema validation, complete fixture validator
implementation, live evidence, Docker Compose file creation, Docker execution
approval, image pull approval, container startup approval, port binding approval,
production deployment approval, runtime execution readiness, scan authorization,
customer-target authorization, vulnerability detection accuracy, implementation
conformance, compliance certification, legal approval, audit opinion, completed legal
review, completed dependency audit, managed service approval, commercial license
grant, safety guarantee, external framework equivalence, audit sufficiency, or
delivery authorization.

## Out of scope

This checkpoint does not implement required-node checks, implement complete fixture
schemas, implement complete fixture validators, implement negative tests, generate
fixture files, commit sample fixture artifacts, install Docker, run Docker, pull
images, start containers, bind ports, create Docker Compose files, create a runnable
Compose design, build a local lab, select a target for execution, collect live
preflight evidence, satisfy preflight, add dry-run lab execution, enable runtime
execution, enable scanning, add new scanner integrations, create generated sample
evidence artifacts, create generated sample report artifacts, authorize report
delivery, expose private advanced feature details, create private sales material,
publish pricing, create a commercial contract, provide legal advice, authorize
external network testing, authorize credential injection, or authorize customer-target
testing.
