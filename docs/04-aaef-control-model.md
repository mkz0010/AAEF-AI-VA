# AAEF Control Model Draft

## Control Targets

- AI provider usage
- AI input data classification
- Tool action requests
- Authorization decisions
- Credential reference usage
- Tool execution
- Evidence generation
- Human review

## Key Principle

AI output is a request, not authorization.

## Initial Control Areas

### AIUSE: AI Use Controls

- AIUSE-01: AI Provider Use Authorization
- AIUSE-02: Sensitive Data Exclusion
- AIUSE-03: Prompt Data Minimization
- AIUSE-04: Provider Policy Binding
- AIUSE-05: AI Output Non-Authority
- AIUSE-06: Customer AI Preference Enforcement
- AIUSE-07: AI Input/Output Evidence Logging

### TOOL: Tool Execution Controls

### TGW: Tool Gateway Controls

- TGW-01: Tool Gateway must require a valid authorization_decision_id before execution.
- TGW-02: Tool Gateway must verify target_id, scope_id, tool, operation, and credential_ref binding.
- TGW-03: Tool Gateway must expose only narrow approved tool adapter operations.
- TGW-04: Tool Gateway must reject arbitrary AI-generated shell commands.
- TGW-05: Tool Gateway must resolve credential_ref only after authorization.
- TGW-06: Tool Gateway must prevent raw secrets from being returned to AI.
- TGW-07: Tool Gateway must hand off raw artifacts to Sanitizer / Normalizer.
- TGW-08: Tool Gateway must emit execution metadata to Evidence Store.
- TGW-09: Tool Gateway must fail closed when required evidence cannot be recorded.


- Tool actions must be requested through Tool Gateway.
- Tools must not be executed directly by AI.
- Tool actions must reference approved targets and scopes.
- Destructive or high-risk tests require explicit human approval.

### CRED: Credential Reference Controls

- AI receives credential_ref only.
- Raw credentials are stored in Vault.
- Tool Gateway injects secrets only into approved tool runtimes.
- Evidence must record credential_ref usage without exposing raw secrets.
