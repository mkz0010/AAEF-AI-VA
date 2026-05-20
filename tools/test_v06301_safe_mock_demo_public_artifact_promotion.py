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
DOC = ROOT / "docs/376-v06301-safe-mock-demo-public-artifact-promotion.md"
ADR = ROOT / "planning/decisions/ADR-0376-add-v06301-safe-mock-demo-public-artifact-promotion.md"
ISSUE = ROOT / "planning/issues/0376-add-v06301-safe-mock-demo-public-artifact-promotion.md"
ARTIFACT = ROOT / "docs/public-artifacts/safe-mock-demo-public-artifact.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_DECISION_TOKENS = ['safe_mock_demo_public_artifact_promotion_applied = true', 'safe_mock_demo_public_artifact_promotion_created = true', 'safe_mock_demo_public_artifact_promotion_id = safe_mock_demo_public_artifact_promotion_v06301', 'safe_mock_demo_public_artifact_promotion_status = public_artifact_created_not_publication_approved', 'safe_mock_demo_public_artifact_promotion_scope = documentation_only_safe_mock_demo_public_artifact', 'safe_mock_demo_public_artifact_path = docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact_created = true', 'safe_mock_demo_public_artifact_contains_private_generated_outputs = false', 'safe_mock_demo_public_artifact_contains_live_scanner_outputs = false', 'safe_mock_demo_public_artifact_contains_customer_or_target_data = false', 'safe_mock_demo_public_artifact_contains_runtime_execution_authorization = false', 'safe_mock_demo_public_artifact_command_example_included = true', 'safe_mock_demo_public_artifact_expected_statuses_included = true', 'safe_mock_demo_public_artifact_boundary_wording_included = true', 'safe_mock_demo_public_artifact_private_artifact_exclusion_included = true', 'safe_mock_demo_public_artifact_claim_boundaries_included = true', 'safe_mock_demo_public_artifact_promotion_candidate_review_completed = true', 'safe_mock_demo_public_artifact_promotion_candidate_accepted = true', 'safe_mock_demo_public_artifact_promotion_candidate_id = safe_mock_demo_public_artifact_promotion_candidate_v06299', 'safe_mock_demo_public_artifact_promotion_candidate_review_result = accepted_for_future_public_artifact_promotion', 'reviewed_safe_mock_demo_public_artifact_promotion_candidate_review_and_decision_id = safe_mock_demo_public_artifact_promotion_candidate_review_and_decision_v06300', 'safe_mock_demo_status = runnable_private_artifact_demo_available', 'safe_mock_demo_is_live_scanner_execution = false', 'safe_mock_demo_private_artifacts_remain_private = true', 'safe_mock_demo_public_artifact_promotion_review_completed = false', 'safe_mock_demo_public_artifact_promotion_accepted = false', 'safe_mock_demo_public_artifact_promotion_review_and_decision_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'safe_mock_demo_public_positioning_approved_for_publication = false', 'publication_approval_selected = false', 'publication_approval = false', 'public_announcement = deferred', 'private_generated_outputs_moved_public = false', 'local_only_demo_execution_boundary_candidate_selected = false', 'local_only_demo_execution_boundary_candidate_created = false', 'local_only_runnable_demo_path_selected = false', 'real_scanner_execution_path_selected = false', 'real_scanner_execution_status = blocked', 'runtime_demo_ready = false', 'runtime_demo_readiness_claim = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'runtime_readiness_status = not_detected_execution_blocked', 'target_lab_gate_status = target_defined_execution_blocked', 'runtime_destination_binding_status = bound_execution_blocked', 'bounded_execution_transition_status = candidate_recorded_execution_blocked', 'preflight_satisfied = false', 'concrete_checks_implemented = false', 'live_evidence_records_generated = false', 'runtime_enforcement_implemented = false', 'recommended_next_work_item = safe_mock_demo_public_artifact_promotion_review_and_decision', 'safe_mock_demo_public_artifact_promotion_review_and_decision_recommended = true', 'safe_mock_demo_public_artifact_promotion_recommended = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'fixtures_created = false', 'record_candidate_artifacts_created = false', 'actual_records_created = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'certification_claim = false', 'legal_compliance_claim = false', 'audit_opinion_claim = false', 'diagnostic_completeness_claim = false', 'external_framework_equivalence_claim = false']
REQUIRED_SHARED_TOKENS = ['safe_mock_demo_public_artifact_promotion', 'safe_mock_demo_public_artifact_promotion_v06301', 'safe_mock_demo_public_artifact_promotion_review_and_decision', 'safe_mock_demo_public_artifact_promotion_candidate_review_and_decision_v06300', 'safe_mock_demo_public_artifact_promotion_candidate_v06299', 'docs/public-artifacts/safe-mock-demo-public-artifact.md', 'safe_mock_demo_public_artifact', 'safe_mock_demo_initial_path', 'safe mock demo', 'safe mock demo public artifact', 'safe mock demo public artifact promotion', 'safe mock demo public positioning', 'safe mock demo private artifact boundary', 'safe mock demo command example', 'safe mock demo expected statuses', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'local-only runnable demo', 'real scanner execution remains blocked', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'public artifact promotion is not publication approval', 'public artifact promotion is not public announcement', 'public artifact promotion is not runtime demo readiness', 'public artifact promotion is not scanner readiness', 'public artifact promotion is not production readiness', 'No private generated outputs are moved public in v0.6.301.', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false']
REQUIRED_DOC_TOKENS = ['v0.6.301 Safe Mock Demo Public Artifact Promotion', 'Previous checkpoint: v0.6.300 Safe Mock Demo Public Artifact Promotion Candidate Review and Decision', 'Promotion result: safe mock demo public artifact created', 'Application status: public artifact promotion only; no publication approval, public announcement, runtime readiness, scanner readiness, or gateway behavior changed', 'safe mock demo public artifact is created', 'safe mock demo public artifact command example is included', 'safe mock demo public artifact expected statuses are included', 'safe mock demo public artifact boundary wording is included', 'safe mock demo public artifact private artifact exclusion is included', 'safe mock demo public artifact claim boundaries are included', 'public artifact promotion is not publication approval', 'public artifact promotion is not public announcement', 'public artifact promotion is not runtime demo readiness', 'public artifact promotion is not scanner readiness', 'public artifact promotion is not production readiness', 'recommended_next_work_item = safe_mock_demo_public_artifact_promotion_review_and_decision', 'safe_mock_demo_public_artifact_promotion_review_and_decision_recommended = true', 'safe_mock_demo_public_artifact_promotion_review_completed = false', 'safe_mock_demo_public_artifact_promotion_accepted = false', 'publication_approval = false', 'public_announcement = deferred', 'local_only_demo_execution_boundary_candidate_created = false', 'runtime_demo_ready = false', 'execution_authorized = false', 'real_execution_permitted = false', 'verification report creation is deferred', 'implementation changes are deferred', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'v0.6.302 Safe Mock Demo Public Artifact Promotion Review and Decision']

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

def test_v06301_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_DOC_TOKENS + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06301_public_artifact_tokens() -> None:
    assert_tokens(ARTIFACT, [
        "Safe Mock Demo Public Artifact",
        "Status: promoted public artifact, not publication approval",
        "not a live scanner",
        "not runtime demo readiness",
        "not scanner readiness",
        "not execution authorization",
        "not real execution permission",
        "not publication approval",
        "py tools/run_tool_gateway_example.py all",
        "allowed-action: completed",
        "denied-action: blocked",
        "human-approval-required: requires_human_approval",
        "Generated outputs remain under `private-not-in-git`.",
        "No private generated outputs are moved public in v0.6.301.",
        "Model output is not authority.",
        "real scanner execution remains blocked",
        "execution authorized: False",
        "real execution permitted: False",
    ])

def test_v06301_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0376",
        "Status: promoted public artifact",
        "Create the documentation-only safe mock demo public artifact",
    ] + REQUIRED_DECISION_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06301_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0376 - Add v0.6.301 Safe Mock Demo Public Artifact Promotion",
        "Status: completed by v0.6.301",
        "safe_mock_demo_public_artifact_promotion_applied = true",
        "recommended_next_work_item = safe_mock_demo_public_artifact_promotion_review_and_decision",
        "Proceed to v0.6.302 Safe Mock Demo Public Artifact Promotion Review and Decision",
    ])

