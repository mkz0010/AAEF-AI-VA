from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/298-v06222-existing-element-inventory-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0292-add-v06222-existing-element-inventory-candidate.md"
ISSUE = ROOT / "planning/issues/0291-add-v06222-existing-element-inventory-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DOC_TOKENS = [
    "Existing Element Inventory Candidate",
    "Status: Candidate only",
    "existing_element_inventory_candidate_recorded = true",
    "existing_element_inventory_accepted = false",
    "Inventory classification model",
    "Minimum flow steps covered",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Candidate inventory table",
    "INV-001",
    "INV-020",
    "Four-scenario coverage candidate",
    "permitted safe diagnostic",
    "denied out-of-scope request",
    "held / requires human approval",
    "expired-not-executed",
    "Evidence linkage coverage candidate",
    "AAEF five questions coverage candidate",
    "Public/private/patent-sensitive boundary candidate",
    "Candidate risks",
    "Boundary notes retained",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_BOUNDARY_TOKENS = [
    "v0.6.222 does not",
    "accept the existing element inventory",
    "create the minimum flow package",
    "create new fixtures",
    "modify existing fixtures",
    "create evidence linkage records",
    "create reviewer walkthrough content",
    "create AAEF five questions mapping content",
    "create an AAEF handback summary",
    "change Tool Gateway behavior",
    "apply runtime changes",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.222",
    "Existing Element Inventory Candidate",
    "candidate only",
    "not accepted",
    "not applied",
    "v0.6.223 Existing Element Inventory Review and Decision",
    "no existing element inventory is accepted in v0.6.222",
    "no minimum flow package is created in v0.6.222",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "existing_element_inventory_accepted = true",
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


def test_v06222_files_exist_and_record_inventory_candidate() -> None:
    assert_contains_all(DOC, REQUIRED_DOC_TOKENS)
    assert_contains_all(DOC, REQUIRED_BOUNDARY_TOKENS)
    assert_contains_all(ADR, ["Status: Candidate recorded", "candidate inventory is not accepted", "v0.6.223 must review"])
    assert_contains_all(ISSUE, ["Existing Element Inventory Candidate", "no inventory is accepted in v0.6.222", "v0.6.223 must review"])


def test_v06222_repository_surfaces_inventory_candidate() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


def test_v06222_does_not_apply_inventory_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06222_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06222_existing_element_inventory_candidate.py" in run_all


if __name__ == "__main__":
    test_v06222_files_exist_and_record_inventory_candidate()
    test_v06222_repository_surfaces_inventory_candidate()
    test_v06222_does_not_apply_inventory_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06222_run_all_registers_local_test()
    print("v0.6.222 Existing Element Inventory Candidate checks passed")
