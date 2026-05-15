from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/304-v06228-evidence-linkage-table-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0298-add-v06228-evidence-linkage-table-candidate.md"
ISSUE = ROOT / "planning/issues/0297-add-v06228-evidence-linkage-table-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "Evidence Linkage Table Candidate",
    "Status: Candidate only",
    "evidence_linkage_table_candidate_recorded = true",
    "evidence_linkage_table_accepted = false",
    "Linkage classification model",
    "Link status model",
    "existing_public_safe",
    "planned_public_safe_after_sanitization",
    "Candidate evidence linkage table",
    "LNK-001",
    "LNK-002",
    "LNK-003",
    "LNK-004",
    "SCN-001",
    "SCN-002",
    "SCN-003",
    "SCN-004",
    "model_output_id",
    "tool_action_request_id",
    "gate_decision_id",
    "dispatch_decision_id or non_dispatch_decision_id",
    "execution_result_id or non_execution_result_id",
    "evidence_event_id",
    "reviewer_walkthrough_id",
    "five_questions_mapping_id",
    "Minimum flow link coverage candidate",
    "Scenario linkage expectations",
    "AAEF five questions linkage candidate",
    "Public/private/patent-sensitive linkage notes",
    "Evidence-boundary notes retained",
    "Linkage risks",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_BOUNDARY_TOKENS = [
    "v0.6.228 does not",
    "accept the evidence linkage table",
    "create the minimum flow package",
    "create new fixtures",
    "modify existing fixtures",
    "create evidence linkage records",
    "create tool_action_request records",
    "create gate_decision records",
    "create dispatch or non-dispatch evidence records",
    "create execution result records",
    "create non-execution result records",
    "create reviewer walkthrough content",
    "create AAEF five questions mapping content",
    "create an AAEF handback summary",
    "change Tool Gateway behavior",
    "apply runtime changes",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.228",
    "Evidence Linkage Table Candidate",
    "candidate only",
    "not accepted",
    "not applied",
    "v0.6.229 Evidence Linkage Table Review and Decision",
    "no evidence linkage table is accepted in v0.6.228",
    "no minimum flow package is created in v0.6.228",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "evidence_linkage_table_accepted = true",
    "minimum_flow_package_created = true",
    "fixtures_created = true",
    "fixtures_modified = true",
    "evidence_linkage_records_created = true",
    "tool_action_request_records_created = true",
    "gate_decision_records_created = true",
    "dispatch_evidence_records_created = true",
    "execution_result_records_created = true",
    "non_execution_result_records_created = true",
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


def test_v06228_files_exist_and_record_linkage_candidate() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "candidate table is not accepted", "v0.6.229 must review"])
    assert_contains_all(ISSUE, ["Evidence Linkage Table Candidate", "no linkage table is accepted in v0.6.228", "v0.6.229 must review"])


def test_v06228_repository_surfaces_linkage_candidate() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06228_does_not_apply_linkage_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06228_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06228_evidence_linkage_table_candidate.py" in run_all


if __name__ == "__main__":
    test_v06228_files_exist_and_record_linkage_candidate()
    test_v06228_repository_surfaces_linkage_candidate()
    test_v06228_does_not_apply_linkage_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06228_run_all_registers_local_test()
    print("v0.6.228 Evidence Linkage Table Candidate checks passed")
