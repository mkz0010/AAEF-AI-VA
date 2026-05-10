# Issue 0198: Add v0.6.129 authorization expiry current-time check candidate

## Summary

Implement the authorization expiry current-time check candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.127.

## Acceptance criteria

* Add `tools/authorization_expiry_current_time.py`.
* Add `tools/test_authorization_expiry_current_time_check.py`.
* Add `docs/205-v06129-authorization-expiry-current-time-check-candidate.md`.
* Add `planning/decisions/ADR-0199-add-v06129-authorization-expiry-current-time-check-candidate.md`.
* Add this issue note.
* Add `tools/test_v06129_authorization_expiry_current_time_check_candidate.py`.
* Register candidate tests in `tools/run_all_local_checks.py`.
* Support deterministic current-time injection.
* Fail closed for expired, malformed, missing-required, timezone-naive, and ambiguous current-time inputs.
* Continue existing checks for not-expired authorization and deterministic equal-boundary cases.
* Return evidence-safe decision fields without secrets, credentials, scanner output, customer material, or private artifacts.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
