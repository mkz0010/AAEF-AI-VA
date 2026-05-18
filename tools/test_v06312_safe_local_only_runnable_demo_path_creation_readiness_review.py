from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/387-v06312-safe-local-only-runnable-demo-path-creation-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0387-add-v06312-safe-local-only-runnable-demo-path-creation-readiness-review.md"
ISSUE = ROOT / "planning/issues/0387-add-v06312-safe-local-only-runnable-demo-path-creation-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_path_creation_readiness_review_completed = true', 'safe_local_only_runnable_demo_path_creation_readiness_review_id = safe_local_only_runnable_demo_path_creation_readiness_review_v06312', 'safe_local_only_runnable_demo_path_creation_readiness_review_result = ready_for_creation_candidate_not_created', 'safe_local_only_runnable_demo_path_creation_readiness_review_status = completed_creation_candidate_recommended', 'safe_local_only_runnable_demo_path_creation_readiness_review_scope = readiness_review_only', 'safe_local_only_runnable_demo_path_review_completed = true', 'safe_local_only_runnable_demo_path_accepted = true', 'safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310', 'safe_local_only_runnable_demo_path_status = accepted_not_created', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'readiness_prerequisite_boundary_accepted = true', 'readiness_prerequisite_path_accepted = true', 'readiness_prerequisite_mock_gateway_demo_available = true', 'readiness_prerequisite_public_artifact_accepted = true', 'readiness_prerequisite_local_target_lab_profile_available = true', 'readiness_prerequisite_runtime_destination_binding_available = true', 'readiness_prerequisite_runtime_readiness_gate_available = true', 'readiness_prerequisite_bounded_execution_transition_available = true', 'readiness_prerequisite_local_execution_plan_review_available = true', 'readiness_prerequisite_runtime_safety_policy_available = true', 'readiness_prerequisite_runtime_enforcement_design_available = true', 'readiness_prerequisite_execution_authorization_gate_available = true', 'readiness_prerequisite_preflight_validation_available = true', 'readiness_prerequisite_preflight_evidence_model_available = true', 'readiness_prerequisite_preflight_evidence_examples_available = true', 'readiness_prerequisite_preflight_evidence_validation_rules_available = true', 'readiness_prerequisite_preflight_negative_examples_available = true', 'readiness_prerequisite_private_artifact_exclusion_available = true', 'readiness_prerequisite_claim_boundary_tests_available = true', 'readiness_gap_runtime_path_not_created = true', 'readiness_gap_runtime_enforcement_not_implemented = true', 'readiness_gap_concrete_checks_not_implemented = true', 'readiness_gap_execution_authorization_false = true', 'readiness_gap_preflight_not_satisfied = true', 'readiness_gap_live_evidence_records_not_generated = true', 'readiness_gap_no_external_target_authorization = true', 'creation_candidate_safe_to_prepare = true', 'creation_candidate_should_remain_mock_first = true', 'creation_candidate_should_remain_localhost_only = true', 'creation_candidate_should_keep_execution_blocked_by_default = true', 'creation_candidate_should_use_private_not_in_git_outputs = true', 'creation_candidate_should_not_move_private_outputs_public = true', 'safe_local_only_runnable_demo_path_creation_candidate_created = false', 'safe_local_only_runnable_demo_path_creation_candidate_review_completed = false', 'safe_local_only_runnable_demo_path_creation_candidate_accepted = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_path_applied = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_runnable_demo_review_completed = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'local_only_runnable_demo_path_created = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate', 'safe_local_only_runnable_demo_path_creation_candidate_recommended = true', 'safe_local_only_runnable_demo_path_creation_readiness_review_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_path_creation_readiness_review', 'safe_local_only_runnable_demo_path_creation_readiness_review_v06312', 'safe_local_only_runnable_demo_path_creation_candidate', 'safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_v06310', 'safe_local_only_runnable_demo_path_review_and_decision', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'safe local-only demo execution boundary', 'safe local-only runnable demo path', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo path creation readiness review is not execution authorization', 'safe local-only runnable demo path creation readiness review is not runnable demo creation', 'safe local-only runnable demo path creation readiness review is not runtime-applied enforcement', 'safe local-only runnable demo path creation readiness review is not runtime demo readiness', 'safe local-only runnable demo path creation readiness review is not scanner readiness', 'safe local-only runnable demo path creation readiness review is not production readiness', 'safe local-only runnable demo path creation readiness review is not external target authorization', 'No private generated outputs are moved public in v0.6.312.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.312 Safe Local-Only Runnable Demo Path Creation Readiness Review', 'Previous checkpoint: v0.6.311 Safe Local-Only Runnable Demo Path Review and Decision', 'Readiness result: ready for creation candidate, not created', 'Application status: readiness review only; no runnable demo path created, runtime application, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only runnable demo path creation readiness prerequisites are reviewed', 'safe local-only runnable demo path creation readiness gaps are recorded', 'safe local-only runnable demo path creation candidate is recommended', 'safe local-only runnable demo path creation readiness review is not execution authorization', 'safe local-only runnable demo path creation readiness review is not runnable demo creation', 'safe local-only runnable demo path creation readiness review is not runtime-applied enforcement', 'safe local-only runnable demo path creation readiness review is not runtime demo readiness', 'safe local-only runnable demo path creation readiness review is not scanner readiness', 'safe local-only runnable demo path creation readiness review is not production readiness', 'safe local-only runnable demo path creation readiness review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate', 'safe_local_only_runnable_demo_path_creation_candidate_recommended = true', 'safe_local_only_runnable_demo_path_creation_candidate_created = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.313 Safe Local-Only Runnable Demo Path Creation Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06312_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06312_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0387",
        "Status: completed readiness review",
        "Record that the project is ready to prepare a Safe Local-Only Runnable Demo Path Creation Candidate",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06312_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0387 - Add v0.6.312 Safe Local-Only Runnable Demo Path Creation Readiness Review",
        "Status: completed by v0.6.312",
        "safe_local_only_runnable_demo_path_creation_readiness_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate",
        "Proceed to v0.6.313 Safe Local-Only Runnable Demo Path Creation Candidate",
    ])

