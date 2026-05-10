# Issue 0202: Add v0.6.133 request/decision constraint-diff enforcement candidate

## Summary

Implement the request/decision constraint-diff enforcement candidate as checkpoint 2 of 3 for the High-risk gate-semantics work item selected in v0.6.131.

## Acceptance criteria

* Add `tools/request_decision_constraint_diff.py`.
* Add `tools/test_request_decision_constraint_diff_enforcement.py`.
* Add `docs/209-v06133-request-decision-constraint-diff-enforcement-candidate.md`.
* Add `planning/decisions/ADR-0203-add-v06133-request-decision-constraint-diff-enforcement-candidate.md`.
* Add this issue note.
* Add `tools/test_v06133_request_decision_constraint_diff_enforcement_candidate.py`.
* Register candidate tests in `tools/run_all_local_checks.py`.
* Support deterministic evidence-safe request/decision constraint comparison.
* Fail closed for material mismatches, missing required fields, malformed inputs, and external_discovery escalation.
* Continue existing checks for exact request/decision matches.
* Return evidence-safe decision fields without raw secrets, raw credentials, tokens, private customer material, scanner output, private artifacts, or full raw payloads.
* Confirm no runtime/scanner/Docker/credential/customer/delivery authorization, AAEF main issue/PR, issue command/URL, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not complete the review/decision checkpoint.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
* Do not reopen the AAEF main handback sequence.
* Do not modify validator behavior.
