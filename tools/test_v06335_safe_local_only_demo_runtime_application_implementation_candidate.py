from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/410-v06335-safe-local-only-demo-runtime-application-implementation-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0410-add-v06335-safe-local-only-demo-runtime-application-implementation-candidate.md"
ISSUE = ROOT / "planning/issues/0410-add-v06335-safe-local-only-demo-runtime-application-implementation-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate', 'safe_local_only_demo_runtime_application_implementation_candidate_created = true', 'safe_local_only_demo_runtime_application_implementation_candidate_id = safe_local_only_demo_runtime_application_implementation_candidate_v06335', 'safe_local_only_demo_runtime_application_implementation_candidate_status = candidate_not_reviewed', 'safe_local_only_demo_runtime_application_implementation_candidate_scope = candidate_only_no_runtime_behavior_change', 'safe_local_only_demo_runtime_application_implementation_candidate_review_completed = false', 'safe_local_only_demo_runtime_application_implementation_candidate_accepted = false', 'safe_local_only_demo_runtime_application_go_no_go_review_completed = true', 'safe_local_only_demo_runtime_application_go_no_go_review_id = safe_local_only_demo_runtime_application_go_no_go_review_v06334', 'safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go', 'safe_local_only_demo_runtime_application_go_no_go_review_result = conditional_go_for_bounded_implementation_candidate_not_runtime_applied', 'safe_local_only_demo_runtime_application_implementation_candidate_allowed_next = true', 'safe_local_only_demo_runtime_application_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_closeout_review_id = safe_local_only_demo_runtime_application_closeout_review_v06332', 'safe_local_only_demo_runtime_application_track_status = closed', 'safe_local_only_demo_runtime_application_track_outcome = bounded_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_candidate_review_completed = true', 'safe_local_only_demo_runtime_application_candidate_accepted = true', 'safe_local_only_demo_runtime_application_candidate_id = safe_local_only_demo_runtime_application_candidate_v06330', 'safe_local_only_demo_runtime_application_candidate_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'implementation_candidate_localhost_only_binding_required = true', 'implementation_candidate_loopback_only_target_required = true', 'implementation_candidate_mock_first_default_required = true', 'implementation_candidate_private_artifact_boundary_required = true', 'implementation_candidate_no_external_target_authorization_required = true', 'implementation_candidate_no_real_scanner_execution_required = true', 'implementation_candidate_no_gateway_behavior_change_required = true', 'implementation_candidate_no_runtime_behavior_change_required = true', 'implementation_candidate_no_scanner_behavior_change_required = true', 'implementation_candidate_reversal_or_rollback_boundary_required = true', 'implementation_candidate_test_command_clarity_required = true', 'implementation_candidate_preflight_and_authorization_false_states_required = true', 'implementation_candidate_reviewer_visible_outcomes_required = true', 'implementation_candidate_fail_closed_paths_required = true', 'implementation_candidate_claim_boundary_preservation_required = true', 'implementation_candidate_proposed_artifact = safe_local_only_runtime_application_implementation_candidate_record', 'implementation_candidate_proposed_artifact_public = false', 'implementation_candidate_proposed_runtime_change = false', 'implementation_candidate_proposed_gateway_change = false', 'implementation_candidate_proposed_scanner_change = false', 'implementation_candidate_proposed_schema_change = false', 'implementation_candidate_allows_later_review_only = true', 'implementation_candidate_forbids_direct_runtime_application = true', 'implementation_candidate_forbids_execution_authorization = true', 'implementation_candidate_forbids_real_execution = true', 'implementation_candidate_forbids_external_target_authorization = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate_review_and_decision', 'safe_local_only_demo_runtime_application_implementation_candidate_review_and_decision_recommended = true', 'safe_local_only_demo_runtime_application_implementation_candidate_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'implementation candidate is not runtime application', 'implementation candidate is not execution authorization', 'implementation candidate is not real execution permission', 'implementation candidate is not external target authorization', 'implementation candidate is not public demo readiness', 'implementation candidate is not scanner readiness', 'implementation candidate is not production readiness', 'No private generated outputs are moved public in v0.6.335.', 'v0.6.336 Safe Local-Only Demo Runtime Application Implementation Candidate Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06335_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0410",
        "Status: proposed candidate",
        "Create the implementation candidate as a bounded candidate only.",
    ])
    assert_tokens(ISSUE, [
        "0410 - Add v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate",
        "Status: completed by v0.6.335",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate_review_and_decision",
        "Proceed to v0.6.336 Safe Local-Only Demo Runtime Application Implementation Candidate Review and Decision",
    ])

def test_v06335_index_files() -> None:
    assert_tokens(README, [
        "v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate",
        "safe_local_only_demo_runtime_application_implementation_candidate_created = true",
        "safe_local_only_demo_runtime_application_implementation_candidate_id = safe_local_only_demo_runtime_application_implementation_candidate_v06335",
        "safe_local_only_demo_runtime_application_implementation_candidate_status = candidate_not_reviewed",
        "safe_local_only_demo_runtime_application_implementation_candidate_review_completed = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate_review_and_decision",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.335 - Safe Local-Only Demo Runtime Application Implementation Candidate",
        "Created a bounded safe local-only demo runtime application implementation candidate.",
        "safe_local_only_demo_runtime_application_implementation_candidate_created = true",
        "safe_local_only_demo_runtime_application_implementation_candidate_id = safe_local_only_demo_runtime_application_implementation_candidate_v06335",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate_review_and_decision",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.335",
        "v0.6.336 Safe Local-Only Demo Runtime Application Implementation Candidate Review and Decision",
        "no safe local-only demo runtime application implementation candidate review completed",
        "no safe local-only demo execution boundary runtime-applied",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06335_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06335_safe_local_only_demo_runtime_application_implementation_candidate.py"])

def test_v06335_avoids_raw_forbidden_claim_phrases() -> None:
    scanned_paths = [DOC, ADR, ISSUE, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
        "AI pentest agent",
        "production-ready scanner",
        "runtime-enforced scanner",
        "external-target-ready demo",
        "customer-ready PoC",
        "certified / audit-ready system",
        "compliance-sufficient control",
        "diagnostically complete",
        "diagnostically-complete",
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06335_primary_files()
    test_v06335_index_files()
    test_v06335_registered_in_run_all()
    test_v06335_avoids_raw_forbidden_claim_phrases()
    print("v0.6.335 safe local-only demo runtime application implementation candidate checks passed")

if __name__ == "__main__":
    main()
