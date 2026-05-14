from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/281-v06205-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0275-add-v06205-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0274-add-v06205-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = static_fixture_review_path_repository_wording_integration_plan",
    "selected_next_work_item_risk_tier = medium",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate",
    "selected_followup_checkpoint = v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision",
    "v0.6.205 does not create the repository wording integration plan body",
    "publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.205",
    "static_fixture_review_path_repository_wording_integration_plan",
    "v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate",
    "v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "publication_approval = true",
    "public_announcement = approved",
    "social_post_publication = approved",
    "runtime_execution_ready = true",
    "scanner_readiness_claim = true",
    "customer_poc_readiness_claim = true",
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


def test_v06205_files_exist_and_record_selection() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS[:5])
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS[:5])


def test_v06205_repository_surfaces_selection() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06205_does_not_approve_publication_or_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06205_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06205_next_work_selection_using_risk_tiered_granularity.py" in run_all


if __name__ == "__main__":
    test_v06205_files_exist_and_record_selection()
    test_v06205_repository_surfaces_selection()
    test_v06205_does_not_approve_publication_or_readiness()
    test_v06205_run_all_registers_local_test()
    print("v0.6.205 next work selection checks passed")
