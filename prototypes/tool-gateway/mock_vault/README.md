# Mock Vault

## Metadata

`metadata.json` contains fictitious credential_ref metadata only.

It does not contain raw secrets.

The MVP mock runner uses this metadata to validate whether a credential_ref is allowed for a given target, scope, tool, and operation.


This directory is a placeholder for MVP mock Vault design notes.

Do not commit raw credentials, passwords, API keys, session cookies, VPN credentials, MFA seeds, or other secrets.

For the MVP prototype, use only fictitious metadata in committed files. Any local mock secret material must be stored under ignored paths such as:

- private-not-in-git/
- secrets/
- vault/
