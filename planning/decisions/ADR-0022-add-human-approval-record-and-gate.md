# ADR-0022: Add human approval record and approval gate without enabling real execution

## Status

Accepted

## Context

The project now has operator readiness review summaries. Operators need a way to record an approval decision, rejection, request for more information, or decision to keep execution blocked.

However, human approval alone must not bypass readiness gates, executor policy, scope binding, credential policy, artifact policy, or evidence requirements.

## Decision

Add a human approval record and approval gate.

The approval record binds a decision to command plan ID, tool, operation, target ID, scope ID, approval scope, expiration, and evidence requirement.

In the current MVP, `real_execution_allowed` must remain false even when the decision is `approved`.

## Consequences

- Human decisions become explicit review artifacts.
- Approval binding can be tested.
- Approval expiration can be enforced.
- Approval cannot bypass real execution readiness controls.
- The project moves closer to auditable review workflow without enabling real execution.
