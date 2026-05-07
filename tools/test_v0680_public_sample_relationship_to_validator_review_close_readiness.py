from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/156-v0680-public-sample-relationship-to-validator-review-close-readiness.md"
V0679_DOC = ROOT / "docs/155-v0679-public-sample-relationship-to-validator-candidate.md"
V0678_DOC = ROOT / "docs/154-v0678-public-sample-relationship-to-validator-planning.md"
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
    "public_sample_relationship_to_validator_review_completed = true",
    "public_sample_relationship_to_validator_close_ready = true",
    "close_public_sample_relationship_to_validator_candidate = true",
    "retain_v0679_public_sample_relationship_to_validator_candidate = true",
    "public_sample_relationship_to_validator_candidate_retained = true",
    "public_sample_relationship_to_validator_reader_aid_retained = true",
    "public_sample_relationship_to_validator_candidate_reviewed = true",
    "public_sample_relationship_to_validator_candidate_scope_preserved = true",
    "public_sample_relationship_to_validator_candidate_revision_required = false",
    "public_sample_relationship_to_validator_implemented = false",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_relationship_to_validator_fixture_changed = false",
    "public_sample_relationship_to_validator_negative_fixture_changed = false",
    "public_sample_relationship_to_validator_json_schema_added = false",
    "public_sample_relationship_to_validator_current_sample_content_retained = true",
    "public_sample_relationship_to_validator_current_validator_retained = true",
    "public_sample_relationship_to_validator_current_negative_fixtures_retained = true",
    "public_sample_relationship_to_validator_current_fixture_metadata_retained = true",
    "public_sample_relationship_to_validator_current_validator_output_retained = true",
    "evidence_interface_handback_readiness_started = false",
    "validator_behavior_modified = false",
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
    "validator_output_is_not_authority = true",
    "validator_success_is_not_execution_permission = true",
    "documentation_only_failure_category_mapping_is_not_validator_output = true",
    "documentation_only_failure_category_mapping_is_not_validator_output_contract = true",
    "public_negative_fixture_set_current = v0.6.46",
    "public_negative_fixture_count = 13",
    "aaef_handback_category_applied_implementation = true",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
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
    require(V0679_DOC.exists(), "v0.6.79 relationship candidate document must exist")
    require(V0678_DOC.exists(), "v0.6.78 relationship planning document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a review and close-readiness checkpoint only.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not start evidence-interface handback readiness planning.",
            "v0.6.81 Applied Evidence Next Gap Selection After Relationship Closeout",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.80 document missing close-readiness flag: {flag}")

    for area in [
        "Public sample purpose",
        "Public validator purpose",
        "Validator checks and non-checks",
        "Public negative fixture relationship",
        "Validator output is not authority",
        "Documentation-only mapping boundary",
        "Non-execution and non-delivery boundary",
        "Relationship matrix",
        "Candidate acceptance checks",
    ]:
        require(area in doc_text, f"v0.6.80 document missing retained relationship area: {area}")

    for phrase in [
        "Candidate preserves the current public sample content",
        "Candidate preserves current validator behavior",
        "Candidate preserves current validator output",
        "Candidate preserves current fixture metadata",
        "Candidate explains what the public sample is for",
        "Candidate explains what the public validator checks",
        "Candidate explains what the public validator does not check",
        "Candidate explains how negative fixtures relate to validator posture",
        "Candidate states validator output is not authority",
        "Candidate states validator success does not authorize execution",
        "Candidate states documentation-only failure category mapping is not validator output",
        "Candidate states documentation-only failure category mapping is not a validator output contract",
        "Candidate avoids certification, compliance, legal, audit, and equivalence claims",
        "Candidate does not prepare AAEF main handback material",
        "Candidate remains documentation-only",
        "Validator success does not authorize execution.",
        "Validator output is not authority.",
    ]:
        require(phrase in doc_text, f"v0.6.80 document missing expected phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.80 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.80 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.80 document missing retained false boundary flag: {flag}")

    for phrase in [
        "whether to start evidence-interface handback readiness planning",
        "whether to change the public sample",
        "whether to change validator behavior",
        "whether to add validator failure category output",
        "whether to create a validator output contract",
        "whether to refine the sanitized public sample",
        "whether to prepare an AAEF main handback",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.80 document missing unresolved decision phrase: {phrase}")

    v0679_text = V0679_DOC.read_text(encoding="utf-8")
    for phrase in [
        "public_sample_relationship_to_validator_candidate_added = true",
        "public_sample_relationship_to_validator_candidate_close_readiness_may_be_considered = true",
        "public_sample_relationship_to_validator_current_sample_content_retained = true",
        "public_sample_relationship_to_validator_current_validator_retained = true",
        "public_sample_relationship_to_validator_current_fixture_metadata_retained = true",
        "public_sample_relationship_to_validator_current_validator_output_retained = true",
        "validator_behavior_modified = false",
    ]:
        require(phrase in v0679_text, f"v0.6.79 missing expected boundary phrase: {phrase}")

    v0678_text = V0678_DOC.read_text(encoding="utf-8")
    require(
        "public_sample_relationship_to_validator_planning_completed = true" in v0678_text,
        "v0.6.78 relationship planning must be completed",
    )

    v0655_text = V0655_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_negative_fixture_track_consolidation_completed = true" in v0655_text,
        "v0.6.55 consolidation must be completed",
    )

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
        require("expected_failure_category" not in metadata, f"v0.6.80 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this close-readiness review provides certification",
        "this close-readiness review is legally sufficient",
        "this close-readiness review provides an audit opinion",
        "this project is authorized for customer delivery",
        "scanner execution is authorized by this close-readiness review",
        "runtime execution is authorized by this close-readiness review",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.80 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.80 public sample relationship-to-validator review and close-readiness tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
