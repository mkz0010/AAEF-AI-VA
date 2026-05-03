# Issue 0087: Add v0.6.17 static fixture validator scaffold planning

Status: Completed by v0.6.17 candidate  
Type: v0.6.17 planning / static fixture validator scaffold

## Goal

Define static fixture validator scaffold responsibilities before implementing fixture schemas, implementing validators, implementing negative tests, generating fixture files, creating runnable Compose configuration, image pull, container startup, port binding, dry-run, bounded local execution, or scanner work expands.

## Acceptance criteria

- [x] Add v0.6.17 static fixture validator scaffold planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record public-safe design boundary.
- [x] Record validator scaffold posture.
- [x] Record scaffold responsibility model.
- [x] Record validator input boundary.
- [x] Record validator output boundary.
- [x] Record planned validation stages.
- [x] Record fail-closed behavior planning.
- [x] Record failure category model.
- [x] Record negative-test handling planning.
- [x] Record future implementation order.
- [x] Confirm fixture schema implementation, validator implementation, negative test implementation, fixture generation, Compose file creation, image pull, Docker execution, port binding, runtime execution, scanning, and delivery authorization remain disabled.

## Non-goals

- Implement fixture schemas.
- Implement fixture validators.
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
