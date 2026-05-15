# 0315 - Add v0.6.240 Next Work Selection Using Risk-Tiered Granularity

Status: completed by v0.6.240  
Version: v0.6.240  
Type: planning / next work selection checkpoint

## Objective

Use risk-tiered granularity to select the next work item after v0.6.239 accepted the Record Candidate Planning Candidate for future record candidate artifact creation planning.

## Selected work item

~~~text
record_candidate_artifact_creation_planning
~~~

## Acceptance criteria

- `next_work_selection_completed = true` is recorded.
- `selected_work_item = record_candidate_artifact_creation_planning` is recorded.
- `selected_work_item_status = selected_for_next_candidate_checkpoint` is recorded.
- `record_candidate_artifact_creation_planning_selected = true` is recorded.
- `selection_applied_to_record_candidate_artifacts = false` is recorded.
- The checkpoint states that this is selection only.
- No record candidate artifacts are created in v0.6.240.
- No actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.240 structural test.
- No production readiness, scanner readiness, runtime demo readiness, external PoC readiness, publication approval, legal compliance, audit sufficiency, audit opinion, certification, diagnostic completeness, automated risk acceptance, or external-framework equivalence claim is made.

## Out of scope

- Creating the record candidate artifact creation planning candidate.
- Creating record candidate artifacts.
- Creating actual records.
- Creating or modifying fixtures.
- Creating runtime behavior.
- Changing Tool Gateway or adapter behavior.
- Changing schema behavior.
- Changing validator behavior, except registration of the v0.6.240 structural test.
- Moving private generated outputs public.
- Publishing announcements or social posts.
- Creating commercial terms.

## Next

Proceed to v0.6.241 Record Candidate Artifact Creation Planning Candidate after v0.6.240 is merged and tagged.
