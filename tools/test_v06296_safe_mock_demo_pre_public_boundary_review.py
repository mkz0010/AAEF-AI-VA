from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/371-v06296-safe-mock-demo-pre-public-boundary-review.md"
ADR = ROOT / "planning/decisions/ADR-0371-add-v06296-safe-mock-demo-pre-public-boundary-review.md"
ISSUE = ROOT / "planning/issues/0371-add-v06296-safe-mock-demo-pre-public-boundary-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_mock_demo_pre_public_boundary_review_applied = true', 'safe_mock_demo_pre_public_boundary_review_completed = true', 'safe_mock_demo_pre_public_boundary_review_id = safe_mock_demo_pre_public_boundary_review_v06296', 'safe_mock_demo_pre_public_boundary_review_status = completed_review_pending_decision', 'safe_mock_demo_pre_public_boundary_review_scope = documentation_only_pre_public_boundary_review_for_safe_mock_demo_path', 'reviewed_safe_mock_demo_pre_public_boundary_review_candidate_id = safe_mock_demo_pre_public_boundary_review_candidate_v06294', 'reviewed_safe_mock_demo_pre_public_boundary_review_candidate_review_completed = true', 'reviewed_safe_mock_demo_pre_public_boundary_review_candidate_accepted = true', 'safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision_completed = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'safe_mock_demo_pre_public_required_checks_reviewed = true', 'safe_mock_demo_pre_public_public_wording_checks_reviewed = true', 'safe_mock_demo_pre_public_private_artifact_checks_reviewed = true', 'safe_mock_demo_pre_public_demo_command_checks_reviewed = true', 'safe_mock_demo_pre_public_claim_boundary_checks_reviewed = true', 'safe_mock_demo_pre_public_release_blockers_reviewed = true', 'safe_mock_demo_pre_public_boundary_review_findings_recorded = true', 'safe_mock_demo_pre_public_boundary_review_release_blockers_remain = true', 'safe_mock_demo_pre_public_boundary_review_requires_decision = true', 'safe_mock_demo_pre_public_boundary_review_accepted = false', 'safe_mock_demo_pre_public_boundary_review_and_decision_created = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'safe_mock_demo_public_positioning_approved_for_publication = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_and_decision', 'safe_mock_demo_pre_public_boundary_review_and_decision_recommended = true', 'safe_mock_demo_pre_public_boundary_review_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_mock_demo_pre_public_boundary_review', 'safe_mock_demo_pre_public_boundary_review_v06296', 'safe_mock_demo_pre_public_boundary_review_and_decision', 'safe_mock_demo_pre_public_boundary_review_candidate_v06294', 'safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision', 'safe_mock_demo_initial_path', 'safe mock demo', 'safe mock demo path hardening', 'safe mock demo pre-public boundary review', 'safe mock demo public artifact promotion', 'safe mock demo public positioning', 'safe mock demo private artifact boundary', 'safe mock demo demo command boundary', 'safe mock demo claim boundary checks', 'safe mock demo release blockers', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'pre-public boundary review is not publication approval', 'pre-public boundary review is not public artifact promotion', 'pre-public boundary review is not runtime demo readiness', 'pre-public boundary review is not scanner readiness', 'pre-public boundary review is not production readiness', 'No private generated outputs are moved public in v0.6.296.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.296 Safe Mock Demo Pre-Public Boundary Review', 'Previous checkpoint: v0.6.295 Safe Mock Demo Pre-Public Boundary Review Candidate Review and Decision', 'Review result: pre-public boundary review completed pending decision', 'Application status: review only; no review acceptance, public artifact promotion, publication approval, runtime readiness, scanner readiness, or gateway behavior changed', 'safe mock demo pre-public required checks are reviewed', 'safe mock demo pre-public public wording checks are reviewed', 'safe mock demo pre-public private artifact checks are reviewed', 'safe mock demo pre-public demo command checks are reviewed', 'safe mock demo pre-public claim boundary checks are reviewed', 'safe mock demo pre-public release blockers are reviewed', 'safe mock demo pre-public boundary review findings are recorded', 'safe mock demo pre-public boundary review requires decision', 'pre-public boundary review is not publication approval', 'pre-public boundary review is not public artifact promotion', 'pre-public boundary review is not runtime demo readiness', 'pre-public boundary review is not scanner readiness', 'pre-public boundary review is not production readiness', 'recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_and_decision', 'safe_mock_demo_pre_public_boundary_review_and_decision_recommended = true', 'safe_mock_demo_pre_public_boundary_review_accepted = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'publication_approval = false', 'local_only_demo_execution_boundary_candidate_created = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.297 Safe Mock Demo Pre-Public Boundary Review and Decision']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06296_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06296_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0371",
        "Status: reviewed pending decision",
        "Apply the safe mock demo pre-public boundary review and leave acceptance to a later decision checkpoint.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06296_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0371 - Add v0.6.296 Safe Mock Demo Pre-Public Boundary Review",
        "Status: completed by v0.6.296",
        "safe_mock_demo_pre_public_boundary_review_applied = true",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_and_decision",
        "Proceed to v0.6.297 Safe Mock Demo Pre-Public Boundary Review and Decision",
    ])

def test_v06296_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.296 Safe Mock Demo Pre-Public Boundary Review",
        "safe_mock_demo_pre_public_boundary_review_applied = true",
        "safe_mock_demo_pre_public_boundary_review_completed = true",
        "safe_mock_demo_pre_public_boundary_review_id = safe_mock_demo_pre_public_boundary_review_v06296",
        "safe_mock_demo_pre_public_required_checks_reviewed = true",
        "safe_mock_demo_pre_public_public_wording_checks_reviewed = true",
        "safe_mock_demo_pre_public_private_artifact_checks_reviewed = true",
        "safe_mock_demo_pre_public_demo_command_checks_reviewed = true",
        "safe_mock_demo_pre_public_claim_boundary_checks_reviewed = true",
        "safe_mock_demo_pre_public_boundary_review_accepted = false",
        "safe_mock_demo_public_artifact_promotion_created = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_and_decision",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.296 - Safe Mock Demo Pre-Public Boundary Review",
        "Applied the Safe Mock Demo Pre-Public Boundary Review",
        "safe_mock_demo_pre_public_boundary_review_applied = true",
        "safe_mock_demo_pre_public_boundary_review_completed = true",
        "safe_mock_demo_pre_public_boundary_review_id = safe_mock_demo_pre_public_boundary_review_v06296",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_and_decision",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.296",
        "v0.6.297 Safe Mock Demo Pre-Public Boundary Review and Decision",
        "no pre-public boundary review accepted",
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

def test_v06296_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06296_safe_mock_demo_pre_public_boundary_review.py"])

def main() -> None:
    test_v06296_doc_tokens()
    test_v06296_adr_tokens()
    test_v06296_issue_tokens()
    test_v06296_index_tokens()
    test_v06296_registered_in_run_all()
    print("v0.6.296 safe mock demo pre-public boundary review checks passed")

if __name__ == "__main__":
    main()
