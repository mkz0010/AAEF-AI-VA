# Tool Gateway Adapter Stubs

## Purpose

This document describes the initial Tool Gateway adapter stub layer.

The adapter layer prepares the prototype for future ZAP, Nmap, nuclei, and browser automation integration without executing real tools yet.

## Design Position

Tool Gateway should not directly construct arbitrary commands.

Instead, it should route approved actions through narrow adapter interfaces.

This keeps the execution boundary explicit and prevents AI-generated requests from becoming unrestricted command execution.

## Adapter Registry

The initial registry contains:

- `zap`
- `nmap`
- `nuclei`
- `browser`

## Adapter Operations

| Adapter | Allowed Operations |
|---|---|
| zap | passive_scan, authenticated_crawl |
| nmap | safe_port_discovery, service_version_detection |
| nuclei | safe_template_scan |
| browser | safe_login_check |

## Current Behavior

These adapters are stubs.

They do not execute real tools. They return mock artifact references and finding candidate IDs so that Tool Gateway can validate routing behavior.

## Safety Rules

Adapter stubs must not:

- run shell commands,
- call real tools,
- access customer systems,
- resolve raw credentials,
- write raw artifacts to tracked paths,
- accept arbitrary AI-generated operations.

## Validation

Run:

~~~bash
py tools/run_all_local_checks.py
~~~

This includes adapter registry and fail-closed operation checks.

## Internal Adapter Artifact Boundary

Adapter output is internal Tool Gateway information.

It must not appear directly in generated public `tool_execution_result` objects or evidence records.

Future real tool integrations should persist raw adapter output only under ignored/private artifact paths and expose only sanitized references or summaries to AI-visible and evidence-facing components.

See `docs/22-internal-adapter-artifact-policy.md`.

## ZAP Command Plan Step

The ZAP adapter now supports a dry-run command plan.

This does not execute ZAP. It only structures the future execution plan so that real execution can later be added through a controlled executor rather than arbitrary AI-generated shell commands.

See `docs/23-zap-adapter-command-plan.md`.
