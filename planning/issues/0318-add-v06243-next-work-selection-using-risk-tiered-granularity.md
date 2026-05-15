# 0318 - Add v0.6.243 Next Work Selection Using Risk-Tiered Granularity

Status: completed by v0.6.243  
Version: v0.6.243  
Type: planning / next work selection checkpoint

## Objective

Use risk-tiered granularity to select the next work item after v0.6.242 accepted the Record Candidate Artifact Creation Planning Candidate.

## Selected work item

~~~text
record_candidate_artifact_creation_candidate
~~~

## Acceptance criteria

- `next_work_selection_completed = true` is recorded.
- `selected_work_item = record_candidate_artifact_creation_candidate` is recorded.
- `selected_work_item_status = selected_for_next_candidate_checkpoint` is recorded.
- `record_candidate_artifact_creation_candidate_selected = true` is recorded.
- `selection_applied_to_record_candidate_artifacts = false` is recorded.
- The checkpoint states that this is selection only.
- No record candidate artifacts are created in v0.6.243.
- No actual records, minimum flow package, package implementation, fixtures, reviewer walkthrough, AAEF five questions mapping, or AAEF handback summary are created.
- No runtime behavior, scanner behavior, Tool Gateway behavior, adapter behavior, schema behavior, or validator behavior is changed, except registration of the v0.6.243 structural test.

## Next

Proceed to v0.6.244 Record Candidate Artifact Creation Candidate after v0.6.243 is merged and tagged.
