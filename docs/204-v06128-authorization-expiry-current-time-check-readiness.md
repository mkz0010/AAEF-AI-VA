# v0.6.128 Authorization Expiry Current-Time Check Readiness

Status: readiness
Date: 2026-05-10

## Purpose

This checkpoint prepares the authorization expiry current-time check selected in v0.6.127.

This is checkpoint 1 of 3 for a High-risk gate-semantics work item.

This checkpoint prepares authorization expiry current-time check readiness.

The candidate implementation is deferred to v0.6.129.

The review and decision are deferred to v0.6.130.

This checkpoint does not implement the authorization expiry current-time check.

This checkpoint does not modify authorization behavior.

This checkpoint does not modify runtime behavior.

## Readiness record

~~~text
authorization_expiry_current_time_check_readiness_completed = true
authorization_expiry_current_time_check_readiness_is_high_risk = true
authorization_expiry_current_time_check_readiness_checkpoint_1_of_3 = true
authorization_expiry_current_time_check_candidate_deferred_to_v06129 = true
authorization_expiry_current_time_check_review_decision_deferred_to_v06130 = true
authorization_expiry_current_time_check_readiness_documentation_only = true
authorization_expiry_current_time_check_readiness_identifies_target_discovery = true
authorization_expiry_current_time_check_readiness_identifies_expected_behavior = true
authorization_expiry_current_time_check_readiness_identifies_tests_to_add_or_update = true
authorization_expiry_current_time_check_readiness_identifies_fail_closed_boundary = true
authorization_expiry_current_time_check_readiness_identifies_non_goals = true
authorization_expiry_now_check_added = false
authorization_expiry_behavior_modified = false
authorization_validation_logic_modified = false
authorization_gate_runtime_behavior_modified = false
current_time_source_implemented = false
expired_authorization_fail_closed_behavior_implemented = false
candidate_implementation_started = false
review_decision_completed = false
security_reporting_channel_consistency_work_item_closed = true
aaef_main_handback_sequence_remains_paused = true
aaef_main_handback_sequence_reopened = false
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
constraint_diff_enforcement_added = false
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
selected_next_checkpoint = v0.6.129 Authorization Expiry Current-Time Check Candidate
~~~

## Readiness target discovery

The readiness scan looked for repository files that mention authorization and expiry/current-time related terms.

Potential target files or review starting points:

