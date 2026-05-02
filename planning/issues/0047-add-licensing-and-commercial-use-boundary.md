# 0047: Add licensing and commercial-use boundary

## Goal

Add the initial licensing and commercial-use boundary for AAEF-AI-VA.

## Scope

- Add AGPL-3.0 LICENSE text.
- Add README license section.
- Record AAEF attribution and CC BY 4.0 boundary.
- Add a licensing and commercial-use boundary document.
- Add an ADR for the AGPL-3.0 decision.
- Add local validation for the license boundary.

## Acceptance criteria

- `LICENSE` contains AGPL-3.0 text.
- `README.md` states AGPL-3.0 for AAEF-AI-VA.
- `README.md` attributes AAEF and states CC BY 4.0 for the parent framework/specification.
- Documentation records that commercial licensing is handled separately.
- Documentation records that this change does not authorize runtime execution.
- Local checks pass.

## Safety boundary

This issue does not change execution safety state. Runtime execution remains blocked.
