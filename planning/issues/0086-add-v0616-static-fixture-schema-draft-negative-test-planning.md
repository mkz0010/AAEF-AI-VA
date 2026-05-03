# Issue 0086: Add v0.6.16 static fixture schema draft and negative test planning

Status: Completed by v0.6.16 candidate  
Type: v0.6.16 planning / static fixture schema draft / negative tests

## Goal

Define static fixture schema draft fields and negative test expectations before
implementing fixture schemas, implementing validators, generating fixture files,
creating runnable Compose configuration, image pull, container startup, port binding,
dry-run, bounded local execution, or scanner work expands.

## Acceptance criteria

- [x] Add v0.6.16 static fixture schema draft and negative test planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record public-safe design boundary.
- [x] Record schema draft posture.
- [x] Record fixture manifest draft fields.
- [x] Record node envelope draft fields.
- [x] Record required node draft fields.
- [x] Record scenario trace draft rules.
- [x] Record negative test planning scope.
- [x] Record missing-node negative test planning.
- [x] Record broken-reference negative test planning.
- [x] Record runtime-implication negative test planning.
- [x] Record runnable-configuration negative test planning.
- [x] Record secret-like and customer-like negative test planning.
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
