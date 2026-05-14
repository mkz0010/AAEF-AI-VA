from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/285-v06209-static-fixture-review-path-repository-wording-integration-implementation-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0279-add-v06209-static-fixture-review-path-repository-wording-integration-implementation-candidate.md"
ISSUE = ROOT / "planning/issues/0278-add-v06209-static-fixture-review-path-repository-wording-integration-implementation-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
CLARITY_DOC = ROOT / "docs/repository-landing-demo-path-clarity.md"
WALKTHROUGH = ROOT / "docs/examples/safe-demo/blocked-tool-action-request-review/reviewer-walkthrough.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_STATUS_TOKENS = [
    "v0.6.209",
    "Implementation candidate applied; not accepted",
    "repository_wording_integration_implementation_candidate_applied = true",
    "repository_wording_integration_implementation_accepted = false",
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


REQUIRED_BOUNDARY_TOKENS = [
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
    "v0.6.209",
    "Static Fixture Review Path Repository Wording Integration Implementation Candidate",
    "implementation candidate",
    "not accepted",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "repository_wording_integration_implementation_accepted = true",
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


def test_v06209_files_exist_and_record_candidate_status() -> None:
    assert_contains_all(DOC, REQUIRED_STATUS_TOKENS)
    assert_contains_all(ADR, REQUIRED_STATUS_TOKENS)
    assert_contains_all(ISSUE, ["implementation candidate", "not accepted", "v0.6.210"])


def test_v06209_target_surfaces_contain_candidate_boundary_wording() -> None:
    for path in [README, ROADMAP, CLARITY_DOC, WALKTHROUGH]:
        assert_contains_all(path, REQUIRED_BOUNDARY_TOKENS)


def test_v06209_repository_surfaces_candidate_without_acceptance() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06209_does_not_accept_or_approve_publication_or_readiness() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP, CLARITY_DOC, WALKTHROUGH]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06209_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06209_static_fixture_review_path_repository_wording_integration_implementation_candidate.py" in run_all


if __name__ == "__main__":
    test_v06209_files_exist_and_record_candidate_status()
    test_v06209_target_surfaces_contain_candidate_boundary_wording()
    test_v06209_repository_surfaces_candidate_without_acceptance()
    test_v06209_does_not_accept_or_approve_publication_or_readiness()
    test_v06209_run_all_registers_local_test()
    print("v0.6.209 Static Fixture Review Path repository wording integration implementation candidate checks passed")
