# Domain 6: Operations & Delivery (471829)

*Executing with precision and adaptability*

**Classification:** Value Chain
**Version:** v0.1 (Draft)

---

## Overview

This domain encompasses the enterprise's ability to plan, execute, and continuously improve its core operational activities — whether producing physical goods, delivering services, or running hybrid fulfilment models. It covers the full span from operational planning through delivery execution, quality assurance, and ongoing operational refinement.

In a ZORBA-enabled enterprise, operations is where **agents move from advisory to executive roles** — scheduling production runs, monitoring quality in real time, detecting anomalies before they escalate, and orchestrating exception handling across the delivery chain.

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

### 6.1 Plan and Schedule Operational Activities (629471)

Translate demand signals and strategic priorities into executable operational plans and schedules that balance throughput, resource constraints, and customer commitments.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.1.1 | Develop aggregate operational plans aligned to demand | 384216 | H=A — Agents model demand scenarios; humans select and approve plans |
| 6.1.2 | Create and maintain detailed production or service schedules | 715943 | h+A — Agents generate optimised schedules; humans review constraints and approve |
| 6.1.3 | Allocate resources and materials to scheduled activities | 528367 | h+A — Agents optimise allocation; humans resolve conflicts and exceptions |
| 6.1.4 | Manage schedule changes and re-planning triggers | 263814 | A — Agents detect disruptions and re-plan within defined parameters |
| 6.1.5 | Coordinate cross-functional scheduling dependencies | 849172 | H=A — Agents identify clashes and propose resolutions; humans arbitrate |

---

### 6.2 Execute Production and Service Delivery (183746)

Run the core operational processes that produce goods or deliver services — ensuring work is completed on time, to specification, and within cost targets.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.2.1 | Initiate and manage production runs or service engagements | 492638 | H=A — Agents trigger and track; humans manage exceptions |
| 6.2.2 | Monitor work-in-progress and operational throughput | 637281 | A — Agent-executed; real-time monitoring with threshold-based alerts |
| 6.2.3 | Manage handoffs and transitions between operational stages | 318457 | h+A — Agents orchestrate transitions; humans handle escalations |
| 6.2.4 | Record and validate completion of deliverables | 754129 | h+A — Agents log completions and validate against specs; humans sign off critical items |
| 6.2.5 | Manage rework, returns, and service recovery processes | 861345 | H+a — Humans lead recovery decisions; agents track and report rework costs |
| 6.2.6 | Coordinate delivery and fulfilment to the customer | 245893 | H=A — Agents manage logistics handoffs; humans handle customer-sensitive issues |

---

### 6.3 Manage Quality and Assurance (536482)

Establish and operate the quality management system — defining standards, conducting inspections, managing non-conformances, and ensuring consistent output quality across all operational activities.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.3.1 | Define quality standards, specifications, and acceptance criteria | 419573 | H+a — Humans set standards; agents benchmark against industry norms |
| 6.3.2 | Conduct in-process and final quality inspections | 782316 | h+A — Agents perform automated checks; humans inspect edge cases |
| 6.3.3 | Detect, log, and classify non-conformances | 364925 | A — Agent-executed; automated detection with classification models |
| 6.3.4 | Investigate root causes and determine corrective actions | 651748 | H+a — Humans lead root-cause analysis; agents correlate data and suggest hypotheses |
| 6.3.5 | Track corrective and preventive action closure | 893261 | h+A — Agents track timelines and chase overdue actions; humans verify effectiveness |
| 6.3.6 | Manage quality audits and certification compliance | 127584 | H=A — Agents prepare audit evidence; humans conduct and respond to audits |

---

### 6.4 Drive Operational Excellence and Continuous Improvement (274951)

