# Issue 0091: Add v0.6.21 static fixture validator required-node check planning

Status: Completed by v0.6.21 candidate  
Type: v0.6.21 planning / static fixture validator required-node checks

## Goal

Define required-node check planning before implementing required-node checks, complete
fixture schemas, complete validators, negative tests, generated fixtures, runnable
Compose configuration, image pull, container startup, port binding, dry-run, bounded
local execution, or scanner work.

## Acceptance criteria

- [x] Add v0.6.21 static fixture validator required-node check planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record public-safe design boundary.
- [x] Record required-node planning posture.
- [x] Record planned manifest expectation.
- [x] Record required fixture node set.
- [x] Record missing-node failure planning.
- [x] Record review-only result planning.
- [x] Record fail-closed behavior planning.
- [x] Record read-only implementation boundary.
- [x] Record future implementation sequence.
- [x] Record negative test planning.
- [x] Confirm required-node check implementation, complete validator implementation, negative test implementation, fixture generation, Compose file creation, image pull, Docker execution, port binding, runtime execution, scanning, and delivery authorization remain disabled.

## Non-goals

- Implement required-node checks.
- Implement complete fixture schemas.
- Implement complete fixture validators.
- Implement negative tests.
- Generate fixture files.
- Commit sample fixture artifacts.
- Install Docker.
- Run Docker.
- Pull images.
- Start containers.
- Bind ports.
- Create Docker Compose files.
- Build a local lab.
- Enable runtime execution.
- Enable scanning.
- Authorize report delivery.
- Expose private advanced feature details.
