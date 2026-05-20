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
DOC = ROOT / "docs/382-v06307-safe-local-only-demo-execution-boundary-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0382-add-v06307-safe-local-only-demo-execution-boundary-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0382-add-v06307-safe-local-only-demo-execution-boundary-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_review_result = accepted_as_documentation_level_boundary', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'reviewed_safe_local_only_demo_execution_boundary_defined = true', 'reviewed_safe_local_only_demo_execution_boundary_status = defined_not_runtime_applied', 'reviewed_safe_local_only_demo_execution_boundary_scope = documentation_level_localhost_only_demo_boundary', 'reviewed_safe_local_only_demo_execution_boundary_candidate_id = safe_local_only_demo_execution_boundary_candidate_v06304', 'reviewed_safe_local_only_demo_execution_boundary_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_loopback_targets_accepted = true', 'safe_local_only_demo_execution_boundary_allowed_targets_accepted = true', 'safe_local_only_demo_execution_boundary_denied_targets_accepted = true', 'safe_local_only_demo_execution_boundary_external_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_private_lan_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_public_ip_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_non_localhost_dns_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_customer_or_third_party_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_production_targets_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_external_discovery_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_credential_use_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_ai_only_target_selection_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_tool_mode_accepted = mock_first_no_live_scanner_default', 'safe_local_only_demo_execution_boundary_tool_allowlist_accepted = true', 'safe_local_only_demo_execution_boundary_no_live_scanner_default_accepted = true', 'safe_local_only_demo_execution_boundary_preflight_requirements_accepted = true', 'safe_local_only_demo_execution_boundary_fail_closed_conditions_accepted = true', 'safe_local_only_demo_execution_boundary_evidence_outputs_accepted = true', 'safe_local_only_demo_execution_boundary_operator_review_accepted = true', 'safe_local_only_demo_execution_boundary_human_approval_requirement_accepted = true', 'safe_local_only_demo_execution_boundary_runtime_transition_conditions_accepted = true', 'safe_local_only_demo_execution_boundary_external_authorization_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_path_selected = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_runnable_demo_review_completed = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_path_candidate', 'safe_local_only_runnable_demo_path_candidate_recommended = true', 'safe_local_only_demo_execution_boundary_review_and_decision_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_demo_execution_boundary_review_and_decision', 'safe_local_only_demo_execution_boundary_review_completed', 'safe_local_only_demo_execution_boundary_accepted', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'safe_local_only_demo_execution_boundary_candidate_v06304', 'safe_local_only_runnable_demo_path_candidate', 'safe_local_only_runnable_demo_path', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'safe local-only demo execution boundary', 'safe local-only runnable demo path candidate', 'safe local-only runnable demo path', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only demo execution boundary review is not execution authorization', 'safe local-only demo execution boundary review is not runtime-applied enforcement', 'safe local-only demo execution boundary review is not runnable demo readiness', 'safe local-only demo execution boundary review is not scanner readiness', 'safe local-only demo execution boundary review is not production readiness', 'safe local-only demo execution boundary review is not external target authorization', 'No private generated outputs are moved public in v0.6.307.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.307 Safe Local-Only Demo Execution Boundary Review and Decision', 'Previous checkpoint: v0.6.306 Safe Local-Only Demo Execution Boundary', 'Reviewed boundary: `safe_local_only_demo_execution_boundary_v06306`', 'Decision result: accepted as documentation-level boundary', 'Application status: review and decision only; no runtime application, runnable demo path created, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only demo execution boundary loopback targets are accepted', 'safe local-only demo execution boundary external target blockers are accepted', 'safe local-only demo execution boundary preflight requirements are accepted', 'safe local-only demo execution boundary fail-closed conditions are accepted', 'safe local-only demo execution boundary evidence outputs are accepted', 'safe local-only demo execution boundary review is not execution authorization', 'safe local-only demo execution boundary review is not runtime-applied enforcement', 'safe local-only demo execution boundary review is not runnable demo readiness', 'safe local-only demo execution boundary review is not scanner readiness', 'safe local-only demo execution boundary review is not production readiness', 'safe local-only demo execution boundary review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_path_candidate', 'safe_local_only_runnable_demo_path_candidate_recommended = true', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_path_created = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.308 Safe Local-Only Runnable Demo Path Candidate']

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

def test_v06307_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06307_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0382",
        "Status: accepted",
        "Accept the v0.6.306 Safe Local-Only Demo Execution Boundary as a documentation-level boundary.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06307_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0382 - Add v0.6.307 Safe Local-Only Demo Execution Boundary Review and Decision",
        "Status: completed by v0.6.307",
        "safe_local_only_demo_execution_boundary_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_candidate",
        "Proceed to v0.6.308 Safe Local-Only Runnable Demo Path Candidate",
    ])

def test_v06307_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.307 Safe Local-Only Demo Execution Boundary Review and Decision",
        "safe_local_only_demo_execution_boundary_review_completed = true",
        "safe_local_only_demo_execution_boundary_accepted = true",
        "safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306",
        "safe_local_only_demo_execution_boundary_review_result = accepted_as_documentation_level_boundary",
        "safe_local_only_demo_execution_boundary_target_mode = localhost_only",
        "safe_local_only_demo_execution_boundary_loopback_targets_accepted = true",
        "safe_local_only_demo_execution_boundary_external_targets_blocked_accepted = true",
        "safe_local_only_demo_execution_boundary_preflight_requirements_accepted = true",
        "safe_local_only_demo_execution_boundary_fail_closed_conditions_accepted = true",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "safe_local_only_demo_execution_boundary_applied = false",
        "safe_local_only_runnable_demo_path_created = false",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.307 - Safe Local-Only Demo Execution Boundary Review and Decision",
        "Accepted the v0.6.306 Safe Local-Only Demo Execution Boundary as a documentation-level boundary.",
        "safe_local_only_demo_execution_boundary_review_completed = true",
        "safe_local_only_demo_execution_boundary_accepted = true",
        "safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306",
        "recommended_next_work_item = safe_local_only_runnable_demo_path_candidate",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "safe_local_only_runnable_demo_path_created = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.307",
        "v0.6.308 Safe Local-Only Runnable Demo Path Candidate",
        "no safe local-only demo execution boundary runtime-applied",
        "no local-only runnable demo path created",
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

def test_v06307_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06307_safe_local_only_demo_execution_boundary_review_and_decision.py"])

def main() -> None:
    test_v06307_doc_tokens()
    test_v06307_adr_tokens()
    test_v06307_issue_tokens()
    test_v06307_index_tokens()
    test_v06307_registered_in_run_all()
    print("v0.6.307 safe local-only demo execution boundary review and decision checks passed")

if __name__ == "__main__":
    main()
