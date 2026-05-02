# ADR-0025: Add sanitizer and redaction policy scaffold before AI-visible tool output

## Status

Accepted

## Context

The platform now has execution control, review, approval, evidence chain, and reconstruction reporting.

The next major risk is raw adapter output. Real tools may produce credentials, tokens, cookies, request/response bodies, internal IPs, and other sensitive details.

Before real tool integration, the project needs a sanitizer boundary.

## Decision

Add a sanitizer and redaction policy scaffold.

Raw artifacts remain private. Sanitized artifacts may become AI-visible only after sanitizer completion and validation.

The MVP redacts common token, cookie, password, CSRF, session, and private IP patterns.

## Consequences

- Raw adapter output remains separated from AI-visible content.
- Sanitized artifact generation can be tested before real tool execution.
- Future finding normalization can consume sanitized artifacts.
- Evidence claims about secret exposure can later be tied to sanitizer policy version.
