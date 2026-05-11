from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/224-v06148-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0218-add-v06148-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0217-add-v06148-next-work-selection-using-risk-tiered-granularity.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06146_DOC = ROOT / "docs/222-v06146-technical-due-diligence-summary-candidate.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06141_DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is Safe PoC Boundary Template.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.149 Safe PoC Boundary Template Candidate.', 'This checkpoint does not create the Safe PoC Boundary Template.', 'This checkpoint does not authorize a customer PoC.', 'This checkpoint does not modify runtime behavior.', 'This checkpoint does not reopen the AAEF main handback sequence.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'Claim boundaries for the selected work', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_v06148_completed = true', 'next_work_selection_v06148_is_documentation_only = true', 'next_work_selection_v06148_uses_v06120_granularity_policy = true', 'next_work_selection_v06148_uses_v06147_completed_work_item = true', 'v06148_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = safe_poc_boundary_template', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_implementation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.149 Safe PoC Boundary Template Candidate', 'safe_poc_boundary_template_selected = true', 'technical_due_diligence_summary_work_item_closed = true', 'enterprise_review_guide_work_item_closed = true', 'mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true', 'external_discovery_fail_closed_behavior_work_item_closed = true', 'request_decision_constraint_diff_enforcement_work_item_closed = true', 'authorization_expiry_current_time_check_work_item_closed = true', 'control_matrix_selected = false', 'reviewer_walkthrough_selected = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'safe_poc_boundary_template_created = false', 'safe_poc_boundary_template_behavior_modified = false', 'technical_due_diligence_summary_created = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_created = false', 'enterprise_review_guide_modified = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'commercial_contract_created = false', 'customer_poc_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06147_DOC, V06146_DOC, V06144_DOC, V06141_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.148 document missing required text: {phrase}")

    v06147 = V06147_DOC.read_text(encoding="utf-8")
    for phrase in [
        "technical_due_diligence_summary_review_decision_completed = true",
        "technical_due_diligence_summary_candidate_accepted = true",
        "technical_due_diligence_summary_work_item_closed = true",
        "selected_next_checkpoint = v0.6.148 Next Work Selection Using Risk-Tiered Granularity",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06147, f"v0.6.147 baseline missing required phrase: {phrase}")

    v06146 = V06146_DOC.read_text(encoding="utf-8")
    require("technical_due_diligence_summary_candidate_completed = true" in v06146, "v0.6.146 Technical Due Diligence Summary candidate must remain recorded")
    require("technical_due_diligence_summary_created = true" in v06146, "v0.6.146 Technical Due Diligence Summary creation must remain recorded")

    v06144 = V06144_DOC.read_text(encoding="utf-8")
    require("enterprise_review_guide_work_item_closed = true" in v06144, "v0.6.144 Enterprise Review Guide work item must be closed")

    v06141 = V06141_DOC.read_text(encoding="utf-8")
    require("mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true" in v06141, "v0.6.141 mock/dry-run terminology work item must be closed")

    v06138 = V06138_DOC.read_text(encoding="utf-8")
    require("external_discovery_fail_closed_behavior_work_item_closed = true" in v06138, "v0.6.138 external discovery work item must be closed")

    v06134 = V06134_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_work_item_closed = true" in v06134, "v0.6.134 constraint-diff work item must be closed")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must be closed")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    for phrase in [
        "risk_tiered_granularity_adopted = true",
        "Low risk",
        "Medium risk",
        "High risk",
        "Critical risk",
        "expanded_checkpoint_pattern_no_longer_default = true",
    ]:
        require(phrase in v06120, f"v0.6.120 policy missing required phrase: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in [
        "aaef_main_handback_sequence_paused = true",
        "aaef_main_handback_sequence_closed_for_now = true",
        "aaef_main_issue_opened = false",
        "aaef_main_pull_request_opened = false",
    ]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this checkpoint creates the safe poc boundary template",
        "this checkpoint authorizes a customer poc",
        "this checkpoint modifies runtime behavior",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
        "customer target is authorized by this checkpoint",
        "commercial contract is created by this checkpoint",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.148 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.148 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
