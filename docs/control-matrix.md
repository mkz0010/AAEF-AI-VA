# Control Matrix

Status: candidate
Version: v0.6.152
Date: 2026-05-11

## Reader

This matrix is for enterprise reviewers, vulnerability assessment company decision-makers, security architects, technical due-diligence reviewers, project sponsors, and maintainers reviewing AAEF-AI-VA after the Enterprise Review Guide, Technical Due Diligence Summary, and Safe PoC Boundary Template.

## Purpose

The purpose of this matrix is to align reviewer-facing questions, control boundaries, expected evidence, related artifacts, explicit non-goals, and reviewer notes.

Core boundary proposition:

~~~text
AI output is a request; gates decide execution.
~~~

The matrix helps reviewers inspect the current documentation and evidence boundaries without treating the project as a compliance matrix, audit checklist, certification checklist, production readiness checklist, or permission structure.

## Non-authorizing notice

This matrix is not a certification checklist.

This matrix is not a legal compliance checklist.

This matrix is not an audit checklist.

This matrix does not approve runtime execution.

This matrix does not approve scanner execution.

This matrix does not grant permission to test any system.

This matrix does not create customer PoC approval.

This matrix does not create a commercial contract.

This matrix does not approve credential injection.

This matrix does not approve customer delivery.

## How to read this matrix

Each row should be read as a review aid.

A row identifies:

* the reviewer question,
* the control boundary being inspected,
* expected evidence,
* related artifact or test family,
* explicit non-goal,
* reviewer note.

A row is not a compliance control, certification requirement, audit procedure, legal conclusion, deployment approval, or authorization record.

## Matrix row design

| Column | Meaning |
| --- | --- |
| Review question | What the reviewer should ask. |
| Control boundary | What boundary AAEF-AI-VA intends to make visible. |
| Expected evidence | What evidence or record should support review. |
| Related artifacts | Where reviewers should look. |
| Explicit non-goal | What the row must not be interpreted to prove. |
| Reviewer note | Practical interpretation note. |

## Control matrix

| ID | Review question | Control boundary | Expected evidence | Related artifacts | Explicit non-goal | Reviewer note |
| --- | --- | --- | --- | --- | --- | --- |
| CM-01 | Did the AI request an action without becoming the authority for that action? | AI request is not authority | AI request record, gate input, and evidence linkage | Enterprise Review Guide; Technical Due Diligence Summary; Tool Gateway tests | Does not prove autonomous execution safety | Review model output as a request object, not a permission object. |
| CM-02 | Did a gate decide whether the action was allowed, blocked, or required human review? | Gate decision boundary | Gate decision record and outcome status | Tool Gateway runner tests; human approval gate tests; evidence chain tests | Does not approve real tool execution | Review the gate outcome before reviewing any result. |
| CM-03 | Was authorization evaluated against the relevant current time? | Current-time authorization expiry | Authorization expiry evaluation result | Authorization expiry current-time helper and tests | Does not create a live authorization record | Expired or missing authorization should fail closed or require review. |
| CM-04 | Did request constraints drift from decision constraints? | Request/decision constraint drift | Constraint-diff result | Request/decision constraint-diff helper and tests | Does not prove all possible constraint drift cases | Compare allowed targets, action types, and execution conditions. |
| CM-05 | Did external discovery fail closed unless explicitly allowed and boundary-compatible? | External discovery fail-closed behavior | External discovery gate result | External discovery fail-closed helper and tests | Does not permit external discovery | External target expansion should remain blocked unless explicitly approved. |
| CM-06 | Are mock/dry-run completed statuses disambiguated from real execution completion? | Mock/dry-run status disambiguation | Reviewer-facing status and no-real-execution status | Mock/dry-run completed status terminology helper and tests | Does not prove real execution completion | A mock or dry-run completed status should remain reviewer-visible as non-real-execution. |
| CM-07 | Is non-execution explicitly evidenced? | Non-execution evidence | Blocked, mocked, dry-run, or review-required record | Evidence chain linkage; reconstruction report tests; generated output validation | Does not imply a finding was validated | Non-execution should be reviewable, not hidden as absence of data. |
| CM-08 | Is human approval action-bound and evidence-linked? | Human approval boundary | Human approval record and gate result | Human approval gate tests; finding review gate tests | Does not replace risk-owner authorization | Human approval should identify the action and supporting evidence. |
| CM-09 | Are credentials and sensitive data kept out of AI-visible and public artifacts? | Credential and data handling | Credential reference, redaction result, private artifact exclusion | Sanitizer/redaction tests; credential_ref mock Vault metadata tests; publication hygiene tests | Does not approve credential injection | Review references and redaction behavior before any credential discussion. |
| CM-10 | Are private outputs separated from public documentation? | Public/private artifact boundary | Private-not-in-git paths and hygiene validation | Publication hygiene tests; public repository readiness tests | Does not prove all private operational material is safe to publish | Keep raw outputs, secrets, customer data, and operational playbooks outside public docs. |
| CM-11 | Are findings, reports, packets, and delivery authorization separated? | Report and delivery boundary | Finding review, report promotion, report review, packet review, and delivery gate records | Finding/review/report/packet/delivery gate tests | Does not approve customer delivery | Delivery should require a separate gate after report packet review. |
| CM-12 | Does the PoC boundary template avoid granting permission? | PoC non-authorization boundary | Non-authorizing notice, required fields, exclusions, stop conditions | Safe PoC Boundary Template; v0.6.150 review record | Does not approve any customer PoC | Blank fields and template completion should not be treated as permission. |
| CM-13 | Are commercial and license limits separated from technical review? | Commercial and license boundary | License/commercial boundary language and review notes | Safe PoC Boundary Template; licensing/commercial-use boundary tests | Does not create a commercial contract | Commercial terms require separate review and agreement. |
| CM-14 | Are conservative claim boundaries explicit? | Conservative claim boundaries | No-certification, no-legal, no-audit, no-production, no-equivalence, no-diagnostic-completeness statements | Enterprise Review Guide; Technical Due Diligence Summary; Safe PoC Boundary Template; README | Does not assert conformity or sufficiency | Use the matrix to find overclaims, not to make them. |

## Matrix interpretation limits

This matrix is intentionally narrow.

It helps reviewers locate boundaries and evidence expectations.

It does not make claims about:

* certification,
* legal compliance,
* audit sufficiency,
* production readiness,
* diagnostic completeness,
* permission to test third-party systems,
* customer PoC approval,
* commercial contract creation,
* external-framework equivalence,
* AAEF Core/Profile/Practical Package status.

## Claim boundaries

This matrix must remain conservative.

Do not interpret this matrix as:

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
AAEF-AI-VA provides a reviewer-facing matrix for locating control boundaries, expected evidence, related artifacts, explicit non-goals, and reviewer notes across its current safety-first documentation package.
~~~
