# Issue 0095: Add v0.6.25 static applied evidence fixture planning

Status: Completed by v0.6.25 candidate  
Type: v0.6.25 planning / static applied evidence fixtures

## Goal

Define the static fixture artifacts for each applied evidence scenario before
generating fixtures, generating evidence packages, running local diagnostic tools,
creating runnable Compose configuration, image pull, container startup, port binding,
dry-run, bounded local execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.25 static applied evidence fixture planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define planned fixture root.
- [x] Define common fixture artifact set.
- [x] Define common identifier linkage.
- [x] Define per-artifact fixture planning.
- [x] Define per-scenario fixture plans for all four minimum scenarios.
- [x] Define fixture-to-AAEF five questions planning.
- [x] Define future static fixture generation readiness.
- [x] Define structural validator planning hooks.
- [x] Preserve runtime/scanning and public/private boundaries.

## Non-goals

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
