# Issue 0061: Add README compatibility phrase registry and test design hardening

Status: Completed by v0.5.2 candidate  
Type: README maintenance / test design / compatibility hardening

## Goal

Create a registry of README compatibility phrases and test-design rules to reduce
future README rewrite regressions.

## Acceptance criteria

- [x] Add README compatibility phrase registry documentation.
- [x] Add ADR recording the decision.
- [x] Add local validation test.
- [x] Register the validation test in `tools/run_all_local_checks.py`.
- [x] Record stable README headings.
- [x] Record stable README phrases.
- [x] Record stable README links.
- [x] Record forbidden positive claims.
- [x] Record allowed negative boundary statements.
- [x] Preserve runtime and scanning boundaries.

## Non-goals

- Rewrite README again.
- Generate README from templates.
- Publish outreach material.
- Create a commercial contact channel.
- Provide legal advice.
- Enable runtime execution.
- Enable ZAP, scans, external process execution, credential injection, or network activity.
