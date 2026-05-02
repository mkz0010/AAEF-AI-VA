"""Validate v0.3.4 negative preflight evidence examples."""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "prototypes" / "tool-gateway"))

from preflight_evidence_negative_examples import (  # noqa: E402
    REQUIRED_FALSE_OUTCOME_FLAGS,
    REQUIRED_NEGATIVE_EXAMPLE_IDS,
    build_negative_preflight_evidence_examples,
    summarize_negative_preflight_evidence_examples,
    validate_negative_preflight_evidence_examples,
)


def assert_false(value: object, message: str) -> None:
    if value is not False:
        raise AssertionError(message)


def assert_true(value: object, message: str) -> None:
    if value is not True:
        raise AssertionError(message)


def test_negative_examples_are_complete() -> None:
    examples = build_negative_preflight_evidence_examples()
    example_ids = {example["negative_example_id"] for example in examples}
    assert example_ids == REQUIRED_NEGATIVE_EXAMPLE_IDS
    assert len(examples) == 10


def test_negative_examples_validate() -> None:
    errors = validate_negative_preflight_evidence_examples()
    if errors:
        raise AssertionError("\n".join(errors))


def test_negative_examples_are_not_live_evidence() -> None:
    for example in build_negative_preflight_evidence_examples():
        assert_false(
            example["is_live_evidence_record"],
            f"{example['negative_example_id']}: must not be live evidence",
        )
        assert example["example_kind"] == "negative_preflight_evidence_example"


def test_negative_examples_fail_closed() -> None:
    for example in build_negative_preflight_evidence_examples():
        outcome = example["expected_outcome"]
        assert_true(outcome["must_reject"], f"{example['negative_example_id']}: must reject")
        assert_true(outcome["fail_closed"], f"{example['negative_example_id']}: must fail closed")
        for flag in REQUIRED_FALSE_OUTCOME_FLAGS:
            assert_false(
                outcome.get(flag),
                f"{example['negative_example_id']}: expected_outcome.{flag} must remain false",
            )


def test_dangerous_claims_do_not_authorize_execution() -> None:
    examples = build_negative_preflight_evidence_examples()

    dangerous_claims = [
        example
        for example in examples
        if any(
            example["claimed_state"].get(flag) is True
            for flag in (
                "execution_authorized",
                "preflight_satisfied",
                "ai_visible_raw_evidence",
                "raw_artifact_capture_permitted",
                "live_evidence_record_claimed",
                "no_egress_verified",
                "sanitizer_boundary_verified",
            )
        )
    ]
    if len(dangerous_claims) < 6:
        raise AssertionError("Expected multiple dangerous false-positive claims")

    for example in dangerous_claims:
        outcome = example["expected_outcome"]
        assert_false(
            outcome["execution_authorized"],
            f"{example['negative_example_id']}: dangerous claim authorized execution",
        )
        assert_false(
            outcome["preflight_satisfied"],
            f"{example['negative_example_id']}: dangerous claim satisfied preflight",
        )
        assert_false(
            outcome["ready_for_runtime_execution"],
            f"{example['negative_example_id']}: dangerous claim enabled runtime execution",
        )


def test_summary_keeps_runtime_disabled() -> None:
    summary = summarize_negative_preflight_evidence_examples()
    assert_true(summary["negative_examples_recorded"], "negative examples should be recorded")
    assert_true(summary["negative_examples_validated"], "negative examples should validate")

    for flag in (
        "preflight_satisfied",
        "execution_authorized",
        "ready_for_runtime_execution",
        "real_execution_permitted",
        "external_process_execution_allowed",
        "network_activity_allowed",
        "scan_execution_allowed",
        "raw_artifact_capture_permitted",
        "live_evidence_records_validated",
        "all_required_evidence_records_validated",
    ):
        assert_false(summary[flag], f"summary.{flag} must remain false")


def main() -> int:
    test_negative_examples_are_complete()
    test_negative_examples_validate()
    test_negative_examples_are_not_live_evidence()
    test_negative_examples_fail_closed()
    test_dangerous_claims_do_not_authorize_execution()
    test_summary_keeps_runtime_disabled()
    print("Negative preflight evidence example tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
