from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/299-v06223-existing-element-inventory-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0293-add-v06223-existing-element-inventory-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0292-add-v06223-existing-element-inventory-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "Existing Element Inventory Review and Decision",
    "Accepted for minimum flow planning; not applied",
    "existing_element_inventory_accepted = true",
    "existing_element_inventory_applied_to_package = false",
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
    "private_generated_outputs_moved_public = false",
    "tool_gateway_behavior_changed = false",
    "runtime_demo_ready = false",
    "publication_approval = false",
]


REQUIRED_ACCEPTANCE_TOKENS = [
    "Accepted inventory classification model",
    "Accepted minimum flow coverage",
    "model_output",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision / non_dispatch_decision",
    "execution_result / non_execution_result",
    "evidence_event",
    "reviewer_walkthrough",
    "Accepted inventory rows",
    "INV-001",
    "INV-020",
    "Accepted four-scenario coverage assessment",
    "permitted safe diagnostic",
    "denied out-of-scope request",
    "held / requires human approval",
    "expired-not-executed",
    "Accepted evidence linkage coverage assessment",
    "Accepted AAEF five questions coverage assessment",
    "Accepted public/private/patent-sensitive boundary assessment",
    "Accepted candidate risks",
    "Accepted boundary notes",
    "v0.6.224 Next Work Selection Using Risk-Tiered Granularity",
    "runtime demo remains necessary but deferred",
    "Publication remains deferred",
]


REQUIRED_REPOSITORY_TOKENS = [
    "v0.6.223",
    "Existing Element Inventory Review and Decision",
    "accepted for minimum flow planning",
    "not applied",
    "v0.6.224 Next Work Selection Using Risk-Tiered Granularity",
    "no minimum flow package is created in v0.6.223",
    "no private generated outputs are moved public in v0.6.223",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
]


FORBIDDEN_TOKENS = [
    "existing_element_inventory_applied_to_package = true",
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


def test_v06223_files_exist_and_record_review_decision() -> None:
    assert_contains_all(DOC, REQUIRED_DECISION_TOKENS)
    assert_contains_all(DOC, REQUIRED_ACCEPTANCE_TOKENS)
    assert_contains_all(ADR, REQUIRED_DECISION_TOKENS)
    assert_contains_all(ISSUE, ["accepted for future minimum flow planning", "No minimum flow package is created in this checkpoint", "runtime demo remains necessary but deferred"])


def test_v06223_repository_surfaces_review_decision() -> None:
    for path in [README, CHANGELOG, ROADMAP]:
        assert_contains_all(path, REQUIRED_REPOSITORY_TOKENS)


# v0.6.356 scope note: README/CHANGELOG/ROADMAP are rolling aggregate files; historical forbidden-token checks stay scoped to checkpoint-local artifacts.
def test_v06223_does_not_apply_inventory_flow_cleanup_gateway_runtime_publication_or_assurance_changes() -> None:
    for path in [DOC, ADR, ISSUE]:
        text = read(path)
        for token in FORBIDDEN_TOKENS:
            assert token not in text, f"{path.relative_to(ROOT)} contains forbidden token: {token}"


def test_v06223_run_all_registers_local_test() -> None:
    run_all = read(RUN_ALL)
    assert "tools/test_v06223_existing_element_inventory_review_and_decision.py" in run_all


if __name__ == "__main__":
    test_v06223_files_exist_and_record_review_decision()
    test_v06223_repository_surfaces_review_decision()
    test_v06223_does_not_apply_inventory_flow_cleanup_gateway_runtime_publication_or_assurance_changes()
    test_v06223_run_all_registers_local_test()
    print("v0.6.223 Existing Element Inventory Review and Decision checks passed")
