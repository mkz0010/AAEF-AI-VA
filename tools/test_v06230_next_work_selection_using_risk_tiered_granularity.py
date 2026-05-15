from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/306-v06230-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0306-add-v06230-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0306-add-v06230-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selection_applied_to_package = false",
    "minimum_flow_package_created = false",
    "package_candidate_created = false",
    "fixtures_created = false",
    "fixtures_modified = false",
    "evidence_linkage_records_created = false",
    "tool_action_request_records_created = false",
    "gate_decision_records_created = false",
    "dispatch_evidence_records_created = false",
    "non_dispatch_evidence_records_created = false",
    "execution_result_records_created = false",
    "non_execution_result_records_created = false",
    "evidence_event_records_created = false",
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
    "v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.229 Evidence Linkage Table Review and Decision",
    "Selection result: `tool_action_request_gate_decision_dispatch_evidence_package`",
    "Application status: selection only; not applied",
    "v0.6.229 accepted Evidence Linkage Table Review and Decision",
    "model output as request source",
    "`tool_action_request`",
    "gate decision",
    "dispatch decision or non-dispatch decision",
    "execution result or non-execution result",
    "evidence event",
    "reviewer reconstruction path",
    "selected next work item is not an implemented package",
    "Model output is not authority.",
    "AI rationale is not authorization",
    "gate decision is not AI self-approval",
    "evidence supports reconstruction; it does not prove legal truth",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "No private generated outputs are moved public in v0.6.230.",
    "v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06230_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06230_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0306",
            "Status: accepted",
            "Select the following next work item",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "This is a selection-only checkpoint.",
            "The selected package is not created in v0.6.230.",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.230.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06230_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0306 - Add v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.230",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "next_work_selection_completed = true",
            "selected_work_item_status = selected_for_next_candidate_checkpoint",
            "The selected package is not created in v0.6.230.",
            "No minimum flow package, package candidate, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
        ],
    )


def test_v06230_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "This is selection only.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.230.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.230 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `tool_action_request_gate_decision_dispatch_evidence_package` as the next work item.",
            "next_work_selection_completed = true",
            "selected_work_item_status = selected_for_next_candidate_checkpoint",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.230",
            "v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06230_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06230_next_work_selection_using_risk_tiered_granularity.py",
        ],
    )


def main() -> None:
    test_v06230_doc_tokens()
    test_v06230_adr_tokens()
    test_v06230_issue_tokens()
    test_v06230_index_tokens()
    test_v06230_registered_in_run_all()
    print("v0.6.230 next work selection checks passed")


if __name__ == "__main__":
    main()
