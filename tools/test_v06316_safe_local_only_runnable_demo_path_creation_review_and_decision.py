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
DOC = ROOT / "docs/391-v06316-safe-local-only-runnable-demo-path-creation-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0391-add-v06316-safe-local-only-runnable-demo-path-creation-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0391-add-v06316-safe-local-only-runnable-demo-path-creation-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_path_creation_review_completed = true', 'safe_local_only_runnable_demo_path_creation_accepted = true', 'safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path_creation_review_result = accepted_as_mock_first_localhost_only_reviewer_path', 'safe_local_only_runnable_demo_path_creation_status = accepted_created_not_ready', 'reviewed_safe_local_only_runnable_demo_path_creation_created = true', 'reviewed_safe_local_only_runnable_demo_path_creation_status = created_documentation_and_command_path_only', 'reviewed_safe_local_only_runnable_demo_path_creation_scope = safe_local_only_mock_first_localhost_only_reviewer_path', 'safe_local_only_runnable_demo_path_created = true', 'safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310', 'safe_local_only_runnable_demo_path_status = accepted_created_not_ready', 'safe_local_only_runnable_demo_path_applied = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_runnable_demo_review_completed = false', 'safe_local_only_runnable_demo_readiness_review_created = false', 'safe_local_only_runnable_demo_path_creation_candidate_review_completed = true', 'safe_local_only_runnable_demo_path_creation_candidate_accepted = true', 'safe_local_only_runnable_demo_path_creation_candidate_id = safe_local_only_runnable_demo_path_creation_candidate_v06313', 'safe_local_only_runnable_demo_path_creation_candidate_review_result = accepted_as_safe_local_only_runnable_demo_path_creation_candidate', 'safe_local_only_runnable_demo_path_creation_readiness_review_completed = true', 'safe_local_only_runnable_demo_path_creation_readiness_review_id = safe_local_only_runnable_demo_path_creation_readiness_review_v06312', 'safe_local_only_runnable_demo_path_review_completed = true', 'safe_local_only_runnable_demo_path_accepted = true', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'creation_path_mock_gateway_demo_command_accepted = true', 'creation_path_allowed_action_output_reference_accepted = true', 'creation_path_denied_action_output_reference_accepted = true', 'creation_path_human_approval_required_output_reference_accepted = true', 'creation_path_local_target_lab_profile_reference_accepted = true', 'creation_path_runtime_destination_binding_reference_accepted = true', 'creation_path_bounded_transition_reference_accepted = true', 'creation_path_local_execution_plan_review_reference_accepted = true', 'creation_path_runtime_safety_policy_reference_accepted = true', 'creation_path_runtime_enforcement_design_reference_accepted = true', 'creation_path_execution_authorization_gate_reference_accepted = true', 'creation_path_preflight_validation_reference_accepted = true', 'creation_path_preflight_evidence_reference_accepted = true', 'creation_path_private_artifact_review_reference_accepted = true', 'creation_path_reviewer_walkthrough_accepted = true', 'creation_path_expected_terminal_outputs_accepted = true', 'creation_path_expected_json_outputs_accepted = true', 'creation_path_expected_markdown_outputs_accepted = true', 'creation_path_stop_conditions_accepted = true', 'creation_path_cleanup_boundary_accepted = true', 'creation_path_mock_first = true', 'creation_path_localhost_only = true', 'creation_path_execution_blocked_by_default = true', 'creation_path_private_not_in_git_outputs = true', 'creation_path_no_private_outputs_moved_public = true', 'creation_path_excludes_external_targets = true', 'creation_path_excludes_public_internet_targets = true', 'creation_path_excludes_private_lan_targets = true', 'creation_path_excludes_customer_or_third_party_targets = true', 'creation_path_excludes_production_targets = true', 'creation_path_excludes_credential_use = true', 'creation_path_excludes_unreviewed_live_scanner_execution = true', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_readiness_review', 'safe_local_only_runnable_demo_readiness_review_recommended = true', 'safe_local_only_runnable_demo_path_creation_review_and_decision_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_path_creation_review_and_decision', 'safe_local_only_runnable_demo_path_creation_review_completed', 'safe_local_only_runnable_demo_path_creation_accepted', 'safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path_creation', 'safe_local_only_runnable_demo_readiness_review', 'safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_v06310', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'safe local-only runnable demo path', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo path creation review is not execution authorization', 'safe local-only runnable demo path creation review is not runtime-applied enforcement', 'safe local-only runnable demo path creation review is not runtime demo readiness', 'safe local-only runnable demo path creation review is not scanner readiness', 'safe local-only runnable demo path creation review is not production readiness', 'safe local-only runnable demo path creation review is not external target authorization', 'No private generated outputs are moved public in v0.6.316.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.316 Safe Local-Only Runnable Demo Path Creation Review and Decision', 'Previous checkpoint: v0.6.315 Safe Local-Only Runnable Demo Path Creation', 'Reviewed creation: `safe_local_only_runnable_demo_path_creation_v06315`', 'Decision result: accepted as mock-first localhost-only reviewer path', 'Application status: review only; no runtime application, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only runnable demo path creation mock gateway demo command is accepted', 'safe local-only runnable demo path creation local target lab profile reference is accepted', 'safe local-only runnable demo path creation runtime destination binding reference is accepted', 'safe local-only runnable demo path creation execution authorization gate reference is accepted', 'safe local-only runnable demo path creation preflight validation reference is accepted', 'safe local-only runnable demo path creation private artifact review reference is accepted', 'safe local-only runnable demo path creation review is not execution authorization', 'safe local-only runnable demo path creation review is not runtime-applied enforcement', 'safe local-only runnable demo path creation review is not runtime demo readiness', 'safe local-only runnable demo path creation review is not scanner readiness', 'safe local-only runnable demo path creation review is not production readiness', 'safe local-only runnable demo path creation review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_readiness_review', 'safe_local_only_runnable_demo_readiness_review_recommended = true', 'safe_local_only_runnable_demo_readiness_review_created = false', 'safe_local_only_runnable_demo_path_created = true', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.317 Safe Local-Only Runnable Demo Readiness Review']

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

