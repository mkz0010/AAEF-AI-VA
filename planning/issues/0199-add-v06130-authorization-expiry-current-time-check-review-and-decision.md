# Issue 0199: Add v0.6.130 authorization expiry current-time check review and decision

## Summary

Review and accept the authorization expiry current-time check candidate as checkpoint 3 of 3 for the High-risk gate-semantics work item selected in v0.6.127.

## Acceptance criteria

* Add `docs/206-v06130-authorization-expiry-current-time-check-review-and-decision.md`.
* Add `planning/decisions/ADR-0200-add-v06130-authorization-expiry-current-time-check-review-and-decision.md`.
* Add this issue note.
* Add `tools/test_v06130_authorization_expiry_current_time_check_review_and_decision.py`.
* Register the v0.6.130 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.129 helper and tests exist.
* Confirm deterministic current-time injection.
* Confirm fail-closed behavior for expired, malformed, missing-required, timezone-naive, and ambiguous current-time inputs.
* Confirm not-expired and equal-boundary cases continue existing checks.
* Confirm evidence-safe result fields avoid secrets, credentials, scanner output, customer material, and private artifacts.
* Confirm the High-risk work item is closed.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
