# ADR-0190: Add v0.6.120 checkpoint granularity policy decision record

Status: Accepted
Date: 2026-05-10

## Context

The recent AAEF main handback sequence used a highly conservative checkpoint pattern. That pattern was useful for first-time public-safe handback exploration, but it is too heavy as a default for every decision.

## Decision

Adopt a risk-tiered checkpoint granularity policy.

Low-risk operational policy decisions normally complete in one checkpoint. Medium-risk public-facing material normally uses two checkpoints. High-risk validator/schema/fixture/public-sample changes normally use three checkpoints. Critical-risk runtime, scanner, Docker, credential, customer, delivery, or actual external submission work may continue using four to five checkpoints.

v0.6.120 intentionally completes this low-risk policy decision in one checkpoint as the first application of the policy.

## Consequences

Future work should explicitly select a risk tier and checkpoint count. Existing checkpoints, tags, and release history are not rewritten.
