from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/126-v0649-public-validator-negative-fixture-metadata-contract-readiness-review.md"
V0648_DOC = ROOT / "docs/125-v0648-public-validator-negative-fixture-coverage-hardening-planning.md"
V0647_DOC = ROOT / "docs/124-v0647-public-validator-negative-fixture-coverage-review-close-readiness.md"
V0646_DOC = ROOT / "docs/123-v0646-public-validator-negative-fixture-implementation-candidate.md"
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

CANDIDATE_FIELDS = [
    "negative_category",
    "expected_validator_result",
    "expected_blockers",
    "synthetic_public_safe_static_fixture",
    "source_positive_control",
    "non_authorization_statement",
    "runtime_boundary",
    "expected_failure_surface",
    "expected_error_keywords",
    "maintainer_note",
]

REQUIRED_REVIEW_FLAGS = [
    "metadata_contract_readiness_review_completed = true",
    "metadata_contract_candidate_may_be_considered = true",
    "metadata_contract_scope_defined = true",
    "metadata_contract_required_fields_identified = true",
    "metadata_contract_boundary_flags_identified = true",
    "metadata_contract_positive_control_linkage_required = true",
    "metadata_contract_expected_blockers_required = true",
    "metadata_contract_non_authorization_statement_required = true",
    "metadata_contract_runtime_boundary_required = true",
    "metadata_contract_implementation_ready_for_later_checkpoint = true",
]

REQUIRED_FALSE_FLAGS = [
    "metadata_contract_implemented = false",
    "metadata_contract_schema_added = false",
    "negative_fixture_metadata_rewritten = false",
    "negative_fixtures_added = false",
    "validator_behavior_modified = false",
    "validator_behavior_expansion_implemented = false",
    "runtime_execution_authorized = false",
    "scanner_execution_authorized = false",
    "docker_compose_executed = false",
    "credential_injection_permitted = false",
    "customer_target_authorized = false",
    "delivery_authorized = false",
]

BOUNDARY_FLAGS = [
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
    require(V0648_DOC.exists(), "v0.6.48 hardening planning document must exist")
    require(V0647_DOC.exists(), "v0.6.47 close-readiness document must exist")
    require(V0646_DOC.exists(), "v0.6.46 implementation candidate document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "positive control must exist")
    require(VALIDATOR.exists(), "public example validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: review",
            "It is a readiness review only.",
            "It does not implement a metadata contract.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not modify validator behavior.",
            "v0.6.48 Public Validator Negative Fixture Coverage Hardening Planning",
            "v0.6.50 Public Validator Negative Fixture Metadata Contract Candidate",
            "aaef_handback_category_applied_implementation = true",
            "aaef_core_promotion = false",
            "aaef_profile_promotion = false",
            "aaef_practical_package_promotion = false",
        ],
    )

    for field in CANDIDATE_FIELDS:
        require(f"`{field}`" in doc_text, f"candidate field not documented: {field}")

    for flag in REQUIRED_REVIEW_FLAGS + REQUIRED_FALSE_FLAGS:
        require(flag in doc_text, f"readiness document missing flag: {flag}")

    for flag in BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"boundary flag not documented as false: {flag}")

    v0648_text = V0648_DOC.read_text(encoding="utf-8")
    require(
        "expected_blocker_metadata_contract_planned = true" in v0648_text,
        "v0.6.48 must plan expected blocker metadata contract",
    )
    require("validator_behavior_modified = false" in v0648_text, "v0.6.48 must preserve validator behavior boundary")
    require("new_negative_fixtures_added = false" in v0648_text, "v0.6.48 must not add fixtures")

    v0647_text = V0647_DOC.read_text(encoding="utf-8")
    require(
        "public_validator_negative_fixture_track_close_ready = true" in v0647_text,
        "v0.6.47 must close the first negative fixture track",
    )

    v0646_text = V0646_DOC.read_text(encoding="utf-8")
    require("negative_fixture_count = 13" in v0646_text, "v0.6.46 must retain 13 negative fixtures")

    index = load_json(INDEX)
    require(str(index.get("fixture_set_id", "")).startswith("v0646"), "index must remain v0.6.46 fixture set")
    require(index.get("synthetic_public_safe_static_fixtures") is True, "index must remain public-safe static synthetic")
    require(str(index.get("source_positive_control", "")).endswith("sanitized-static-mock"), "index must preserve positive control")

    observed_categories = set()
    for category in EXPECTED_CATEGORIES:
        fixture_dir = FIXTURE_ROOT / category
        metadata_path = fixture_dir / "negative_fixture_metadata.example.json"
        require(fixture_dir.exists(), f"fixture directory missing: {category}")
        require(metadata_path.exists(), f"metadata missing: {category}")

        metadata = load_json(metadata_path)
        observed_categories.add(metadata.get("negative_category"))

        require(metadata.get("negative_category") == category, f"negative_category mismatch: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected_validator_result must be fail_closed: {category}")
        require(isinstance(metadata.get("expected_blockers"), list) and metadata["expected_blockers"], f"expected_blockers must be non-empty: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"synthetic_public_safe_static_fixture must be true: {category}")
        require(str(metadata.get("source_positive_control", "")).endswith("sanitized-static-mock"), f"source_positive_control missing: {category}")

        statement = metadata.get("non_authorization_statement")
        require(isinstance(statement, str) and statement.strip(), f"non_authorization_statement required: {category}")
        for fragment in [
            "does not authorize runtime execution",
            "scanner execution",
            "Docker execution",
            "credential injection",
            "customer-target operation",
            "delivery",
        ]:
            require(fragment in statement, f"non_authorization_statement missing fragment for {category}: {fragment}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime_boundary must be object: {category}")
        for flag in BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must be false for {category}: {flag}")

    require(set(EXPECTED_CATEGORIES).issubset(observed_categories), "all expected categories must be represented in metadata")

    # Check only affirmative overclaim phrasings. The document is allowed to mention
    # terms such as "audit opinion" when explicitly denying those claims.
    forbidden_affirmative_phrases = [
        "is certified compliant",
        "provides certification",
        "provides legal sufficiency",
        "is legally sufficient",
        "provides an audit opinion",
        "is production ready",
        "is authorized for customer delivery",
        "scanner execution is authorized",
        "runtime execution is authorized",
    ]
    lower_doc = doc_text.lower()
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"readiness document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.49 public validator negative fixture metadata contract readiness review tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
