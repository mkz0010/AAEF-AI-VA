from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DOC = ROOT / "docs/237-v06161-public-review-entry-point-polish-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0231-add-v06161-public-review-entry-point-polish-candidate.md"
ISSUE = ROOT / "planning/issues/0230-add-v06161-public-review-entry-point-polish-candidate.md"
EXTERNAL_PACKAGE = ROOT / "docs/external-review-package.md"
V06160_DOC = ROOT / "docs/236-v06160-next-work-selection-using-risk-tiered-granularity.md"
V06159_DOC = ROOT / "docs/235-v06159-external-review-package-integration-review-and-decision.md"
V06158_DOC = ROOT / "docs/234-v06158-external-review-package-integration-candidate.md"
V06156_DOC = ROOT / "docs/232-v06156-reviewer-walkthrough-review-and-decision.md"
V06153_DOC = ROOT / "docs/229-v06153-control-matrix-review-and-decision.md"
V06150_DOC = ROOT / "docs/226-v06150-safe-poc-boundary-template-review-and-decision.md"
V06147_DOC = ROOT / "docs/223-v06147-technical-due-diligence-summary-review-and-decision.md"
V06144_DOC = ROOT / "docs/220-v06144-enterprise-review-guide-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_README_PHRASES = ['## Public Review Entry Point', 'For external review, start with `docs/external-review-package.md`.', 'This entry point is for review and orientation only.', 'It does not authorize a PoC.', 'It does not approve runtime execution.', 'It does not approve scanner execution.', 'It does not grant permission to test any system.', 'It does not create a commercial contract.', 'It does not approve customer delivery.', '`docs/external-review-package.md`', '`docs/reviewer-walkthrough.md`', '`docs/control-matrix.md`', '`docs/technical-due-diligence-summary.md`', '`docs/enterprise-review-guide.md`', '`docs/safe-poc-boundary-template.md`', 'AI output is a request; gates decide execution.', 'Use this path to review boundaries, not to approve real-world action.', 'Customer PoC, commercial terms, runtime/scanner execution, credential use, customer targets, and delivery require separate authorization.']

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk public-facing documentation work item.', 'This checkpoint creates the Public Review Entry Point Polish candidate.', 'The review and decision are deferred to v0.6.162.', 'Candidate implementation summary', 'README public entry point', 'Public entry point scope', 'Claim boundaries', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.162 Public Review Entry Point Polish Review and Decision']
FLAGS = ['public_review_entry_point_polish_candidate_completed = true', 'public_review_entry_point_polish_candidate_is_medium_risk = true', 'public_review_entry_point_polish_candidate_checkpoint_1_of_2 = true', 'public_review_entry_point_polish_review_decision_deferred_to_v06162 = true', 'public_review_entry_point_created = true', 'public_review_entry_point_modified = true', 'readme_public_entry_modified = true', 'public_review_entry_point_candidate_claim_safe = true', 'public_review_entry_points_to_external_review_package = true', 'public_review_entry_identifies_intended_readers = true', 'public_review_entry_includes_non_authorizing_notice = true', 'public_review_entry_links_key_reviewer_artifacts = true', 'public_review_entry_includes_safe_review_order = true', 'public_review_entry_mentions_separate_authorization_for_poc_commercial_runtime_delivery = true', 'public_review_entry_claim_boundaries_included = true', 'public_review_entry_review_decision_completed = false', 'review_decision_completed = false', 'external_review_package_modified = false', 'reviewer_walkthrough_modified = false', 'control_matrix_modified = false', 'safe_poc_boundary_template_modified = false', 'technical_due_diligence_summary_modified = false', 'enterprise_review_guide_modified = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.162 Public Review Entry Point Polish Review and Decision']

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
    for path in [README, DOC, ADR, ISSUE, EXTERNAL_PACKAGE, V06160_DOC, V06159_DOC, V06158_DOC, V06156_DOC, V06153_DOC, V06150_DOC, V06147_DOC, V06144_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    readme_text = README.read_text(encoding="utf-8")
    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED_README_PHRASES:
        require(phrase in readme_text, f"README missing required public review entry text: {phrase}")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.161 document missing required text: {phrase}")

    combined_lower = (readme_text + "\n" + doc_text).lower()
    for phrase in FORBIDDEN_AFFIRMATIVE_PHRASES:
        require(phrase not in combined_lower, f"forbidden affirmative claim found: {phrase}")

    v06160 = V06160_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = public_review_entry_point_polish",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.161 Public Review Entry Point Polish Candidate",
        "readme_public_entry_modified = false",
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
        require(phrase in v06160, f"v0.6.160 selection missing required phrase: {phrase}")

    require("external_review_package_integration_work_item_closed = true" in V06159_DOC.read_text(encoding="utf-8"), "v0.6.159 External Review Package work item must remain closed")
    require("external_review_package_integration_candidate_completed = true" in V06158_DOC.read_text(encoding="utf-8"), "v0.6.158 External Review Package candidate must remain recorded")
    require("reviewer_walkthrough_work_item_closed = true" in V06156_DOC.read_text(encoding="utf-8"), "v0.6.156 Reviewer Walkthrough work item must remain closed")
    require("control_matrix_work_item_closed = true" in V06153_DOC.read_text(encoding="utf-8"), "v0.6.153 Control Matrix work item must remain closed")
    require("safe_poc_boundary_template_work_item_closed = true" in V06150_DOC.read_text(encoding="utf-8"), "v0.6.150 Safe PoC Boundary Template work item must remain closed")
    require("technical_due_diligence_summary_work_item_closed = true" in V06147_DOC.read_text(encoding="utf-8"), "v0.6.147 Technical Due Diligence Summary work item must remain closed")
    require("enterprise_review_guide_work_item_closed = true" in V06144_DOC.read_text(encoding="utf-8"), "v0.6.144 Enterprise Review Guide work item must remain closed")
    require("aaef_main_handback_sequence_paused = true" in V06119_DOC.read_text(encoding="utf-8"), "v0.6.119 handback pause must remain recorded")

    print("v0.6.161 Public Review Entry Point Polish candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
