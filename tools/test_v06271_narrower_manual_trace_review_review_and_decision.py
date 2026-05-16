from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/346-v06271-narrower-manual-trace-review-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0346-add-v06271-narrower-manual-trace-review-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0346-add-v06271-narrower-manual-trace-review-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = [
    "narrower_manual_trace_review_review_completed = true",
    "narrower_manual_trace_review_accepted = true",
    "narrower_manual_trace_review_id = narrower_manual_trace_review_v06270",
    "narrower_manual_trace_review_review_result = accepted_as_non_claim_manual_review_records_for_follow_up_trace_planning",
    "manual_trace_review_records_accepted = true",
    "manual_trace_review_results_accepted = true",
    "manual_trace_review_dispositions_accepted = true",
    "manual_trace_review_gap_triage_accepted = true",
    "manual_trace_review_follow_up_trace_candidates_accepted = true",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
    "recommended_next_work_item = manual_trace_review_follow_up_trace_candidate",
    "manual_trace_review_follow_up_trace_candidate_recommended = true",
    "accepted_defect_records_created = false",
    "code_inspection_report_created = false",
    "gateway_path_integration_verification_report_created = false",
    "gateway_execution_path_behavior_modified = false",
    "tool_gateway_behavior_changed = false",
    "adapter_behavior_changed = false",
    "schema_changed = false",
    "runtime_behavior_changed = false",
    "scanner_behavior_changed = false",
    "readme_front_page_rewritten = false",
    "repository_metadata_changed = false",
    "publication_approval = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]

REQUIRED_SHARED_TOKENS = [
    "manual_trace_review_records",
    "manual_trace_review_results",
    "manual_trace_review_dispositions",
    "manual_trace_review_gap_triage",
    "manual_trace_review_follow_up_trace_candidates",
    "manual_trace_review_scope",
    "manual_trace_review_rationale",
    "manual_trace_review_disposition",
    "manual_trace_review_follow_up_trace_candidate",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
    "Manual trace review records are not accepted defects.",
    "Manual trace review results are not report findings.",
    "Manual trace review dispositions are not implementation changes.",
    "No private generated outputs are moved public in v0.6.271.",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06271_doc_tokens() -> None:
    assert_tokens(
        DOC,
        [
            "v0.6.271 Narrower Manual Trace Review Review and Decision",
            "Previous checkpoint: v0.6.270 Narrower Manual Trace Review",
            "Decision result: accepted as non-claim manual review records for follow-up trace planning",
            "v0.6.272 Next Work Selection Using Risk-Tiered Granularity",
            "Model output is not authority.",
            "AI rationale is not authorization.",
            "A gate decision is not AI self-approval.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "validator success is structural only",
            "runtime demo remains necessary but deferred",
            "publication remains deferred",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06271_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0346",
            "Status: accepted",
            "Accept the v0.6.270 Narrower Manual Trace Review as non-claim manual review records",
        ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS,
    )


def test_v06271_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0346 - Add v0.6.271 Narrower Manual Trace Review Review and Decision",
            "Status: completed by v0.6.271",
            "narrower_manual_trace_review_review_completed = true",
            "manual_trace_review_follow_up_trace_candidates_accepted = true",
            "Proceed to v0.6.272 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06271_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.271 Narrower Manual Trace Review Review and Decision",
            "narrower_manual_trace_review_review_completed = true",
            "manual_trace_review_follow_up_trace_candidates_accepted = true",
            "recommended_next_work_item = manual_trace_review_follow_up_trace_candidate",
            "accepted_defect_records_created = false",
            "code_inspection_report_created = false",
            "gateway_path_integration_verification_report_created = false",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.271 - Narrower Manual Trace Review Review and Decision",
            "Accepted the v0.6.270 Narrower Manual Trace Review as non-claim manual review records",
            "recommended_next_work_item = manual_trace_review_follow_up_trace_candidate",
            "validator success is structural only",
        ] + REQUIRED_SHARED_TOKENS,
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.271",
            "v0.6.272 Next Work Selection Using Risk-Tiered Granularity",
            "manual_trace_review_follow_up_trace_candidate",
            "accepted defect candidate planning",
            "code-inspection report candidate",
            "gateway-path integration verification report candidate",
            "no manual trace review conclusions",
            "no accepted defect records",
            "no code-inspection report",
            "no gateway-path integration verification report",
            "no gateway behavior change",
        ],
    )


def test_v06271_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06271_narrower_manual_trace_review_review_and_decision.py"])


def main() -> None:
    test_v06271_doc_tokens()
    test_v06271_adr_tokens()
    test_v06271_issue_tokens()
    test_v06271_index_tokens()
    test_v06271_registered_in_run_all()
    print("v0.6.271 narrower manual trace review review and decision checks passed")


if __name__ == "__main__":
    main()
