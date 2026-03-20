# Governance & Trust Framework

## Overview

Governing a blended workforce is fundamentally different from governing a human-only organisation. Traditional governance assumes that every decision-maker is a person with judgement, accountability, and legal personhood. In the agentic enterprise, some of the most active participants in decision-making and execution are AI agents — entities that can act autonomously but cannot be held personally accountable.

This creates a **governance gap** that most frameworks ignore entirely.

ZORBA's Governance & Trust Framework addresses this gap with six interconnected components:

1. **Agent Accountability Model** — Who is responsible when an agent acts?
2. **Decision Authority Matrix** — Who (human or agent) can decide what?
3. **Escalation Protocols** — How and when do agents escalate to humans?
4. **Audit & Traceability** — How do you audit a blended decision chain?
5. **Trust Calibration** — How do you manage evolving trust in agents?
6. **Human Override Principles** — The non-negotiable right to intervene

---

## 1. Agent Accountability Model

### The Accountability Problem

When a human makes a bad decision, accountability is clear. When an agent makes a bad decision, accountability fragments across:

- The agent (which cannot be disciplined or held legally liable)
- The human who deployed the agent
- The human who configured or trained the agent
- The human who approved the agent's autonomy level
- The organisation that chose to use the agent

### ZORBA's Accountability Framework

ZORBA resolves this through the **Chain of Accountability** model:

| Role | Accountability |
|------|---------------|
| **Agent Owner** | The human or team responsible for the agent's existence, configuration, and fitness for purpose. Accountable for the agent's behaviour within its defined scope. |
| **Authority Grantor** | The human who approved the agent's autonomy level and authority boundaries. Accountable for the appropriateness of the authority granted. |
| **Process Owner** | The human who owns the process in which the agent operates. Accountable for the process design including agent participation. |
| **Domain Owner** | The human who owns the enterprise domain. Accountable for the overall workforce composition decisions in their domain. |
| **Governance Function** | The function responsible for enterprise-wide agent governance. Accountable for the governance framework itself. |

### Key Principles

1. **Accountability cannot be delegated to an agent.** An agent can execute a decision, but a human must be accountable for that decision being executable by the agent.

2. **Accountability follows authority.** The human who granted the agent its authority is accountable for outcomes within that authority scope.

3. **Shared accountability is explicit.** When multiple humans share accountability for an agent's actions, each person's accountability scope must be documented.

4. **Agent "decisions" are executions of human-defined policy.** When an agent "decides" to approve a refund, it is executing a policy that a human defined and another human authorised the agent to apply.

---

## 2. Decision Authority Matrix

### Overview

The Decision Authority Matrix (DAM) defines, for every significant decision type in the enterprise, **who has authority to make that decision** — and specifically, whether an agent can make it, and under what conditions.

### Authority Levels

| Level | Name | Description |
|-------|------|-------------|
| **D1** | **Human-Only** | Decision requires human authority. No agent involvement in the decision itself (agents may prepare information). |
| **D2** | **Human-Decided, Agent-Prepared** | Agent prepares the decision package (analysis, recommendation, options). Human makes the decision. |
| **D3** | **Agent-Decided, Human-Approved** | Agent makes a preliminary decision. Decision takes effect only after human approval. |
| **D4** | **Agent-Decided, Human-Notified** | Agent makes and executes the decision. Human is notified and can review/reverse. |
| **D5** | **Agent-Decided, Exception-Reported** | Agent makes and executes the decision autonomously. Human is informed only of exceptions or anomalies. |

### Example Decision Authority Assignments

| Decision Type | Authority Level | Rationale |
|---------------|----------------|-----------|
| Strategic direction changes | D1 | Values, vision, and risk appetite |
| Annual budget approval | D1 | Resource commitment at scale |
| Hiring decisions | D2 | Legal and cultural implications |
| Customer refund < £100 | D5 | Low risk, high volume, clear rules |
| Customer refund £100–£1,000 | D4 | Medium risk, human visibility |
| Customer refund > £1,000 | D2 | High value, human judgement |
| Standard purchase order < threshold | D5 | Routine procurement |
| Vendor contract negotiation | D1 | Relationship and commitment |
| Content publication (routine) | D4 | Brand risk manageable |
| Content publication (sensitive) | D2 | Reputational risk |
| System configuration change | D3 | Operational risk |
| Emergency incident response (initial) | D5 | Speed critical |
| Emergency incident response (major) | D1 | Consequence severity |

### Maintaining the Matrix

The Decision Authority Matrix is a **living document**:

- Reviewed quarterly or when significant changes occur
- Updated when agent capabilities evolve
- Adjusted after incidents involving agent decisions
- Domain owners are responsible for their section of the matrix
- Enterprise governance reviews the overall matrix for consistency

---

## 3. Escalation Protocols

### Why Escalation Is a Design Feature

Escalation is not failure. It is the mechanism by which agents **acknowledge the limits of their authority and capability**. Well-designed escalation is the single most important safety feature in a blended workforce.

### Escalation Triggers

Agents must escalate when:

