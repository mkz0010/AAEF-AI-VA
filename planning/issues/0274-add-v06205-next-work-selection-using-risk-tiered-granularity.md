# Issue 0274: Add v0.6.205 next work selection using risk-tiered granularity

Status: Closed by v0.6.205

## Summary

Add a low-risk direction-selection checkpoint that selects the next Medium-risk work item after v0.6.204.

## Selected work item

- selected_next_work_item = static_fixture_review_path_repository_wording_integration_plan
- selected_next_work_item_risk_tier = medium
- selected_next_work_item_checkpoint_count = 2
- selected_next_checkpoint = v0.6.206 Static Fixture Review Path Repository Wording Integration Plan Candidate
- selected_followup_checkpoint = v0.6.207 Static Fixture Review Path Repository Wording Integration Plan Review and Decision

## Acceptance criteria

- [x] Add v0.6.205 direction-selection document.
- [x] Add ADR record.
- [x] Add planning issue record.
- [x] Add a local test for the v0.6.205 selection boundary.
- [x] Register the local test in `tools/run_all_local_checks.py`.
- [x] Update README, CHANGELOG, and ROADMAP.
- [x] Confirm that v0.6.205 does not create the integration plan body.
- [x] Preserve publication-deferred boundaries.

## Non-goals

This issue does not create the integration plan body, apply repository wording changes, publish an announcement, approve a social post, add runtime/scanner readiness, authorize customer PoC intake, create AAEF main publication material, create commercial terms, or make certification/legal/audit/production/equivalence/diagnostic-completeness claims.
