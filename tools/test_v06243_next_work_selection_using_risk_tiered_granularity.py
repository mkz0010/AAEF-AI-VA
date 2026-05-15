from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/318-v06243-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0318-add-v06243-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0318-add-v06243-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "next_work_selection_completed = true",
    "selected_work_item = record_candidate_artifact_creation_candidate",
    "selected_work_item_status = selected_for_next_candidate_checkpoint",
    "selected_work_item_reason = accepted_artifact_creation_planning_requires_candidate_before_artifact_review_or_fixture_planning",
    "selection_applied_to_record_candidate_artifacts = false",
    "record_candidate_artifact_creation_candidate_selected = true",
    "future_fixture_planning_selected = false",
    "reviewer_walkthrough_planning_selected = false",
    "aaef_five_questions_mapping_planning_selected = false",
    "record_candidate_artifact_creation_candidate_created = false",
    "record_candidate_artifacts_created = false",
    "actual_records_created = false",
    "records_created = false",
    "fixtures_created = false",
    "runtime_behavior_changed = false",
    "scanner_behavior_changed = false",
    "publication_approval = false",
    "production_readiness_claim = false",
    "certification_claim = false",
    "legal_compliance_claim = false",
    "audit_opinion_claim = false",
    "diagnostic_completeness_claim = false",
    "external_framework_equivalence_claim = false",
]

REQUIRED_ARTIFACT_SCOPE_TOKENS = [
    "record_candidate_artifact_set",
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
    "v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
    "Previous checkpoint: v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
    "Selection result: `record_candidate_artifact_creation_candidate`",
    "Application status: selection only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.243.",
    "record_candidate_artifact_creation_candidate",
    "record candidate artifact creation candidate work as the next work item",
    "This checkpoint uses the risk-tiered granularity policy",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.244 Record Candidate Artifact Creation Candidate",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06243_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_ARTIFACT_SCOPE_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06243_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0318",
            "Status: accepted",
            "Select the following next work item",
            "record_candidate_artifact_creation_candidate",
            "This is a selection-only checkpoint.",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.243.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06243_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0318 - Add v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
            "Status: completed by v0.6.243",
            "record_candidate_artifact_creation_candidate",
            "No record candidate artifacts are created in v0.6.243.",
            "Proceed to v0.6.244 Record Candidate Artifact Creation Candidate",
        ],
    )


def test_v06243_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
            "record_candidate_artifact_creation_candidate",
            "This is selection only.",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.243.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.243 - Next Work Selection Using Risk-Tiered Granularity",
            "Selected `record_candidate_artifact_creation_candidate` as the next work item",
            "next_work_selection_completed = true",
            "record_candidate_artifact_creation_candidate_selected = true",
            "selection_applied_to_record_candidate_artifacts = false",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.243",
            "v0.6.244 Record Candidate Artifact Creation Candidate",
            "no actual record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06243_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06243_next_work_selection_using_risk_tiered_granularity.py"])


def main() -> None:
    test_v06243_doc_tokens()
    test_v06243_adr_tokens()
    test_v06243_issue_tokens()
    test_v06243_index_tokens()
    test_v06243_registered_in_run_all()
    print("v0.6.243 next work selection checks passed")


if __name__ == "__main__":
    main()
