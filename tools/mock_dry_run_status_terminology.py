from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

COMPLETED = "completed"
MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION = "mock_dry_run_completed_no_real_execution"
COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW = "completed_context_unclassified_requires_review"

MOCK_OR_DRY_RUN_MODES = {
    "mock",
    "mock_only",
    "mock_run",
    "dry_run",
    "dry-run",
    "dryrun",
    "simulated",
    "simulation",
    "static_mock",
    "static/mock",
}

NO_REAL_EXECUTION_FLAGS = (
    "real_execution_permitted",
    "real_execution_authorized",
    "runtime_execution_authorized",
    "scanner_execution_authorized",
    "execution_authorized",
)


@dataclass(frozen=True)
class MockDryRunStatusTerminology:
    raw_status: str
    reviewer_status: str
    reviewer_label: str
    reason: str
    raw_status_preserved: bool
    behavior_modified: bool
    evidence_notes: tuple[str, ...]

    def as_evidence(self) -> dict[str, Any]:
        return {
            "raw_status": self.raw_status,
            "reviewer_status": self.reviewer_status,
            "reviewer_label": self.reviewer_label,
            "reason": self.reason,
            "raw_status_preserved": self.raw_status_preserved,
            "behavior_modified": self.behavior_modified,
            "evidence_notes": list(self.evidence_notes),
        }


def _string_value(value: Any) -> str | None:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped:
            return stripped
    return None


def _extract_status(record: Mapping[str, Any]) -> str:
    for key in ("status", "result_status", "execution_status", "tool_status"):
        value = _string_value(record.get(key))
        if value is not None:
            return value
    return ""


def _has_mock_or_dry_run_marker(record: Mapping[str, Any]) -> bool:
    for key in ("execution_mode", "mode", "run_mode", "target_mode", "scenario_mode"):
        value = _string_value(record.get(key))
        if value is not None and value.lower() in MOCK_OR_DRY_RUN_MODES:
            return True

    for key in ("mock", "mocked", "dry_run", "dryrun", "simulation", "simulated"):
        if record.get(key) is True:
            return True

    labels = record.get("labels")
    if isinstance(labels, (list, tuple, set)):
        for label in labels:
            value = _string_value(label)
            if value is not None and value.lower() in MOCK_OR_DRY_RUN_MODES:
                return True

    return False


def _has_explicit_no_real_execution(record: Mapping[str, Any]) -> bool:
    for key in NO_REAL_EXECUTION_FLAGS:
        if record.get(key) is False:
            return True

    for key in ("status_reason", "reason", "note", "evidence_note"):
        value = _string_value(record.get(key))
        if value is not None:
            lower = value.lower()
            if (
                "execution blocked" in lower
                or "execution_blocked" in lower
                or "execution-blocked" in lower
                or ("real execution" in lower and "false" in lower)
                or ("real_execution" in lower and "false" in lower)
                or ("real-execution" in lower and "false" in lower)
            ):
                return True

    return False


def classify_mock_dry_run_completed_status(record: Mapping[str, Any]) -> MockDryRunStatusTerminology:
    # Classify reviewer-facing terminology for mock/dry-run completed outputs.
    # This helper deliberately preserves the raw status string and does not
    # modify runtime behavior, gate behavior, scanner behavior, or delivery
    # behavior. It only creates a clearer reviewer-facing label.
    if not isinstance(record, Mapping):
        return MockDryRunStatusTerminology(
            raw_status="",
            reviewer_status="malformed_status_record_requires_review",
            reviewer_label="Malformed status record; reviewer must inspect source evidence.",
            reason="status_record_not_mapping",
            raw_status_preserved=True,
            behavior_modified=False,
            evidence_notes=("raw_status_not_changed", "terminology_only"),
        )

    raw_status = _extract_status(record)
    if raw_status != COMPLETED:
        return MockDryRunStatusTerminology(
            raw_status=raw_status,
            reviewer_status=raw_status,
            reviewer_label=f"Status remains `{raw_status}`.",
            reason="raw_status_not_completed",
            raw_status_preserved=True,
            behavior_modified=False,
            evidence_notes=("raw_status_not_changed", "terminology_only"),
        )

    has_mock_marker = _has_mock_or_dry_run_marker(record)
    has_no_real_execution = _has_explicit_no_real_execution(record)

    if has_mock_marker or has_no_real_execution:
        return MockDryRunStatusTerminology(
            raw_status=COMPLETED,
            reviewer_status=MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION,
            reviewer_label="Mock/dry-run completed; no real execution is implied.",
            reason="completed_status_in_mock_or_no_real_execution_context",
            raw_status_preserved=True,
            behavior_modified=False,
            evidence_notes=("raw_status_completed_preserved", "reviewer_label_disambiguates_no_real_execution"),
        )

    return MockDryRunStatusTerminology(
        raw_status=COMPLETED,
        reviewer_status=COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW,
        reviewer_label="Completed status requires context review before interpreting execution meaning.",
        reason="completed_status_without_mock_or_no_real_execution_context",
        raw_status_preserved=True,
        behavior_modified=False,
        evidence_notes=("raw_status_completed_preserved", "context_required_before_execution_interpretation"),
    )
