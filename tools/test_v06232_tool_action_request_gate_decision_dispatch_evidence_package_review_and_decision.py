from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/308-v06232-tool-action-request-gate-decision-dispatch-evidence-package-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0308-add-v06232-tool-action-request-gate-decision-dispatch-evidence-package-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0308-add-v06232-tool-action-request-gate-decision-dispatch-evidence-package-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "package_candidate_review_completed = true",
    "package_candidate_accepted = true",
    "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
    "package_candidate_review_result = accepted_for_future_fixture_and_record_planning",
    "package_candidate_status = accepted_for_future_fixture_and_record_planning",
    "package_candidate_applied = false",
    "selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package",
    "selected_work_item_status = accepted_package_boundary_for_future_planning",
    "accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package",
    "accepted_package_boundary_application_status = not_applied",
    "minimum_flow_package_created = false",
    "package_implementation_created = false",
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
    "v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
    "Previous checkpoint: v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
    "Reviewed candidate: `tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231`",
    "Decision result: accepted for future fixture and record planning",
    "Application status: not applied to fixtures, records, runtime, or scanner behavior",
    "package_candidate_previous_status = candidate_not_applied",
    "package_candidate_review_result = accepted_for_future_fixture_and_record_planning",
    "package_candidate_application_status = not_applied",
    "model output reference is a request source only",
    "tool action request records the proposed action",
    "gate decision records the authorization gate result",
    "dispatch decision records execution dispatch only when allowed",
    "non-dispatch decision records denied, held, or expired paths",
    "execution result records controlled execution outcomes only when dispatch occurs",
    "non-execution result records why execution did not occur",
    "evidence event links request, decision, dispatch or non-dispatch, and result",
    "reviewer reconstruction path supports future review without treating evidence as legal proof",
    "AAEF five questions mapping reference remains a future artifact reference",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package",
    "accepted_package_boundary_status = accepted_for_future_fixture_and_record_planning",
    "accepted_package_boundary_application_status = not_applied",
    "accepted_package_boundary_runtime_status = no_runtime_behavior",
    "accepted_package_boundary_scanner_status = no_scanner_behavior",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "accepted package boundary is not an implemented package",
    "accepted package boundary is not a minimum flow package",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "No private generated outputs are moved public in v0.6.232.",
    "v0.6.233 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06232_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06232_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0308",
            "Status: accepted",
            "Accept the v0.6.231 candidate package shape for future fixture and record planning.",
            "package_candidate_review_completed = true",
            "package_candidate_accepted = true",
            "package_candidate_status = accepted_for_future_fixture_and_record_planning",
            "package_candidate_applied = false",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.232.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06232_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0308 - Add v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
            "Status: completed by v0.6.232",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "package_candidate_review_completed = true",
            "package_candidate_accepted = true",
            "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
            "package_candidate_review_result = accepted_for_future_fixture_and_record_planning",
            "package_candidate_status = accepted_for_future_fixture_and_record_planning",
            "package_candidate_applied = false",
            "model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference",
            "SCN-001 permitted safe diagnostic",
            "SCN-002 denied out-of-scope request",
            "SCN-003 held / requires human approval",
            "SCN-004 expired-not-executed",
            "No minimum flow package, package implementation, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.233 Next Work Selection Using Risk-Tiered Granularity",
        ],
    )


def test_v06232_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
            "accepts the v0.6.231 documentation-only candidate package shape for future fixture and record planning",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "package_candidate_accepted = true",
            "package_candidate_status = accepted_for_future_fixture_and_record_planning",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.232.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.232 - Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
            "Accepted the v0.6.231 documentation-only candidate package shape",
            "package_candidate_review_completed = true",
            "package_candidate_accepted = true",
            "package_candidate_status = accepted_for_future_fixture_and_record_planning",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.232",
            "v0.6.233 Next Work Selection Using Risk-Tiered Granularity",
            "future fixture and record planning",
            "future fixture planning, future record planning, reviewer walkthrough planning, or AAEF five questions mapping planning",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06232_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06232_tool_action_request_gate_decision_dispatch_evidence_package_review_and_decision.py",
        ],
    )


def main() -> None:
    test_v06232_doc_tokens()
    test_v06232_adr_tokens()
    test_v06232_issue_tokens()
    test_v06232_index_tokens()
    test_v06232_registered_in_run_all()
    print("v0.6.232 tool action request gate decision dispatch evidence package review and decision checks passed")


if __name__ == "__main__":
    main()
