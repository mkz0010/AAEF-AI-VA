from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/414-v06339-safe-local-only-demo-minimal-runtime-wiring-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0414-add-v06339-safe-local-only-demo-minimal-runtime-wiring-readiness-review.md"
ISSUE = ROOT / "planning/issues/0414-add-v06339-safe-local-only-demo-minimal-runtime-wiring-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_id = safe_local_only_demo_minimal_runtime_wiring_readiness_review_v06339', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_result = candidate_needed_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_scope = review_only_no_runtime_wiring_change', 'safe_local_only_demo_minimal_runtime_wiring_candidate_needed = true', 'safe_local_only_demo_minimal_runtime_wiring_candidate_created = false', 'safe_local_only_demo_minimal_runtime_wiring_candidate_review_completed = false', 'safe_local_only_demo_runtime_application_implementation_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_implementation_closeout_review_id = safe_local_only_demo_runtime_application_implementation_closeout_review_v06337', 'safe_local_only_demo_runtime_application_implementation_closeout_review_result = track_closed_runtime_applied_false', 'safe_local_only_demo_runtime_application_implementation_track_status = closed', 'safe_local_only_demo_runtime_application_implementation_track_outcome = bounded_implementation_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_implementation_candidate_review_completed = true', 'safe_local_only_demo_runtime_application_implementation_candidate_accepted = true', 'safe_local_only_demo_runtime_application_implementation_candidate_id = safe_local_only_demo_runtime_application_implementation_candidate_v06335', 'safe_local_only_demo_runtime_application_implementation_candidate_status = accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_go_no_go_review_completed = true', 'safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go', 'safe_local_only_demo_runtime_application_go_no_go_review_result = conditional_go_for_bounded_implementation_candidate_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'minimal_runtime_wiring_existing_safe_local_runner_outputs_checked = true', 'minimal_runtime_wiring_allowed_blocked_human_approval_visibility_checked = true', 'minimal_runtime_wiring_localhost_only_binding_checked = true', 'minimal_runtime_wiring_loopback_only_target_checked = true', 'minimal_runtime_wiring_mock_first_default_checked = true', 'minimal_runtime_wiring_private_artifact_boundary_checked = true', 'minimal_runtime_wiring_no_external_target_authorization_checked = true', 'minimal_runtime_wiring_no_real_scanner_execution_checked = true', 'minimal_runtime_wiring_no_gateway_behavior_change_checked = true', 'minimal_runtime_wiring_no_runtime_behavior_change_checked = true', 'minimal_runtime_wiring_reversal_or_rollback_boundary_checked = true', 'minimal_runtime_wiring_test_command_clarity_checked = true', 'minimal_runtime_wiring_claim_boundary_preservation_checked = true', 'minimal_runtime_wiring_candidate_boundary_defined = true', 'minimal_runtime_wiring_readiness_allows_later_candidate = true', 'minimal_runtime_wiring_readiness_does_not_change_runtime_wiring = true', 'minimal_runtime_wiring_readiness_does_not_apply_runtime_behavior = true', 'minimal_runtime_wiring_readiness_does_not_authorize_execution = true', 'minimal_runtime_wiring_readiness_does_not_permit_real_execution = true', 'minimal_runtime_wiring_readiness_does_not_authorize_external_targets = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'minimal_runtime_wiring_changed = false', 'recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_candidate', 'safe_local_only_demo_minimal_runtime_wiring_candidate_recommended = true', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'minimal runtime wiring readiness review is not runtime wiring', 'minimal runtime wiring readiness review is not runtime application', 'minimal runtime wiring readiness review is not execution authorization', 'minimal runtime wiring readiness review is not real execution permission', 'minimal runtime wiring readiness review is not external target authorization', 'minimal runtime wiring readiness review is not public demo readiness', 'minimal runtime wiring readiness review is not scanner readiness', 'minimal runtime wiring readiness review is not production readiness', 'No private generated outputs are moved public in v0.6.339.', 'v0.6.340 Safe Local-Only Demo Minimal Runtime Wiring Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06339_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0414",
        "Status: accepted",
        "Record that a bounded minimal runtime wiring candidate is needed, but do not change runtime wiring or runtime behavior in this checkpoint.",
    ])
    assert_tokens(ISSUE, [
        "0414 - Add v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review",
        "Status: completed by v0.6.339",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_candidate",
        "Proceed to v0.6.340 Safe Local-Only Demo Minimal Runtime Wiring Candidate",
    ])

def test_v06339_index_files() -> None:
    assert_tokens(README, [
        "v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review",
        "safe_local_only_demo_minimal_runtime_wiring_readiness_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_readiness_review_result = candidate_needed_not_runtime_wiring_changed",
        "safe_local_only_demo_minimal_runtime_wiring_candidate_needed = true",
        "safe_local_only_demo_minimal_runtime_wiring_candidate_created = false",
        "minimal_runtime_wiring_existing_safe_local_runner_outputs_checked = true",
        "minimal_runtime_wiring_allowed_blocked_human_approval_visibility_checked = true",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.339 - Safe Local-Only Demo Minimal Runtime Wiring Readiness Review",
        "Reviewed readiness for a later safe local-only demo minimal runtime wiring candidate.",
        "safe_local_only_demo_minimal_runtime_wiring_readiness_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_readiness_review_result = candidate_needed_not_runtime_wiring_changed",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.339",
        "v0.6.340 Safe Local-Only Demo Minimal Runtime Wiring Candidate",
        "no safe local-only demo minimal runtime wiring candidate created",
        "no safe local-only demo execution boundary runtime-applied",
        "no minimal runtime wiring change",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06339_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06339_safe_local_only_demo_minimal_runtime_wiring_readiness_review.py"])

def test_v06339_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06339_primary_files()
    test_v06339_index_files()
    test_v06339_registered_in_run_all()
    test_v06339_avoids_raw_forbidden_claim_phrases()
    print("v0.6.339 safe local-only demo minimal runtime wiring readiness review checks passed")

if __name__ == "__main__":
    main()
