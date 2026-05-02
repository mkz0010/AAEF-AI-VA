# AAEF-controlled AI Vulnerability Assessment Platform

## v0.3.4 Negative preflight evidence examples

v0.3.4 adds representative negative preflight evidence examples. These examples describe invalid, missing, stale, mismatched, or unsafe evidence claims that must be rejected fail-closed.

This release does not generate live evidence, does not satisfy preflight, does not authorize execution, and does not permit runtime scanning, network activity, external process execution, credential injection, or raw artifact capture.

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

## License

## Public Repository Readiness

This repository is prepared as a local-first implementation project until an explicit public repository readiness checkpoint is satisfied.

The current public-readiness posture is:

- license boundary recorded: AGPL-3.0 for AAEF-AI-VA code
- AAEF attribution boundary recorded: AAEF remains CC BY 4.0
- private generated artifacts remain under `private-not-in-git/`
- runtime execution remains disabled unless future explicit authorization gates are implemented and satisfied
- external network activity, scan execution, and credential injection remain disabled
- commercial licensing contact information remains a placeholder until the author publishes a durable contact channel

See `docs/55-public-repository-readiness-checkpoint.md` for the detailed checkpoint.

AAEF-AI-VA is licensed under the GNU Affero General Public License v3.0.
See [LICENSE](LICENSE) for details.

This project builds on concepts and documentation from the
Agentic Authority & Evidence Framework (AAEF), which is licensed under
Creative Commons Attribution 4.0 International (CC BY 4.0).

AAEF:
https://github.com/mkz0010/agentic-authority-evidence-framework

AAEF-AI-VA is a separate code implementation project. Use of AAEF-AI-VA
must comply with AGPL-3.0 unless a separate commercial license has been
granted by the author.

For commercial licensing inquiries, please contact the author.

## Publication Hygiene and Private Artifact Boundary

Before any public push, this repository treats publication hygiene as a separate checkpoint from runtime readiness.

The expected publication hygiene posture is:

- `private-not-in-git/` is excluded from version control
- generated local evidence, run outputs, and review artifacts are not intended for public publication
- Python caches and local environment files are excluded
- repository publication does not authorize runtime execution
- repository publication does not permit external network activity, scan execution, credential injection, or raw artifact capture

See `docs/56-publication-hygiene-and-private-artifact-exclusion-checkpoint.md` for the detailed checkpoint.

## Security Policy

AAEF-AI-VA includes a public security policy and vulnerability disclosure checkpoint.

Before public repository publication, the project distinguishes:

- security vulnerability reports
- commercial licensing inquiries
- runtime execution authorization
- publication hygiene and private artifact exclusion

See `SECURITY.md` and `docs/57-public-security-policy-and-vulnerability-disclosure-checkpoint.md`.

## First Publication Repository Settings

AAEF-AI-VA includes a first-publication repository settings checklist before any remote repository is created, configured, or pushed.

The checklist separates:

- repository visibility decision: public, private, or staged public
- repository metadata: description, topics, About sidebar, license display
- security settings: `SECURITY.md`, private vulnerability reporting, security advisories
- repository collaboration settings: Issues, Discussions, Wiki, pull requests
- branch protection or ruleset planning for `main`
- initial remote setup and push commands as a manual, non-automated step
- runtime execution authorization, which remains disabled

See `docs/58-first-publication-repository-settings-checklist.md`.
