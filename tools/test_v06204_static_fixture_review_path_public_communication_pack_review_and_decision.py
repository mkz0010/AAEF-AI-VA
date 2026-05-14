from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/280-v06204-static-fixture-review-path-public-communication-pack-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0274-add-v06204-static-fixture-review-path-public-communication-pack-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0273-add-v06204-static-fixture-review-path-public-communication-pack-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "v0.6.204",
    "Accepted for repository wording use; publication deferred",
    "communication_pack_accepted_for_repository_wording = true",
    "publication_approval = false",
    "public_announcement = deferred",
    "social_post_publication = deferred",
    "public_demo_label_ready = false",
    "executable_demo_ready = false",
    "scanner_readiness_claim = false",
    "customer_poc_readiness_claim = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]


REQUIRED_PACK_TOKENS = [
    "Accepted short public description",
    "Accepted medium public description",
    "Accepted README-compatible summary",
    "Accepted social-post-style draft boundary",
    "not published",
    "not a publication approval",
    "Static Fixture Review Path",
    "publicly reviewable static fixture set",
    "static, mock, fixture-only, non-execution review path",
    "AI output is a request, not authority",
    "execution is decided by gates",
    "evidence links the request, gate decision, execution or non-execution result, and review",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.204",
    "accepted for repository wording use",
    "publication deferred",
    "not published",
    "Static Fixture Review Path",
]


FORBIDDEN_PUBLICATION_OR_READINESS_TOKENS = [
    "published announcement",
    "approved for publication",
    "authorized for customer PoC",
    "ready for runtime execution",
    "ready for scanner execution",
    "production-ready workflow is provided",
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


def test_v06204_files_exist_and_record_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_PACK_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for repository wording use", "Publication remains deferred"])


def test_v06204_repository_surfaces_decision_with_boundaries() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06204_does_not_publish_or_add_readiness_claims() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_PUBLICATION_OR_READINESS_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06204_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06204_static_fixture_review_path_public_communication_pack_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06204_files_exist_and_record_decision()
    test_v06204_repository_surfaces_decision_with_boundaries()
    test_v06204_does_not_publish_or_add_readiness_claims()
    test_v06204_run_all_registers_local_test()
    print("v0.6.204 Static Fixture Review Path Public Communication Pack review and decision checks passed")