- `docs/07-tool-gateway-design.md` — matched terms: authorization, authorized, now
- `docs/10-exit-strategy.md` — matched terms: authorization, now
- `docs/100-v0623-aaef-applied-evidence-package-design.md` — matched terms: authorization, authorized, now
- `docs/101-v0624-applied-evidence-scenario-set-planning.md` — matched terms: authorization, authorized, expiry
- `docs/102-v0625-static-applied-evidence-fixture-planning.md` — matched terms: authorization, authorized, expiry
- `docs/103-v0626-reviewer-walkthrough-and-five-questions-mapping.md` — matched terms: authorization, authorized, expiry
- `docs/11-mvp-scope.md` — matched terms: authorization, now
- `docs/114-v0637-sanitized-public-sample-close-readiness-review.md` — matched terms: authorization, authorized, now
- `docs/118-v0641-public-example-structural-validator-review-and-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/12-credential-ref-flow.md` — matched terms: authorization, authorized, expires, expires_at, expiry, now
- `docs/120-v0643-applied-implementation-handback-review-and-next-direction.md` — matched terms: authorization, authorized, now
- `docs/122-v0645-public-validator-negative-fixture-implementation-readiness-review.md` — matched terms: authorization, authorized, now
- `docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md` — matched terms: authorization, authorized, now
- `docs/13-tool-gateway-mvp-design.md` — matched terms: authorization, authorized, expires, expires_at, now
- `docs/131-v0654-public-validator-failure-category-mapping-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md` — matched terms: authorization, authorized, now
- `docs/14-mvp-schemas.md` — matched terms: authorization, authorized, now
- `docs/141-v0664-public-validator-maintenance-pause-next-direction-review.md` — matched terms: authorization, authorized, now
- `docs/142-v0665-public-validator-pause-review-closeout.md` — matched terms: authorization, authorized, now
- `docs/143-v0666-applied-evidence-next-direction-intake.md` — matched terms: authorization, authorized, now
- `docs/144-v0667-applied-evidence-current-state-review.md` — matched terms: authorization, authorized, now
- `docs/145-v0668-applied-evidence-gap-prioritization-review.md` — matched terms: authorization, authorized, now
- `docs/146-v0669-applied-evidence-reviewer-current-state-summary-planning.md` — matched terms: authorization, authorized, now
- `docs/147-v0670-applied-evidence-reviewer-current-state-summary-candidate.md` — matched terms: authorization, authorized, now
- `docs/148-v0671-applied-evidence-reviewer-current-state-summary-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/149-v0672-applied-evidence-next-gap-selection-review.md` — matched terms: authorization, authorized, now
- `docs/150-v0673-public-sample-five-questions-clarity-planning.md` — matched terms: authorization, authorized, now
- `docs/151-v0674-public-sample-five-questions-clarity-candidate.md` — matched terms: authorization, authorized, now
- `docs/152-v0675-public-sample-five-questions-clarity-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/153-v0676-applied-evidence-next-gap-selection-after-clarity-closeout.md` — matched terms: authorization, authorized, now
- `docs/154-v0678-public-sample-relationship-to-validator-planning.md` — matched terms: authorization, authorized, now
- `docs/155-v0679-public-sample-relationship-to-validator-candidate.md` — matched terms: authorization, authorized, now
- `docs/156-v0680-public-sample-relationship-to-validator-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/157-v0681-applied-evidence-next-gap-selection-after-relationship-closeout.md` — matched terms: authorization, authorized, now
- `docs/158-v0682-evidence-interface-handback-readiness-planning.md` — matched terms: authorization, authorized, now
- `docs/159-v0683-evidence-interface-handback-readiness-candidate.md` — matched terms: authorization, authorized, now
- `docs/160-v0684-evidence-interface-handback-readiness-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/161-v0685-applied-evidence-handback-preparation-decision.md` — matched terms: authorization, authorized, now
- `docs/162-v0686-narrow-public-safe-aaef-main-handback-preparation-planning.md` — matched terms: authorization, authorized, now
- `docs/163-v0687-narrow-public-safe-aaef-main-handback-preparation-candidate.md` — matched terms: authorization, authorized, now
- `docs/164-v0688-narrow-public-safe-aaef-main-handback-preparation-review-close-readiness.md` — matched terms: authorization, authorized, now
- `docs/165-v0689-applied-evidence-handback-drafting-decision.md` — matched terms: authorization, authorized, now
- `docs/166-v0690-narrow-public-safe-aaef-main-handback-drafting-planning.md` — matched terms: authorization, authorized, now
- `docs/167-v0691-narrow-public-safe-aaef-main-handback-drafting-candidate.md` — matched terms: authorization, authorized, now
- `docs/169-v0693-applied-evidence-handback-material-preparation-decision.md` — matched terms: authorization, authorized, now
- `docs/17-tool-gateway-negative-tests.md` — matched terms: authorization, expires, expires_at, now
- `docs/170-v0694-narrow-public-safe-aaef-main-handback-material-preparation-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/171-v0695-narrow-public-safe-aaef-main-handback-material-preparation-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/172-v0696-narrow-public-safe-aaef-main-handback-material-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/173-v0697-applied-evidence-handback-material-drafting-or-submission-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/174-v0698-narrow-public-safe-aaef-main-handback-text-drafting-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/175-v0699-narrow-public-safe-aaef-main-handback-text-drafting-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/176-v06100-narrow-public-safe-aaef-main-handback-text-drafting-candidate-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/177-v06101-applied-evidence-handback-text-submission-or-pause-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/178-v06102-narrow-public-safe-aaef-main-handback-final-text-preparation-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/179-v06103-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/18-mock-vault-credential-ref-validation.md` — matched terms: authorization, now
- `docs/180-v06104-narrow-public-safe-aaef-main-handback-final-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/181-v06105-applied-evidence-handback-submittable-text-or-pause-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/182-v06106-narrow-public-safe-aaef-main-handback-submittable-text-preparation-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/183-v06107-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/184-v06108-narrow-public-safe-aaef-main-handback-submittable-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/185-v06109-applied-evidence-handback-submission-or-pause-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/186-v06110-narrow-public-safe-aaef-main-handback-submission-workflow-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/187-v06111-narrow-public-safe-aaef-main-handback-workflow-selection-or-exact-text-preparation-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/188-v06112-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-planning.md` — matched terms: authorization, authorized, expiry, now
- `docs/189-v06113-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/190-v06114-narrow-public-safe-aaef-main-handback-exact-issue-text-preparation-candidate-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/191-v06115-narrow-public-safe-aaef-main-handback-exact-issue-submission-or-pause-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/192-v06116-narrow-public-safe-aaef-main-handback-human-submission-checklist-preparation.md` — matched terms: authorization, authorized, expiry, now
- `docs/193-v06117-narrow-public-safe-aaef-main-handback-human-submission-checklist-review-close-readiness.md` — matched terms: authorization, authorized, expiry, now
- `docs/194-v06118-narrow-public-safe-aaef-main-handback-human-maintainer-final-submission-decision-or-pause.md` — matched terms: authorization, authorized, expiry, now
- `docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md` — matched terms: authorization, authorized, expiry, now
- `docs/197-v06121-next-direction-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, expiry, now
- `docs/198-v06122-readme-current-latest-baseline-clarity-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/199-v06123-readme-current-latest-baseline-clarity-review-and-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, expiry, now
- `docs/201-v06125-security-reporting-channel-consistency-candidate.md` — matched terms: authorization, authorized, expiry, now
- `docs/202-v06126-security-reporting-channel-consistency-review-and-decision.md` — matched terms: authorization, authorized, expiry, now
- `docs/203-v06127-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, authorized, current_time, expiry, now
- `docs/22-internal-adapter-artifact-policy.md` — matched terms: authorization, now
- `docs/23-zap-adapter-command-plan.md` — matched terms: authorization, now
- `docs/24-controlled-executor-policy.md` — matched terms: authorization, now
- `docs/26-real-execution-readiness-gate.md` — matched terms: authorization, now
- `docs/27-operator-readiness-review.md` — matched terms: authorization, expiration
- `docs/28-human-approval-record-gate.md` — matched terms: authorization, expiration
- `docs/29-evidence-chain-review-linkage.md` — matched terms: authorization, authorized, now
- `docs/37-delivery-authorization-gate.md` — matched terms: authorization, authorized, now
- `docs/44-no-egress-timeout-kill-switch-policy.md` — matched terms: authorization, now
- `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md` — matched terms: authorization, authorized, now
- `docs/62-public-facing-repository-metadata-and-announcement-pack.md` — matched terms: authorization, authorized, now
- `docs/64-public-release-notes-and-launch-announcement-package.md` — matched terms: authorization, authorized, now
- `docs/75-public-evidence-and-capability-boundary-summary.md` — matched terms: authorization, authorized, now
- `docs/78-v061-capability-inventory-and-maturity-map.md` — matched terms: authorization, authorized, now
- `docs/79-v062-evaluation-criteria-and-acceptance-model.md` — matched terms: authorization, authorized, now
- `docs/80-v063-safety-boundary-and-non-goal-review.md` — matched terms: authorization, authorized, now
- `docs/81-v064-local-assessment-lab-decision-record.md` — matched terms: authorization, authorized, now
- `docs/83-v066-ai-request-decision-boundary-and-tool-selection-criteria.md` — matched terms: authorization, authorized, now
- `docs/84-v067-observation-normalization-and-diagnostic-fidelity-risk-review.md` — matched terms: authorization, authorized, now
- `docs/85-v068-demo-scenario-and-reviewer-walkthrough-planning.md` — matched terms: authorization, authorized, now
- `docs/89-v0612-non-running-docker-compose-design-review-planning.md` — matched terms: authorization, authorized, now
- `docs/94-v0617-static-fixture-validator-scaffold-planning.md` — matched terms: authorization, authorized, now
- `docs/95-v0618-static-fixture-validator-minimal-scaffold-design.md` — matched terms: authorization, authorized, now
- `planning/decisions/ADR-0007-tool-gateway-as-trusted-control-boundary.md` — matched terms: authorization, authorized, now
- `planning/decisions/ADR-0008-mvp-schema-contracts.md` — matched terms: authorization, now
- `planning/decisions/ADR-0011-add-fail-closed-negative-tests-for-tool-gateway.md` — matched terms: authorization, expiration
- `planning/decisions/ADR-0012-validate-credential-ref-against-vault-metadata.md` — matched terms: authorization, expiry, now
- `planning/decisions/ADR-0014-add-tool-gateway-adapter-stubs-before-real-tool-integration.md` — matched terms: authorization, now
- `planning/decisions/ADR-0023-add-evidence-chain-review-decision-linkage.md` — matched terms: authorization, now
- `planning/decisions/ADR-0024-add-evidence-reconstruction-report.md` — matched terms: authorization, now
- `planning/decisions/ADR-0030-add-report-packet-review-gate.md` — matched terms: authorization, now
- `planning/decisions/ADR-0031-add-delivery-authorization-gate.md` — matched terms: authorization, authorized, now
- `planning/decisions/ADR-0032-add-lifecycle-integration-checkpoint.md` — matched terms: authorization, now
- `planning/decisions/ADR-0046-add-preflight-evidence-validation-rules.md` — matched terms: authorization, now
- `planning/decisions/ADR-0050-add-publication-hygiene-private-artifact-exclusion-checkpoint.md` — matched terms: authorization, now
- `planning/decisions/ADR-0053-prepare-v040-publication-preparation-release.md` — matched terms: authorization, now
- `planning/decisions/ADR-0055-clean-up-readme-public-english-wording.md` — matched terms: authorization, now
- `planning/decisions/ADR-0056-add-public-facing-repository-metadata-announcement-pack.md` — matched terms: authorization, now
- `planning/decisions/ADR-0058-add-public-release-notes-launch-announcement-package.md` — matched terms: authorization, now
- `planning/decisions/ADR-0060-add-commercial-adoption-preparation-checkpoint.md` — matched terms: authorization, now
- `planning/decisions/ADR-0067-add-public-trust-reviewer-navigation-checkpoint.md` — matched terms: authorization, now
- `planning/decisions/ADR-0068-add-public-front-page-repository-landing-polish-checkpoint.md` — matched terms: authorization, now
- `planning/decisions/ADR-0091-add-v0620-static-fixture-validator-read-only-implementation-scaffold.md` — matched terms: authorization, now
- `planning/decisions/ADR-0102-add-v0631-static-mock-applied-evidence-private-review-record.md` — matched terms: authorization, now
- `planning/decisions/ADR-0111-add-v0640-public-example-structural-validator-implementation-candidate.md` — matched terms: authorization, now
- `planning/decisions/ADR-0197-add-v06127-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, expiry
- `planning/issues/0002-design-credential-ref-flow.md` — matched terms: authorization, expiry
- `planning/issues/0006-build-tool-gateway-prototype-scaffold.md` — matched terms: authorization, now
- `planning/issues/0008-add-tool-gateway-negative-tests.md` — matched terms: authorization, expiration
- `planning/issues/0009-add-mock-vault-credential-ref-validation.md` — matched terms: authorization, expiry, now
- `planning/issues/0029-add-report-packet-review-gate.md` — matched terms: authorization, now
- `planning/issues/0030-add-delivery-authorization-gate.md` — matched terms: authorization, authorized, now
- `planning/issues/0039-add-execution-authorization-gate-scaffold.md` — matched terms: authorization, authorized, now
- `planning/issues/0040-add-preflight-validation-scaffold.md` — matched terms: authorization, authorized, now
- `planning/issues/0044-add-generated-preflight-evidence-record-examples.md` — matched terms: authorization, authorized, now
- `planning/issues/0196-add-v06127-next-work-selection-using-risk-tiered-granularity.md` — matched terms: authorization, expiry
- `prototypes/tool-gateway/README.md` — matched terms: authorization, expiry, now
- `prototypes/tool-gateway/delivery_authorization.py` — matched terms: authorization, authorized, now
- `prototypes/tool-gateway/examples/allowed-action.authorization-decision.json` — matched terms: authorization, expires, expires_at
- `prototypes/tool-gateway/examples/denied-action.authorization-decision.json` — matched terms: authorization, expires, expires_at
- `prototypes/tool-gateway/examples/human-approval-required.authorization-decision.json` — matched terms: authorization, expires, expires_at
- `prototypes/tool-gateway/finding_review.py` — matched terms: authorization, now
- `prototypes/tool-gateway/gateway.py` — matched terms: authorization, now
- `prototypes/tool-gateway/policy.py` — matched terms: authorization, expires, expires_at, now
- `prototypes/tool-gateway/preflight_evidence_record.py` — matched terms: authorization, authorized, now
- `prototypes/tool-gateway/report_packet_review.py` — matched terms: authorization, now
- `prototypes/tool-gateway/report_review.py` — matched terms: authorization, now
- `prototypes/tool-gateway/runner.py` — matched terms: authorization, now
- `prototypes/tool-gateway/sanitizer.py` — matched terms: authorization, now
- `tools/test_human_approval_gate.py` — matched terms: authorization, expires, expires_at
- `tools/test_real_execution_readiness_gate.py` — matched terms: authorization, now
- `tools/test_tool_gateway_runner.py` — matched terms: authorization, expires, expires_at
- `tools/test_v06100_narrow_public_safe_aaef_main_handback_text_drafting_candidate_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06101_applied_evidence_handback_text_submission_or_pause_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06102_narrow_public_safe_aaef_main_handback_final_text_preparation_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06103_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06104_narrow_public_safe_aaef_main_handback_final_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06105_applied_evidence_handback_submittable_text_or_pause_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06106_narrow_public_safe_aaef_main_handback_submittable_text_preparation_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06107_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate.py` — matched terms: authorization, authorized, expiry
- `tools/test_v06108_narrow_public_safe_aaef_main_handback_submittable_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06109_applied_evidence_handback_submission_or_pause_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06110_narrow_public_safe_aaef_main_handback_submission_workflow_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06111_narrow_public_safe_aaef_main_handback_workflow_selection_or_exact_text_preparation_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06112_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06113_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06114_narrow_public_safe_aaef_main_handback_exact_issue_text_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06115_narrow_public_safe_aaef_main_handback_exact_issue_submission_or_pause_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06116_narrow_public_safe_aaef_main_handback_human_submission_checklist_preparation.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06117_narrow_public_safe_aaef_main_handback_human_submission_checklist_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06118_narrow_public_safe_aaef_main_handback_human_maintainer_final_submission_decision_or_pause.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06119_narrow_public_safe_aaef_main_handback_pause_and_current_state_closeout_review.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06121_next_direction_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06122_readme_current_latest_baseline_clarity_candidate.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06123_readme_current_latest_baseline_clarity_review_and_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06124_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06125_security_reporting_channel_consistency_candidate.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06126_security_reporting_channel_consistency_review_and_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v06127_next_work_selection_using_risk_tiered_granularity.py` — matched terms: authorization, authorized, current_time, expiry, now
- `tools/test_v0637_sanitized_public_sample_close_readiness_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0664_public_validator_maintenance_pause_next_direction_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0665_public_validator_pause_review_closeout.py` — matched terms: authorization, authorized, now
- `tools/test_v0666_applied_evidence_next_direction_intake.py` — matched terms: authorization, authorized, now
- `tools/test_v0667_applied_evidence_current_state_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0668_applied_evidence_gap_prioritization_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0669_applied_evidence_reviewer_current_state_summary_planning.py` — matched terms: authorization, authorized, now
- `tools/test_v0670_applied_evidence_reviewer_current_state_summary_candidate.py` — matched terms: authorization, authorized, now
- `tools/test_v0671_applied_evidence_reviewer_current_state_summary_review_close_readiness.py` — matched terms: authorization, authorized, now
- `tools/test_v0672_applied_evidence_next_gap_selection_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0673_public_sample_five_questions_clarity_planning.py` — matched terms: authorization, authorized, now
- `tools/test_v0674_public_sample_five_questions_clarity_candidate.py` — matched terms: authorization, authorized, now
- `tools/test_v0675_public_sample_five_questions_clarity_review_close_readiness.py` — matched terms: authorization, authorized, now
- `tools/test_v0676_applied_evidence_next_gap_selection_after_clarity_closeout.py` — matched terms: authorization, authorized, now
- `tools/test_v0679_public_sample_relationship_to_validator_candidate.py` — matched terms: authorization, authorized, now
- `tools/test_v067_observation_normalization_diagnostic_fidelity_risk_review.py` — matched terms: authorization, authorized, now
- `tools/test_v0682_evidence_interface_handback_readiness_planning.py` — matched terms: authorization, authorized, now
- `tools/test_v0683_evidence_interface_handback_readiness_candidate.py` — matched terms: authorization, authorized, now
- `tools/test_v0685_applied_evidence_handback_preparation_decision.py` — matched terms: authorization, authorized, now
- `tools/test_v0689_applied_evidence_handback_drafting_decision.py` — matched terms: authorization, authorized, now
- `tools/test_v0693_applied_evidence_handback_material_preparation_decision.py` — matched terms: authorization, authorized, now
- `tools/test_v0694_narrow_public_safe_aaef_main_handback_material_preparation_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v0695_narrow_public_safe_aaef_main_handback_material_preparation_candidate.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v0696_narrow_public_safe_aaef_main_handback_material_preparation_candidate_review_close_readiness.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v0697_applied_evidence_handback_material_drafting_or_submission_decision.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v0698_narrow_public_safe_aaef_main_handback_text_drafting_planning.py` — matched terms: authorization, authorized, expiry, now
- `tools/test_v0699_narrow_public_safe_aaef_main_handback_text_drafting_candidate.py` — matched terms: authorization, authorized, expiry, now

