from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/138-v0661-public-validator-hardening-maintenance-cleanup-planning.md"
V0660_DOC = ROOT / "docs/137-v0660-public-validator-hardening-maintenance-baseline-review.md"
V0659_DOC = ROOT / "docs/136-v0659-public-validator-hardening-maintenance-direction-review.md"
V0658_DOC = ROOT / "docs/135-v0658-public-validator-behavior-hardening-scope-review-close-readiness.md"
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

REQUIRED_DOC_FLAGS = [
    "public_validator_hardening_maintenance_cleanup_planning_completed = true",
    "public_validator_hardening_maintenance_cleanup_scope_defined = true",
    "public_validator_hardening_maintenance_cleanup_is_documentation_only = true",
    "public_validator_hardening_maintenance_cleanup_uses_v0660_baseline = true",
    "public_validator_hardening_maintenance_cleanup_may_be_considered = true",
    "public_validator_hardening_maintenance_cleanup_candidate_added = false",
    "public_validator_hardening_maintenance_cleanup_implemented = false",
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
    "validator_code_change = false",
    "validator_behavior_change = false",
    "validator_json_output_change = false",
    "validator_failure_category_output = false",
    "validator_output_contract = false",
    "metadata_level_expected_failure_category = false",
    "fixture_metadata_rewrite = false",
    "fixture_structure_rewrite = false",
    "json_schema_creation = false",
    "new_negative_fixture_category = false",
    "runtime_execution = false",
    "scanner_execution = false",
    "docker_execution = false",
    "credential_injection = false",
    "customer_target_operation = false",
    "delivery_authorization = false",
    "retain_public_safe_static_negative_fixtures = true",
    "retain_negative_fixture_index = true",
    "retain_read_only_negative_fixture_harness = true",
    "retain_metadata_contract_candidate = true",
    "retain_metadata_contract_test = true",
    "retain_documentation_only_mapping_candidate = true",
    "retain_mapping_candidate_test = true",
    "retain_documentation_only_hardening_scope = true",
    "retain_positive_control = true",
    "retain_public_example_structural_validator = true",
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
    require(V0660_DOC.exists(), "v0.6.60 maintenance baseline document must exist")
    require(V0659_DOC.exists(), "v0.6.59 maintenance direction document must exist")
    require(V0658_DOC.exists(), "v0.6.58 scope close-readiness document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: planning",
            "It is a maintenance cleanup planning checkpoint only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files in this checkpoint.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only planning test.",
            "It does not start validator behavior hardening implementation.",
            "It does not approve validator behavior hardening implementation readiness.",
            "v0.6.62 Public Validator Hardening Maintenance Cleanup Candidate",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.61 document missing cleanup planning flag: {flag}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.61 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for phrase in [
        "public validator negative fixture index summary",
        "reviewer navigation note for v0.6.44-v0.6.61",
        "`run_all_local_checks.py` negative fixture test grouping comments",
        "fixture metadata explanations",
        "documentation-only failure category mapping layout",
        "hardening scope non-implementation wording",
        "public claim boundaries",
        "next-step clarity",
        "Add validator JSON failure category output",
        "Metadata-level `expected_failure_category`",
        "JSON Schema for metadata or mapping",
        "New negative fixture categories",
        "Fixture rewrite or reduction",
    ]:
        require(phrase in doc_text, f"v0.6.61 document missing cleanup or deferred path phrase: {phrase}")

    v0660_text = V0660_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_maintenance_baseline_established = true" in v0660_text,
        "v0.6.60 must establish maintenance baseline",
    )
    require(
        "maintenance_cleanup_may_be_considered = true" in v0660_text,
        "v0.6.60 must allow maintenance cleanup consideration",
    )
    require(
        "validator_behavior_hardening_implementation_may_be_considered = false" in v0660_text,
        "v0.6.60 must not approve hardening implementation",
    )
    require("validator_behavior_modified = false" in v0660_text, "v0.6.60 must preserve validator behavior boundary")

    v0659_text = V0659_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_hardening_direction_selected = maintenance_first" in v0659_text,
        "v0.6.59 must select maintenance-first direction",
    )

    v0658_text = V0658_DOC.read_text(encoding="utf-8")
    require(
        "validator_behavior_hardening_scope_track_close_ready = true" in v0658_text,
        "v0.6.58 scope track must be close-ready",
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

        require(metadata.get("negative_category") == category, f"metadata category mismatch: {category}")
        require("expected_failure_category" not in metadata, f"v0.6.61 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this cleanup plan provides certification",
        "this cleanup plan is legally sufficient",
        "this cleanup plan provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this cleanup plan",
        "runtime execution is authorized by this cleanup plan",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.61 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.61 public validator hardening maintenance cleanup planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
