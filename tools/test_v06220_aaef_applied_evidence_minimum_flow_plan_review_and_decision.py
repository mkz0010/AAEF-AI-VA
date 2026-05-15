from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/296-v06220-aaef-applied-evidence-minimum-flow-plan-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0290-add-v06220-aaef-applied-evidence-minimum-flow-plan-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0289-add-v06220-aaef-applied-evidence-minimum-flow-plan-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "AAEF Applied Evidence Minimum Flow Plan Review and Decision",
    "Accepted for minimum flow planning; not applied",
    "aaef_applied_evidence_minimum_flow_plan_accepted = true",
    "minimum_flow_package_created = false",
    "fixtures_created = false",
    "fixtures_modified = false",
    "evidence_linkage_records_created = false",
    "tool_action_request_records_created = false",
    "gate_decision_records_created = false",
    "dispatch_evidence_records_created = false",
    "reviewer_walkthrough_created = false",
    "aaef_five_questions_mapping_created = false",
    "aaef_handback_summary_created = false",
    "tool_gateway_behavior_changed = false",
    "runtime_demo_ready = false",
    "publication_approval = false",
]


REQUIRED_PLAN_TOKENS = [
    "Accepted central proposition",
    "Model output is not authority",
    "AI generates `tool_action_request`, but execution is decided by gates",
    "Accepted minimum flow",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Accepted existing element inventory requirement",
    "Accepted four-scenario matrix requirement",
    "Accepted evidence linkage table requirement",
    "Accepted tool_action_request record requirement",
    "Accepted gate_decision record requirement",
    "Accepted dispatch / non-dispatch evidence requirement",
    "Accepted evidence event package requirement",
    "Accepted reviewer walkthrough requirement",
    "Accepted AAEF five questions mapping requirement",
    "Accepted evidence trust boundary and non-proof boundary requirement",
    "Accepted handback summary requirement",
    "Accepted public/private/patent-sensitive boundary",
    "Accepted sequencing",
    "v0.6.221 Next Work Selection Using Risk-Tiered Granularity",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.220",
    "AAEF Applied Evidence Minimum Flow Plan Review and Decision",
    "accepted for minimum flow planning",
    "not applied",
    "v0.6.221 Next Work Selection Using Risk-Tiered Granularity",
    "no minimum flow package is created in v0.6.220",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "minimum_flow_package_created = true",
    "fixtures_created = true",
    "fixtures_modified = true",
    "evidence_linkage_records_created = true",
    "tool_action_request_records_created = true",
    "gate_decision_records_created = true",
    "dispatch_evidence_records_created = true",
    "reviewer_walkthrough_created = true",
    "aaef_five_questions_mapping_created = true",
    "aaef_handback_summary_created = true",
    "public_exposure_cleanup_applied = true",
    "readme_front_page_rewritten = true",
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


def test_v06220_files_exist_and_record_review_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_PLAN_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for minimum flow planning", "No minimum flow package is created in this checkpoint", "runtime demo remains necessary but deferred"])


def test_v06220_repository_surfaces_review_decision() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06220_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06220_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06220_aaef_applied_evidence_minimum_flow_plan_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06220_files_exist_and_record_review_decision()
    test_v06220_repository_surfaces_review_decision()
    test_v06220_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06220_run_all_registers_local_test()
    print("v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision checks passed")
