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
DOC = ROOT / "docs/363-v06288-safe-runnable-demo-path-selection.md"
ADR = ROOT / "planning/decisions/ADR-0363-add-v06288-safe-runnable-demo-path-selection.md"
ISSUE = ROOT / "planning/issues/0363-add-v06288-safe-runnable-demo-path-selection.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_runnable_demo_path_selection_completed = true', 'safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288', 'selected_demo_path = safe_mock_demo_initial_path', 'selected_demo_path_status = selected_for_initial_safe_demo_path_hardening', 'selected_demo_path_reason = safe_mock_demo_is_currently_runnable_while_local_only_runtime_remains_blocked', 'safe_mock_demo_initial_path_selected = true', 'safe_mock_demo_path_hardening_recommended = true', 'safe_mock_demo_public_positioning_recommended = true', 'local_only_demo_execution_boundary_candidate_recommended = true', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'local_execution_plan_review_status = plan_recorded_execution_blocked', 'runtime_safety_policy_status = policy_recorded_execution_blocked', 'runtime_enforcement_design_status = design_recorded_execution_blocked', 'execution_authorization_gate_status = authorization_scaffold_recorded_execution_blocked', 'preflight_validation_status = preflight_scaffold_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'private_generated_outputs_moved_public = false', 'safe_runnable_demo_gap_inventory_completed = true', 'safe_runnable_demo_gap_inventory_id = safe_runnable_demo_gap_inventory_v06287', 'safe_runnable_demo_gap_inventory_accepted_as_runtime_demo = false', 'safe_runnable_demo_gap_inventory_accepted_as_scanner_readiness = false', 'recommended_next_work_item = safe_mock_demo_initial_path_hardening_candidate', 'safe_mock_demo_initial_path_hardening_candidate_created = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'publication_approval = false', 'public_announcement = deferred', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_runnable_demo_path_selection', 'safe_runnable_demo_path_selection_v06288', 'safe_mock_demo_initial_path', 'safe_mock_demo_initial_path_selected', 'safe_mock_demo_initial_path_hardening_candidate', 'safe_runnable_demo_gap_inventory_v06287', 'safe mock demo', 'local-only runnable demo', 'real scanner execution remains blocked', 'mock demo is not live scanner execution', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe mock demo initial path selection is not runtime demo readiness', 'safe mock demo initial path selection is not scanner readiness', 'safe mock demo initial path selection is not production readiness', 'safe mock demo public positioning is not publication approval', 'No private generated outputs are moved public in v0.6.288.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.288 Safe Runnable Demo Path Selection', 'Previous checkpoint: v0.6.287 Safe Runnable Demo Gap Inventory', 'Selection result: `safe_mock_demo_initial_path`', 'Application status: selection only; no runtime demo readiness, scanner readiness, execution authorization, publication approval, or gateway behavior changed', 'safe mock demo is selected as the initial path because it is currently runnable through private generated artifacts', 'local-only runnable demo remains a later boundary candidate', 'real scanner execution remains blocked', 'safe_mock_demo_initial_path_selected = true', 'local_only_demo_execution_boundary_candidate_created = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'recommended_next_work_item = safe_mock_demo_initial_path_hardening_candidate', 'safe mock demo initial path selection is not runtime demo readiness', 'safe mock demo initial path selection is not scanner readiness', 'safe mock demo initial path selection is not production readiness', 'safe mock demo public positioning is not publication approval', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.289 Safe Mock Demo Initial Path Hardening Candidate']

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

def test_v06288_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06288_adr_tokens() -> None:
    assert_tokens(ADR, ["ADR-0363", "Status: accepted", "Select `safe_mock_demo_initial_path` as the initial safe demo path."] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06288_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0363 - Add v0.6.288 Safe Runnable Demo Path Selection",
        "Status: completed by v0.6.288",
        "selected_demo_path = safe_mock_demo_initial_path",
        "Proceed to v0.6.289 Safe Mock Demo Initial Path Hardening Candidate",
    ])

def test_v06288_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.288 Safe Runnable Demo Path Selection",
        "safe_runnable_demo_path_selection_completed = true",
        "safe_runnable_demo_path_selection_id = safe_runnable_demo_path_selection_v06288",
        "selected_demo_path = safe_mock_demo_initial_path",
        "safe_mock_demo_initial_path_selected = true",
        "local_only_demo_execution_boundary_candidate_created = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_mock_demo_initial_path_hardening_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.288 - Safe Runnable Demo Path Selection",
        "Selected `safe_mock_demo_initial_path` as the initial safe demo path.",
        "safe_runnable_demo_path_selection_completed = true",
        "safe_mock_demo_initial_path_selected = true",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.288",
        "v0.6.289 Safe Mock Demo Initial Path Hardening Candidate",
        "no local-only demo execution boundary candidate",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no publication approval",
        "no public artifact promotion",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06288_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06288_safe_runnable_demo_path_selection.py"])

def main() -> None:
    test_v06288_doc_tokens()
    test_v06288_adr_tokens()
    test_v06288_issue_tokens()
    test_v06288_index_tokens()
    test_v06288_registered_in_run_all()
    print("v0.6.288 safe runnable demo path selection checks passed")

if __name__ == "__main__":
    main()
