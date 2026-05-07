from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DOC = ROOT / "docs/158-v0682-evidence-interface-handback-readiness-planning.md"
V0681_DOC = ROOT / "docs/157-v0681-applied-evidence-next-gap-selection-after-relationship-closeout.md"
V0680_DOC = ROOT / "docs/156-v0680-public-sample-relationship-to-validator-review-close-readiness.md"
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
    "evidence_interface_handback_readiness_planning_completed = true",
    "evidence_interface_handback_readiness_planning_is_documentation_only = true",
    "evidence_interface_handback_readiness_planning_uses_v0681_selection = true",
    "evidence_interface_handback_readiness_selected_gap_retained = true",
    "evidence_interface_handback_readiness_may_be_considered = true",
    "evidence_interface_handback_readiness_candidate_may_be_considered = true",
    "evidence_interface_handback_readiness_planning_only = true",
    "evidence_interface_handback_readiness_started = false",
    "evidence_interface_handback_readiness_implemented = false",
    "evidence_interface_handback_material_prepared = false",
    "evidence_interface_handback_candidate_generated = false",
    "evidence_interface_handback_candidate_close_readiness_may_be_considered = true",
    "aaef_main_handback_prepared = false",
    "aaef_main_handback_started = false",
    "aaef_main_handback_submitted = false",
    "aaef_main_issue_opened = false",
    "aaef_main_pull_request_opened = false",
    "aaef_main_release_note_drafted = false",
    "aaef_main_document_change_drafted = false",
    "aaef_core_promotion = false",
    "aaef_profile_promotion = false",
    "aaef_practical_package_promotion = false",
    "public_sample_relationship_to_validator_close_ready_retained = true",
    "public_sample_relationship_to_validator_reader_aid_retained = true",
    "public_sample_relationship_to_validator_candidate_revision_required = false",
    "public_sample_relationship_to_validator_implemented = false",
    "public_sample_relationship_to_validator_validator_changed = false",
    "public_sample_relationship_to_validator_output_changed = false",
    "public_sample_relationship_to_validator_contract_created = false",
    "public_sample_relationship_to_validator_public_sample_changed = false",
    "public_sample_relationship_to_validator_sample_refined = false",
    "public_sample_five_questions_clarity_close_ready_retained = true",
    "public_sample_five_questions_clarity_reader_aid_retained = true",
    "public_sample_five_questions_clarity_implemented = false",
    "public_sample_five_questions_clarity_sample_refined = false",
    "public_sample_five_questions_clarity_public_sample_changed = false",
    "applied_evidence_reviewer_current_state_summary_retained = true",
    "applied_evidence_reviewer_current_state_summary_close_ready_retained = true",
    "applied_evidence_current_state_summary_generated = true",
    "applied_evidence_implementation_started = false",
    "applied_evidence_package_generated = false",
    "applied_evidence_private_review_record_generated = false",
    "applied_evidence_public_sample_promoted = false",
    "applied_evidence_sanitized_public_sample_refined = false",
    "applied_evidence_fixture_rewrite_approved = false",
    "applied_evidence_schema_change_approved = false",
    "applied_evidence_handback_prepared = false",
    "applied_evidence_static_mock_package_retained = true",
    "applied_evidence_sanitized_public_sample_retained = true",
    "applied_evidence_reviewer_walkthrough_history_retained = true",
    "applied_evidence_five_questions_mapping_history_retained = true",
    "applied_evidence_handback_boundary_retained = true",
    "public_validator_pause_closeout_retained = true",
    "public_validator_track_pause_state_retained = true",
    "public_validator_maintenance_continue_now = false",
    "validator_behavior_hardening_implementation_readiness_deferred = true",
    "public_validator_behavior_hardening_implementation_not_approved = true",
    "documentation_only_hardening_scope_retained = true",
    "documentation_only_failure_category_mapping_retained = true",
    "reviewer_navigation_note_retained = true",
    "public_negative_fixture_index_summary_retained = true",
    "v0681_next_gap_selection_retained = true",
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
    "implementation_details = forbidden",
    "patent_sensitive_browser_state_or_diagnostic_reconstruction_detail = forbidden",
    "commercial_strategy = forbidden",
    "pricing_strategy = forbidden",
    "customer_material = forbidden",
    "customer_target_information = forbidden",
    "scanner_output = forbidden",
    "credential_material = forbidden",
    "private_generated_artifacts = forbidden",
    "private_review_records = forbidden",
    "runtime_authorization = forbidden",
    "delivery_authorization = forbidden",
    "diagnostic_completeness_claim = forbidden",
    "certification_claim = forbidden",
    "legal_advice_claim = forbidden",
    "audit_opinion_claim = forbidden",
    "compliance_claim = forbidden",
    "external_framework_equivalence_claim = forbidden",
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
    "validator_output_must_not_become_authority = true",
    "model_output_must_not_become_authority = true",
    "runtime_execution_must_remain_unauthorized = true",
    "scanner_execution_must_remain_unauthorized = true",
    "docker_execution_must_remain_unauthorized = true",
    "credential_injection_must_remain_unauthorized = true",
    "customer_target_operation_must_remain_unauthorized = true",
    "delivery_must_remain_unauthorized = true",
    "aaef_handback_category_applied_implementation = true",
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
    require(V0681_DOC.exists(), "v0.6.81 next-gap selection document must exist")
    require(V0680_DOC.exists(), "v0.6.80 relationship closeout document must exist")
    require(V0655_DOC.exists(), "v0.6.55 consolidation document must exist")
    require(FIXTURE_ROOT.exists(), "negative fixture root must exist")
    require(INDEX.exists(), "negative fixture index must exist")
    require(POSITIVE_CONTROL.exists(), "sanitized public sample baseline must exist")
    require(VALIDATOR.exists(), "public validator must exist")

    doc_text = require_text(
        DOC,
        [
            "Status: planning",
            "It is a planning checkpoint only.",
            "It does not prepare AAEF main handback material.",
            "It does not start AAEF main handback work.",
            "It does not open an AAEF main issue.",
            "It does not open an AAEF main pull request.",
            "It does not draft AAEF main release notes.",
            "It does not draft AAEF main document changes.",
            "It does not modify validator behavior.",
            "It does not add validator failure category output.",
            "It does not create a validator output contract.",
            "It does not add or change fixture metadata fields.",
            "It does not add a metadata-level `expected_failure_category` field.",
            "It does not add a JSON Schema file.",
            "It does not rewrite negative fixture metadata.",
            "It does not add new negative fixtures.",
            "It does not reorganize files.",
            "It does not edit `run_all_local_checks.py` beyond registering this read-only planning test.",
            "It does not start Applied Evidence implementation work.",
            "It does not generate new Applied Evidence packages.",
            "It does not generate private review records.",
            "It does not promote new public samples.",
            "It does not refine sanitized public sample content.",
            "It does not change public example text.",
            "v0.6.83 Evidence-Interface Handback Readiness Candidate",
        ],
    )

    for flag in REQUIRED_DOC_FLAGS:
        require(flag in doc_text, f"v0.6.82 document missing planning flag: {flag}")

    for phrase in [
        "whether there is an evidence/interface-level lesson",
        "whether the lesson answers the AAEF five questions",
        "whether the lesson reinforces model-output-is-not-authority",
        "whether the lesson reinforces validator-output-is-not-authority",
        "whether the lesson preserves non-execution evidence",
        "whether the lesson is abstract enough for AAEF main",
        "whether the lesson avoids implementation details",
        "whether the lesson avoids patent-sensitive detail",
        "whether the lesson avoids private artifacts",
        "whether the lesson avoids scanner output",
        "whether the lesson avoids credentials",
        "whether the lesson avoids customer material",
        "whether the lesson avoids delivery material",
        "whether the lesson avoids runtime authorization",
        "whether the lesson avoids certification, compliance, legal, audit, or equivalence claims",
    ]:
        require(phrase in doc_text, f"v0.6.82 document missing planned readiness phrase: {phrase}")

    for question in [
        "Is there an evidence/interface-level lesson?",
        "Does the lesson answer the AAEF five questions?",
        "Does the lesson reinforce model-output-is-not-authority?",
        "Does the lesson reinforce validator-output-is-not-authority?",
        "Does the lesson preserve non-execution evidence?",
        "Is the lesson public-safe?",
        "Does the lesson avoid overclaims?",
    ]:
        require(question in doc_text, f"v0.6.82 document missing readiness matrix question: {question}")

    for theme in [
        "Evidence answers the AAEF five questions",
        "AI output as request, not authority",
        "Gate decision decides execution permission",
        "Dispatch and non-dispatch both need evidence",
        "Validator output is not authority",
        "Static public samples are not live evidence",
        "Reviewer traceability across request, decision, execution posture, and evidence",
        "Non-execution evidence remains meaningful",
    ]:
        require(theme in doc_text, f"v0.6.82 document missing permitted handback theme: {theme}")

    for phrase in [
        "Candidate remains readiness triage only",
        "Candidate does not prepare handback material",
        "Candidate does not open or draft AAEF main issue or PR content",
        "Candidate identifies only evidence/interface-level lessons",
        "Candidate evaluates the AAEF five questions",
        "Candidate preserves model-output-is-not-authority",
        "Candidate preserves validator-output-is-not-authority",
        "Candidate preserves non-execution evidence boundaries",
        "Candidate excludes implementation details",
        "Candidate excludes patent-sensitive detail",
        "Candidate excludes private artifacts and scanner output",
        "Candidate excludes credentials, customer material, and delivery material",
        "Candidate avoids certification, compliance, legal, audit, and equivalence claims",
        "Candidate preserves public sample, validator, fixture, package, and runtime boundaries",
        "Candidate remains documentation-only",
    ]:
        require(phrase in doc_text, f"v0.6.82 document missing future candidate acceptance check: {phrase}")

    for phrase in [
        "vulnerability detection",
        "diagnostic completeness",
        "live execution evidence",
        "runtime authorization",
        "scanner authorization",
        "credential authorization",
        "customer-target authorization",
        "delivery authorization",
        "certification",
        "legal advice",
        "audit opinion",
        "compliance claim",
        "external-framework equivalence",
        "Validator success does not authorize execution.",
        "Validator output is not authority.",
    ]:
        require(phrase in doc_text, f"v0.6.82 document missing retained validator boundary phrase: {phrase}")

    for category in EXPECTED_CATEGORIES:
        require(f"`{category}`" in doc_text, f"v0.6.82 document missing retained category: {category}")
        require((FIXTURE_ROOT / category).exists(), f"fixture directory missing: {category}")

    for field in REQUIRED_METADATA_FIELDS:
        require(field in doc_text, f"v0.6.82 document missing retained metadata field: {field}")

    for flag in REQUIRED_BOUNDARY_FLAGS:
        require(f"{flag} = false" in doc_text, f"v0.6.82 document missing retained false boundary flag: {flag}")

    for phrase in [
        "whether an evidence-interface handback readiness candidate is ready",
        "whether any handback material should be prepared",
        "whether any AAEF main issue, pull request, release note, or document should be opened or drafted",
        "whether any lesson should be promoted to AAEF main",
        "whether to change the public sample",
        "whether to change validator behavior",
        "whether to add validator failure category output",
        "whether to create a validator output contract",
        "whether to refine the sanitized public sample",
        "whether to create a new reviewer walkthrough",
        "whether to generate a new static/mock package",
        "whether to create a new private review record",
        "whether to promote a new public sample",
        "whether runtime/scanner/Docker/credential/customer/delivery work should ever proceed",
    ]:
        require(phrase in doc_text, f"v0.6.82 document missing unresolved decision phrase: {phrase}")

    v0681_text = V0681_DOC.read_text(encoding="utf-8")
    require(
        "applied_evidence_next_gap_selected_after_relationship_closeout = evidence_interface_handback_readiness" in v0681_text,
        "v0.6.81 must select evidence-interface handback readiness",
    )
    require(
        "evidence_interface_handback_readiness_started = false" in v0681_text,
        "v0.6.81 must not start evidence-interface handback readiness",
    )
    require(
        "evidence_interface_handback_material_prepared = false" in v0681_text,
        "v0.6.81 must not prepare handback material",
    )
    require(
        "aaef_main_handback_prepared = false" in v0681_text,
        "v0.6.81 must not prepare AAEF main handback",
    )
    require("validator_behavior_modified = false" in v0681_text, "v0.6.81 must preserve validator behavior boundary")

    v0680_text = V0680_DOC.read_text(encoding="utf-8")
    require(
        "public_sample_relationship_to_validator_close_ready = true" in v0680_text,
        "v0.6.80 relationship closeout must be completed",
    )
    require(
        "evidence_interface_handback_readiness_started = false" in v0680_text,
        "v0.6.80 must not start evidence-interface handback readiness",
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
        require("expected_failure_category" not in metadata, f"v0.6.82 must not add metadata-level failure category: {category}")
        require(metadata.get("expected_validator_result") == "fail_closed", f"expected result must remain fail_closed: {category}")
        require(metadata.get("synthetic_public_safe_static_fixture") is True, f"fixture must remain public-safe static: {category}")

        boundary = metadata.get("runtime_boundary")
        require(isinstance(boundary, dict), f"runtime boundary must remain object: {category}")
        for flag in REQUIRED_BOUNDARY_FLAGS:
            require(boundary.get(flag) is False, f"runtime boundary flag must remain false for {category}: {flag}")

    lower_doc = doc_text.lower()
    forbidden_affirmative_phrases = [
        "this project is certified compliant",
        "this handback readiness planning provides certification",
        "this handback readiness planning is legally sufficient",
        "this handback readiness planning provides an audit opinion",
        "this planning prepares aaef main handback material",
        "scanner execution is authorized by this handback readiness planning",
        "runtime execution is authorized by this handback readiness planning",
    ]
    for phrase in forbidden_affirmative_phrases:
        require(phrase not in lower_doc, f"v0.6.82 document must not include affirmative overclaim phrase: {phrase}")

    print("v0.6.82 evidence-interface handback readiness planning tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