def test_v06301_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.301 Safe Mock Demo Public Artifact Promotion",
        "docs/public-artifacts/safe-mock-demo-public-artifact.md",
        "safe_mock_demo_public_artifact_promotion_applied = true",
        "safe_mock_demo_public_artifact_promotion_created = true",
        "safe_mock_demo_public_artifact_promotion_id = safe_mock_demo_public_artifact_promotion_v06301",
        "safe_mock_demo_public_artifact_created = true",
        "safe_mock_demo_public_artifact_contains_private_generated_outputs = false",
        "safe_mock_demo_public_artifact_contains_live_scanner_outputs = false",
        "safe_mock_demo_public_artifact_promotion_review_completed = false",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_mock_demo_public_artifact_promotion_review_and_decision",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.301 - Safe Mock Demo Public Artifact Promotion",
        "Created the documentation-only safe mock demo public artifact",
        "safe_mock_demo_public_artifact_promotion_applied = true",
        "safe_mock_demo_public_artifact_promotion_created = true",
        "safe_mock_demo_public_artifact_promotion_id = safe_mock_demo_public_artifact_promotion_v06301",
        "recommended_next_work_item = safe_mock_demo_public_artifact_promotion_review_and_decision",
        "publication_approval = false",
        "public_announcement = deferred",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.301",
        "v0.6.302 Safe Mock Demo Public Artifact Promotion Review and Decision",
        "no public artifact promotion accepted",
        "no publication approval",
        "no public announcement",
        "no runtime demo readiness",
        "no scanner readiness",
        "no execution authorization",
        "no real execution permitted",
        "no local-only demo execution boundary candidate",
        "no gateway behavior change",
        "no runtime behavior change",
        "no scanner behavior change",
    ])

def test_v06301_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06301_safe_mock_demo_public_artifact_promotion.py"])

def main() -> None:
    test_v06301_doc_tokens()
    test_v06301_public_artifact_tokens()
    test_v06301_adr_tokens()
    test_v06301_issue_tokens()
    test_v06301_index_tokens()
    test_v06301_registered_in_run_all()
    print("v0.6.301 safe mock demo public artifact promotion checks passed")

if __name__ == "__main__":
    main()
