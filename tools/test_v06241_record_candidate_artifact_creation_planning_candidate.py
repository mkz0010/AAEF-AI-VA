from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/316-v06241-record-candidate-artifact-creation-planning-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0316-add-v06241-record-candidate-artifact-creation-planning-candidate.md"
ISSUE = ROOT / "planning/issues/0316-add-v06241-record-candidate-artifact-creation-planning-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"


REQUIRED_DECISION_TOKENS = [
    "record_candidate_artifact_creation_planning_candidate_created = true",
    "record_candidate_artifact_creation_planning_candidate_id = record_candidate_artifact_creation_planning_candidate_v06241",
    "record_candidate_artifact_creation_planning_candidate_status = candidate_not_applied",
    "record_candidate_artifact_creation_planning_candidate_scope = documentation_only_record_candidate_artifact_creation_planning",
    "selected_work_item = record_candidate_artifact_creation_planning",
    "selected_work_item_status = record_candidate_artifact_creation_planning_candidate_created",
    "accepted_package_boundary = tool_action_request_gate_decision_dispatch_evidence_package",
    "accepted_future_record_planning_candidate = future_record_planning_candidate_v06234",
    "accepted_record_candidate_planning_candidate = record_candidate_planning_candidate_v06237",
    "future_record_candidate_artifact_families_planned = true",
    "future_record_candidate_artifact_sets_planned = true",
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
    "v0.6.241 Record Candidate Artifact Creation Planning Candidate",
    "Previous checkpoint: v0.6.240 Next Work Selection Using Risk-Tiered Granularity",
    "Selected work item: `record_candidate_artifact_creation_planning`",
    "Application status: planning only; no record candidate artifacts created",
    "No private generated outputs are moved public in v0.6.241.",
    "Planned future artifact families",
    "Planned artifact creation grouping",
    "This artifact creation grouping model is planning only. It is not an implemented schema, not a generated record candidate artifact set, not an actual record set, not a fixture, not runtime behavior, and not scanner behavior.",
    "SCN-001 permitted safe diagnostic",
    "SCN-002 denied out-of-scope request",
    "SCN-003 held / requires human approval",
    "SCN-004 expired-not-executed",
    "candidate artifacts are not actual records",
    "candidate artifacts are not runtime behavior",
    "candidate artifacts are not scanner behavior",
    "model_output_authority_status = not_authority",
    "model_output_rationale_authorization_status = not_authorization",
    "dispatch_ai_self_approval_status = prohibited",
    "evidence_reconstruction_status = supports_reconstruction_not_legal_proof",
    "record candidate artifact creation planning is not record candidate artifact creation",
    "record candidate artifact creation planning is not actual record creation",
    "Model output is not authority.",
    "AI rationale is not authorization.",
    "A gate decision is not AI self-approval.",
    "Evidence supports reconstruction; it does not prove legal truth.",
    "validator success is structural only",
    "runtime demo remains necessary but deferred",
    "publication remains deferred",
    "v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
]


def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")


def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"


def test_v06241_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_ARTIFACT_TOKENS + REQUIRED_DECISION_TOKENS)


def test_v06241_adr_tokens() -> None:
    assert_tokens(
        ADR,
        [
            "ADR-0316",
            "Status: proposed candidate",
            "Create a documentation-only Record Candidate Artifact Creation Planning Candidate",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "No private generated outputs are moved public in v0.6.241.",
        ] + REQUIRED_DECISION_TOKENS,
    )


def test_v06241_issue_tokens() -> None:
    assert_tokens(
        ISSUE,
        [
            "0316 - Add v0.6.241 Record Candidate Artifact Creation Planning Candidate",
            "Status: completed by v0.6.241",
            "record_candidate_artifact_creation_planning",
            "No record candidate artifacts, actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.",
            "Proceed to v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
        ] + REQUIRED_ARTIFACT_TOKENS[1:],
    )


def test_v06241_index_tokens() -> None:
    assert_tokens(
        README,
        [
            "v0.6.241 Record Candidate Artifact Creation Planning Candidate",
            "record_candidate_artifact_creation_planning",
            "does not create record candidate artifacts",
            "Runtime demo remains necessary but deferred.",
            "Publication remains deferred.",
            "Evidence supports reconstruction; it does not prove legal truth.",
            "No private generated outputs are moved public in v0.6.241.",
        ],
    )
    assert_tokens(
        CHANGELOG,
        [
            "v0.6.241 - Record Candidate Artifact Creation Planning Candidate",
            "record_candidate_artifact_creation_planning_candidate_created = true",
            "future_record_candidate_artifact_families_planned = true",
            "future_record_candidate_artifact_sets_planned = true",
            "validator success is structural only",
            "evidence supports reconstruction; it does not prove legal truth",
        ],
    )
    assert_tokens(
        ROADMAP,
        [
            "After v0.6.241",
            "v0.6.242 Record Candidate Artifact Creation Planning Review and Decision",
            "no record candidate artifact creation",
            "no actual record creation",
            "no fixture creation",
            "no runtime demo readiness claim",
            "no scanner readiness claim",
            "no external PoC readiness claim",
            "no publication approval",
        ],
    )


def test_v06241_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06241_record_candidate_artifact_creation_planning_candidate.py"])


def main() -> None:
    test_v06241_doc_tokens()
    test_v06241_adr_tokens()
    test_v06241_issue_tokens()
    test_v06241_index_tokens()
    test_v06241_registered_in_run_all()
    print("v0.6.241 record candidate artifact creation planning candidate checks passed")


if __name__ == "__main__":
    main()
