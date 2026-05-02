# 0018: Add scope registry and target alias resolution

## Status

In Progress

## Priority

P0

## Type

Control / Prototype

## Background

The project needs a controlled mapping between AI-visible `target_id` aliases and future executor-visible destinations.

Without a scope registry, `target_id` could become an ambiguous string and future real tool integration could accidentally allow scope expansion or raw destination leakage.

## Decision Summary

Add a Tool Gateway scope registry with fictitious demo targets.

The ZAP command plan includes a resolved target binding.

The controlled executor validates the target binding but still performs no real execution.

## Acceptance Criteria

- scope registry file is added
- scope registry resolver is added
- allowed target resolution succeeds
- missing target fails closed
- wrong scope fails closed
- wrong tool fails closed
- wrong operation fails closed
- denied target fails closed
- raw destination inclusion fails closed
- ZAP command plan includes target binding
- controlled executor validates target binding
- local checks pass

## Related Documents

- docs/25-scope-registry-target-alias-resolution.md
- docs/24-controlled-executor-policy.md
- docs/23-zap-adapter-command-plan.md
- planning/decisions/ADR-0019-add-scope-registry-target-alias-resolution.md
