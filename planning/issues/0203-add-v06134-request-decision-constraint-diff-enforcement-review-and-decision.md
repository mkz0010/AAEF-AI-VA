# Issue 0203: Add v0.6.134 request/decision constraint-diff enforcement review and decision

## Summary

Review and accept the request/decision constraint-diff enforcement candidate as checkpoint 3 of 3 for the High-risk gate-semantics work item selected in v0.6.131.

## Acceptance criteria

* Add `docs/210-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md`.
* Add `planning/decisions/ADR-0204-add-v06134-request-decision-constraint-diff-enforcement-review-and-decision.md`.
* Add this issue note.
* Add `tools/test_v06134_request_decision_constraint_diff_enforcement_review_and_decision.py`.
* Register the v0.6.134 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.133 helper and tests exist.
* Confirm deterministic request/decision comparison.
* Confirm fail-closed behavior for material mismatches, missing required fields, malformed inputs, and external_discovery escalation.
* Confirm exact matches continue existing checks.
* Confirm evidence-safe result fields avoid raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, and full raw payloads.
* Confirm the High-risk work item is closed.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
