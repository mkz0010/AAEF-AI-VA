# 0312 - Add v0.6.236 Next Work Selection Using Risk-Tiered Granularity

Status: completed by v0.6.236  
Version: v0.6.236  
Type: planning / next work selection checkpoint

## Objective

Use risk-tiered granularity to select the next work item after v0.6.235 accepted the Future Record Planning Candidate for future fixture planning and record candidate planning.

## Selected work item

~~~text
record_candidate_planning
~~~

## Acceptance criteria

- `next_work_selection_completed = true` is recorded.
- `selected_work_item = record_candidate_planning` is recorded.
- `selected_work_item_status = selected_for_next_candidate_checkpoint` is recorded.
- `record_candidate_planning_selected = true` is recorded.
- `selection_applied_to_record_candidates = false` is recorded.
- The checkpoint states that this is selection only.
- No record candidate artifacts are created in v0.6.236.
- No actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.236 structural test.
- No production readiness, scanner readiness, runtime demo readiness, external PoC readiness, publication approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Out of scope

- Creating the record candidate planning candidate.
- Creating record candidate artifacts.
- Creating actual records.
- Creating or modifying fixtures.
- Creating runtime behavior.
- Changing Tool Gateway or adapter behavior.
- Changing schema behavior.
- Changing validator behavior, except registration of the v0.6.236 structural test.
- Moving private generated outputs public.
- Publishing announcements or social posts.
- Creating commercial terms.

## Next

Proceed to v0.6.237 Record Candidate Planning Candidate after v0.6.236 is merged and tagged.
