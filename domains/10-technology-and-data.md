# Domain 10: Technology & Data (847261)

*Powering the enterprise with platforms and insight*

**Classification:** Management Function
**Version:** v0.1 (Draft)

---

## Overview

This domain encompasses the enterprise's ability to design, build, operate, and evolve its technology landscape — from core infrastructure and applications through to data platforms, cybersecurity, and end-user technology services. It ensures technology investments align with strategic intent and that data is treated as a first-class enterprise asset.

In a ZORBA-enabled enterprise, this domain carries a unique additional responsibility: **managing the agent platform itself**. The technology function not only deploys agents — it operates the infrastructure, tooling, and guardrails that make the blended workforce possible.

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

### 10.1 Shape Technology Strategy and Architecture (529147)

Define the technology vision, principles, and enterprise architecture that guide investment decisions, platform choices, and the evolution of the technology estate.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.1.1 | Define the enterprise technology vision and principles | 631824 | H — Human-led; technology strategy requires human judgement on business priorities |
| 10.1.2 | Develop and maintain enterprise architecture standards | 274953 | H=A — Agents maintain architecture artefacts; humans set standards and make trade-offs |
| 10.1.3 | Assess emerging technologies and evaluate adoption readiness | 918362 | h+A — Agents scan, evaluate, and benchmark; humans decide strategic relevance |
| 10.1.4 | Manage the technology investment portfolio and roadmap | 453271 | H+a — Humans prioritise investments; agents model costs and dependencies |
| 10.1.5 | Govern architecture conformance and technical debt | 186439 | H=A — Agents detect drift and debt; humans approve remediation priorities |

---

### 10.2 Build and Manage Applications (362819)

Design, develop, test, deploy, and maintain the enterprise's application portfolio — including custom-built, configured, and integrated software solutions.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.2.1 | Gather and prioritise application requirements | 741258 | H=A — Agents collect and structure requirements; humans validate and prioritise |
| 10.2.2 | Design and architect application solutions | 529463 | H+a — Humans design; agents generate reference architectures and patterns |
| 10.2.3 | Develop and configure application code | 384716 | h+A — Agents generate and refactor code; humans review, approve, and guide |
| 10.2.4 | Test and validate application quality | 862147 | h+A — Agents execute automated test suites; humans define test strategies and review edge cases |
| 10.2.5 | Deploy and release applications to production | 195384 | H=A — Agents orchestrate CI/CD pipelines; humans approve production releases |
| 10.2.6 | Manage the application portfolio lifecycle | 647932 | H=A — Agents track usage, costs, and health; humans decide rationalisation actions |

---

### 10.3 Operate Infrastructure and Cloud Platforms (714538)

Provision, manage, and optimise the enterprise's computing infrastructure — including on-premises, cloud, hybrid, and edge environments.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.3.1 | Provision and configure infrastructure resources | 428163 | h+A — Agents execute infrastructure-as-code; humans define policies and approve changes |
| 10.3.2 | Monitor infrastructure health and performance | 563291 | A — Agent-autonomous; continuous monitoring with human-defined alert thresholds |
| 10.3.3 | Manage capacity planning and resource optimisation | 819427 | h+A — Agents forecast and recommend; humans approve scaling decisions |
| 10.3.4 | Operate cloud platform services and governance | 246875 | H=A — Agents enforce guardrails and track spend; humans set cloud strategy |
| 10.3.5 | Execute infrastructure auto-remediation and self-healing | 738514 | A — Agent-autonomous; automated remediation within predefined runbooks |
| 10.3.6 | Manage network and connectivity services | 391648 | H=A — Agents monitor and configure; humans approve topology changes |

---

### 10.4 Govern Data and Deliver Analytics (283946)

Manage data as an enterprise asset — ensuring quality, accessibility, governance, and the delivery of analytics and insights that drive decision-making.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.4.1 | Define data governance frameworks and ownership | 625813 | H+a — Humans define governance; agents maintain catalogues and lineage |
| 10.4.2 | Manage data quality, profiling, and remediation | 948271 | h+A — Agents profile and cleanse data; humans set quality thresholds and resolve exceptions |
| 10.4.3 | Build and operate data pipelines and integration | 174593 | A — Agent-executed; automated pipeline orchestration with human-defined schemas |
| 10.4.4 | Deliver business intelligence and reporting | 536184 | h+A — Agents generate dashboards and reports; humans interpret and act on insights |
| 10.4.5 | Develop and manage advanced analytics and models | 812367 | H=A — Agents train and tune models; humans validate methodology and interpret results |
| 10.4.6 | Manage master data and reference data | 469752 | H=A — Agents maintain records; humans resolve conflicts and approve golden records |

