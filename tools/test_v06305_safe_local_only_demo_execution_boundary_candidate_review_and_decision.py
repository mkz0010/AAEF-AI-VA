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
DOC = ROOT / "docs/380-v06305-safe-local-only-demo-execution-boundary-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0380-add-v06305-safe-local-only-demo-execution-boundary-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0380-add-v06305-safe-local-only-demo-execution-boundary-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_demo_execution_boundary_candidate_review_completed = true', 'safe_local_only_demo_execution_boundary_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_candidate_id = safe_local_only_demo_execution_boundary_candidate_v06304', 'safe_local_only_demo_execution_boundary_candidate_review_result = accepted_as_safe_local_only_boundary_candidate', 'safe_local_only_demo_execution_boundary_candidate_status = accepted_as_safe_local_only_boundary_candidate', 'reviewed_safe_local_only_demo_execution_boundary_candidate_created = true', 'reviewed_safe_local_only_demo_execution_boundary_candidate_status = candidate_not_applied', 'reviewed_safe_local_only_demo_execution_boundary_candidate_scope = documentation_only_candidate_for_safe_local_only_demo_execution_boundary', 'reviewed_next_work_selection_id = next_work_selection_v06303', 'selected_work_item = safe_local_only_demo_execution_boundary_candidate', 'safe_local_only_demo_execution_boundary_candidate_selected = true', 'safe_local_only_demo_execution_boundary_target_mode_candidate = localhost_only', 'safe_local_only_demo_execution_boundary_loopback_targets_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_external_targets_candidate_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_private_lan_targets_candidate_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_public_ip_targets_candidate_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_dns_targets_candidate_blocked_accepted = true', 'safe_local_only_demo_execution_boundary_target_allowlist_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_target_denylist_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_tool_allowlist_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_mock_first_mode_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_no_live_scanner_default_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_preflight_requirements_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_fail_closed_conditions_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_evidence_outputs_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_operator_review_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_human_approval_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_runtime_transition_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_external_authorization_boundary_candidate_accepted = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_external_target_authorization = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_real_scanner_execution = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_customer_or_third_party_target = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_public_internet_target = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_production_target = true', 'safe_local_only_demo_execution_boundary_candidate_excludes_credential_use = true', 'safe_local_only_demo_execution_boundary_defined = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_demo_execution_boundary_accepted = false', 'safe_local_only_runnable_demo_path_selected = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_ready = false', 'safe_local_only_runnable_demo_review_completed = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_promotion_id = safe_mock_demo_public_artifact_promotion_v06301', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact_reviewed = true', 'safe_mock_demo_public_artifact_accepted = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'public_artifact_promotion_selected = false', 'safe_mock_demo_public_positioning_approved_for_publication = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_demo_execution_boundary', 'safe_local_only_demo_execution_boundary_recommended = true', 'safe_local_only_demo_execution_boundary_candidate_review_and_decision_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_demo_execution_boundary_candidate_review_and_decision', 'safe_local_only_demo_execution_boundary_candidate_review_completed', 'safe_local_only_demo_execution_boundary_candidate_accepted', 'safe_local_only_demo_execution_boundary_candidate_v06304', 'safe_local_only_demo_execution_boundary_candidate', 'safe_local_only_demo_execution_boundary', 'safe_local_only_runnable_demo_path', 'next_work_selection_v06303', 'safe_mock_demo_public_artifact_promotion_v06301', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact', 'safe_mock_demo_initial_path', 'safe mock demo', 'safe local-only demo execution boundary candidate', 'safe local-only demo execution boundary', 'safe local-only runnable demo path', 'localhost_only', 'loopback-only target boundary', 'external target authorization remains false', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only demo execution boundary candidate review is not execution authorization', 'safe local-only demo execution boundary candidate review is not boundary application', 'safe local-only demo execution boundary candidate review is not runtime demo readiness', 'safe local-only demo execution boundary candidate review is not scanner readiness', 'safe local-only demo execution boundary candidate review is not production readiness', 'safe local-only demo execution boundary candidate review is not external target authorization', 'No private generated outputs are moved public in v0.6.305.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.305 Safe Local-Only Demo Execution Boundary Candidate Review and Decision', 'Previous checkpoint: v0.6.304 Safe Local-Only Demo Execution Boundary Candidate', 'Reviewed candidate: `safe_local_only_demo_execution_boundary_candidate_v06304`', 'Decision result: accepted as safe local-only boundary candidate', 'Application status: review only; no boundary applied, runnable demo path created, execution authorization, runtime readiness, scanner readiness, or gateway behavior changed', 'safe local-only demo execution boundary loopback targets candidate is accepted', 'safe local-only demo execution boundary external targets candidate blocked rule is accepted', 'safe local-only demo execution boundary private LAN targets candidate blocked rule is accepted', 'safe local-only demo execution boundary preflight requirements candidate is accepted', 'safe local-only demo execution boundary fail-closed conditions candidate is accepted', 'safe local-only demo execution boundary evidence outputs candidate is accepted', 'safe local-only demo execution boundary candidate review is not execution authorization', 'safe local-only demo execution boundary candidate review is not boundary application', 'safe local-only demo execution boundary candidate review is not runtime demo readiness', 'safe local-only demo execution boundary candidate review is not scanner readiness', 'safe local-only demo execution boundary candidate review is not production readiness', 'safe local-only demo execution boundary candidate review is not external target authorization', 'recommended_next_work_item = safe_local_only_demo_execution_boundary', 'safe_local_only_demo_execution_boundary_recommended = true', 'safe_local_only_demo_execution_boundary_defined = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_runnable_demo_path_created = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.306 Safe Local-Only Demo Execution Boundary']

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

