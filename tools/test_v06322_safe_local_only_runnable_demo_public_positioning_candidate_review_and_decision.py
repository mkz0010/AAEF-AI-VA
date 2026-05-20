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
DOC = ROOT / "docs/397-v06322-safe-local-only-runnable-demo-public-positioning-candidate-review-and-decision.md"
ADR = ROOT / "planning/decisions/ADR-0397-add-v06322-safe-local-only-runnable-demo-public-positioning-candidate-review-and-decision.md"
ISSUE = ROOT / "planning/issues/0397-add-v06322-safe-local-only-runnable-demo-public-positioning-candidate-review-and-decision.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_candidate_accepted = true', 'safe_local_only_runnable_demo_public_positioning_candidate_id = safe_local_only_runnable_demo_public_positioning_candidate_v06321', 'safe_local_only_runnable_demo_public_positioning_candidate_review_result = accepted_as_public_wording_candidate_not_public_ready', 'safe_local_only_runnable_demo_public_positioning_candidate_status = accepted_not_integrated_public_ready_false', 'reviewed_safe_local_only_runnable_demo_public_positioning_candidate_created = true', 'reviewed_safe_local_only_runnable_demo_public_positioning_candidate_scope = public_wording_candidate_only', 'safe_local_only_runnable_demo_public_positioning_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_review_id = safe_local_only_runnable_demo_public_positioning_review_v06320', 'safe_local_only_runnable_demo_public_positioning_review_result = candidate_needed_not_public_ready', 'safe_local_only_runnable_demo_public_positioning_review_status = completed_candidate_recommended', 'safe_local_only_runnable_demo_public_positioning_scope = public_wording_review_only', 'safe_local_only_runnable_demo_reviewer_runbook_review_completed = true', 'safe_local_only_runnable_demo_reviewer_runbook_accepted = true', 'safe_local_only_runnable_demo_reviewer_runbook_id = safe_local_only_runnable_demo_reviewer_runbook_v06318', 'safe_local_only_runnable_demo_reviewer_runbook_review_result = accepted_as_local_reviewer_walkthrough_runbook', 'safe_local_only_runnable_demo_reviewer_runbook_status = accepted_not_public_demo_ready', 'safe_local_only_runnable_demo_readiness_review_completed = true', 'safe_local_only_runnable_demo_readiness_review_id = safe_local_only_runnable_demo_readiness_review_v06317', 'safe_local_only_runnable_demo_readiness_review_result = ready_as_mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_ready_status = ready_for_local_reviewer_walkthrough', 'safe_local_only_runnable_demo_public_ready = false', 'safe_local_only_runnable_demo_publication_ready = false', 'safe_local_only_runnable_demo_external_poc_ready = false', 'safe_local_only_runnable_demo_customer_demo_ready = false', 'safe_local_only_runnable_demo_path_creation_review_completed = true', 'safe_local_only_runnable_demo_path_creation_accepted = true', 'safe_local_only_runnable_demo_path_creation_id = safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path_created = true', 'safe_local_only_runnable_demo_path_id = safe_local_only_runnable_demo_path_v06310', 'safe_local_only_runnable_demo_path_status = accepted_created_not_runtime_applied', 'safe_local_only_runnable_demo_path_applied = false', 'public_positioning_candidate_tagline_accepted = true', 'public_positioning_candidate_short_description_accepted = true', 'public_positioning_candidate_boundary_notice_accepted = true', 'public_positioning_candidate_demo_scope_statement_accepted = true', 'public_positioning_candidate_allowed_outcomes_statement_accepted = true', 'public_positioning_candidate_evidence_statement_accepted = true', 'public_positioning_candidate_local_only_statement_accepted = true', 'public_positioning_candidate_no_public_ready_statement_accepted = true', 'public_positioning_candidate_no_customer_demo_ready_statement_accepted = true', 'public_positioning_candidate_no_runtime_demo_ready_statement_accepted = true', 'public_positioning_candidate_no_scanner_ready_statement_accepted = true', 'public_positioning_candidate_no_execution_authorization_statement_accepted = true', 'public_positioning_candidate_no_external_target_authorization_statement_accepted = true', 'public_positioning_candidate_private_artifact_statement_accepted = true', 'public_positioning_candidate_allowed_phrase_local_reviewer_walkthrough = true', 'public_positioning_candidate_allowed_phrase_mock_first_localhost_only_demo = true', 'public_positioning_candidate_allowed_phrase_three_gate_outcomes = true', 'public_positioning_candidate_allowed_phrase_evidence_linked_review = true', 'public_positioning_candidate_allowed_phrase_execution_boundary_demo = true', 'public_positioning_candidate_allowed_phrase_ai_requests_gate_decides = true', 'public_positioning_candidate_allowed_phrase_no_live_tool_execution = true', 'public_positioning_candidate_allowed_phrase_no_external_target_authorization = true', 'public_positioning_candidate_prohibited_claim_category_autonomous_vulnerability_scanning = true', 'public_positioning_candidate_prohibited_claim_category_ai_pentest_agent_framing = true', 'public_positioning_candidate_prohibited_claim_category_scanner_production_readiness = true', 'public_positioning_candidate_prohibited_claim_category_runtime_enforcement_for_scanner = true', 'public_positioning_candidate_prohibited_claim_category_external_target_readiness = true', 'public_positioning_candidate_prohibited_claim_category_customer_poc_readiness = true', 'public_positioning_candidate_prohibited_claim_category_certification_or_audit_readiness = true', 'public_positioning_candidate_prohibited_claim_category_compliance_sufficiency = true', 'public_positioning_candidate_prohibited_claim_category_diagnostic_completeness = true', 'public_positioning_candidate_preserves_local_only_scope = true', 'public_positioning_candidate_preserves_mock_first_scope = true', 'public_positioning_candidate_preserves_public_ready_false = true', 'public_positioning_candidate_preserves_publication_approval_false = true', 'public_positioning_candidate_preserves_customer_demo_ready_false = true', 'public_positioning_candidate_integration_plan_needed = true', 'safe_local_only_demo_execution_boundary_review_completed = true', 'safe_local_only_demo_execution_boundary_accepted = true', 'safe_local_only_demo_execution_boundary_id = safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary_status = accepted_not_runtime_applied', 'safe_local_only_demo_execution_boundary_target_mode = localhost_only', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_recommended = true', 'safe_local_only_runnable_demo_public_positioning_candidate_review_and_decision_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_local_only_runnable_demo_public_positioning_candidate_review_and_decision', 'safe_local_only_runnable_demo_public_positioning_candidate_review_completed', 'safe_local_only_runnable_demo_public_positioning_candidate_accepted', 'safe_local_only_runnable_demo_public_positioning_candidate_v06321', 'safe_local_only_runnable_demo_public_positioning_candidate', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate', 'safe_local_only_runnable_demo_public_positioning_review_v06320', 'safe_local_only_runnable_demo_reviewer_runbook_v06318', 'safe_local_only_runnable_demo_reviewer_runbook', 'safe_local_only_runnable_demo_ready', 'mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_path_creation_v06315', 'safe_local_only_runnable_demo_path', 'safe_local_only_runnable_demo_path_v06310', 'safe_local_only_demo_execution_boundary_v06306', 'safe_local_only_demo_execution_boundary', 'localhost_only', 'loopback-only target boundary', 'mock_first_no_live_scanner_default', 'external target authorization remains false', 'safe_mock_demo_public_artifact', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe mock demo', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'AI requests; gates decide', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only runnable demo public positioning candidate review is not publication approval', 'safe local-only runnable demo public positioning candidate review is not public demo readiness', 'safe local-only runnable demo public positioning candidate review is not customer demo readiness', 'safe local-only runnable demo public positioning candidate review is not execution authorization', 'safe local-only runnable demo public positioning candidate review is not runtime demo readiness', 'safe local-only runnable demo public positioning candidate review is not scanner readiness', 'safe local-only runnable demo public positioning candidate review is not production readiness', 'safe local-only runnable demo public positioning candidate review is not external target authorization', 'No private generated outputs are moved public in v0.6.322.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.322 Safe Local-Only Runnable Demo Public Positioning Candidate Review and Decision', 'Previous checkpoint: v0.6.321 Safe Local-Only Runnable Demo Public Positioning Candidate', 'Reviewed candidate: `safe_local_only_runnable_demo_public_positioning_candidate_v06321`', 'Decision result: accepted as public wording candidate, not public ready', 'Application status: review only; no publication approval, public demo readiness, runtime readiness, scanner readiness, execution authorization, or gateway behavior changed', 'safe local-only runnable demo public positioning candidate tagline is accepted', 'safe local-only runnable demo public positioning candidate boundary notice is accepted', 'safe local-only runnable demo public positioning candidate local-only scope statement is accepted', 'safe local-only runnable demo public positioning candidate private artifact statement is accepted', 'safe local-only runnable demo public positioning candidate review is not publication approval', 'safe local-only runnable demo public positioning candidate review is not public demo readiness', 'safe local-only runnable demo public positioning candidate review is not customer demo readiness', 'safe local-only runnable demo public positioning candidate review is not execution authorization', 'safe local-only runnable demo public positioning candidate review is not runtime demo readiness', 'safe local-only runnable demo public positioning candidate review is not scanner readiness', 'safe local-only runnable demo public positioning candidate review is not production readiness', 'safe local-only runnable demo public positioning candidate review is not external target authorization', 'recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate', 'safe_local_only_runnable_demo_public_positioning_integration_plan_candidate_recommended = true', 'safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.323 Safe Local-Only Runnable Demo Public Positioning Integration Plan Candidate']

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

