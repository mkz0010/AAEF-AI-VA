from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/216-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0210-add-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md"
ISSUE = ROOT / "planning/issues/0209-add-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md"
HELPER = ROOT / "tools/mock_dry_run_status_terminology.py"
HELPER_TEST = ROOT / "tools/test_mock_dry_run_completed_status_terminology.py"
V06139_DOC = ROOT / "docs/215-v06139-next-work-selection-using-risk-tiered-granularity.md"
V06138_DOC = ROOT / "docs/214-v06138-external-discovery-fail-closed-behavior-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk terminology and evidence-interpretation work item.', 'This checkpoint implements the mock/dry-run `completed` status terminology cleanup candidate.', 'The review and decision are deferred to v0.6.141.', 'Candidate implementation summary', 'Candidate helper', 'Candidate behavior', 'Raw status compatibility', 'Evidence-safe result model', 'Candidate tests', 'What changed', 'What did not happen', 'Next checkpoint', 'v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision']
FLAGS = ['mock_dry_run_completed_status_terminology_cleanup_candidate_completed = true', 'mock_dry_run_completed_status_terminology_cleanup_candidate_is_medium_risk = true', 'mock_dry_run_completed_status_terminology_cleanup_candidate_checkpoint_1_of_2 = true', 'mock_dry_run_completed_status_terminology_cleanup_review_decision_deferred_to_v06141 = true', 'mock_dry_run_completed_status_terminology_helper_added = true', 'mock_dry_run_completed_status_terminology_helper_tests_added = true', 'mock_dry_run_completed_status_reviewer_label_added = true', 'mock_dry_run_completed_status_raw_status_preserved = true', 'mock_dry_run_completed_status_behavior_preserved = true', 'mock_dry_run_completed_status_no_real_execution_label_supported = true', 'mock_dry_run_completed_status_ambiguous_context_requires_review = true', 'mock_completed_status_renamed = false', 'mock_dry_run_status_behavior_modified = false', 'raw_completed_status_behavior_modified = false', 'runtime_status_contract_modified = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'review_decision_completed = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'external_discovery_fail_closed_added = false', 'constraint_diff_enforcement_added = false', 'authorization_expiry_now_check_added = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.141 Mock/Dry-Run Completed Status Terminology Cleanup Review and Decision']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, HELPER, HELPER_TEST, V06139_DOC, V06138_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    helper_text = HELPER.read_text(encoding="utf-8")
    helper_test_text = HELPER_TEST.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.140 document missing required text: {phrase}")

    for phrase in [
        "def classify_mock_dry_run_completed_status(",
        "class MockDryRunStatusTerminology",
        "def as_evidence(",
        "mock_dry_run_completed_no_real_execution",
        "completed_context_unclassified_requires_review",
        "malformed_status_record_requires_review",
        "raw_status_preserved",
        "behavior_modified",
    ]:
        require(phrase in helper_text, f"helper missing required implementation phrase: {phrase}")

    for phrase in [
        "raw completed status must be preserved for dry_run",
        "dry_run completed must get no-real-execution reviewer status",
        "mock completed must get no-real-execution reviewer status",
        "completed with real_execution_permitted false must get no-real-execution reviewer status",
        "completed with execution-blocked note must get no-real-execution reviewer status",
        "ambiguous completed must require context review",
        "non-completed raw status must be preserved",
        "malformed status record must require review",
        "evidence should not include sensitive material",
    ]:
        require(phrase in helper_test_text, f"helper test missing required case phrase: {phrase}")

    import sys
    sys.path.insert(0, str(ROOT / "tools"))
    from mock_dry_run_status_terminology import classify_mock_dry_run_completed_status

    dry_run = classify_mock_dry_run_completed_status({"status": "completed", "execution_mode": "dry_run"})
    require(dry_run.raw_status == "completed", "dry-run raw status must remain completed")
    require(dry_run.reviewer_status == "mock_dry_run_completed_no_real_execution", "dry-run reviewer status mismatch")
    require(dry_run.behavior_modified is False, "dry-run terminology must not modify behavior")

    ambiguous = classify_mock_dry_run_completed_status({"status": "completed"})
    require(ambiguous.raw_status == "completed", "ambiguous raw status must remain completed")
    require(ambiguous.reviewer_status == "completed_context_unclassified_requires_review", "ambiguous completed reviewer status mismatch")
    require(ambiguous.behavior_modified is False, "ambiguous terminology must not modify behavior")

    blocked = classify_mock_dry_run_completed_status({"status": "blocked", "execution_mode": "dry_run"})
    require(blocked.reviewer_status == "blocked", "blocked status should remain unchanged")

    evidence = dry_run.as_evidence()
    evidence_text = str(evidence).lower()
    for term in ["secret", "password", "token", "scanner_output", "customer", "credential"]:
        require(term not in evidence_text, f"evidence output contains forbidden sensitive/raw term: {term}")

    v06139 = V06139_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.140 Mock/Dry-Run Completed Status Terminology Cleanup Candidate",
        "mock_completed_status_renamed = false",
        "mock_dry_run_status_behavior_modified = false",
    ]:
        require(phrase in v06139, f"v0.6.139 selection missing required phrase: {phrase}")

    v06138 = V06138_DOC.read_text(encoding="utf-8")
    require("external_discovery_fail_closed_behavior_work_item_closed = true" in v06138, "v0.6.138 external discovery work item must remain closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_doc = doc_text.lower()
    for phrase in [
        "runtime execution is authorized by this candidate",
        "scanner execution is authorized by this candidate",
        "credential injection is permitted by this candidate",
        "this candidate opens an aaef main issue",
        "this candidate submits to aaef main",
    ]:
        require(phrase not in lower_doc, f"v0.6.140 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.140 mock/dry-run completed status terminology cleanup candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
