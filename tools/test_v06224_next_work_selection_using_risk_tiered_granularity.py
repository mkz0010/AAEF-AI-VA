from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/300-v06224-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0294-add-v06224-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0293-add-v06224-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = minimum_flow_scenario_matrix",
    "selected_next_work_item_risk_tier = high",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.225 Minimum Flow Scenario Matrix Candidate",
    "selected_followup_checkpoint = v0.6.226 Minimum Flow Scenario Matrix Review and Decision",
]


REQUIRED_SCOPE_TOKENS = [
    "Required v0.6.225 candidate scope",
    "permitted safe diagnostic",
    "denied out-of-scope request",
    "held / requires human approval",
    "expired-not-executed",
    "Required v0.6.225 minimum flow coverage",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Required v0.6.225 scenario expectations",
    "Required v0.6.225 linkage planning",
    "Required v0.6.225 evidence-boundary review",
    "Required v0.6.225 public/private boundary review",
]


REQUIRED_DEFERRED_TOKENS = [
    "deferred_work_item = public_exposure_cleanup_work",
    "deferred_reason = aaef_applied_evidence_minimum_flow_work_in_progress",
    "deferred_return_condition = aaef_applied_evidence_minimum_flow_track_reviewed_or_explicitly_paused",
    "deferred_work_item = mock_dry_run_completed_status_terminology_cleanup",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.224",
    "Next Work Selection Using Risk-Tiered Granularity",
    "minimum_flow_scenario_matrix",
    "v0.6.225 Minimum Flow Scenario Matrix Candidate",
    "v0.6.226 Minimum Flow Scenario Matrix Review and Decision",
    "no minimum flow scenario matrix is created in v0.6.224",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "minimum_flow_scenario_matrix_created = true",
    "minimum_flow_package_created = true",
    "fixtures_created = true",
    "fixtures_modified = true",
    "evidence_linkage_records_created = true",
    "tool_action_request_records_created = true",
    "gate_decision_records_created = true",
    "dispatch_evidence_records_created = true",
    "reviewer_walkthrough_created = true",
    "aaef_five_questions_mapping_created = true",
    "aaef_handback_summary_created = true",
    "private_generated_outputs_moved_public = true",
    "public_exposure_cleanup_applied = true",
    "readme_front_page_rewritten = true",
    "gateway_core_safety_controls_implemented = true",
    "tool_gateway_behavior_changed = true",
    "adapter_behavior_changed = true",
    "execution_status_renamed = true",
    "runtime_demo_ready = true",
    "scanner_readiness_claim = true",
    "external_poc_readiness_claim = true",
    "publication_approval = true",
    "public_announcement = approved",
    "social_post_publication = approved",
    "commercial_terms_created = true",
    "production_readiness_claim = true",
    "certification_claim = true",
    "legal_compliance_claim = true",
    "audit_opinion_claim = true",
    "diagnostic_completeness_claim = true",
    "external_framework_equivalence_claim = true",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06224_files_exist_and_record_selection() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(DOC, REQUIRED_SCOPE_TOKENS)
    assert_contains_all(DOC, REQUIRED_DEFERRED_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_DEFERRED_TOKENS)


def test_v06224_repository_surfaces_selection() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06224_does_not_apply_matrix_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06224_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06224_next_work_selection_using_risk_tiered_granularity.py" in run_all


if __name__ == "__main__":
    test_v06224_files_exist_and_record_selection()
    test_v06224_repository_surfaces_selection()
    test_v06224_does_not_apply_matrix_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06224_run_all_registers_local_test()
    print("v0.6.224 Next Work Selection Using Risk-Tiered Granularity checks passed")
