from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/201-v06125-security-reporting-channel-consistency-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0195-add-v06125-security-reporting-channel-consistency-candidate.md"
ISSUE = ROOT / "planning/issues/0194-add-v06125-security-reporting-channel-consistency-candidate.md"
SECURITY = ROOT / "SECURITY.md"
V06124_DOC = ROOT / "docs/200-v06124-next-work-selection-using-risk-tiered-granularity.md"
V06123_DOC = ROOT / "docs/199-v06123-readme-current-latest-baseline-clarity-review-and-decision.md"
V06119_DOC = ROOT / "docs/195-v06119-narrow-public-safe-aaef-main-handback-pause-and-current-state-closeout-review.md"

FLAGS = ['security_reporting_channel_consistency_candidate_completed = true', 'security_reporting_channel_consistency_candidate_is_medium_risk = true', 'security_reporting_channel_consistency_candidate_checkpoint_1_of_2 = true', 'security_reporting_channel_consistency_review_decision_deferred_to_v06126 = true', 'security_reporting_channel_consistency_candidate_added_security_section = true', 'security_reporting_channel_consistency_candidate_public_facing = true', 'security_reporting_channel_consistency_candidate_documentation_only = true', 'security_reporting_channel_consistency_candidate_not_final_review = true', 'security_reporting_channel_consistency_candidate_not_closeout = true', 'security_reporting_channel_consistency_private_reporting_when_available = true', 'security_reporting_channel_consistency_public_issue_non_sensitive_only = true', 'security_reporting_channel_consistency_no_third_party_testing_authorization = true', 'security_reporting_channel_consistency_no_public_secrets_or_scanner_output = true', 'security_reporting_channel_consistency_commercial_contact_separated = true', 'aaef_main_handback_sequence_remains_paused = true', 'aaef_main_handback_sequence_reopened = false', 'aaef_main_issue_opened = false', 'aaef_main_pull_request_opened = false', 'aaef_main_issue_submission_command_generated = false', 'aaef_main_issue_url_generated = false', 'readme_current_latest_baseline_clarity_work_item_closed = true', 'authorization_expiry_now_check_added = false', 'constraint_diff_enforcement_added = false', 'external_discovery_fail_closed_added = false', 'mock_completed_status_renamed = false', 'enterprise_review_guide_created = false', 'technical_due_diligence_summary_created = false', 'safe_poc_boundary_template_created = false', 'control_matrix_created = false', 'reviewer_walkthrough_created = false', 'validator_behavior_modified = false', 'metadata_level_expected_failure_category_added = false', 'json_schema_added = false', 'public_sample_changed = false', 'runtime_execution_authorized = false', 'scanner_execution_authorized = false', 'docker_execution_authorized = false', 'credential_injection_permitted = false', 'customer_target_authorized = false', 'delivery_authorized = false', 'aaef_core_promotion = false', 'aaef_profile_promotion = false', 'aaef_practical_package_promotion = false', 'selected_next_checkpoint = v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision']
REQUIRED_DOC_PHRASES = ['Status: candidate', 'This is checkpoint 1 of 2 for a Medium-risk public-facing documentation change.', 'This checkpoint prepares the SECURITY.md reporting-channel consistency candidate.', 'The review and decision are deferred to v0.6.126.', 'SECURITY.md reporting-channel consistency candidate', 'Reporting channel and scope clarification', 'Use GitHub Security Advisories / private vulnerability reporting for sensitive reports about this repository when that channel is available.', 'open a public GitHub issue only for non-sensitive coordination', 'do not include exploit details, secrets, credentials, target-specific data, private customer material, scanner output, or other sensitive information', 'should concern the AAEF-AI-VA implementation, documentation, examples, release process, or repository configuration', 'This repository is not an authorization to test third-party systems.', 'Do not submit live third-party vulnerability details', 'not a production vulnerability scanner', 'not a managed vulnerability disclosure program', 'not a bug bounty program', 'not an emergency response service', 'not a certification scheme', 'not a legal compliance claim', 'not an audit opinion', 'not an authorization service', 'commercial licensing, paid evaluation, or NDA-based adoption discussions', 'What did not happen', 'Next checkpoint', 'v0.6.126 SECURITY.md Reporting-Channel Consistency Review and Decision']
REQUIRED_SECURITY_PHRASES = ['## Reporting channel and scope clarification', 'Use GitHub Security Advisories / private vulnerability reporting for sensitive reports about this repository when that channel is available.', 'open a public GitHub issue only for non-sensitive coordination', 'do not include exploit details, secrets, credentials, target-specific data, private customer material, scanner output, or other sensitive information', 'Security reports for this repository should concern the AAEF-AI-VA implementation, documentation, examples, release process, or repository configuration.', 'This repository is not an authorization to test third-party systems.', 'Do not use this repository, its examples, or its documentation as permission to scan, attack, probe, exploit, or otherwise test systems', 'Do not submit live third-party vulnerability details', 'credentials, tokens, private scan output, exploit chains, or operationally sensitive diagnostics', 'It is not a production vulnerability scanner', 'not a managed vulnerability disclosure program', 'not a bug bounty program', 'not an emergency response service', 'not a certification scheme', 'not a legal compliance claim', 'not an audit opinion', 'not an authorization service', 'commercial licensing, paid evaluation, or NDA-based adoption discussions', 'rather than the vulnerability reporting channel']

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> int:
    for path in [DOC, ADR, ISSUE, SECURITY, V06124_DOC, V06123_DOC, V06119_DOC]:
        require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")

    doc_text = DOC.read_text(encoding="utf-8")
    security_text = SECURITY.read_text(encoding="utf-8")

    for phrase in REQUIRED_DOC_PHRASES + FLAGS:
        require(phrase in doc_text, f"v0.6.125 document missing required text: {phrase}")

    for phrase in REQUIRED_SECURITY_PHRASES:
        require(phrase in security_text, f"SECURITY.md missing v0.6.125 reporting-channel phrase: {phrase}")

    require(security_text.count("## Reporting channel and scope clarification") == 1, "SECURITY.md reporting channel section must appear exactly once")

    v06124 = V06124_DOC.read_text(encoding="utf-8")
    for phrase in [
        "selected_next_work_item = security_reporting_channel_consistency",
        "selected_next_work_item_risk_tier = medium",
        "selected_next_work_item_checkpoint_count = 2",
        "selected_next_checkpoint = v0.6.125 SECURITY.md Reporting-Channel Consistency Candidate",
    ]:
        require(phrase in v06124, f"v0.6.124 baseline missing required phrase: {phrase}")

    v06123 = V06123_DOC.read_text(encoding="utf-8")
    require("readme_current_latest_baseline_clarity_work_item_closed = true" in v06123, "v0.6.123 README clarity work item must be closed")

    v06119 = V06119_DOC.read_text(encoding="utf-8")
    require("aaef_main_handback_sequence_paused = true" in v06119, "v0.6.119 handback pause must remain recorded")

    lower_security = security_text.lower()
    for phrase in [
        "this repository authorizes testing against third-party systems",
        "this repository is a bug bounty program",
        "this repository is a managed vulnerability disclosure program",
        "this repository is a production vulnerability scanner",
        "send credentials in public issues",
        "post private scan output in public issues",
        "public issues are for sensitive reports",
    ]:
        require(phrase not in lower_security, f"SECURITY.md must not include affirmative forbidden phrase: {phrase}")

    print("v0.6.125 SECURITY.md reporting-channel consistency candidate tests passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
