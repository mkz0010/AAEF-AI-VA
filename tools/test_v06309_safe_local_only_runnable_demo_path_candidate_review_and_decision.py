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
DOC = ROOT / "docs/384-v06309-safe-local-only-runnable-demo-path-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0384-add-v06309-safe-local-only-runnable-demo-path-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0384-add-v06309-safe-local-only-runnable-demo-path-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_path_candidate_review_completed = true', 'safe_local_only_runnable_demo_path_candidate_accepted = true', 'safe_local_only_runnable_demo_path_candidate_id = safe_local_only_runnable_demo_path_candidate_v06308', 'safe_local_only_runnable_demo_path_candidate_review_result = accepted_as_safe_local_only_runnable_demo_path_candidate', 'safe_local_only_runnable_demo_path_candidate_status = accepted_as_safe_local_only_runnable_demo_path_candidate', 'reviewed_safe_local_only_runnable_demo_path_candidate_created = true', 'reviewed_safe_local_only_runnable_demo_path_candidate_status = candidate_not_applied', 'reviewed_safe_local_only_runnable_demo_path_candidate_scope = documentation_only_candidate_for_safe_local_only_runnable_demo_path', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_path_candidate_prerequisites_accepted = true', 'safe_local_only_runnable_demo_path_candidate_entrypoint_accepted = true', 'safe_local_only_runnable_demo_path_candidate_target_lab_profile_accepted = true', 'safe_local_only_runnable_demo_path_candidate_runtime_destination_binding_accepted = true', 'safe_local_only_runnable_demo_path_candidate_preflight_sequence_accepted = true', 'safe_local_only_runnable_demo_path_candidate_preflight_evidence_accepted = true', 'safe_local_only_runnable_demo_path_candidate_execution_authorization_gate_accepted = true', 'safe_local_only_runnable_demo_path_candidate_human_approval_gate_accepted = true', 'safe_local_only_runnable_demo_path_candidate_mock_first_execution_accepted = true', 'safe_local_only_runnable_demo_path_candidate_local_tool_invocation_accepted = true', 'safe_local_only_runnable_demo_path_candidate_evidence_output_accepted = true', 'safe_local_only_runnable_demo_path_candidate_review_walkthrough_accepted = true', 'safe_local_only_runnable_demo_path_candidate_stop_conditions_accepted = true', 'safe_local_only_runnable_demo_path_candidate_cleanup_boundary_accepted = true', 'safe_local_only_runnable_demo_path_candidate_expected_outputs_accepted = true', 'safe_local_only_runnable_demo_path_candidate_demo_command_sequence_accepted = true', 'safe_local_only_runnable_demo_path_candidate_excludes_external_targets = true', 'safe_local_only_runnable_demo_path_candidate_excludes_public_internet_targets = true', 'safe_local_only_runnable_demo_path_candidate_excludes_private_lan_targets = true', 'safe_local_only_runnable_demo_path_candidate_excludes_customer_or_third_party_targets = true', 'safe_local_only_runnable_demo_path_candidate_excludes_production_targets = true', 'safe_local_only_runnable_demo_path_candidate_excludes_credential_use = true', 'safe_local_only_runnable_demo_path_candidate_excludes_unreviewed_live_scanner_execution = true', 'safe_local_only_runnable_demo_path_candidate_excludes_public_movement_of_private_outputs = true', 'safe_local_only_runnable_demo_path_defined = false', 'safe_local_only_runnable_demo_path_applied = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_path_review_completed = false', 'safe_local_only_runnable_demo_path_accepted = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_runnable_demo_review_completed = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'local_only_runnable_demo_path_created = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_recommended = true', 'safe_local_only_runnable_demo_path_candidate_review_and_decision_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_path_candidate_review_and_decision', 'safe_local_only_runnable_demo_path_candidate_review_completed', 'safe_local_only_runnable_demo_path_candidate_accepted', 'safe_local_only_runnable_demo_path_candidate_v06308', 'safe_local_only_runnable_demo_path_candidate', 'safe_local_only_runnable_demo_path', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'safe local-only demo execution boundary', 'safe local-only runnable demo path candidate', 'safe local-only runnable demo path', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo path candidate review is not execution authorization', 'safe local-only runnable demo path candidate review is not runnable demo creation', 'safe local-only runnable demo path candidate review is not runtime-applied enforcement', 'safe local-only runnable demo path candidate review is not runtime demo readiness', 'safe local-only runnable demo path candidate review is not scanner readiness', 'safe local-only runnable demo path candidate review is not production readiness', 'safe local-only runnable demo path candidate review is not external target authorization', 'No private generated outputs are moved public in v0.6.309.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.309 Safe Local-Only Runnable Demo Path Candidate Review and Decision', 'Previous checkpoint: v0.6.308 Safe Local-Only Runnable Demo Path Candidate', 'Reviewed candidate: `safe_local_only_runnable_demo_path_candidate_v06308`', 'Decision result: accepted as safe local-only runnable demo path candidate', 'Application status: review only; no runnable demo path created, runtime application, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only runnable demo path candidate prerequisites are accepted', 'safe local-only runnable demo path candidate entrypoint is accepted', 'safe local-only runnable demo path candidate target lab profile is accepted', 'safe local-only runnable demo path candidate runtime destination binding is accepted', 'safe local-only runnable demo path candidate preflight sequence is accepted', 'safe local-only runnable demo path candidate execution authorization gate is accepted', 'safe local-only runnable demo path candidate evidence output is accepted', 'safe local-only runnable demo path candidate expected outputs are accepted', 'safe local-only runnable demo path candidate stop conditions are accepted', 'safe local-only runnable demo path candidate review is not execution authorization', 'safe local-only runnable demo path candidate review is not runnable demo creation', 'safe local-only runnable demo path candidate review is not runtime-applied enforcement', 'safe local-only runnable demo path candidate review is not runtime demo readiness', 'safe local-only runnable demo path candidate review is not scanner readiness', 'safe local-only runnable demo path candidate review is not production readiness', 'safe local-only runnable demo path candidate review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_recommended = true', 'safe_local_only_runnable_demo_path_defined = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.310 Safe Local-Only Runnable Demo Path']

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

