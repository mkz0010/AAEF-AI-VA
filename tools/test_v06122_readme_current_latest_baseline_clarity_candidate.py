from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/198-v06122-readme-current-latest-baseline-clarity-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0192-add-v06122-readme-current-latest-baseline-clarity-candidate.md"
ISSUE = ROOT / "planning/issues/0191-add-v06122-readme-current-latest-baseline-clarity-candidate.md"
README = ROOT / "README.md"
V06121_DOC = ROOT / "docs/197-v06121-next-direction-selection-using-risk-tiered-granularity.md"
V06120_DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['readme_current_latest_baseline_clarity_candidate_completed = true', 'readme_current_latest_baseline_clarity_candidate_is_medium_risk = true', 'readme_current_latest_baseline_clarity_candidate_checkpoint_1_of_2 = true', 'readme_current_latest_baseline_clarity_review_decision_deferred_to_v06123 = true', 'readme_current_latest_baseline_clarity_candidate_added_readme_section = true', 'readme_current_latest_baseline_clarity_candidate_documentation_only = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'security_reporting_channel_updated = false', 'authorization_expiry_now_check_added = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.123 README Current/Latest Baseline Clarity Review and Decision']
REQUIRED_README_PHRASES = ['## Current repository checkpoint and baseline interpretation', 'The latest tagged AAEF-AI-VA checkpoint describes the current repository state for this applied implementation.', "This repository's latest checkpoint is not an AAEF main active control or assessment baseline.", 'AAEF-AI-VA is an applied implementation and reference boundary demonstration.', 'not a production vulnerability scanner', 'certification scheme', 'legal compliance claim', 'audit opinion', 'conformity assessment', 'diagnostic completeness claim', 'external-framework equivalence claim', 'Such a tag does not by itself change AAEF main', 'authorize testing against third-party systems', 'authorize runtime/scanner/Docker/credential/customer/delivery activity', 'current tagged repository checkpoint for this applied implementation']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, README, V06121_DOC, V06120_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    readme_text = README.read_text(encoding="utf-8")

    for phrase in FLAGS + [
        "Status: candidate",
        "This is checkpoint 1 of 2 for a Medium-risk public-facing documentation change.",
        "The review and decision are deferred to v0.6.123.",
        "Current repository checkpoint and baseline interpretation",
        "What did not happen",
        "v0.6.123 README Current/Latest Baseline Clarity Review and Decision",
    ]:
        require(phrase in doc_text, f"v0.6.122 document missing required text: {phrase}")

    for phrase in REQUIRED_README_PHRASES:
        require(phrase in readme_text, f"README missing v0.6.122 clarity phrase: {phrase}")

    require(readme_text.count("## Current repository checkpoint and baseline interpretation") == 1, "README clarity section must appear exactly once")

    v06121 = V06121_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = readme_current_latest_baseline_clarity",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.122 README Current/Latest Baseline Clarity Candidate",
    ]:
        require(phrase in v06121, f"v0.6.121 baseline missing required phrase: {phrase}")

    v06120 = V06120_DOC.read_text(encoding="utf-8")
    require("risk_tiered_granularity_adopted = true" in v06120, "v0.6.120 risk-tiered policy must exist")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_readme = readme_text.lower()
    for phrase in [
        "aaef-ai-va is a production vulnerability scanner",
        "aaef-ai-va is certified",
        "aaef-ai-va provides legal compliance",
        "aaef-ai-va provides an audit opinion",
        "aaef-ai-va is equivalent to",
        "this repository authorizes testing against third-party systems",
        "this tag authorizes runtime execution",
    ]:
        require(phrase not in lower_readme, f"README must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.122 README current/latest baseline clarity candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
