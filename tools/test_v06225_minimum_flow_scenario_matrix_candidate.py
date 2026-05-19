from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/301-v06225-minimum-flow-scenario-matrix-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0295-add-v06225-minimum-flow-scenario-matrix-candidate.md"
ISSUE = ROOT / "planning/issues/0294-add-v06225-minimum-flow-scenario-matrix-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "Minimum Flow Scenario Matrix Candidate",
    "Status: Candidate only",
    "minimum_flow_scenario_matrix_candidate_recorded = true",
    "minimum_flow_scenario_matrix_accepted = false",
    "Scenario matrix classification model",
    "Minimum flow steps covered",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Candidate scenario matrix",
    "SCN-001",
    "SCN-002",
    "SCN-003",
    "SCN-004",
    "permitted safe diagnostic",
    "denied out-of-scope request",
    "held / requires human approval",
    "expired-not-executed",
    "Scenario step coverage candidate",
    "Linkage planning candidate",
    "Scenario-specific maturity notes",
    "AAEF five questions planning candidate",
    "Evidence-boundary notes retained",
    "Public/private/patent-sensitive boundary notes retained",
    "Matrix risks",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_BOUNDARY_TOKENS = [
    "v0.6.225 does not",
    "accept the minimum flow scenario matrix",
    "create the minimum flow package",
    "create new fixtures",
    "modify existing fixtures",
    "create evidence linkage records",
    "create tool_action_request records",
    "create gate_decision records",
    "create dispatch or non-dispatch evidence records",
    "create reviewer walkthrough content",
    "create AAEF five questions mapping content",
    "create an AAEF handback summary",
    "change Tool Gateway behavior",
    "apply runtime changes",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.225",
    "Minimum Flow Scenario Matrix Candidate",
    "candidate only",
    "not accepted",
    "not applied",
    "v0.6.226 Minimum Flow Scenario Matrix Review and Decision",
    "no minimum flow scenario matrix is accepted in v0.6.225",
    "no minimum flow package is created in v0.6.225",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "minimum_flow_scenario_matrix_accepted = true",
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
    "private_generated_outputs_moved_public = true",
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


def test_v06225_files_exist_and_record_matrix_candidate() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "candidate matrix is not accepted", "v0.6.226 must review"])
    assert_contains_all(ISSUE, ["Minimum Flow Scenario Matrix Candidate", "no matrix is accepted in v0.6.225", "v0.6.226 must review"])


def test_v06225_repository_surfaces_matrix_candidate() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


# v0.6.356 scope note: README/CHANGELOG/ROADMAP are rolling aggregate files; historical forbidden-token checks stay scoped to checkpoint-local artifacts.
def test_v06225_does_not_apply_matrix_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06225_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06225_minimum_flow_scenario_matrix_candidate.py" in run_all


if __name__ == "__main__":
    test_v06225_files_exist_and_record_matrix_candidate()
    test_v06225_repository_surfaces_matrix_candidate()
    test_v06225_does_not_apply_matrix_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06225_run_all_registers_local_test()
    print("v0.6.225 Minimum Flow Scenario Matrix Candidate checks passed")
