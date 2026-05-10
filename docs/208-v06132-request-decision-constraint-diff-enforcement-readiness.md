# v0.6.132 Request/Decision Constraint-Diff Enforcement Readiness

Status: readiness
Date: 2026-05-10

## Purpose

This checkpoint prepares the request/decision constraint-diff enforcement work item selected in v0.6.131.

This is checkpoint 1 of 3 for a High-risk gate-semantics work item.

This checkpoint prepares request/decision constraint-diff enforcement readiness.

The candidate implementation is deferred to v0.6.133.

The review and decision are deferred to v0.6.134.

This checkpoint does not implement request/decision constraint-diff enforcement.

This checkpoint does not modify constraint-diff behavior.

This checkpoint does not modify runtime behavior.

## Readiness record

~~~text
request_decision_constraint_diff_enforcement_readiness_completed = true
request_decision_constraint_diff_enforcement_readiness_is_high_risk = true
request_decision_constraint_diff_enforcement_readiness_checkpoint_1_of_3 = true
request_decision_constraint_diff_enforcement_candidate_deferred_to_v06133 = true
request_decision_constraint_diff_enforcement_review_decision_deferred_to_v06134 = true
request_decision_constraint_diff_enforcement_readiness_documentation_only = true
request_decision_constraint_diff_enforcement_readiness_identifies_target_discovery = true
request_decision_constraint_diff_enforcement_readiness_identifies_comparison_inputs = true
request_decision_constraint_diff_enforcement_readiness_identifies_diff_categories = true
request_decision_constraint_diff_enforcement_readiness_identifies_fail_closed_boundary = true
request_decision_constraint_diff_enforcement_readiness_identifies_tests_to_add_or_update = true
request_decision_constraint_diff_enforcement_readiness_identifies_non_goals = true
constraint_diff_enforcement_added = false
constraint_diff_behavior_modified = false
constraint_diff_helper_added = false
request_decision_comparison_logic_modified = false
authorization_gate_runtime_behavior_modified = false
candidate_implementation_started = false
review_decision_completed = false
authorization_expiry_current_time_check_work_item_closed = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
authorization_expiry_now_check_added = false
external_discovery_fail_closed_added = false
mock_completed_status_renamed = false
enterprise_review_guide_created = false
technical_due_diligence_summary_created = false
safe_poc_boundary_template_created = false
control_matrix_created = false
reviewer_walkthrough_created = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_checkpoint = v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate
~~~

## Readiness target discovery

The readiness scan looked for repository files that mention request/dispatch, decision/authorization, and scope/constraint/gate concepts.

Potential target files or review starting points:

