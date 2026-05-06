# Issue 0093: Add v0.6.23 AAEF applied evidence package design

Status: Completed by v0.6.23 candidate  
Type: v0.6.23 design / AAEF applied evidence package

## Goal

Define the AAEF applied evidence package structure before generating evidence
artifacts, implementing scenario fixtures, running local diagnostic tools, creating
runnable Compose configuration, image pull, container startup, port binding, dry-run,
bounded local execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.23 AAEF applied evidence package design.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Define package manifest design.
- [x] Define required artifact chain.
- [x] Define `tool_action_request` design.
- [x] Define `gate_decision` design.
- [x] Define `dispatch_decision` design.
- [x] Define execution and non-execution result design.
- [x] Define evidence event design.
- [x] Define review summary design.
- [x] Define minimum scenario package set.
- [x] Clarify diagnostic system build timing.
- [x] Preserve public/private and runtime/scanning boundaries.

## Non-goals

- Generate evidence packages.
- Generate fixture files.
- Build a local diagnostic system.
- Run Docker.
- Run scanners.
- Pull images.
- Start containers.
- Bind ports.
- Enable runtime execution.
- Authorize report delivery.
- Expose private advanced feature details.
