from pathlib import Path
import hashlib
import subprocess

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/428-v06353-emergency-public-commercial-term-cleanup.md"
ADR = ROOT / "planning/decisions/ADR-0428-add-v06353-emergency-public-commercial-term-cleanup.md"
ISSUE = ROOT / "planning/issues/0428-add-v06353-emergency-public-commercial-term-cleanup.md"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
ROADMAP = ROOT / "ROADMAP.md"
RUN_ALL = ROOT / "tools/run_all_local_checks.py"

REMOVED_PATHS = [
    ROOT / "product" / "personas.md",
    ROOT / "product" / ("pricing" + "-draft.md"),
]

FORBIDDEN_TERM_HASHES = ['351ce820b2b44449deed62b76c7a239d87ec5094a2b9ea71042721c18cdeb1df', 'a8fa7fd60893411a49907b5545ccf9c47ed8073cc38e2ac3b79c4f6156cd7755', '09503753a1b54f537202043a52ad1de940f0e14145fafc60b006b43481350769', 'e04a40e0fdc60d0d3028f787120d6f1554932b20df05ee2823e3adfe65ba53a8', '9c999ea21cd8378b20dfc3ea7a899c619bd957502bad38ecf0a07147b7d75c80']

REQUIRED = ['v0.6.353 Emergency Public Commercial Term Cleanup', 'public_commercial_term_cleanup_completed = true', 'current_public_tree_exact_commercial_draft_terms_removed = true', 'v06352_cleanup_test_plaintext_commercial_terms_removed = true', 'current_public_tree_product_pricing_files_absent = true', 'history_rewrite_performed = false', 'git_history_exposure_may_remain = true', 'separate_history_exposure_review_still_required = true', 'commercial_packaging_publication_deferred = true', 'pricing_draft_publication_deferred = true', 'commercial_offer_approval = false', 'gateway_core_integration_still_required = true', 'public_status_terminology_cleanup_still_required = true', 'readme_maturity_matrix_still_required = true', 'safe_local_only_demo_execution_boundary_runtime_applied = false', 'minimal_runtime_wiring_changed = false', 'tool_gateway_behavior_changed = false', 'runtime_behavior_changed = false', 'scanner_behavior_changed = false', 'execution_authorized = false', 'real_execution_permitted = false', 'external_target_authorization = false', 'publication_approval = false', 'public_announcement = deferred', 'runtime_demo_ready = false', 'scanner_readiness_claim = false', 'production_readiness_claim = false', 'recommended_next_work_item = public_history_exposure_review', 'public_history_exposure_review_recommended = true', 'Model output is not authority.', 'AI rationale is not authorization.', 'A gate decision is not AI self-approval.', 'Evidence supports reconstruction; it does not prove legal truth.', 'validator success is structural only', 'publication remains deferred', 'public commercial term cleanup is not publication approval', 'public commercial term cleanup is not customer demo readiness', 'public commercial term cleanup is not commercial offer approval', 'public commercial term cleanup is not runtime wiring', 'public commercial term cleanup is not runtime application', 'public commercial term cleanup is not execution authorization', 'public commercial term cleanup is not real execution permission', 'public commercial term cleanup is not external target authorization', 'public commercial term cleanup is not scanner readiness', 'public commercial term cleanup is not production readiness', 'No private generated outputs are moved public in v0.6.353.', 'v0.6.354 Public History Exposure Review']

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

def test_v06353_removed_files_absent_from_worktree() -> None:
    for path in REMOVED_PATHS:
        assert not path.exists(), f"removed public file still exists: {path.relative_to(ROOT)}"

def test_v06353_removed_files_absent_from_git_index() -> None:
    result = subprocess.run(
        ["git", "ls-files", *(path.relative_to(ROOT).as_posix() for path in REMOVED_PATHS)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    assert result.stdout.strip() == "", "removed public files are still tracked by Git: " + result.stdout

def test_v06353_primary_files() -> None:
    assert_tokens(DOC, REQUIRED)
    assert_tokens(ADR, [
        "ADR-0428",
        "Status: accepted emergency cleanup",
        "Remove plaintext commercial draft terms from the current tracked tree",
    ])
    assert_tokens(ISSUE, [
        "0428 - Add v0.6.353 Emergency Public Commercial Term Cleanup",
        "Status: completed by v0.6.353",
        "recommended_next_work_item = public_history_exposure_review",
        "Proceed to v0.6.354 Public History Exposure Review",
    ])

def test_v06353_index_files() -> None:
    assert_tokens(README, [
        "v0.6.353 Emergency Public Commercial Term Cleanup",
        "public_commercial_term_cleanup_completed = true",
        "current_public_tree_exact_commercial_draft_terms_removed = true",
        "history_rewrite_performed = false",
        "git_history_exposure_may_remain = true",
        "separate_history_exposure_review_still_required = true",
        "gateway_core_integration_still_required = true",
        "recommended_next_work_item = public_history_exposure_review",
    ])
    assert_tokens(CHANGELOG, [
        "v0.6.353 - Emergency Public Commercial Term Cleanup",
        "Removed exact commercial draft terms from the v0.6.352 cleanup test",
        "history_rewrite_performed = false",
        "recommended_next_work_item = public_history_exposure_review",
    ])
    assert_tokens(ROADMAP, [
        "After v0.6.353",
        "v0.6.354 Public History Exposure Review",
        "public history exposure review remains required",
        "Gateway core integration remains required",
    ])

def test_v06353_registered_in_run_all() -> None:
    assert_tokens(RUN_ALL, ["tools/test_v06353_emergency_public_commercial_term_cleanup.py"])

def test_v06353_plaintext_commercial_terms_absent_from_current_tracked_files() -> None:
    for path in tracked_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for phrase in candidate_phrases(text):
            assert digest(phrase) not in FORBIDDEN_TERM_HASHES, (
                f"{path.relative_to(ROOT)} contains a forbidden commercial draft term"
            )

def main() -> None:
    test_v06353_removed_files_absent_from_worktree()
    test_v06353_removed_files_absent_from_git_index()
    test_v06353_primary_files()
    test_v06353_index_files()
    test_v06353_registered_in_run_all()
    test_v06353_plaintext_commercial_terms_absent_from_current_tracked_files()
    print("v0.6.353 emergency public commercial term cleanup checks passed")

if __name__ == "__main__":
    main()
