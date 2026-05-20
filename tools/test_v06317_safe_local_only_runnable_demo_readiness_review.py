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
DOC = ROOT / "docs/392-v06317-safe-local-only-runnable-demo-readiness-review.md"
ADR = ROOT / "planning/decisions/ADR-0392-add-v06317-safe-local-only-runnable-demo-readiness-review.md"
ISSUE = ROOT / "planning/issues/0392-add-v06317-safe-local-only-runnable-demo-readiness-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_readiness_review_completed = true', 'safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317', 'safe_local_only_runnable_demo_readiness_review_result = ready_as_mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_readiness_review_status = completed_safe_local_only_demo_ready', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'safe_local_only_runnable_demo_publication_ready = false', 'safe_local_only_runnable_demo_external_poc_ready = false', 'safe_local_only_runnable_demo_customer_demo_ready = false', 'safe_local_only_runnable_demo_path_creation_review_completed = true', 'safe_local_only_runnable_demo_path_creation_accepted = true', 'safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path_creation_review_result = accepted_as_mock_first_localhost_only_reviewer_path', 'safe_local_only_runnable_demo_path_created = true', 'safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310', 'safe_local_only_runnable_demo_path_status = accepted_created_not_runtime_applied', 'safe_local_only_runnable_demo_path_applied = false', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'readiness_review_mock_gateway_demo_available = true', 'readiness_review_allowed_action_output_available = true', 'readiness_review_denied_action_output_available = true', 'readiness_review_human_approval_required_output_available = true', 'readiness_review_local_target_lab_profile_available = true', 'readiness_review_runtime_destination_binding_available = true', 'readiness_review_bounded_transition_available = true', 'readiness_review_local_execution_plan_review_available = true', 'readiness_review_runtime_safety_policy_available = true', 'readiness_review_runtime_enforcement_design_available = true', 'readiness_review_execution_authorization_gate_available = true', 'readiness_review_preflight_validation_available = true', 'readiness_review_preflight_evidence_examples_available = true', 'readiness_review_private_artifact_review_available = true', 'readiness_review_terminal_walkthrough_available = true', 'readiness_review_json_evidence_references_available = true', 'readiness_review_markdown_evidence_references_available = true', 'readiness_review_expected_outputs_available = true', 'readiness_review_stop_conditions_available = true', 'readiness_review_cleanup_boundary_available = true', 'readiness_review_mock_first_confirmed = true', 'readiness_review_localhost_only_confirmed = true', 'readiness_review_execution_blocked_by_default_confirmed = true', 'readiness_review_private_not_in_git_outputs_confirmed = true', 'readiness_review_no_private_outputs_moved_public_confirmed = true', 'readiness_review_no_external_targets_confirmed = true', 'readiness_review_no_public_internet_targets_confirmed = true', 'readiness_review_no_private_lan_targets_confirmed = true', 'readiness_review_no_customer_or_third_party_targets_confirmed = true', 'readiness_review_no_production_targets_confirmed = true', 'readiness_review_no_credential_use_confirmed = true', 'readiness_review_no_unreviewed_live_scanner_execution_confirmed = true', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook', 'safe_local_only_runnable_demo_reviewer_runbook_recommended = true', 'safe_local_only_runnable_demo_readiness_review_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_readiness_review', 'safe_local_only_runnable_demo_readiness_review_v06317', 'safe_local_only_runnable_demo_reviewer_runbook', 'safe_local_only_runnable_demo_ready', 'safe_local_only_runnable_demo_ready_scope', 'mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_v06310', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'safe local-only runnable demo path', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo readiness review is not execution authorization', 'safe local-only runnable demo readiness review is not runtime-applied enforcement', 'safe local-only runnable demo readiness review is not runtime demo readiness', 'safe local-only runnable demo readiness review is not scanner readiness', 'safe local-only runnable demo readiness review is not production readiness', 'safe local-only runnable demo readiness review is not external target authorization', 'No private generated outputs are moved public in v0.6.317.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.317 Safe Local-Only Runnable Demo Readiness Review', 'Previous checkpoint: v0.6.316 Safe Local-Only Runnable Demo Path Creation Review and Decision', 'Readiness result: ready as mock-first localhost-only reviewer demo', 'Application status: readiness review only; no runtime application, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only runnable demo readiness mock gateway demo is available', 'safe local-only runnable demo readiness local target lab profile is available', 'safe local-only runnable demo readiness runtime destination binding is available', 'safe local-only runnable demo readiness execution authorization gate is available', 'safe local-only runnable demo readiness preflight validation is available', 'safe local-only runnable demo readiness private artifact review is available', 'safe local-only runnable demo readiness review is not execution authorization', 'safe local-only runnable demo readiness review is not runtime-applied enforcement', 'safe local-only runnable demo readiness review is not runtime demo readiness', 'safe local-only runnable demo readiness review is not scanner readiness', 'safe local-only runnable demo readiness review is not production readiness', 'safe local-only runnable demo readiness review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook', 'safe_local_only_runnable_demo_reviewer_runbook_recommended = true', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_public_ready = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.318 Safe Local-Only Runnable Demo Reviewer Runbook']

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

def test_v06317_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06317_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0392",
        "Status: completed readiness review",
        "Record that the safe local-only runnable demo is ready for a local reviewer walkthrough, limited to a mock-first localhost-only demo scope.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06317_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0392 - Add v0.6.317 Safe Local-Only Runnable Demo Readiness Review",
        "Status: completed by v0.6.317",
        "safe_local_only_runnable_demo_readiness_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook",
        "Proceed to v0.6.318 Safe Local-Only Runnable Demo Reviewer Runbook",
    ])

def test_v06317_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.317 Safe Local-Only Runnable Demo Readiness Review",
        "safe_local_only_runnable_demo_readiness_review_completed = true",
        "safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317",
        "safe_local_only_runnable_demo_readiness_review_result = ready_as_mock_first_localhost_only_reviewer_demo",
        "safe_local_only_runnable_demo_ready = true",
        "safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo",
        "safe_local_only_runnable_demo_public_ready = false",
        "readiness_review_mock_gateway_demo_available = true",
        "readiness_review_local_target_lab_profile_available = true",
        "readiness_review_runtime_destination_binding_available = true",
        "readiness_review_execution_authorization_gate_available = true",
        "readiness_review_preflight_validation_available = true",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.317 - Safe Local-Only Runnable Demo Readiness Review",
        "Reviewed the safe local-only runnable demo and recorded readiness for a local reviewer walkthrough.",
        "safe_local_only_runnable_demo_readiness_review_completed = true",
        "safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317",
        "safe_local_only_runnable_demo_readiness_review_result = ready_as_mock_first_localhost_only_reviewer_demo",
        "safe_local_only_runnable_demo_ready = true",
        "safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo",
        "safe_local_only_runnable_demo_public_ready = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_reviewer_runbook",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.317",
        "v0.6.318 Safe Local-Only Runnable Demo Reviewer Runbook",
        "no public demo readiness",
        "no publication approval",
        "no public announcement",
        "no customer demo approval",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
        "no safe local-only demo execution boundary runtime-applied",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06317_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06317_safe_local_only_runnable_demo_readiness_review.py"])

def main() -> None:
    test_v06317_doc_tokens()
    test_v06317_adr_tokens()
    test_v06317_issue_tokens()
    test_v06317_index_tokens()
    test_v06317_registered_in_run_all()
    print("v0.6.317 safe local-only runnable demo readiness review checks passed")

if __name__ == "__main__":
    main()
