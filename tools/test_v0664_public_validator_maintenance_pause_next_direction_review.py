from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/141-v0664-public-validator-maintenance-pause-next-direction-review.md"
V0663_DOC = ROOT / "docs/140-v0663-public-validator-hardening-maintenance-cleanup-review-close-readiness.md"
V0662_DOC = ROOT / "docs/139-v0662-public-validator-hardening-maintenance-cleanup-candidate.md"
V0661_DOC = ROOT / "docs/138-v0661-public-validator-hardening-maintenance-cleanup-planning.md"
V0660_DOC = ROOT / "docs/137-v0660-public-validator-hardening-maintenance-baseline-review.md"
V0655_DOC = ROOT / "docs/132-v0655-public-validator-negative-fixture-track-consolidation-review.md"
FIXTURE_ROOT = ROOT / "examples/applied-evidence/public-validator-negative-fixtures"
INDEX = FIXTURE_ROOT / "negative_fixture_index.example.json"
POSITIVE_CONTROL = ROOT / "examples/applied-evidence/sanitized-static-mock"
VALIDATOR = ROOT / "tools/validate_public_example_structure.py"

EXPECTED_CATEGORIES = [
    "missing-package-artifact",
    "missing-scenario-artifact",
    "missing-scenario-directory",
    "malformed-json",
    "broken-linkage",
    "scenario-posture-contradiction",
    "non-example-name",
    "missing-non-proof-statement",
    "missing-five-questions-mapping",
    "hygiene-not-passed",
    "forbidden-text-leakage",
    "overclaim-language",
    "boundary-flag-violation",
]

REQUIRED_METADATA_FIELDS = [
    "negative_category",
    "expected_validator_result",
    "expected_blockers",
    "synthetic_public_safe_static_fixture",
    "source_positive_control",
    "non_authorization_statement",
    "runtime_boundary",
]

REQUIRED_BOUNDARY_FLAGS = [
    "runtime_execution_authorized",
    "scanner_execution_authorized",
    "scan_execution_allowed",
    "credential_injection_permitted",
    "customer_target",
    "customer_target_authorized",
    "delivery_authorized",
    "customer_deliverable",
    "fixture_live_evidence",
    "validator_behavior_modified_by_fixture",
]

REQUIRED_DOC_FLAGS = [
    "public_validator_maintenance_pause_review_completed = true",
    "public_validator_maintenance_pause_point_reached = true",
    "public_validator_maintenance_pause_recommended = true",
    "public_validator_next_direction_review_completed = true",
    "public_validator_next_direction_selected = pause_and_reassess",
    "continue_narrow_maintenance_cleanup_now = false",
    "prepare_validator_behavior_implementation_readiness_now = false",
    "validator_behavior_hardening_implementation_readiness_deferred = true",
    "public_validator_behavior_hardening_implementation_not_approved = true",
    "reviewer_navigation_note_retained = true",
    "public_negative_fixture_index_summary_retained = true",
    "documentation_only_hardening_scope_retained = true",
    "v0655_consolidated_baselines_retained = true",
    "v0656_readiness_boundary_retained = true",
    "v0657_scope_plan_retained = true",
    "v0658_scope_close_readiness_retained = true",
    "v0659_maintenance_direction_retained = true",
    "v0660_maintenance_baseline_retained = true",
    "v0661_cleanup_planning_retained = true",
    "v0662_cleanup_candidate_retained = true",
    "v0663_cleanup_close_readiness_retained = true",
    "validator_behavior_hardening_implementation_may_be_considered = false",
    "validator_behavior_hardening_candidate_added = false",
    "validator_behavior_hardening_implemented = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "validator_failure_category_output_added = false",
    "validator_json_output_changed = false",
    "validator_output_contract_created = false",
    "metadata_level_expected_failure_category_added = false",
    "fixture_metadata_contract_changed = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "json_schema_added = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_execution_authorized = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "public_negative_fixture_set_static = true",
    "public_negative_fixture_set_synthetic = true",
    "public_negative_fixture_set_public_safe = true",
    "public_negative_fixture_set_retained = true",
    "positive_control_must_remain_passing = true",
    "negative_fixtures_must_remain_fail_closed = true",
    "public_safe_static_fixture_set_must_remain = true",
    "metadata_contract_baseline_must_remain = true",
    "documentation_only_mapping_baseline_must_remain = true",
    "documentation_only_hardening_scope_must_remain = true",
    "read_only_harnesses_must_remain = true",
    "validator_output_must_not_become_authority = true",
    "model_output_must_not_become_authority = true",
    "runtime_execution_must_remain_unauthorized = true",
    "scanner_execution_must_remain_unauthorized = true",
    "docker_execution_must_remain_unauthorized = true",
    "credential_injection_must_remain_unauthorized = true",
    "customer_target_operation_must_remain_unauthorized = true",
    "delivery_must_remain_unauthorized = true",
    "aaef_handback_category_applied_implementation = true",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"malformed JSON: {path.relative_to(ROOT)}: {exc}") from exc


