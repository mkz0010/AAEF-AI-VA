from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/control-matrix.md"
DOC = ROOT / "docs/228-v06152-control-matrix-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0222-add-v06152-control-matrix-candidate.md"
ISSUE = ROOT / "planning/issues/0221-add-v06152-control-matrix-candidate.md"
V06151_DOC = ROOT / "docs/227-v06151-next-work-selection-using-risk-tiered-granularity.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06149_DOC = ROOT / "docs/225-v06149-safe-poc-boundary-template-candidate.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06141_DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk reviewer-facing documentation work item.', 'This checkpoint creates the Control Matrix candidate.', 'The review and decision are deferred to v0.6.153.', 'Candidate implementation summary', 'Candidate matrix', 'Matrix row design', 'Claim boundaries', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.153 Control Matrix Review and Decision']
REQUIRED_MATRIX_PHRASES = ['# Control Matrix', 'Reader', 'Purpose', 'Non-authorizing notice', 'How to read this matrix', 'Matrix row design', 'Control matrix', 'AI request is not authority', 'Gate decision boundary', 'Current-time authorization expiry', 'Request/decision constraint drift', 'External discovery fail-closed behavior', 'Mock/dry-run status disambiguation', 'Non-execution evidence', 'Human approval boundary', 'Credential and data handling', 'Public/private artifact boundary', 'Report and delivery boundary', 'PoC non-authorization boundary', 'Commercial and license boundary', 'Conservative claim boundaries', 'Matrix interpretation limits', 'Claim boundaries', 'AI output is a request; gates decide execution.', 'This matrix is not a certification checklist.', 'This matrix is not a legal compliance checklist.', 'This matrix is not an audit checklist.', 'This matrix does not approve runtime execution.', 'This matrix does not approve scanner execution.', 'This matrix does not grant permission to test any system.']
FLAGS = ['control_matrix_candidate_completed = true', 'control_matrix_candidate_is_medium_risk = true', 'control_matrix_candidate_checkpoint_1_of_2 = true', 'control_matrix_review_decision_deferred_to_v06153 = true', 'control_matrix_created = true', 'control_matrix_candidate_claim_safe = true', 'control_matrix_reader_identified = true', 'control_matrix_non_authorizing_notice_included = true', 'control_matrix_rows_include_review_question = true', 'control_matrix_rows_include_control_boundary = true', 'control_matrix_rows_include_expected_evidence = true', 'control_matrix_rows_include_related_artifacts = true', 'control_matrix_rows_include_explicit_non_goal = true', 'control_matrix_rows_include_reviewer_note = true', 'control_matrix_ai_request_boundary_included = true', 'control_matrix_gate_decision_boundary_included = true', 'control_matrix_authorization_expiry_boundary_included = true', 'control_matrix_constraint_drift_boundary_included = true', 'control_matrix_external_discovery_boundary_included = true', 'control_matrix_mock_dry_run_status_boundary_included = true', 'control_matrix_non_execution_evidence_boundary_included = true', 'control_matrix_human_approval_boundary_included = true', 'control_matrix_credential_data_boundary_included = true', 'control_matrix_public_private_artifact_boundary_included = true', 'control_matrix_report_delivery_boundary_included = true', 'control_matrix_poc_non_authorization_boundary_included = true', 'control_matrix_commercial_license_boundary_included = true', 'control_matrix_claim_boundaries_included = true', 'control_matrix_review_decision_completed = false', 'review_decision_completed = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'reviewer_walkthrough_created = false', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.153 Control Matrix Review and Decision']

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
    "authorized for third-party testing by this matrix",
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

REQUIRED_ROW_IDS = [
    "CM-01",
    "CM-02",
    "CM-03",
    "CM-04",
    "CM-05",
    "CM-06",
    "CM-07",
    "CM-08",
    "CM-09",
    "CM-10",
    "CM-11",
    "CM-12",
    "CM-13",
    "CM-14",
]

REQUIRED_COLUMNS = [
    "Review question",
    "Control boundary",
    "Expected evidence",
    "Related artifacts",
    "Explicit non-goal",
    "Reviewer note",
]

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [MATRIX, DOC, ADR, ISSUE, V06151_DOC, V06150_DOC, V06149_DOC, V06147_DOC, V06144_DOC, V06141_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    matrix_text = MATRIX.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_MATRIX_PHRASES:
        require(phrase in matrix_text, f"Control Matrix missing required text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.152 document missing required text: {phrase}")

    for row_id in REQUIRED_ROW_IDS:
        require(row_id in matrix_text, f"Control Matrix missing required row id: {row_id}")

    for column in REQUIRED_COLUMNS:
        require(column in matrix_text, f"Control Matrix missing required column: {column}")

    for phrase in [
        "A row is not a compliance control, certification requirement, audit procedure, legal conclusion, deployment approval, or authorization record.",
        "Use the matrix to find overclaims, not to make them.",
        "This matrix does not create customer PoC approval.",
        "This matrix does not create a commercial contract.",
    ]:
        require(phrase in matrix_text, f"Control Matrix missing safeguard: {phrase}")

    combined_lower = (matrix_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06151 = V06151_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = control_matrix",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.152 Control Matrix Candidate",
        "control_matrix_created = false",
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
        require(phrase in v06151, f"v0.6.151 selection missing required phrase: {phrase}")

    v06150 = V06150_DOC.read_text(encoding="utf-8")
    require("safe_poc_boundary_template_work_item_closed = true" in v06150, "v0.6.150 Safe PoC Boundary Template work item must remain closed")

    v06149 = V06149_DOC.read_text(encoding="utf-8")
    require("safe_poc_boundary_template_candidate_completed = true" in v06149, "v0.6.149 Safe PoC Boundary Template candidate must remain recorded")

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
        require(phrase not in lower_doc, f"v0.6.152 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.152 Control Matrix candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
