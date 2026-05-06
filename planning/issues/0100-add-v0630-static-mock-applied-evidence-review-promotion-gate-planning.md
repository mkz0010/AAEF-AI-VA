# Issue 0100: Add v0.6.30 static/mock applied evidence package review and promotion gate planning

Status: Completed by v0.6.30 candidate  
Type: v0.6.30 planning / private package review / promotion gate

## Goal

Define the review and promotion gate for the private static/mock applied evidence
package generated in v0.6.29 before public sample promotion, structural validator
implementation, local diagnostic execution, Docker execution, scanner execution, or
delivery authorization.

## Acceptance criteria

- [x] Add v0.6.30 static/mock applied evidence package review and promotion gate planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define review input package.
- [x] Define review objectives.
- [x] Define private package review criteria.
- [x] Define promotion gate criteria.
- [x] Define promotion blocker categories.
- [x] Define promotion outcomes.
- [x] Define public sample planning boundary.
- [x] Define AAEF-side reporting boundary.
- [x] Define runtime and diagnostic execution separation.
- [x] Define rollback posture.
- [x] Preserve runtime/scanning/customer-target/delivery boundaries.

## Non-goals

- Promote public samples.
- Generate public sample artifacts.
- Generate a private review record.
- Implement structural validators.
- Execute validator checks.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
