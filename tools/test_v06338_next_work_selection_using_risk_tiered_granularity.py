from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/413-v06338-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0413-add-v06338-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0413-add-v06338-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.338 Next Work Selection Using Risk-Tiered Granularity', 'next_work_selection_using_risk_tiered_granularity_completed = true', 'next_work_selection_using_risk_tiered_granularity_id = next_work_selection_using_risk_tiered_granularity_v06338', 'next_work_selection_result = safe_local_only_demo_minimal_runtime_wiring_readiness_review', 'selected_next_work_item = safe_local_only_demo_minimal_runtime_wiring_readiness_review', 'selected_next_work_version = v0.6.339', 'selected_next_work_title = Safe Local-Only Demo Minimal Runtime Wiring Readiness Review', 'selected_next_work_scope = review_only_no_runtime_wiring_change', 'selected_next_work_reason = implementation_candidate_track_closed_runtime_applied_false_requires_minimal_wiring_readiness_review_before_runtime_application', 'selected_next_work_risk_tier = high_value_high_boundary_risk_review_only', 'selected_next_work_granularity = single_minimal_runtime_wiring_readiness_review_checkpoint', 'safe_local_only_demo_runtime_application_implementation_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_implementation_closeout_review_id = safe_local_only_demo_runtime_application_implementation_closeout_review_v06337', 'safe_local_only_demo_runtime_application_implementation_closeout_review_result = track_closed_runtime_applied_false', 'safe_local_only_demo_runtime_application_implementation_track_status = closed', 'safe_local_only_demo_runtime_application_implementation_track_outcome = bounded_implementation_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_implementation_candidate_review_completed = true', 'safe_local_only_demo_runtime_application_implementation_candidate_accepted = true', 'safe_local_only_demo_runtime_application_implementation_candidate_id = safe_local_only_demo_runtime_application_implementation_candidate_v06335', 'safe_local_only_demo_runtime_application_implementation_candidate_status = accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_go_no_go_review_completed = true', 'safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go', 'safe_local_only_demo_runtime_application_go_no_go_review_result = conditional_go_for_bounded_implementation_candidate_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'minimal_runtime_wiring_readiness_review_selected = true', 'minimal_runtime_wiring_readiness_review_created = false', 'minimal_runtime_wiring_readiness_review_completed = false', 'minimal_runtime_wiring_readiness_review_should_check_existing_safe_local_runner_outputs = true', 'minimal_runtime_wiring_readiness_review_should_check_allowed_blocked_human_approval_visibility = true', 'minimal_runtime_wiring_readiness_review_should_check_localhost_only_binding = true', 'minimal_runtime_wiring_readiness_review_should_check_loopback_only_target = true', 'minimal_runtime_wiring_readiness_review_should_check_mock_first_default = true', 'minimal_runtime_wiring_readiness_review_should_check_private_artifact_boundary = true', 'minimal_runtime_wiring_readiness_review_should_check_no_external_target_authorization = true', 'minimal_runtime_wiring_readiness_review_should_check_no_real_scanner_execution = true', 'minimal_runtime_wiring_readiness_review_should_check_no_gateway_behavior_change = true', 'minimal_runtime_wiring_readiness_review_should_check_no_runtime_behavior_change = true', 'minimal_runtime_wiring_readiness_review_should_check_reversal_or_rollback_boundary = true', 'minimal_runtime_wiring_readiness_review_should_check_test_command_clarity = true', 'minimal_runtime_wiring_readiness_review_should_check_claim_boundary_preservation = true', 'deprioritized_direct_runtime_application_work = true', 'deprioritized_public_launch_work = true', 'deprioritized_customer_demo_work = true', 'deprioritized_repository_metadata_work = true', 'deprioritized_real_scanner_execution_work = true', 'deprioritized_external_target_work = true', 'deprioritized_commercial_material_work = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'minimal_runtime_wiring_changed = false', 'recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_readiness_review', 'safe_local_only_demo_minimal_runtime_wiring_readiness_review_recommended = true', 'next_work_selection_using_risk_tiered_granularity_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'next work selection is not runtime application', 'next work selection is not runtime wiring', 'next work selection is not execution authorization', 'next work selection is not real execution permission', 'next work selection is not external target authorization', 'next work selection is not public demo readiness', 'next work selection is not scanner readiness', 'next work selection is not production readiness', 'No private generated outputs are moved public in v0.6.338.', 'v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06338_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0413",
        "Status: accepted",
        "Select `safe_local_only_demo_minimal_runtime_wiring_readiness_review` as the next work item using risk-tiered granularity.",
    ])
    assert_tokens(ISSUE, [
        "0413 - Add v0.6.338 Next Work Selection Using Risk-Tiered Granularity",
        "Status: completed by v0.6.338",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_readiness_review",
        "Proceed to v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review",
    ])

def test_v06338_index_files() -> None:
    assert_tokens(README, [
        "v0.6.338 Next Work Selection Using Risk-Tiered Granularity",
        "next_work_selection_result = safe_local_only_demo_minimal_runtime_wiring_readiness_review",
        "selected_next_work_version = v0.6.339",
        "minimal_runtime_wiring_readiness_review_selected = true",
        "minimal_runtime_wiring_readiness_review_completed = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_readiness_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.338 - Next Work Selection Using Risk-Tiered Granularity",
        "Selected `safe_local_only_demo_minimal_runtime_wiring_readiness_review` as the next work item",
        "selected_next_work_version = v0.6.339",
        "recommended_next_work_item = safe_local_only_demo_minimal_runtime_wiring_readiness_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.338",
        "v0.6.339 Safe Local-Only Demo Minimal Runtime Wiring Readiness Review",
        "no safe local-only demo minimal runtime wiring readiness review completed",
        "no safe local-only demo execution boundary runtime-applied",
        "no minimal runtime wiring change",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06338_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06338_next_work_selection_using_risk_tiered_granularity.py"])

def test_v06338_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06338_primary_files()
    test_v06338_index_files()
    test_v06338_registered_in_run_all()
    test_v06338_avoids_raw_forbidden_claim_phrases()
    print("v0.6.338 next work selection using risk-tiered granularity checks passed")

if __name__ == "__main__":
    main()
