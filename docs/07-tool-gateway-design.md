# Tool Gateway Design Draft

## Role

## Trusted Control Boundary

Tool Gateway is a trusted control boundary.

It is the component that prevents AI-generated tool requests from becoming direct execution authority.

Tool Gateway must not be implemented as:

- a generic shell wrapper,
- an unrestricted command runner,
- a blind executor of AI-generated commands,
- a convenience layer that bypasses AAEF authorization.

Tool Gateway must execute only authorized, constrained, known operations through approved tool adapters.


Tool Gatewayは、AIからの診断アクション要求を直接実行せず、AAEF Authorization Gatewayによる認可済みアクションのみを診断ツールへ渡す。

## Initial Tools

- OWASP ZAP
- Nmap
- nuclei

## Later Tools

- Burp Suite
- Nessus / Tenable
- Browser automation
- Custom validation scripts

## Responsibilities

## credential_ref Responsibilities

When a tool action requires authentication, Tool Gateway is responsible for:

- verifying the authorization_decision_id,
- verifying that the requested credential_ref is allowed,
- resolving credential_ref through Vault or mock Vault,
- injecting the secret into the approved tool runtime,
- preventing the secret from being returned to AI,
- sending raw output to Sanitizer / Normalizer,
- recording credential_ref usage in Evidence Store without exposing the raw secret.

Tool Gateway must not accept arbitrary AI-generated shell commands as equivalent to authorized tool actions.


- Validate authorized tool actions.
- Retrieve secrets from Vault when required.
- Inject secrets into approved tool runtimes.
- Enforce target scope and execution constraints.
- Capture execution logs.
- Send raw artifacts to Sanitizer / Normalizer.
- Prevent direct AI-to-tool unrestricted execution.
