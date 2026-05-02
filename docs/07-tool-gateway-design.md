# Tool Gateway Design Draft

## Role

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

- Validate authorized tool actions.
- Retrieve secrets from Vault when required.
- Inject secrets into approved tool runtimes.
- Enforce target scope and execution constraints.
- Capture execution logs.
- Send raw artifacts to Sanitizer / Normalizer.
- Prevent direct AI-to-tool unrestricted execution.
