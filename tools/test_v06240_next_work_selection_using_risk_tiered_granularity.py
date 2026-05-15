from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/315-v06240-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0315-add-v06240-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0315-add-v06240-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = record_candidate_artifact_creation_planning",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_record_candidate_planning_requires_artifact_creation_planning_before_artifact_creation",
    "selection_applied_to_record_candidate_artifacts = false",
    "record_candidate_artifact_creation_planning_selected = true",
    "future_fixture_planning_selected = false",
    "reviewer_walkthrough_planning_selected = false",
    "aaef_five_questions_mapping_planning_selected = false",
    "record_candidate_artifact_creation_planning_candidate_created = false",
    "record_candidate_artifact_creation_candidate_created = false",
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
    "model_output_reference_record_candidate_artifacts_created = false",
    "tool_action_request_record_candidate_artifacts_created = false",
    "gate_decision_record_candidate_artifacts_created = false",
    "dispatch_decision_record_candidate_artifacts_created = false",
    "non_dispatch_decision_record_candidate_artifacts_created = false",
    "execution_result_record_candidate_artifacts_created = false",
    "non_execution_result_record_candidate_artifacts_created = false",
    "evidence_event_record_candidate_artifacts_created = false",
    "reviewer_reconstruction_reference_record_candidate_artifacts_created = false",
    "aaef_five_questions_mapping_reference_record_candidate_artifacts_created = false",
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


REQUIRED_ARTIFACT_SCOPE_TOKENS = [
    "model_output_reference_record_candidate_artifact",
    "tool_action_request_record_candidate_artifact",
    "gate_decision_record_candidate_artifact",
    "dispatch_decision_record_candidate_artifact",
    "non_dispatch_decision_record_candidate_artifact",
    "execution_result_record_candidate_artifact",
    "non_execution_result_record_candidate_artifact",
    "evidence_event_record_candidate_artifact",
    "reviewer_reconstruction_reference_record_candidate_artifact",
    "aaef_five_questions_mapping_reference_record_candidate_artifact",
]


REQUIRED_DOC_TOKENS = [
    "v0.6.240 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.239 Record Candidate Planning Review and Decision",
    "Selection result: `record_candidate_artifact_creation_planning`",
    "Application status: selection only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.240.",
    "v0.6.239 accepted the Record Candidate Planning Candidate for future record candidate artifact creation planning",
    "record_candidate_artifact_creation_planning",
    "Record candidate artifact creation planning should come before fixture planning",
    "This checkpoint selects record candidate artifact creation planning only. It does not create any actual record candidate artifacts or actual records.",
    "record candidate artifact creation planning selection is not record candidate artifact creation",
    "record candidate artifact creation planning is not actual record creation",
    "future record planning is not schema implementation",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.241 Record Candidate Artifact Creation Planning Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06240_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_ARTIFACT_SCOPE_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06240_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0315",
            "Status: accepted",
            "Select the following next work item",
            "record_candidate_artifact_creation_planning",
            "This is a selection-only checkpoint.",
            "No record candidate artifacts, actual records, fixtures, reviewer walkthrough, AAEF five questions mapping, AAEF handback summary, runtime behavior, scanner behavior, publication approval, or public announcement are created in v0.6.240.",
            "Model output is not authority.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.240.",
        ]
        + REQUIRED_DECISION_TOKENS,
    )


def test_v06240_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0315 - Add v0.6.240 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.240",
            "record_candidate_artifact_creation_planning",
            "next_work_selection_completed = true",
            "selected_work_item = record_candidate_artifact_creation_planning",
            "record_candidate_artifact_creation_planning_selected = true",
            "selection_applied_to_record_candidate_artifacts = false",
            "No record candidate artifacts are created in v0.6.240.",
            "No actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.241 Record Candidate Artifact Creation Planning Candidate",
        ],
    )


def test_v06240_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.240 Next Work Selection Using Risk-Tiered Granularity",
            "record_candidate_artifact_creation_planning",
            "This is selection only.",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.240.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.240 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `record_candidate_artifact_creation_planning` as the next work item",
            "next_work_selection_completed = true",
            "record_candidate_artifact_creation_planning_selected = true",
            "selection_applied_to_record_candidate_artifacts = false",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.240",
            "v0.6.241 Record Candidate Artifact Creation Planning Candidate",
            "documentation-only candidate plan for future record candidate artifact creation",
            "no record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06240_registered_in_run_all() -> None:
    assert_tokens(
        RUN_ALL,
        [
            "tools/test_v06240_next_work_selection_using_risk_tiered_granularity.py",
        ],
    )


def main() -> None:
    test_v06240_doc_tokens()
    test_v06240_adr_tokens()
    test_v06240_issue_tokens()
    test_v06240_index_tokens()
    test_v06240_registered_in_run_all()
    print("v0.6.240 next work selection checks passed")


if __name__ == "__main__":
    main()