def test_v06316_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06316_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0391",
        "Status: accepted",
        "Accept the v0.6.315 created path as the current safe local-only runnable demo path.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06316_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0391 - Add v0.6.316 Safe Local-Only Runnable Demo Path Creation Review and Decision",
        "Status: completed by v0.6.316",
        "safe_local_only_runnable_demo_path_creation_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_readiness_review",
        "Proceed to v0.6.317 Safe Local-Only Runnable Demo Readiness Review",
    ])

def test_v06316_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.316 Safe Local-Only Runnable Demo Path Creation Review and Decision",
        "safe_local_only_runnable_demo_path_creation_review_completed = true",
        "safe_local_only_runnable_demo_path_creation_accepted = true",
        "safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315",
        "safe_local_only_runnable_demo_path_creation_review_result = accepted_as_mock_first_localhost_only_reviewer_path",
        "safe_local_only_runnable_demo_path_created = true",
        "safe_local_only_runnable_demo_path_status = accepted_created_not_ready",
        "creation_path_mock_gateway_demo_command_accepted = true",
        "creation_path_local_target_lab_profile_reference_accepted = true",
        "creation_path_runtime_destination_binding_reference_accepted = true",
        "creation_path_execution_authorization_gate_reference_accepted = true",
        "creation_path_preflight_validation_reference_accepted = true",
        "safe_local_only_runnable_demo_readiness_review_created = false",
        "safe_local_only_runnable_demo_ready = false",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_readiness_review",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.316 - Safe Local-Only Runnable Demo Path Creation Review and Decision",
        "Accepted the v0.6.315 Safe Local-Only Runnable Demo Path Creation as a mock-first, localhost-only reviewer path.",
        "safe_local_only_runnable_demo_path_creation_review_completed = true",
        "safe_local_only_runnable_demo_path_creation_accepted = true",
        "safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315",
        "recommended_next_work_item = safe_local_only_runnable_demo_readiness_review",
        "safe_local_only_runnable_demo_ready = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.316",
        "v0.6.317 Safe Local-Only Runnable Demo Readiness Review",
        "no safe local-only runnable demo readiness review created",
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

def test_v06316_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06316_safe_local_only_runnable_demo_path_creation_review_and_decision.py"])

def main() -> None:
    test_v06316_doc_tokens()
    test_v06316_adr_tokens()
    test_v06316_issue_tokens()
    test_v06316_index_tokens()
    test_v06316_registered_in_run_all()
    print("v0.6.316 safe local-only runnable demo path creation review and decision checks passed")

if __name__ == "__main__":
    main()
