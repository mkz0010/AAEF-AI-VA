from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/282-v06206-static-fixture-review-path-repository-wording-integration-plan-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0276-add-v06206-static-fixture-review-path-repository-wording-integration-plan-candidate.md"
ISSUE = ROOT / "planning/issues/0275-add-v06206-static-fixture-review-path-repository-wording-integration-plan-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "Status: Candidate only",
    "candidate only",
    "not accepted",
    "not applied",
    "not published",
    "subject to v0.6.207 review and decision",
    "Candidate integration objective",
    "Candidate target surfaces",
    "Candidate non-target surfaces",
    "Candidate wording reuse rules",
    "Candidate required boundary checklist",
    "Candidate review requirements for v0.6.207",
    "Candidate next step if accepted",
    "Static Fixture Review Path",
    "publication remains deferred",
    "v0.6.206 does not",
]


REQUIRED_TARGET_TOKENS = [
    "README.md",
    "docs/repository-landing-demo-path-clarity.md",
    "docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md",
    "ROADMAP.md",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.206",
    "Static Fixture Review Path Repository Wording Integration Plan Candidate",
    "candidate only",
    "not applied",
    "publication remains deferred",
    "v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision",
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
    "applied wording changes",
    "published announcement",
    "approved social post",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06206_files_exist_and_candidate_plan_is_recorded() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_TARGET_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "not accepted", "v0.6.207"])
    assert_contains_all(ISSUE, ["candidate plan only", "does not apply the plan", "v0.6.207 must review"])


def test_v06206_repository_surfaces_candidate_without_application() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06206_does_not_approve_publication_or_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06206_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06206_static_fixture_review_path_repository_wording_integration_plan_candidate.py" in run_all


if __name__ == "__main__":
    test_v06206_files_exist_and_candidate_plan_is_recorded()
    test_v06206_repository_surfaces_candidate_without_application()
    test_v06206_does_not_approve_publication_or_readiness()
    test_v06206_run_all_registers_local_test()
    print("v0.6.206 Static Fixture Review Path repository wording integration plan candidate checks passed")
