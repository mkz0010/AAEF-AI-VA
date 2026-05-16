from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/362-v06287-safe-runnable-demo-gap-inventory.md"
ADR = ROOT / "planning/decisions/ADR-0362-add-v06287-safe-runnable-demo-gap-inventory.md"
ISSUE = ROOT / "planning/issues/0362-add-v06287-safe-runnable-demo-gap-inventory.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_runnable_demo_gap_inventory_created = true', 'safe_runnable_demo_gap_inventory_completed = true', 'safe_runnable_demo_gap_inventory_id = safe_runnable_demo_gap_inventory_v06287', 'safe_runnable_demo_gap_inventory_status = completed_gap_inventory_not_runtime_readiness', 'safe_runnable_demo_gap_inventory_scope = inventory_only_for_current_safe_mock_and_local_only_demo_path_gaps', 'recommended_next_work_item = safe_runnable_demo_path_selection', 'safe_runnable_demo_path_selection_recommended = true', 'safe_runnable_demo_path_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_demo_execution_boundary_accepted = false', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'safe_runnable_demo_gap_inventory_accepted_as_runtime_demo = false', 'safe_runnable_demo_gap_inventory_accepted_as_scanner_readiness = false', 'safe_runnable_demo_gap_inventory_accepted_as_production_readiness = false', 'safe_mock_demo_inventory_recorded = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'local_only_runnable_demo_inventory_recorded = true', 'local_only_runnable_demo_status = gap_inventory_only_not_ready', 'real_scanner_execution_inventory_recorded = true', 'real_scanner_execution_status = blocked', 'real_execution_permitted = false', 'execution_authorized = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'local_execution_plan_review_status = plan_recorded_execution_blocked', 'runtime_safety_policy_status = policy_recorded_execution_blocked', 'runtime_enforcement_design_status = design_recorded_execution_blocked', 'execution_authorization_gate_status = authorization_scaffold_recorded_execution_blocked', 'preflight_validation_status = preflight_scaffold_recorded_execution_blocked', 'preflight_check_implementation_status = implementation_scaffold_recorded_execution_blocked', 'preflight_evidence_model_status = evidence_model_recorded_execution_blocked', 'preflight_evidence_examples_status = examples_recorded_execution_blocked', 'preflight_evidence_validation_rules_status = validation_rules_recorded_execution_blocked', 'concrete_checks_implemented = false', 'preflight_satisfied = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'local_target_mode = localhost_only', 'external_discovery_allowed = false', 'external_discovery_fail_closed_required = true', 'kill_switch_required_for_future_runtime_demo = true', 'allowlist_required_for_future_runtime_demo = true', 'human_approval_required_for_future_runtime_demo = true', 'result_sanitization_required_for_future_runtime_demo = true', 'evidence_chain_required_for_future_runtime_demo = true', 'safe_mock_demo_private_artifacts_remain_private = true', 'private_generated_outputs_moved_public = false', 'continued_follow_up_trace_review_completed = true', 'continued_follow_up_trace_accepted = true', 'continued_follow_up_trace_id = continued_follow_up_trace_v06285', 'continued_follow_up_trace_review_result = accepted_as_non_claim_continued_trace_records_for_demo_path_inventory', 'continued_follow_up_trace_conclusions_created = false', 'continued_follow_up_trace_report_findings_created = false', 'accepted_defect_records_created = false', 'code_inspection_report_created = false', 'gateway_path_integration_verification_report_created = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'fixtures_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'publication_approval = false', 'production_readiness_claim = false', 'scanner_readiness_claim = false', 'external_poc_readiness_claim = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_runnable_demo_gap_inventory', 'safe_runnable_demo_gap_inventory_v06287', 'safe_runnable_demo_path_selection', 'local_only_demo_execution_boundary_candidate', 'safe mock demo', 'local-only runnable demo', 'real scanner execution remains blocked', 'mock demo is not live scanner execution', 'runtime readiness status', 'target lab gate status', 'transition gate status', 'execution authorized', 'real execution permitted', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'plan review gate status: plan_recorded_execution_blocked', 'safety policy gate status: policy_recorded_execution_blocked', 'runtime enforcement implemented: False', 'execution authorized: False', 'real execution permitted: False', 'safe runnable demo gap inventory is not runtime demo readiness', 'safe runnable demo gap inventory is not scanner readiness', 'safe runnable demo gap inventory is not production readiness', 'No private generated outputs are moved public in v0.6.287.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.287 Safe Runnable Demo Gap Inventory', 'Previous checkpoint: v0.6.286 Continued Follow-Up Trace Review and Decision', 'Inventory result: safe runnable demo gap inventory created', 'Application status: inventory only; no runtime demo readiness, scanner readiness, execution authorization, or gateway behavior changed', 'safe mock demo is currently available as private generated artifacts', 'local-only runnable demo is not yet ready', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe runnable demo gap inventory is not runtime demo readiness', 'safe runnable demo gap inventory is not scanner readiness', 'safe runnable demo gap inventory is not production readiness', 'recommended_next_work_item = safe_runnable_demo_path_selection', 'safe_runnable_demo_path_selection_recommended = true', 'local_only_demo_execution_boundary_candidate_created = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.288 Safe Runnable Demo Path Selection']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06287_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06287_adr_tokens() -> None:
    assert_tokens(ADR, ["ADR-0362", "Status: accepted", "Create a Safe Runnable Demo Gap Inventory."] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06287_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0362 - Add v0.6.287 Safe Runnable Demo Gap Inventory",
        "Status: completed by v0.6.287",
        "safe_runnable_demo_gap_inventory_created = true",
        "recommended_next_work_item = safe_runnable_demo_path_selection",
        "Proceed to v0.6.288 Safe Runnable Demo Path Selection",
    ])

def test_v06287_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.287 Safe Runnable Demo Gap Inventory",
        "safe_runnable_demo_gap_inventory_created = true",
        "safe_runnable_demo_gap_inventory_id = safe_runnable_demo_gap_inventory_v06287",
        "safe_mock_demo_status = runnable_private_artifact_demo_available",
        "local_only_runnable_demo_status = gap_inventory_only_not_ready",
        "real_scanner_execution_status = blocked",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_runnable_demo_path_selection",
        "safe_runnable_demo_path_selection_recommended = true",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.287 - Safe Runnable Demo Gap Inventory",
        "Created a Safe Runnable Demo Gap Inventory.",
        "safe_runnable_demo_gap_inventory_created = true",
        "safe_runnable_demo_gap_inventory_id = safe_runnable_demo_gap_inventory_v06287",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.287",
        "v0.6.288 Safe Runnable Demo Path Selection",
        "no safe runnable demo path selected",
        "no local-only demo execution boundary candidate",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06287_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06287_safe_runnable_demo_gap_inventory.py"])

def main() -> None:
    test_v06287_doc_tokens()
    test_v06287_adr_tokens()
    test_v06287_issue_tokens()
    test_v06287_index_tokens()
    test_v06287_registered_in_run_all()
    print("v0.6.287 safe runnable demo gap inventory checks passed")

if __name__ == "__main__":
    main()
