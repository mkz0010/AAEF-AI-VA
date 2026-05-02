# ADR-0010: Use a standard-library mock runner before integrating real tools

## Status

Accepted

## Context

The Tool Gateway is a trusted control boundary. Integrating real tools too early could make it harder to validate the control model and could introduce unnecessary environmental complexity.

The project needs a minimal executable prototype that proves request/authorization/result/evidence linkage first.

## Decision

Implement a standard-library-only Tool Gateway mock runner before integrating real tools.

The mock runner will not run ZAP, Nmap, nuclei, Burp Suite, or Nessus.

It will consume existing example contract flows and generate mock execution and evidence outputs.

## Rationale

This allows the project to validate:

- request/decision binding,
- allow / deny / require_human_approval behavior,
- credential_ref as reference-only,
- fail-closed assumptions,
- evidence linkage,
- local ignored output behavior.

## Consequences

- No additional Python dependencies are required.
- The prototype remains safe and easy to run.
- Real tool adapters can be added after the control flow is proven.
- Generated outputs must stay under ignored local directories.