- `docs/03-architecture.md` — matched terms: authorization, gate, request, scope, tool gateway
- `docs/04-aaef-control-model.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `docs/06-credential-ref-model.md` — matched terms: authorization, gate, request, scope, tool gateway
- `docs/07-tool-gateway-design.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool gateway
- `docs/100-v0623-aaef-applied-evidence-package-design.md` — matched terms: authorization, authorized, decision, diff, dispatch, gate, request, scope, tool_action_request
- `docs/101-v0624-applied-evidence-scenario-set-planning.md` — matched terms: authorization, authorized, decision, diff, dispatch, gate, request, scope, tool_action_request
- `docs/102-v0625-static-applied-evidence-fixture-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/103-v0626-reviewer-walkthrough-and-five-questions-mapping.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool gateway, tool_action_request
- `docs/104-v0627-applied-evidence-structural-validator-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/105-v0628-static-mock-applied-evidence-package-generation-readiness-review.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/106-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/107-v0630-static-mock-applied-evidence-package-review-and-promotion-gate-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/108-v0631-static-mock-applied-evidence-package-private-review-record.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/109-v0632-static-mock-applied-evidence-package-public-sample-promotion-decision-record.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/11-mvp-scope.md` — matched terms: authorization, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/110-v0633-sanitized-public-sample-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/111-v0634-sanitized-public-sample-generation-readiness-review.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool_action_request
- `docs/112-v0635-sanitized-public-sample-generation-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/113-v0636-sanitized-public-sample-publication-review-record.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/114-v0637-sanitized-public-sample-close-readiness-review.md` — matched terms: authorization, authorized, gate, request, scope, tool_action_request
- `docs/115-v0638-public-example-structural-validation-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/116-v0639-public-example-structural-validator-implementation-readiness-review.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/117-v0640-public-example-structural-validator-implementation-candidate.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/118-v0641-public-example-structural-validator-review-and-close-readiness.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/119-v0642-aaef-applied-implementation-handback-summary.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `docs/12-credential-ref-flow.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/120-v0643-applied-implementation-handback-review-and-next-direction.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/121-v0644-public-validator-negative-fixture-planning.md` — matched terms: authorization, authorized, dispatch, gate, request, scope
- `docs/122-v0645-public-validator-negative-fixture-implementation-readiness-review.md` — matched terms: authorization, authorized, constraint, constraints, decision, dispatch, gate, request, scope
- `docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md` — matched terms: authorization, authorized, decision, request, scope
- `docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/13-tool-gateway-mvp-design.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, gate, request, scope, tool gateway, tool_action_request
- `docs/133-v0656-public-validator-behavior-hardening-readiness-review.md` — matched terms: authorized, decision, dispatch, gate, request, scope
- `docs/134-v0657-public-validator-behavior-hardening-scope-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/135-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/139-v0662-public-validator-hardening-maintenance-cleanup-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/14-mvp-schemas.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/144-v0667-applied-evidence-current-state-review.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/145-v0668-applied-evidence-gap-prioritization-review.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/146-v0669-applied-evidence-reviewer-current-state-summary-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/147-v0670-applied-evidence-reviewer-current-state-summary-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/149-v0672-applied-evidence-next-gap-selection-review.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/15-tool-gateway-prototype-examples.md` — matched terms: authorization, authorized, decision, gate, request, tool gateway
- `docs/150-v0673-public-sample-five-questions-clarity-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/151-v0674-public-sample-five-questions-clarity-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/155-v0679-public-sample-relationship-to-validator-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/158-v0682-evidence-interface-handback-readiness-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/159-v0683-evidence-interface-handback-readiness-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/160-v0684-evidence-interface-handback-readiness-review-close-readiness.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/161-v0685-applied-evidence-handback-preparation-decision.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/162-v0686-narrow-public-safe-aaef-main-handback-preparation-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, dispatch, gate, request, scope
- `docs/163-v0687-narrow-public-safe-aaef-main-handback-preparation-candidate.md` — matched terms: authorization, authorized, constraint, constraints, decision, dispatch, gate, request, scope
- `docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/165-v0689-applied-evidence-handback-drafting-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, dispatch, gate, request, scope
- `docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/168-v0692-narrow-public-safe-aaef-main-handback-drafting-candidate-review-close-readiness.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/169-v0693-applied-evidence-handback-material-preparation-decision.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `docs/17-tool-gateway-negative-tests.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `docs/170-v0694-narrow-public-safe-aaef-main-handback-material-preparation-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/171-v0695-narrow-public-safe-aaef-main-handback-material-preparation-candidate.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/172-v0696-narrow-public-safe-aaef-main-handback-material-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/173-v0697-applied-evidence-handback-material-drafting-or-submission-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/174-v0698-narrow-public-safe-aaef-main-handback-text-drafting-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/175-v0699-narrow-public-safe-aaef-main-handback-text-drafting-candidate.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/176-v06100-narrow-public-safe-aaef-main-handback-text-drafting-candidate-review-close-readiness.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/177-v06101-applied-evidence-handback-text-submission-or-pause-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, tool gateway
- `docs/178-v06102-narrow-public-safe-aaef-main-handback-final-text-preparation-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, tool gateway
- `docs/179-v06103-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/18-mock-vault-credential-ref-validation.md` — matched terms: authorization, decision, diff, gate, request, scope, tool gateway
- `docs/180-v06104-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/181-v06105-applied-evidence-handback-submittable-text-or-pause-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, tool gateway
- `docs/182-v06106-narrow-public-safe-aaef-main-handback-submittable-text-preparation-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/184-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/185-v06109-applied-evidence-handback-submission-or-pause-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/186-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/187-v06111-narrow-public-safe-aaef-main-handback-workflow-selection-or-exact-text-preparation-decision.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, scope
- `docs/188-v06112-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-planning.md` — matched terms: authorization, authorized, constraint, constraints, decision, diff, dispatch, gate, request, tool gateway
- `docs/189-v06113-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/190-v06114-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope, tool gateway
- `docs/191-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope
- `docs/192-v06116-narrow-public-safe-aaef-main-handback-human-submission-checklist-preparation.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, tool gateway
- `docs/193-v06117-narrow-public-safe-aaef-main-handback-human-submission-checklist-review-close-readiness.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `docs/194-v06118-narrow-public-safe-aaef-main-handback-human-maintainer-final-submission-decision-or-pause.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope
- `docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `docs/196-v06120-checkpoint-granularity-policy-decision-record.md` — matched terms: authorization, authorized, decision, gate, request
- `docs/197-v06121-next-direction-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `docs/198-v06122-readme-current-latest-baseline-clarity-candidate.md` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `docs/199-v06123-readme-current-latest-baseline-clarity-review-and-decision.md` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `docs/201-v06125-security-reporting-channel-consistency-candidate.md` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `docs/202-v06126-security-reporting-channel-consistency-review-and-decision.md` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request, scope
- `docs/204-v06128-authorization-expiry-current-time-check-readiness.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request, scope
- `docs/205-v06129-authorization-expiry-current-time-check-candidate.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `docs/207-v06131-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope
- `docs/22-internal-adapter-artifact-policy.md` — matched terms: authorization, decision, gate, request, tool gateway, tool_action_request
- `docs/23-zap-adapter-command-plan.md` — matched terms: authorization, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/24-controlled-executor-policy.md` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/26-real-execution-readiness-gate.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `docs/29-evidence-chain-review-linkage.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/30-evidence-reconstruction-report.md` — matched terms: authorized, decision, gate, request, tool gateway
- `docs/31-sanitizer-redaction-policy.md` — matched terms: authorization, gate, request
- `docs/37-delivery-authorization-gate.md` — matched terms: authorization, authorized, decision, dispatch, gate, scope
- `docs/38-lifecycle-integration-checkpoint.md` — matched terms: authorization, decision, dispatch, gate, request, scope, tool gateway, tool_action_request
- `docs/54-licensing-and-commercial-use-boundary.md` — matched terms: authorized, decision, gate, request
- `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md` — matched terms: authorization, authorized, request, scope
- `docs/58-first-publication-repository-settings-checklist.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/60-github-actions-ci-scaffold.md` — matched terms: authorization, authorized, constraint, constraints, dispatch, request, scope
- `docs/61-readme-public-english-wording-cleanup.md` — matched terms: authorization, authorized, gate, request, scope, tool gateway
- `docs/62-public-facing-repository-metadata-and-announcement-pack.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway
- `docs/63-public-repository-launch-checkpoint.md` — matched terms: authorization, authorized, dispatch, scope
- `docs/64-public-release-notes-and-launch-announcement-package.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway
- `docs/65-github-release-publication-checkpoint.md` — matched terms: authorization, authorized, gate, request, scope, tool gateway
- `docs/66-commercial-adoption-preparation-checkpoint.md` — matched terms: authorization, authorized, diff, gate, request, scope, tool gateway
- `docs/67-readme-public-baseline-and-commercial-entrypoint-cleanup.md` — matched terms: authorization, authorized, gate, request, scope, tool gateway
- `docs/68-readme-compatibility-phrase-registry-and-test-design-hardening.md` — matched terms: authorization, authorized, gate, request, scope, tool gateway
- `docs/69-licensing-trademark-authorship-protection-checkpoint.md` — matched terms: authorization, authorized, request, scope
- `docs/70-dependency-and-repository-governance-readiness-checkpoint.md` — matched terms: authorization, authorized, request, scope
- `docs/71-github-repository-ruleset-and-branch-protection-planning-checkpoint.md` — matched terms: authorization, authorized, request, scope
- `docs/72-release-governance-and-maintainer-operations-checklist.md` — matched terms: authorization, authorized, diff, gate, request, scope
- `docs/74-public-front-page-and-repository-landing-polish-checkpoint.md` — matched terms: authorization, authorized, diff, gate, request, scope, tool gateway
- `docs/75-public-evidence-and-capability-boundary-summary.md` — matched terms: authorization, authorized, gate, request, scope, tool gateway
- `docs/76-public-faq-and-reviewer-objections-handling.md` — matched terms: authorization, authorized, decision, diff, gate, request, scope, tool gateway
- `docs/77-v060-implementation-and-evaluation-work-ordering.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/79-v062-evaluation-criteria-and-acceptance-model.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/80-v063-safety-boundary-and-non-goal-review.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool gateway
- `docs/82-v065-documentation-only-local-lab-profile-and-action-taxonomy.md` — matched terms: authorization, authorized, decision, gate, request, scope
- `docs/83-v066-ai-request-decision-boundary-and-tool-selection-criteria.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/84-v067-observation-normalization-and-diagnostic-fidelity-risk-review.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool_action_request
- `docs/85-v068-demo-scenario-and-reviewer-walkthrough-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/86-v069-evidence-reconstruction-and-sample-report-demonstration-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/87-v0610-safe-docker-lab-roadmap-and-local-target-candidate-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway, tool_action_request
- `docs/88-v0611-local-lab-candidate-profile-and-preflight-evidence-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/89-v0612-non-running-docker-compose-design-review-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/90-v0613-static-compose-design-sketch-and-network-boundary-review.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/91-v0614-static-lab-scenario-fixture-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/92-v0615-static-fixture-schema-and-validator-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/93-v0616-static-fixture-schema-draft-and-negative-test-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/94-v0617-static-fixture-validator-scaffold-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/95-v0618-static-fixture-validator-minimal-scaffold-design.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/96-v0619-static-fixture-validator-implementation-readiness-review.md` — matched terms: authorization, authorized, gate, request, scope, tool_action_request
- `docs/97-v0620-static-fixture-validator-read-only-implementation-scaffold.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/98-v0621-static-fixture-validator-required-node-check-planning.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `docs/99-v0622-aaef-applied-evidence-work-intake-and-current-state-review.md` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool gateway, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/boundary-flag-violation/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/negative_fixture_metadata.example.json` — matched terms: authorization, authorized, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/broken-linkage/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/forbidden-text-leakage/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/hygiene-not-passed/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/malformed-json/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-five-questions-mapping/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-non-proof-statement/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-package-artifact/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-artifact/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/missing-scenario-directory/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/negative_fixture_index.example.json` — matched terms: authorized, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/non-example-name/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/overclaim-language/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/negative_fixture_metadata.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/public-validator-negative-fixtures/scenario-posture-contradiction/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/sanitized-static-mock/aaef_five_questions_mapping.example.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `examples/applied-evidence/sanitized-static-mock/package_manifest.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/sanitized-static-mock/publication_review_record.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/reviewer_walkthrough.example.md` — matched terms: decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/evidence_event.example.json` — matched terms: authorization, decision, dispatch, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/non_proof_statement.example.md` — matched terms: authorization, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/denied-out-of-scope-request/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/human-approval-required/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/sanitized-static-mock/scenarios/human-approval-required/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/human-approval-required/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/sanitized-static-mock/scenarios/human-approval-required/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/sanitized-static-mock/scenarios/human-approval-required/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/not-executed-expired/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/sanitized-static-mock/scenarios/not-executed-expired/gate_decision.example.json` — matched terms: authorization, decision, dispatch, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/not-executed-expired/non_execution_result.example.json` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `examples/applied-evidence/sanitized-static-mock/scenarios/not-executed-expired/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/sanitized-static-mock/scenarios/not-executed-expired/tool_action_request.example.json` — matched terms: authorization, authorized, dispatch, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/permitted-safe-diagnostic/dispatch_decision.example.json` — matched terms: authorization, authorized, decision, dispatch, gate
- `examples/applied-evidence/sanitized-static-mock/scenarios/permitted-safe-diagnostic/gate_decision.example.json` — matched terms: authorization, decision, gate, request, scope
- `examples/applied-evidence/sanitized-static-mock/scenarios/permitted-safe-diagnostic/review_summary.example.md` — matched terms: authorization, decision, dispatch, gate, request
- `examples/applied-evidence/sanitized-static-mock/scenarios/permitted-safe-diagnostic/tool_action_request.example.json` — matched terms: authorization, authorized, request, scope
- `planning/decisions/ADR-0006-credential-ref-lifecycle.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/decisions/ADR-0007-tool-gateway-as-trusted-control-boundary.md` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway
- `planning/decisions/ADR-0008-mvp-schema-contracts.md` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `planning/decisions/ADR-0009-use-example-contract-flows-before-tool-execution-code.md` — matched terms: authorization, decision, gate, request, tool gateway
- `planning/decisions/ADR-0010-use-standard-library-mock-runner-before-real-tools.md` — matched terms: authorization, decision, gate, request, tool gateway
- `planning/decisions/ADR-0012-validate-credential-ref-against-vault-metadata.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/decisions/ADR-0014-add-tool-gateway-adapter-stubs-before-real-tool-integration.md` — matched terms: authorization, decision, gate, request, tool gateway
- `planning/decisions/ADR-0019-add-scope-registry-target-alias-resolution.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/decisions/ADR-0022-add-human-approval-record-and-gate.md` — matched terms: decision, gate, request, scope
- `planning/decisions/ADR-0023-add-evidence-chain-review-decision-linkage.md` — matched terms: authorization, decision, gate, request, scope
- `planning/decisions/ADR-0024-add-evidence-reconstruction-report.md` — matched terms: authorization, decision, gate, request
- `planning/decisions/ADR-0031-add-delivery-authorization-gate.md` — matched terms: authorization, authorized, decision, dispatch, gate
- `planning/decisions/ADR-0032-add-lifecycle-integration-checkpoint.md` — matched terms: authorization, decision, dispatch, gate, scope, tool gateway
- `planning/decisions/ADR-0048-adopt-agpl-commercial-boundary.md` — matched terms: authorization, decision, gate, request
- `planning/decisions/ADR-0055-clean-up-readme-public-english-wording.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/decisions/ADR-0066-add-release-governance-maintainer-operations-checklist.md` — matched terms: decision, request, scope
- `planning/decisions/ADR-0077-add-v066-ai-request-decision-boundary-tool-selection-criteria.md` — matched terms: decision, gate, request
- `planning/decisions/ADR-0078-add-v067-observation-normalization-diagnostic-fidelity-risk-review.md` — matched terms: decision, gate, request, tool_action_request
- `planning/decisions/ADR-0079-add-v068-demo-scenario-reviewer-walkthrough-planning.md` — matched terms: decision, gate, request
- `planning/decisions/ADR-0080-add-v069-evidence-reconstruction-sample-report-demonstration-planning.md` — matched terms: decision, gate, request, scope
- `planning/decisions/ADR-0085-add-v0614-static-lab-scenario-fixture-planning.md` — matched terms: decision, gate, request
- `planning/decisions/ADR-0086-add-v0615-static-fixture-schema-validator-planning.md` — matched terms: decision, gate, request, scope
- `planning/decisions/ADR-0087-add-v0616-static-fixture-schema-draft-negative-test-planning.md` — matched terms: decision, gate, request, scope
- `planning/decisions/ADR-0093-add-v0622-aaef-applied-evidence-work-intake-current-state-review.md` — matched terms: decision, request, scope
- `planning/decisions/ADR-0094-add-v0623-aaef-applied-evidence-package-design.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `planning/decisions/ADR-0095-add-v0624-applied-evidence-scenario-set-planning.md` — matched terms: decision, request, scope
- `planning/decisions/ADR-0100-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` — matched terms: decision, dispatch, gate, request
- `planning/decisions/ADR-0113-add-v0642-aaef-applied-implementation-handback-summary.md` — matched terms: decision, dispatch, gate, request, scope
- `planning/decisions/ADR-0169-add-v0699-narrow-public-safe-aaef-main-handback-text-drafting-candidate.md` — matched terms: decision, request, scope
- `planning/decisions/ADR-0177-add-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md` — matched terms: decision, request, scope
- `planning/decisions/ADR-0180-add-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md` — matched terms: decision, gate, request
- `planning/decisions/ADR-0182-add-v06112-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-planning.md` — matched terms: constraint, constraints, decision, gate, request
- `planning/decisions/ADR-0201-add-v06131-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, constraint, decision, diff, gate, request
- `planning/issues/0002-design-credential-ref-flow.md` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `planning/issues/0004-design-tool-gateway-mvp.md` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `planning/issues/0005-define-mvp-schema-contracts.md` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `planning/issues/0006-build-tool-gateway-prototype-scaffold.md` — matched terms: authorization, decision, dispatch, gate, tool gateway
- `planning/issues/0007-build-tool-gateway-mock-runner.md` — matched terms: authorization, decision, gate, request, tool gateway, tool_action_request
- `planning/issues/0008-add-tool-gateway-negative-tests.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/issues/0009-add-mock-vault-credential-ref-validation.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `planning/issues/0022-add-evidence-chain-review-linkage.md` — matched terms: decision, gate, request, scope
- `planning/issues/0030-add-delivery-authorization-gate.md` — matched terms: authorization, authorized, decision, dispatch, gate, scope
- `planning/issues/0031-add-lifecycle-integration-checkpoint.md` — matched terms: authorization, decision, dispatch, gate
- `planning/issues/0076-add-v066-ai-request-decision-boundary-tool-selection-criteria.md` — matched terms: decision, gate, request
- `planning/issues/0084-add-v0614-static-lab-scenario-fixture-planning.md` — matched terms: authorization, decision, gate, request
- `planning/issues/0092-add-v0622-aaef-applied-evidence-work-intake-current-state-review.md` — matched terms: authorization, decision, request, scope
- `planning/issues/0093-add-v0623-aaef-applied-evidence-package-design.md` — matched terms: decision, dispatch, gate, request, tool_action_request
- `planning/issues/0094-add-v0624-applied-evidence-scenario-set-planning.md` — matched terms: decision, request, scope
- `planning/issues/0099-add-v0629-static-mock-applied-evidence-package-private-generation-candidate.md` — matched terms: decision, dispatch, gate, request
- `planning/issues/0112-add-v0642-aaef-applied-implementation-handback-summary.md` — matched terms: decision, dispatch, gate, request, scope
- `planning/issues/0200-add-v06131-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, constraint, decision, diff, request
- `prototypes/tool-gateway/README.md` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `prototypes/tool-gateway/adapters/base.py` — matched terms: decision, request, scope
- `prototypes/tool-gateway/adapters/zap_adapter.py` — matched terms: authorized, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `prototypes/tool-gateway/delivery_authorization.py` — matched terms: authorization, authorized, decision, dispatch, gate, scope
- `prototypes/tool-gateway/evidence_chain.py` — matched terms: authorization, decision, gate, request, scope, tool_action_request
- `prototypes/tool-gateway/evidence_reconstruction_report.py` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `prototypes/tool-gateway/examples/README.md` — matched terms: authorized, gate, request, tool gateway
- `prototypes/tool-gateway/examples/allowed-action.authorization-decision.json` — matched terms: authorization, constraint, constraints, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/allowed-action.evidence-record.json` — matched terms: authorization, decision, gate, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/allowed-action.tool-execution-result.json` — matched terms: authorization, decision, gate, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/denied-action.authorization-decision.json` — matched terms: authorization, constraint, constraints, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/denied-action.evidence-record.json` — matched terms: authorization, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/denied-action.tool-execution-result.json` — matched terms: authorization, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/human-approval-required.authorization-decision.json` — matched terms: authorization, constraint, constraints, decision, gate, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/human-approval-required.evidence-record.json` — matched terms: authorization, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/examples/human-approval-required.tool-execution-result.json` — matched terms: authorization, decision, request, scope, tool_action_request
- `prototypes/tool-gateway/finding_review.py` — matched terms: authorization, decision, gate, request, scope
- `prototypes/tool-gateway/gateway.py` — matched terms: authorization, decision, gate, request, scope, tool gateway, tool_action_request
- `prototypes/tool-gateway/human_approval.py` — matched terms: decision, gate, request, scope
- `prototypes/tool-gateway/lifecycle_checkpoint.py` — matched terms: authorization, decision, dispatch, gate, scope, tool gateway
- `prototypes/tool-gateway/operator_readiness_review.py` — matched terms: decision, request, scope
- `prototypes/tool-gateway/policy.py` — matched terms: authorization, constraint, constraints, decision, gate, request, scope, tool gateway, tool_action_request
- `prototypes/tool-gateway/preflight_check_implementation.py` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope
- `prototypes/tool-gateway/preflight_validation.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `prototypes/tool-gateway/runner.py` — matched terms: authorization, decision, gate, request, tool gateway
- `tools/generate_delivery_authorization_demo.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `tools/generate_evidence_chain_review.py` — matched terms: authorization, decision, gate, request, tool_action_request
- `tools/generate_evidence_reconstruction_report.py` — matched terms: authorization, decision, gate, request, tool_action_request
- `tools/generate_finding_candidate_demo.py` — matched terms: authorization, gate, request, scope
- `tools/generate_finding_review_demo.py` — matched terms: authorization, decision, gate, request, scope
- `tools/generate_human_approval_record.py` — matched terms: authorization, decision, gate, request
- `tools/generate_lifecycle_checkpoint.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `tools/generate_operator_readiness_review.py` — matched terms: authorization, decision, gate, request
- `tools/generate_report_finding_promotion_demo.py` — matched terms: authorization, decision, gate, request, scope
- `tools/generate_report_packet_review_demo.py` — matched terms: authorization, decision, gate, request, scope
- `tools/generate_report_review_demo.py` — matched terms: authorization, decision, gate, request, scope
- `tools/generate_sanitized_artifact_demo.py` — matched terms: authorization, gate, request
- `tools/generate_sanitized_public_sample.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/generate_sanitized_public_sample_publication_review_record.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/generate_static_mock_applied_evidence_package.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool gateway, tool_action_request
- `tools/generate_static_mock_applied_evidence_private_review_record.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/run_all_local_checks.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_controlled_executor_policy.py` — matched terms: authorization, constraint, constraints, decision, gate, request, scope
- `tools/test_delivery_authorization_gate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_evidence_chain_linkage.py` — matched terms: authorization, decision, gate, request, tool_action_request
- `tools/test_evidence_reconstruction_report.py` — matched terms: authorization, decision, gate, request, tool_action_request
- `tools/test_finding_candidate_model.py` — matched terms: authorization, gate, request, scope
- `tools/test_finding_review_gate.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_github_repository_ruleset_branch_protection_planning.py` — matched terms: authorization, authorized, decision, request, scope
- `tools/test_human_approval_gate.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_operator_readiness_review.py` — matched terms: authorization, decision, gate, request
- `tools/test_public_evidence_capability_boundary_summary.py` — matched terms: authorization, authorized, decision, gate, request
- `tools/test_public_security_policy_vulnerability_disclosure.py` — matched terms: authorized, decision, request, scope
- `tools/test_readme_public_english_wording.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway
- `tools/test_real_execution_readiness_gate.py` — matched terms: authorization, decision, gate, request
- `tools/test_release_governance_maintainer_operations_checklist.py` — matched terms: authorization, authorized, decision, request, scope
- `tools/test_report_finding_promotion_gate.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_report_packet_review_gate.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_report_review_gate.py` — matched terms: authorization, decision, gate, request, scope
- `tools/test_sanitizer_redaction_policy.py` — matched terms: authorization, gate, request
- `tools/test_tool_gateway_adapters.py` — matched terms: authorization, decision, gate, request, scope, tool gateway
- `tools/test_tool_gateway_runner.py` — matched terms: authorization, constraint, constraints, decision, gate, request, scope, tool gateway
- `tools/test_v06100_narrow_public_safe_aaef_main_handback_text_drafting_candidate_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request, scope
- `tools/test_v06101_applied_evidence_handback_text_submission_or_pause_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06102_narrow_public_safe_aaef_main_handback_final_text_preparation_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06103_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `tools/test_v06104_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request, scope
- `tools/test_v06105_applied_evidence_handback_submittable_text_or_pause_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06106_narrow_public_safe_aaef_main_handback_submittable_text_preparation_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06107_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `tools/test_v06108_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope
- `tools/test_v06109_applied_evidence_handback_submission_or_pause_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06110_narrow_public_safe_aaef_main_handback_submission_workflow_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06111_narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06112_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06113_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `tools/test_v06114_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request
- `tools/test_v06115_narrow_public_safe_aaef_main_handback_exact_issue_submission_or_pause_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06116_narrow_public_safe_aaef_main_handback_human_submission_checklist_preparation.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06117_narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06118_narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06119_narrow_public_safe_aaef_main_handback_pause_and_current_state_closeout_review.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06121_next_direction_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v06122_readme_current_latest_baseline_clarity_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v06123_readme_current_latest_baseline_clarity_review_and_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v06124_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v06125_security_reporting_channel_consistency_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `tools/test_v06126_security_reporting_channel_consistency_review_and_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, request, scope
- `tools/test_v06127_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v06128_authorization_expiry_current_time_check_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06129_authorization_expiry_current_time_check_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06130_authorization_expiry_current_time_check_review_and_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v06131_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, constraint, decision, diff, request
- `tools/test_v0614_static_lab_scenario_fixture_planning.py` — matched terms: authorization, authorized, decision, gate, request
- `tools/test_v0615_static_fixture_schema_validator_planning.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `tools/test_v0616_static_fixture_schema_draft_negative_test_planning.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `tools/test_v0621_static_fixture_validator_required_node_check_planning.py` — matched terms: authorization, authorized, decision, gate, request
- `tools/test_v0622_aaef_applied_evidence_work_intake_current_state_review.py` — matched terms: authorized, decision, dispatch, gate, request, scope, tool gateway, tool_action_request
- `tools/test_v0623_aaef_applied_evidence_package_design.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0624_applied_evidence_scenario_set_planning.py` — matched terms: authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0625_static_applied_evidence_fixture_planning.py` — matched terms: authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0626_reviewer_walkthrough_five_questions_mapping.py` — matched terms: authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0627_applied_evidence_structural_validator_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, tool_action_request
- `tools/test_v0628_static_mock_applied_evidence_generation_readiness_review.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, tool_action_request
- `tools/test_v0629_static_mock_applied_evidence_package_private_generation_candidate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0631_static_mock_applied_evidence_private_review_record.py` — matched terms: authorization, authorized, decision, gate, request
- `tools/test_v0633_sanitized_public_sample_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0634_sanitized_public_sample_generation_readiness_review.py` — matched terms: authorized, constraint, constraints, decision, diff, dispatch, gate, request, tool_action_request
- `tools/test_v0635_sanitized_public_sample_generation_candidate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v0638_public_example_structural_validation_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request
- `tools/test_v063_safety_boundary_non_goal_review.py` — matched terms: authorization, authorized, constraint, constraints, decision, gate, request, scope
- `tools/test_v0640_public_example_structural_validator_implementation_candidate.py` — matched terms: authorized, decision, request, scope
- `tools/test_v0642_aaef_applied_implementation_handback_summary.py` — matched terms: authorized, decision, dispatch, gate, request, scope
- `tools/test_v0643_applied_implementation_handback_review_next_direction.py` — matched terms: authorized, decision, request, scope
- `tools/test_v065_documentation_only_local_lab_profile_action_taxonomy.py` — matched terms: authorization, authorized, decision, request, scope
- `tools/test_v066_ai_request_decision_boundary_tool_selection_criteria.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool gateway, tool_action_request
- `tools/test_v0673_public_sample_five_questions_clarity_planning.py` — matched terms: authorization, authorized, decision, request, scope
- `tools/test_v0674_public_sample_five_questions_clarity_candidate.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `tools/test_v0675_public_sample_five_questions_clarity_review_close_readiness.py` — matched terms: authorization, authorized, decision, gate, request, scope
- `tools/test_v067_observation_normalization_diagnostic_fidelity_risk_review.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `tools/test_v0682_evidence_interface_handback_readiness_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0683_evidence_interface_handback_readiness_candidate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0684_evidence_interface_handback_readiness_review_close_readiness.py` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `tools/test_v0685_applied_evidence_handback_preparation_decision.py` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `tools/test_v0686_narrow_public_safe_aaef_main_handback_preparation_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0687_narrow_public_safe_aaef_main_handback_preparation_candidate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0688_narrow_public_safe_aaef_main_handback_preparation_review_close_readiness.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0689_applied_evidence_handback_drafting_decision.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v068_demo_scenario_reviewer_walkthrough_planning.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `tools/test_v0690_narrow_public_safe_aaef_main_handback_drafting_planning.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0691_narrow_public_safe_aaef_main_handback_drafting_candidate.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0692_narrow_public_safe_aaef_main_handback_drafting_candidate_review_close_readiness.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope
- `tools/test_v0693_applied_evidence_handback_material_preparation_decision.py` — matched terms: authorization, authorized, decision, dispatch, gate, request
- `tools/test_v0694_narrow_public_safe_aaef_main_handback_material_preparation_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, tool gateway
- `tools/test_v0695_narrow_public_safe_aaef_main_handback_material_preparation_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope, tool gateway
- `tools/test_v0696_narrow_public_safe_aaef_main_handback_material_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope, tool gateway
- `tools/test_v0697_applied_evidence_handback_material_drafting_or_submission_decision.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v0698_narrow_public_safe_aaef_main_handback_text_drafting_planning.py` — matched terms: authorization, authorized, constraint, decision, diff, gate, request
- `tools/test_v0699_narrow_public_safe_aaef_main_handback_text_drafting_candidate.py` — matched terms: authorization, authorized, constraint, decision, diff, dispatch, gate, request, scope
- `tools/test_v069_evidence_reconstruction_sample_report_demonstration_planning.py` — matched terms: authorization, authorized, decision, gate, request, scope, tool_action_request
- `tools/validate_mvp_examples.py` — matched terms: authorization, decision, gate, request
- `tools/validate_public_example_structure.py` — matched terms: authorization, authorized, decision, dispatch, gate, request, scope, tool_action_request

