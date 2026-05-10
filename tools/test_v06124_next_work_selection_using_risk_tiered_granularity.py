from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0194-add-v06124-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0193-add-v06124-next-work-selection-using-risk-tiered-granularity.md"
V06123_DOC = ROOT / "docs/199-v06123-readme-current-latest-baseline-clarity-review-and-decision.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED = ['Status: decision', 'This checkpoint applies the v0.6.120 risk-tiered checkpoint granularity policy.', 'This checkpoint is intentionally completed as one Low-risk checkpoint.', 'The selected next work item is SECURITY.md reporting-channel consistency.', 'The selected next work item risk tier is Medium risk.', 'The selected checkpoint count is 2 checkpoints.', 'The next checkpoint is v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate.', 'This checkpoint does not update SECURITY.md reporting-channel wording.', 'This checkpoint does not reopen the AAEF main handback sequence.', 'No AAEF main issue is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered selection record', 'Candidate work items reviewed', 'Selected work item', 'Why this is Medium risk', 'Why not High or Critical risk', 'Why not Low risk', 'Planned checkpoint split', 'What did not happen', 'Next direction']
FLAGS = ['next_work_selection_using_risk_tiered_granularity_completed = true', 'next_work_selection_is_documentation_only = true', 'next_work_selection_uses_v06120_granularity_policy = true', 'next_work_selection_uses_v06123_completed_work_item = true', 'v06124_completed_as_low_risk_one_checkpoint = true', 'selected_next_work_item = security_reporting_channel_consistency', 'selected_next_work_item_risk_tier = medium', 'selected_next_work_item_checkpoint_count = 2', 'selected_next_work_item_first_checkpoint = candidate_preparation', 'selected_next_work_item_second_checkpoint = review_and_decision', 'selected_next_checkpoint = v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate', 'security_reporting_channel_consistency_selected = true', 'readme_current_latest_baseline_clarity_selected = false', 'readme_current_latest_baseline_clarity_work_item_closed = true', 'authorization_expiry_now_check_selected = false', 'request_decision_constraint_diff_enforcement_selected = false', 'external_discovery_fail_closed_selected = false', 'mock_dry_run_completed_status_cleanup_selected = false', 'enterprise_review_guide_selected = false', 'technical_due_diligence_summary_selected = false', 'safe_poc_boundary_template_selected = false', 'control_matrix_selected = false', 'reviewer_walkthrough_selected = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'security_reporting_channel_updated = false', 'authorization_expiry_now_check_added = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, V06123_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED + FLAGS:
        require(phrase in doc_text, f"v0.6.124 document missing required text: {phrase}")

    v06123 = V06123_DOC.read_text(encoding="utf-8")
    for phrase in [
        "readme_current_latest_baseline_clarity_review_decision_completed = true",
        "readme_current_latest_baseline_clarity_candidate_accepted = true",
        "readme_current_latest_baseline_clarity_work_item_closed = true",
        "selected_next_checkpoint = v0.6.124 Next Work Selection Using Risk-Tiered Granularity",
    ]:
        require(phrase in v06123, f"v0.6.123 baseline missing required phrase: {phrase}")

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
        "this checkpoint updates security.md reporting-channel wording",
        "this checkpoint opens an aaef main issue",
        "this checkpoint submits to aaef main",
        "runtime execution is authorized by this checkpoint",
        "scanner execution is authorized by this checkpoint",
        "credential injection is permitted by this checkpoint",
    ]:
        require(phrase not in lower_doc, f"v0.6.124 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.124 next work selection using risk-tiered granularity tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
