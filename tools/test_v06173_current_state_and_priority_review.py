from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/249-v06173-current-state-and-priority-review.md"
ADR = ROOT / "planning/decisions/ADR-0243-add-v06173-current-state-and-priority-review.md"
ISSUE = ROOT / "planning/issues/0242-add-v06173-current-state-and-priority-review.md"
V06172_DOC = ROOT / "docs/248-v06172-aaef-main-contact-reflection-deferral-decision.md"
V06170_DOC = ROOT / "docs/246-v06170-public-entry-and-inquiry-route-consistency-review-review-and-decision.md"
V06167_DOC = ROOT / "docs/243-v06167-maintainer-inquiry-address-publication-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: review', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'Documentation and review package layer: implemented.', 'Safe demo layer: near-term candidate.', 'Runtime and scanner layer: deferred pending readiness review.', 'Customer PoC layer: deferred pending commercial and scope boundaries.', 'The first implementation layer should be a safe non-execution or mock/local-only demonstration.', 'Real scanner execution is not selected now.', 'Runtime execution is not selected now.', 'Customer PoC intake is not selected now.', 'AAEF main contact publication remains deferred.', 'Recommended next direction', 'v0.6.174 Next Work Selection Using Risk-Tiered Granularity']
FLAGS = ['current_state_and_priority_review_v06173_completed = true', 'current_state_and_priority_review_v06173_is_low_risk = true', 'current_state_and_priority_review_v06173_one_checkpoint = true', 'documentation_and_review_package_layer_status = implemented', 'safe_demo_layer_status = near_term_candidate', 'runtime_scanner_layer_status = deferred_pending_readiness_review', 'customer_poc_layer_status = deferred_pending_commercial_and_scope_boundaries', 'priority_p0_current_state_review = complete', 'priority_p1_current_state_executive_summary = recommended', 'priority_p1_public_demo_positioning = recommended', 'priority_p1_commercial_inquiry_response_boundary = recommended', 'priority_p2_runtime_scanner_implementation_readiness = deferred_but_visible', 'priority_p2_customer_poc_intake = deferred', 'priority_p2_aaef_main_contact_publication = deferred', 'recommended_next_work_item = current_state_executive_summary', 'recommended_next_work_item_risk_tier = medium', 'recommended_next_work_item_checkpoint_count = 2', 'recommended_next_checkpoint = v0.6.174 Next Work Selection Using Risk-Tiered Granularity', 'safe_demo_should_precede_real_scanner_execution = true', 'non_execution_demo_is_preferred_first_demo = true', 'local_only_mock_or_fixture_demo_is_preferred_initial_implementation = true', 'real_scanner_execution_is_not_selected_now = true', 'runtime_execution_is_not_selected_now = true', 'customer_poc_is_not_selected_now = true', 'aaef_main_contact_publication_remains_deferred = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_repository_modified = false', 'aaef_main_contact_publication_modified = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'customer_poc_authorized = false', 'commercial_contract_created = false', 'paid_engagement_approved = false', 'commercial_license_terms_created = false', 'customer_specific_material_created = false', 'validator_behavior_modified = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_behavior_modified = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'certification_claim_occurs = false', 'legal_compliance_claim_occurs = false', 'audit_opinion_claim_occurs = false', 'production_readiness_claim_occurs = false', 'external_framework_equivalence_claim_occurs = false', 'diagnostic_completeness_claim_occurs = false', 'third_party_testing_authorization_claim_occurs = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']
FORBIDDEN_DOC_PHRASES = ['real scanner execution is selected now', 'runtime execution is selected now', 'customer poc intake is selected now', 'customer poc is authorized', 'commercial contract is created', 'commercial license terms are created', 'paid engagement is approved', 'runtime execution is authorized', 'scanner execution is authorized', 'docker execution is authorized', 'credential injection is permitted', 'customer target is authorized', 'delivery is authorized', 'authorized to test third-party systems', 'permission to test third-party systems is granted', 'aaef main repository modified = true', 'aaef main handback sequence reopened = true', 'is certified as', 'certified framework for', 'legally compliant with', 'legal compliance achieved', 'audit opinion provided', 'deployment approved', 'is production ready', 'production-ready scanner', 'complete vulnerability scanner', 'equivalent to nist', 'equivalent to iso', 'ai can safely run tools without gates']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06172_DOC, V06170_DOC, V06167_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")

    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.173 document missing required text: {phrase}")

    v06172 = V06172_DOC.read_text(encoding="utf-8")
    for phrase in [
        "aaef_main_contact_reflection_deferral_decision_completed = true",
        "aaef_main_contact_reflection_deferred = true",
        "aaef_ai_va_interim_inquiry_route_continues = true",
        "selected_next_checkpoint = v0.6.173 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06172, f"v0.6.172 closeout missing required phrase: {phrase}")

    require("public_entry_and_inquiry_route_consistency_review_work_item_closed = true" in V06170_DOC.read_text(encoding="utf-8"), "v0.6.170 route consistency work item must remain closed")
    require("maintainer_inquiry_address_publication_work_item_closed = true" in V06167_DOC.read_text(encoding="utf-8"), "v0.6.167 inquiry address work item must remain closed")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    for phrase in ["risk_tiered_granularity_adopted = true", "Low risk", "Medium risk", "High risk", "Critical risk"]:
        require(phrase in v06120, f"v0.6.120 policy missing required phrase: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in ["aaef_main_handback_sequence_paused = true", "aaef_main_issue_opened = false", "aaef_main_pull_request_opened = false"]:
        require(phrase in v06119, f"v0.6.119 closeout missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in FORBIDDEN_DOC_PHRASES:
        require(phrase not in lower_doc, f"v0.6.173 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.173 Current State and Priority Review tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
