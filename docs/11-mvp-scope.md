# MVP Scope

## Purpose

This document defines the initial MVP scope for the AAEF-controlled AI Vulnerability Assessment Platform.

The MVP is not intended to demonstrate fully autonomous penetration testing. It is intended to demonstrate that AI-assisted vulnerability assessment can be performed under explicit scope, authorization, tool execution, evidence, confidentiality, and human review controls.

## MVP Objective

The MVP should prove the following:

- AI can assist with scope interpretation and assessment planning.
- AI can generate tool action requests without directly executing tools.
- AAEF Authorization Gateway can approve, deny, or constrain requested actions.
- Tool Gateway can execute only approved tool actions.
- credential_ref can separate AI reasoning from raw credentials.
- Evidence can connect scope, authorization, tool execution, observed results, findings, and human review.
- Human review remains the final authority for findings and reports.

## Initial Assessment Scope

The initial MVP focuses on controlled support for:

- Web application vulnerability assessment assistance
- API vulnerability assessment assistance
- Small-scale network vulnerability assessment assistance

The MVP does not attempt to cover full penetration testing, adversary emulation, internal network compromise, exploit chaining, or destructive testing.

## Initial Tool Scope

### Included in MVP

The following tools are in scope for the first MVP:

- OWASP ZAP
- Nmap
- nuclei
- simple browser automation where needed for safe crawling or workflow support

### Deferred Tools

The following tools are deferred until the core control model is stable:

- Burp Suite
- Nessus / Tenable
- cloud security posture tools
- custom exploit validation scripts
- advanced browser automation
- source code analysis tools

Burp Suite and Nessus are important future integrations, but they should not be required for the first proof of the control model.

## Initial AI Scope

AI may assist with:

- reading sanitized or fictitious scope documents,
- extracting target candidates,
- identifying missing scope information,
- drafting assessment plans,
- drafting tool action requests,
- summarizing sanitized scan outputs,
- generating finding candidates,
- mapping findings to CWE / OWASP / CVSS where appropriate,
- drafting report sections.

AI must not directly:

- access customer systems,
- access Vault,
- read raw credentials,
- run shell commands freely,
- execute tools outside Tool Gateway,
- decide final findings,
- approve its own actions,
- expand scope without human approval.

## Initial Data Handling Scope

The MVP should use fictitious, sanitized, or intentionally created demo data.

Real customer contracts, real customer target materials, raw scan logs, credentials, session cookies, API keys, personal data, or confidential vulnerability information must not be committed to Git.

External AI use, if used during the MVP, must follow the draft AI Data Handling Policy:

- use minimum necessary data,
- avoid raw secrets,
- avoid personal data,
- prefer aliases and references,
- record what data classification would apply,
- require human review before use in reporting.

## credential_ref Scope

The MVP should define and demonstrate the credential_ref pattern, even if the first implementation uses a simple local mock Vault.

The intended model is:

~~~text
AI
  ↓
tool_action_request with credential_ref
  ↓
AAEF Authorization Gateway
  ↓
Tool Gateway
  ↓
Vault or mock Vault
  ↓
approved tool runtime
~~~

The AI may know that `credential_ref: test-account-001` exists, but must not receive the raw username, password, session cookie, API key, or other secret value.

## Authorization Scope

The MVP Authorization Gateway should support at least the following decisions:

- allow
- deny
- require_human_approval

The MVP should also support basic constraints:

- target_id
- scope_id
- allowed tool
- allowed operation
- credential_ref usage
- rate limit category
- destructive testing prohibited
- external discovery prohibited
- evidence required

## Evidence Scope

The MVP should capture enough evidence to reconstruct:

- what the AI requested,
- what policy or scope was used,
- what authorization decision was made,
- what tool action was executed,
- what target was assessed,
- what sanitized result was produced,
- what finding candidate was generated,
- what human review decision was made.

The MVP does not need a production-grade evidence store. A structured local JSONL or SQLite-based prototype is sufficient for early validation.

## Explicitly Out of Scope

The following are out of scope for the MVP:

- fully autonomous penetration testing,
- exploit chain automation,
- destructive testing,
- DoS or stress testing,
- brute force,
- credential spraying,
- password attacks,
- lateral movement,
- persistence,
- privilege escalation against real systems,
- production data modification,
- uncontrolled internet-wide scanning,
- unsupervised testing of customer production environments,
- use of raw customer secrets by AI,
- use of raw customer confidential documents in external AI services.

## MVP Success Criteria

The MVP is successful when it can demonstrate the following scenario:

1. A fictitious or sanitized scope document is ingested.
2. AI proposes a limited assessment plan.
3. AI generates a tool action request for an approved target.
4. AAEF Authorization Gateway evaluates the request.
5. Tool Gateway executes only an approved safe action.
6. Evidence is recorded for the request, decision, execution, and result.
7. AI summarizes sanitized results and drafts a finding candidate.
8. Human review confirms, edits, or rejects the finding.
9. A draft report is generated with evidence linkage.
10. No raw credentials or prohibited data are exposed to AI.

## Initial Non-Goals

The initial MVP is not designed to optimize for:

- highest vulnerability discovery rate,
- advanced exploit development,
- fully automated red teaming,
- replacing expert human assessors,
- production-grade multi-tenant SaaS,
- enterprise sales readiness,
- regulatory certification.

The MVP is designed to validate the control architecture first.

## Relationship to AAEF

This MVP is a commercial implementation experiment derived from AAEF.

AAEF remains the conceptual and control framework. This project tests whether AAEF-style authorization, execution control, evidence, and non-authoritative AI output can be applied to AI-assisted vulnerability assessment.
