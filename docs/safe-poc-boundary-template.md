# Safe PoC Boundary Template

Status: candidate
Version: v0.6.149
Date: 2026-05-11

## Reader

This template is for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, and project sponsors who may later consider a controlled AAEF-AI-VA PoC.

## Purpose

The purpose of this template is to define the boundary information that must exist before a future controlled PoC can be considered.

It is a planning and review template only.

Core boundary proposition:

~~~text
AI output is a request; gates decide execution.
~~~

## Non-authorizing notice

This template does not authorize a PoC.

This template does not grant permission to test any system.

This template does not create a commercial contract.

This template does not approve runtime execution.

This template does not approve scanner execution.

This template does not approve credential injection.

This template does not approve customer delivery.

A real PoC would require separate written authorization, legal/commercial review, environment approval, tool approval, credential approval, evidence-handling approval, human-review approval, and stop-condition approval.

## Boundary summary

Fill this section only when a separate PoC approval process exists.

| Field | Required value |
| --- | --- |
| PoC name | TBD |
| Requesting organization | TBD |
| Asset owner | TBD |
| PoC sponsor | TBD |
| Technical owner | TBD |
| Risk owner | TBD |
| Legal/commercial reviewer | TBD |
| Approved target set | TBD |
| Explicit exclusions | TBD |
| Approved time window | TBD |
| Approved tool set | TBD |
| Approved action types | TBD |
| Evidence retention location | TBD |
| Deletion date or retention rule | TBD |
| Human reviewer | TBD |
| Stop-condition owner | TBD |
| Delivery reviewer | TBD |

No blank field should be treated as permission.

## Required written authorization fields

A future controlled PoC should not proceed unless written authorization separately defines:

* asset owner,
* legal authority,
* contract or evaluation basis,
* target inventory,
* excluded systems,
* network boundaries,
* time window,
* action types,
* tool set,
* credential handling,
* data-handling rules,
* evidence retention and deletion,
* human review responsibilities,
* stop conditions,
* communication and escalation path,
* delivery boundary.

This template records required fields. It does not supply authorization.

## Parties and responsibilities

| Role | Responsibility |
| --- | --- |
| PoC sponsor | Owns business reason for evaluation. |
| Asset owner | Confirms ownership and allowed target boundary. |
| Risk owner | Accepts residual evaluation risk after review. |
| Technical owner | Confirms technical environment constraints. |
| Legal/commercial reviewer | Reviews contract, permission, and commercial terms outside this template. |
| Human reviewer | Reviews AI requests, gate decisions, evidence, and outputs. |
| Tool operator | Operates only within separately approved constraints. |
| Stop-condition owner | Can pause or terminate the PoC when conditions are met. |
| Delivery reviewer | Confirms whether any output can be shared. |

## Target scope

A controlled PoC boundary should define:

* target mode,
* target hostnames or addresses,
* owned assets,
* lab assets,
* customer assets, if separately approved,
* environment name,
* network segment,
* allowed protocols,
* allowed ports,
* allowed test accounts,
* target data sensitivity,
* maximum request rate or intensity,
* out-of-band communication restrictions.

If a target is not explicitly listed, it is outside the PoC boundary.

## Excluded systems

A controlled PoC boundary should list exclusions such as:

* production systems,
* third-party systems,
* shared infrastructure,
* unmanaged assets,
* payment systems,
* regulated data stores,
* identity provider systems,
* email systems,
* destructive-test targets,
* social engineering targets,
* denial-of-service targets,
* systems with unclear ownership.

If an exclusion conflicts with an approved target entry, the exclusion should win until separately resolved.

## PoC time window

A controlled PoC boundary should define:

* start date and time,
* end date and time,
* maintenance windows,
* blackout periods,
* daily operating hours,
* time zone,
* emergency stop contact,
* expiration behavior.

PoC authorization should expire automatically outside the written time window.

## Tool and action limits

A controlled PoC boundary should define:

| Category | Boundary |
| --- | --- |
| Allowed tools | TBD |
| Disallowed tools | TBD |
| Allowed action types | TBD |
| Disallowed action types | TBD |
| Passive-only actions | TBD |
| Active actions | TBD |
| Rate limits | TBD |
| Payload constraints | TBD |
| Authentication constraints | TBD |
| Data extraction constraints | TBD |
| Destructive actions | Prohibited unless separately and explicitly approved. |
| Denial-of-service actions | Prohibited unless separately and explicitly approved. |
| Persistence or post-exploitation actions | Prohibited unless separately and explicitly approved. |

## AI request and gate boundary

The PoC boundary should preserve the AAEF-AI-VA proposition:

~~~text
AI output is a request; gates decide execution.
~~~

