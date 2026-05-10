from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/217-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0211-add-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0210-add-v06141-mock-dry-run-completed-status-terminology-cleanup-review-and-decision.md"
HELPER = ROOT / "tools/mock_dry_run_status_terminology.py"
HELPER_TEST = ROOT / "tools/test_mock_dry_run_completed_status_terminology.py"
V06140_DOC = ROOT / "docs/216-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md"
V06139_DOC = ROOT / "docs/215-v06139-next-work-selection-using-risk-tiered-granularity.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06134_DOC = ROOT / "docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md"
V06130_DOC = ROOT / "docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: decision', 'This is checkpoint 2 of 2 for a Medium-risk terminology and evidence-interpretation work item.', 'This checkpoint reviews and accepts the mock/dry-run `completed` status terminology cleanup candidate from v0.6.140.', 'The mock/dry-run `completed` status terminology cleanup work item is closed.', 'Review conclusion', 'Candidate accepted', 'Raw status compatibility confirmed', 'Reviewer-facing terminology confirmed', 'No-real-execution disambiguation confirmed', 'Evidence-safe result model confirmed', 'No raw status rename', 'No runtime behavior modification', 'No runtime execution authorization effect', 'No scanner execution authorization effect', 'No Docker execution authorization effect', 'No credential injection authorization effect', 'No customer target authorization effect', 'No delivery authorization effect', 'Reviewed candidate behavior', 'Reviewed helper and tests', 'Review checklist', 'Work item closeout', 'What did not happen', 'Next direction', 'v0.6.142 Next Work Selection Using Risk-Tiered Granularity']
FLAGS = ['mock_dry_run_completed_status_terminology_cleanup_review_decision_completed = true', 'mock_dry_run_completed_status_terminology_cleanup_review_decision_is_medium_risk = true', 'mock_dry_run_completed_status_terminology_cleanup_review_decision_checkpoint_2_of_2 = true', 'mock_dry_run_completed_status_terminology_cleanup_candidate_reviewed = true', 'mock_dry_run_completed_status_terminology_cleanup_candidate_accepted = true', 'mock_dry_run_completed_status_terminology_cleanup_work_item_closed = true', 'mock_dry_run_completed_status_terminology_helper_reviewed = true', 'mock_dry_run_completed_status_terminology_helper_tests_reviewed = true', 'mock_dry_run_completed_status_raw_status_preservation_confirmed = true', 'mock_dry_run_completed_status_reviewer_label_confirmed = true', 'mock_dry_run_completed_status_no_real_execution_label_confirmed = true', 'mock_dry_run_completed_status_ambiguous_context_review_confirmed = true', 'mock_dry_run_completed_status_non_completed_status_preservation_confirmed = true', 'mock_dry_run_completed_status_malformed_record_review_required_confirmed = true', 'mock_dry_run_completed_status_execution_blocked_marker_support_confirmed = true', 'mock_dry_run_completed_status_evidence_safe_result_confirmed = true', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'raw_completed_status_behavior_modified = false', 'runtime_status_contract_modified = false', 'runtime_behavior_modified = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = next_work_selection_using_risk_tiered_granularity', 'selected_next_checkpoint = v0.6.142 Next Work Selection Using Risk-Tiered Granularity']
REQUIRED_HELPER_PHRASES = ['def classify_mock_dry_run_completed_status(', 'class MockDryRunStatusTerminology', 'def as_evidence(', 'MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION', 'COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW', 'malformed_status_record_requires_review', 'raw_status_preserved', 'behavior_modified', 'execution_blocked', 'execution-blocked', 'real_execution', 'real-execution']
REQUIRED_HELPER_TEST_PHRASES = ['raw completed status must be preserved for dry_run', 'dry_run completed must get no-real-execution reviewer status', 'mock completed must get no-real-execution reviewer status', 'completed with real_execution_permitted false must get no-real-execution reviewer status', 'completed with execution-blocked note must get no-real-execution reviewer status', 'ambiguous completed must require context review', 'non-completed raw status must be preserved', 'malformed status record must require review', 'evidence should not include sensitive material']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06140_DOC, V06139_DOC, V06138_DOC, V06134_DOC, V06130_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.141 document missing required text: {phrase}")

    for phrase in REQUIRED_HELPER_PHRASES:
        require(phrase in helper_text, f"helper missing reviewed phrase: {phrase}")

    for phrase in REQUIRED_HELPER_TEST_PHRASES:
        require(phrase in helper_test_text, f"helper test missing reviewed phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from mock_dry_run_status_terminology import (
        COMPLETED,
        COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW,
        MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION,
        classify_mock_dry_run_completed_status,
    )

    dry_run = classify_mock_dry_run_completed_status({"status": "completed", "execution_mode": "dry_run"})
    require(dry_run.raw_status == COMPLETED, "dry-run raw completed status must be preserved")
    require(dry_run.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "dry-run reviewer status must disambiguate no real execution")
    require(dry_run.raw_status_preserved is True, "dry-run raw status preservation must be recorded")
    require(dry_run.behavior_modified is False, "dry-run terminology must not modify behavior")

    mock = classify_mock_dry_run_completed_status({"status": "completed", "mock": True})
    require(mock.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "mock completed reviewer status mismatch")

    blocked_note = classify_mock_dry_run_completed_status({"status": "completed", "status_reason": "candidate_recorded_execution_blocked"})
    require(blocked_note.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "execution_blocked marker must disambiguate no real execution")

    blocked_dash_note = classify_mock_dry_run_completed_status({"status": "completed", "reason": "candidate-recorded-execution-blocked"})
    require(blocked_dash_note.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "execution-blocked marker must disambiguate no real execution")

    real_execution_false = classify_mock_dry_run_completed_status({"status": "completed", "note": "real_execution false"})
    require(real_execution_false.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "real_execution false marker must disambiguate no real execution")

    ambiguous = classify_mock_dry_run_completed_status({"status": "completed"})
    require(ambiguous.raw_status == COMPLETED, "ambiguous raw completed status must be preserved")
    require(ambiguous.reviewer_status == COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW, "ambiguous completed must require context review")
    require(ambiguous.behavior_modified is False, "ambiguous terminology must not modify behavior")

    non_completed = classify_mock_dry_run_completed_status({"status": "blocked", "execution_mode": "dry_run"})
    require(non_completed.raw_status == "blocked", "non-completed raw status must be preserved")
    require(non_completed.reviewer_status == "blocked", "non-completed reviewer status must remain unchanged")
    require(non_completed.behavior_modified is False, "non-completed terminology must not modify behavior")

    malformed = classify_mock_dry_run_completed_status("not-a-record")
    require(malformed.reviewer_status == "malformed_status_record_requires_review", "malformed record must require review")
    require(malformed.behavior_modified is False, "malformed record terminology must not modify behavior")

    evidence = dry_run.as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["secret", "password", "token", "scanner_output", "customer", "credential"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")
    require(evidence["raw_status"] == "completed", "evidence must preserve raw_status")
    require(evidence["reviewer_status"] == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "evidence must include reviewer_status")
    require(evidence["raw_status_preserved"] is True, "evidence must record raw_status_preserved")
    require(evidence["behavior_modified"] is False, "evidence must record behavior_modified false")

    v06140 = V06140_DOC.read_text(encoding="utf-8")
    for phrase in [
        "mock_dry_run_completed_status_terminology_cleanup_candidate_completed = true",
        "mock_dry_run_completed_status_terminology_cleanup_candidate_checkpoint_1_of_2 = true",
        "mock_dry_run_completed_status_terminology_helper_added = true",
        "mock_dry_run_completed_status_terminology_helper_tests_added = true",
        "selected_next_checkpoint = v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision",
    ]:
        require(phrase in v06140, f"v0.6.140 candidate missing required phrase: {phrase}")

    v06139 = V06139_DOC.read_text(encoding="utf-8")
    require("selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup" in v06139, "v0.6.139 selection must remain recorded")
    require("selected_next_work_item_risk_tier = medium" in v06139, "v0.6.139 medium-risk selection must remain recorded")

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
        "runtime execution is authorized by this review",
        "scanner execution is authorized by this review",
        "credential injection is permitted by this review",
        "this review opens an aaef main issue",
        "this review submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.141 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.141 mock/dry-run completed status terminology cleanup review and decision tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
