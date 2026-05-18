from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/403-v06328-next-work-selection-using-risk-tiered-granularity.md"
ADR = ROOT / "planning/decisions/ADR-0403-add-v06328-next-work-selection-using-risk-tiered-granularity.md"
ISSUE = ROOT / "planning/issues/0403-add-v06328-next-work-selection-using-risk-tiered-granularity.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REQUIRED = ['v0.6.328 Next Work Selection Using Risk-Tiered Granularity', 'next_work_selection_using_risk_tiered_granularity_completed = true', 'next_work_selection_result = safe_local_only_demo_runtime_application_readiness_review', 'selected_next_work_item = safe_local_only_demo_runtime_application_readiness_review', 'selected_next_work_version = v0.6.329', 'selected_next_work_title = Safe Local-Only Demo Runtime Application Readiness Review', 'selected_next_work_scope = review_only_no_runtime_application', 'runtime_application_readiness_review_selected = true', 'runtime_application_readiness_review_created = false', 'runtime_application_readiness_review_completed = false', 'safe_local_only_runnable_demo_public_positioning_integration_closeout_review_completed = true', 'safe_local_only_runnable_demo_public_positioning_integration_track_status = closed', 'safe_local_only_runnable_demo_public_positioning_integration_outcome = bounded_readme_status_and_boundary_wording_integrated', 'safe_local_only_runnable_demo_ready = true', 'safe_local_only_runnable_demo_ready_scope = mock_first_localhost_only_reviewer_demo', 'safe_local_only_runnable_demo_public_ready = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'gateway_execution_path_behavior_modified = false', 'tool_gateway_behavior_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'deprioritized_public_launch_work = true', 'deprioritized_customer_demo_work = true', 'deprioritized_repository_metadata_work = true', 'deprioritized_real_scanner_execution_work = true', 'deprioritized_external_target_work = true', 'recommended_next_work_item = safe_local_only_demo_runtime_application_readiness_review', 'safe_local_only_demo_runtime_application_readiness_review_recommended = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'next work selection is not publication approval', 'next work selection is not public demo readiness', 'next work selection is not customer demo readiness', 'next work selection is not execution authorization', 'next work selection is not runtime demo readiness', 'next work selection is not scanner readiness', 'next work selection is not production readiness', 'next work selection is not external target authorization', 'No private generated outputs are moved public in v0.6.328.', 'v0.6.329 Safe Local-Only Demo Runtime Application Readiness Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06328_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0403",
        "Status: accepted",
        "Select `safe_local_only_demo_runtime_application_readiness_review` as the next work item using risk-tiered granularity.",
    ])
    assert_tokens(ISSUE, [
        "0403 - Add v0.6.328 Next Work Selection Using Risk-Tiered Granularity",
        "Status: completed by v0.6.328",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_readiness_review",
        "Proceed to v0.6.329 Safe Local-Only Demo Runtime Application Readiness Review",
    ])

def test_v06328_index_files() -> None:
    assert_tokens(README, [
        "v0.6.328 Next Work Selection Using Risk-Tiered Granularity",
        "next_work_selection_result = safe_local_only_demo_runtime_application_readiness_review",
        "selected_next_work_version = v0.6.329",
        "runtime_application_readiness_review_selected = true",
        "safe_local_only_runnable_demo_public_ready = false",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_readiness_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.328 - Next Work Selection Using Risk-Tiered Granularity",
        "Selected `safe_local_only_demo_runtime_application_readiness_review` as the next work item",
        "selected_next_work_version = v0.6.329",
        "recommended_next_work_item = safe_local_only_demo_runtime_application_readiness_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.328",
        "v0.6.329 Safe Local-Only Demo Runtime Application Readiness Review",
        "no runtime application readiness review completed",
        "no safe local-only demo execution boundary runtime-applied",
        "no execution authorization",
        "no real execution permitted",
        "no external target authorization",
    ])

def test_v06328_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06328_next_work_selection_using_risk_tiered_granularity.py"])

def test_v06328_avoids_raw_forbidden_claim_phrases() -> None:
    scanned_paths = [DOC, ADR, ISSUE, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
        "AI pentest agent",
        "production-ready scanner",
        "runtime-enforced scanner",
        "external-target-ready demo",
        "customer-ready PoC",
        "certified / audit-ready system",
        "compliance-sufficient control",
        "diagnostically complete",
        "diagnostically-complete",
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains raw forbidden phrase: {phrase}"

def main() -> None:
    test_v06328_primary_files()
    test_v06328_index_files()
    test_v06328_registered_in_run_all()
    test_v06328_avoids_raw_forbidden_claim_phrases()
    print("v0.6.328 next work selection using risk-tiered granularity checks passed")

if __name__ == "__main__":
    main()
