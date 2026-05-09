from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/196-v06120-checkpoint-granularity-policy-decision-record.md"
ADR = ROOT / "planning/decisions/ADR-0190-add-v06120-checkpoint-granularity-policy-decision-record.md"
ISSUE = ROOT / "planning/issues/0189-add-v06120-checkpoint-granularity-policy-decision-record.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

REQUIRED_POLICY_PHRASES = ['Status: decision', 'This checkpoint is intentionally completed as one checkpoint.', 'This is the first application of the new risk-tiered checkpoint granularity policy.', 'Low-risk operational policy decisions should normally complete in one checkpoint.', 'The previous planning -> candidate -> review -> close-readiness -> decision pattern is no longer the default.', 'That expanded pattern remains available for critical-risk work.', 'Existing checkpoints are not retroactively rewritten.', 'Existing tags are not rewritten.', 'Existing release history is not collapsed.', 'No AAEF main issue is opened.', 'No AAEF main pull request is opened.', 'No issue creation command is generated.', 'No issue URL is created.', 'Risk-tiered checkpoint granularity policy', 'Low risk', 'Medium risk', 'High risk', 'Critical risk', '1 checkpoint', '2 checkpoints', '3 checkpoints', '4-5 checkpoints', 'Default rule', 'Escalation rule', 'De-escalation rule', 'What did not happen', 'Next direction', 'v0.6.121']
POLICY_FLAGS = ['checkpoint_granularity_policy_decision_record_completed = true', 'checkpoint_granularity_policy_is_documentation_only = true', 'checkpoint_granularity_policy_adopted = true', 'risk_tiered_granularity_adopted = true', 'single_checkpoint_application_demonstrated = true', 'low_risk_policy_decision_completed_in_one_checkpoint = true', 'planning_candidate_review_close_readiness_decision_chain_not_used = true', 'expanded_checkpoint_pattern_no_longer_default = true', 'expanded_checkpoint_pattern_retained_for_critical_risk = true', 'existing_checkpoints_retroactively_modified = false', 'existing_tags_rewritten = false', 'existing_release_history_collapsed = false', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_direction = apply_risk_tiered_granularity_to_future_work_selection']


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    for path in [DOC, ADR, ISSUE, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    for phrase in REQUIRED_POLICY_PHRASES + POLICY_FLAGS:
        require(phrase in doc_text, f"v0.6.120 document missing required text: {phrase}")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    for phrase in [
        "aaef_main_handback_sequence_paused = true",
        "aaef_main_handback_sequence_closed_for_now = true",
        "selected_next_step_after_pause_and_current_state_closeout_review = none_for_this_handback_sequence_until_human_maintainer_reopens",
        "aaef_main_issue_opened = false",
        "aaef_main_pull_request_opened = false",
        "aaef_main_issue_submission_command_generated = false",
        "aaef_main_issue_url_generated = false",
        "validator_behavior_modified = false",
    ]:
        require(phrase in v06119, f"v0.6.119 baseline missing required phrase: {phrase}")

    lower_doc = doc_text.lower()
    for phrase in [
        "this policy opens an aaef main issue",
        "this policy submits to aaef main",
        "runtime execution is authorized by this policy",
        "scanner execution is authorized by this policy",
        "credential injection is permitted by this policy",
        "this policy rewrites existing tags",
        "this policy collapses existing release history",
    ]:
        require(phrase not in lower_doc, f"v0.6.120 document must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.120 checkpoint granularity policy decision record tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
