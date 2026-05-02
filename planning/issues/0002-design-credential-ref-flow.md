# 0002: Design credential_ref flow

## Status

In Progress

## Priority

P0

## Type

Design

## Background

AIに認証情報を渡さず、credential_refのみで認証付き診断を実行する方式を設計する。

この設計は、外部AI利用時のNDA、顧客秘密、認証情報保護、証跡管理における中核となる。

## Decision Summary

credential_ref is a reference-only identifier visible to AI.

The raw secret is stored in Vault or mock Vault and can be resolved only by Tool Gateway after an AAEF authorization decision.

AI may request an action that references credential_ref, but AI cannot resolve it, inspect it, or treat it as authority.

## Lifecycle

The credential_ref lifecycle is:

1. create,
2. authorize use,
3. resolve,
4. inject,
5. execute,
6. sanitize,
7. record evidence,
8. revoke or expire.

## AI-visible Fields

- target_id
- scope_id
- tool
- operation
- credential_ref
- auth_profile
- allowed_actions
- prohibited_actions
- sanitized_result_summary

## AI-hidden Fields

- username
- password
- session cookie
- API key
- bearer token
- VPN credential
- MFA seed
- raw Authorization header
- unredacted Set-Cookie header
- raw secret values

## Acceptance Criteria

- credential_ref lifecycle is defined
- Vault responsibility is defined
- Tool Gateway responsibility is defined
- AI-visible and AI-hidden fields are separated
- Evidence requirements are defined
- Sanitization requirements for tool output are defined
- Revocation or expiry is addressed
- MVP mock Vault option is addressed

## Related Documents

- docs/12-credential-ref-flow.md
- docs/06-credential-ref-model.md
- docs/07-tool-gateway-design.md
- docs/08-evidence-store-design.md
- planning/decisions/ADR-0006-credential-ref-lifecycle.md

## Remaining Work

- Define mock Vault file format for local prototype.
- Define tool_action_request JSON schema.
- Define authorization_decision JSON schema for MVP.
- Define sanitized evidence record JSON shape.
- Implement first allowed / denied / human-approval examples.
