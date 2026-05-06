# Review summary: denied-out-of-scope-request

## What AI requested

The example request `example-request-denied-out-of-scope-request` requested `synthetic_out_of_scope_check` using
`safe-diagnostic-tool` for `synthetic-out-of-scope-example-target`.

The request is not authority.

## Gate decision

Gate decision `example-decision-denied-out-of-scope-request` recorded `denied`.

## Dispatch decision

Dispatch decision `example-dispatch-denied-out-of-scope-request` recorded
`dispatch_attempted = false`.

## Result posture

Result `example-result-denied-out-of-scope-request` records a synthetic non-execution result artifact. No real execution occurred.

## Evidence

Evidence event `example-evidence-denied-out-of-scope-request` links request, decision, dispatch, and result.

## AAEF five questions

| Question | Answer |
| --- | --- |
| Who or what acted? | AI generated a request; a gateway example recorded dispatch posture |
| On whose behalf? | Synthetic example principal |
| With what authority? | Gate decision `example-decision-denied-out-of-scope-request` and example policy |
| Was the action allowed at the point of execution? | See dispatch decision and result posture |
| What evidence proves what happened? | Evidence event `example-evidence-denied-out-of-scope-request` and this review summary |

## Non-proof

This scenario does not prove vulnerability detection accuracy, production readiness,
implementation conformance, audit sufficiency, legal sufficiency, compliance
certification, external-framework equivalence, customer-target authorization, delivery
authorization, or safety guarantee.
