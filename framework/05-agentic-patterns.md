# Agentic Enterprise Patterns

## Overview

Agentic Enterprise Patterns are **reusable architectural blueprints** for how AI agents participate in enterprise operations. Each pattern describes a proven way to integrate agents into a specific type of enterprise work, with defined human touchpoints, autonomy levels, and governance requirements.

These patterns are technology-agnostic. They describe **what** the agent does and **how** it relates to humans — not which platform or model implements it.

### Pattern Structure

Each pattern is documented with:

- **Description** — What this pattern does
- **Applicable ZORBA Layers** — Where in the architecture this pattern operates
- **Agent Type** — Which agent type (from the [Workforce Model](03-workforce-model.md)) this pattern uses
- **Human Touchpoints** — Where and how humans interact with this pattern
- **Autonomy Level** — The typical autonomy level (A0–A4)
- **Governance Requirements** — What governance must be in place
- **Example Applications** — Concrete enterprise use cases

---

## Pattern 1: Strategy Formulation Assistant

**Description:** An agent that continuously monitors the external and internal environment, synthesises information, generates strategic insights, and prepares materials for human strategic decision-making. It does not make strategic decisions — it ensures that the humans who do are comprehensively informed.

**Applicable Layers:** L1 (Strategy), L2 (Objectives)

**Agent Type:** Co-Pilot

**Human Touchpoints:**
- Human defines strategic questions and areas of focus
- Human reviews and interrogates agent-generated analyses
- Human makes all strategic decisions
- Human provides feedback on relevance and quality of insights

**Autonomy Level:** A1 (Supervised) — all outputs reviewed before influencing decisions

**Governance Requirements:**
- Source attribution for all intelligence gathered
- Bias disclosure — agent must flag when data sources are limited or skewed
- No autonomous external communications or commitments
- Audit trail of all analyses provided to decision-makers
- Periodic review of the agent's information sources and analytical methods

**Example Applications:**
- Board meeting preparation — scanning market, competitor, and regulatory developments
- Strategic planning cycles — generating scenario analyses and strategic options
- M&A opportunity screening — monitoring and evaluating potential targets
- Strategic risk radar — continuous monitoring of threats and emerging risks

---

## Pattern 2: Autonomous Process Monitor

**Description:** An agent that continuously observes business processes in real-time, detects deviations from expected behaviour, identifies bottlenecks and quality issues, and either resolves them autonomously (within authority) or escalates to humans.

**Applicable Layers:** L4 (Processes), L5 (Activities), L6 (Work)

**Agent Type:** Autonomous Agent

**Human Touchpoints:**
- Human defines monitoring parameters and alert thresholds
- Human receives and acts on escalations
- Human reviews periodic performance summaries
- Human adjusts parameters based on changing business needs

**Autonomy Level:** A3 (Trusted) — operates autonomously, escalates by exception

**Governance Requirements:**
- Defined escalation triggers (cannot be modified by the agent)
- Complete monitoring logs retained for audit
- False positive / false negative tracking
- Human review of auto-resolved issues on a sampling basis
- Clear authority boundaries for autonomous remediation actions

**Example Applications:**
- Order fulfilment monitoring — detecting delays, stock issues, routing problems
- SLA compliance monitoring — tracking service levels across customer contracts
- Financial control monitoring — detecting anomalous transactions or approval violations
- IT operations monitoring — infrastructure health, performance, and security

---

## Pattern 3: Decision Support Analyst

**Description:** An agent that gathers data, performs analysis, models scenarios, and presents structured recommendations to a human decision-maker. The agent prepares the decision; the human makes it.

**Applicable Layers:** L2 (Objectives), L3 (Capabilities), L4 (Processes)

**Agent Type:** Specialist Agent

**Human Touchpoints:**
- Human frames the decision and defines the question
- Human reviews analysis and recommendations
- Human makes the final decision
- Human provides feedback on the quality and relevance of analysis

**Autonomy Level:** A1 (Supervised) for high-stakes decisions; A2 (Guided) for operational decisions

**Governance Requirements:**
- Methodology transparency — the agent must explain its analytical approach
- Confidence levels on all recommendations
- Sensitivity analysis showing how conclusions change with different assumptions
- No cherry-picking — the agent must present countervailing evidence
- Decision log linking recommendation to final decision and outcome

**Example Applications:**
- Pricing decisions — market analysis, elasticity modelling, competitive positioning
- Resource allocation — capacity analysis, ROI projections, scenario comparison
- Vendor selection — multi-criteria evaluation with weighted scoring
- Investment decisions — financial modelling, risk assessment, portfolio impact

---

## Pattern 4: Execution Orchestrator

