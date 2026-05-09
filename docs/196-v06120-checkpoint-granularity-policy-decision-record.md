# v0.6.120 Checkpoint Granularity Policy — Decision Record

Status: decision
Date: 2026-05-10

## Purpose

This checkpoint adopts a risk-tiered checkpoint granularity policy for future AAEF-AI-VA work.

This checkpoint is intentionally completed as one checkpoint.

This is the first application of the new risk-tiered checkpoint granularity policy.

Low-risk operational policy decisions should normally complete in one checkpoint.

The previous planning -> candidate -> review -> close-readiness -> decision pattern is no longer the default.

That expanded pattern remains available for critical-risk work.

## Decision

AAEF-AI-VA adopts risk-tiered checkpoint granularity.

The checkpoint count should be selected based on the risk and reversibility of the work, rather than applying the expanded five-step pattern to every decision.

The new default is:

~~~text
1 decision = 1 checkpoint, unless the risk tier justifies more.
~~~

## Decision record

~~~text
checkpoint_granularity_policy_decision_record_completed = true
checkpoint_granularity_policy_is_documentation_only = true
checkpoint_granularity_policy_adopted = true
risk_tiered_granularity_adopted = true
single_checkpoint_application_demonstrated = true
low_risk_policy_decision_completed_in_one_checkpoint = true
planning_candidate_review_close_readiness_decision_chain_not_used = true
expanded_checkpoint_pattern_no_longer_default = true
expanded_checkpoint_pattern_retained_for_critical_risk = true
existing_checkpoints_retroactively_modified = false
existing_tags_rewritten = false
existing_release_history_collapsed = false
aaef_main_handback_sequence_remains_paused = true
aaef_main_issue_opened = false
aaef_main_pull_request_opened = false
aaef_main_issue_submission_command_generated = false
aaef_main_issue_url_generated = false
runtime_execution_authorized = false
scanner_execution_authorized = false
docker_execution_authorized = false
credential_injection_permitted = false
customer_target_authorized = false
delivery_authorized = false
validator_behavior_modified = false
metadata_level_expected_failure_category_added = false
json_schema_added = false
public_sample_changed = false
aaef_core_promotion = false
aaef_profile_promotion = false
aaef_practical_package_promotion = false
selected_next_direction = apply_risk_tiered_granularity_to_future_work_selection
~~~

## Rationale

The previous fine-grained pattern was introduced for good reasons:

* to preserve "AI output is not authority" in the work process itself,
* to separate proposal, candidate text, review, close-readiness, and decision,
* to prevent accidental public disclosure of private, patent-sensitive, customer, credential, scanner, or commercial material,
* to preserve non-execution evidence,
* to keep high-risk or public-facing work reversible,
* to protect human-maintainer-only authority boundaries.

That pattern was useful while AAEF-AI-VA was first exploring public-safe AAEF main handback boundaries.

However, recent work showed that applying the expanded pattern to every decision can become excessive:

* one decision can become many tags,
* README, CHANGELOG, ROADMAP, and `run_all_local_checks.py` grow quickly,
* repeated boundary text can obscure the actual change,
* reviewers can lose the current state,
* low-risk operational policy records can become heavier than the decision itself.

Therefore, the expanded pattern should become a risk-based option, not the default.

## Risk-tiered checkpoint granularity policy

| Risk tier | Examples | Normal checkpoint count |
| --- | --- | --- |
| Low risk | current-state review, closeout, pause record, operational policy decision, workstream direction selection | 1 checkpoint |
| Medium risk | public wording, issue text candidate, README/public overview changes, non-executing external handback material | 2 checkpoints |
| High risk | validator behavior, schema, fixture, public sample, release-facing evidence artifact changes | 3 checkpoints |
| Critical risk | runtime execution, scanner execution, Docker/lab execution, credential injection, customer target, delivery authorization, actual external submission | 4-5 checkpoints |

## Low risk

Low risk work should normally be handled in one checkpoint.

Expected structure:

~~~text
Decision Record
- context
- risk tier
- decision
- rationale
- what did not happen
- next direction
~~~

This v0.6.120 checkpoint is intentionally a low-risk one-checkpoint decision record.

## Medium risk

Medium risk work should normally use two checkpoints:

~~~text
1. Candidate / preparation
2. Review + decision
~~~

Use this for public-facing wording or external handback material where content leakage and overclaim risk exist, but where no runtime execution, validator behavior change, schema change, public sample change, or actual submission occurs.

## High risk

High risk work should normally use three checkpoints:

~~~text
1. Planning / readiness
2. Candidate / implementation
3. Review + close-readiness / decision
~~~

Use this for validator, schema, fixture, and public sample changes because they can affect repository behavior, public examples, or reviewer interpretation.

## Critical risk

Critical risk work may continue using four to five checkpoints.

Examples:

* runtime execution,
* scanner execution,
* Docker or local lab execution,
* credential injection,
* customer target handling,
* delivery authorization,
* actual external repository submission,
* public release actions with irreversible external effects.

For critical-risk work, the expanded pattern may remain appropriate:

~~~text
planning
candidate
review
close-readiness
decision
human/execution gate
~~~

## Default rule

Use the smallest checkpoint count that preserves the authority, evidence, safety, and reversibility requirements of the work.

## Escalation rule

Escalate to more checkpoints if the work involves any of the following:

* public-facing claim risk,
* external repository effects,
* validator behavior changes,
* schema or fixture changes,
* public sample changes,
* runtime or scanner execution,
* Docker or lab execution,
* credential handling,
* customer target handling,
* delivery authorization,
* patent-sensitive detail,
* commercial or paid/NDA adoption package material.

## De-escalation rule

Do not use the expanded five-step pattern merely because a prior workstream used it.

Low-risk decisions should not be inflated into planning, candidate, review, close-readiness, and decision unless a specific risk justifies that expansion.

## What did not happen

Existing checkpoints are not retroactively rewritten.

Existing tags are not rewritten.

Existing release history is not collapsed.

The v0.6.109 through v0.6.119 handback sequence remains valid historical evidence of a deliberately conservative first handback exploration.

No AAEF main issue is opened.

No AAEF main pull request is opened.

No issue creation command is generated.

No issue URL is created.

No AAEF main submission is executed.

No validator behavior is modified.

No metadata-level `expected_failure_category` is added.

No JSON Schema is added.

No public sample is changed.

No runtime execution is authorized.

No scanner execution is authorized.

No Docker execution is authorized.

No credential injection is permitted.

No customer target is authorized.

No delivery is authorized.

No AAEF Core, Profile, or Practical Package promotion is decided.

## Relationship to v0.6.119

v0.6.119 closed the current narrow public-safe AAEF main handback sequence as paused.

This v0.6.120 checkpoint does not reopen that sequence.

The close-ready exact issue text candidate and close-ready human checklist remain internal reviewer aids only.

## Next direction

Future work should apply this risk-tiered checkpoint granularity policy when selecting the next work item.

A likely next checkpoint is:

~~~text
v0.6.121 Next-Direction Selection Using Risk-Tiered Granularity
~~~

That checkpoint should choose a future work item and explicitly assign its risk tier and checkpoint count before implementation begins.
