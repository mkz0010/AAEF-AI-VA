# Safe Mock Demo Public Artifact

Status: promoted public artifact, not publication approval  
Version introduced: v0.6.301  
Scope: safe mock demo path only

## What this artifact is

This public artifact explains the safe mock demo path for reviewers.

It is intended to show how the AAEF-AI-VA prototype separates AI-requested actions from gate-decided execution outcomes in a safe mock setting.

## What this artifact is not

- not a live scanner
- not runtime demo readiness
- not scanner readiness
- not execution authorization
- not real execution permission
- not publication approval
- not public announcement
- not production readiness
- not certification
- not legal compliance
- not audit opinion
- not diagnostic completeness

## Safe mock command example

~~~bash
py tools/run_tool_gateway_example.py all
~~~

Expected safe mock statuses:

~~~text
allowed-action: completed
denied-action: blocked
human-approval-required: requires_human_approval
~~~

## Private artifact boundary

Generated outputs remain under `private-not-in-git`.

No private generated outputs are moved public in v0.6.301.

This public artifact does not include customer data, target data, live scanner outputs, runtime execution authorization, credentials, or private generated evidence.

## Boundary statements

- Model output is not authority.
- AI rationale is not authorization.
- A gate decision is not AI self-approval.
- Evidence supports reconstruction; it does not prove legal truth.
- safe mock demo is not live scanner execution
- real scanner execution remains blocked

## Current blocked runtime posture

~~~text
runtime readiness status: not_detected_execution_blocked
target lab gate status: target_defined_execution_blocked
binding gate status: bound_execution_blocked
transition gate status: candidate_recorded_execution_blocked
execution authorized: False
real execution permitted: False
~~~