**Description:** An agent that manages the end-to-end execution of a business process, routing work to the appropriate performers (human or agent), managing dependencies and sequencing, monitoring progress, and ensuring completion.

**Applicable Layers:** L4 (Processes), L5 (Activities)

**Agent Type:** Orchestrator Agent

**Human Touchpoints:**
- Human defines process design and rules
- Human performs assigned decision/judgement steps within the process
- Human handles escalations from the orchestrator
- Human reviews process performance metrics

**Autonomy Level:** A3 (Trusted) — manages flow autonomously, escalates exceptions

**Governance Requirements:**
- Process definition is human-approved and version-controlled
- Routing logic is transparent and auditable
- Cannot modify process definitions without human approval
- Full process execution audit trail
- SLA tracking with automated alerting
- Defined behaviour for process failures and exceptions

**Example Applications:**
- Employee onboarding — coordinating IT setup, HR paperwork, manager introductions, training
- Incident management — coordinating detection, triage, investigation, resolution, post-mortem
- Procurement cycle — requisition through approval, sourcing, PO, receipt, payment
- Campaign launch — coordinating creative, compliance review, channel setup, activation

---

## Pattern 5: Continuous Compliance Guardian

**Description:** An agent that continuously monitors enterprise activities for compliance with regulations, policies, and standards. Operates as an always-on compliance function that catches issues in real-time rather than in periodic audits.

**Applicable Layers:** L4 (Processes), L5 (Activities), L6 (Work)

**Agent Type:** Autonomous Agent

**Human Touchpoints:**
- Human defines compliance rules and regulatory interpretations
- Human receives and investigates flagged violations
- Human makes judgement calls on ambiguous compliance situations
- Human reviews false positive rates and adjusts rules

**Autonomy Level:** A3 (Trusted) for monitoring and flagging; A1 (Supervised) for enforcement actions

**Governance Requirements:**
- Compliance rule definitions require legal/compliance human approval
- All flags and enforcement actions logged and auditable
- False positive tracking with regular calibration
- Cannot autonomously impose sanctions or penalties
- Regular testing against known compliance scenarios
- Regulatory change monitoring to keep rules current

**Example Applications:**
- Data privacy compliance — monitoring data handling against GDPR/privacy regulations
- Financial compliance — transaction monitoring for AML, fraud, sanctions screening
- HR compliance — monitoring employment practices against labour regulations
- Information security — monitoring access patterns, data flows, and policy adherence

---

## Pattern 6: Intelligent Triage Engine

**Description:** An agent that receives incoming requests, enquiries, or issues, classifies them, assesses priority and urgency, enriches them with context, and routes them to the appropriate handler (human or agent).

**Applicable Layers:** L4 (Processes), L5 (Activities)

**Agent Type:** Autonomous Agent

**Human Touchpoints:**
- Human defines classification taxonomy and routing rules
- Human handles escalated or ambiguous cases
- Human reviews triage accuracy periodically
- Human adjusts rules based on changing patterns

**Autonomy Level:** A3–A4 (Trusted to Autonomous) — high-volume, pattern-based work

**Governance Requirements:**
- Classification accuracy metrics with minimum thresholds
- Misrouting tracking and correction protocols
- Priority override capability for humans
- Full audit trail of triage decisions
- Regular retraining/recalibration based on outcomes

**Example Applications:**
- Customer support triage — classifying and routing customer enquiries
- IT service desk — categorising and prioritising incidents and requests
- Lead qualification — scoring and routing sales leads
- Document processing — classifying, extracting, and routing incoming documents

---

## Pattern 7: Knowledge Curator

**Description:** An agent that continuously maintains, updates, and improves the organisation's knowledge base. It ingests new information, identifies outdated content, resolves contradictions, and ensures knowledge is accessible to both humans and agents.

**Applicable Layers:** L3 (Capabilities), L5 (Activities)

**Agent Type:** Autonomous Agent

**Human Touchpoints:**
- Human subject matter experts validate significant knowledge updates
- Human defines knowledge quality standards
- Human reviews agent-proposed changes to critical knowledge articles
- Human provides feedback on knowledge gaps

**Autonomy Level:** A3 (Trusted) for routine maintenance; A2 (Guided) for significant content changes

**Governance Requirements:**
- Version control on all knowledge artefacts
- Change approval workflow for sensitive or regulated content
- Source attribution for all knowledge claims
- Contradiction detection and resolution logging
- Knowledge usage analytics to prioritise maintenance

**Example Applications:**
- Customer-facing knowledge base maintenance
- Internal policy and procedure documentation
- Technical documentation and runbook management
- Regulatory and compliance knowledge management

---

## Pattern 8: Predictive Advisor

**Description:** An agent that analyses historical and real-time data to predict future states, risks, or opportunities, and proactively advises humans on actions to take.