This discovery is advisory only. It does not prove that these are the only files that matter, and it does not authorize implementation in this checkpoint.

## Comparison inputs

The v0.6.133 candidate should compare only evidence-safe, gate-relevant request and authorization decision fields.

Candidate comparison inputs should include, where present:

| Input area | Expected comparison target |
| --- | --- |
| requested tool/action | authorized tool/action |
| requested target or destination binding | authorized target or destination binding |
| requested target mode | authorized target mode |
| requested scope identifier | authorized scope identifier |
| requested credential reference | authorized credential reference or allowed credential reference |
| requested execution mode | authorized execution mode |
| requested external discovery flag | authorized external discovery allowance |
| requested time/expiry boundary | authorization validity result |
| requested delivery/reporting action | authorized delivery/reporting action |

The candidate should not compare raw secrets, raw credentials, private customer material, scanner output, or private artifacts.

## Expected candidate behavior

The v0.6.133 candidate should evaluate whether a dispatched request materially differs from the authorization decision that is supposed to permit it.

Expected behavior:

* If request fields match the authorization decision constraints, the gate may continue existing checks.
* If a request changes tool/action beyond the authorized decision, the gate should fail closed.
* If a request changes target, destination, target mode, or scope beyond the authorized decision, the gate should fail closed.
* If a request adds external discovery when the decision did not authorize it, the gate should fail closed.
* If a request changes credential reference beyond the authorized decision, the gate should fail closed.
* If a request changes execution mode beyond the authorized decision, the gate should fail closed.
* If comparison inputs are missing, malformed, or ambiguous where required, the gate should fail closed.
* The comparison result should be evidence-safe and reviewable.