Build and sustain a culture and practice of continuous improvement — leveraging methodologies, metrics, and employee engagement to systematically eliminate waste and enhance performance.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.4.1 | Establish and maintain the continuous improvement framework | 593847 | H+a — Humans design the framework; agents maintain documentation and track adoption |
| 6.4.2 | Identify improvement opportunities from operational data | 816234 | h+A — Agents mine data for patterns and waste; humans validate and prioritise |
| 6.4.3 | Manage the improvement initiative pipeline | 428716 | H=A — Agents track initiatives and ROI; humans approve and resource projects |
| 6.4.4 | Facilitate improvement workshops and problem-solving events | 345192 | H+a — Humans facilitate; agents prepare data packs and track outcomes |
| 6.4.5 | Measure and report improvement impact | 762481 | h+A — Agents calculate savings and performance uplift; humans validate claims |

---

### 6.5 Manage Operational Capacity (918263)

Plan, monitor, and adjust capacity to meet current and anticipated demand — balancing utilisation, flexibility, and cost across people, equipment, and facilities.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.5.1 | Assess current capacity and utilisation levels | 483619 | A — Agent-executed; continuous monitoring of capacity metrics |
| 6.5.2 | Forecast capacity requirements against demand plans | 217438 | h+A — Agents model scenarios; humans review assumptions and approve |
| 6.5.3 | Plan and execute capacity adjustments | 695172 | H+a — Humans decide capacity changes; agents model cost and timing implications |
| 6.5.4 | Manage equipment, facility, and workforce availability | 354281 | H=A — Agents track availability and flag risks; humans resolve constraints |
| 6.5.5 | Monitor capacity performance and recommend rebalancing | 738425 | h+A — Agents surface rebalancing opportunities; humans approve changes |

---

### 6.6 Manage Operational Risk and Resilience (352194)

Identify, assess, and mitigate risks specific to operational delivery — including supply disruptions, equipment failures, safety incidents, and process breakdowns. This is the operational risk layer; enterprise-wide risk oversight sits within Domain 1.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.6.1 | Identify and assess operational risks and vulnerabilities | 584321 | H=A — Agents scan for emerging risks; humans assess severity and define responses |
| 6.6.2 | Define and maintain operational risk mitigation plans | 419682 | H+a — Humans design mitigations; agents track implementation and test readiness |
| 6.6.3 | Monitor operational risk indicators in real time | 763215 | A — Agent-executed; continuous monitoring with escalation protocols |
| 6.6.4 | Conduct operational resilience testing and simulations | 291843 | H=A — Agents run simulations; humans evaluate results and refine plans |
| 6.6.5 | Manage business continuity for operational functions | 847536 | H+a — Humans own continuity plans; agents monitor triggers and coordinate activation |

---

### 6.7 Handle Incidents and Operational Exceptions (643518)

Detect, respond to, and resolve incidents and exceptions that disrupt normal operational flow — restoring service, minimising impact, and capturing lessons for prevention.

| # | Process | ID | Agentic Profile |
|---|---------|-----|-----------------|
| 6.7.1 | Detect and classify operational incidents and exceptions | 175342 | A — Agent-executed; real-time anomaly detection and classification |
| 6.7.2 | Triage and prioritise incident response | 428916 | h+A — Agents triage by severity; humans override for complex or sensitive incidents |
| 6.7.3 | Coordinate incident response and resolution activities | 593274 | H=A — Agents orchestrate response workflows; humans lead critical decisions |
| 6.7.4 | Communicate incident status to stakeholders | 316748 | h+A — Agents generate and distribute status updates; humans handle sensitive comms |
| 6.7.5 | Conduct post-incident reviews and embed learnings | 842157 | H+a — Humans lead reviews; agents compile data, timelines, and suggested improvements |

---

## Summary

| Capability | ID | Process Count |
|-----------|-----|---------------|
| 6.1 Plan and Schedule Operational Activities | 629471 | 5 |
| 6.2 Execute Production and Service Delivery | 183746 | 6 |
| 6.3 Manage Quality and Assurance | 536482 | 6 |
| 6.4 Drive Operational Excellence and Continuous Improvement | 274951 | 5 |
| 6.5 Manage Operational Capacity | 918263 | 5 |
| 6.6 Manage Operational Risk and Resilience | 352194 | 5 |
| 6.7 Handle Incidents and Operational Exceptions | 643518 | 5 |
| **Total** | | **37 processes** |

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
