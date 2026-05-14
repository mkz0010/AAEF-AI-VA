from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/286-v06210-static-fixture-review-path-repository-wording-integration-implementation-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0280-add-v06210-static-fixture-review-path-repository-wording-integration-implementation-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0279-add-v06210-static-fixture-review-path-repository-wording-integration-implementation-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
CLARITY_DOC = ROOT / "docs/repository-landing-demo-path-clarity.md"
WALKTHROUGH = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "v0.6.210",
    "Accepted for repository wording integration; publication deferred",
    "repository_wording_integration_implementation_review_decision = accepted",
    "repository_wording_changes_accepted_for_repository_use = true",
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


REQUIRED_SURFACE_TOKENS = [
    "v0.6.210",
    "accepted for repository wording integration",
    "Static Fixture Review Path",
    "static, mock, fixture-only",
    "non-execution",
    "reviewer-facing",
    "AI output is treated as a request, not authority",
    "Execution is decided by gates",
    "Evidence links the request, gate decision, execution or non-execution result, and review",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.210",
    "Static Fixture Review Path Repository Wording Integration Implementation Review and Decision",
    "accepted for repository wording integration",
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
    "approved social post",
    "published announcement",
]


FIXTURE_FORBIDDEN_TOKENS = [
    "customer",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing expected file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_contains_all(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06210_files_exist_and_record_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for repository wording use", "Publication remains deferred"])


def test_v06210_repository_surfaces_record_accepted_wording_boundary() -> None:
    for path in [README, ROADMAP, CLARITY_DOC, WALKTHROUGH]:
        assert_contains_all(path, REQUIRED_SURFACE_TOKENS)


def test_v06210_repository_summaries_record_decision() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06210_does_not_approve_publication_or_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP, CLARITY_DOC, WALKTHROUGH]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06210_reviewer_walkthrough_avoids_fixture_forbidden_terms() -> None:
    text = read(WALKTHROUGH).lower()
    for token in FIXTURE_FORBIDDEN_TOKENS:
        assert token not in text, f"{WALKTHROUGH.relative_to(ROOT)} contains forbidden fixture token: {token}"


def test_v06210_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06210_static_fixture_review_path_repository_wording_integration_implementation_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06210_files_exist_and_record_decision()
    test_v06210_repository_surfaces_record_accepted_wording_boundary()
    test_v06210_repository_summaries_record_decision()
    test_v06210_does_not_approve_publication_or_readiness()
    test_v06210_reviewer_walkthrough_avoids_fixture_forbidden_terms()
    test_v06210_run_all_registers_local_test()
    print("v0.6.210 Static Fixture Review Path repository wording integration implementation review and decision checks passed")
