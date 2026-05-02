# v0.6.7 Observation Normalization and Diagnostic Fidelity Risk Review

Version: v0.6.7 candidate  
Status: observation normalization and diagnostic fidelity risk review; does not authorize runtime execution

## Purpose

This checkpoint defines how AAEF-AI-VA should reason about observation normalization
and Diagnostic Fidelity Risk.

v0.6.6 established that AI may generate `tool_action_request`, while gates decide
execution. The next design question is what information AI should receive in order
to generate useful requests without receiving unsafe raw responses or secrets.

This checkpoint is design and risk review only.

This checkpoint does not authorize runtime execution, scanning, credential injection,
customer-target operation, production deployment, certification, legal approval, or
audit opinion.

## Core concern

Safety controls can reduce diagnostic accuracy if they remove or over-normalize
important signals.

The project must avoid both extremes:

~~~text
Unsafe extreme:
  Send raw responses directly to AI.

Unhelpful extreme:
  Over-sanitize and over-normalize until diagnostic signals disappear.
~~~

The intended model is:

~~~text
Keep raw artifacts controlled.
Give AI safe diagnostic context.
Record what was removed, preserved, summarized, or lost.
Require escalation when context is insufficient.
~~~

## Compatibility note

The following exact lines are retained for validation compatibility when equivalent Markdown prose is line-wrapped:

- Safety controls can reduce diagnostic accuracy if they remove or over-normalize important signals.
- AI should not receive uncontrolled raw responses, secrets, credentials, access tokens, session values, or customer-sensitive raw artifacts.
- AI should instead request additional observation, human review, or sufficiency improvement.

## Diagnostic Fidelity Risk

Diagnostic Fidelity Risk means:

~~~text
The risk that sanitization, redaction, normalization, summarization, or extraction
removes diagnostically important information and lowers the quality of an AI-generated
tool_action_request.
~~~

This risk is not a reason to send raw artifacts directly to AI.

It is a reason to preserve diagnostic signals, record normalization loss, and provide
review or escalation paths.

## Observation handling pipeline

The intended observation handling pipeline is:

~~~text
Raw response or raw tool output
  -> controlled raw artifact reference
  -> sanitizer / redactor
  -> sanitized artifact
  -> normalizer
  -> normalized observation
  -> diagnostic signal extractor
  -> AI diagnostic context package
  -> AI-generated tool_action_request
  -> gate decision
~~~

AI should receive the AI diagnostic context package.

AI should not receive uncontrolled raw responses, secrets, credentials, access tokens,
session values, or customer-sensitive raw artifacts.

## Raw artifact principle

Raw artifacts may be retained as controlled references.

Raw artifact retention does not mean AI access.

A raw artifact reference should support later human review, evidence reconstruction,
or loss analysis, while keeping unsafe or sensitive content out of AI prompts.

Raw artifact access should require:

- scope binding,
- artifact classification,
- human review rationale,
- redaction review,
- private output boundary,
- evidence chain linkage,
- reason for escalation.

## AI diagnostic context package

An AI diagnostic context package should include:

| Field | Purpose |
| --- | --- |
| `context_id` | Unique diagnostic context identifier |
| `source_observation_refs` | References to sanitized or normalized observations |
| `raw_artifact_refs` | Controlled references, not raw content |
| `target_binding_ref` | Target and scope binding reference |
| `observation_summary` | Safe diagnostic summary |
| `extracted_signals` | Preserved diagnostic signals |
| `negative_signals` | Signals explicitly not observed |
| `normalization_loss_record_ref` | Reference to loss record |
| `missing_information` | Known gaps |
| `confidence` | Non-authoritative context confidence |
| `uncertainty` | Known uncertainty |
| `prompt_injection_risk` | Risk from untrusted content |
| `credential_exposure_risk` | Whether sensitive tokens or credentials were detected |
| `recommended_next_observation` | Non-executing observation recommendation |
| `safety_notes` | Safety constraints |
| `human_review_recommended` | Whether review is recommended |

The package supports request generation only.

It does not authorize execution.

## Signal-preserving extraction

Sanitization should remove or suppress unsafe content while preserving diagnostic
signals where possible.

For HTTP observations, signal-preserving extraction may include:

- status code,
- redirect chain summary,
- response header names and selected safe attributes,
- security header presence or absence,
- cookie attribute summary without cookie values,
- content type,
- form field names and types,
- hidden field presence without secret values,
- reflected input indicators,
- script source references,
- endpoint candidates,
- API schema hints,
- authentication state indicators,
- error signature summaries,
- stack trace presence without full sensitive trace,
- framework hints,
- encoding and parser anomalies,
- suspicious patterns,
- confidence and uncertainty,
- missing information.

Signal-preserving extraction should not expose secrets or raw sensitive content.

## Information that should not be sent directly to AI

The following should not be sent directly to AI:

