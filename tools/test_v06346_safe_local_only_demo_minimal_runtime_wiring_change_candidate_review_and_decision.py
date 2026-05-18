from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/421-v06346-safe-local-only-demo-minimal-runtime-wiring-change-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0421-add-v06346-safe-local-only-demo-minimal-runtime-wiring-change-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0421-add-v06346-safe-local-only-demo-minimal-runtime-wiring-change-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.346 Safe Local-Only Demo Minimal Runtime Wiring Change Candidate Review and Decision', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_accepted = true', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_id = safe_local_only_demo_minimal_runtime_wiring_change_candidate_v06345', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_result = accepted_as_bounded_candidate_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_status = accepted_not_runtime_wiring_changed', 'reviewed_safe_local_only_demo_minimal_runtime_wiring_change_candidate_created = true', 'reviewed_safe_local_only_demo_minimal_runtime_wiring_change_candidate_scope = bounded_candidate_only_no_runtime_wiring_change', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_review_id = safe_local_only_demo_minimal_runtime_wiring_go_no_go_review_v06344', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_review_result = conditional_go_for_bounded_runtime_wiring_change_candidate_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_decision = conditional_go', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_allowed_next = true', 'safe_local_only_demo_minimal_runtime_wiring_closeout_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_track_status = closed', 'safe_local_only_demo_minimal_runtime_wiring_track_outcome = bounded_candidate_accepted_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_candidate_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_candidate_accepted = true', 'safe_local_only_demo_minimal_runtime_wiring_candidate_id = safe_local_only_demo_minimal_runtime_wiring_candidate_v06340', 'safe_local_only_demo_minimal_runtime_wiring_candidate_status = accepted_not_runtime_wiring_changed', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'minimal_runtime_wiring_change_candidate_existing_safe_local_runner_outputs_accepted = true', 'minimal_runtime_wiring_change_candidate_allowed_blocked_human_approval_visibility_accepted = true', 'minimal_runtime_wiring_change_candidate_localhost_only_binding_accepted = true', 'minimal_runtime_wiring_change_candidate_loopback_only_target_accepted = true', 'minimal_runtime_wiring_change_candidate_mock_first_default_accepted = true', 'minimal_runtime_wiring_change_candidate_private_artifact_boundary_accepted = true', 'minimal_runtime_wiring_change_candidate_no_external_target_authorization_accepted = true', 'minimal_runtime_wiring_change_candidate_no_real_scanner_execution_accepted = true', 'minimal_runtime_wiring_change_candidate_no_gateway_behavior_change_accepted = true', 'minimal_runtime_wiring_change_candidate_no_runtime_behavior_change_accepted = true', 'minimal_runtime_wiring_change_candidate_no_scanner_behavior_change_accepted = true', 'minimal_runtime_wiring_change_candidate_reversal_or_rollback_boundary_accepted = true', 'minimal_runtime_wiring_change_candidate_test_command_clarity_accepted = true', 'minimal_runtime_wiring_change_candidate_preflight_and_authorization_false_states_accepted = true', 'minimal_runtime_wiring_change_candidate_reviewer_visible_outcomes_accepted = true', 'minimal_runtime_wiring_change_candidate_fail_closed_paths_accepted = true', 'minimal_runtime_wiring_change_candidate_claim_boundary_preservation_accepted = true', 'minimal_runtime_wiring_change_candidate_proposed_artifact = safe_local_only_minimal_runtime_wiring_change_candidate_record', 'minimal_runtime_wiring_change_candidate_proposed_artifact_public = false', 'minimal_runtime_wiring_change_candidate_proposed_wiring_change = false', 'minimal_runtime_wiring_change_candidate_proposed_runtime_change = false', 'minimal_runtime_wiring_change_candidate_proposed_gateway_change = false', 'minimal_runtime_wiring_change_candidate_proposed_scanner_change = false', 'minimal_runtime_wiring_change_candidate_proposed_schema_change = false', 'minimal_runtime_wiring_change_candidate_forbids_direct_runtime_wiring_change = true', 'minimal_runtime_wiring_change_candidate_forbids_runtime_application = true', 'minimal_runtime_wiring_change_candidate_forbids_execution_authorization = true', 'minimal_runtime_wiring_change_candidate_forbids_real_execution = true', 'minimal_runtime_wiring_change_candidate_forbids_external_target_authorization = true', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'minimal_runtime_wiring_changed = false', 'recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_change_closeout_review', 'safe_local_only_demo_minimal_runtime_wiring_change_closeout_review_recommended = true', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_and_decision_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'minimal runtime wiring change candidate review is not runtime wiring', 'minimal runtime wiring change candidate review is not runtime application', 'minimal runtime wiring change candidate review is not execution authorization', 'minimal runtime wiring change candidate review is not real execution permission', 'minimal runtime wiring change candidate review is not external target authorization', 'minimal runtime wiring change candidate review is not public demo readiness', 'minimal runtime wiring change candidate review is not scanner readiness', 'minimal runtime wiring change candidate review is not production readiness', 'No private generated outputs are moved public in v0.6.346.', 'v0.6.347 Safe Local-Only Demo Minimal Runtime Wiring Change Closeout Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06346_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0421",
        "Status: accepted",
        "Accept the runtime wiring change candidate as a bounded planning candidate that remains not runtime-wiring-changed.",
    ])
    assert_tokens(ISSUE, [
        "0421 - Add v0.6.346 Safe Local-Only Demo Minimal Runtime Wiring Change Candidate Review and Decision",
        "Status: completed by v0.6.346",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_change_closeout_review",
        "Proceed to v0.6.347 Safe Local-Only Demo Minimal Runtime Wiring Change Closeout Review",
    ])

def test_v06346_index_files() -> None:
    assert_tokens(README, [
        "v0.6.346 Safe Local-Only Demo Minimal Runtime Wiring Change Candidate Review and Decision",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_accepted = true",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_id = safe_local_only_demo_minimal_runtime_wiring_change_candidate_v06345",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_status = accepted_not_runtime_wiring_changed",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_change_closeout_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.346 - Safe Local-Only Demo Minimal Runtime Wiring Change Candidate Review and Decision",
        "Reviewed and accepted the bounded safe local-only demo minimal runtime wiring change candidate.",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_change_candidate_accepted = true",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_change_closeout_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.346",
        "v0.6.347 Safe Local-Only Demo Minimal Runtime Wiring Change Closeout Review",
        "no safe local-only demo minimal runtime wiring change closeout review completed",
        "no safe local-only demo execution boundary runtime-applied",
        "no minimal runtime wiring change",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06346_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06346_safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_and_decision.py"])

def test_v06346_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06346_primary_files()
    test_v06346_index_files()
    test_v06346_registered_in_run_all()
    test_v06346_avoids_raw_forbidden_claim_phrases()
    print("v0.6.346 safe local-only demo minimal runtime wiring change candidate review and decision checks passed")

if __name__ == "__main__":
    main()
