from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/283-v06207-static-fixture-review-path-repository-wording-integration-plan-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0277-add-v06207-static-fixture-review-path-repository-wording-integration-plan-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0276-add-v06207-static-fixture-review-path-repository-wording-integration-plan-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "v0.6.207",
    "Accepted for future integration planning; not applied",
    "repository_wording_integration_plan_accepted = true",
    "repository_wording_changes_applied = false",
    "publication_approval = false",
    "public_announcement = deferred",
    "social_post_publication = deferred",
    "runtime_execution_ready = false",
    "scanner_readiness_claim = false",
    "customer_poc_readiness_claim = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]


REQUIRED_PLAN_TOKENS = [
    "Accepted integration objective",
    "Accepted target surfaces",
    "Accepted non-target surfaces",
    "Accepted wording reuse rules",
    "Accepted required boundary checklist",
    "Future implementation requirements",
    "repository wording changes remain not applied",
    "publication remains deferred",
    "Static Fixture Review Path",
    "AI output remains a request, not authority",
    "execution remains decided by gates",
]


REQUIRED_TARGET_TOKENS = [
    "README.md",
    "docs/repository-landing-demo-path-clarity.md",
    "docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md",
    "ROADMAP.md",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.207",
    "Static Fixture Review Path Repository Wording Integration Plan Review and Decision",
    "accepted for future integration planning",
    "repository wording changes remain not applied",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "repository_wording_changes_applied = true",
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
    "approved social post",
    "published announcement",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06207_files_exist_and_record_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_PLAN_TOKENS)
    assert_contains_all(DOC, REQUIRED_TARGET_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for future integration planning", "Repository wording changes remain not applied", "Publication remains deferred"])


def test_v06207_repository_surfaces_decision_without_application() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06207_does_not_apply_or_approve_publication_or_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06207_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06207_static_fixture_review_path_repository_wording_integration_plan_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06207_files_exist_and_record_decision()
    test_v06207_repository_surfaces_decision_without_application()
    test_v06207_does_not_apply_or_approve_publication_or_readiness()
    test_v06207_run_all_registers_local_test()
    print("v0.6.207 Static Fixture Review Path repository wording integration plan review and decision checks passed")
