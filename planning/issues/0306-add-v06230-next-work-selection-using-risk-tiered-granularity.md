# 0306 - Add v0.6.230 Next Work Selection Using Risk-Tiered Granularity

Status: completed by v0.6.230  
Version: v0.6.230  
Type: planning / next work selection checkpoint

## Objective

Use risk-tiered granularity to select the next work item after v0.6.229 accepted the Evidence Linkage Table Candidate for future package planning / future record planning.

## Selected work item

~~~text
tool_action_request_gate_decision_dispatch_evidence_package
~~~

## Acceptance criteria

- `next_work_selection_completed = true` is recorded.
- `selected_work_item = tool_action_request_gate_decision_dispatch_evidence_package` is recorded.
- `selected_work_item_status = selected_for_next_candidate_checkpoint` is recorded.
- The checkpoint states that this is selection only.
- The selected package is not created in v0.6.230.
- No minimum flow package, package candidate, fixtures, evidence linkage records, request records, decision records, dispatch records, result records, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.230 structural test.
- No production readiness, scanner readiness, runtime demo readiness, external PoC readiness, publication approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Out of scope

- Creating the selected package.
- Creating package-level artifacts.
- Creating or modifying fixtures.
- Creating evidence linkage records.
- Creating runtime behavior.
- Changing Tool Gateway or adapter behavior.
- Changing schema behavior.
- Changing validator behavior, except registration of the v0.6.230 structural test.
- Moving private generated outputs public.
- Publishing announcements or social posts.
- Creating commercial terms.

## Next

Proceed to v0.6.231 Tool Action Request Gate Decision Dispatch Evidence Package Candidate after v0.6.230 is merged and tagged.
