from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/312-v06236-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0312-add-v06236-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0312-add-v06236-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = record_candidate_planning",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_future_record_planning_requires_record_candidate_planning_before_fixture_creation",
    "selection_applied_to_record_candidates = false",
    "record_candidate_planning_selected = true",
    "future_fixture_planning_selected = false",
    "reviewer_walkthrough_planning_selected = false",
    "aaef_five_questions_mapping_planning_selected = false",
    "record_candidate_planning_candidate_created = false",
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


REQUIRED_RECORD_CANDIDATE_SCOPE_TOKENS = [
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
    "v0.6.236 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.235 Future Record Planning Review and Decision",
    "Selection result: `record_candidate_planning`",
    "Application status: selection only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.236.",
    "v0.6.235 accepted the Future Record Planning Candidate for future fixture planning and record candidate planning",
    "record_candidate_planning",
    "Record candidate planning should come before fixture planning",
    "This checkpoint selects record candidate planning only. It does not create any actual record candidate artifacts or actual records.",
    "record candidate planning selection is not record candidate creation",
    "record candidate planning is not actual record creation",
    "future record planning is not schema implementation",
    "Model output is not authority.",
    "AI rationale is not authorization",
    "gate decision is not AI self-approval",
    "evidence supports reconstruction; it does not prove legal truth",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.237 Record Candidate Planning Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06236_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_RECORD_CANDIDATE_SCOPE_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06236_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0312",
            "Status: accepted",
            "Select the following next work item",
            "record_candidate_planning",
            "This is a selection-only checkpoint.",
            "No record candidate artifacts, actual records, fixtures, reviewer walkthrough, AAEF five questions mapping, AAEF handback summary, runtime behavior, scanner behavior, publication approval, or public announcement are created in v0.6.236.",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.236.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06236_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0312 - Add v0.6.236 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.236",
            "record_candidate_planning",
            "next_work_selection_completed = true",
            "selected_work_item = record_candidate_planning",
            "record_candidate_planning_selected = true",
            "selection_applied_to_record_candidates = false",
            "No record candidate artifacts are created in v0.6.236.",
            "No actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.237 Record Candidate Planning Candidate",
        ],
    )


def test_v06236_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.236 Next Work Selection Using Risk-Tiered Granularity",
            "record_candidate_planning",
            "This is selection only.",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.236.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.236 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `record_candidate_planning` as the next work item",
            "next_work_selection_completed = true",
            "record_candidate_planning_selected = true",
            "selection_applied_to_record_candidates = false",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.236",
            "v0.6.237 Record Candidate Planning Candidate",
            "documentation-only candidate plan for future record candidate artifacts",
            "no record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06236_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06236_next_work_selection_using_risk_tiered_granularity.py",
        ],
    )


def main() -> None:
    test_v06236_doc_tokens()
    test_v06236_adr_tokens()
    test_v06236_issue_tokens()
    test_v06236_index_tokens()
    test_v06236_registered_in_run_all()
    print("v0.6.236 next work selection checks passed")


if __name__ == "__main__":
    main()
