from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/139-v0662-public-validator-hardening-maintenance-cleanup-candidate.md"
V0661_DOC = ROOT / "docs/138-v0661-public-validator-hardening-maintenance-cleanup-planning.md"
V0660_DOC = ROOT / "docs/137-v0660-public-validator-hardening-maintenance-baseline-review.md"
V0659_DOC = ROOT / "docs/136-v0659-public-validator-hardening-maintenance-direction-review.md"
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
    "public_validator_hardening_maintenance_cleanup_candidate_added = true",
    "public_validator_hardening_maintenance_cleanup_candidate_is_documentation_only = true",
    "public_validator_hardening_maintenance_cleanup_candidate_uses_v0661_plan = true",
    "public_validator_hardening_maintenance_cleanup_candidate_uses_v0660_baseline = true",
    "reviewer_navigation_note_added = true",
    "public_validator_negative_fixture_index_summary_added = true",
    "cleanup_candidate_scope_limited_to_navigation_and_summary = true",
    "public_validator_hardening_maintenance_cleanup_implemented = true",
    "public_validator_hardening_maintenance_cleanup_file_reorganization_approved = false",
    "public_validator_hardening_maintenance_cleanup_fixture_rewrite_approved = false",
    "public_validator_hardening_maintenance_cleanup_validator_change_approved = false",
    "public_validator_behavior_hardening_implementation_readiness_deferred = true",
    "public_validator_behavior_hardening_implementation_not_approved = true",
    "documentation_only_hardening_scope_retained = true",
    "v0655_consolidated_baselines_retained = true",
    "v0656_readiness_boundary_retained = true",
    "v0657_scope_plan_retained = true",
    "v0658_scope_close_readiness_retained = true",
    "v0659_maintenance_direction_retained = true",
    "v0660_maintenance_baseline_retained = true",
    "v0661_cleanup_planning_retained = true",
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
    require(V0661_DOC.exists(), "v0.6.61 cleanup planning document must exist")
    require(V0660_DOC.exists(), "v0.6.60 maintenance baseline document must exist")
    require(V0659_DOC.exists(), "v0.6.59 maintenance direction document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: candidate",
            "reviewer navigation for the v0.6.44 through v0.6.62 public validator negative fixture and hardening track",
            "a reviewer-facing public validator negative fixture index summary",
            "It is a maintenance cleanup candidate only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only cleanup candidate test.",
            "v0.6.63 Public Validator Hardening Maintenance Cleanup Review and Close-Readiness",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.62 document missing cleanup candidate flag: {flag}")

    for version in [
        "v0.6.38-v0.6.41",
        "v0.6.42-v0.6.43",
        "v0.6.44-v0.6.46",
        "v0.6.47-v0.6.48",
        "v0.6.49-v0.6.51",
        "v0.6.52-v0.6.54",
        "v0.6.55",
        "v0.6.56-v0.6.58",
        "v0.6.59-v0.6.62",
    ]:
        require(version in doc_text, f"v0.6.62 document missing navigation range: {version}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.62 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.62 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.62 document missing retained false boundary flag: {flag}")

    for phrase in [
        "`run_all_local_checks.py` grouping comments",
        "mapping documentation layout",
        "fixture metadata explanations without field changes",
        "duplicate prose reduction across review documents",
        "Add validator JSON failure category output",
        "Metadata-level `expected_failure_category`",
        "JSON Schema for metadata or mapping",
        "New negative fixture categories",
        "Fixture rewrite or reduction",
    ]:
        require(phrase in doc_text, f"v0.6.62 document missing deferred cleanup or implementation phrase: {phrase}")

    v0661_text = V0661_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_cleanup_planning_completed = true" in v0661_text,
        "v0.6.61 cleanup planning must be completed",
    )
    require(
        "public_validator_hardening_maintenance_cleanup_candidate_added = false" in v0661_text,
        "v0.6.61 must not already add cleanup candidate",
    )
    require(
        "validator_behavior_modified = false" in v0661_text,
        "v0.6.61 must preserve validator behavior boundary",
    )

    v0660_text = V0660_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_baseline_established = true" in v0660_text,
        "v0.6.60 must establish maintenance baseline",
    )
    require(
        "maintenance_cleanup_may_be_considered = true" in v0660_text,
        "v0.6.60 must allow maintenance cleanup consideration",
    )

    v0659_text = V0659_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_direction_selected = maintenance_first" in v0659_text,
        "v0.6.59 must select maintenance-first direction",
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
        require("expected_failure_category" not in metadata, f"v0.6.62 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this cleanup candidate provides certification",
        "this cleanup candidate is legally sufficient",
        "this cleanup candidate provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this cleanup candidate",
        "runtime execution is authorized by this cleanup candidate",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.62 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.62 public validator hardening maintenance cleanup candidate tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
