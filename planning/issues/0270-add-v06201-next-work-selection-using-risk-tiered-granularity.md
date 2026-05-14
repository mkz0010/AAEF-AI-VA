# Issue 0270: Add v0.6.201 next work selection using risk-tiered granularity

Status: Closed by v0.6.201

## Summary

Add a low-risk direction-selection checkpoint that selects the next Medium-risk work item after v0.6.200.

## Selected work item

- selected_next_work_item = static_fixture_review_path_public_communication_pack
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.202 Static Fixture Review Path Public Communication Pack Candidate
- selected_followup_checkpoint = v0.6.203 Static Fixture Review Path Public Communication Pack Review and Decision

## Acceptance criteria

- [x] Add v0.6.201 direction-selection document.
- [x] Add ADR record.
- [x] Add planning issue record.
- [x] Add a local test for the v0.6.201 selection boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.
- [x] Confirm that v0.6.201 does not create the communication pack body.
- [x] Preserve `Static Fixture Review Path` as the accepted phrase.

## Non-goals

This issue does not create communication pack content, publish an announcement, add runtime/scanner readiness, add customer PoC intake, or introduce production/compliance/equivalence claims.