This discovery is advisory only. It does not prove that these are the only files that matter, and it does not authorize implementation in this checkpoint.

## Expected candidate behavior

The v0.6.129 candidate should evaluate authorization expiry against the current time at the relevant gate boundary.

Expected behavior:

* If an authorization record has an expiry timestamp and the current time is later than that expiry timestamp, the gate should fail closed.
* If an authorization record has an expiry timestamp and the current time is before or equal to the expiry timestamp, the gate may proceed to the next existing authorization checks.
* If an authorization record has a malformed expiry timestamp, the gate should fail closed.
* If an authorization record requires expiry but the expiry value is missing, the gate should fail closed.
* The evidence or gate result should make the expiry decision reviewable without exposing secrets, credentials, customer material, scanner output, or private artifacts.
* The implementation should avoid using model output as authority.
* The implementation should avoid treating validator output as authority.
* The implementation should not authorize runtime execution, scanner execution, Docker execution, credential injection, customer targets, or delivery.

## Expected tests to add or update

The v0.6.129 candidate should add or update tests for at least these cases:

| Case | Expected result |
| --- | --- |
| not expired authorization | continue existing authorization checks |
| expired authorization | fail closed |
| expiry equal to current time | deterministic boundary result, documented in test expectation |
| malformed expiry timestamp | fail closed |
| missing required expiry timestamp | fail closed |
| timezone-aware timestamp | deterministic comparison |
| timezone-naive timestamp if present | fail closed or normalized only if explicitly documented |
| evidence output | records expiry decision without sensitive material |

