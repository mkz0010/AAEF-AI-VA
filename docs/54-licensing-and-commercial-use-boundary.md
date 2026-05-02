# Licensing and Commercial-Use Boundary

AAEF-AI-VA adopts the GNU Affero General Public License v3.0 (AGPL-3.0) for the code implementation.

This document records the licensing and commercial-use boundary for the AAEF-AI-VA project. It is a project planning and governance note, not legal advice.

## Decision

AAEF-AI-VA code is licensed under AGPL-3.0.

The parent Agentic Authority & Evidence Framework (AAEF) framework/specification remains licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

AAEF-AI-VA is a separate code implementation project that builds on AAEF concepts and documentation. AAEF attribution must be preserved in the README and related documentation.

## Commercial-use boundary

Organizations that want to embed, operate, modify, or provide AAEF-AI-VA in a manner that is not compatible with AGPL-3.0 may request a separate commercial license from the author.

This supports a dual-track model:

- public AGPL-3.0 code for transparency, review, and trust-building;
- separate commercial licensing for organizations that need proprietary embedding, managed-service use, private modifications, or contractual terms not provided by AGPL-3.0.

The commercial license is not defined by this repository. It must be handled through a separate agreement.

## AAEF attribution boundary

AAEF-AI-VA must clearly state that it builds on AAEF and must preserve AAEF attribution.

Minimum attribution language:

> This project builds on concepts and documentation from the Agentic Authority & Evidence Framework (AAEF), licensed under Creative Commons Attribution 4.0 International (CC BY 4.0).

## Non-goals

This licensing boundary does not:

- change any runtime execution gate;
- authorize network activity;
- authorize external process execution;
- authorize scanning;
- authorize credential injection;
- authorize raw artifact capture;
- satisfy preflight checks;
- create a certification scheme, legal compliance claim, audit opinion, or conformity assessment.

## Safety invariants

The following safety state remains unchanged:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Future commercial-readiness tasks

Before public commercial use, the project should still define or review:

- commercial licensing contact information;
- third-party dependency license compatibility;
- contributor terms, CLA, or equivalent contribution policy if external contributors are accepted;
- whether source files should include SPDX headers;
- whether a separate `COMMERCIAL.md` or `LICENSING.md` should be added;
- whether a lawyer should review the public README and commercial licensing workflow.

## Review status

This document records the v0.3.5 licensing and commercial-use boundary. It does not by itself create a commercial contract.
