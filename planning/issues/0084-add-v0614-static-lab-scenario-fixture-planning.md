# Issue 0084: Add v0.6.14 static lab scenario fixture planning

Status: Completed by v0.6.14 candidate  
Type: v0.6.14 planning / static lab scenario fixtures

## Goal

Define static, non-executing lab scenario fixture planning before generating fixture
files, creating runnable Compose configuration, image pull, container startup, port
binding, dry-run, bounded local execution, or scanner work expands.

## Acceptance criteria

- [x] Add v0.6.14 static lab scenario fixture planning.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record public-safe design boundary.
- [x] Record fixture set model.
- [x] Record fixture manifest model.
- [x] Record fixture node status model.
- [x] Record candidate-to-sketch linkage.
- [x] Record AI request fixture boundary.
- [x] Record gate decision fixture boundary.
- [x] Record expected evidence fixture boundary.
- [x] Confirm fixture generation, Compose file creation, image pull, Docker execution, port binding, runtime execution, scanning, and delivery authorization remain disabled.

## Non-goals

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
