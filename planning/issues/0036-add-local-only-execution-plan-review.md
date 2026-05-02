# 0036: Add local-only execution plan review

## Status

In Progress

## Priority

P0

## Type

Execution Plan / Review Control

## Background

The project now has a bounded execution transition candidate.

Before any local-only runtime behavior can be designed, the platform should define a local-only execution plan review object that remains non-executing.

## Decision Summary

Add local-only execution plan review.

The plan permits only `runtime_detection` and `health_check_plan_only` as plan-level operations. All actual runtime operations remain prohibited.

## Acceptance Criteria

- local execution plan module is added
- local execution plan generator is added
- plan binds to bounded execution transition candidate
- allowed plan operations are restricted to runtime_detection and health_check_plan_only
- active_scan/spider/ajax_spider/authenticated_crawl are prohibited
- ZAP start/stop/API calls are prohibited
- execution plan review remains required
- human approval remains required
- no-egress requirement remains true
- timeout requirement remains true
- kill-switch requirement remains true
- evidence requirement remains true
- scan execution remains false
- network activity remains false
- real execution remains false
- external process execution remains false
- credential injection remains false
- raw artifact capture remains false
- customer target remains false
- external network target remains false
- local checks pass

## Related Documents

- docs/43-local-only-execution-plan-review.md
- docs/42-bounded-execution-transition-candidate.md
- planning/decisions/ADR-0037-add-local-only-execution-plan-review.md