The candidate should prefer deterministic test inputs instead of relying on wall-clock time directly.

## Fail-closed boundary

The fail-closed boundary for this work item is:

~~~text
expired_authorization -> blocked / not authorized
malformed_expiry -> blocked / not authorized
missing_required_expiry -> blocked / not authorized
ambiguous_current_time -> blocked / not authorized
~~~

The candidate should not introduce a permissive fallback for ambiguous expiry handling.

## Current-time source boundary

The candidate should use a controlled current-time source suitable for deterministic tests.

Preferred pattern:

~~~text
- production/default path may use a current-time provider
- tests inject fixed current-time values
- evidence records the comparison basis
- parsing and comparison errors fail closed
~~~

The readiness checkpoint does not choose final implementation mechanics.

## Non-goals

This readiness checkpoint does not:

* implement the authorization expiry current-time check,
* modify authorization behavior,
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

## Relationship to v0.6.127

v0.6.127 selected authorization expiry checked against current time as the next High-risk work item and assigned three checkpoints:

~~~text
v0.6.128 Authorization Expiry Current-Time Check Readiness
v0.6.129 Authorization Expiry Current-Time Check Candidate
v0.6.130 Authorization Expiry Current-Time Check Review and Decision
~~~

This checkpoint is the readiness checkpoint.

## Relationship to v0.6.126

v0.6.126 closed the SECURITY.md reporting-channel consistency work item as documentation-only.

This checkpoint starts the next selected High-risk gate-semantics track without implementing behavior.

## Relationship to v0.6.119

The v0.6.119 AAEF main handback sequence remains paused.

This checkpoint does not reopen that sequence.

## What did not happen

No authorization expiry now check is added in this checkpoint.

No authorization behavior is modified.

No authorization validation logic is modified.

No authorization gate runtime behavior is modified.

No current-time source is implemented.

No expired authorization fail-closed behavior is implemented.

No candidate implementation is started.

No review/decision closeout is completed.

No request/decision constraint-diff enforcement is added.

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
v0.6.129 Authorization Expiry Current-Time Check Candidate
~~~

That checkpoint may implement the candidate behavior and tests within the boundaries defined here.
