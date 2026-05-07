# Issue 0123: Add v0.6.53 public validator failure category mapping candidate

## Summary

Add a v0.6.53 documentation-only candidate mapping between public negative fixture categories and public validator failure category names.

## Acceptance criteria

* Add `docs/130-v0653-public-validator-failure-category-mapping-candidate.md`.
* Add `planning/decisions/ADR-0124-add-v0653-public-validator-failure-category-mapping-candidate.md`.
* Add this issue note.
* Add `tools/test_v0653_public_validator_failure_category_mapping_candidate.py`.
* Register the v0.6.53 test in `tools/run_all_local_checks.py`.
* Confirm v0.6.52 readiness review exists.
* Confirm the mapping table covers all current 13 negative fixture categories.
* Confirm candidate failure category names are documented.
* Confirm the mapping is documentation-only.
* Confirm no validator output is added.
* Confirm no fixture metadata field is added.
* Confirm no fixture metadata is rewritten.
* Confirm no fixtures are added.
* Confirm validator behavior remains unchanged.
* Preserve runtime, scanner, Docker, credential, customer-target, and delivery prohibitions.

## Non-goals

* Do not add validator failure category output.
* Do not add metadata-level failure category fields.
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
