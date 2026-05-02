# Tool Gateway Negative Tests

## Purpose

This document defines the first negative tests for the Tool Gateway mock runner.

The purpose is to confirm that Tool Gateway behaves as a fail-closed control boundary, not as a convenience wrapper around AI output.

## Test Scope

The tests validate three groups of behavior:

1. positive example scenarios,
2. negative fail-closed scenarios,
3. generated runner outputs.

## Positive Scenarios

The positive scenarios verify the expected status for each existing example flow.

| Scenario | Expected Result |
|---|---|
| allowed-action | completed |
| denied-action | blocked |
| human-approval-required | requires_human_approval |

## Negative Fail-Closed Scenarios

The negative tests mutate an otherwise valid allowed request/decision pair and confirm that Tool Gateway raises a policy error.

Initial negative cases:

| Case | Expected Behavior |
|---|---|
| target_id mismatch | reject |
| scope_id mismatch | reject |
| tool mismatch | reject |
| operation mismatch | reject |
| credential_ref mismatch | reject |
| destructive_tests = true | reject |
| evidence_required = false | reject |
| expires_at not after decided_at | reject |

## Generated Output Validation

The tests also run:

~~~bash
py tools/run_tool_gateway_example.py all --out-dir private-not-in-git/test-runs/tool-gateway-runner
~~~

Then they verify that:

- generated result files exist,
- generated evidence files exist,
- generated statuses match expected behavior,
- `secret_exposed_to_ai` remains false,
- evidence links back to generated execution results.

## Run Command

~~~bash
py tools/test_tool_gateway_runner.py
~~~

Expected output:

~~~text
PASS: positive scenarios
PASS: negative fail-closed scenarios
PASS: generated runner outputs
Tool Gateway runner tests passed.
~~~

## Relationship to AAEF

These tests demonstrate that model output is not authority.

Even if an AI-generated request is structurally valid, Tool Gateway must reject execution when the authorization decision is missing, mismatched, unsafe, or insufficiently constrained.
