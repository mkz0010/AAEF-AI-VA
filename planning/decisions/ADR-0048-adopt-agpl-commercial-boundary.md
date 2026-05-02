# ADR-0048: Adopt AGPL-3.0 and commercial-use boundary

## Status

Accepted for v0.3.5.

## Context

AAEF-AI-VA is moving toward possible OSS publication and commercial positioning as an AI-assisted vulnerability assessment control platform.

The parent AAEF framework/specification is licensed under CC BY 4.0. AAEF-AI-VA is a code implementation project and therefore needs a software license appropriate for source code, network-service use, and commercial licensing discussions.

## Decision

Adopt GNU Affero General Public License v3.0 (AGPL-3.0) for the AAEF-AI-VA code repository.

Record a commercial-use boundary stating that organizations needing terms incompatible with AGPL-3.0 may request a separate commercial license from the author.

Preserve AAEF attribution and clarify that AAEF itself remains CC BY 4.0.

## Rationale

AGPL-3.0 supports public review and transparency while preserving leverage for commercial licensing discussions where a company wants proprietary embedding, managed-service use, or private modifications outside the AGPL-3.0 path.

This is especially relevant because AAEF-AI-VA is intended to be a security control and evidence platform rather than only a permissive developer library.

## Consequences

Positive:

- the repository has a clear software license;
- public review remains possible;
- commercial licensing can be discussed without changing the public license;
- the parent AAEF attribution boundary is explicit.

Tradeoffs:

- some organizations may avoid AGPL-3.0 code unless a commercial license is available;
- dependency compatibility must be reviewed carefully;
- external contributions may require CLA or equivalent contributor terms if commercial dual licensing is intended.

## Non-goals

This ADR does not authorize runtime execution and does not change preflight, authorization, network, scan, credential, or artifact-capture safety gates.