def test_v06312_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.312 Safe Local-Only Runnable Demo Path Creation Readiness Review",
        "safe_local_only_runnable_demo_path_creation_readiness_review_completed = true",
        "safe_local_only_runnable_demo_path_creation_readiness_review_id = safe_local_only_runnable_demo_path_creation_readiness_review_v06312",
        "safe_local_only_runnable_demo_path_creation_readiness_review_result = ready_for_creation_candidate_not_created",
        "readiness_prerequisite_boundary_accepted = true",
        "readiness_prerequisite_path_accepted = true",
        "readiness_prerequisite_mock_gateway_demo_available = true",
        "readiness_prerequisite_local_target_lab_profile_available = true",
        "readiness_prerequisite_runtime_destination_binding_available = true",
        "readiness_prerequisite_execution_authorization_gate_available = true",
        "readiness_prerequisite_preflight_validation_available = true",
        "safe_local_only_runnable_demo_path_creation_candidate_created = false",
        "safe_local_only_runnable_demo_path_created = false",
        "safe_local_only_runnable_demo_ready = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.312 - Safe Local-Only Runnable Demo Path Creation Readiness Review",
        "Reviewed readiness to prepare a Safe Local-Only Runnable Demo Path Creation Candidate.",
        "safe_local_only_runnable_demo_path_creation_readiness_review_completed = true",
        "safe_local_only_runnable_demo_path_creation_readiness_review_id = safe_local_only_runnable_demo_path_creation_readiness_review_v06312",
        "safe_local_only_runnable_demo_path_creation_readiness_review_result = ready_for_creation_candidate_not_created",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_creation_candidate",
        "safe_local_only_runnable_demo_path_creation_candidate_created = false",
        "safe_local_only_runnable_demo_path_created = false",
        "safe_local_only_runnable_demo_ready = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.312",
        "v0.6.313 Safe Local-Only Runnable Demo Path Creation Candidate",
        "no safe local-only runnable demo path creation candidate created",
        "no safe local-only runnable demo path created",
        "no safe local-only runnable demo ready",
        "no safe local-only demo execution boundary runtime-applied",
        "no publication approval",
        "no public announcement",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06312_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06312_safe_local_only_runnable_demo_path_creation_readiness_review.py"])

def main() -> None:
    test_v06312_doc_tokens()
    test_v06312_adr_tokens()
    test_v06312_issue_tokens()
    test_v06312_index_tokens()
    test_v06312_registered_in_run_all()
    print("v0.6.312 safe local-only runnable demo path creation readiness review checks passed")

if __name__ == "__main__":
    main()
