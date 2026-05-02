# ADR-0059: Add GitHub release publication checkpoint

Status: Accepted  
Date: 2026-05-03

## Context

AAEF-AI-VA is public on GitHub and the public launch state has been recorded in
v0.4.4. The project then added public release notes and launch announcement material
in v0.4.5.

After that, a GitHub Release was manually created for `v0.4.5`.

The release publication state should be recorded in source control so that the first
GitHub Release publication posture is auditable later.

## Decision

Add a v0.4.6 GitHub Release publication checkpoint.

The checkpoint records:

- `v0.4.5` release tag,
- release title,
- release URL,
- Latest release status,
- release notes source path,
- release note safety boundaries,
- continued runtime-execution prohibition.

## Consequences

Positive:

- The first GitHub Release publication state is auditable from the repository.
- Release communication boundaries are preserved in versioned documentation.
- Release publication is explicitly separated from runtime readiness.

Negative / deferred:

- This does not create or edit the GitHub Release.
- This does not publish social announcements.
- This does not finalize commercial contact or security contact channels.
- This does not authorize runtime execution.
