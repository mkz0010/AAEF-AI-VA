from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/409-v06334-safe-local-only-demo-runtime-application-go-no-go-review.md"
ADR = ROOT / "planning/decisions/ADR-0409-add-v06334-safe-local-only-demo-runtime-application-go-no-go-review.md"
ISSUE = ROOT / "planning/issues/0409-add-v06334-safe-local-only-demo-runtime-application-go-no-go-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review', 'safe_local_only_demo_runtime_application_go_no_go_review_completed = true', 'safe_local_only_demo_runtime_application_go_no_go_review_id = safe_local_only_demo_runtime_application_go_no_go_review_v06334', 'safe_local_only_demo_runtime_application_go_no_go_review_result = conditional_go_for_bounded_implementation_candidate_not_runtime_applied', 'safe_local_only_demo_runtime_application_go_no_go_review_scope = review_only_no_runtime_application', 'safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go', 'safe_local_only_demo_runtime_application_go_no_go_decision_reason = accepted_candidate_track_closed_runtime_applied_false_with_local_only_constraints_preserved', 'safe_local_only_demo_runtime_application_implementation_candidate_allowed_next = true', 'safe_local_only_demo_runtime_application_implementation_candidate_created = false', 'safe_local_only_demo_runtime_application_implementation_candidate_review_completed = false', 'safe_local_only_demo_runtime_application_closeout_review_completed = true', 'safe_local_only_demo_runtime_application_closeout_review_id = safe_local_only_demo_runtime_application_closeout_review_v06332', 'safe_local_only_demo_runtime_application_closeout_review_result = track_closed_runtime_applied_false', 'safe_local_only_demo_runtime_application_track_status = closed', 'safe_local_only_demo_runtime_application_track_outcome = bounded_candidate_accepted_not_runtime_applied', 'safe_local_only_demo_runtime_application_candidate_review_completed = true', 'safe_local_only_demo_runtime_application_candidate_accepted = true', 'safe_local_only_demo_runtime_application_candidate_id = safe_local_only_demo_runtime_application_candidate_v06330', 'safe_local_only_demo_runtime_application_candidate_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'go_no_go_accepted_candidate_scope_checked = true', 'go_no_go_localhost_only_binding_checked = true', 'go_no_go_loopback_only_target_checked = true', 'go_no_go_mock_first_default_checked = true', 'go_no_go_private_artifact_boundary_checked = true', 'go_no_go_no_external_target_authorization_checked = true', 'go_no_go_no_real_scanner_execution_checked = true', 'go_no_go_gateway_behavior_change_risk_checked = true', 'go_no_go_reversal_or_rollback_boundary_checked = true', 'go_no_go_test_command_clarity_checked = true', 'go_no_go_claim_boundary_preservation_checked = true', 'go_no_go_result_requires_candidate_only_next_step = true', 'go_no_go_result_forbids_direct_runtime_application = true', 'go_no_go_result_forbids_execution_authorization = true', 'go_no_go_result_forbids_real_execution = true', 'go_no_go_result_forbids_external_target_authorization = true', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'private_generated_outputs_moved_public = false', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate', 'safe_local_only_demo_runtime_application_implementation_candidate_recommended = true', 'safe_local_only_demo_runtime_application_go_no_go_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'Go/No-Go review is not runtime application', 'Go/No-Go review is not execution authorization', 'Go/No-Go review is not real execution permission', 'Go/No-Go review is not external target authorization', 'Go/No-Go review is not public demo readiness', 'Go/No-Go review is not scanner readiness', 'Go/No-Go review is not production readiness', 'No private generated outputs are moved public in v0.6.334.', 'v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06334_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0409",
        "Status: accepted",
        "Record a conditional go for a bounded implementation candidate only. Direct runtime application remains deferred.",
    ])
    assert_tokens(ISSUE, [
        "0409 - Add v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review",
        "Status: completed by v0.6.334",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate",
        "Proceed to v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate",
    ])

def test_v06334_index_files() -> None:
    assert_tokens(README, [
        "v0.6.334 Safe Local-Only Demo Runtime Application Go/No-Go Review",
        "safe_local_only_demo_runtime_application_go_no_go_review_completed = true",
        "safe_local_only_demo_runtime_application_go_no_go_review_result = conditional_go_for_bounded_implementation_candidate_not_runtime_applied",
        "safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go",
        "safe_local_only_demo_runtime_application_implementation_candidate_allowed_next = true",
        "safe_local_only_demo_runtime_application_implementation_candidate_created = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.334 - Safe Local-Only Demo Runtime Application Go/No-Go Review",
        "Performed a Go/No-Go review for a later bounded safe local-only demo runtime application implementation candidate.",
        "safe_local_only_demo_runtime_application_go_no_go_decision = conditional_go",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_implementation_candidate",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.334",
        "v0.6.335 Safe Local-Only Demo Runtime Application Implementation Candidate",
        "no safe local-only demo runtime application implementation candidate created",
        "no safe local-only demo execution boundary runtime-applied",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06334_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06334_safe_local_only_demo_runtime_application_go_no_go_review.py"])

def test_v06334_avoids_raw_forbidden_claim_phrases() -> None:
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
    test_v06334_primary_files()
    test_v06334_index_files()
    test_v06334_registered_in_run_all()
    test_v06334_avoids_raw_forbidden_claim_phrases()
    print("v0.6.334 safe local-only demo runtime application go/no-go review checks passed")

if __name__ == "__main__":
    main()
