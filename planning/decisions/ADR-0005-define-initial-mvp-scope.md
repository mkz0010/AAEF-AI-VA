# ADR-0005: Define initial MVP scope around controlled Web/API/NW assessment assistance

## Status

Accepted

## Context

The project could expand into many forms of AI-assisted security testing, including Web assessment, API assessment, network vulnerability assessment, Burp automation, Nessus integration, exploit validation, source code review, cloud configuration review, and autonomous penetration testing.

Attempting to cover too much in the first MVP would increase safety, legal, technical, and implementation risk.

## Decision

The initial MVP will focus on controlled assistance for:

- Web application vulnerability assessment,
- API vulnerability assessment,
- small-scale network vulnerability assessment.

The first tool integrations will be limited to:

- OWASP ZAP,
- Nmap,
- nuclei,
- simple browser automation where necessary.

Burp Suite, Nessus / Tenable, cloud posture tools, advanced browser automation, and custom exploit validation scripts are deferred.

The MVP will prioritize validating the control model over maximizing vulnerability discovery.

## Rationale

The most important early proof is not that AI can find every vulnerability.

The most important early proof is that AI-assisted diagnostic actions can be constrained by:

- explicit scope,
- authorization decisions,
- Tool Gateway mediation,
- credential_ref-based secret handling,
- evidence capture,
- output sanitization,
- human review.

## Consequences

- The MVP remains small enough to build and reason about.
- Safety controls can be tested before adding high-risk tooling.
- Burp and Nessus can be added later with stronger gateway patterns.
- The project can produce a clear demo scenario for partners and buyers.
- The project avoids prematurely claiming fully autonomous penetration testing capability.
