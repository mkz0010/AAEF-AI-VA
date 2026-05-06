# AAEF five questions mapping

| AAEF question | Public example evidence source |
| --- | --- |
| Who or what acted? | `tool_action_request.example.json`, gateway identity, `dispatch_decision.example.json` |
| On whose behalf? | synthetic principal context in `tool_action_request.example.json` |
| With what authority? | `gate_decision.example.json`, policy version, rule version |
| Was the action allowed at the point of execution? | `dispatch_decision.example.json`, execution boundary, result artifact |
| What evidence proves what happened? | `evidence_event.example.json`, result artifact, `review_summary.example.md` |

This mapping is reviewer guidance, not certification, audit opinion, legal approval, or
implementation conformance.
