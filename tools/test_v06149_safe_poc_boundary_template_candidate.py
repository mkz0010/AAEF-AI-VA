from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs/safe-poc-boundary-template.md"
DOC = ROOT / "docs/225-v06149-safe-poc-boundary-template-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0219-add-v06149-safe-poc-boundary-template-candidate.md"
ISSUE = ROOT / "planning/issues/0218-add-v06149-safe-poc-boundary-template-candidate.md"
V06148_DOC = ROOT / "docs/224-v06148-next-work-selection-using-risk-tiered-granularity.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06141_DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk PoC-facing documentation work item.', 'This checkpoint creates the Safe PoC Boundary Template candidate.', 'The review and decision are deferred to v0.6.150.', 'Candidate implementation summary', 'Candidate template', 'Claim boundaries', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.150 Safe PoC Boundary Template Review and Decision']
REQUIRED_TEMPLATE_PHRASES = ['# Safe PoC Boundary Template', 'Reader', 'Purpose', 'Non-authorizing notice', 'Boundary summary', 'Required written authorization fields', 'Parties and responsibilities', 'Target scope', 'Excluded systems', 'PoC time window', 'Tool and action limits', 'AI request and gate boundary', 'Credential and data handling', 'Evidence retention and deletion', 'Human review and approval', 'Stop conditions', 'Communications and escalation', 'Deliverables boundary', 'Commercial and license boundary', 'Pre-PoC review checklist', 'Not allowed by this template', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'This template does not authorize a PoC.', 'This template does not grant permission to test any system.', 'This template does not create a commercial contract.', 'This template does not approve runtime execution.', 'This template does not approve scanner execution.', 'This template does not approve credential injection.', 'This template does not approve customer delivery.']
FLAGS = ['safe_poc_boundary_template_candidate_completed = true', 'safe_poc_boundary_template_candidate_is_medium_risk = true', 'safe_poc_boundary_template_candidate_checkpoint_1_of_2 = true', 'safe_poc_boundary_template_review_decision_deferred_to_v06150 = true', 'safe_poc_boundary_template_created = true', 'safe_poc_boundary_template_candidate_claim_safe = true', 'safe_poc_boundary_template_non_authorizing_notice_included = true', 'safe_poc_boundary_template_required_written_authorization_fields_included = true', 'safe_poc_boundary_template_parties_and_responsibilities_included = true', 'safe_poc_boundary_template_target_scope_included = true', 'safe_poc_boundary_template_excluded_systems_included = true', 'safe_poc_boundary_template_time_window_included = true', 'safe_poc_boundary_template_tool_action_limits_included = true', 'safe_poc_boundary_template_ai_gate_boundary_included = true', 'safe_poc_boundary_template_credential_data_handling_included = true', 'safe_poc_boundary_template_evidence_retention_deletion_included = true', 'safe_poc_boundary_template_human_review_approval_included = true', 'safe_poc_boundary_template_stop_conditions_included = true', 'safe_poc_boundary_template_communications_escalation_included = true', 'safe_poc_boundary_template_deliverables_boundary_included = true', 'safe_poc_boundary_template_commercial_license_boundary_included = true', 'safe_poc_boundary_template_pre_poc_review_checklist_included = true', 'safe_poc_boundary_template_not_allowed_section_included = true', 'safe_poc_boundary_template_claim_boundaries_included = true', 'safe_poc_boundary_template_review_decision_completed = false', 'review_decision_completed = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'enterprise_review_guide_modified = false', 'technical_due_diligence_summary_modified = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.150 Safe PoC Boundary Template Review and Decision']

FORBIDDEN_AFFIRMATIVE_PHRASES = [
    "customer poc is authorized",
    "commercial contract is created",
    "runtime execution is authorized",
    "scanner execution is authorized",
    "docker execution is authorized",
    "credential injection is permitted",
    "customer target is authorized",
    "delivery is authorized",
    "authorized to test third-party systems",
    "authorized for third-party testing by this template",
    "permission to test third-party systems is granted",
    "is certified as",
    "certified framework for",
    "legally compliant with",
    "legal compliance achieved",
    "audit opinion provided",
    "audit sufficiency achieved",
    "deployment approved",
    "is production ready",
    "production-ready scanner",
    "complete vulnerability scanner",
    "complete vulnerability assessment capability is provided",
    "equivalent to nist",
    "equivalent to iso",
    "safe to run without gates",
    "ai can safely run tools without gates",
    "aaef core promotion = true",
    "aaef profile promotion = true",
    "aaef practical package promotion = true",
]

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [TEMPLATE, DOC, ADR, ISSUE, V06148_DOC, V06147_DOC, V06144_DOC, V06141_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    template_text = TEMPLATE.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_TEMPLATE_PHRASES:
        require(phrase in template_text, f"Safe PoC Boundary Template missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.149 document missing required text: {phrase}")

    for phrase in [
        "No blank field should be treated as permission.",
        "If a target is not explicitly listed, it is outside the PoC boundary.",
        "If an exclusion conflicts with an approved target entry, the exclusion should win until separately resolved.",
        "PoC authorization should expire automatically outside the written time window.",
        "Human approval should be action-bound and evidence-linked.",
        "When a stop condition occurs, the safe default is pause and review.",
        "Delivery should require a separate delivery authorization gate.",
    ]:
        require(phrase in template_text, f"Safe PoC Boundary Template missing boundary safeguard: {phrase}")

    combined_lower = (template_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06148 = V06148_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = safe_poc_boundary_template",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.149 Safe PoC Boundary Template Candidate",
        "safe_poc_boundary_template_created = false",
        "customer_poc_authorized = false",
        "commercial_contract_created = false",
        "certification_claim_occurs = false",
        "legal_compliance_claim_occurs = false",
        "audit_opinion_claim_occurs = false",
        "production_readiness_claim_occurs = false",
        "external_framework_equivalence_claim_occurs = false",
        "diagnostic_completeness_claim_occurs = false",
        "third_party_testing_authorization_claim_occurs = false",
    ]:
        require(phrase in v06148, f"v0.6.148 selection missing required phrase: {phrase}")

    v06147 = V06147_DOC.read_text(encoding="utf-8")
    require("technical_due_diligence_summary_work_item_closed = true" in v06147, "v0.6.147 Technical Due Diligence Summary work item must remain closed")

    v06144 = V06144_DOC.read_text(encoding="utf-8")
    require("enterprise_review_guide_work_item_closed = true" in v06144, "v0.6.144 Enterprise Review Guide work item must remain closed")

    v06141 = V06141_DOC.read_text(encoding="utf-8")
    require("mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true" in v06141, "v0.6.141 mock/dry-run terminology work item must remain closed")

    v06138 = V06138_DOC.read_text(encoding="utf-8")
    require("external_discovery_fail_closed_behavior_work_item_closed = true" in v06138, "v0.6.138 external discovery work item must remain closed")

    v06134 = V06134_DOC.read_text(encoding="utf-8")
    require("request_decision_constraint_diff_enforcement_work_item_closed = true" in v06134, "v0.6.134 constraint-diff work item must remain closed")

    v06130 = V06130_DOC.read_text(encoding="utf-8")
    require("authorization_expiry_current_time_check_work_item_closed = true" in v06130, "v0.6.130 authorization expiry work item must remain closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "customer poc is authorized by this candidate",
        "commercial contract is created by this candidate",
        "runtime execution is authorized by this candidate",
        "scanner execution is authorized by this candidate",
        "credential injection is permitted by this candidate",
        "customer target is authorized by this candidate",
        "delivery is authorized by this candidate",
        "this candidate opens an aaef main issue",
        "this candidate submits to aaef main",
        "certification claim is made",
        "legal compliance claim is made",
        "audit opinion claim is made",
        "production readiness claim is made",
        "external-framework equivalence claim is made",
    ]:
        require(phrase not in lower_doc, f"v0.6.149 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.149 Safe PoC Boundary Template candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
