from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/279-v06203-candidate-test-alignment-correction.md"
ADR = ROOT / "planning/decisions/ADR-0273-add-v06203-candidate-test-alignment-correction.md"
ISSUE = ROOT / "planning/issues/0272-add-v06203-candidate-test-alignment-correction.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_TOKENS = [
    "v0.6.203",
    "candidate test alignment correction",
    "not published",
    "v0.6.204 Static Fixture Review Path Public Communication Pack Review and Decision",
]


FORBIDDEN_TOKENS = [
    "Status: Accepted communication pack",
    "published announcement",
    "approved for publication",
    "authorized for customer PoC",
    "ready for runtime execution",
    "ready for scanner execution",
    "production-ready scanner",
    "diagnostically complete",
    "external-framework equivalent",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06203_correction_files_record_deferral() -> None:
    assert_contains_all(DOC, REQUIRED_TOKENS)
    assert_contains_all(ADR, ["v0.6.203", "not published", "v0.6.204"])
    assert_contains_all(ISSUE, ["v0.6.203", "not published", "v0.6.204"])


def test_v06203_readme_contains_lowercase_not_published() -> None:
    readme = read(README)
    assert "not published" in readme
    assert "v0.6.202 communication pack candidate checkpoint" in readme


def test_v06203_repository_surfaces_correction_and_deferral() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, ["v0.6.203", "not published"])


def test_v06203_does_not_accept_or_publish_pack() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06203_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06203_candidate_test_alignment_correction.py" in run_all


if __name__ == "__main__":
    test_v06203_correction_files_record_deferral()
    test_v06203_readme_contains_lowercase_not_published()
    test_v06203_repository_surfaces_correction_and_deferral()
    test_v06203_does_not_accept_or_publish_pack()
    test_v06203_run_all_registers_local_test()
    print("v0.6.203 candidate test alignment correction checks passed")
