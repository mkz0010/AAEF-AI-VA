# Issue 0114: Add v0.6.44 public validator negative fixture planning

Status: Completed by v0.6.44 candidate  
Type: v0.6.44 planning / public validator negative fixtures

## Goal

Plan negative fixtures for the read-only public example structural validator without implementing fixtures, modifying validator behavior, running scanners, enabling runtime execution, or authorizing delivery.

## Acceptance criteria

- [x] Add public validator negative fixture planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record planned fixture root.
- [x] Record planned negative fixture categories.
- [x] Record expected blocker mapping.
- [x] Record fixture construction rules.
- [x] Record validation harness behavior.
- [x] Record positive control expectations.
- [x] Record AAEF handback relationship.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Implement negative fixtures.
- Implement negative fixture harness.
- Modify validator behavior.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
