# README Public English Wording Cleanup

Version: v0.4.2 candidate  
Status: public README wording cleanup; does not authorize runtime execution

## Purpose

This checkpoint cleans up README wording for public repository presentation.

The repository is intended to be English-first. Internal Japanese wording that was
useful during local development should not appear in the public-facing README.

## Cleanup scope

This checkpoint updates README wording to avoid:

- local-only management phrasing,
- Japanese public-facing sentences,
- ambiguity between AI output and authority to perform assessment actions,
- wording that could imply the repository itself authorizes live scanning.

## Preferred public wording

The README should use this English positioning:

~~~text
A safety-first reference implementation for AI-assisted vulnerability assessment control boundaries.
~~~

The README should also preserve the core authority boundary:

~~~text
AI output is not authority to perform assessment actions.
AI may request assessment actions, but execution is decided by the AAEF Authorization Gateway, Tool Gateway, contractual scope, and human review.
~~~

## English-first repository posture

AAEF-AI-VA may have Japanese planning conversations and local development history,
but the public repository should be readable primarily in English.

This does not prohibit future Japanese companion materials. It only keeps the main
repository README English-first for public review, adoption, and commercial
evaluation.

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

## Required local checks

Before tagging v0.4.2, verify:

1. README uses English-first public wording.
2. README does not contain the Japanese local-management sentence.
3. README does not contain the Japanese AI authority statement.
4. README includes the English AI authority boundary.
5. README still links to license, security, publication readiness, and CI materials.
6. `tools/run_all_local_checks.py` includes the README wording validation test.
7. Runtime execution remains disabled.

## Out of scope

This checkpoint does not:

- rewrite all documentation into English
- create a Japanese README
- change repository visibility
- push code to GitHub
- create a GitHub release
- authorize runtime execution
- authorize scanning, external network testing, credential injection, or customer-target testing
