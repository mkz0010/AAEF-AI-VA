from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/288-v06212-gateway-core-safety-integration-plan-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0282-add-v06212-gateway-core-safety-integration-plan-candidate.md"
ISSUE = ROOT / "planning/issues/0281-add-v06212-gateway-core-safety-integration-plan-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DOC_TOKENS = [
    "Gateway Core Safety Integration Plan Candidate",
    "Status: Candidate only",
    "candidate only",
    "not accepted",
    "not implemented",
    "not gateway-integrated",
    "not runtime-ready",
    "not scanner-ready",
    "mandatory Gateway core sequence",
    "Schema validation",
    "Request / decision binding validation",
    "Authorization current-time expiry validation",
    "Request / decision constraint-diff validation",
    "External discovery fail-closed validation",
    "Target / scope / tool / operation binding validation",
    "Credential_ref validation against mock Vault metadata",
    "Adapter command-plan generation",
    "Controlled executor dry-run validation",
    "Tool result / evidence record generation",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]

REQUIRED_PRIORITY_TOKENS = [
    "Mock / dry-run completed status terminology cleanup",
    "Authorization current-time expiry integration",
    "Request / decision constraint-diff integration",
    "External discovery fail-closed integration",
    "Common target / scope / tool / operation binding",
    "Adapter consistency review",
    "Implementation maturity matrix",
    "Evidence wording cleanup",
    "Public / private commercial material boundary review",
    "Safe demo / mock runtime / controlled runtime PoC separation",
]

REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.212",
    "Gateway Core Safety Integration Plan Candidate",
    "candidate only",
    "not implemented",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.213 Gateway Core Safety Integration Plan Review and Decision",
]

FORBIDDEN_TOKENS = [
    "gateway_core_safety_controls_implemented = true",
    "tool_gateway_behavior_changed = true",
    "adapter_behavior_changed = true",
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


def test_v06212_files_exist_and_record_candidate_plan() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_PRIORITY_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "candidate plan is not accepted", "v0.6.213 must review"])
    assert_contains_all(ISSUE, ["Gateway Core Safety Integration Plan Candidate", "runtime demo remains necessary but deferred", "does not change Tool Gateway behavior"])


def test_v06212_repository_surfaces_candidate_plan() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06212_does_not_apply_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06212_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06212_gateway_core_safety_integration_plan_candidate.py" in run_all


if __name__ == "__main__":
    test_v06212_files_exist_and_record_candidate_plan()
    test_v06212_repository_surfaces_candidate_plan()
    test_v06212_does_not_apply_gateway_runtime_publication_or_assurance_changes()
    test_v06212_run_all_registers_local_test()
    print("v0.6.212 Gateway Core Safety Integration Plan Candidate checks passed")
