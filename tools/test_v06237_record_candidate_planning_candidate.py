from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/313-v06237-record-candidate-planning-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0313-add-v06237-record-candidate-planning-candidate.md"
ISSUE = ROOT / "planning/issues/0313-add-v06237-record-candidate-planning-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "record_candidate_planning_candidate_created = true",
    "record_candidate_planning_candidate_id = record_candidate_planning_candidate_v06237",
    "record_candidate_planning_candidate_status = candidate_not_applied",
    "record_candidate_planning_candidate_scope = documentation_only_record_candidate_planning",
    "selected_work_item = record_candidate_planning",
    "selected_work_item_status = record_candidate_planning_candidate_created",
    "accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package",
    "accepted_future_record_planning_candidate = future_record_planning_candidate_v06234",
    "future_record_candidate_artifacts_planned = true",
    "record_candidate_artifacts_created = false",
    "record_candidates_created = false",
    "actual_records_created = false",
    "records_created = false",
    "minimum_flow_package_created = false",
    "package_implementation_created = false",
    "fixtures_created = false",
    "fixtures_modified = false",
    "fixture_planning_created = false",
    "evidence_linkage_records_created = false",
    "model_output_reference_record_candidates_created = false",
    "tool_action_request_record_candidates_created = false",
    "gate_decision_record_candidates_created = false",
    "dispatch_decision_record_candidates_created = false",
    "non_dispatch_decision_record_candidates_created = false",
    "execution_result_record_candidates_created = false",
    "non_execution_result_record_candidates_created = false",
    "evidence_event_record_candidates_created = false",
    "reviewer_reconstruction_reference_record_candidates_created = false",
    "aaef_five_questions_mapping_reference_record_candidates_created = false",
    "model_output_reference_records_created = false",
    "tool_action_request_records_created = false",
    "gate_decision_records_created = false",
    "dispatch_decision_records_created = false",
    "non_dispatch_decision_records_created = false",
    "dispatch_evidence_records_created = false",
    "non_dispatch_evidence_records_created = false",
    "execution_result_records_created = false",
    "non_execution_result_records_created = false",
    "evidence_event_records_created = false",
    "reviewer_reconstruction_reference_records_created = false",
    "aaef_five_questions_mapping_reference_records_created = false",
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


REQUIRED_RECORD_CANDIDATE_TOKENS = [
    "model_output_reference_record_candidate",
    "tool_action_request_record_candidate",
    "gate_decision_record_candidate",
    "dispatch_decision_record_candidate",
    "non_dispatch_decision_record_candidate",
    "execution_result_record_candidate",
    "non_execution_result_record_candidate",
    "evidence_event_record_candidate",
    "reviewer_reconstruction_reference_record_candidate",
    "aaef_five_questions_mapping_reference_record_candidate",
]


REQUIRED_DOC_TOKENS = [
    "v0.6.237 Record Candidate Planning Candidate",
    "Previous checkpoint: v0.6.236 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `record_candidate_planning`",
    "Candidate result: record candidate planning candidate created",
    "Application status: planning only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.237.",
    "record_candidate_planning_candidate_id = record_candidate_planning_candidate_v06237",
    "record_candidate_planning_candidate_status = candidate_not_applied",
    "record_candidate_planning_candidate_scope = documentation_only_record_candidate_planning",
    "Planned future record candidate artifacts",
    "Planned candidate artifact linkage",
    "This candidate linkage model is planning only. It is not an implemented schema, not a generated record candidate artifact set, not an actual record set, not a fixture, not runtime behavior, and not scanner behavior.",
    "Planned minimum candidate fields",
    "model_output_authority_status = not_authority",
    "model_output_rationale_authorization_status = not_authorization",
    "dispatch_ai_self_approval_status = prohibited",
    "evidence_reconstruction_status = supports_reconstruction_not_legal_proof",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "record candidate planning is not record candidate artifact creation",
    "record candidate planning is not actual record creation",
    "future record planning is not schema implementation",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.238 Record Candidate Planning Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06237_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_RECORD_CANDIDATE_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06237_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0313",
            "Status: proposed candidate",
            "Create a documentation-only Record Candidate Planning Candidate",
            "record_candidate_planning_candidate_id = record_candidate_planning_candidate_v06237",
            "record_candidate_planning_candidate_status = candidate_not_applied",
            "record_candidate_planning_candidate_scope = documentation_only_record_candidate_planning",
            "model output reference, tool action request, gate decision, dispatch decision, non-dispatch decision, execution result, non-execution result, evidence event, reviewer reconstruction reference, and AAEF five questions mapping reference",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.237.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06237_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0313 - Add v0.6.237 Record Candidate Planning Candidate",
            "Status: completed by v0.6.237",
            "record_candidate_planning",
            "record_candidate_planning_candidate_created = true",
            "record_candidate_planning_candidate_id = record_candidate_planning_candidate_v06237",
            "record_candidate_planning_candidate_status = candidate_not_applied",
            "record_candidate_planning_candidate_scope = documentation_only_record_candidate_planning",
            "future_record_candidate_artifacts_planned = true",
            "record_candidate_artifacts_created = false",
            "SCN-001 permitted safe diagnostic",
            "SCN-002 denied out-of-scope request",
            "SCN-003 held / requires human approval",
            "SCN-004 expired-not-executed",
            "No record candidate artifacts, actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.238 Record Candidate Planning Review and Decision",
        ]
        + REQUIRED_RECORD_CANDIDATE_TOKENS,
    )


def test_v06237_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.237 Record Candidate Planning Candidate",
            "record_candidate_planning",
            "documentation-only Record Candidate Planning Candidate",
            "model output reference, tool action request, gate decision, dispatch decision, non-dispatch decision, execution result, non-execution result, evidence event, reviewer reconstruction reference, and AAEF five questions mapping reference",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.237.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.237 - Record Candidate Planning Candidate",
            "Created a documentation-only Record Candidate Planning Candidate",
            "record_candidate_planning_candidate_created = true",
            "record_candidate_planning_candidate_id = record_candidate_planning_candidate_v06237",
            "future_record_candidate_artifacts_planned = true",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.237",
            "v0.6.238 Record Candidate Planning Review and Decision",
            "no record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06237_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06237_record_candidate_planning_candidate.py",
        ],
    )


def main() -> None:
    test_v06237_doc_tokens()
    test_v06237_adr_tokens()
    test_v06237_issue_tokens()
    test_v06237_index_tokens()
    test_v06237_registered_in_run_all()
    print("v0.6.237 record candidate planning candidate checks passed")


if __name__ == "__main__":
    main()
