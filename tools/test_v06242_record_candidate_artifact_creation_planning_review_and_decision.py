from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/317-v06242-record-candidate-artifact-creation-planning-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0317-add-v06242-record-candidate-artifact-creation-planning-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0317-add-v06242-record-candidate-artifact-creation-planning-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "record_candidate_artifact_creation_planning_candidate_review_completed = true",
    "record_candidate_artifact_creation_planning_candidate_accepted = true",
    "record_candidate_artifact_creation_planning_candidate_id = record_candidate_artifact_creation_planning_candidate_v06241",
    "record_candidate_artifact_creation_planning_candidate_review_result = accepted_for_future_record_candidate_artifact_creation_candidate_work",
    "record_candidate_artifact_creation_planning_candidate_status = accepted_for_future_record_candidate_artifact_creation_candidate_work",
    "record_candidate_artifact_creation_planning_candidate_applied = false",
    "selected_work_item = record_candidate_artifact_creation_planning",
    "selected_work_item_status = accepted_for_future_record_candidate_artifact_creation_candidate_work",
    "accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package",
    "accepted_future_record_planning_candidate = future_record_planning_candidate_v06234",
    "accepted_record_candidate_planning_candidate = record_candidate_planning_candidate_v06237",
    "future_record_candidate_artifact_families_accepted = true",
    "future_record_candidate_artifact_sets_accepted = true",
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

REQUIRED_ARTIFACT_TOKENS = [
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
    "v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
    "Previous checkpoint: v0.6.241 Record Candidate Artifact Creation Planning Candidate",
    "Reviewed candidate: `record_candidate_artifact_creation_planning_candidate_v06241`",
    "Decision result: accepted for future record candidate artifact creation candidate work",
    "Application status: review only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.242.",
    "record_candidate_artifact_creation_planning_candidate_previous_status = candidate_not_applied",
    "record_candidate_artifact_creation_planning_candidate_review_result = accepted_for_future_record_candidate_artifact_creation_candidate_work",
    "future artifact families are accepted for future record candidate artifact creation candidate work",
    "This accepted artifact creation grouping model remains a planning model only. It is not an implemented schema, not a generated record candidate artifact set, not an actual record set, not a fixture, not runtime behavior, and not scanner behavior.",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06242_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_ARTIFACT_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06242_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0317",
            "Status: accepted",
            "Accept the v0.6.241 Record Candidate Artifact Creation Planning Candidate",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.242.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06242_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0317 - Add v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
            "Status: completed by v0.6.242",
            "future_record_candidate_artifact_families_accepted = true",
            "future_record_candidate_artifact_sets_accepted = true",
            "No record candidate artifacts, actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
        ] + REQUIRED_ARTIFACT_TOKENS[1:],
    )


def test_v06242_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
            "record_candidate_artifact_creation_planning_candidate_v06241",
            "record_candidate_artifact_creation_planning_candidate_accepted = true",
            "future_record_candidate_artifact_families_accepted = true",
            "future_record_candidate_artifact_sets_accepted = true",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.242.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.242 - Record Candidate Artifact Creation Planning Review and Decision",
            "Accepted the v0.6.241 documentation-only Record Candidate Artifact Creation Planning Candidate",
            "record_candidate_artifact_creation_planning_candidate_review_completed = true",
            "record_candidate_artifact_creation_planning_candidate_accepted = true",
            "future_record_candidate_artifact_families_accepted = true",
            "future_record_candidate_artifact_sets_accepted = true",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.242",
            "v0.6.243 Next Work Selection Using Risk-Tiered Granularity",
            "record candidate artifact creation candidate, future fixture planning, reviewer walkthrough planning, or AAEF five questions mapping planning",
            "no record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06242_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06242_record_candidate_artifact_creation_planning_review_and_decision.py"])


def main() -> None:
    test_v06242_doc_tokens()
    test_v06242_adr_tokens()
    test_v06242_issue_tokens()
    test_v06242_index_tokens()
    test_v06242_registered_in_run_all()
    print("v0.6.242 record candidate artifact creation planning review and decision checks passed")


if __name__ == "__main__":
    main()
