from pathlib import Path
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/429-v06354-public-history-exposure-review.md"
ADR = ROOT / "planning/decisions/ADR-0429-add-v06354-public-history-exposure-review.md"
ISSUE = ROOT / "planning/issues/0429-add-v06354-public-history-exposure-review.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REMOVED_PATHS = [
    ROOT / "product" / "personas.md",
    ROOT / "product" / ("pricing" + "-draft.md"),
]

FORBIDDEN_TERM_HASHES = ['4242364b442cf336c32cbaf994caa968cc5186002b235802dfbcb592b43c0372', 'd2105b8c0fa18fd728fef3e7efb7331f89c126f2faf90790b19a2809d4b9b30f', '4d54f9f7f3d65f1f920979fba721ce20934b8f6d1623ec3250f3093f2f660ac8', '606c582aa0e75d1217874e2c440545c58e809720542ce61e46ecba2605363cfb', '56b61a897e608cb43537136475452aa6ff80dc3a3451f5f7b8e1e09694fa3184']

REQUIRED = ['v0.6.354 Public History Exposure Review', 'public_history_exposure_review_completed = true', 'public_history_exposure_review_id = public_history_exposure_review_v06354', 'current_tree_cleanup_completed = true', 'current_tree_product_pricing_files_absent = true', 'current_tree_exact_commercial_draft_terms_absent = true', 'current_tree_plaintext_commercial_draft_terms_absent = true', 'prior_git_history_exposure_confirmed = true', 'history_exposure_category = prior_removed_commercial_draft_material', 'history_exposure_severity = competitive_draft_exposure_not_secret_credential_exposure', 'history_rewrite_required = false', 'history_rewrite_deferred = true', 'repo_recreation_required = false', 'repo_recreation_deferred = true', 'history_rewrite_performed = false', 'repo_recreated = false', 'git_history_exposure_may_remain = true', 'public_history_exposure_accepted_with_current_tree_cleanup = true', 'commercial_material_publication_deferred = true', 'commercial_packaging_publication_deferred = true', 'pricing_draft_publication_deferred = true', 'commercial_offer_approval = false', 'publication_approval = false', 'public_announcement = deferred', 'customer_demo_approval = false', 'gateway_core_integration_still_required = true', 'authorization_expiry_gateway_core_integration_still_required = true', 'constraint_diff_gateway_core_integration_still_required = true', 'external_discovery_fail_closed_gateway_core_integration_still_required = true', 'public_status_terminology_cleanup_still_required = true', 'readme_maturity_matrix_still_required = true', 'readme_front_page_simplification_still_required = true', 'evidence_trace_strengthening_still_required = true', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'tool_gateway_behavior_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = gateway_core_safety_integration_status_and_priority_review', 'gateway_core_safety_integration_status_and_priority_review_recommended = true', 'public_history_exposure_review_recommended = false', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'public history exposure review is not history rewrite', 'public history exposure review is not repository recreation', 'public history exposure review is not publication approval', 'public history exposure review is not customer demo readiness', 'public history exposure review is not commercial offer approval', 'public history exposure review is not runtime wiring', 'public history exposure review is not runtime application', 'public history exposure review is not execution authorization', 'public history exposure review is not real execution permission', 'public history exposure review is not external target authorization', 'public history exposure review is not scanner readiness', 'public history exposure review is not production readiness', 'No private generated outputs are moved public in v0.6.354.', 'v0.6.355 Gateway Core Safety Integration Status and Priority Review']

def read(path: Path) -> str:
    assert path.exists(), f"missing file: {path.relative_to(ROOT)}"
    return path.read_text(encoding="utf-8")

def assert_tokens(path: Path, tokens: list[str]) -> None:
    text = read(path)
    for token in tokens:
        assert token in text, f"{path.relative_to(ROOT)} missing token: {token}"

def digest(value: str) -> str:
    return hashlib.sha256(value.lower().encode("utf-8")).hexdigest()

def candidate_phrases(text: str) -> set[str]:
    words = []
    for token in text.replace("_", " ").replace("-", " ").split():
        cleaned = "".join(ch for ch in token.lower() if ch.isalnum())
        if cleaned:
            words.append(cleaned)
    phrases = set()
    for width in range(1, 5):
        for idx in range(0, max(0, len(words) - width + 1)):
            phrases.add(" ".join(words[idx:idx + width]))
    return phrases

def tracked_text_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    allowed_suffixes = {".md", ".py", ".txt", ".json", ".yml", ".yaml", ".csv"}
    files = []
    for line in result.stdout.splitlines():
        path = ROOT / line
        if path.suffix.lower() in allowed_suffixes:
            files.append(path)
    return files

def test_v06354_removed_files_absent_from_worktree() -> None:
    for path in REMOVED_PATHS:
        assert not path.exists(), f"removed public file still exists: {path.relative_to(ROOT)}"

def test_v06354_removed_files_absent_from_git_index() -> None:
    result = subprocess.run(
        ["git", "ls-files", *(path.relative_to(ROOT).as_posix() for path in REMOVED_PATHS)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    assert result.stdout.strip() == "", "removed public files are still tracked by Git: " + result.stdout

def test_v06354_plaintext_commercial_terms_absent_from_current_tracked_files() -> None:
    for path in tracked_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for phrase in candidate_phrases(text):
            assert digest(phrase) not in FORBIDDEN_TERM_HASHES, (
                f"{path.relative_to(ROOT)} contains a forbidden commercial draft term"
            )

def test_v06354_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0429",
        "Status: accepted",
        "Do not rewrite Git history and do not recreate the repository at this checkpoint.",
    ])
    assert_tokens(ISSUE, [
        "0429 - Add v0.6.354 Public History Exposure Review",
        "Status: completed by v0.6.354",
        "recommended_next_work_item = gateway_core_safety_integration_status_and_priority_review",
        "Proceed to v0.6.355 Gateway Core Safety Integration Status and Priority Review",
    ])

def test_v06354_index_files() -> None:
    assert_tokens(README, [
        "v0.6.354 Public History Exposure Review",
        "public_history_exposure_review_completed = true",
        "current_tree_cleanup_completed = true",
        "history_rewrite_required = false",
        "repo_recreation_required = false",
        "history_rewrite_performed = false",
        "repo_recreated = false",
        "gateway_core_integration_still_required = true",
        "recommended_next_work_item = gateway_core_safety_integration_status_and_priority_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.354 - Public History Exposure Review",
        "history_rewrite_required = false",
        "repo_recreation_required = false",
        "recommended_next_work_item = gateway_core_safety_integration_status_and_priority_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.354",
        "v0.6.355 Gateway Core Safety Integration Status and Priority Review",
        "no history rewrite performed",
        "no repository recreation performed",
        "Gateway core integration remains required",
    ])

def test_v06354_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06354_public_history_exposure_review.py"])

def main() -> None:
    test_v06354_removed_files_absent_from_worktree()
    test_v06354_removed_files_absent_from_git_index()
    test_v06354_plaintext_commercial_terms_absent_from_current_tracked_files()
    test_v06354_primary_files()
    test_v06354_index_files()
    test_v06354_registered_in_run_all()
    print("v0.6.354 public history exposure review checks passed")

if __name__ == "__main__":
    main()
