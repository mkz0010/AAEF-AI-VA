from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/295-v06219-aaef-applied-evidence-minimum-flow-plan-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0289-add-v06219-aaef-applied-evidence-minimum-flow-plan-candidate.md"
ISSUE = ROOT / "planning/issues/0288-add-v06219-aaef-applied-evidence-minimum-flow-plan-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "AAEF Applied Evidence Minimum Flow Plan Candidate",
    "Status: Candidate only",
    "candidate only",
    "not accepted",
    "not applied",
    "Central proposition",
    "Model output is not authority",
    "AI generates `tool_action_request`, but execution is decided by gates",
    "Candidate minimum flow",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Existing element inventory plan",
    "Four-scenario matrix plan",
    "Evidence linkage table plan",
    "tool_action_request record plan",
    "gate_decision record plan",
    "dispatch / non-dispatch evidence plan",
    "Evidence event package plan",
    "Reviewer walkthrough plan",
    "AAEF five questions mapping plan",
    "Evidence trust boundary and non-proof boundary plan",
    "Handback summary plan",
    "Public/private/patent-sensitive boundary plan",
    "Candidate sequencing",
]


REQUIRED_BOUNDARY_TOKENS = [
    "v0.6.219 does not",
    "create the minimum flow package",
    "create new fixtures",
    "modify existing fixtures",
    "create reviewer walkthrough content",
    "create an AAEF handback summary",
    "change Tool Gateway behavior",
    "apply runtime changes",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.219",
    "AAEF Applied Evidence Minimum Flow Plan Candidate",
    "candidate only",
    "not accepted",
    "not applied",
    "v0.6.220 AAEF Applied Evidence Minimum Flow Plan Review and Decision",
    "no minimum flow package is created in v0.6.219",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "minimum_flow_plan_accepted = true",
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


def test_v06219_files_exist_and_record_plan_candidate() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "candidate plan is not accepted", "v0.6.220 must review"])
    assert_contains_all(ISSUE, ["AAEF Applied Evidence Minimum Flow Plan Candidate", "no minimum flow package is created in v0.6.219", "v0.6.220 must review"])


def test_v06219_repository_surfaces_plan_candidate() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


# v0.6.356 scope note: README/CHANGELOG/ROADMAP are rolling aggregate files; historical forbidden-token checks stay scoped to checkpoint-local artifacts.
def test_v06219_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06219_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06219_aaef_applied_evidence_minimum_flow_plan_candidate.py" in run_all


if __name__ == "__main__":
    test_v06219_files_exist_and_record_plan_candidate()
    test_v06219_repository_surfaces_plan_candidate()
    test_v06219_does_not_apply_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06219_run_all_registers_local_test()
    print("v0.6.219 AAEF Applied Evidence Minimum Flow Plan Candidate checks passed")
