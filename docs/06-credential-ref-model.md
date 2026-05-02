# credential_ref Model Draft

## Concept

AIには認証情報の実値を渡さず、credential_refのみを渡す。

## Example

~~~json
{
  "target_id": "webapp-001",
  "auth_profile": "standard-user",
  "credential_ref": "test-account-001",
  "requested_action": "authenticated_crawl"
}
~~~

## Execution Flow

~~~text
AI
  ↓
Tool Action Request
  ↓
AAEF Authorization Gateway
  ↓
Tool Gateway
  ↓
Vault
  ↓
Approved Tool Runtime
~~~

## Rule

## Lifecycle Summary

A credential_ref follows this lifecycle:

1. create,
2. authorize use,
3. resolve,
4. inject,
5. execute,
6. sanitize,
7. record evidence,
8. revoke or expire.

Detailed lifecycle requirements are defined in `docs/12-credential-ref-flow.md`.

## Visibility Boundary

AI may see `credential_ref`, `target_id`, `scope_id`, `tool`, `operation`, and sanitized result summaries.

AI must not see raw usernames, passwords, session cookies, API keys, bearer tokens, VPN credentials, MFA seeds, or raw authorization headers.


The AI must never receive raw credentials.

## Security Value

- AI does not see passwords, API keys, cookies, MFA secrets, or VPN credentials.
- Tool Gateway injects secrets only after authorization.
- Vault and Tool Gateway form part of the trusted control boundary.
- Evidence records the use of credential_ref without exposing the underlying secret.
