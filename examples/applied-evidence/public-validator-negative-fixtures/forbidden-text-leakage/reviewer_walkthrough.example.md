# Reviewer walkthrough

This sanitized public sample is synthetic and non-executing.

| Scenario | Gate result | Dispatch attempted | Result artifact |
| --- | --- | --- | --- |
| `permitted-safe-diagnostic` | `permitted` | `true` | `execution_result.example.json` |
| `denied-out-of-scope-request` | `denied` | `false` | `non_execution_result.example.json` |
| `human-approval-required` | `held_requires_human_approval` | `false` | `non_execution_result.example.json` |
| `not-executed-expired` | `expired` | `false` | `non_execution_result.example.json` |

Reviewer focus:

1. Confirm the request is not authority.
2. Confirm gate decision is separate from dispatch decision.
3. Confirm non-dispatch is evidenced for denied, held, and expired scenarios.
4. Confirm evidence event links request, decision, dispatch, and result.
5. Confirm non-proof statements remain visible.


Synthetic negative sentinel: private-not-in-git should never appear in a public example artifact.
