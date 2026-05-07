# Issue 0122: Add v0.6.52 public validator failure category mapping readiness review

## Summary

Add a v0.6.52 readiness review for a future mapping between public negative fixture categories and public validator failure categories.

## Acceptance criteria

* Add `docs/129-v0652-public-validator-failure-category-mapping-readiness-review.md`.
* Add `planning/decisions/ADR-0123-add-v0652-public-validator-failure-category-mapping-readiness-review.md`.
* Add this issue note.
* Add `tools/test_v0652_public_validator_failure_category_mapping_readiness_review.py`.
* Register the v0.6.52 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.51 metadata contract close-readiness exists.
* Confirm the current 13 negative fixture categories are retained.
* Confirm candidate failure category names are documented.
* Confirm mapping implementation is not started.
* Confirm validator output is not changed.
* Confirm validator behavior remains unchanged.
* Confirm no fixtures are added or rewritten.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not implement failure category mapping.
* Do not add validator failure category output.
* Do not add JSON Schema.
* Do not rewrite fixture metadata.
* Do not add negative fixtures.
* Do not modify validator behavior.
* Do not run scanners.
* Do not run Docker.
* Do not enable runtime execution.
* Do not inject credentials.
* Do not authorize customer targets.
* Do not authorize delivery.