def test_v06305_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06305_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0380",
        "Status: accepted",
        "Accept the v0.6.304 candidate as a safe local-only boundary candidate for a future boundary step.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06305_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0380 - Add v0.6.305 Safe Local-Only Demo Execution Boundary Candidate Review and Decision",
        "Status: completed by v0.6.305",
        "safe_local_only_demo_execution_boundary_candidate_review_completed = true",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary",
        "Proceed to v0.6.306 Safe Local-Only Demo Execution Boundary",
    ])

def test_v06305_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.305 Safe Local-Only Demo Execution Boundary Candidate Review and Decision",
        "safe_local_only_demo_execution_boundary_candidate_review_completed = true",
        "safe_local_only_demo_execution_boundary_candidate_accepted = true",
        "safe_local_only_demo_execution_boundary_candidate_id = safe_local_only_demo_execution_boundary_candidate_v06304",
        "safe_local_only_demo_execution_boundary_target_mode_candidate = localhost_only",
        "safe_local_only_demo_execution_boundary_loopback_targets_candidate_accepted = true",
        "safe_local_only_demo_execution_boundary_external_targets_candidate_blocked_accepted = true",
        "safe_local_only_demo_execution_boundary_preflight_requirements_candidate_accepted = true",
        "safe_local_only_demo_execution_boundary_fail_closed_conditions_candidate_accepted = true",
        "safe_local_only_demo_execution_boundary_defined = false",
        "safe_local_only_demo_execution_boundary_applied = false",
        "safe_local_only_runnable_demo_path_created = false",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.305 - Safe Local-Only Demo Execution Boundary Candidate Review and Decision",
        "Accepted the v0.6.304 Safe Local-Only Demo Execution Boundary Candidate.",
        "safe_local_only_demo_execution_boundary_candidate_review_completed = true",
        "safe_local_only_demo_execution_boundary_candidate_accepted = true",
        "safe_local_only_demo_execution_boundary_candidate_id = safe_local_only_demo_execution_boundary_candidate_v06304",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary",
        "safe_local_only_demo_execution_boundary_applied = false",
        "safe_local_only_runnable_demo_path_created = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.305",
        "v0.6.306 Safe Local-Only Demo Execution Boundary",
        "no safe local-only demo execution boundary applied",
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

def test_v06305_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06305_safe_local_only_demo_execution_boundary_candidate_review_and_decision.py"])

def main() -> None:
    test_v06305_doc_tokens()
    test_v06305_adr_tokens()
    test_v06305_issue_tokens()
    test_v06305_index_tokens()
    test_v06305_registered_in_run_all()
    print("v0.6.305 safe local-only demo execution boundary candidate review and decision checks passed")

if __name__ == "__main__":
    main()