---

### 10.5 Protect Information and Ensure Cyber Resilience (492638)

Defend the enterprise against cyber threats, manage information security risks, and ensure resilience through detection, response, and recovery capabilities.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.5.1 | Define cybersecurity strategy and risk posture | 317524 | H — Human-led; security strategy requires executive judgement and risk appetite alignment |
| 10.5.2 | Manage identity, access, and authentication controls | 853162 | H=A — Agents enforce policies and detect anomalies; humans approve access exceptions |
| 10.5.3 | Monitor threats and operate security operations | 246819 | A — Agent-autonomous; continuous threat monitoring and initial incident triage |
| 10.5.4 | Respond to and recover from security incidents | 671438 | H+a — Humans lead incident response; agents execute containment playbooks and collect forensics |
| 10.5.5 | Conduct vulnerability management and penetration testing | 594273 | h+A — Agents scan and prioritise vulnerabilities; humans validate findings and approve remediation |
| 10.5.6 | Manage security awareness and training | 738291 | H=A — Agents deliver training and simulate phishing; humans design curriculum and review results |

---

### 10.6 Deliver Technology Operations and End-User Support (158493)

Operate the day-to-day technology services that keep the enterprise running — including service desk, incident management, problem resolution, and end-user computing.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.6.1 | Operate the service desk and manage service requests | 824367 | h+A — Agents handle tier-0/1 requests; humans manage complex escalations |
| 10.6.2 | Manage incidents and restore services | 396142 | H=A — Agents detect, categorise, and initiate response; humans lead major incident resolution |
| 10.6.3 | Conduct problem management and root cause analysis | 571829 | H+a — Humans lead analysis; agents correlate data and suggest patterns |
| 10.6.4 | Manage change and release processes | 249618 | H=A — Agents assess impact and schedule changes; humans approve and review |
| 10.6.5 | Provision and manage end-user devices and workplace technology | 683475 | h+A — Agents automate provisioning and configuration; humans handle exceptions |

---

### 10.7 Manage the Agent Platform (925743)

Operate, evolve, and govern the infrastructure that enables enterprise AI agents — including agent hosting, orchestration, lifecycle management, and the tooling that connects agents to enterprise systems. This is the ZORBA-specific meta-capability: the technology that enables the blended workforce.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 10.7.1 | Operate agent hosting infrastructure and runtime environments | 348261 | H=A — Agents monitor their own platform; humans manage capacity and architecture |
| 10.7.2 | Manage agent lifecycle — provisioning, versioning, and retirement | 517948 | H+a — Humans approve agent deployment; agents manage version control and rollback |
| 10.7.3 | Govern agent access to enterprise systems and data | 264839 | H — Human-led; access decisions require accountability and policy alignment |
| 10.7.4 | Monitor agent performance, health, and resource consumption | 893162 | A — Agent-autonomous; agents monitor agent fleet health and flag anomalies |
| 10.7.5 | Manage agent orchestration and inter-agent coordination | 471526 | H=A — Agents execute orchestration; humans define workflow boundaries and escalation rules |
| 10.7.6 | Maintain the agent tooling ecosystem and integration layer | 635274 | H=A — Agents maintain integrations; humans approve new tool access and capabilities |
| 10.7.7 | Manage agent platform security and isolation | 182943 | H+a — Humans set security policies; agents enforce isolation and detect breaches |

---

## Summary

| Capability | ID | Process Count |
|-----------|-----|---------------|
| 10.1 Shape Technology Strategy and Architecture | 529147 | 5 |
| 10.2 Build and Manage Applications | 362819 | 6 |
| 10.3 Operate Infrastructure and Cloud Platforms | 714538 | 6 |
| 10.4 Govern Data and Deliver Analytics | 283946 | 6 |
| 10.5 Protect Information and Ensure Cyber Resilience | 492638 | 6 |
| 10.6 Deliver Technology Operations and End-User Support | 158493 | 5 |
| 10.7 Manage the Agent Platform | 925743 | 7 |
| **Total** | | **41 processes** |

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