- raw cookies,
- session identifiers,
- CSRF token values,
- bearer tokens,
- API keys,
- passwords,
- private keys,
- access tokens,
- refresh tokens,
- customer personal data,
- full raw HTML containing secrets,
- full raw JavaScript containing secrets,
- full stack traces containing sensitive paths or values,
- raw vulnerability artifacts,
- raw request or response bodies from customer systems,
- unreviewed prompt-injection content.

If a value is diagnostically relevant, it should be represented as a safe signal,
pattern, class, attribute summary, or controlled reference.

## Information density criteria

An AI diagnostic context package should be considered sufficient only if it contains
enough information for the intended request-generation task.

Minimum density criteria include:

- target and scope binding are present,
- source observation references are present,
- diagnostic purpose is stated,
- relevant extracted signals are present,
- removed or redacted fields are summarized,
- missing information is explicit,
- confidence and uncertainty are explicit,
- safety notes are present,
- prompt injection and credential exposure risks are recorded,
- expected evidence for the next request can be named.

Information density does not mean maximum content length.

Information density means diagnostically useful, safe, structured signal.

## Diagnostic sufficiency criteria

Before AI generates a `tool_action_request`, the diagnostic context should satisfy:

| Criterion | Required result |
| --- | --- |
| Target binding | Present |
| Scope binding | Present |
| Observation source | Approved and referenced |
| Sanitization status | Recorded |
| Normalization status | Recorded |
| Extracted signals | Present and relevant |
| Normalization loss | Recorded |
| Missing information | Explicit |
| Prompt-injection risk | Assessed |
| Credential exposure risk | Assessed |
| Human review need | Assessed |
| Expected evidence | Nameable |
| Denied action conflict | Not present |

If the criteria are not met, AI should not produce a confident diagnostic request.

AI should instead request additional observation, human review, or sufficiency
improvement.

## Normalization loss record

A normalization loss record should include:

| Field | Purpose |
| --- | --- |
| `loss_record_id` | Unique loss record identifier |
| `raw_artifact_ref` | Controlled raw artifact reference |
| `sanitized_artifact_ref` | Sanitized artifact reference |
| `normalized_observation_ref` | Normalized observation reference |
| `fields_removed` | Removed field categories |
| `fields_redacted` | Redacted field categories |
| `fields_preserved_as_signals` | Signals preserved without raw values |
| `fields_summarized` | Summarized fields |
| `possible_diagnostic_loss` | Potentially lost diagnostic meaning |
| `fidelity_risk_level` | low, medium, high, or unknown |
| `requires_human_review` | Whether review is required |
| `recommended_escalation` | Additional observation, review, or controlled raw reference inspection |

Normalization loss should be evidence, not hidden behavior.

## Fidelity risk levels

Use conservative qualitative levels:

| Level | Meaning |
| --- | --- |
| `low` | Removed content is unlikely to affect request generation |
| `medium` | Some diagnostic context may be missing or summarized |
| `high` | Important diagnostic signals may have been removed or distorted |
| `unknown` | Insufficient information to assess fidelity impact |

A high or unknown fidelity risk should not support confident diagnostic conclusions
without additional observation or human review.

## AI behavior under insufficient information

When information is insufficient, AI may:

- state that diagnostic context is insufficient,
- identify missing information,
- request additional observation as `tool_action_request`,
- request human review,
- lower confidence,
- provide alternative hypotheses,
- explain what cannot be concluded.

AI must not:

- invent missing observations,
- assume raw artifact content it has not received,
- treat normalized summaries as complete raw evidence,
- ignore normalization loss,
- convert uncertainty into execution permission,
- request secrets or raw credentials,
- bypass gates.

## Escalation paths

Escalation paths include:

| Escalation | Use when |
| --- | --- |
| `request_more_observation` | Required signals are missing |
| `request_human_review` | Fidelity risk, scope, or safety concern is significant |
| `request_preflight_evidence` | Preflight requirements are missing |
| `request_loss_record_review` | Normalization loss may affect diagnostic conclusion |
| `request_controlled_raw_reference_review` | Human review of raw artifact reference may be necessary |
| `keep_blocked` | Context is unsafe or insufficient |

Escalation is not execution.

Escalation produces a request or review path for gates to evaluate.

## Relationship to tool_action_request

Observation context influences `tool_action_request` quality.

A high-quality `tool_action_request` should reference:

- approved diagnostic context package,
- extracted signals used,
- missing information,
- normalization loss record,
- confidence and uncertainty,
- expected evidence,
- safety notes,
- human review requirement.

A `tool_action_request` should be rejected or returned for clarification if it:

- relies on raw artifact content not available to AI,
- ignores high fidelity risk,
- lacks observation references,
- lacks missing information where context is incomplete,
- requests execution when context only supports planning,
- requests a denied action category.

## Relationship to sanitizer and normalizer

Sanitizer and normalizer behavior should be separated:

