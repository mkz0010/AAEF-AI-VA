# ADR-0014: Add Tool Gateway adapter stubs before real tool integration

## Status

Accepted

## Context

The Tool Gateway mock runner currently validates request, authorization, credential_ref, and evidence linkage.

Before integrating real tools such as ZAP, Nmap, nuclei, Burp Suite, or Nessus, the project needs a narrow adapter boundary.

## Decision

Add adapter stubs for:

- ZAP,
- Nmap,
- nuclei,
- browser automation.

The adapters will expose only approved operations and will not execute real tools yet.

## Rationale

Adapter stubs allow the project to validate routing and fail-closed behavior before introducing environmental complexity.

They also prevent a future design where Tool Gateway becomes a generic shell wrapper.

## Consequences

- Tool Gateway now routes completed mock actions through an adapter registry.
- Unsupported operations fail closed at the adapter layer.
- Future real tool integrations must preserve the same narrow adapter model.
- Local checks now include adapter tests.
