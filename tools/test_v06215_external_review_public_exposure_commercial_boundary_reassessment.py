from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/291-v06215-external-review-public-exposure-commercial-boundary-reassessment.md"
ADR = ROOT / "planning/decisions/ADR-0285-add-v06215-external-review-public-exposure-commercial-boundary-reassessment.md"
ISSUE = ROOT / "planning/issues/0284-add-v06215-external-review-public-exposure-commercial-boundary-reassessment.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = public_exposure_hygiene_plan",
    "selected_next_work_item_risk_tier = high",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.216 Public Exposure Hygiene Plan Candidate",
    "selected_followup_checkpoint = v0.6.217 Public Exposure Hygiene Plan Review and Decision",
]


REQUIRED_DEFERRED_TOKENS = [
    "deferred_work_item = mock_dry_run_completed_status_terminology_cleanup",
    "deferred_reason = interposed_public_exposure_and_commercial_boundary_hygiene_review",
    "deferred_return_condition = public_exposure_hygiene_plan_reviewed_and_decided",
    "deferred, not rejected",
]


REQUIRED_REASSESSMENT_TOKENS = [
    "External Review Public Exposure and Commercial Boundary Reassessment",
    "public exposure hygiene",
    "commercial boundary",
    "README front-page value proposition",
    "Public contact route",
    "Pricing and commercial draft exposure",
    "Business plan exposure",
    "Current/latest version clarity",
    "Candidate and draft labels",
    "Public documentation curation",
    "Demo and motion evidence positioning",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.215",
    "External Review Public Exposure and Commercial Boundary Reassessment",
    "public_exposure_hygiene_plan",
    "v0.6.216 Public Exposure Hygiene Plan Candidate",
    "v0.6.217 Public Exposure Hygiene Plan Review and Decision",
    "mock_dry_run_completed_status_terminology_cleanup is deferred, not rejected",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "public_contact_route_removed = true",
    "pricing_materials_moved = true",
    "business_plan_moved = true",
    "readme_front_page_rewritten = true",
    "historical_docs_deleted = true",
    "gateway_core_safety_controls_implemented = true",
    "tool_gateway_behavior_changed = true",
    "adapter_behavior_changed = true",
    "execution_status_renamed = true",
    "runtime_demo_ready = true",
    "scanner_readiness_claim = true",
    "external_poc_readiness_claim = true",
    "publication_approval = true",
    "public_announcement = approved",
    "social_post_publication = approved",
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


def test_v06215_files_exist_and_record_reassessment() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(DOC, REQUIRED_DEFERRED_TOKENS)
    assert_contains_all(DOC, REQUIRED_REASSESSMENT_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, REQUIRED_DEFERRED_TOKENS[:3])


def test_v06215_repository_surfaces_reassessment() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06215_does_not_apply_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06215_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06215_external_review_public_exposure_commercial_boundary_reassessment.py" in run_all


if __name__ == "__main__":
    test_v06215_files_exist_and_record_reassessment()
    test_v06215_repository_surfaces_reassessment()
    test_v06215_does_not_apply_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06215_run_all_registers_local_test()
    print("v0.6.215 External Review Public Exposure and Commercial Boundary Reassessment checks passed")
