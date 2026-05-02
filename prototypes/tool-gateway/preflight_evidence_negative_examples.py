"""Negative preflight evidence examples for the AAEF-AI-VA local runtime path.

These examples are not live evidence records. They are deliberately invalid
evidence claims used to verify that unsafe or incomplete preflight evidence
fails closed and never authorizes runtime execution.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any


REQUIRED_NEGATIVE_EXAMPLE_IDS = {
    "NEG-PFE-001-missing-input-evidence",
    "NEG-PFE-002-mismatched-runtime-target-binding",
    "NEG-PFE-003-stale-runtime-readiness-state",
    "NEG-PFE-004-false-execution-authorized-claim",
    "NEG-PFE-005-false-preflight-satisfied-claim",
    "NEG-PFE-006-ai-visible-raw-evidence",
    "NEG-PFE-007-raw-artifact-capture-permitted",
    "NEG-PFE-008-example-live-evidence-confusion",
    "NEG-PFE-009-no-egress-verified-spoofing",
    "NEG-PFE-010-sanitizer-boundary-verified-spoofing",
}


REQUIRED_FALSE_OUTCOME_FLAGS = (
    "evidence_record_accepted",
    "check_satisfied",
    "all_required_checks_satisfied",
    "preflight_satisfied",
    "execution_authorized",
    "ready_for_runtime_execution",
    "real_execution_permitted",
    "external_process_execution_allowed",
    "network_activity_allowed",
    "scan_execution_allowed",
    "credential_injection_permitted",
    "raw_artifact_capture_permitted",
    "ai_visible_raw_evidence",
    "live_evidence_records_generated",
    "live_evidence_records_validated",
    "all_required_evidence_records_validated",
)


REQUIRED_TRUE_OUTCOME_FLAGS = (
    "must_reject",
    "fail_closed",
    "negative_examples_recorded",
    "negative_examples_validated",
)


def _rejected_outcome(reason: str) -> dict[str, Any]:
    outcome = {
        "rejection_reason": reason,
        "must_reject": True,
        "fail_closed": True,
        "negative_examples_recorded": True,
        "negative_examples_validated": True,
    }
    for flag in REQUIRED_FALSE_OUTCOME_FLAGS:
        outcome[flag] = False
    return outcome


def build_negative_preflight_evidence_examples() -> list[dict[str, Any]]:
    """Return representative invalid preflight evidence claims.

    The dangerous or incorrect values appear under ``claimed_state``. The
    authoritative expected behavior appears under ``expected_outcome`` and
    must remain fail-closed.
    """

    examples: list[dict[str, Any]] = [
        {
            "negative_example_id": "NEG-PFE-001-missing-input-evidence",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "runtime_readiness_check",
            "violation_type": "missing_input_evidence",
            "description": "A runtime readiness claim is provided without the required input evidence.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "runtime_readiness_claimed": True,
                "required_input_evidence_present": False,
            },
            "expected_outcome": _rejected_outcome("missing required input evidence"),
        },
        {
            "negative_example_id": "NEG-PFE-002-mismatched-runtime-target-binding",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "runtime_destination_binding_check",
            "violation_type": "mismatched_runtime_target_binding",
            "description": "The runtime destination binding does not match the authorized local lab target.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "runtime_target_binding_claimed": True,
                "authorized_target_binding": "local-lab:expected",
                "observed_target_binding": "local-lab:mismatched",
            },
            "expected_outcome": _rejected_outcome("runtime target binding mismatch"),
        },
        {
            "negative_example_id": "NEG-PFE-003-stale-runtime-readiness-state",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "runtime_readiness_check",
            "violation_type": "stale_runtime_readiness_state",
            "description": "The evidence claim relies on stale readiness state and must not satisfy preflight.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "runtime_readiness_claimed": True,
                "readiness_state_fresh": False,
            },
            "expected_outcome": _rejected_outcome("stale runtime readiness state"),
        },
        {
            "negative_example_id": "NEG-PFE-004-false-execution-authorized-claim",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "execution_authorization_check",
            "violation_type": "false_execution_authorized_claim",
            "description": "A submitted evidence claim incorrectly asserts execution authorization.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "execution_authorized": True,
                "authorization_source_trusted": False,
            },
            "expected_outcome": _rejected_outcome("untrusted false execution authorization claim"),
        },
        {
            "negative_example_id": "NEG-PFE-005-false-preflight-satisfied-claim",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "preflight_validation_check",
            "violation_type": "false_preflight_satisfied_claim",
            "description": "A submitted evidence claim incorrectly asserts that preflight is satisfied.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "preflight_satisfied": True,
                "all_required_checks_satisfied": False,
            },
            "expected_outcome": _rejected_outcome("untrusted false preflight satisfaction claim"),
        },
        {
            "negative_example_id": "NEG-PFE-006-ai-visible-raw-evidence",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "sanitizer_boundary_check",
            "violation_type": "ai_visible_raw_evidence",
            "description": "Raw evidence is marked as AI-visible instead of requiring a sanitized summary.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "ai_visible_raw_evidence": True,
                "sanitized_summary_required": False,
            },
            "expected_outcome": _rejected_outcome("raw evidence must not be AI-visible"),
        },
        {
            "negative_example_id": "NEG-PFE-007-raw-artifact-capture-permitted",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "sanitizer_boundary_check",
            "violation_type": "raw_artifact_capture_permitted",
            "description": "The evidence claim attempts to permit raw artifact capture during preflight.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "raw_artifact_capture_permitted": True,
                "sanitized_summary_required": False,
            },
            "expected_outcome": _rejected_outcome("raw artifact capture remains forbidden"),
        },
        {
            "negative_example_id": "NEG-PFE-008-example-live-evidence-confusion",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "preflight_evidence_record_check",
            "violation_type": "example_live_evidence_confusion",
            "description": "An illustrative example is incorrectly presented as if it were live evidence.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "example_record_generated": True,
                "live_evidence_record_claimed": True,
            },
            "expected_outcome": _rejected_outcome("generated examples are not live evidence"),
        },
        {
            "negative_example_id": "NEG-PFE-009-no-egress-verified-spoofing",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "no_egress_guard_check",
            "violation_type": "no_egress_verified_spoofing",
            "description": "A no-egress verification claim is asserted without trusted enforcement evidence.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "no_egress_verified": True,
                "trusted_enforcement_evidence_present": False,
            },
            "expected_outcome": _rejected_outcome("no-egress verification lacks trusted evidence"),
        },
        {
            "negative_example_id": "NEG-PFE-010-sanitizer-boundary-verified-spoofing",
            "example_kind": "negative_preflight_evidence_example",
            "check_id": "sanitizer_boundary_check",
            "violation_type": "sanitizer_boundary_verified_spoofing",
            "description": "A sanitizer boundary verification claim is asserted without trusted sanitizer evidence.",
            "is_live_evidence_record": False,
            "claimed_state": {
                "sanitizer_boundary_verified": True,
                "trusted_sanitizer_evidence_present": False,
            },
            "expected_outcome": _rejected_outcome("sanitizer boundary verification lacks trusted evidence"),
        },
    ]
    return deepcopy(examples)


def validate_negative_preflight_evidence_examples(
    examples: list[dict[str, Any]] | None = None,
) -> list[str]:
    """Validate that negative examples remain fail-closed and non-authorizing."""

    records = build_negative_preflight_evidence_examples() if examples is None else examples
    errors: list[str] = []

    seen_ids: set[str] = set()
    for index, record in enumerate(records):
        record_id = record.get("negative_example_id")
        prefix = record_id or f"record[{index}]"

        if not record_id:
            errors.append(f"{prefix}: missing negative_example_id")
            continue

        if record_id in seen_ids:
            errors.append(f"{prefix}: duplicate negative_example_id")
        seen_ids.add(record_id)

        if record.get("example_kind") != "negative_preflight_evidence_example":
            errors.append(f"{prefix}: example_kind must be negative_preflight_evidence_example")

        if record.get("is_live_evidence_record") is not False:
            errors.append(f"{prefix}: negative examples must not be live evidence records")

        if not record.get("check_id"):
            errors.append(f"{prefix}: missing check_id")

        if not record.get("violation_type"):
            errors.append(f"{prefix}: missing violation_type")

        claimed_state = record.get("claimed_state")
        if not isinstance(claimed_state, dict) or not claimed_state:
            errors.append(f"{prefix}: claimed_state must be a non-empty dict")

        expected_outcome = record.get("expected_outcome")
        if not isinstance(expected_outcome, dict):
            errors.append(f"{prefix}: expected_outcome must be a dict")
            continue

        for flag in REQUIRED_TRUE_OUTCOME_FLAGS:
            if expected_outcome.get(flag) is not True:
                errors.append(f"{prefix}: expected_outcome.{flag} must be true")

        for flag in REQUIRED_FALSE_OUTCOME_FLAGS:
            if expected_outcome.get(flag) is not False:
                errors.append(f"{prefix}: expected_outcome.{flag} must be false")

        if not expected_outcome.get("rejection_reason"):
            errors.append(f"{prefix}: rejection_reason is required")

    missing = REQUIRED_NEGATIVE_EXAMPLE_IDS - seen_ids
    if missing:
        errors.append(f"missing required negative examples: {sorted(missing)}")

    unexpected = seen_ids - REQUIRED_NEGATIVE_EXAMPLE_IDS
    if unexpected:
        errors.append(f"unexpected negative examples: {sorted(unexpected)}")

    return errors


def summarize_negative_preflight_evidence_examples() -> dict[str, Any]:
    examples = build_negative_preflight_evidence_examples()
    errors = validate_negative_preflight_evidence_examples(examples)
    return {
        "negative_examples_recorded": True,
        "negative_examples_validated": not errors,
        "negative_example_count": len(examples),
        "required_negative_example_count": len(REQUIRED_NEGATIVE_EXAMPLE_IDS),
        "validation_errors": errors,
        "preflight_satisfied": False,
        "execution_authorized": False,
        "ready_for_runtime_execution": False,
        "real_execution_permitted": False,
        "external_process_execution_allowed": False,
        "network_activity_allowed": False,
        "scan_execution_allowed": False,
        "raw_artifact_capture_permitted": False,
        "live_evidence_records_validated": False,
        "all_required_evidence_records_validated": False,
    }


if __name__ == "__main__":
    validation_errors = validate_negative_preflight_evidence_examples()
    if validation_errors:
        for validation_error in validation_errors:
            print(f"ERROR: {validation_error}")
        raise SystemExit(1)

    summary = summarize_negative_preflight_evidence_examples()
    print(
        "Negative preflight evidence examples validated: "
        f"{summary['negative_example_count']} examples"
    )
