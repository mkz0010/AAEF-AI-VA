# Licensing, Trademark, Authorship, and Commercial-Use Protection Checkpoint

Version: v0.5.3 candidate  
Status: public protection hardening; does not authorize runtime execution

## Purpose

This checkpoint strengthens the public repository boundary for commercial adoption.

It adds public documents for:

- notice and attribution,
- authorship,
- copyright notice,
- commercial licensing discussion boundary,
- project-name and trademark-like usage boundary,
- contribution rules.

These documents are intended to improve project clarity, reduce confusion, support
commercial discussions, and preserve safety boundaries.

They are not legal advice.

## Added public protection files

| File | Purpose |
| --- | --- |
| `NOTICE` | Public notice, attribution, and safety-boundary summary |
| `AUTHORS` | Project author and parent framework attribution |
| `COPYRIGHT` | Copyright notice and parent framework attribution |
| `COMMERCIAL-LICENSE.md` | Commercial licensing discussion boundary |
| `TRADEMARKS.md` | Project-name and mark usage policy |
| `CONTRIBUTING.md` | Contribution rules and safety boundaries |

## Commercial protection goals

This checkpoint supports the commercial strategy by making these boundaries explicit:

- AGPL-3.0 remains the public code license.
- Separate commercial licensing may be discussed.
- No commercial license is granted without a separate written agreement.
- Commercial inquiries are separate from vulnerability reports.
- Commercial inquiries do not authorize runtime execution or scanning.
- Pricing, customer lists, proposal drafts, and negotiation notes remain private.
- Service-provider, MSSP, consulting, and managed-service use require careful review.

## Authorship and attribution goals

The checkpoint records:

- project author attribution,
- parent AAEF attribution,
- parent AAEF repository link,
- parent AAEF CC BY 4.0 attribution,
- AAEF-AI-VA AGPL-3.0 code license.

## Project-name usage goals

The checkpoint records project-name usage boundaries for:

- `AAEF-AI-VA`,
- `AAEF-controlled AI Vulnerability Assessment`,
- `AI output is not authority`,
- `Model output is not authority`.

The project does not claim registered trademark status unless separately registered
and documented.

The policy focuses on avoiding confusion, false endorsement, false certification,
or false production-readiness claims.

## Contribution protection goals

Contribution rules clarify that pull requests, issues, forks, and discussions do not
create:

- commercial licenses,
- partnerships,
- support agreements,
- endorsements,
- managed-service approvals.

Contribution rules also keep high-risk changes under explicit review.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

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

## Compatibility note

Commercial license negative-boundary statements must not be treated as forbidden positive claims. For example, `No separate commercial license is granted unless a separate written agreement...` is an intended no-implied-grant boundary, not a commercial-license grant.

`CONTRIBUTING.md` must preserve the exact phrase `commercial license` because the protection test treats that wording as a compatibility phrase.

`NOTICE` must preserve the exact phrase `commercial licensing inquiries` because the
licensing, trademark, authorship, and commercial-use protection test treats that
wording as a compatibility phrase.

## Required local checks

Before tagging v0.5.3, verify:

1. README links to the protection documents.
2. NOTICE exists and records license, parent framework, and safety boundary.
3. AUTHORS exists and records project author and parent attribution.
4. COPYRIGHT exists and records copyright and parent attribution.
5. COMMERCIAL-LICENSE.md exists and states no commercial license is granted without separate written agreement.
6. TRADEMARKS.md exists and avoids registered trademark overclaiming.
7. CONTRIBUTING.md exists and preserves safety, license, security, and commercial boundaries.
8. Runtime and scanning boundaries remain disabled.
9. `tools/run_all_local_checks.py` includes the protection test.

## Out of scope

This checkpoint does not:

- register a trademark,
- create a commercial contract,
- define final commercial license terms,
- publish pricing,
- publish customer target lists,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
