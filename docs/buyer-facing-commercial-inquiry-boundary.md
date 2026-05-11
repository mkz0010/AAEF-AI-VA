# Buyer-Facing Commercial Inquiry Boundary

Status: candidate
Version: v0.6.164
Date: 2026-05-12

## Reader

This boundary is for buyer-facing readers, vulnerability assessment company decision-makers, commercial reviewers, sponsors, maintainers, and enterprise reviewers who want to ask about AAEF-AI-VA without turning public review language into authorization, contract, delivery, or production claims.

## Purpose

The purpose of this boundary is to clarify how commercial inquiry should be interpreted.

Core boundary proposition:

~~~text
AI output is a request; gates decide execution.
~~~

Commercial inquiry is not action authority.

Commercial inquiry is not PoC approval.

Commercial inquiry is not runtime approval.

Commercial inquiry is not scanner approval.

Commercial inquiry is not delivery approval.

## Contact channel

Email-based inquiry is the selected contact model.

The public repository does not commit an email address in this candidate.

Use the maintainer-provided email address when it is published or otherwise provided by the maintainer.

Do not infer a contact address from repository metadata, commit history, private files, generated outputs, or unrelated public profiles.

## Allowed commercial inquiry topics

Commercial readers may ask about:

* project overview and positioning,
* external review package navigation,
* licensing and commercial-use boundaries,
* evaluation discussion,
* non-authorizing PoC boundary concepts,
* high-level integration questions,
* responsibility and authority boundary design,
* evidence/reviewability concepts,
* what information would be needed before a future private discussion.

These inquiries are discussion topics only.

## Topics requiring separate agreement

The following topics require separate written agreement or authorization before they can proceed beyond discussion:

* customer-specific target discussion,
* customer credentials,
* customer environment details,
* customer-specific generated artifacts,
* private implementation guidance,
* paid engagement scope,
* commercial license terms,
* NDA-covered materials,
* customer PoC planning,
* tool execution,
* scanner execution,
* runtime execution,
* credential use,
* customer target use,
* report delivery,
* operational playbooks,
* patent-sensitive browser-state intelligence details.

## Inquiry is not a contract

A commercial inquiry is not a contract.

A reply to a commercial inquiry is not a commercial agreement unless a separate written agreement says so.

This repository does not publish commercial license terms in this candidate.

This repository does not approve a paid engagement through public inquiry language.

## Inquiry does not approve a paid engagement

Commercial inquiry may start a conversation.

It does not approve budget, scope, procurement, paid work, delivery responsibility, acceptance criteria, support responsibility, or commercial license terms.

## Inquiry does not authorize customer PoC activity

Commercial inquiry does not authorize a customer PoC.

A future customer PoC would require a separate written boundary, separate customer/asset authorization, separate scope, separate time window, separate tool constraints, separate evidence handling, separate credential handling, separate stop conditions, and separate responsibility acceptance.

## Inquiry does not authorize runtime or scanner execution

Commercial inquiry does not authorize runtime execution.

Commercial inquiry does not authorize scanner execution.

Commercial inquiry does not authorize Docker execution.

Commercial inquiry does not authorize use of ZAP, Nmap, nuclei, browser automation, or any other diagnostic tool against any system.

## Inquiry does not authorize credential use, customer target use, or delivery

Commercial inquiry does not authorize credential use.

Commercial inquiry does not authorize customer target use.

Commercial inquiry does not authorize report delivery.

Commercial inquiry does not authorize delivery package approval.

Commercial inquiry does not authorize third-party testing.

## Relationship to the External Review Package

Commercial readers should first review:

~~~text
docs/external-review-package.md
~~~

The External Review Package explains the safe public review path.

Commercial inquiry should build on that review path, not bypass it.

## Relationship to the Safe PoC Boundary Template

Commercial inquiry may refer to:

~~~text
docs/safe-poc-boundary-template.md
~~~

The Safe PoC Boundary Template helps identify information that would be needed before a future controlled PoC could even be discussed.

The template is not permission.

The template is not a contract.

The template is not approval to test.

## Relationship to licensing and commercial-use boundaries

The public code implementation is AGPL-3.0.

Commercial inquiry may ask about commercial licensing, but public inquiry language does not create commercial license terms.

Any commercial license, paid engagement, embedding arrangement, or private implementation discussion would require separate written agreement.

## Public/private material boundary

The public repository should not include:

* customer targets,
* customer credentials,
* customer contracts,
* commercial license terms,
* private generated artifacts,
* raw scanner output,
* customer-specific report materials,
* paid engagement scope,
* NDA materials,
* patent-sensitive browser-state intelligence details,
* operational customer delivery playbooks.

## Claim boundaries

Do not interpret commercial inquiry as:

* certification,
* legal compliance determination,
* audit opinion,
* audit sufficiency determination,
* production readiness,
* production scanner status,
* diagnostic completeness,
* authorization for third-party testing,
* customer PoC approval,
* commercial contract creation,
* commercial license terms creation,
* paid engagement approval,
* customer delivery approval,
* equivalence with external frameworks,
* AAEF Core/Profile/Practical Package promotion.

Allowed interpretation:

~~~text
AAEF-AI-VA provides a public boundary for asking commercial questions without converting inquiry into authorization, contract, delivery, or production claims.
~~~
