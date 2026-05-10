# ADR-0210: Add v0.6.140 mock/dry-run completed status terminology cleanup candidate

Status: Accepted
Date: 2026-05-10

## Context

v0.6.139 selected mock/dry-run `completed` status terminology cleanup as a Medium-risk work item and assigned two checkpoints.

## Decision

Add a reviewer-facing terminology helper and tests for disambiguating mock/dry-run `completed` status records.

The helper preserves raw status values and adds reviewer-facing terminology such as `mock_dry_run_completed_no_real_execution` when a completed record is clearly mock, dry-run, or explicitly no-real-execution.

## Consequences

v0.6.141 should review the candidate terminology behavior and decide whether to close the work item.

No runtime execution, scanner execution, Docker execution, credential injection, customer target, delivery authorization, AAEF main issue, or AAEF main PR is authorized by this candidate.
