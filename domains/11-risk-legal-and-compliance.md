# Domain 11: Risk, Legal & Compliance (329571)

*Governing trust in a human-agent enterprise*

**Classification:** Management Function
**Version:** v0.1 (Draft)

---

## Overview

This domain encompasses the enterprise's ability to identify, assess, and mitigate risk, provide legal counsel, ensure regulatory compliance, conduct independent assurance, and uphold ethical standards. It is the domain where organisational trust is built, protected, and demonstrated to regulators, customers, and the public.

In a ZORBA-enabled enterprise, this domain bears a critical additional responsibility: **governing the behaviour, compliance, and trustworthiness of AI agents** — ensuring algorithmic decisions are explainable, auditable, and aligned with regulatory expectations and organisational values.

---

## ZORBA Hierarchy: Domain → Capability → Process

```
ZORBA Level    │  APQC Equivalent     │  Description
───────────────┼──────────────────────┼─────────────────────────────────────
Domain         │  Category            │  Major area of enterprise activity
Capability     │  Process Group       │  What the organisation can do
Process        │  Process             │  How work flows to deliver a capability
```

---

## Capabilities & Processes

### 11.1 Manage Enterprise Risk (481327)

Identify, assess, treat, and monitor risks across the enterprise — maintaining the risk register, operating risk frameworks, and ensuring risks are owned, communicated, and actively managed.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.1.1 | Maintain the enterprise risk framework and taxonomy | 724619 | H+a — Humans design the framework; agents maintain documentation and version control |
| 11.1.2 | Identify and register risks across domains and units | 358241 | H=A — Agents scan for emerging risks and prompt registration; humans validate and classify |
| 11.1.3 | Assess and score risks by likelihood and impact | 916473 | H=A — Agents compute risk scores using agreed methodologies; humans exercise qualitative judgement |
| 11.1.4 | Define and track risk treatment plans | 542168 | H+a — Humans design treatments; agents track implementation and flag overdue actions |
| 11.1.5 | Monitor the risk landscape and produce risk reports | 273894 | h+A — Agents monitor continuously and generate risk dashboards; humans interpret for leadership |
| 11.1.6 | Conduct risk scenario analysis and stress testing | 685312 | H=A — Agents run simulations and model scenarios; humans define parameters and interpret results |

---

### 11.2 Provide Legal Services and Manage Contracts (817432)

Deliver legal counsel to the enterprise, manage the contract lifecycle, handle disputes and litigation, and ensure the organisation's legal interests are protected.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.2.1 | Provide legal advice and counsel to business units | 439256 | H — Human-led; legal judgement requires qualified human practitioners |
| 11.2.2 | Draft, review, and negotiate contracts | 763148 | H+a — Humans lead negotiation and review; agents draft from templates and flag non-standard clauses |
| 11.2.3 | Manage the contract lifecycle and obligations tracking | 291875 | h+A — Agents track milestones, renewals, and obligations; humans handle exceptions and renegotiations |
| 11.2.4 | Manage disputes, litigation, and regulatory proceedings | 648312 | H — Human-led; agents manage case files, deadlines, and document assembly |
| 11.2.5 | Maintain the legal entity structure and corporate records | 527493 | h+A — Agents maintain records and filing calendars; humans authorise structural changes |
| 11.2.6 | Manage intellectual property and brand protection | 184736 | H+a — Humans make IP strategy decisions; agents monitor infringement and manage filings |

---

### 11.3 Ensure Regulatory Compliance (265918)

Monitor the regulatory environment, interpret obligations, implement compliance programmes, and demonstrate adherence to all applicable laws, regulations, and industry standards.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.3.1 | Monitor and interpret regulatory changes and obligations | 834152 | h+A — Agents scan regulatory feeds and summarise changes; humans assess applicability |
| 11.3.2 | Design and implement compliance programmes | 496731 | H+a — Humans design programmes; agents operationalise controls and track adoption |
| 11.3.3 | Conduct compliance assessments and testing | 713549 | H=A — Agents execute automated compliance checks; humans investigate exceptions |
| 11.3.4 | Manage regulatory filings and submissions | 358274 | h+A — Agents prepare and submit filings; humans review and approve before submission |
| 11.3.5 | Manage relationships with regulators and supervisory bodies | 621483 | H — Human-led; regulatory relationships require human diplomacy and judgement |

---

### 11.4 Conduct Internal Audit and Assurance (742613)

Provide independent, objective assurance over the effectiveness of governance, risk management, and internal controls — operating with professional scepticism and organisational independence.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.4.1 | Develop the risk-based internal audit plan | 318947 | H+a — Humans set audit priorities; agents analyse risk data to inform planning |
| 11.4.2 | Execute audit engagements and fieldwork | 856271 | H=A — Agents perform data analytics and automated testing; humans conduct interviews and assess controls |
| 11.4.3 | Report audit findings and recommendations | 493128 | H+a — Humans form opinions and present findings; agents draft reports and track management responses |
| 11.4.4 | Monitor remediation of audit findings | 627314 | h+A — Agents track action completion and escalate overdue items; humans validate remediation quality |
| 11.4.5 | Assess internal audit effectiveness and independence | 185439 | H — Human-led; independence assessment requires human objectivity |

