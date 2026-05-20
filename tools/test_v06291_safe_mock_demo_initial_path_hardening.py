from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_V06371_ALLOWED_ACTION_DISPLAY = (
    "allowed-action: raw_execution_status=completed; "
    "reviewer_status=mock_dry_run_completed_no_real_execution; "
    "external_process_executed=false; "
    "network_activity_performed=false"
)
EXPECTED_V06371_ALLOWED_ACTION_DISPLAY_MULTILINE = "\n".join(
    [
        "allowed-action:",
        "  raw_execution_status: completed",
        "  reviewer_status: mock_dry_run_completed_no_real_execution",
        "  external_process_executed: false",
        "  network_activity_performed: false",
    ]
)
DOC = ROOT / "docs/366-v06291-safe-mock-demo-initial-path-hardening.md"
ADR = ROOT / "planning/decisions/ADR-0366-add-v06291-safe-mock-demo-initial-path-hardening.md"
ISSUE = ROOT / "planning/issues/0366-add-v06291-safe-mock-demo-initial-path-hardening.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_mock_demo_initial_path_hardening_applied = true', 'safe_mock_demo_initial_path_hardening_completed = true', 'safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291', 'safe_mock_demo_initial_path_hardening_status = completed_documentation_only_safe_mock_demo_path_hardening', 'safe_mock_demo_initial_path_hardening_scope = documentation_only_safe_mock_demo_command_status_artifact_and_reviewer_boundary_hardening', 'reviewed_safe_mock_demo_initial_path_hardening_candidate_id = safe_mock_demo_initial_path_hardening_candidate_v06289', 'reviewed_safe_mock_demo_initial_path_hardening_candidate_accepted = true', 'reviewed_safe_mock_demo_initial_path_hardening_candidate_review_result = accepted_for_future_safe_mock_demo_initial_path_hardening', 'reviewed_safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288', 'selected_demo_path = safe_mock_demo_initial_path', 'safe_mock_demo_initial_path_selected = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'safe_mock_demo_command_clarity_hardened = true', 'safe_mock_demo_expected_status_explanation_hardened = true', 'safe_mock_demo_private_artifact_boundary_hardened = true', 'safe_mock_demo_reviewer_walkthrough_boundary_hardened = true', 'safe_mock_demo_non_live_scanner_warning_hardened = true', 'safe_mock_demo_local_only_runtime_separation_hardened = true', 'safe_mock_demo_public_positioning_hardened = true', 'safe_mock_demo_public_positioning_approved_for_publication = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'private_generated_outputs_moved_public = false', 'safe_mock_demo_initial_path_hardening_candidate_review_and_decision_completed = true', 'future_safe_mock_demo_initial_path_hardening_accepted = true', 'safe_mock_demo_initial_path_hardening_review_and_decision_created = false', 'recommended_next_work_item = safe_mock_demo_initial_path_hardening_review_and_decision', 'safe_mock_demo_initial_path_hardening_review_and_decision_recommended = true', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'local_execution_plan_review_status = plan_recorded_execution_blocked', 'runtime_safety_policy_status = policy_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'publication_approval = false', 'public_announcement = deferred', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_mock_demo_initial_path_hardening', 'safe_mock_demo_initial_path_hardening_v06291', 'safe_mock_demo_initial_path_hardening_review_and_decision', 'safe_mock_demo_initial_path_hardening_candidate_v06289', 'safe_mock_demo_initial_path_hardening_candidate_review_and_decision', 'safe_mock_demo_initial_path', 'safe_runnable_demo_path_selection_v06288', 'safe mock demo', 'safe mock demo path hardening', 'safe mock demo command clarity', 'safe mock demo expected status explanation', 'safe mock demo private artifact boundary', 'safe mock demo reviewer walkthrough boundary', 'safe mock demo non-live-scanner warning', 'safe mock demo local-only runtime separation', 'safe mock demo public positioning', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe mock demo hardening is not publication approval', 'safe mock demo hardening is not public artifact promotion', 'safe mock demo hardening is not runtime demo readiness', 'safe mock demo hardening is not scanner readiness', 'safe mock demo hardening is not production readiness', 'No private generated outputs are moved public in v0.6.291.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.291 Safe Mock Demo Initial Path Hardening', 'Previous checkpoint: v0.6.290 Safe Mock Demo Initial Path Hardening Candidate Review and Decision', 'Hardening result: safe mock demo initial path hardening applied', 'Application status: documentation-only hardening; no public artifact promotion, publication approval, runtime readiness, scanner readiness, or gateway behavior changed', 'safe mock demo command clarity is hardened', 'safe mock demo expected status explanation is hardened', 'safe mock demo private artifact boundary is hardened', 'safe mock demo reviewer walkthrough boundary is hardened', 'safe mock demo non-live-scanner warning is hardened', 'safe mock demo local-only runtime separation is hardened', 'safe mock demo hardening is not publication approval', 'safe mock demo hardening is not public artifact promotion', 'safe mock demo hardening is not runtime demo readiness', 'safe mock demo hardening is not scanner readiness', 'safe mock demo hardening is not production readiness', 'recommended_next_work_item = safe_mock_demo_initial_path_hardening_review_and_decision', 'safe_mock_demo_initial_path_hardening_review_and_decision_recommended = true', 'safe_mock_demo_public_artifact_promotion_created = false', 'publication_approval = false', 'local_only_demo_execution_boundary_candidate_created = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        if token == "allowed-action: completed":
            assert token in text or EXPECTED_V06371_ALLOWED_ACTION_DISPLAY in text or EXPECTED_V06371_ALLOWED_ACTION_DISPLAY_MULTILINE in text, (
                f"{path.relative_to(ROOT)} missing legacy or v0.6.371 allowed-action display"
            )
            continue
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06291_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06291_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0366",
        "Status: accepted",
        "Apply documentation-only hardening to the selected safe mock demo initial path.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06291_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0366 - Add v0.6.291 Safe Mock Demo Initial Path Hardening",
        "Status: completed by v0.6.291",
        "safe_mock_demo_initial_path_hardening_applied = true",
        "recommended_next_work_item = safe_mock_demo_initial_path_hardening_review_and_decision",
        "Proceed to v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision",
    ])