| Trigger Type | Description | Example |
|-------------|-------------|---------|
| **Authority boundary** | The action required exceeds the agent's decision authority level | Refund amount exceeds agent's approval threshold |
| **Confidence threshold** | The agent's confidence in its assessment falls below the defined minimum | Classification confidence < 80% |
| **Novel situation** | The agent encounters a scenario not covered by its training or rules | Customer request type never seen before |
| **Conflict detection** | The agent detects conflicting rules, data, or instructions | Two policies give contradictory guidance |
| **Safety concern** | The agent detects potential harm, legal risk, or ethical issue | Data suggests discriminatory outcome |
| **Consecutive failures** | The agent has failed at this task type multiple times consecutively | Third failed attempt at automated resolution |
| **Human request** | A human explicitly requests escalation or review | Customer asks to speak to a person |

### Escalation Protocol Structure

Every escalation must include:

```
ESCALATION PACKET:
├── Escalation ID (unique, traceable)
├── Trigger type and description
├── Full context of the situation
├── Actions already taken by the agent
├── Agent's assessment (if any) with confidence level
├── Recommended actions (if applicable)
├── Time sensitivity / SLA implications
├── Suggested escalation target (human or higher-authority agent)
└── Current state preservation (so the target can resume seamlessly)
```

### Escalation Response SLAs

| Escalation Priority | Response Target | Use When |
|---------------------|-----------------|----------|
| **Critical** | < 15 minutes | Safety, legal, major financial impact |
| **High** | < 1 hour | Customer-impacting, SLA at risk |
| **Standard** | < 4 hours | Normal exception handling |
| **Low** | < 24 hours | Improvement opportunity, non-urgent review |

### Anti-Patterns

- **Escalation flooding** — Agent escalates too frequently, overwhelming humans. *Fix: Recalibrate thresholds, expand agent authority, or improve agent capability.*
- **Escalation avoidance** — Agent operates beyond its authority rather than escalating. *Fix: This is a critical governance failure. Reduce autonomy level. Investigate root cause.*
- **Escalation ping-pong** — Issue bounces between agents and humans without resolution. *Fix: Define clear ownership. If escalated to a human, the human owns it until resolved or explicitly delegated back.*
- **Context-free escalation** — Agent escalates without adequate context. *Fix: Enforce escalation packet structure. Agent cannot escalate without the required fields.*

---

## 4. Audit & Traceability

### The Audit Challenge

In a traditional enterprise, audit follows humans. In a blended workforce, audit must follow **decisions and actions regardless of whether the performer was human or agent**.

### ZORBA Audit Requirements

#### 4.1 Decision Lineage

Every significant decision must be traceable through its full lineage:

```
Decision Lineage:
├── Strategic context (which strategy/objective does this serve?)
├── Authority basis (what gave the decision-maker authority?)
├── Information basis (what data/analysis informed the decision?)
├── Decision rationale (why this option vs. alternatives?)
├── Performer (human ID or agent ID)
├── Autonomy level at time of decision
├── Review status (reviewed by whom, or auto-approved)
└── Outcome (what happened as a result?)
```

#### 4.2 Agent Execution Logs

Agent-executed activities must produce logs that meet audit standards:

| Log Element | Requirement |
|-------------|-------------|
| **Timestamp** | Precise time of every action |
| **Agent identity** | Which agent instance performed the action |
| **Input data** | What data the agent received |
| **Processing logic** | What rules, models, or reasoning the agent applied |
| **Output** | What the agent produced or decided |
| **Confidence** | Agent's self-assessed confidence level |
| **Alternatives considered** | Other options the agent evaluated (where applicable) |
| **Escalations** | Any escalations triggered, to whom, and resolution |
| **Exceptions** | Any anomalies detected or errors encountered |

#### 4.3 Human-Agent Handoff Logs

Every transition between human and agent must be logged:

- Who handed off to whom
- What state was transferred
- What authority was conferred or revoked
- What the receiving party (human or agent) did next

#### 4.4 Audit Capabilities

The blended workforce must support:

- **End-to-end process trace** — follow any work instance from inception to completion across all human and agent performers
- **Agent performance audit** — evaluate any agent's decision quality over time
- **Authority compliance audit** — verify that agents operated within their authority boundaries
- **Escalation audit** — analyse escalation patterns for governance and capability gaps
- **Workforce composition audit** — assess whether the actual human/agent mix matches the designed composition

---

## 5. Trust Calibration

### Overview

Trust in agents is not a switch (on/off). It is a **continuously calibrated variable** that determines how much autonomy an agent receives. Trust calibration is the process by which the organisation adjusts agent autonomy based on evidence.

### Trust Signals

Trust is calibrated based on observable signals:

**Positive signals (trust increases):**
- Consistent decision quality over sustained periods
- Appropriate escalation behaviour (escalates when it should, doesn't when it shouldn't)
- Graceful handling of edge cases
- Accurate self-assessment of confidence
- Positive human feedback on outputs

