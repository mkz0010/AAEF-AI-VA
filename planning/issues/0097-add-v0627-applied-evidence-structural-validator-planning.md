# Issue 0097: Add v0.6.27 applied evidence structural validator planning

Status: Completed by v0.6.27 candidate  
Type: v0.6.27 planning / applied evidence structural validator

## Goal

Define applied evidence structural validator planning before implementing validators,
generating fixtures, generating evidence packages, running local diagnostic tools,
creating runnable Compose configuration, image pull, container startup, port binding,
dry-run, bounded local execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.27 applied evidence structural validator planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define validator input boundary.
- [x] Define validator output boundary.
- [x] Define required artifact presence checks.
- [x] Define required field checks.
- [x] Define identifier linkage checks.
- [x] Define scenario consistency checks.
- [x] Define contradiction checks.
- [x] Define non-execution evidence checks.
- [x] Define reviewer walkthrough coverage checks.
- [x] Define non-proof statement checks.
- [x] Define overclaim prevention checks.
- [x] Define failure category planning.
- [x] Preserve runtime/scanning and public/private boundaries.

## Non-goals

- Implement structural validators.
- Execute validator checks.
- Generate evidence packages.
- Generate scenario fixtures.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
