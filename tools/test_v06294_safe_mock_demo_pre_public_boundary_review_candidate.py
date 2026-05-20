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
DOC = ROOT / "docs/369-v06294-safe-mock-demo-pre-public-boundary-review-candidate.md"
ADR = ROOT / "planning/decisions/ADR-0369-add-v06294-safe-mock-demo-pre-public-boundary-review-candidate.md"
ISSUE = ROOT / "planning/issues/0369-add-v06294-safe-mock-demo-pre-public-boundary-review-candidate.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED_TOKENS = ['safe_mock_demo_pre_public_boundary_review_candidate_created = true', 'safe_mock_demo_pre_public_boundary_review_candidate_id = safe_mock_demo_pre_public_boundary_review_candidate_v06294', 'safe_mock_demo_pre_public_boundary_review_candidate_status = candidate_not_applied', 'safe_mock_demo_pre_public_boundary_questions_defined = true', 'safe_mock_demo_pre_public_boundary_required_checks_defined = true', 'safe_mock_demo_pre_public_boundary_public_wording_checks_defined = true', 'safe_mock_demo_pre_public_boundary_private_artifact_checks_defined = true', 'safe_mock_demo_pre_public_boundary_demo_command_checks_defined = true', 'safe_mock_demo_pre_public_boundary_claim_boundary_checks_defined = true', 'safe_mock_demo_pre_public_boundary_release_blockers_defined = true', 'safe_mock_demo_pre_public_boundary_review_applied = false', 'safe_mock_demo_pre_public_boundary_review_completed = false', 'safe_mock_demo_pre_public_boundary_review_accepted = false', 'safe_mock_demo_public_artifact_promotion_created = false', 'safe_mock_demo_public_artifact_promotion_approved = false', 'publication_approval = false', 'private_generated_outputs_moved_public = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'local_only_demo_execution_boundary_candidate_created = false', 'real_scanner_execution_status = blocked', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'adapter_behavior_changed = false', 'schema_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'readme_front_page_rewritten = false', 'repository_metadata_changed = false', 'recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision', 'safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision_recommended = true']
REQUIRED_SHARED_TOKENS = ['v0.6.294 Safe Mock Demo Pre-Public Boundary Review Candidate', 'Previous checkpoint: v0.6.293 Next Work Selection Using Risk-Tiered Granularity', 'safe_mock_demo_pre_public_boundary_review_candidate', 'safe_mock_demo_pre_public_boundary_review_candidate_v06294', 'safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision', 'safe mock demo pre-public boundary review', 'safe mock demo is not live scanner execution', 'private-not-in-git', 'allowed-action: completed', 'denied-action: blocked', 'human-approval-required: requires_human_approval', 'runtime readiness status: not_detected_execution_blocked', 'target lab gate status: target_defined_execution_blocked', 'binding gate status: bound_execution_blocked', 'transition gate status: candidate_recorded_execution_blocked', 'execution authorized: False', 'real execution permitted: False', 'pre-public boundary review candidate is not publication approval', 'pre-public boundary review candidate is not public artifact promotion', 'pre-public boundary review candidate is not runtime demo readiness', 'pre-public boundary review candidate is not scanner readiness', 'pre-public boundary review candidate is not production readiness', 'No private generated outputs are moved public in v0.6.294.', 'v0.6.295 Safe Mock Demo Pre-Public Boundary Review Candidate Review and Decision']

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

def test_v06294_doc_tokens() -> None:
    assert_tokens(DOC, REQUIRED_TOKENS + REQUIRED_SHARED_TOKENS + [
        "Candidate result: safe mock demo pre-public boundary review candidate created",
        "Application status: candidate only; no review applied, public artifact promotion, publication approval, runtime readiness, scanner readiness, or gateway behavior changed",
    ])

def test_v06294_adr_tokens() -> None:
    assert_tokens(ADR, [
        "ADR-0369",
        "Status: proposed candidate",
        "Create a documentation-only Safe Mock Demo Pre-Public Boundary Review Candidate.",
    ] + REQUIRED_TOKENS + REQUIRED_SHARED_TOKENS)

def test_v06294_issue_tokens() -> None:
    assert_tokens(ISSUE, [
        "0369 - Add v0.6.294 Safe Mock Demo Pre-Public Boundary Review Candidate",
        "Status: completed by v0.6.294",
        "safe_mock_demo_pre_public_boundary_review_candidate_created = true",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision",
        "Proceed to v0.6.295 Safe Mock Demo Pre-Public Boundary Review Candidate Review and Decision",
    ])

def test_v06294_index_tokens() -> None:
    assert_tokens(README, [
        "v0.6.294 Safe Mock Demo Pre-Public Boundary Review Candidate",
        "safe_mock_demo_pre_public_boundary_review_candidate_created = true",
        "safe_mock_demo_pre_public_boundary_review_candidate_id = safe_mock_demo_pre_public_boundary_review_candidate_v06294",
        "safe_mock_demo_pre_public_boundary_review_candidate_status = candidate_not_applied",
        "safe_mock_demo_pre_public_boundary_required_checks_defined = true",
        "safe_mock_demo_pre_public_boundary_public_wording_checks_defined = true",
        "safe_mock_demo_public_artifact_promotion_created = false",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(CHANGELOG, [
        "v0.6.294 - Safe Mock Demo Pre-Public Boundary Review Candidate",
        "Created a documentation-only Safe Mock Demo Pre-Public Boundary Review Candidate.",
        "safe_mock_demo_pre_public_boundary_review_candidate_created = true",
        "safe_mock_demo_pre_public_boundary_review_candidate_id = safe_mock_demo_pre_public_boundary_review_candidate_v06294",
        "recommended_next_work_item = safe_mock_demo_pre_public_boundary_review_candidate_review_and_decision",
        "publication_approval = false",
        "runtime_demo_ready = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
    ] + REQUIRED_SHARED_TOKENS)
    assert_tokens(ROADMAP, [
        "After v0.6.294",
        "v0.6.295 Safe Mock Demo Pre-Public Boundary Review Candidate Review and Decision",
        "no pre-public boundary review applied",
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

def test_v06294_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06294_safe_mock_demo_pre_public_boundary_review_candidate.py"])

def main() -> None:
    test_v06294_doc_tokens()
    test_v06294_adr_tokens()
    test_v06294_issue_tokens()
    test_v06294_index_tokens()
    test_v06294_registered_in_run_all()
    print("v0.6.294 safe mock demo pre-public boundary review candidate checks passed")

if __name__ == "__main__":
    main()
