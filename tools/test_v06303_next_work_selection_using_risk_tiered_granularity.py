from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/378-v06303-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0378-add-v06303-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0378-add-v06303-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['next_work_selection_completed = true', 'next_work_selection_id = next_work_selection_v06303', 'selected_work_item = safe_local_only_demo_execution_boundary_candidate', 'selected_work_item_status = selected_for_safe_local_only_demo_execution_boundary_candidate', 'selected_work_item_reason = public_artifact_accepted_and_runtime_execution_still_blocked', 'safe_local_only_demo_execution_boundary_candidate_selected = true', 'safe_local_only_demo_execution_boundary_candidate_recommended = true', 'safe_local_only_demo_execution_boundary_candidate_created = false', 'safe_local_only_demo_execution_boundary_candidate_review_completed = false', 'safe_local_only_demo_execution_boundary_candidate_accepted = false', 'safe_local_only_demo_execution_boundary_defined = false', 'safe_local_only_demo_execution_boundary_applied = false', 'safe_local_only_demo_execution_boundary_accepted = false', 'safe_local_only_runnable_demo_path_selected = false', 'safe_local_only_runnable_demo_path_created = false', 'safe_local_only_runnable_demo_ready = false', 'safe_mock_demo_public_artifact_promotion_review_completed = true', 'safe_mock_demo_public_artifact_promotion_accepted = true', 'safe_mock_demo_public_artifact_promotion_id = safe_mock_demo_public_artifact_promotion_v06301', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact_reviewed = true', 'safe_mock_demo_public_artifact_accepted = true', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'public_artifact_promotion_selected = false', 'safe_mock_demo_public_artifact_promotion_reopened = false', 'safe_mock_demo_public_positioning_approved_for_publication = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_local_only_demo_execution_boundary_candidate', 'next_work_selection_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['next_work_selection_using_risk_tiered_granularity', 'next_work_selection_v06303', 'safe_local_only_demo_execution_boundary_candidate', 'safe_local_only_demo_execution_boundary', 'safe_local_only_runnable_demo_path', 'safe_mock_demo_public_artifact_promotion_review_and_decision', 'safe_mock_demo_public_artifact_promotion_v06301', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact', 'safe_mock_demo_initial_path', 'safe mock demo', 'safe local-only demo execution boundary candidate', 'safe local-only demo execution boundary', 'safe local-only runnable demo path', 'localhost_only', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'safe local-only demo execution boundary candidate is not execution authorization', 'safe local-only demo execution boundary candidate is not runtime demo readiness', 'safe local-only demo execution boundary candidate is not scanner readiness', 'safe local-only demo execution boundary candidate is not production readiness', 'safe local-only demo execution boundary candidate is not external target authorization', 'No private generated outputs are moved public in v0.6.303.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.303 Next Work Selection Using Risk-Tiered Granularity', 'Previous checkpoint: v0.6.302 Safe Mock Demo Public Artifact Promotion Review and Decision', 'Selection result: `safe_local_only_demo_execution_boundary_candidate`', 'Application status: selection only; no safe local-only boundary candidate created, runtime readiness, scanner readiness, execution authorization, or gateway behavior changed', 'public artifact has been accepted but runtime execution remains blocked', 'selected_work_item = safe_local_only_demo_execution_boundary_candidate', 'safe_local_only_demo_execution_boundary_candidate_selected = true', 'safe_local_only_demo_execution_boundary_candidate_created = false', 'safe_local_only_demo_execution_boundary_defined = false', 'safe_local_only_runnable_demo_path_created = false', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'safe local-only demo execution boundary candidate is not execution authorization', 'safe local-only demo execution boundary candidate is not runtime demo readiness', 'safe local-only demo execution boundary candidate is not scanner readiness', 'safe local-only demo execution boundary candidate is not production readiness', 'safe local-only demo execution boundary candidate is not external target authorization', 'recommended_next_work_item = safe_local_only_demo_execution_boundary_candidate', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.304 Safe Local-Only Demo Execution Boundary Candidate']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06303_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06303_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0378",
        "Status: accepted",
        "Select `safe_local_only_demo_execution_boundary_candidate` as the next work item.",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06303_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0378 - Add v0.6.303 Next Work Selection Using Risk-Tiered Granularity",
        "Status: completed by v0.6.303",
        "selected_work_item = safe_local_only_demo_execution_boundary_candidate",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary_candidate",
        "Proceed to v0.6.304 Safe Local-Only Demo Execution Boundary Candidate",
    ])

def test_v06303_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.303 Next Work Selection Using Risk-Tiered Granularity",
        "next_work_selection_completed = true",
        "next_work_selection_id = next_work_selection_v06303",
        "selected_work_item = safe_local_only_demo_execution_boundary_candidate",
        "safe_local_only_demo_execution_boundary_candidate_selected = true",
        "safe_local_only_demo_execution_boundary_candidate_created = false",
        "safe_local_only_demo_execution_boundary_defined = false",
        "safe_local_only_runnable_demo_path_created = false",
        "publication_approval_selected = false",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary_candidate",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.303 - Next Work Selection Using Risk-Tiered Granularity",
        "Selected `safe_local_only_demo_execution_boundary_candidate` as the next work item.",
        "next_work_selection_completed = true",
        "next_work_selection_id = next_work_selection_v06303",
        "safe_local_only_demo_execution_boundary_candidate_selected = true",
        "recommended_next_work_item = safe_local_only_demo_execution_boundary_candidate",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.303",
        "v0.6.304 Safe Local-Only Demo Execution Boundary Candidate",
        "no safe local-only demo execution boundary candidate created yet",
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

def test_v06303_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06303_next_work_selection_using_risk_tiered_granularity.py"])

def main() -> None:
    test_v06303_doc_tokens()
    test_v06303_adr_tokens()
    test_v06303_issue_tokens()
    test_v06303_index_tokens()
    test_v06303_registered_in_run_all()
    print("v0.6.303 next work selection checks passed")

if __name__ == "__main__":
    main()
