# Domain 7: Supply Chain (824713)

*Building a resilient, responsive supply network*

**Classification:** Value Chain
**Version:** v0.1 (Draft)

---

## Overview

This domain encompasses the enterprise's ability to source, procure, move, store, and distribute goods and services across its extended supply network. It spans from upstream supplier relationships through internal logistics to final-mile delivery, and includes the planning and risk management activities that keep the supply chain responsive and resilient.

In a ZORBA-enabled enterprise, the supply chain is arguably the **most agent-ready domain** — with mature use cases in demand forecasting, inventory optimisation, route planning, supplier monitoring, and autonomous procurement within defined parameters. Agents here operate at scale and speed that human-only models cannot match.

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

### 7.1 Source and Procure Goods and Services (391572)

Identify, evaluate, negotiate, and contract with suppliers to secure the goods and services the enterprise requires — balancing cost, quality, risk, and sustainability objectives.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.1.1 | Define sourcing strategies and category plans | 518234 | H+a — Humans design strategy; agents analyse spend data and market conditions |
| 7.1.2 | Identify and qualify potential suppliers | 673841 | h+A — Agents screen supplier databases and assess fit; humans shortlist |
| 7.1.3 | Conduct sourcing events and negotiate terms | 429187 | H+a — Humans lead negotiations; agents model scenarios and benchmark pricing |
| 7.1.4 | Manage purchase orders and procurement transactions | 856312 | A — Agent-executed; automated PO creation within approved parameters |
| 7.1.5 | Evaluate and onboard new suppliers | 294768 | H=A — Agents run due diligence checks; humans make final approval decisions |
| 7.1.6 | Manage contract compliance and renewal cycles | 731456 | h+A — Agents track contract terms and flag renewals; humans negotiate amendments |

---

### 7.2 Manage Supplier Relationships and Performance (562381)

Build, maintain, and govern ongoing relationships with suppliers — monitoring performance, managing development, and ensuring mutual value creation across the supply base.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.2.1 | Segment and tier the supplier base | 184329 | H=A — Agents analyse spend and risk data; humans define segmentation criteria |
| 7.2.2 | Monitor and evaluate supplier performance | 647213 | h+A — Agents track KPIs and generate scorecards; humans review and act |
| 7.2.3 | Conduct supplier business reviews and development programmes | 815674 | H+a — Humans lead reviews; agents prepare performance packs and trend analysis |
| 7.2.4 | Manage supplier corrective actions and improvement plans | 392847 | H=A — Agents track actions and deadlines; humans manage supplier engagement |
| 7.2.5 | Manage supplier risk and contingency planning | 536412 | h+A — Agents monitor risk signals (financial, geopolitical); humans define contingencies |

---

### 7.3 Plan and Manage Logistics and Distribution (418639)

Design, operate, and optimise the physical movement of goods from origin to destination — including transportation, warehousing, and distribution network management.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.3.1 | Design and optimise the distribution network | 729385 | H=A — Agents model network scenarios; humans decide structural changes |
| 7.3.2 | Plan and schedule transportation movements | 563412 | A — Agent-executed; automated route optimisation and carrier assignment |
| 7.3.3 | Manage warehousing and distribution centre operations | 847261 | H=A — Agents optimise storage and picking; humans manage workforce and exceptions |
| 7.3.4 | Track shipments and manage in-transit visibility | 218534 | A — Agent-executed; real-time tracking with proactive exception alerts |
| 7.3.5 | Manage freight costs and carrier performance | 694173 | h+A — Agents analyse costs and benchmark carriers; humans negotiate and select |
| 7.3.6 | Manage returns logistics and reverse supply chain | 375918 | H=A — Agents process returns and route items; humans handle disposition decisions |

---

### 7.4 Manage Inventory Across the Supply Network (257914)

