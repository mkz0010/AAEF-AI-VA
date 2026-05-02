# AAEF-controlled AI Vulnerability Assessment Platform

AAEF制御型AI脆弱性診断基盤のローカル管理リポジトリ。

This repository is local-first and private by default.

## Core Principle

Model output is not authority.

AIの出力は診断行為の権限ではない。AIは診断行為を要求できるが、実行可否はAAEF Authorization Gateway、Tool Gateway、契約スコープ、人間レビューによって決定される。

## Repository Rule


## Local Validation

Run the complete local validation set before committing, merging, or tagging implementation changes:

~~~bash
py tools/run_all_local_checks.py
~~~

As of `v0.1.10`, the Tool Gateway mock runner baseline is the current stable local checkpoint.

Do not commit raw customer materials, credentials, scan artifacts, personal data, secrets, or confidential client data.

## Local Lifecycle Checkpoint

The local prototype includes a v0.1.30 lifecycle integration checkpoint.

It summarizes the current control and review workflow while keeping real execution, network activity, report-ready status, delivery dispatch, and customer delivery disabled.

See `docs/38-lifecycle-integration-checkpoint.md`.

## Controlled Local Runtime Readiness

v0.2.0 introduces controlled local ZAP runtime readiness.

This is detection-only: it may record whether a local ZAP runtime appears available, but it does not start ZAP, run scans, perform network activity, inject credentials, or capture raw runtime artifacts.

See `docs/39-controlled-local-runtime-readiness.md`.

## Local Target Lab Profile

v0.2.1 introduces a local target lab profile.

It defines localhost/Docker-internal intentionally vulnerable lab targets for future bounded execution consideration, while keeping scans, network activity, customer targets, and external targets disabled.

See `docs/40-local-target-lab-profile.md`.

## Runtime Destination Binding

v0.2.2 introduces scope-registry-style runtime destination binding.

It binds a controlled local ZAP runtime readiness profile to a local lab target profile while keeping scans, network activity, real execution, customer targets, and external targets disabled.

See `docs/41-scope-registry-runtime-destination-binding.md`.

## Bounded Execution Transition Candidate

v0.2.3 introduces a bounded execution transition candidate.

It structures prerequisites for future local-only execution planning while keeping scan execution, network activity, real execution, process execution, credential injection, and raw artifact capture disabled.

See `docs/42-bounded-execution-transition-candidate.md`.

## Local-Only Execution Plan Review

v0.2.4 introduces local-only execution plan review.

It allows only plan-level `runtime_detection` and `health_check_plan_only` while keeping ZAP start/stop/API calls, scans, network activity, credential injection, raw artifact capture, customer targets, and external targets disabled.

See `docs/43-local-only-execution-plan-review.md`.

## Runtime Safety Policy Scaffold

v0.2.5 introduces a no-egress, timeout, and kill-switch policy scaffold.

It defines future safety requirements while keeping ZAP process launch, network activity, scans, credential injection, raw artifact capture, customer targets, and external targets disabled.

See `docs/44-no-egress-timeout-kill-switch-policy.md`.

## Runtime Enforcement Design Scaffold

v0.2.6 introduces a runtime enforcement design scaffold.

It records future components such as preflight check, process wrapper, no-egress guard, timeout watcher, kill-switch controller, evidence emitter, and sanitizer boundary while keeping all runtime enforcement unimplemented and execution disabled.

See `docs/45-runtime-enforcement-design-scaffold.md`.

## Execution Authorization Gate Scaffold

v0.2.7 introduces an execution authorization gate scaffold.

It defines future approval and verification requirements while keeping execution authorization, real execution, process execution, network activity, scans, credential injection, and raw artifact capture disabled.

See `docs/46-execution-authorization-gate-scaffold.md`.

## Preflight Validation Scaffold

v0.2.8 introduces a preflight validation scaffold.

It defines the future execution-before-checklist across runtime readiness, target binding, authorization, approvals, no-egress, timeout, kill-switch, evidence, and sanitizer boundaries while keeping preflight unsatisfied and execution disabled.

See `docs/47-preflight-validation-scaffold.md`.

## Runtime Transition Checkpoint

v0.2.9 introduces a runtime transition checkpoint.

It summarizes v0.2.0 through v0.2.8 and confirms that the project is ready for concrete preflight implementation work, while runtime execution, process launch, network activity, scans, credential injection, raw artifact capture, customer targets, and external targets remain disabled.

See `docs/48-runtime-transition-checkpoint.md`.

## Concrete Preflight Check Implementation Scaffold

v0.3.0 introduces concrete preflight check implementation scaffolding.

Each required preflight check receives input sources, evidence type, fail-closed behavior, and responsibility while all checks remain unimplemented, preflight remains unsatisfied, and execution remains disabled.

See `docs/49-preflight-check-implementation-scaffold.md`.

## Preflight Evidence Record Model

v0.3.1 introduces the preflight evidence record model.

Each required preflight check receives a non-generated evidence record shape with evidence type, input sources, fail-closed behavior, AI visibility boundary, raw artifact boundary, and sanitized summary requirement while execution remains disabled.

See `docs/50-preflight-evidence-record-model.md`.

## Generated Preflight Evidence Record Examples

v0.3.2 introduces representative generated preflight evidence record examples.

The examples demonstrate fail-closed evidence behavior for selected checks while remaining separate from live evidence generation, check satisfaction, preflight satisfaction, and execution authorization.

See `docs/51-generated-preflight-evidence-record-examples.md`.

## Preflight Evidence Validation Rules

v0.3.3 introduces preflight evidence validation rules.

The rules validate generated preflight evidence examples while keeping live evidence validation, preflight satisfaction, execution authorization, and runtime execution disabled.

See `docs/52-preflight-evidence-validation-rules.md`.