## Diff categories

The v0.6.133 candidate should classify differences into explicit categories such as:

~~~text
tool_action_mismatch
target_mismatch
destination_binding_mismatch
target_mode_mismatch
scope_mismatch
credential_ref_mismatch
execution_mode_mismatch
external_discovery_escalation
delivery_action_mismatch
missing_required_request_field
missing_required_decision_field
malformed_request_constraints
malformed_decision_constraints
ambiguous_constraint_comparison
~~~

The category names can be refined during implementation, but the candidate should keep reviewer-readable reasons.

## Fail-closed boundary

The fail-closed boundary for this work item is:

~~~text
request_outside_authorized_tool_action -> blocked / not authorized
request_outside_authorized_target -> blocked / not authorized
request_outside_authorized_scope -> blocked / not authorized
request_outside_authorized_credential_ref -> blocked / not authorized
request_outside_authorized_execution_mode -> blocked / not authorized
request_escalates_external_discovery -> blocked / not authorized
missing_required_request_constraint -> blocked / not authorized
missing_required_decision_constraint -> blocked / not authorized
malformed_constraint_inputs -> blocked / not authorized
ambiguous_constraint_comparison -> blocked / not authorized
~~~

The candidate should not introduce permissive fallback behavior for ambiguous or missing required comparison inputs.

