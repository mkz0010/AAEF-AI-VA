# Issue 0098: Add v0.6.28 static/mock applied evidence generation readiness review

Status: Completed by v0.6.28 candidate  
Type: v0.6.28 review / static mock applied evidence generation readiness

## Goal

Review whether static/mock applied evidence package generation is safe to begin before
generating fixtures, generating evidence packages, implementing structural validators,
running local diagnostic tools, creating runnable Compose configuration, image pull,
container startup, port binding, dry-run, bounded local execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.28 static/mock applied evidence generation readiness review.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define readiness summary.
- [x] Define required readiness inputs.
- [x] Define static/mock generation readiness criteria.
- [x] Define private-first generation posture.
- [x] Define public-safe promotion criteria.
- [x] Define blocker categories.
- [x] Define minimum generated package candidate.
- [x] Define generation sequence.
- [x] Define structural validator readiness relationship.
- [x] Define reviewer review requirement.
- [x] Define diagnostic system timing.
- [x] Preserve runtime/scanning and public/private boundaries.

## Non-goals

- Generate static/mock evidence packages.
- Generate scenario fixtures.
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
