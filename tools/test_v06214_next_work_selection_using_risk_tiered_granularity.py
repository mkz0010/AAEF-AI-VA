from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/290-v06214-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0284-add-v06214-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0283-add-v06214-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = mock_dry_run_completed_status_terminology_cleanup",
    "selected_next_work_item_risk_tier = high",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.215 Mock/Dry-run Completed Status Terminology Cleanup Candidate",
    "selected_followup_checkpoint = v0.6.216 Mock/Dry-run Completed Status Terminology Cleanup Review and Decision",
]


REQUIRED_BOUNDARY_TOKENS = [
    "v0.6.214 does not",
    "rename execution statuses",
    "Tool Gateway behavior",
    "adapter behavior",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.214",
    "Next Work Selection Using Risk-Tiered Granularity",
    "mock_dry_run_completed_status_terminology_cleanup",
    "v0.6.215 Mock/Dry-run Completed Status Terminology Cleanup Candidate",
    "v0.6.216 Mock/Dry-run Completed Status Terminology Cleanup Review and Decision",
    "execution statuses are not renamed in v0.6.214",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "gateway_core_safety_controls_implemented = true",
    "tool_gateway_behavior_changed = true",
    "adapter_behavior_changed = true",
    "execution_status_renamed = true",
    "schema_changed = true",
    "validator_behavior_changed = true",
    "fixture_semantics_changed = true",
    "runtime_behavior_changed = true",
    "scanner_behavior_changed = true",
    "runtime_demo_ready = true",
    "scanner_readiness_claim = true",
    "external_poc_readiness_claim = true",
    "publication_approval = true",
    "public_announcement = approved",
    "social_post_publication = approved",
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


def test_v06214_files_exist_and_record_selection() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS)


def test_v06214_repository_surfaces_selection() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


# v0.6.356 scope note: README/CHANGELOG/ROADMAP are rolling aggregate files; historical planning-only forbidden-token checks must stay scoped to that checkpoint's own artifacts.
def test_v06214_does_not_apply_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06214_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06214_next_work_selection_using_risk_tiered_granularity.py" in run_all


if __name__ == "__main__":
    test_v06214_files_exist_and_record_selection()
    test_v06214_repository_surfaces_selection()
    test_v06214_does_not_apply_gateway_runtime_publication_or_assurance_changes()
    test_v06214_run_all_registers_local_test()
    print("v0.6.214 next work selection using risk-tiered granularity checks passed")
