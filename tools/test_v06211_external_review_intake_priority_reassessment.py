from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/287-v06211-external-review-intake-priority-reassessment.md"
ADR = ROOT / "planning/decisions/ADR-0281-add-v06211-external-review-intake-priority-reassessment.md"
ISSUE = ROOT / "planning/issues/0280-add-v06211-external-review-intake-priority-reassessment.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_SELECTION_TOKENS = [
    "selected_next_work_item = gateway_core_safety_integration_plan",
    "selected_next_work_item_risk_tier = high",
    "selected_next_work_item_checkpoint_count = 2",
    "selected_next_checkpoint = v0.6.212 Gateway Core Safety Integration Plan Candidate",
    "selected_followup_checkpoint = v0.6.213 Gateway Core Safety Integration Plan Review and Decision",
]


REQUIRED_REASSESSMENT_TOKENS = [
    "External review intake",
    "documented control pattern",
    "helper implementation",
    "Tool Gateway core-path enforcement",
    "Gateway Core Safety Integration",
    "reviewer navigation polish is deferred",
    "Closed runtime demo remains necessary",
    "runtime demo work should not advance",
    "implementation maturity matrix",
    "safe demo / mock runtime / controlled runtime PoC separation",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.211",
    "External Review Intake and Priority Reassessment",
    "gateway_core_safety_integration_plan",
    "v0.6.212 Gateway Core Safety Integration Plan Candidate",
    "v0.6.213 Gateway Core Safety Integration Plan Review and Decision",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "runtime_demo_ready = true",
    "scanner_readiness_claim = true",
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


def test_v06211_files_exist_and_record_reassessment() -> None:
    assert_contains_all(DOC, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(DOC, REQUIRED_REASSESSMENT_TOKENS)
    assert_contains_all(ADR, REQUIRED_SELECTION_TOKENS)
    assert_contains_all(ISSUE, ["Gateway Core Safety Integration planning is selected as the next priority", "closed runtime demo remains necessary but deferred"])


def test_v06211_repository_surfaces_reassessment() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06211_does_not_approve_runtime_publication_or_assurance_claims() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06211_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06211_external_review_intake_priority_reassessment.py" in run_all


if __name__ == "__main__":
    test_v06211_files_exist_and_record_reassessment()
    test_v06211_repository_surfaces_reassessment()
    test_v06211_does_not_approve_runtime_publication_or_assurance_claims()
    test_v06211_run_all_registers_local_test()
    print("v0.6.211 external review intake and priority reassessment checks passed")
