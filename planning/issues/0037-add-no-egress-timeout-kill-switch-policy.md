# 0037: Add no-egress, timeout, and kill-switch policy scaffold

## Status

In Progress

## Priority

P0

## Type

Runtime Safety / Policy Scaffold

## Background

The project now has a local-only execution plan review object.

Before any future local runtime execution can be considered, the project should define safety policies for no-egress, timeout, and kill-switch behavior.

## Decision Summary

Add no-egress, timeout, and kill-switch policy scaffold.

The policy defines future requirements but keeps execution disabled.

## Acceptance Criteria

- runtime safety policy module is added
- runtime safety policy generator is added
- policy binds to local-only execution plan
- no-egress requirement is true
- no-egress policy is defined
- denied destination categories include public internet and customer networks
- timeout requirement is true
- timeout policy is defined
- kill-switch requirement is true
- kill-switch policy is defined
- process tree termination is required
- evidence requirement remains true
- sanitizer requirement remains true
- human approval requirement remains true
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

- docs/44-no-egress-timeout-kill-switch-policy.md
- docs/43-local-only-execution-plan-review.md
- planning/decisions/ADR-0038-add-no-egress-timeout-kill-switch-policy.md
