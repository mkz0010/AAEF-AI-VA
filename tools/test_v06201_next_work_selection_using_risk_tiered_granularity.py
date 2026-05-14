from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/277-v06201-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0271-add-v06201-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0270-add-v06201-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = static_fixture_review_path_public_communication_pack",
    "selected_next_work_item_risk_tier = medium",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.202 Static Fixture Review Path Public Communication Pack Candidate",
    "selected_followup_checkpoint = v0.6.203 Static Fixture Review Path Public Communication Pack Review and Decision",
    "Static Fixture Review Path",
    "v0.6.201 does not create the communication pack body",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.201",
    "static_fixture_review_path_public_communication_pack",
    "Static Fixture Review Path",
]


FORBIDDEN_ASSERTIVE_CLAIMS = [
    "is a live scanner",
    "is an executable demo",
    "is a production-ready scanner",
    "is customer PoC-ready",
    "provides third-party testing authorization",
    "provides certification",
    "provides legal compliance",
    "provides an audit opinion",
    "provides diagnostic completeness",
    "provides external framework equivalence",
    "production-ready scanner",
    "certification-ready",
    "audit-ready",
    "diagnostically complete",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def assert_no_forbidden_assertive_claims(path: Path) -> None:
    lowered = read(path).lower()
    for phrase in FORBIDDEN_ASSERTIVE_CLAIMS:
        assert phrase.lower() not in lowered, (
            f"{path.relative_to(ROOT)} contains forbidden assertive claim phrase: {phrase}"
        )


def test_v06201_files_exist_and_record_selection() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS[:5])
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS[:5])


def test_v06201_repository_surfaces_selection() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06201_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06201_next_work_selection_using_risk_tiered_granularity.py" in run_all


def test_v06201_does_not_assert_readiness_or_equivalence() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        assert_no_forbidden_assertive_claims(path)


if __name__ == "__main__":
    test_v06201_files_exist_and_record_selection()
    test_v06201_repository_surfaces_selection()
    test_v06201_run_all_registers_local_test()
    test_v06201_does_not_assert_readiness_or_equivalence()
    print("v0.6.201 next work selection checks passed")