def test_v06322_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06322_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0397",
        "Status: accepted",
        "Accept the v0.6.321 candidate as the public wording candidate for later integration planning.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06322_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0397 - Add v0.6.322 Safe Local-Only Runnable Demo Public Positioning Candidate Review and Decision",
        "Status: completed by v0.6.322",
        "safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate",
        "Proceed to v0.6.323 Safe Local-Only Runnable Demo Public Positioning Integration Plan Candidate",
    ])

def test_v06322_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.322 Safe Local-Only Runnable Demo Public Positioning Candidate Review and Decision",
        "safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true",
        "safe_local_only_runnable_demo_public_positioning_candidate_accepted = true",
        "safe_local_only_runnable_demo_public_positioning_candidate_id = safe_local_only_runnable_demo_public_positioning_candidate_v06321",
        "safe_local_only_runnable_demo_public_positioning_candidate_review_result = accepted_as_public_wording_candidate_not_public_ready",
        "safe_local_only_runnable_demo_public_positioning_candidate_status = accepted_not_integrated_public_ready_false",
        "public_positioning_candidate_tagline_accepted = true",
        "public_positioning_candidate_short_description_accepted = true",
        "public_positioning_candidate_boundary_notice_accepted = true",
        "public_positioning_candidate_local_only_statement_accepted = true",
        "public_positioning_candidate_private_artifact_statement_accepted = true",
        "public_positioning_candidate_integration_plan_needed = true",
        "safe_local_only_runnable_demo_ready = true",
        "safe_local_only_runnable_demo_public_ready = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.322 - Safe Local-Only Runnable Demo Public Positioning Candidate Review and Decision",
        "Accepted the v0.6.321 public positioning candidate for the safe local-only runnable demo.",
        "safe_local_only_runnable_demo_public_positioning_candidate_review_completed = true",
        "safe_local_only_runnable_demo_public_positioning_candidate_accepted = true",
        "safe_local_only_runnable_demo_public_positioning_candidate_id = safe_local_only_runnable_demo_public_positioning_candidate_v06321",
        "public_positioning_candidate_integration_plan_needed = true",
        "safe_local_only_runnable_demo_public_ready = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = safe_local_only_runnable_demo_public_positioning_integration_plan_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.322",
        "v0.6.323 Safe Local-Only Runnable Demo Public Positioning Integration Plan Candidate",
        "no public positioning integration plan candidate created",
        "no README front page rewrite",
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

def test_v06322_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06322_safe_local_only_runnable_demo_public_positioning_candidate_review_and_decision.py"])

def test_v06322_avoids_raw_forbidden_public_positioning_claims() -> None:
    scanned_paths = [DOC, ADR, ISSUE, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
        "AI pentest agent",
        "production-ready scanner",
        "runtime-enforced scanner",
        "external-target-ready demo",
        "customer-ready PoC",
        "certified / audit-ready system",
        "compliance-sufficient control",
        "diagnostically complete scanner",
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06322_doc_tokens()
    test_v06322_adr_tokens()
    test_v06322_issue_tokens()
    test_v06322_index_tokens()
    test_v06322_registered_in_run_all()
    test_v06322_avoids_raw_forbidden_public_positioning_claims()
    print("v0.6.322 safe local-only runnable demo public positioning candidate review and decision checks passed")

if __name__ == "__main__":
    main()
