from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/345-v06270-narrower-manual-trace-review.md"
ADR = ROOT / "planning/decisions/ADR-0345-add-v06270-narrower-manual-trace-review.md"
ISSUE = ROOT / "planning/issues/0345-add-v06270-narrower-manual-trace-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

CORE_TOKENS = [
    "narrower_manual_trace_review_performed = true",
    "narrower_manual_trace_review_completed = true",
    "narrower_manual_trace_review_id = narrower_manual_trace_review_v06270",
    "manual_trace_review_records_created = true",
    "narrower_manual_trace_review_records_created = true",
    "manual_trace_review_results_created = true",
    "manual_trace_review_dispositions_created = true",
    "manual_trace_review_conclusions_created = false",
    "manual_trace_review_report_findings_created = false",
    "implementation_change_required_count = 0",
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
]

REVIEW_TOKENS = [
    "manual_trace_review_records != accepted_defect_records",
    "manual_trace_review_results != code_inspection_report",
    "manual_trace_review_dispositions != report_findings",
    "manual_trace_review_gap_triage != accepted_defect_records",
    "manual_trace_review_follow_up_trace_candidates != implementation_changes",
    "manual_trace_review_questions != manual_trace_review_conclusions",
    "manual_trace_review_scope != accepted_defect_scope",
    "manual trace review records are not accepted defects",
    "manual trace review results are not report findings",
    "manual trace review dispositions are not implementation changes",
    "recommended_next_work_item = narrower_manual_trace_review_review_and_decision",
    "v0.6.271 Narrower Manual Trace Review Review and Decision",
]

SCOPE_TOKENS = [
    "source_file_observation_records",
    "source_symbol_observation_records",
    "call_path_status_records",
    "symbol_trace_records",
    "trace_record_schema",
    "trace_status_vocabulary",
    "gap_records",
    "recommended_next_action_records",
    "verification_required statuses",
    "lane_01_pre_dispatch_enforcement_review",
    "lane_06_claim_boundary_review",
    "manual_trace_review_scope",
    "manual_trace_review_gap_triage",
    "accepted defect candidate planning",
    "code-inspection report candidate",
    "gateway-path integration verification report candidate",
]

BOUNDARY_TOKENS = [
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "validator success is structural only",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06270_doc_tokens() -> None:
    assert_tokens(DOC, CORE_TOKENS + REVIEW_TOKENS + SCOPE_TOKENS + BOUNDARY_TOKENS)


def test_v06270_adr_tokens() -> None:
    assert_tokens(ADR, CORE_TOKENS + [
        "ADR-0345",
        "Status: accepted",
        "Perform the narrower manual trace review",
        "Manual trace review records are not accepted defects.",
        "Manual trace review results are not report findings.",
        "Manual trace review dispositions are not implementation changes.",
        "No private generated outputs are moved public in v0.6.270.",
    ])


def test_v06270_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0345 - Add v0.6.270 Narrower Manual Trace Review",
        "Status: completed by v0.6.270",
        "narrower_manual_trace_review_performed = true",
        "manual_trace_review_records_created = true",
        "manual_trace_review_conclusions_created = false",
        "accepted_defect_records_created = false",
        "Proceed to v0.6.271 Narrower Manual Trace Review Review and Decision",
    ])


def test_v06270_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.270 Narrower Manual Trace Review",
        "narrower_manual_trace_review_performed = true",
        "manual_trace_review_records_created = true",
        "manual_trace_review_results_created = true",
        "manual_trace_review_conclusions_created = false",
        "accepted_defect_records_created = false",
        "code_inspection_report_created = false",
        "gateway_path_integration_verification_report_created = false",
        "Manual trace review records are not accepted defects.",
        "Manual trace review results are not report findings.",
        "Manual trace review dispositions are not implementation changes.",
        "No private generated outputs are moved public in v0.6.270.",
        "manual_trace_review_scope",
        "manual_trace_review_gap_triage",
        "readme_front_page_rewritten = false",
        "repository_metadata_changed = false",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.270 - Narrower Manual Trace Review",
        "Performed the first narrower manual trace review.",
        "narrower_manual_trace_review_performed = true",
        "manual_trace_review_conclusions_created = false",
        "accepted_defect_records_created = false",
        "manual trace review records are not accepted defects",
        "manual trace review results are not report findings",
        "manual trace review dispositions are not implementation changes",
        "validator success is structural only",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.270",
        "v0.6.271 Narrower Manual Trace Review Review and Decision",
        "no manual trace review conclusions",
        "no accepted defect records",
        "no code-inspection report",
        "no gateway-path integration verification report",
        "no gateway behavior change",
        "no adapter behavior change",
        "no schema behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])


def test_v06270_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06270_narrower_manual_trace_review.py"])


def main() -> None:
    test_v06270_doc_tokens()
    test_v06270_adr_tokens()
    test_v06270_issue_tokens()
    test_v06270_index_tokens()
    test_v06270_registered_in_run_all()
    print("v0.6.270 narrower manual trace review checks passed")


if __name__ == "__main__":
    main()
