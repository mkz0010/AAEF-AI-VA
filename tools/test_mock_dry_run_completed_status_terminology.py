from __future__ import annotations

from mock_dry_run_status_terminology import (
    COMPLETED,
    COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW,
    MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION,
    classify_mock_dry_run_completed_status,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    dry_run_completed = classify_mock_dry_run_completed_status(
        {
            "status": "completed",
            "execution_mode": "dry_run",
        }
    )
    require(dry_run_completed.raw_status == COMPLETED, "raw completed status must be preserved for dry_run")
    require(dry_run_completed.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "dry_run completed must get no-real-execution reviewer status")
    require(dry_run_completed.behavior_modified is False, "dry_run terminology helper must not modify behavior")

    mock_completed = classify_mock_dry_run_completed_status(
        {
            "result_status": "completed",
            "mock": True,
        }
    )
    require(mock_completed.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "mock completed must get no-real-execution reviewer status")

    no_real_execution_completed = classify_mock_dry_run_completed_status(
        {
            "execution_status": "completed",
            "real_execution_permitted": False,
        }
    )
    require(no_real_execution_completed.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "completed with real_execution_permitted false must get no-real-execution reviewer status")

    execution_blocked_note_completed = classify_mock_dry_run_completed_status(
        {
            "tool_status": "completed",
            "status_reason": "candidate_recorded_execution_blocked",
        }
    )
    require(execution_blocked_note_completed.reviewer_status == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "completed with execution-blocked note must get no-real-execution reviewer status")

    ambiguous_completed = classify_mock_dry_run_completed_status(
        {
            "status": "completed",
        }
    )
    require(ambiguous_completed.raw_status == COMPLETED, "ambiguous completed raw status must be preserved")
    require(ambiguous_completed.reviewer_status == COMPLETED_CONTEXT_UNCLASSIFIED_REQUIRES_REVIEW, "ambiguous completed must require context review")
    require(ambiguous_completed.behavior_modified is False, "ambiguous completed must not modify behavior")

    blocked = classify_mock_dry_run_completed_status(
        {
            "status": "blocked",
            "execution_mode": "dry_run",
        }
    )
    require(blocked.raw_status == "blocked", "non-completed raw status must be preserved")
    require(blocked.reviewer_status == "blocked", "non-completed reviewer status should remain unchanged")
    require(blocked.behavior_modified is False, "non-completed status must not modify behavior")

    malformed = classify_mock_dry_run_completed_status("not-a-record")
    require(malformed.reviewer_status == "malformed_status_record_requires_review", "malformed status record must require review")
    require(malformed.behavior_modified is False, "malformed status record terminology must not modify behavior")

    evidence = dry_run_completed.as_evidence()
    require(evidence["raw_status"] == "completed", "evidence must preserve raw_status")
    require(evidence["reviewer_status"] == MOCK_DRY_RUN_COMPLETED_NO_REAL_EXECUTION, "evidence must include reviewer_status")
    require(evidence["raw_status_preserved"] is True, "evidence must record raw_status_preserved")
    require(evidence["behavior_modified"] is False, "evidence must record behavior_modified false")

    evidence_text = str(evidence).lower()
    for forbidden in ["secret", "password", "token", "scanner_output", "customer", "credential"]:
        require(forbidden not in evidence_text, f"evidence should not include sensitive material: {forbidden}")

    print("Mock/dry-run completed status terminology helper tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
