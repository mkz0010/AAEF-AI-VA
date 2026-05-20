from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/443-v06368-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0443-add-v06368-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0443-add-v06368-private-reviewer-gateway-validation-result-evidence-trace-artifact-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"
TEST_NAME = "tools/test_v06368_private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_review_and_decision.py"

REQUIRED = [
    "v0.6.368 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_review_completed = true",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_decision = accepted_for_private_reviewer_evidence_trace_artifact_path",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_accepted = true",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_publication_approved = false",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_schema_changed = false",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_generated_outputs_changed = false",
    "private_reviewer_gateway_validation_result_evidence_trace_artifact_raw_and_reviewer_status_separated = true",
    "gateway_validation_result_application_phase_2_schema_field_decision = deferred",
    "gateway_validation_result_application_phase_3_generated_output_application_decision = deferred",
    "gateway_validation_result_application_phase_4_runtime_application_decision = deferred",
    "v06368_schema_changed = false",
    "v06368_gateway_core_behavior_changed = false",
    "v06368_runtime_behavior_changed = false",
    "v06368_scanner_behavior_changed = false",
    "execution_authorized = false",
    "real_execution_permitted = false",
    "external_target_authorization = false",
    "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review",
    "v0.6.369 Private Reviewer Gateway Validation Result Evidence Trace Artifact Closeout Review",
]

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(DOC, ["| Review item | Decision |", "Private reviewer artifact candidate | accepted"])
    assert_tokens(ADR, ["ADR-0443", "Status: accepted", "Accept the v0.6.367 private reviewer artifact candidate"])
    assert_tokens(ISSUE, ["Status: completed by v0.6.368", "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review"])

def test_index_files() -> None:
    assert_tokens(README, [
        "v0.6.368 Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision",
        "private_reviewer_gateway_validation_result_evidence_trace_artifact_candidate_decision = accepted_for_private_reviewer_evidence_trace_artifact_path",
        "v06368_schema_changed = false",
        "recommended_next_work_item = private_reviewer_gateway_validation_result_evidence_trace_artifact_closeout_review",
    ])
    assert_tokens(CHANGELOG, ["v0.6.368 - Private Reviewer Gateway Validation Result Evidence Trace Artifact Candidate Review and Decision", "private evidence trace artifact path"])
    assert_tokens(ROADMAP, ["After v0.6.368", "v0.6.369 Private Reviewer Gateway Validation Result Evidence Trace Artifact Closeout Review"])

def test_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, [TEST_NAME])

def test_no_unsupported_claims() -> None:
    forbidden = ["production-ready scanner", "runtime-enforced scanner", "external-target-ready demo", "customer-ready PoC", "certified / audit-ready system", "compliance-sufficient control", "diagnostically complete"]
    for path in [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]:
        text = read(path)
        for phrase in forbidden:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains forbidden phrase: {phrase}"

def main() -> None:
    test_primary_files()
    test_index_files()
    test_registered_in_run_all()
    test_no_unsupported_claims()
    print("v0.6.368 private reviewer Gateway validation result evidence trace artifact candidate review and decision checks passed")

if __name__ == "__main__":
    main()