## Expected tests to add or update

The v0.6.133 candidate should add or update tests for at least these cases:

| Case | Expected result |
| --- | --- |
| exact request/decision match | continue existing checks |
| tool/action mismatch | fail closed |
| target mismatch | fail closed |
| destination binding mismatch | fail closed |
| target mode mismatch | fail closed |
| scope mismatch | fail closed |
| credential_ref mismatch | fail closed |
| execution mode mismatch | fail closed |
| external_discovery escalation | fail closed |
| missing required request field | fail closed |
| missing required decision field | fail closed |
| malformed request/decision constraints | fail closed |
| evidence output | records diff categories without sensitive material |

The candidate should prefer deterministic fixtures over environment-dependent behavior.

## Evidence boundary

The candidate result should be evidence-safe.

It may record:

~~~text
comparison_status
allowed_to_continue
diff_categories
diff_reasons
request_field_names
decision_field_names
matched_constraints
blocked_constraints
~~~

It should not record:

~~~text
raw secrets
raw credentials
tokens
private customer material
scanner output
private artifacts
full raw request payloads when unnecessary
full raw authorization decision payloads when unnecessary
~~~

## Non-goals

This readiness checkpoint does not:

* implement request/decision constraint-diff enforcement,
* modify constraint-diff behavior,
* modify runtime behavior,
* authorize runtime execution,
* authorize scanner execution,
* authorize Docker/lab execution,
* permit credential injection,
* authorize customer targets,
* authorize delivery,
* change validator behavior,
* change schemas,
* change public samples,
* reopen AAEF main handback,
* open an AAEF main issue or PR,
* generate an issue command or URL,
* promote AAEF-AI-VA into AAEF Core/Profile/Practical Package status.

