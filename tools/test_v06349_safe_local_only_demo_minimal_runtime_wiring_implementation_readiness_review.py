from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/424-v06349-safe-local-only-demo-minimal-runtime-wiring-implementation-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0424-add-v06349-safe-local-only-demo-minimal-runtime-wiring-implementation-readiness-review.md"
ISSUE = ROOT / "planning/issues/0424-add-v06349-safe-local-only-demo-minimal-runtime-wiring-implementation-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.349 Safe Local-Only Demo Minimal Runtime Wiring Implementation Readiness Review', 'safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_id = safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_v06349', 'safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_result = implementation_candidate_needed_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_scope = review_only_no_runtime_wiring_change', 'safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_needed = true', 'safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_created = false', 'safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_review_completed = false', 'safe_local_only_demo_minimal_runtime_wiring_change_closeout_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_change_closeout_review_id = safe_local_only_demo_minimal_runtime_wiring_change_closeout_review_v06347', 'safe_local_only_demo_minimal_runtime_wiring_change_closeout_review_result = track_closed_runtime_wiring_changed_false', 'safe_local_only_demo_minimal_runtime_wiring_change_track_status = closed', 'safe_local_only_demo_minimal_runtime_wiring_change_track_outcome = bounded_change_candidate_accepted_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_accepted = true', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_id = safe_local_only_demo_minimal_runtime_wiring_change_candidate_v06345', 'safe_local_only_demo_minimal_runtime_wiring_change_candidate_status = accepted_not_runtime_wiring_changed', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_review_completed = true', 'safe_local_only_demo_minimal_runtime_wiring_go_no_go_decision = conditional_go', 'safe_local_only_demo_minimal_runtime_wiring_track_status = closed', 'safe_local_only_demo_minimal_runtime_wiring_track_outcome = bounded_candidate_accepted_not_runtime_wiring_changed', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'minimal_runtime_wiring_implementation_readiness_accepted_change_candidate_scope_checked = true', 'minimal_runtime_wiring_implementation_readiness_existing_safe_local_runner_outputs_checked = true', 'minimal_runtime_wiring_implementation_readiness_allowed_blocked_human_approval_visibility_checked = true', 'minimal_runtime_wiring_implementation_readiness_localhost_only_binding_checked = true', 'minimal_runtime_wiring_implementation_readiness_loopback_only_target_checked = true', 'minimal_runtime_wiring_implementation_readiness_mock_first_default_checked = true', 'minimal_runtime_wiring_implementation_readiness_private_artifact_boundary_checked = true', 'minimal_runtime_wiring_implementation_readiness_no_external_target_authorization_checked = true', 'minimal_runtime_wiring_implementation_readiness_no_real_scanner_execution_checked = true', 'minimal_runtime_wiring_implementation_readiness_no_gateway_behavior_change_checked = true', 'minimal_runtime_wiring_implementation_readiness_no_runtime_behavior_change_checked = true', 'minimal_runtime_wiring_implementation_readiness_no_scanner_behavior_change_checked = true', 'minimal_runtime_wiring_implementation_readiness_reversal_or_rollback_boundary_checked = true', 'minimal_runtime_wiring_implementation_readiness_test_command_clarity_checked = true', 'minimal_runtime_wiring_implementation_readiness_claim_boundary_preservation_checked = true', 'minimal_runtime_wiring_implementation_readiness_result_requires_candidate_only_next_step = true', 'minimal_runtime_wiring_implementation_readiness_forbids_direct_runtime_wiring_change = true', 'minimal_runtime_wiring_implementation_readiness_forbids_runtime_application = true', 'minimal_runtime_wiring_implementation_readiness_forbids_execution_authorization = true', 'minimal_runtime_wiring_implementation_readiness_forbids_real_execution = true', 'minimal_runtime_wiring_implementation_readiness_forbids_external_target_authorization = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_existing_safe_local_runner_outputs = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_allowed_blocked_human_approval_visibility = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_localhost_only_binding = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_loopback_only_target = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_mock_first_default = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_private_artifact_boundary = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_fail_closed_paths = true', 'minimal_runtime_wiring_implementation_candidate_should_preserve_rollback_boundary = true', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'minimal_runtime_wiring_changed = false', 'recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_implementation_candidate', 'safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_recommended = true', 'safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'minimal runtime wiring implementation readiness review is not runtime wiring', 'minimal runtime wiring implementation readiness review is not runtime application', 'minimal runtime wiring implementation readiness review is not execution authorization', 'minimal runtime wiring implementation readiness review is not real execution permission', 'minimal runtime wiring implementation readiness review is not external target authorization', 'minimal runtime wiring implementation readiness review is not public demo readiness', 'minimal runtime wiring implementation readiness review is not scanner readiness', 'minimal runtime wiring implementation readiness review is not production readiness', 'No private generated outputs are moved public in v0.6.349.', 'v0.6.350 Safe Local-Only Demo Minimal Runtime Wiring Implementation Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06349_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0424",
        "Status: accepted",
        "Record that a bounded minimal runtime wiring implementation candidate is needed, but do not change runtime wiring or runtime behavior in this checkpoint.",
    ])
    assert_tokens(ISSUE, [
        "0424 - Add v0.6.349 Safe Local-Only Demo Minimal Runtime Wiring Implementation Readiness Review",
        "Status: completed by v0.6.349",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_implementation_candidate",
        "Proceed to v0.6.350 Safe Local-Only Demo Minimal Runtime Wiring Implementation Candidate",
    ])

def test_v06349_index_files() -> None:
    assert_tokens(README, [
        "v0.6.349 Safe Local-Only Demo Minimal Runtime Wiring Implementation Readiness Review",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_result = implementation_candidate_needed_not_runtime_wiring_changed",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_needed = true",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_candidate_created = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_implementation_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.349 - Safe Local-Only Demo Minimal Runtime Wiring Implementation Readiness Review",
        "Reviewed readiness for a later safe local-only demo minimal runtime wiring implementation candidate.",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_completed = true",
        "safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review_result = implementation_candidate_needed_not_runtime_wiring_changed",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_implementation_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.349",
        "v0.6.350 Safe Local-Only Demo Minimal Runtime Wiring Implementation Candidate",
        "no safe local-only demo minimal runtime wiring implementation candidate created",
        "no safe local-only demo execution boundary runtime-applied",
        "no minimal runtime wiring change",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06349_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06349_safe_local_only_demo_minimal_runtime_wiring_implementation_readiness_review.py"])

def test_v06349_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06349_primary_files()
    test_v06349_index_files()
    test_v06349_registered_in_run_all()
    test_v06349_avoids_raw_forbidden_claim_phrases()
    print("v0.6.349 safe local-only demo minimal runtime wiring implementation readiness review checks passed")

if __name__ == "__main__":
    main()
