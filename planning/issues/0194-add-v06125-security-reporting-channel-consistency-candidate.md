# Issue 0194: Add v0.6.125 SECURITY.md reporting-channel consistency candidate

## Summary

Prepare SECURITY.md reporting-channel consistency as checkpoint 1 of 2 for the Medium-risk public-facing documentation work item selected in v0.6.124.

## Acceptance criteria

* Add `docs/201-v06125-security-reporting-channel-consistency-candidate.md`.
* Add `planning/decisions/ADR-0195-add-v06125-security-reporting-channel-consistency-candidate.md`.
* Add this issue note.
* Add `tools/test_v06125_security_reporting_channel_consistency_candidate.py`.
* Register the v0.6.125 test in `tools/run_all_local_checks.py`.
* Add SECURITY.md wording that clarifies sensitive report handling, non-sensitive public issue limits, repository-scope reporting, no third-party testing authorization, and separation from commercial/NDA discussions.
* Confirm no runtime behavior, validator behavior, schema, public sample, AAEF main issue, AAEF main PR, issue command, issue URL, or delivery authorization changes.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
