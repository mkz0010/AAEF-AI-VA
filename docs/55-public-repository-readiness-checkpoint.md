# Public Repository Readiness Checkpoint

Version: v0.3.6 candidate  
Status: publication-readiness checkpoint; does not authorize runtime execution

## Purpose

This document records the repository-level checks that should be satisfied before the
AAEF-AI-VA implementation is published as a public repository.

This checkpoint is intentionally separate from runtime readiness.

A repository can be ready for public review while still being blocked from:

- runtime execution
- external network activity
- scan execution
- credential injection
- raw artifact capture
- customer target operation

## Current publication posture

AAEF-AI-VA is prepared as a local-first implementation project.

The repository can move toward public publication only after the following boundaries
are visible and locally validated:

| Boundary | Expected state |
| --- | --- |
| Code license | AGPL-3.0 recorded in `LICENSE` |
| Framework attribution | AAEF / CC BY 4.0 attribution recorded in README and docs |
| Commercial licensing | Commercial inquiry placeholder recorded, durable contact still pending |
| Runtime execution | Disabled |
| External network activity | Disabled |
| Scan execution | Disabled |
| Credential injection | Disabled |
| Raw artifact capture | Disabled |
| Private/generated artifacts | Kept under `private-not-in-git/` |
| Public-readiness validation | Local check present and included in `tools/run_all_local_checks.py` |

## Publication readiness is not execution readiness

This checkpoint does not change any runtime authorization boundary.

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

## Required repository checks before public release

Before creating or pushing a public repository, verify:

1. `LICENSE` exists and records AGPL-3.0.
2. `README.md` contains the license section and AAEF attribution.
3. README states that separate commercial licensing may be available.
4. The commercial contact remains a placeholder or is replaced with a durable contact.
5. `private-not-in-git/` is not intended for repository publication.
6. Generated private artifacts remain outside tracked source artifacts.
7. Local validation passes with `tools/run_all_local_checks.py`.
8. No runtime execution readiness language is introduced by publication wording.
9. No public text implies that scans, ZAP execution, external process execution, or network activity are allowed.
10. Public documentation distinguishes:
    - open-source code license,
    - AAEF framework attribution,
    - commercial licensing path,
    - runtime/execution safety boundary.

## Suggested first-publication sequence

~~~bash
cd /e/AAEF-AI-VA

py tools/run_all_local_checks.py
git status
git log --oneline --decorate -10
~~~

Only after the repository is clean and checks pass should the author create a
remote repository and decide what to publish.

## Out of scope

This checkpoint does not:

- create a GitHub repository
- push code to a remote
- authorize live scanning
- configure ZAP
- perform external network access
- define commercial license terms
- replace legal review
- approve third-party dependency use

## Follow-up candidates

- Define durable commercial contact channel.
- Add dependency/license inventory.
- Add `.gitignore` review for generated/private artifacts.
- Add public security policy and vulnerability disclosure channel.
- Add first-publication checklist for GitHub repository settings.
