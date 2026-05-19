from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/294-v06218-aaef-applied-evidence-minimum-flow-intake-priority-reconciliation.md"
ADR = ROOT / "planning/decisions/ADR-0288-add-v06218-aaef-applied-evidence-minimum-flow-intake-priority-reconciliation.md"
ISSUE = ROOT / "planning/issues/0287-add-v06218-aaef-applied-evidence-minimum-flow-intake-priority-reconciliation.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = aaef_applied_evidence_minimum_flow_plan",
    "selected_next_work_item_risk_tier = high",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate",
    "selected_followup_checkpoint = v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision",
]


REQUIRED_DEFERRED_TOKENS = [
    "deferred_work_item = public_exposure_cleanup_work",
    "deferred_reason = aaef_main_applied_evidence_minimum_flow_priority",
    "deferred_return_condition = aaef_applied_evidence_minimum_flow_plan_reviewed_and_decided",
    "deferred_work_item = mock_dry_run_completed_status_terminology_cleanup",
]


REQUIRED_FLOW_TOKENS = [
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Scenario matrix required",
    "permitted safe diagnostic",
    "denied out-of-scope request",
    "held / requires human approval",
    "expired-not-executed",
    "Evidence linkage table required",
    "AAEF five questions mapping required",
    "Evidence trust boundary required",
    "Handback summary requirement",
    "Public/private/patent-sensitive boundary retained",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.218",
    "AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation",
    "aaef_applied_evidence_minimum_flow_plan",
    "v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate",
    "v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision",
    "public exposure cleanup is deferred, not rejected",
    "mock/dry-run completed status terminology cleanup is deferred, not rejected",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "minimum_flow_package_created = true",
    "fixtures_created = true",
    "fixtures_modified = true",
    "reviewer_walkthrough_created = true",
    "aaef_handback_summary_created = true",
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


def test_v06218_files_exist_and_record_intake() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(DOC, REQUIRED_DEFERRED_TOKENS)
    assert_contains_all(DOC, REQUIRED_FLOW_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_DEFERRED_TOKENS)


def test_v06218_repository_surfaces_intake() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


# v0.6.356 scope note: README/CHANGELOG/ROADMAP are rolling aggregate files; historical forbidden-token checks stay scoped to checkpoint-local artifacts.
def test_v06218_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06218_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06218_aaef_applied_evidence_minimum_flow_intake_priority_reconciliation.py" in run_all


if __name__ == "__main__":
    test_v06218_files_exist_and_record_intake()
    test_v06218_repository_surfaces_intake()
    test_v06218_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06218_run_all_registers_local_test()
    print("v0.6.218 AAEF Applied Evidence Minimum Flow Intake and Priority Reconciliation checks passed")
