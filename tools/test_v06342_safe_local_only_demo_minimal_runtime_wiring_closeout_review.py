from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/417-v06342-safe-local-only-demo-minimal-runtime-wiring-closeout-review.md"
ADR = ROOT / "planning/decisions/ADR-0417-add-v06342-safe-local-only-demo-minimal-runtime-wiring-closeout-review.md"
ISSUE = ROOT / "planning/issues/0417-add-v06342-safe-local-only-demo-minimal-runtime-wiring-closeout-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.342 Safe Local-Only Demo Minimal Runtime Wiring Closeout Review', 'safe_local_only_demo_minimal_runtime_wiring_closeout_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_closeout_review_id = safe_local_only_demo_minimal_runtime_wiring_closeout_review_v06342', 'safe_local_only_demo_minimal_runtime_wiring_closeout_review_result = track_closed_runtime_wiring_changed_false', 'safe_local_only_demo_minimal_runtime_wiring_track_status = closed', 'safe_local_only_demo_minimal_runtime_wiring_track_outcome = bounded_candidate_accepted_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_candidate_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_candidate_accepted = true', 'safe_local_only_demo_minimal_runtime_wiring_candidate_id = safe_local_only_demo_minimal_runtime_wiring_candidate_v06340', 'safe_local_only_demo_minimal_runtime_wiring_candidate_review_result = accepted_as_bounded_candidate_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_candidate_status = accepted_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_id = safe_local_only_demo_minimal_runtime_wiring_readiness_review_v06339', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_result = candidate_needed_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_candidate_needed = true', 'safe_local_only_demo_runtime_application_implementation_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_implementation_closeout_review_id = safe_local_only_demo_runtime_application_implementation_closeout_review_v06337', 'safe_local_only_demo_runtime_application_implementation_track_status = closed', 'safe_local_only_demo_runtime_application_implementation_track_outcome = bounded_implementation_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'minimal_runtime_wiring_closeout_existing_safe_local_runner_outputs_preserved = true', 'minimal_runtime_wiring_closeout_allowed_blocked_human_approval_visibility_preserved = true', 'minimal_runtime_wiring_closeout_localhost_only_binding_preserved = true', 'minimal_runtime_wiring_closeout_loopback_only_target_preserved = true', 'minimal_runtime_wiring_closeout_mock_first_default_preserved = true', 'minimal_runtime_wiring_closeout_private_artifact_boundary_preserved = true', 'minimal_runtime_wiring_closeout_no_external_target_authorization_preserved = true', 'minimal_runtime_wiring_closeout_no_real_scanner_execution_preserved = true', 'minimal_runtime_wiring_closeout_no_gateway_behavior_change_preserved = true', 'minimal_runtime_wiring_closeout_no_runtime_behavior_change_preserved = true', 'minimal_runtime_wiring_closeout_no_scanner_behavior_change_preserved = true', 'minimal_runtime_wiring_closeout_no_schema_behavior_change_preserved = true', 'minimal_runtime_wiring_closeout_reversal_or_rollback_boundary_preserved = true', 'minimal_runtime_wiring_closeout_preflight_and_authorization_false_states_preserved = true', 'minimal_runtime_wiring_closeout_reviewer_visible_outcomes_preserved = true', 'minimal_runtime_wiring_closeout_fail_closed_paths_preserved = true', 'minimal_runtime_wiring_closeout_claim_boundary_preservation_confirmed = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'minimal_runtime_wiring_changed = false', 'recommended_next_work_item = next_work_selection_using_risk_tiered_granularity', 'next_work_selection_using_risk_tiered_granularity_recommended = true', 'safe_local_only_demo_minimal_runtime_wiring_closeout_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'minimal runtime wiring closeout review is not runtime wiring', 'minimal runtime wiring closeout review is not runtime application', 'minimal runtime wiring closeout review is not execution authorization', 'minimal runtime wiring closeout review is not real execution permission', 'minimal runtime wiring closeout review is not external target authorization', 'minimal runtime wiring closeout review is not public demo readiness', 'minimal runtime wiring closeout review is not scanner readiness', 'minimal runtime wiring closeout review is not production readiness', 'No private generated outputs are moved public in v0.6.342.', 'v0.6.343 Next Work Selection Using Risk-Tiered Granularity']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06342_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0417",
        "Status: completed closeout",
        "Close the safe local-only demo minimal runtime wiring candidate track while preserving runtime-wiring-changed false.",
    ])
    assert_tokens(ISSUE, [
        "0417 - Add v0.6.342 Safe Local-Only Demo Minimal Runtime Wiring Closeout Review",
        "Status: completed by v0.6.342",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
        "Proceed to v0.6.343 Next Work Selection Using Risk-Tiered Granularity",
    ])

def test_v06342_index_files() -> None:
    assert_tokens(README, [
        "v0.6.342 Safe Local-Only Demo Minimal Runtime Wiring Closeout Review",
        "safe_local_only_demo_minimal_runtime_wiring_closeout_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_closeout_review_result = track_closed_runtime_wiring_changed_false",
        "safe_local_only_demo_minimal_runtime_wiring_track_status = closed",
        "safe_local_only_demo_minimal_runtime_wiring_track_outcome = bounded_candidate_accepted_not_runtime_wiring_changed",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.342 - Safe Local-Only Demo Minimal Runtime Wiring Closeout Review",
        "Closed the safe local-only demo minimal runtime wiring candidate track.",
        "safe_local_only_demo_minimal_runtime_wiring_closeout_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_track_status = closed",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.342",
        "v0.6.343 Next Work Selection Using Risk-Tiered Granularity",
        "no safe local-only demo execution boundary runtime-applied",
        "no minimal runtime wiring change",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06342_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06342_safe_local_only_demo_minimal_runtime_wiring_closeout_review.py"])

def test_v06342_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06342_primary_files()
    test_v06342_index_files()
    test_v06342_registered_in_run_all()
    test_v06342_avoids_raw_forbidden_claim_phrases()
    print("v0.6.342 safe local-only demo minimal runtime wiring closeout review checks passed")

if __name__ == "__main__":
    main()
