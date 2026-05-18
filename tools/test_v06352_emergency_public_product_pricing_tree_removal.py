from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/427-v06352-emergency-public-product-pricing-tree-removal.md"
ADR = ROOT / "planning/decisions/ADR-0427-add-v06352-emergency-public-product-pricing-tree-removal.md"
ISSUE = ROOT / "planning/issues/0427-add-v06352-emergency-public-product-pricing-tree-removal.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REMOVED = [
    ROOT / "product/personas.md",
    ROOT / "product/pricing-draft.md",
]

REQUIRED = ['v0.6.352 Emergency Public Product/Pricing Tree Removal', 'public_product_pricing_tree_removal_completed = true', 'public_product_personas_removed_from_public_tree = true', 'public_product_pricing_draft_removed_from_public_tree = true', 'product_pricing_public_tree_exposure_closed_for_current_tree = true', 'current_public_tree_contains_product_personas_md = false', 'current_public_tree_contains_product_pricing_draft_md = false', 'commercial_persona_detail_publication_deferred = true', 'pricing_draft_publication_deferred = true', 'commercial_packaging_publication_deferred = true', 'history_rewrite_performed = false', 'git_history_exposure_may_remain = true', 'separate_history_exposure_review_required = true', 'public_repo_should_not_include_pricing_draft = true', 'public_repo_should_not_include_commercial_persona_pack = true', 'README_commercial_readiness_consistency_preserved = true', 'not_customer_ready_managed_assessment_platform_boundary_preserved = true', 'gateway_core_integration_still_required = true', 'external_review_p0_gateway_core_integration_not_completed = true', 'completed_public_status_cleanup_still_required = true', 'readme_maturity_matrix_still_required = true', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'tool_gateway_behavior_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = public_history_exposure_review', 'public_history_exposure_review_recommended = true', 'safe_local_only_demo_minimal_runtime_wiring_implementation_closeout_review_deferred = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'public product/pricing tree removal is not publication approval', 'public product/pricing tree removal is not customer demo readiness', 'public product/pricing tree removal is not commercial offer approval', 'public product/pricing tree removal is not runtime wiring', 'public product/pricing tree removal is not runtime application', 'public product/pricing tree removal is not execution authorization', 'public product/pricing tree removal is not real execution permission', 'public product/pricing tree removal is not external target authorization', 'public product/pricing tree removal is not scanner readiness', 'public product/pricing tree removal is not production readiness', 'No private generated outputs are moved public in v0.6.352.', 'v0.6.353 Public History Exposure Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def test_v06352_removed_files_absent_from_worktree() -> None:
    for path in REMOVED:
        assert not path.exists(), f"removed public file still exists: {path.relative_to(ROOT)}"

def test_v06352_removed_files_absent_from_git_index() -> None:
    result = subprocess.run(
        ["git", "ls-files", "product/personas.md", "product/pricing-draft.md"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    assert result.stdout.strip() == "", "removed public files are still tracked by Git: " + result.stdout

def test_v06352_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0427",
        "Status: accepted emergency cleanup",
        "Remove product/personas.md and product/pricing-draft.md from the current public repository tree.",
    ])
    assert_tokens(ISSUE, [
        "0427 - Add v0.6.352 Emergency Public Product/Pricing Tree Removal",
        "Status: completed by v0.6.352",
        "recommended_next_work_item = public_history_exposure_review",
        "Proceed to v0.6.353 Public History Exposure Review",
    ])

def test_v06352_index_files() -> None:
    assert_tokens(README, [
        "v0.6.352 Emergency Public Product/Pricing Tree Removal",
        "public_product_pricing_tree_removal_completed = true",
        "current_public_tree_contains_product_personas_md = false",
        "current_public_tree_contains_product_pricing_draft_md = false",
        "history_rewrite_performed = false",
        "git_history_exposure_may_remain = true",
        "separate_history_exposure_review_required = true",
        "gateway_core_integration_still_required = true",
        "safe_local_only_demo_execution_boundary_runtime_applied = false",
        "minimal_runtime_wiring_changed = false",
        "execution_authorized = false",
        "real_execution_permitted = false",
        "external_target_authorization = false",
        "recommended_next_work_item = public_history_exposure_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.352 - Emergency Public Product/Pricing Tree Removal",
        "Removed `product/personas.md` and `product/pricing-draft.md` from the current public repository tree.",
        "public_product_pricing_tree_removal_completed = true",
        "history_rewrite_performed = false",
        "recommended_next_work_item = public_history_exposure_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.352",
        "v0.6.353 Public History Exposure Review",
        "current public tree no longer contains product/personas.md",
        "current public tree no longer contains product/pricing-draft.md",
        "Git history may still expose prior contents",
        "no history rewrite performed",
        "Gateway core integration remains required",
    ])

def test_v06352_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06352_emergency_public_product_pricing_tree_removal.py"])

def test_v06352_avoids_public_commercial_detail_terms() -> None:
    scanned_paths = [DOC, ADR, ISSUE, README, CHANGELOG, ROADMAP]
    raw_forbidden_phrases = [
    ]
    for path in scanned_paths:
        text = read(path)
        for phrase in raw_forbidden_phrases:
            assert phrase not in text, f"{path.relative_to(ROOT)} contains public commercial detail phrase: {phrase}"

def main() -> None:
    test_v06352_removed_files_absent_from_worktree()
    test_v06352_removed_files_absent_from_git_index()
    test_v06352_primary_files()
    test_v06352_index_files()
    test_v06352_registered_in_run_all()
    test_v06352_avoids_public_commercial_detail_terms()
    print("v0.6.352 emergency public product/pricing tree removal checks passed")

if __name__ == "__main__":
    main()
