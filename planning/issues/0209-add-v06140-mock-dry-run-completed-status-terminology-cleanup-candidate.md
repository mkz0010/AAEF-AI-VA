# Issue 0209: Add v0.6.140 mock/dry-run completed status terminology cleanup candidate

## Summary

Implement the mock/dry-run `completed` status terminology cleanup candidate as checkpoint 1 of 2 for the Medium-risk work item selected in v0.6.139.

## Acceptance criteria

* Add `tools/mock_dry_run_status_terminology.py`.
* Add `tools/test_mock_dry_run_completed_status_terminology.py`.
* Add `docs/216-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md`.
* Add `planning/decisions/ADR-0210-add-v06140-mock-dry-run-completed-status-terminology-cleanup-candidate.md`.
* Add this issue note.
* Add `tools/test_v06140_mock_dry_run_completed_status_terminology_cleanup_candidate.py`.
* Register candidate tests in `tools/run_all_local_checks.py`.
* Preserve raw `completed` status behavior.
* Add reviewer-facing terminology for mock/dry-run or explicitly no-real-execution `completed` records.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not modify runtime behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