**Applicable Layers:** L2 (Objectives), L3 (Capabilities)

**Agent Type:** Specialist Agent

**Human Touchpoints:**
- Human defines prediction domains and acceptable risk thresholds
- Human receives and evaluates predictions
- Human decides on actions based on predictions
- Human provides outcome feedback to improve predictions

**Autonomy Level:** A2 (Guided) — predictions are advisory, not action-triggering

**Governance Requirements:**
- Model transparency and explainability requirements
- Confidence intervals on all predictions
- Backtesting results published and reviewed
- Bias auditing on a regular schedule
- No autonomous action based on predictions alone (unless explicitly authorised)

**Example Applications:**
- Customer churn prediction with retention recommendations
- Demand forecasting with inventory and staffing recommendations
- Equipment failure prediction with maintenance scheduling
- Cash flow forecasting with liquidity management recommendations

---

## Pattern 9: Workforce Coordinator

**Description:** An agent that manages the allocation and coordination of work across a blended workforce — assigning tasks to the most appropriate performer (human or agent) based on capability, availability, autonomy level, and workload.

**Applicable Layers:** L4 (Processes), L5 (Activities), L6 (Work)

**Agent Type:** Orchestrator Agent

**Human Touchpoints:**
- Human defines workforce allocation policies
- Human handles override requests and special assignments
- Human reviews workload balance and performance
- Human makes staffing and capacity decisions

**Autonomy Level:** A3 (Trusted) — allocates work autonomously within defined policies

**Governance Requirements:**
- Allocation logic transparency
- Fairness monitoring (for human workers)
- Workload caps and wellbeing considerations (for human workers)
- Agent capacity and performance monitoring
- Escalation when no suitable performer is available

**Example Applications:**
- Shared services team coordination — routing work to available humans or agents
- Contact centre workforce management — balancing load across human and AI agents
- Project resource management — matching tasks to available capability
- Field service coordination — scheduling and dispatching human and robotic workers

---

## Pattern 10: Autonomous Executor

**Description:** An agent that independently executes a defined class of work from receipt to completion, with no human involvement in the standard flow. The most autonomous pattern — used for high-volume, well-defined, low-risk work.

**Applicable Layers:** L5 (Activities), L6 (Work)

**Agent Type:** Autonomous Agent

**Human Touchpoints:**
- Human defines execution rules and quality standards
- Human reviews exception reports
- Human performs periodic quality audits
- Human adjusts rules and parameters as needed

**Autonomy Level:** A4 (Autonomous) — full authority within defined scope

**Governance Requirements:**
- Strict boundary definition — what the agent can and cannot do
- Continuous quality monitoring with automated alerts
- Statistical process control on outputs
- Exception handling protocols with human escalation
- Regular performance reviews and scope assessments
- Kill switch / pause capability for emergencies

**Example Applications:**
- Invoice processing — receive, validate, match, approve, pay (within thresholds)
- Data migration and transformation — moving and transforming data between systems
- Report generation — automated creation and distribution of standard reports
- Email classification and response — handling routine enquiries end-to-end

---

## Pattern Selection Guide

| Pattern | Best For | Autonomy | Risk Tolerance |
|---------|----------|----------|---------------|
| Strategy Formulation Assistant | Strategic planning support | Low | Low |
| Autonomous Process Monitor | Operational oversight | High | Medium |
| Decision Support Analyst | Complex decision preparation | Low | Low |
| Execution Orchestrator | Multi-step process management | Medium-High | Medium |
| Continuous Compliance Guardian | Regulatory adherence | Medium-High | Low |
| Intelligent Triage Engine | High-volume intake and routing | High | Medium |
| Knowledge Curator | Knowledge management | Medium | Low-Medium |
| Predictive Advisor | Forecasting and early warning | Low-Medium | Low |
| Workforce Coordinator | Blended team management | Medium-High | Medium |
| Autonomous Executor | High-volume routine work | Maximum | Medium-High |

### Combining Patterns

Patterns are composable. A typical enterprise process might combine:

- An **Intelligent Triage Engine** to receive and classify incoming work
- An **Execution Orchestrator** to manage the process flow
- Multiple **Autonomous Executors** for routine steps
- A **Decision Support Analyst** for judgement-required steps
- A **Continuous Compliance Guardian** monitoring the entire flow
- A **Knowledge Curator** maintaining the knowledge that agents and humans rely on

This composition of patterns — not any single pattern — is what characterises the agentic enterprise.

---

*Previous: [← Domain Reference Model](04-domain-reference.md) | Next: [Governance & Trust Framework →](06-governance.md)*

---

*© 2026 Zontally. All rights reserved.*
