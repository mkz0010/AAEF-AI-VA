from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/293-v06217-public-exposure-hygiene-plan-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0287-add-v06217-public-exposure-hygiene-plan-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0286-add-v06217-public-exposure-hygiene-plan-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "Public Exposure Hygiene Plan Review and Decision",
    "Accepted for cleanup planning; not applied",
    "public_exposure_hygiene_plan_accepted = true",
    "public_exposure_cleanup_applied = false",
    "public_contact_route_removed = false",
    "pricing_materials_moved = false",
    "business_plan_moved = false",
    "readme_front_page_rewritten = false",
    "historical_docs_deleted = false",
    "mock_execution_recording_created = false",
    "gateway_core_safety_controls_implemented = false",
    "tool_gateway_behavior_changed = false",
    "adapter_behavior_changed = false",
    "execution_status_renamed = false",
    "runtime_demo_ready = false",
    "publication_approval = false",
    "commercial_terms_created = false",
]


REQUIRED_PLAN_TOKENS = [
    "Accepted problem statement",
    "Accepted principles",
    "Accepted workstreams",
    "README front-page value proposition and reader path",
    "Public contact route hygiene",
    "Pricing and commercial draft exposure hygiene",
    "Business plan exposure hygiene",
    "Current/latest version clarity",
    "External-facing candidate and draft label hygiene",
    "Public documentation curation",
    "Demo and motion-evidence positioning",
    "Accepted sequencing",
    "Accepted definition of done for future cleanup work",
    "Treatment of existing public history",
    "v0.6.218 Next Work Selection Using Risk-Tiered Granularity",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.217",
    "Public Exposure Hygiene Plan Review and Decision",
    "accepted for cleanup planning",
    "not applied",
    "v0.6.218 Next Work Selection Using Risk-Tiered Granularity",
    "no cleanup is applied in v0.6.217",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "public_exposure_cleanup_applied = true",
    "public_contact_route_removed = true",
    "pricing_materials_moved = true",
    "business_plan_moved = true",
    "readme_front_page_rewritten = true",
    "historical_docs_deleted = true",
    "mock_execution_recording_created = true",
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
    "commercial_terms_created = true",
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


def test_v06217_files_exist_and_record_review_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_PLAN_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for cleanup planning", "No cleanup is applied in this checkpoint", "runtime demo remains necessary but deferred"])


def test_v06217_repository_surfaces_review_decision() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06217_does_not_apply_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06217_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06217_public_exposure_hygiene_plan_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06217_files_exist_and_record_review_decision()
    test_v06217_repository_surfaces_review_decision()
    test_v06217_does_not_apply_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06217_run_all_registers_local_test()
    print("v0.6.217 Public Exposure Hygiene Plan Review and Decision checks passed")
