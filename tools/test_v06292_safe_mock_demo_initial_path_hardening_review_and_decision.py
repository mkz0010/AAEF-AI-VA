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
DOC = ROOT / "docs/367-v06292-safe-mock-demo-initial-path-hardening-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0367-add-v06292-safe-mock-demo-initial-path-hardening-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0367-add-v06292-safe-mock-demo-initial-path-hardening-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_mock_demo_initial_path_hardening_review_completed = true', 'safe_mock_demo_initial_path_hardening_accepted = true', 'safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291', 'safe_mock_demo_initial_path_hardening_review_result = accepted_as_documentation_only_safe_mock_demo_path_hardening', 'safe_mock_demo_initial_path_hardening_status = accepted_as_documentation_only_safe_mock_demo_path_hardening', 'selected_demo_path = safe_mock_demo_initial_path', 'safe_mock_demo_initial_path_selected = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'safe_mock_demo_command_clarity_accepted = true', 'safe_mock_demo_expected_status_explanation_accepted = true', 'safe_mock_demo_private_artifact_boundary_accepted = true', 'safe_mock_demo_reviewer_walkthrough_boundary_accepted = true', 'safe_mock_demo_non_live_scanner_warning_accepted = true', 'safe_mock_demo_local_only_runtime_separation_accepted = true', 'safe_mock_demo_initial_path_hardening_accepted_as_public_artifact_promotion = false', 'safe_mock_demo_initial_path_hardening_accepted_as_publication_approval = false', 'safe_mock_demo_initial_path_hardening_accepted_as_runtime_demo_readiness = false', 'safe_mock_demo_initial_path_hardening_accepted_as_scanner_readiness = false', 'safe_mock_demo_initial_path_hardening_accepted_as_production_readiness = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'private_generated_outputs_moved_public = false', 'recommended_next_work_item = next_work_selection_using_risk_tiered_granularity', 'next_work_selection_recommended = true', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'local_only_demo_execution_boundary_candidate_created = false', 'real_scanner_execution_status = blocked', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'publication_approval = false', 'public_announcement = deferred', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_mock_demo_initial_path_hardening_review_and_decision', 'safe_mock_demo_initial_path_hardening_review_completed', 'safe_mock_demo_initial_path_hardening_accepted', 'safe_mock_demo_initial_path_hardening_v06291', 'safe_mock_demo_initial_path_hardening', 'safe_mock_demo_initial_path', 'safe mock demo', 'safe mock demo command clarity', 'safe mock demo expected status explanation', 'safe mock demo private artifact boundary', 'safe mock demo reviewer walkthrough boundary', 'safe mock demo non-live-scanner warning', 'safe mock demo local-only runtime separation', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe mock demo hardening review is not publication approval', 'safe mock demo hardening review is not public artifact promotion', 'safe mock demo hardening review is not runtime demo readiness', 'safe mock demo hardening review is not scanner readiness', 'safe mock demo hardening review is not production readiness', 'No private generated outputs are moved public in v0.6.292.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision', 'Previous checkpoint: v0.6.291 Safe Mock Demo Initial Path Hardening', 'Reviewed hardening: `safe_mock_demo_initial_path_hardening_v06291`', 'Decision result: accepted as documentation-only safe mock demo path hardening', 'Application status: review only; no public artifact promotion, publication approval, runtime readiness, scanner readiness, or gateway behavior changed', 'safe mock demo command clarity is accepted', 'safe mock demo expected status explanation is accepted', 'safe mock demo private artifact boundary is accepted', 'safe mock demo reviewer walkthrough boundary is accepted', 'safe mock demo non-live-scanner warning is accepted', 'safe mock demo local-only runtime separation is accepted', 'safe mock demo hardening review is not publication approval', 'safe mock demo hardening review is not public artifact promotion', 'safe mock demo hardening review is not runtime demo readiness', 'safe mock demo hardening review is not scanner readiness', 'safe mock demo hardening review is not production readiness', 'recommended_next_work_item = next_work_selection_using_risk_tiered_granularity', 'next_work_selection_recommended = true', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.293 Next Work Selection Using Risk-Tiered Granularity']

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

def test_v06292_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06292_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0367",
        "Status: accepted",
        "Accept the v0.6.291 documentation-only safe mock demo initial path hardening.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06292_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0367 - Add v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision",
        "Status: completed by v0.6.292",
        "safe_mock_demo_initial_path_hardening_review_completed = true",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
        "Proceed to v0.6.293 Next Work Selection Using Risk-Tiered Granularity",
    ])

def test_v06292_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.292 Safe Mock Demo Initial Path Hardening Review and Decision",
        "safe_mock_demo_initial_path_hardening_review_completed = true",
        "safe_mock_demo_initial_path_hardening_accepted = true",
        "safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291",
        "safe_mock_demo_initial_path_hardening_review_result = accepted_as_documentation_only_safe_mock_demo_path_hardening",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
        "next_work_selection_recommended = true",
        "safe_mock_demo_public_artifact_promotion_created = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.292 - Safe Mock Demo Initial Path Hardening Review and Decision",
        "Accepted the v0.6.291 documentation-only Safe Mock Demo Initial Path Hardening.",
        "safe_mock_demo_initial_path_hardening_review_completed = true",
        "safe_mock_demo_initial_path_hardening_accepted = true",
        "safe_mock_demo_initial_path_hardening_id = safe_mock_demo_initial_path_hardening_v06291",
        "recommended_next_work_item = next_work_selection_using_risk_tiered_granularity",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.292",
        "v0.6.293 Next Work Selection Using Risk-Tiered Granularity",
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

def test_v06292_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06292_safe_mock_demo_initial_path_hardening_review_and_decision.py"])

def main() -> None:
    test_v06292_doc_tokens()
    test_v06292_adr_tokens()
    test_v06292_issue_tokens()
    test_v06292_index_tokens()
    test_v06292_registered_in_run_all()
    print("v0.6.292 safe mock demo initial path hardening review and decision checks passed")

if __name__ == "__main__":
    main()