---

### 11.5 Protect Data Privacy and Personal Information (593148)

Ensure the enterprise collects, processes, stores, and shares personal data lawfully, transparently, and securely — meeting the requirements of privacy regulations and respecting individual rights.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.5.1 | Maintain the data privacy framework and policies | 274831 | H+a — Humans set privacy policy; agents track regulatory changes and flag required updates |
| 11.5.2 | Conduct data protection impact assessments | 816542 | H=A — Agents perform automated data mapping and initial assessments; humans evaluate high-risk processing |
| 11.5.3 | Manage data subject rights requests | 439617 | h+A — Agents process requests, locate data, and prepare responses; humans approve complex cases |
| 11.5.4 | Monitor data processing activities for compliance | 758243 | A — Agent-executed; continuous monitoring of data flows against consent and purpose records |
| 11.5.5 | Manage data breach notification and response | 361829 | H+a — Humans lead response and notification decisions; agents detect breaches and manage timelines |

---

### 11.6 Uphold Ethics and Standards of Conduct (428173)

Establish and enforce the ethical standards, codes of conduct, and behavioural expectations that govern how people — and agents — operate within the enterprise.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.6.1 | Define and maintain the code of ethics and conduct | 537284 | H — Human-led; ethical standards require human moral reasoning |
| 11.6.2 | Deliver ethics awareness and training programmes | 841396 | H=A — Agents deliver training modules and track completion; humans facilitate ethical reasoning discussions |
| 11.6.3 | Operate whistleblowing and speak-up channels | 629471 | H+a — Humans manage investigations; agents operate reporting channels and ensure anonymity |
| 11.6.4 | Investigate ethical violations and misconduct | 382514 | H — Human-led investigation; agents manage case files and evidence assembly |
| 11.6.5 | Monitor organisational culture and ethical climate | 714928 | H=A — Agents analyse survey data and behavioural signals; humans interpret and intervene |

---

### 11.7 Govern AI Agents and Ensure Algorithmic Compliance (196482)

*ZORBA-specific capability.* Establish and operate the governance framework for AI agents — ensuring their decisions are explainable, their behaviour is auditable, their outputs are fair, and their operation complies with emerging AI regulations and organisational policies.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 11.7.1 | Define and maintain the AI governance framework and policies | 853217 | H+a — Humans set governance principles; agents maintain the policy repository and version history |
| 11.7.2 | Conduct algorithmic impact assessments before deployment | 472831 | H=A — Agents run bias testing and impact simulations; humans evaluate results and approve deployment |
| 11.7.3 | Monitor agent decisions for fairness, bias, and drift | 618943 | h+A — Agents continuously monitor decision patterns and flag anomalies; humans investigate and remediate |
| 11.7.4 | Maintain audit trails and explainability records for agent actions | 345176 | A — Agent-executed; automated logging and explainability record generation |
| 11.7.5 | Ensure compliance with AI-specific regulations and standards | 729368 | H=A — Agents track evolving AI regulation; humans interpret obligations and design compliance responses |
| 11.7.6 | Manage AI incident response and agent-related escalations | 561294 | H+a — Humans lead incident response; agents isolate affected agents and preserve evidence |
| 11.7.7 | Report on AI governance maturity and agent compliance posture | 284713 | h+A — Agents generate compliance dashboards; humans present to governance bodies and regulators |

---

## Summary

| Capability | ID | Process Count |
|-----------|-----|---------------|
| 11.1 Manage Enterprise Risk | 481327 | 6 |
| 11.2 Provide Legal Services and Manage Contracts | 817432 | 6 |
| 11.3 Ensure Regulatory Compliance | 265918 | 5 |
| 11.4 Conduct Internal Audit and Assurance | 742613 | 5 |
| 11.5 Protect Data Privacy and Personal Information | 593148 | 5 |
| 11.6 Uphold Ethics and Standards of Conduct | 428173 | 5 |
| 11.7 Govern AI Agents and Ensure Algorithmic Compliance | 196482 | 7 |
| **Total** | | **39 processes** |

---

## Agentic Profile Legend

| Code | Meaning |
|------|---------|
| **H** | Human-only — agent participation not appropriate |
| **H+a** | Human-led with light agent support |
| **H=A** | Balanced human-agent collaboration |
| **h+A** | Agent-led with human oversight or approval |
| **A** | Agent-autonomous within defined boundaries |

---

*Part of the [ZORBA Domain Reference Model](../04-domain-reference.md)*

---

*© 2026 Zontally. All rights reserved.*
