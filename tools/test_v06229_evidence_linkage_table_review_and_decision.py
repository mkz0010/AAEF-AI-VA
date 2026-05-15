from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/305-v06229-evidence-linkage-table-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0305-add-v06229-evidence-linkage-table-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0305-add-v06229-evidence-linkage-table-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "evidence_linkage_table_accepted = true",
    "evidence_linkage_table_applied_to_package = false",
    "minimum_flow_package_created = false",
    "fixtures_created = false",
    "fixtures_modified = false",
    "evidence_linkage_records_created = false",
    "tool_action_request_records_created = false",
    "gate_decision_records_created = false",
    "dispatch_evidence_records_created = false",
    "execution_result_records_created = false",
    "non_execution_result_records_created = false",
    "reviewer_walkthrough_created = false",
    "aaef_five_questions_mapping_created = false",
    "aaef_handback_summary_created = false",
    "private_generated_outputs_moved_public = false",
    "public_exposure_cleanup_applied = false",
    "readme_front_page_rewritten = false",
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
    "commercial_terms_created = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]


REQUIRED_DOC_TOKENS = [
    "v0.6.229 Evidence Linkage Table Review and Decision",
    "accepted for future package planning / future record planning",
    "Application status: not applied",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "model_output_id",
    "tool_action_request_id",
    "gate_decision_id",
    "dispatch_decision_id / non_dispatch_decision_id",
    "execution_result_id / non_execution_result_id",
    "evidence_event_id",
    "reviewer_walkthrough_id",
    "five_questions_mapping_id",
    "Model output is not authority.",
    "AI rationale is not authorization",
    "gate decision is not AI self-approval",
    "evidence supports reconstruction; it does not prove legal truth",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "No private generated outputs are moved public in v0.6.229.",
    "v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
    "tool_action_request_gate_decision_dispatch_evidence_package",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06229_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06229_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0305",
            "Status: accepted",
            "accepted for future package planning / future record planning",
            "The table is not applied in v0.6.229.",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.229.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06229_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0305 - Add v0.6.229 Evidence Linkage Table Review and Decision",
            "Status: completed by v0.6.229",
            "evidence_linkage_table_accepted = true",
            "evidence_linkage_table_applied_to_package = false",
            "SCN-001 permitted safe diagnostic",
            "SCN-002 denied out-of-scope request",
            "SCN-003 held / requires human approval",
            "SCN-004 expired-not-executed",
            "No minimum flow package, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06229_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.229 Evidence Linkage Table Review and Decision",
            "evidence_linkage_table_accepted = true",
            "evidence_linkage_table_applied_to_package = false",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.229.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.229 - Evidence Linkage Table Review and Decision",
            "Accepted the v0.6.228 Evidence Linkage Table Candidate",
            "evidence_linkage_table_accepted = true",
            "evidence_linkage_table_applied_to_package = false",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.229",
            "accepted for future package planning / future record planning",
            "v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "selection itself remains deferred to v0.6.230",
        ],
    )


def test_v06229_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06229_evidence_linkage_table_review_and_decision.py",
        ],
    )


def main() -> None:
    test_v06229_doc_tokens()
    test_v06229_adr_tokens()
    test_v06229_issue_tokens()
    test_v06229_index_tokens()
    test_v06229_registered_in_run_all()
    print("v0.6.229 evidence linkage table review and decision checks passed")


if __name__ == "__main__":
    main()
