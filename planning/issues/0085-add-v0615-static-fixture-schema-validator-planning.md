# Issue 0085: Add v0.6.15 static fixture schema and validator planning

Status: Completed by v0.6.15 candidate  
Type: v0.6.15 planning / static fixture schema / validator planning

## Goal

Define static fixture schema and validator planning before generating fixture files,
implementing fixture validators, creating runnable Compose configuration, image pull,
container startup, port binding, dry-run, bounded local execution, or scanner work
expands.

## Acceptance criteria

- [x] Add v0.6.15 static fixture schema and validator planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record public-safe design boundary.
- [x] Record fixture schema planning scope.
- [x] Record fixture manifest schema planning.
- [x] Record fixture node schema planning.
- [x] Record required fixture node types.
- [x] Record scenario trace validation planning.
- [x] Record synthetic data validation planning.
- [x] Record no-secret validation planning.
- [x] Record no-runtime validation planning.
- [x] Record no-runnable-configuration validation planning.
- [x] Confirm fixture schema implementation, validator implementation, fixture generation, Compose file creation, image pull, Docker execution, port binding, runtime execution, scanning, and delivery authorization remain disabled.

## Non-goals

- Implement fixture schemas.
- Implement fixture validators.
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