Plan, control, and optimise inventory levels across all nodes in the supply chain — balancing service levels, working capital, and obsolescence risk.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.4.1 | Set inventory policies and target service levels | 483126 | H+a — Humans define policies; agents model trade-offs and recommend targets |
| 7.4.2 | Monitor inventory positions and movements in real time | 926347 | A — Agent-executed; continuous visibility with automated reorder triggers |
| 7.4.3 | Optimise replenishment and reorder parameters | 614283 | h+A — Agents calculate optimal parameters; humans approve significant changes |
| 7.4.4 | Manage slow-moving, excess, and obsolete inventory | 358741 | H=A — Agents identify at-risk stock; humans decide write-down or disposal actions |
| 7.4.5 | Conduct inventory counts and reconciliation | 742158 | H=A — Agents schedule and track counts; humans investigate discrepancies |

---

### 7.5 Optimise Demand Forecasting and Supply Planning (693248)

Generate, refine, and act on demand forecasts that drive supply chain planning decisions — integrating statistical models, market intelligence, and collaborative input from sales and operations.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.5.1 | Generate statistical demand forecasts | 821634 | A — Agent-executed; automated model selection and forecast generation |
| 7.5.2 | Enrich forecasts with market intelligence and sales input | 475312 | H=A — Agents integrate data sources; humans add qualitative judgement |
| 7.5.3 | Conduct sales and operations planning cycles | 316849 | H+a — Humans lead consensus process; agents prepare scenarios and gap analysis |
| 7.5.4 | Translate demand plans into supply and production signals | 548273 | h+A — Agents generate supply plans; humans validate feasibility |
| 7.5.5 | Monitor forecast accuracy and refine models | 192467 | A — Agent-executed; continuous model tuning with human review of significant shifts |
| 7.5.6 | Manage demand shaping and demand sensing | 763518 | h+A — Agents detect demand signals in real time; humans decide shaping actions |

---

### 7.6 Manage Supply Chain Risk and Resilience (438172)

Identify, monitor, and mitigate risks across the extended supply chain — from single-source dependencies to geopolitical disruptions — ensuring the supply network can absorb and recover from shocks.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.6.1 | Map and assess supply chain risk exposure | 524381 | h+A — Agents map multi-tier dependencies; humans assess strategic vulnerabilities |
| 7.6.2 | Monitor supply chain risk signals and early warnings | 879643 | A — Agent-executed; continuous scanning of geopolitical, weather, and financial signals |
| 7.6.3 | Develop and maintain supply chain contingency plans | 316524 | H+a — Humans design contingencies; agents maintain playbooks and test readiness |
| 7.6.4 | Execute supply chain disruption response | 741283 | H=A — Agents activate playbooks and reroute; humans manage critical decisions |
| 7.6.5 | Conduct supply chain resilience assessments and stress tests | 253918 | H=A — Agents run simulations; humans evaluate findings and invest in resilience |

---

### 7.7 Govern Third-Party and Partner Ecosystem Relationships (185463)

Manage the broader ecosystem of third-party service providers, logistics partners, contract manufacturers, and platform participants that extend the enterprise's supply chain capabilities.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 7.7.1 | Define third-party governance frameworks and standards | 642179 | H+a — Humans set governance standards; agents benchmark and track compliance |
| 7.7.2 | Onboard and integrate ecosystem partners | 397514 | H=A — Agents manage onboarding workflows; humans approve and establish relationships |
| 7.7.3 | Monitor ecosystem partner performance and compliance | 813246 | h+A — Agents track SLAs and compliance metrics; humans manage escalations |
| 7.7.4 | Manage data exchange and integration across the ecosystem | 564832 | h+A — Agents operate integration platforms; humans govern data standards |
| 7.7.5 | Review and rationalise the partner ecosystem periodically | 238617 | H+a — Humans make portfolio decisions; agents analyse utilisation and overlap |

---

## Summary

| Capability | ID | Process Count |
|-----------|-----|---------------|
| 7.1 Source and Procure Goods and Services | 391572 | 6 |
| 7.2 Manage Supplier Relationships and Performance | 562381 | 5 |
| 7.3 Plan and Manage Logistics and Distribution | 418639 | 6 |
| 7.4 Manage Inventory Across the Supply Network | 257914 | 5 |
| 7.5 Optimise Demand Forecasting and Supply Planning | 693248 | 6 |
| 7.6 Manage Supply Chain Risk and Resilience | 438172 | 5 |
| 7.7 Govern Third-Party and Partner Ecosystem Relationships | 185463 | 5 |
| **Total** | | **38 processes** |

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