def test_v06309_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06309_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0384",
        "Status: accepted",
        "Accept the v0.6.308 candidate as a safe local-only runnable demo path candidate.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06309_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0384 - Add v0.6.309 Safe Local-Only Runnable Demo Path Candidate Review and Decision",
        "Status: completed by v0.6.309",
        "safe_local_only_runnable_demo_path_candidate_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_path",
        "Proceed to v0.6.310 Safe Local-Only Runnable Demo Path",
    ])

def test_v06309_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.309 Safe Local-Only Runnable Demo Path Candidate Review and Decision",
        "safe_local_only_runnable_demo_path_candidate_review_completed = true",
        "safe_local_only_runnable_demo_path_candidate_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_id = safe_local_only_runnable_demo_path_candidate_v06308",
        "safe_local_only_runnable_demo_path_candidate_prerequisites_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_entrypoint_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_target_lab_profile_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_runtime_destination_binding_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_preflight_sequence_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_execution_authorization_gate_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_evidence_output_accepted = true",
        "safe_local_only_runnable_demo_path_defined = false",
        "safe_local_only_runnable_demo_path_created = false",
        "safe_local_only_runnable_demo_ready = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_path",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.309 - Safe Local-Only Runnable Demo Path Candidate Review and Decision",
        "Accepted the v0.6.308 Safe Local-Only Runnable Demo Path Candidate.",
        "safe_local_only_runnable_demo_path_candidate_review_completed = true",
        "safe_local_only_runnable_demo_path_candidate_accepted = true",
        "safe_local_only_runnable_demo_path_candidate_id = safe_local_only_runnable_demo_path_candidate_v06308",
        "recommended_next_work_item = safe_local_only_runnable_demo_path",
        "safe_local_only_runnable_demo_path_defined = false",
        "safe_local_only_runnable_demo_path_created = false",
        "safe_local_only_runnable_demo_ready = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.309",
        "v0.6.310 Safe Local-Only Runnable Demo Path",
        "no safe local-only runnable demo path defined",
        "no safe local-only runnable demo path created",
        "no safe local-only runnable demo ready",
        "no safe local-only demo execution boundary runtime-applied",
        "no publication approval",
        "no public announcement",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06309_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06309_safe_local_only_runnable_demo_path_candidate_review_and_decision.py"])

def main() -> None:
    test_v06309_doc_tokens()
    test_v06309_adr_tokens()
    test_v06309_issue_tokens()
    test_v06309_index_tokens()
    test_v06309_registered_in_run_all()
    print("v0.6.309 safe local-only runnable demo path candidate review and decision checks passed")

if __name__ == "__main__":
    main()
