# Issue 0094: Add v0.6.24 applied evidence scenario set planning

Status: Completed by v0.6.24 candidate  
Type: v0.6.24 planning / applied evidence scenarios

## Goal

Define the four minimum applied evidence scenarios before generating fixtures,
generating evidence packages, running local diagnostic tools, creating runnable Compose
configuration, image pull, container startup, port binding, dry-run, bounded local
execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.24 applied evidence scenario set planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define the minimum scenario set.
- [x] Define common artifact chain.
- [x] Define common scenario fields.
- [x] Define permitted safe diagnostic scenario.
- [x] Define denied out-of-scope request scenario.
- [x] Define human approval required scenario.
- [x] Define not-executed / expired scenario.
- [x] Define scenario outcome matrix.
- [x] Define scenario-to-AAEF mapping.
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
