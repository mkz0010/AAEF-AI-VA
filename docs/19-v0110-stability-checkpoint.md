# v0.1.10 Stability Checkpoint

## Purpose

This document records the local stability checkpoint after the v0.1.8 and v0.1.9 remediation sequence.

The project is local-first and private by default. This document is intended to help future review by making the validation status explicit.

## Summary

`v0.1.10` is the current stable local checkpoint for the MVP Tool Gateway mock runner.

It includes:

- MVP scope definition,
- credential_ref flow,
- Tool Gateway MVP design,
- MVP schema contracts,
- prototype example flows,
- Tool Gateway mock runner,
- fail-closed negative tests,
- mock Vault metadata validation,
- remaining Python escaped docstring fixes.

## Version Notes

| Version | Status | Notes |
|---|---|---|
| v0.1.8 | Superseded | Added mock Vault metadata validation, but runner validation failed due to escaped Python docstring syntax |
| v0.1.9 | Superseded | Fixed `gateway.py` escaped docstring issue, but `policy.py` still had escaped docstring syntax |
| v0.1.10 | Stable checkpoint | Fixed remaining Python escaped docstrings and passed compile, schema, example, runner, and fail-closed tests |

## Validation Commands

Run the complete local validation set:

~~~bash
py tools/run_all_local_checks.py
~~~

Equivalent individual commands:

~~~bash
py -m compileall -q prototypes tools
py tools/validate_mvp_schemas.py
py tools/validate_mvp_examples.py
py tools/run_tool_gateway_example.py all
py tools/test_tool_gateway_runner.py
~~~

## Expected Result

The expected validation result includes:

~~~text
MVP schema validation passed.
MVP example validation passed for 12 files.
allowed-action: completed
denied-action: blocked
human-approval-required: requires_human_approval
PASS: positive scenarios
PASS: negative fail-closed scenarios
PASS: credential_ref mock Vault metadata negative scenarios
PASS: generated runner outputs
Tool Gateway runner tests passed.
All local checks passed.
~~~

## Operational Lesson

If any validation script fails, do not commit, merge, or tag the branch.

The safe workflow is:

1. stop immediately,
2. inspect the failing command,
3. fix the issue on the feature branch,
4. rerun the full validation set,
5. commit only after validation passes.

## Current Stable Point

For future work, use `v0.1.10` or later as the baseline.

Avoid using `v0.1.8` or `v0.1.9` as implementation baselines except for historical review.
