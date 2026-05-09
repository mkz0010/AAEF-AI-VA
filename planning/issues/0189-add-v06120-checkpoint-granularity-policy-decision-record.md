# Issue 0189: Add v0.6.120 checkpoint granularity policy decision record

## Summary

Add a one-checkpoint decision record that adopts risk-tiered checkpoint granularity for future AAEF-AI-VA work.

## Acceptance criteria

* Add `docs/196-v06120-checkpoint-granularity-policy-decision-record.md`.
* Add `planning/decisions/ADR-0190-add-v06120-checkpoint-granularity-policy-decision-record.md`.
* Add this issue note.
* Add `tools/test_v06120_checkpoint_granularity_policy_decision_record.py`.
* Register the v0.6.120 test in `tools/run_all_local_checks.py`.
* Adopt risk-tiered checkpoint granularity.
* Demonstrate the new policy by completing this low-risk policy decision in one checkpoint.
* Confirm the previous expanded checkpoint pattern is no longer the default.
* Preserve the expanded pattern for critical-risk work.
* Confirm existing checkpoints, tags, and release history are not retroactively rewritten.
* Confirm no AAEF main issue, AAEF main PR, issue command, issue URL, runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, validator behavior change, schema change, public sample change, or AAEF Core/Profile/Practical Package promotion occurs.

## Non-goals

* Do not rewrite existing history.
* Do not modify old checkpoints.
* Do not reopen the AAEF main handback sequence.
* Do not submit anything to AAEF main.
* Do not modify validator behavior.
* Do not authorize runtime/scanner/Docker/credential/customer/delivery activity.