def test_v06291_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.291 Safe Mock Demo Initial Path Hardening",
        "safe_mock_demo_initial_path_hardening_applied = true",
        "safe_mock_demo_initial_path_hardening_completed = true",
        "safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291",
        "safe_mock_demo_command_clarity_hardened = true",
        "safe_mock_demo_expected_status_explanation_hardened = true",
        "safe_mock_demo_private_artifact_boundary_hardened = true",
        "safe_mock_demo_reviewer_walkthrough_boundary_hardened = true",
        "safe_mock_demo_non_live_scanner_warning_hardened = true",
        "safe_mock_demo_local_only_runtime_separation_hardened = true",
        "safe_mock_demo_public_artifact_promotion_created = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.291 - Safe Mock Demo Initial Path Hardening",
        "Applied documentation-only hardening to the selected safe mock demo initial path.",
        "safe_mock_demo_initial_path_hardening_applied = true",
        "safe_mock_demo_initial_path_hardening_completed = true",
        "safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.291",
        "v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision",
        "no public artifact promotion",
        "no publication approval",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no local-only demo execution boundary candidate",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06291_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06291_safe_mock_demo_initial_path_hardening.py"])

def main() -> None:
    test_v06291_doc_tokens()
    test_v06291_adr_tokens()
    test_v06291_issue_tokens()
    test_v06291_index_tokens()
    test_v06291_registered_in_run_all()
    print("v0.6.291 safe mock demo initial path hardening checks passed")

if __name__ == "__main__":
    main()
