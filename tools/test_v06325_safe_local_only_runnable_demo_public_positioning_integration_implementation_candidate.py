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
DOC = ROOT / "docs/400-v06325-safe-local-only-runnable-demo-public-positioning-integration-implementation-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0400-add-v06325-safe-local-only-runnable-demo-public-positioning-integration-implementation-candidate.md"
ISSUE = ROOT / "planning/issues/0400-add-v06325-safe-local-only-runnable-demo-public-positioning-integration-implementation-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_created = true', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_id = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_v06325', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_status = candidate_not_reviewed', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_scope = bounded_readme_status_and_boundary_wording_candidate_only', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_completed = false', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_accepted = false', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_accepted = true', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_id = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_v06323', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_review_result = accepted_as_integration_plan_candidate_not_applied', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_status = accepted_not_implemented_public_ready_false', 'safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_candidate_accepted = true', 'safe_local_only_runnable_demo_public_positioning_candidate_id = safe_local_only_runnable_demo_public_positioning_candidate_v06321', 'safe_local_only_runnable_demo_public_positioning_candidate_review_result = accepted_as_public_wording_candidate_not_public_ready', 'safe_local_only_runnable_demo_public_positioning_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_review_id = safe_local_only_runnable_demo_public_positioning_review_v06320', 'safe_local_only_runnable_demo_reviewer_runbook_review_completed = true', 'safe_local_only_runnable_demo_reviewer_runbook_accepted = true', 'safe_local_only_runnable_demo_reviewer_runbook_id = safe_local_only_runnable_demo_reviewer_runbook_v06318', 'safe_local_only_runnable_demo_readiness_review_completed = true', 'safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'safe_local_only_runnable_demo_publication_ready = false', 'safe_local_only_runnable_demo_external_poc_ready = false', 'safe_local_only_runnable_demo_customer_demo_ready = false', 'integration_implementation_candidate_readme_current_status_wording_added = true', 'integration_implementation_candidate_readme_safe_demo_boundary_wording_added = true', 'integration_implementation_candidate_public_artifact_reference_wording_added = true', 'integration_implementation_candidate_roadmap_boundary_wording_added = true', 'integration_implementation_candidate_changelog_summary_added = true', 'integration_implementation_candidate_front_page_rewrite = false', 'integration_implementation_candidate_repository_metadata_change = false', 'integration_implementation_candidate_public_release_notes_change = false', 'integration_implementation_candidate_public_announcement_change = false', 'integration_implementation_candidate_customer_material_change = false', 'integration_implementation_candidate_runtime_behavior_change = false', 'integration_implementation_candidate_gateway_behavior_change = false', 'integration_implementation_candidate_scanner_behavior_change = false', 'integration_implementation_candidate_private_artifact_publication = false', 'integration_implementation_candidate_uses_accepted_candidate_wording = true', 'integration_implementation_candidate_preserves_local_only_scope = true', 'integration_implementation_candidate_preserves_mock_first_scope = true', 'integration_implementation_candidate_preserves_private_artifacts_private = true', 'integration_implementation_candidate_preserves_public_ready_false = true', 'integration_implementation_candidate_preserves_publication_approval_false = true', 'integration_implementation_candidate_preserves_customer_demo_ready_false = true', 'integration_implementation_candidate_preserves_runtime_demo_ready_false = true', 'integration_implementation_candidate_preserves_scanner_readiness_false = true', 'integration_implementation_candidate_preserves_execution_authorized_false = true', 'integration_implementation_candidate_preserves_external_target_authorization_false = true', 'integration_implementation_candidate_avoids_autonomous_vulnerability_scanning_claim_category = true', 'integration_implementation_candidate_avoids_ai_pentest_agent_framing_category = true', 'integration_implementation_candidate_avoids_scanner_production_readiness_claim_category = true', 'integration_implementation_candidate_avoids_runtime_enforcement_for_scanner_claim_category = true', 'integration_implementation_candidate_avoids_external_target_readiness_claim_category = true', 'integration_implementation_candidate_avoids_customer_poc_readiness_claim_category = true', 'integration_implementation_candidate_avoids_certification_or_audit_readiness_claim_category = true', 'integration_implementation_candidate_avoids_compliance_sufficiency_claim_category = true', 'integration_implementation_candidate_avoids_diagnostic_completeness_claim_category = true', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision_recommended = true', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_v06325', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_v06323', 'safe_local_only_runnable_demo_public_positioning_candidate_v06321', 'safe_local_only_runnable_demo_reviewer_runbook_v06318', 'safe_local_only_runnable_demo_ready', 'mock_first_localhost_only_reviewer_demo', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'private-not-in-git', 'AI requests; gates decide', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo public positioning integration implementation candidate is not publication approval', 'safe local-only runnable demo public positioning integration implementation candidate is not public demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not customer demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not execution authorization', 'safe local-only runnable demo public positioning integration implementation candidate is not runtime demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not scanner readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not production readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not external target authorization', 'No private generated outputs are moved public in v0.6.325.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.325 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate', 'Previous checkpoint: v0.6.324 Safe Local-Only Runnable Demo Public Positioning Integration Plan Candidate Review and Decision', 'Candidate result: bounded public positioning integration implementation candidate created, not accepted', 'Application status: implementation candidate only; no README front page rewrite, publication approval, public demo readiness, runtime readiness, scanner readiness, execution authorization, or gateway behavior changed', 'safe local-only runnable demo public positioning integration implementation candidate README status wording is added', 'safe local-only runnable demo public positioning integration implementation candidate README boundary wording is added', 'safe local-only runnable demo public positioning integration implementation candidate artifact reference wording is added', 'safe local-only runnable demo public positioning integration implementation candidate is not publication approval', 'safe local-only runnable demo public positioning integration implementation candidate is not public demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not customer demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not execution authorization', 'safe local-only runnable demo public positioning integration implementation candidate is not runtime demo readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not scanner readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not production readiness', 'safe local-only runnable demo public positioning integration implementation candidate is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision_recommended = true', 'safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_completed = false', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.326 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate Review and Decision']

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

