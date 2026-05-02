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

The AI must never receive raw credentials.

## Security Value

- AI does not see passwords, API keys, cookies, MFA secrets, or VPN credentials.
- Tool Gateway injects secrets only after authorization.
- Vault and Tool Gateway form part of the trusted control boundary.
- Evidence records the use of credential_ref without exposing the underlying secret.
