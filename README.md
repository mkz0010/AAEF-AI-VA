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