def test_v06325_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06325_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0400",
        "Status: proposed candidate",
        "Create a bounded implementation candidate for the accepted integration plan.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06325_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0400 - Add v0.6.325 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate",
        "Status: completed by v0.6.325",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_created = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision",
        "Proceed to v0.6.326 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate Review and Decision",
    ])

def test_v06325_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.325 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate",
        "Safe local-only reviewer walkthrough: AAEF-AI-VA has a mock-first localhost-only reviewer path",
        "The reviewer-visible outcomes are allowed, blocked, and human approval required.",
        "Generated reviewer artifacts remain under private-not-in-git",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_created = true",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_id = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_v06325",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_status = candidate_not_reviewed",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_completed = false",
        "integration_implementation_candidate_readme_current_status_wording_added = true",
        "integration_implementation_candidate_readme_safe_demo_boundary_wording_added = true",
        "integration_implementation_candidate_public_artifact_reference_wording_added = true",
        "integration_implementation_candidate_front_page_rewrite = false",
        "integration_implementation_candidate_repository_metadata_change = false",
        "safe_local_only_runnable_demo_ready = true",
        "safe_local_only_runnable_demo_public_ready = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.325 - Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate",
        "Created a bounded implementation candidate for the accepted public positioning integration plan.",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_created = true",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_id = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_v06325",
        "safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_status = candidate_not_reviewed",
        "safe_local_only_runnable_demo_public_ready = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate_review_and_decision",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.325",
        "v0.6.326 Safe Local-Only Runnable Demo Public Positioning Integration Implementation Candidate Review and Decision",
        "no public positioning integration implementation candidate review completed",
        "no README front page rewrite",
        "no repository metadata change",
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

def test_v06325_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06325_safe_local_only_runnable_demo_public_positioning_integration_implementation_candidate.py"])

def test_v06325_avoids_raw_forbidden_public_positioning_claims() -> None:
    scanned_paths = [DOC, ADR, ISSUE, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
        "AI pentest agent",
        "production readiness scanner",
        "runtime-enforced scanner",
        "external-target-ready demo",
        "customer-ready PoC",
        "certification / audit-ready system",
        "compliance-sufficient control",
        "diagnostic-completeness claim scanner",
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06325_doc_tokens()
    test_v06325_adr_tokens()
    test_v06325_issue_tokens()
    test_v06325_index_tokens()
    test_v06325_registered_in_run_all()
    test_v06325_avoids_raw_forbidden_public_positioning_claims()
    print("v0.6.325 safe local-only runnable demo public positioning integration implementation candidate checks passed")

if __name__ == "__main__":
    main()