A future PoC should review:

* what the AI requested,
* what authority existed at decision time,
* whether request constraints matched decision constraints,
* whether authorization was current,
* whether external discovery was explicitly allowed and boundary-compatible,
* whether a human approval gate was required,
* whether execution was blocked, mocked, dry-run, or allowed,
* what evidence proves the outcome.

AI text alone should not be treated as authority.

## Credential and data handling

A controlled PoC boundary should define:

* whether credentials are needed,
* who owns credential issuance,
* whether credential references are used instead of raw secrets,
* where secrets are stored,
* who can access secrets,
* whether AI-visible artifacts are sanitized,
* whether raw logs can be retained,
* which data classes may be processed,
* which data classes are prohibited,
* redaction requirements,
* deletion requirements.

No raw secret should be placed in public documentation or AI-visible text.

## Evidence retention and deletion

A controlled PoC boundary should define:

* evidence types,
* evidence location,
* access controls,
* retention period,
* deletion procedure,
* reviewer access,
* customer access,
* redaction process,
* audit trail for deletion,
* incident handling if sensitive material is captured.

Evidence retention should be separate from delivery authorization.

## Human review and approval

A controlled PoC boundary should define where human review is required:

* before target authorization,
* before credential use,
* before external discovery,
* before active tool execution,
* before evidence promotion,
* before report packet creation,
* before delivery authorization,
* before any scope expansion.

Human approval should be action-bound and evidence-linked.

## Stop conditions

A controlled PoC boundary should define stop conditions such as:

* target ambiguity,
* ownership ambiguity,
* authorization expiry,
* unexpected external discovery,
* unexpected production impact,
* unexpected sensitive data exposure,
* rate-limit breach,
* tool behavior outside approved constraints,
* customer request,
* risk owner request,
* legal/commercial reviewer request,
* incident or suspected incident.

When a stop condition occurs, the safe default is pause and review.

## Communications and escalation

A controlled PoC boundary should define:

* primary contact,
* technical contact,
* risk owner contact,
* legal/commercial contact,
* emergency contact,
* escalation channel,
* expected response time,
* out-of-hours process,
* incident notification process,
* decision log location.

## Deliverables boundary

A controlled PoC boundary should define possible deliverables:

* evidence summary,
* technical review notes,
* sanitized finding candidates,
* reviewed findings,
* report packet candidate,
* delivery package.

Delivery should require a separate delivery authorization gate.

A PoC output should not be treated as customer delivery unless separately approved.

## Commercial and license boundary

A controlled PoC boundary should define:

* evaluation purpose,
* commercial contact,
* license posture,
* allowed internal use,
* prohibited external paid training or resale use unless separately contracted,
* confidentiality terms,
* source code handling,
* derivative work handling,
* third-party dependency review,
* post-PoC continuation terms.

This template does not create a commercial contract.

## Pre-PoC review checklist

Before any future controlled PoC, reviewers should confirm:

| Check | Required result |
| --- | --- |
| Written authorization exists | Required |
| Asset owner identified | Required |
| Risk owner identified | Required |
| Targets explicitly listed | Required |
| Exclusions explicitly listed | Required |
| Time window defined | Required |
| Tool set defined | Required |
| Action limits defined | Required |
| Credential handling defined | Required |
| Evidence retention defined | Required |
| Human review gates defined | Required |
| Stop conditions defined | Required |
| Communication path defined | Required |
| Delivery boundary defined | Required |
| Commercial/license boundary defined | Required |
| Claim boundaries acknowledged | Required |

## Not allowed by this template

This template does not allow:

* testing any system,
* expanding target scope,
* running scanners,
* injecting credentials,
* contacting customer systems,
* collecting customer data,
* bypassing human review,
* bypassing gate decisions,
* treating AI output as authority,
* delivering reports,
* claiming production readiness,
* claiming diagnostic completeness,
* claiming certification,
* claiming legal compliance,
* claiming audit opinion,
* claiming equivalence with external frameworks.

## Claim boundaries

This template must remain conservative.

Do not interpret this template as:

* customer authorization,
* commercial contract,
* legal compliance determination,
* audit opinion,
* audit sufficiency determination,
* deployment approval,
* complete vulnerability assessment capability,
* permission for testing third-party systems,
* equivalence mapping to external frameworks,
* production readiness claim,
* proof that gate-free AI tool execution is acceptable,
* promotion of AAEF-AI-VA into AAEF Core, Profile, or Practical Package status.

Allowed interpretation:

~~~text
AAEF-AI-VA provides a non-authorizing template for defining the boundary information a separately approved controlled PoC would need before any real action is considered.
~~~
