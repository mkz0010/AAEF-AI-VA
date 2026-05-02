# Architecture Draft

## Logical Flow

~~~text
Customer Documents / Scope Materials
  ↓
Document Intake & Data Classification
  ↓
Scope Extraction Agent
  ↓
Human Scope Review
  ↓
AAEF Authorization Gateway
  ↓
Tool Action Request
  ↓
Tool Gateway
  ↓
Vault / Credential Store
  ↓
Burp / ZAP / Nmap / nuclei / Nessus / Browser Automation
  ↓
Target System
  ↓
Raw Scan Artifacts
  ↓
Sanitizer / Normalizer
  ↓
Evidence Store
  ↓
Finding Triage Agent
  ↓
Human Review
  ↓
Report Generator
~~~

## Design Rule

AI does not directly access customer systems, secrets, credentials, or unrestricted shells.

## Trusted Components

- AAEF Authorization Gateway
- Tool Gateway
- Vault / Credential Store
- Evidence Store
- Sanitizer / Normalizer

## Untrusted or Restricted Components

- LLM output
- AI-generated tool action requests
- Raw scanner output before sanitization
- Customer-provided documents before classification