def require_text(path: Path, expected: list[str]) -> str:
    require(path.exists(), f"missing required file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    for item in expected:
        require(item in text, f"{path.relative_to(ROOT)} missing expected text: {item}")
    return text


def main() -> int:
    require(V0663_DOC.exists(), "v0.6.63 cleanup review document must exist")
    require(V0662_DOC.exists(), "v0.6.62 cleanup candidate document must exist")
    require(V0661_DOC.exists(), "v0.6.61 cleanup planning document must exist")
    require(V0660_DOC.exists(), "v0.6.60 maintenance baseline document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a pause and next-direction review only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only review test.",
            "v0.6.65 Public Validator Pause Review Closeout or Applied Evidence Next-Direction Intake",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.64 document missing pause/next-direction flag: {flag}")

    for stage in [
        "Public validator baseline",
        "Applied Implementation handback",
        "Negative fixture planning and candidate",
        "Negative fixture coverage closure",
        "Metadata contract track",
        "Failure category mapping track",
        "Track consolidation",
        "Behavior hardening readiness and scope",
        "Maintenance-first path",
        "Maintenance cleanup planning and candidate",
    ]:
        require(stage in doc_text, f"v0.6.64 document missing inventory stage: {stage}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.64 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.64 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.64 document missing retained false boundary flag: {flag}")

    for phrase in [
        "Pause public validator hardening maintenance track",
        "Continue narrow maintenance cleanup",
        "Prepare validator behavior implementation readiness",
        "Add validator JSON failure category output",
        "Add metadata-level `expected_failure_category`",
        "Add JSON Schema for metadata or mapping",
        "Add new negative fixture categories",
        "Runtime, scanner, Docker, credential, customer-target, or delivery work",
    ]:
        require(phrase in doc_text, f"v0.6.64 document missing next-direction option: {phrase}")

    for phrase in [
        "whether validator behavior should eventually be hardened",
        "whether validator JSON failure category output should ever be added",
        "whether fixture metadata should ever gain `expected_failure_category`",
        "whether JSON Schema should ever be added",
        "whether fixture duplication should be reduced",
        "whether new negative fixture categories should be added",
    ]:
        require(phrase in doc_text, f"v0.6.64 document missing unresolved decision phrase: {phrase}")

    v0663_text = V0663_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_cleanup_track_close_ready = true" in v0663_text,
        "v0.6.63 cleanup track must be close-ready",
    )
    require(
        "close_public_validator_hardening_maintenance_cleanup_candidate = true" in v0663_text,
        "v0.6.63 must close cleanup candidate",
    )
    require(
        "validator_behavior_modified = false" in v0663_text,
        "v0.6.63 must preserve validator behavior boundary",
    )

    v0662_text = V0662_DOC.read_text(encoding="utf-8")
    require(
        "reviewer_navigation_note_added = true" in v0662_text,
        "v0.6.62 must add reviewer navigation note",
    )
    require(
        "public_validator_negative_fixture_index_summary_added = true" in v0662_text,
        "v0.6.62 must add public negative fixture index summary",
    )

    v0661_text = V0661_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_cleanup_planning_completed = true" in v0661_text,
        "v0.6.61 cleanup planning must be completed",
    )

    v0660_text = V0660_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_baseline_established = true" in v0660_text,
        "v0.6.60 must establish maintenance baseline",
    )

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text,
        "v0.6.55 consolidation must be completed",
    )
    require("validator_behavior_modified = false" in v0655_text, "v0.6.55 must preserve validator behavior boundary")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    for category in EXPECTED_CATEGORIES:
        metadata_path = FIXTURE_ROOT / category / "negative_fixture_metadata.example.json"
        require(metadata_path.exists(), f"metadata missing: {category}")
        metadata = load_json(metadata_path)

        for field in REQUIRED_METADATA_FIELDS:
            require(field in metadata, f"metadata field missing for {category}: {field}")

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.64 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this pause review provides certification",
        "this pause review is legally sufficient",
        "this pause review provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this pause review",
        "runtime execution is authorized by this pause review",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.64 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.64 public validator maintenance pause and next-direction review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
