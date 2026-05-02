# README Public Baseline and Commercial Entrypoint Cleanup

Version: v0.5.1 candidate  
Status: README public presentation cleanup; does not authorize runtime execution

## Purpose

This checkpoint updates the README so the public repository entry point reflects the
current state of AAEF-AI-VA after public launch, GitHub Release publication, and
commercial adoption preparation.

The README should no longer lead with older implementation checkpoints or
local-only/private-first wording. It should present the current public baseline,
safety boundary, release state, validation posture, and commercial adoption
entrypoint clearly.

## Cleanup goals

The README is updated to:

- present the current public baseline near the top,
- make the authority boundary readable,
- separate "what this is" from "what this is not",
- show the commercial adoption entrypoint without turning the README into a sales deck,
- preserve AGPL-3.0, SECURITY.md, GitHub Actions, release, and checkpoint links,
- remove obsolete local-first/private-by-default presentation from the public entry point,
- avoid making v0.3.x implementation details look like the current front-door baseline.

## Required public baseline

The README should identify:

- repository URL,
- public visibility,
- latest repository checkpoint,
- latest GitHub Release,
- AGPL-3.0 license,
- SECURITY.md,
- private vulnerability reporting,
- GitHub Actions workflow,
- runtime execution disabled,
- live scanning not authorized,
- customer-target operation not authorized.

## Authority boundary

The README should preserve this wording:

~~~text
AI output is not authority to perform assessment actions.

AI may request assessment actions, but execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual scope, and human review.
~~~

The two sentences must remain separated so the README does not render them as a
single jammed sentence.

## Commercial entrypoint

The README should make the commercial path visible but controlled:

- advisory workshop,
- controlled internal PoC design,
- architecture review,
- integration support,
- commercial license discussion.

Commercial adoption wording must remain separate from vulnerability reporting and
must not authorize runtime execution, scanning, credential injection, or customer
target operation.

## Runtime and scanning boundary

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

## README compatibility note

The README is a public entry point, but earlier checkpoint tests also use it as a
stable compatibility surface.

When rewriting README, preserve compatibility phrases expected by earlier tests, or
update those tests so that they distinguish between:

- forbidden positive claims, and
- explicit negative boundary statements such as "this is not an autonomous vulnerability scanner."

This prevents future README cleanups from failing because a prohibited claim is
listed in a "What this is not" or "Claims to avoid" section.

The metadata announcement pack test should follow the same rule: `tools/test_public_facing_repository_metadata_announcement_pack.py` must not reject negative boundary statements such as `not an autonomous vulnerability scanner`.

## Required local checks

Before tagging v0.5.1, verify:

1. README starts with the current public baseline, not an old v0.3.x checkpoint.
2. README does not contain obsolete local-first/private-by-default wording.
3. README keeps the AI authority boundary readable.
4. README includes "What this is" and "What this is not".
5. README includes a commercial adoption entrypoint.
6. README links to license, security, CI, release, launch, and commercial adoption materials.
7. Runtime and scanning boundaries remain disabled.
8. `tools/run_all_local_checks.py` includes the README public baseline cleanup test.

## Out of scope

This checkpoint does not:

- rewrite all repository docs,
- change repository visibility,
- create or edit a GitHub Release,
- publish an announcement,
- define final commercial contract terms,
- provide legal advice,
- authorize runtime execution,
- authorize scan execution,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
