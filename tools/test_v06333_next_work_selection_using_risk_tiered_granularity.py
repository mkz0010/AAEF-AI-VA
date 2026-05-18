from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/408-v06333-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0408-add-v06333-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0408-add-v06333-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.333 Next Work Selection Using Risk-Tiered Granularity', 'next_work_selection_using_risk_tiered_granularity_completed = true', 'next_work_selection_using_risk_tiered_granularity_id = next_work_selection_using_risk_tiered_granularity_v06333', 'next_work_selection_result = safe_local_only_demo_runtime_application_go_no_go_review', 'selected_next_work_item = safe_local_only_demo_runtime_application_go_no_go_review', 'selected_next_work_version = v0.6.334', 'selected_next_work_title = Safe Local-Only Demo Runtime Application Go/No-Go Review', 'selected_next_work_scope = review_only_no_runtime_application', 'selected_next_work_reason = runtime_application_candidate_track_closed_runtime_applied_false_requires_explicit_go_no_go_before_application', 'selected_next_work_risk_tier = high_value_high_boundary_risk_review_only', 'selected_next_work_granularity = single_go_no_go_review_checkpoint', 'safe_local_only_demo_runtime_application_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_closeout_review_id = safe_local_only_demo_runtime_application_closeout_review_v06332', 'safe_local_only_demo_runtime_application_closeout_review_result = track_closed_runtime_applied_false', 'safe_local_only_demo_runtime_application_track_status = closed', 'safe_local_only_demo_runtime_application_track_outcome = bounded_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_candidate_review_completed = true', 'safe_local_only_demo_runtime_application_candidate_accepted = true', 'safe_local_only_demo_runtime_application_candidate_id = safe_local_only_demo_runtime_application_candidate_v06330', 'safe_local_only_demo_runtime_application_candidate_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_application_go_no_go_review_selected = true', 'runtime_application_go_no_go_review_created = false', 'runtime_application_go_no_go_review_completed = false', 'runtime_application_go_no_go_review_should_check_accepted_candidate_scope = true', 'runtime_application_go_no_go_review_should_check_localhost_only_binding = true', 'runtime_application_go_no_go_review_should_check_mock_first_default = true', 'runtime_application_go_no_go_review_should_check_private_artifact_boundary = true', 'runtime_application_go_no_go_review_should_check_no_external_target_authorization = true', 'runtime_application_go_no_go_review_should_check_no_real_scanner_execution = true', 'runtime_application_go_no_go_review_should_check_gateway_behavior_change_risk = true', 'runtime_application_go_no_go_review_should_check_reversal_or_rollback_boundary = true', 'runtime_application_go_no_go_review_should_check_test_command_clarity = true', 'runtime_application_go_no_go_review_should_check_claim_boundary_preservation = true', 'deprioritized_public_launch_work = true', 'deprioritized_customer_demo_work = true', 'deprioritized_repository_metadata_work = true', 'deprioritized_real_scanner_execution_work = true', 'deprioritized_external_target_work = true', 'deprioritized_commercial_material_work = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_demo_runtime_application_go_no_go_review', 'safe_local_only_demo_runtime_application_go_no_go_review_recommended = true', 'next_work_selection_using_risk_tiered_granularity_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'next work selection is not runtime application', 'next work selection is not execution authorization', 'next work selection is not real execution permission', 'next work selection is not external target authorization', 'next work selection is not public demo readiness', 'next work selection is not scanner readiness', 'next work selection is not production readiness', 'No private generated outputs are moved public in v0.6.333.', 'v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06333_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0408",
        "Status: accepted",
        "Select `safe_local_only_demo_runtime_application_go_no_go_review` as the next work item using risk-tiered granularity.",
    ])
    assert_tokens(ISSUE, [
        "0408 - Add v0.6.333 Next Work Selection Using Risk-Tiered Granularity",
        "Status: completed by v0.6.333",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_go_no_go_review",
        "Proceed to v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review",
    ])

def test_v06333_index_files() -> None:
    assert_tokens(README, [
        "v0.6.333 Next Work Selection Using Risk-Tiered Granularity",
        "next_work_selection_result = safe_local_only_demo_runtime_application_go_no_go_review",
        "selected_next_work_version = v0.6.334",
        "runtime_application_go_no_go_review_selected = true",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_go_no_go_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.333 - Next Work Selection Using Risk-Tiered Granularity",
        "Selected `safe_local_only_demo_runtime_application_go_no_go_review` as the next work item",
        "selected_next_work_version = v0.6.334",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_go_no_go_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.333",
        "v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review",
        "no safe local-only demo runtime application Go/No-Go review completed",
        "no safe local-only demo execution boundary runtime-applied",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06333_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06333_next_work_selection_using_risk_tiered_granularity.py"])

def test_v06333_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06333_primary_files()
    test_v06333_index_files()
    test_v06333_registered_in_run_all()
    test_v06333_avoids_raw_forbidden_claim_phrases()
    print("v0.6.333 next work selection using risk-tiered granularity checks passed")

if __name__ == "__main__":
    main()
