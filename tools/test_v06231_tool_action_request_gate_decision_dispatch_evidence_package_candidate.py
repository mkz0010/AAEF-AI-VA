from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/307-v06231-tool-action-request-gate-decision-dispatch-evidence-package-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0307-add-v06231-tool-action-request-gate-decision-dispatch-evidence-package-candidate.md"
ISSUE = ROOT / "planning/issues/0307-add-v06231-tool-action-request-gate-decision-dispatch-evidence-package-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "package_candidate_created = true",
    "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
    "package_candidate_status = candidate_not_applied",
    "package_candidate_scope = documentation_only_package_shape",
    "selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package",
    "selected_work_item_status = candidate_package_shape_created",
    "minimum_flow_package_created = false",
    "package_candidate_applied = false",
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
    "v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
    "Previous checkpoint: v0.6.230 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `tool_action_request_gate_decision_dispatch_evidence_package`",
    "Application status: candidate only; not applied to fixtures, records, runtime, or scanner behavior",
    "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
    "package_candidate_status = candidate_not_applied",
    "package_candidate_scope = documentation_only_package_shape",
    "model_output_reference",
    "tool_action_request",
    "gate_decision",
    "dispatch_decision",
    "non_dispatch_decision",
    "execution_result",
    "non_execution_result",
    "evidence_event",
    "reviewer_reconstruction_path",
    "aaef_five_questions_mapping_reference",
    "model_output_authority_status = not_authority",
    "model_output_rationale_authorization_status = not_authorization",
    "dispatch_ai_self_approval_status = prohibited",
    "evidence_reconstruction_status = supports_reconstruction_not_legal_proof",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "candidate package shape is not an implemented package",
    "candidate package shape is not a minimum flow package",
    "Model output is not authority.",
    "AI rationale is not authorization",
    "gate decision is not AI self-approval",
    "evidence supports reconstruction; it does not prove legal truth",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "No private generated outputs are moved public in v0.6.231.",
    "v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06231_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06231_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0307",
            "Status: proposed candidate",
            "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
            "package_candidate_status = candidate_not_applied",
            "package_candidate_scope = documentation_only_package_shape",
            "model output reference",
            "tool action request",
            "gate decision",
            "dispatch or non-dispatch decision",
            "execution or non-execution result",
            "evidence event",
            "reviewer reconstruction path",
            "AAEF five questions mapping reference",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.231.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06231_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0307 - Add v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
            "Status: completed by v0.6.231",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "package_candidate_created = true",
            "package_candidate_id = tool_action_request_gate_decision_dispatch_evidence_package_candidate_v06231",
            "package_candidate_status = candidate_not_applied",
            "package_candidate_scope = documentation_only_package_shape",
            "model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference",
            "SCN-001 permitted safe diagnostic",
            "SCN-002 denied out-of-scope request",
            "SCN-003 held / requires human approval",
            "SCN-004 expired-not-executed",
            "No minimum flow package, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
        ],
    )


def test_v06231_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
            "tool_action_request_gate_decision_dispatch_evidence_package",
            "documentation-only candidate package shape",
            "model output reference, tool action request, gate decision, dispatch or non-dispatch decision, execution or non-execution result, evidence event, reviewer reconstruction path, and AAEF five questions mapping reference",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.231.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.231 - Tool Action Request Gate Decision Dispatch Evidence Package Candidate",
            "Created a documentation-only candidate package shape",
            "package_candidate_created = true",
            "package_candidate_status = candidate_not_applied",
            "package_candidate_scope = documentation_only_package_shape",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.231",
            "v0.6.232 Tool Action Request Gate Decision Dispatch Evidence Package Review and Decision",
            "accepted for future fixture and record planning",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06231_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06231_tool_action_request_gate_decision_dispatch_evidence_package_candidate.py",
        ],
    )


def main() -> None:
    test_v06231_doc_tokens()
    test_v06231_adr_tokens()
    test_v06231_issue_tokens()
    test_v06231_index_tokens()
    test_v06231_registered_in_run_all()
    print("v0.6.231 tool action request gate decision dispatch evidence package candidate checks passed")


if __name__ == "__main__":
    main()