**Negative signals (trust decreases):**
- Decision errors, especially repeated patterns
- Failure to escalate when appropriate
- Inappropriate autonomous action
- Declining output quality
- Misalignment between confidence scores and actual accuracy
- Adverse incidents involving agent actions

### Trust Calibration Process

```
1. CONTINUOUS MONITORING
   Agent performance metrics are collected continuously.

2. PERIODIC REVIEW (monthly or as triggered)
   Performance data is reviewed against trust thresholds.
   
3. TRUST ASSESSMENT
   Current trust level assessed against criteria for current
   and adjacent autonomy levels.

4. CALIBRATION DECISION (human authority required)
   - Maintain current level
   - Promote to higher autonomy (requires positive evidence)
   - Demote to lower autonomy (triggered by negative signals)
   - Suspend (immediate, pending investigation)

5. IMPLEMENTATION
   Autonomy level adjusted in agent configuration.
   Affected humans notified of the change.

6. OBSERVATION PERIOD
   Enhanced monitoring following any trust level change.
```

### Trust Is Contextual

An agent may hold different trust levels in different contexts:

- High trust for standard transactions, low trust for edge cases
- High trust during normal operations, reduced trust during periods of market volatility
- High trust in one domain, not automatically transferable to another
- Trust earned in one organisation does not transfer to another

### Trust Recovery

When trust is reduced, there must be a defined path to recovery:

1. Root cause analysis of the trust-reducing event
2. Remediation (retraining, rule adjustment, scope reduction)
3. Re-entry at reduced autonomy level with enhanced monitoring
4. Graduated return to previous autonomy based on sustained performance

---

## 6. Human Override Principles

### The Non-Negotiable Right

Human override is the **foundational principle** of the ZORBA Governance Framework. It is not a feature. It is an axiom.

### The Seven Override Principles

**1. Universality**
Every agent, at every autonomy level, in every domain, is subject to human override. No exceptions.

**2. Immediacy**
Override takes effect immediately upon invocation. The agent cannot delay, negotiate, or queue an override request.

**3. Completeness**
Override can stop, redirect, or take over agent activity entirely. Partial override (e.g., "stop doing X but continue Y") is also supported.

**4. Authority**
Override authority is defined — not everyone can override every agent. But the authority structure must ensure that at least one available human can override any given agent at any time.

**5. State Preservation**
When overridden, the agent must preserve and make available its current state, context, and in-progress work so that the overriding human can continue effectively.

**6. Non-Retaliation**
An agent that has been overridden must not treat the override as a signal to change its behaviour in ways not explicitly directed. Override is a governance event, not a training signal (unless explicitly used as such).

**7. Transparency**
All overrides are logged with full context: who overrode, which agent, what the agent was doing, why the override occurred, and what happened next.

---

## Governance Operating Model

### Roles and Responsibilities

| Role | Responsibility |
|------|---------------|
| **Chief Agent Officer** (or equivalent) | Enterprise-wide agent strategy, governance, and risk management |
| **Domain Agent Steward** | Agent governance within a specific domain — workforce composition, autonomy levels, performance |
| **Agent Owner** | Day-to-day management of specific agents — configuration, monitoring, incident response |
| **Agent Auditor** | Independent assessment of agent compliance, performance, and governance adherence |
| **Ethics & AI Review Board** | Oversight of ethical implications, bias, fairness, and societal impact |

### Governance Cadence

| Activity | Frequency | Participants |
|----------|-----------|-------------|
| Agent performance review | Monthly | Agent Owner, Domain Agent Steward |
| Trust calibration assessment | Monthly or triggered | Domain Agent Steward, Agent Owner |
| Decision Authority Matrix review | Quarterly | Domain owners, governance function |
| Workforce composition review | Quarterly | Domain owners, executive leadership |
| Enterprise agent governance review | Semi-annually | Chief Agent Officer, executive leadership |
| Ethics and bias audit | Annually or triggered | Ethics & AI Review Board, Agent Auditor |
| Full governance framework review | Annually | All governance roles |

---

## Governance Maturity Model

Organisations adopt agent governance progressively. ZORBA defines five maturity levels:

| Level | Name | Characteristics |
|-------|------|----------------|
| **G1** | **Ad Hoc** | Agents deployed without formal governance. Accountability unclear. No systematic monitoring. |
| **G2** | **Emerging** | Basic accountability defined. Some monitoring in place. Decision authority informal. |
| **G3** | **Defined** | Governance framework documented. Decision Authority Matrix established. Escalation protocols defined. Regular audits. |
| **G4** | **Managed** | Governance is operationalised and measured. Trust calibration is systematic. Audit is comprehensive. Governance is itself partially agent-assisted. |
| **G5** | **Optimising** | Governance is continuously improving based on data. Agents participate in governance monitoring. Workforce composition is dynamically optimised. The governance framework itself is a living, adaptive system. |

Most organisations today are at G1 or G2. ZORBA provides the path to G3 and beyond.

---

*Previous: [← Agentic Enterprise Patterns](05-agentic-patterns.md) | Next: [Glossary →](13-glossary.md)*

---

*© 2026 Zontally. All rights reserved.*
