from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/278-v06202-static-fixture-review-path-public-communication-pack-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0272-add-v06202-static-fixture-review-path-public-communication-pack-candidate.md"
ISSUE = ROOT / "planning/issues/0271-add-v06202-static-fixture-review-path-public-communication-pack-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "Status: Candidate only",
    "Static Fixture Review Path",
    "candidate-only",
    "not published",
    "not accepted",
    "subject to v0.6.203 review and decision",
    "Candidate short public description",
    "Candidate medium public description",
    "Candidate README-compatible summary",
    "Candidate social-post-style draft",
    "Candidate wording to prefer",
    "Candidate terms to avoid",
    "Candidate required boundary sentences",
    "Candidate reviewer path summary",
    "AI output is a request, not authority",
    "execution is decided by gates",
    "evidence links the request, gate decision, execution or non-execution result, and review",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.202",
    "Static Fixture Review Path Public Communication Pack Candidate",
    "candidate",
    "not published",
]


REQUIRED_BOUNDARY_TOKENS = [
    "not a live scanner",
    "static, mock, fixture-only",
    "does not run tools",
    "does not provide third-party testing authorization",
    "production readiness",
    "certification",
    "legal compliance",
    "audit opinion",
    "diagnostic completeness",
    "external-framework equivalence",
]


FORBIDDEN_ACCEPTANCE_TOKENS = [
    "Status: Accepted",
    "accepted communication pack",
    "published announcement",
    "approved for publication",
    "authorized for customer PoC",
    "ready for runtime execution",
    "ready for scanner execution",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06202_files_exist_and_candidate_pack_is_recorded() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "v0.6.203", "not accepted"])
    assert_contains_all(ISSUE, ["candidate", "not published", "v0.6.203 must review"])


def test_v06202_repository_surfaces_candidate_without_publication() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06202_boundary_sentences_are_present() -> None:
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)


def test_v06202_candidate_does_not_claim_acceptance_or_execution_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_ACCEPTANCE_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden acceptance token: {token}"


def test_v06202_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06202_static_fixture_review_path_public_communication_pack_candidate.py" in run_all


if __name__ == "__main__":
    test_v06202_files_exist_and_candidate_pack_is_recorded()
    test_v06202_repository_surfaces_candidate_without_publication()
    test_v06202_boundary_sentences_are_present()
    test_v06202_candidate_does_not_claim_acceptance_or_execution_readiness()
    test_v06202_run_all_registers_local_test()
    print("v0.6.202 Static Fixture Review Path Public Communication Pack candidate checks passed")