## Relationship to v0.6.131

v0.6.131 selected request/decision constraint-diff enforcement as the next High-risk work item and assigned three checkpoints:

~~~text
v0.6.132 Request/Decision Constraint-Diff Enforcement Readiness
v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate
v0.6.134 Request/Decision Constraint-Diff Enforcement Review and Decision
~~~

This checkpoint is the readiness checkpoint.

## Relationship to v0.6.130

v0.6.130 closed the authorization expiry current-time check work item.

This checkpoint starts the next selected High-risk gate-semantics track without implementing behavior.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

No request/decision constraint-diff enforcement is added in this checkpoint.

No constraint-diff behavior is modified.

No constraint-diff helper is added.

No request/decision comparison logic is modified.

No authorization gate runtime behavior is modified.

No candidate implementation is started.

No review/decision closeout is completed.

No authorization expiry current-time check is added or modified.

No external_discovery fail-closed behavior is added.

No mock/dry-run status terminology is renamed.

No Enterprise Review Guide is created.

No technical due diligence summary is created.

No safe PoC boundary template is created.

No control matrix is created.

No reviewer walkthrough is created.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main handback sequence is reopened.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Next checkpoint

Proceed to:

~~~text
v0.6.133 Request/Decision Constraint-Diff Enforcement Candidate
~~~

That checkpoint may implement the candidate behavior and tests within the boundaries defined here.
