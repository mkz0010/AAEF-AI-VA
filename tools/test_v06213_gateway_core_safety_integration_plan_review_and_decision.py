from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/289-v06213-gateway-core-safety-integration-plan-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0283-add-v06213-gateway-core-safety-integration-plan-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0282-add-v06213-gateway-core-safety-integration-plan-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "Gateway Core Safety Integration Plan Review and Decision",
    "Accepted for implementation planning; not implemented",
    "gateway_core_safety_integration_plan_accepted = true",
    "gateway_core_safety_controls_implemented = false",
    "tool_gateway_behavior_changed = false",
    "adapter_behavior_changed = false",
    "execution_status_renamed = false",
    "schema_changed = false",
    "validator_behavior_changed = false",
    "fixture_semantics_changed = false",
    "runtime_behavior_changed = false",
    "scanner_behavior_changed = false",
    "runtime_demo_ready = false",
    "scanner_readiness_claim = false",
    "external_poc_readiness_claim = false",
    "publication_approval = false",
    "public_announcement = deferred",
    "social_post_publication = deferred",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]


REQUIRED_PLAN_TOKENS = [
    "Accepted problem statement",
    "Accepted integration objective",
    "Accepted mandatory Gateway core sequence",
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
    "Accepted priority controls",
    "Accepted implementation staging",
    "Accepted definition of done for future implementation work",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.214 Next Work Selection Using Risk-Tiered Granularity",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.213",
    "Gateway Core Safety Integration Plan Review and Decision",
    "accepted for implementation planning",
    "not implemented",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.214 Next Work Selection Using Risk-Tiered Granularity",
]


FORBIDDEN_TOKENS = [
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


def test_v06213_files_exist_and_record_review_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_PLAN_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for implementation planning", "Gateway core safety controls remain not implemented", "Runtime demo remains necessary but deferred"])


def test_v06213_repository_surfaces_review_decision() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06213_does_not_apply_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06213_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06213_gateway_core_safety_integration_plan_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06213_files_exist_and_record_review_decision()
    test_v06213_repository_surfaces_review_decision()
    test_v06213_does_not_apply_gateway_runtime_publication_or_assurance_changes()
    test_v06213_run_all_registers_local_test()
    print("v0.6.213 Gateway Core Safety Integration Plan Review and Decision checks passed")