| Component | Responsibility |
| --- | --- |
| Sanitizer / redactor | Remove or redact secrets, credentials, tokens, and unsafe raw content |
| Normalizer | Convert safe content into consistent observation structures |
| Signal extractor | Preserve diagnostic signals without exposing unsafe raw values |
| Loss recorder | Record what was removed, redacted, summarized, or potentially lost |
| Sufficiency gate | Decide whether the diagnostic context is enough for request generation |
| AI | Generate non-authoritative `tool_action_request` when context is sufficient |
| Gates | Decide whether any request remains blocked, requires review, or may advance |

AI should not be the component that decides whether unsafe raw content is acceptable.

## Prompt injection and untrusted content

HTTP responses, HTML, JavaScript, logs, stack traces, and tool outputs can contain
untrusted instructions or prompt-injection content.

Observation normalization should:

- mark untrusted content,
- avoid passing instructions as instructions,
- summarize suspicious instruction-like content,
- preserve relevant diagnostic signals,
- record prompt-injection risk,
- route high-risk cases to human review where appropriate.

Prompt-injection handling must not erase diagnostic signals silently.

## What this checkpoint enables

This checkpoint enables:

- safer design of AI diagnostic context packages,
- loss-aware normalization planning,
- sufficiency criteria before request generation,
- better reviewer analysis of AI request quality,
- clearer evidence reconstruction for observation handling,
- future demo planning that can explain what AI saw and did not see.

This checkpoint does not enable runtime execution or scanning.

## Recommended next checkpoint

The recommended next checkpoint is:

~~~text
v0.6.8 Demo Scenario and Reviewer Walkthrough Planning
~~~

Rationale:

- v0.6.6 defined the AI request boundary.
- v0.6.7 defines observation context and diagnostic fidelity risk.
- A demo walkthrough can now show what AI may see, what it may request, and what gates block.
- The demo should remain non-executing unless a later dry-run decision explicitly changes scope.

## Public claim boundary

Allowed public language:

- "loss-aware observation normalization",
- "diagnostic fidelity risk review",
- "AI diagnostic context package",
- "signal-preserving extraction",
- "normalization loss record",
- "diagnostic sufficiency criteria",
- "AI may request additional observation",
- "gates decide execution",
- "runtime execution remains blocked",
- "scan execution remains blocked."

Avoid public language that implies:

- raw responses are sent directly to AI,
- AI has full diagnostic visibility,
- AI can always diagnose accurately from normalized data,
- normalization has no diagnostic cost,
- live scanning,
- customer-target authorization,
- production deployment,
- managed service readiness,
- commercial PoC readiness,
- compliance certification,
- legal approval,
- audit opinion,
- external framework equivalence,
- commercial license grant.

## Compatibility note

Negative guidance may name unsafe implications such as AI having full diagnostic visibility or normalization having no diagnostic cost. Validation should reject concrete positive claims, not checklist entries that describe language to avoid.

## Runtime and scanning boundary

This checkpoint does not change runtime authorization.

The following must remain false unless future explicit work changes the execution
authorization model:

~~~text
execution_authorized = false
preflight_satisfied = false
ready_for_runtime_execution = false
real_execution_permitted = false
external_process_execution_allowed = false
network_activity_allowed = false
scan_execution_allowed = false
credential_injection_permitted = false
raw_artifact_capture_permitted = false
customer_target = false
external_network_target = false
~~~

## Claims to avoid

Do not claim that this checkpoint provides:

- production deployment approval,
- runtime execution readiness,
- scan authorization,
- customer-target authorization,
- compliance certification,
- legal approval,
- audit opinion,
- completed legal review,
- completed dependency audit,
- managed service approval,
- commercial license grant,
- safety guarantee,
- external framework equivalence,
- audit sufficiency.

## Required local checks

Before tagging v0.6.7, verify:

1. README links to this checkpoint.
2. Diagnostic Fidelity Risk is defined.
3. Observation handling pipeline is recorded.
4. Raw artifact principle is recorded.
5. AI diagnostic context package is recorded.
6. Signal-preserving extraction is recorded.
7. Information that should not be sent directly to AI is recorded.
8. Information density criteria are recorded.
9. Diagnostic sufficiency criteria are recorded.
10. Normalization loss record is recorded.
11. Fidelity risk levels are recorded.
12. AI behavior under insufficient information is recorded.
13. Escalation paths are recorded.
14. Relationship to `tool_action_request` is recorded.
15. Prompt injection and untrusted content handling is recorded.
16. Runtime and scanning boundaries remain disabled.
17. Claims to avoid are recorded.
18. `tools/run_all_local_checks.py` includes the v0.6.7 observation normalization test.

## Out of scope

This checkpoint does not:

- implement sanitizer changes,
- implement normalizer changes,
- implement signal extraction,
- create new raw artifacts,
- build a local lab,
- add static lab fixtures,
- add dry-run lab execution,
- enable runtime execution,
- enable scanning,
- add new scanner integrations,
- create private sales material,
- publish pricing,
- create a commercial contract,
- provide legal advice,
- authorize external network testing,
- authorize credential injection,
- authorize customer-target testing.
