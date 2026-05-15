# 0309 - Add v0.6.233 Next Work Selection Using Risk-Tiered Granularity

Status: completed by v0.6.233  
Version: v0.6.233  
Type: planning / next work selection checkpoint

## Objective

Use risk-tiered granularity to select the next work item after v0.6.232 accepted the `tool_action_request_gate_decision_dispatch_evidence_package` boundary for future fixture and record planning.

## Selected work item

~~~text
future_record_planning
~~~

## Acceptance criteria

- `next_work_selection_completed = true` is recorded.
- `selected_work_item = future_record_planning` is recorded.
- `selected_work_item_status = selected_for_next_candidate_checkpoint` is recorded.
- `future_record_planning_selected = true` is recorded.
- `selection_applied_to_records = false` is recorded.
- The checkpoint states that this is selection only.
- No actual records are created in v0.6.233.
- No minimum flow package, package implementation, record planning candidate, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.233 structural test.
- No production readiness, scanner readiness, runtime demo readiness, external PoC readiness, publication approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Out of scope

- Creating the future record planning candidate.
- Creating actual record artifacts.
- Creating or modifying fixtures.
- Creating runtime behavior.
- Changing Tool Gateway or adapter behavior.
- Changing schema behavior.
- Changing validator behavior, except registration of the v0.6.233 structural test.
- Moving private generated outputs public.
- Publishing announcements or social posts.
- Creating commercial terms.

## Next

Proceed to v0.6.234 Future Record Planning Candidate after v0.6.233 is merged and tagged.
