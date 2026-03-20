# The Blended Workforce Model

## Overview

The Blended Workforce Model is ZORBA's answer to the question that no traditional framework addresses: **how do humans and AI agents co-exist as a unified workforce within an enterprise?**

This document defines:

1. **Agent types** — the roles agents play in enterprise operations
2. **Collaboration patterns** — how humans and agents work together
3. **Trust and autonomy levels** — the graduated spectrum of agent independence
4. **Workforce composition design** — how to make deliberate decisions about the human/agent mix

This is not theory. This is a practical model for designing, governing, and evolving a workforce where some of the participants are not human.

---

## Part 1: Agent Types

Not all agents are alike. ZORBA defines four fundamental agent types based on their **relationship to human workers** and their **scope of autonomy**.

### 1.1 Autonomous Agents

**Definition:** Agents that execute defined work independently, within bounded authority, without requiring human involvement for each instance.

**Characteristics:**
- Operate within clearly defined parameters and constraints
- Handle routine decisions within their authority boundary
- Self-monitor performance and quality
- Escalate only when encountering situations outside their defined scope
- Produce audit-grade execution logs

**Enterprise examples:**
- Invoice processing agent that validates, matches, and approves payments within defined thresholds
- Monitoring agent that detects anomalies and triggers response protocols
- Content moderation agent that applies policy to user-generated content
- Data quality agent that continuously validates and cleanses data pipelines

**ZORBA layer affinity:** Primarily L5 (Activities) and L6 (Work)

**Governance requirement:** Defined authority boundaries, continuous performance monitoring, human-reviewable decision logs, automated escalation triggers.

---

### 1.2 Co-Pilot Agents

**Definition:** Agents that work alongside a specific human, augmenting their capabilities, preparing materials, and handling supporting tasks while the human retains decision authority.

**Characteristics:**
- Paired with a human worker (1:1 or 1:many)
- Understand the human's context, preferences, and patterns
- Prepare options and recommendations rather than making final decisions
- Handle preparatory and follow-up work around human decision points
- Adapt their behaviour based on human feedback

**Enterprise examples:**
- Executive co-pilot that prepares meeting briefs, drafts communications, and tracks action items
- Sales co-pilot that researches prospects, drafts proposals, and updates CRM
- Legal co-pilot that reviews contracts, flags risks, and suggests clause alternatives
- Engineering co-pilot that writes code, reviews PRs, and maintains documentation

**ZORBA layer affinity:** L2 (Objectives) through L5 (Activities) — wherever the paired human operates

**Governance requirement:** Clear scope definition, human override at all times, transparency about agent actions taken on behalf of the human, data access controls.

---

### 1.3 Specialist Agents

**Definition:** Agents with deep expertise in a narrow domain, called upon for specific tasks that require specialist knowledge or capability.

**Characteristics:**
- Deep capability in a bounded domain
- Invoked by humans or other agents for specific tasks
- Stateless between invocations (or with managed state)
- Provide expert output but do not own end-to-end processes
- May be shared across teams and domains

**Enterprise examples:**
- Financial modelling agent that builds and stress-tests financial projections
- Translation agent that localises content across markets
- Compliance checking agent that validates activities against regulatory requirements
- Data analysis agent that performs statistical analysis on demand

**ZORBA layer affinity:** L5 (Activities) — called into processes as needed

**Governance requirement:** Input/output validation, capability certification, version control, access controls for sensitive specialist functions.

---

### 1.4 Orchestrator Agents

**Definition:** Agents that coordinate and manage workflows involving multiple humans and/or agents, ensuring work flows correctly through defined processes.

**Characteristics:**
- Manage the flow of work, not the content of work
- Route tasks to appropriate performers (human or agent)
- Monitor deadlines, SLAs, and dependencies
- Handle handoffs between participants
- Maintain process state and provide visibility

**Enterprise examples:**
- Workflow orchestrator managing an approval chain across departments
- Incident response orchestrator coordinating between detection, analysis, and resolution agents/humans
- Onboarding orchestrator managing the sequence of activities for new employee setup
- Campaign orchestrator coordinating marketing activities across channels

**ZORBA layer affinity:** L4 (Processes) — managing the flow at the process level

**Governance requirement:** Routing logic transparency, SLA enforcement rules, escalation authority, visibility to all process participants, no ability to modify process definitions without human approval.

---

### Agent Type Summary

| Type | Autonomy | Scope | Human Relationship | Primary Layer |
|------|----------|-------|-------------------|---------------|
| Autonomous | High | Bounded | Independent within authority | L5–L6 |
| Co-Pilot | Medium | Adaptive | Paired with human | L2–L5 |
| Specialist | Variable | Narrow & deep | On-demand invocation | L5 |
| Orchestrator | Medium-High | Cross-functional | Coordinates humans & agents | L4 |

---

## Part 2: Collaboration Patterns

Humans and agents don't just "work together" — they collaborate in specific, definable patterns. ZORBA identifies six fundamental collaboration patterns.

### 2.1 Delegation

**Pattern:** A human assigns a task or set of tasks to an agent, defining the expected outcome, constraints, and reporting requirements.

**Characteristics:**
- Clear task definition from human to agent
- Defined success criteria and constraints
- Agent has autonomy within the delegated scope
- Human retains accountability for the outcome
- Agent reports back on completion or exception

**When to use:** Routine tasks with well-defined parameters; tasks where agent execution is more efficient; work that needs to happen at scale or speed beyond human capacity.

**Governance consideration:** The delegating human must have authority to delegate the task, and the agent must operate within the authority it has been granted, not the authority of the delegating human.

---

### 2.2 Supervision

**Pattern:** An agent performs work while a human monitors, reviews, and intervenes as needed. The human does not perform the work but validates and corrects agent output.

**Characteristics:**
- Agent is the primary performer
- Human reviews output (all, sampled, or exception-based)
- Human can intervene, correct, or override at any point
- Agent learning may be informed by human corrections
- Supervision intensity may decrease as trust increases

**When to use:** Early-stage agent deployment; high-stakes activities; regulated processes requiring human oversight; trust calibration periods.

**Governance consideration:** Supervision ratios must be defined (e.g., 100% review, 10% sampling, exception-only). Supervision logs must capture what was reviewed, by whom, and what actions were taken.

---

### 2.3 Peer Collaboration

**Pattern:** Humans and agents work together as peers on a shared task, each contributing their distinct capabilities.

**Characteristics:**
- Shared objective with distinct contributions
- Human provides judgement, creativity, relationships, context
- Agent provides speed, data processing, consistency, breadth
- Iterative exchange — each builds on the other's output
- Neither is subordinate; both are essential

**When to use:** Complex analysis requiring both data processing and judgement; creative work that benefits from AI-generated options with human curation; strategic planning with data-intensive inputs.

**Governance consideration:** Decision authority must be clear even in peer collaboration. When human and agent disagree, the resolution protocol must be defined in advance.

---

### 2.4 Escalation

**Pattern:** An agent encounters a situation outside its authority or capability and transfers control to a human (or to a higher-authority agent).

**Characteristics:**
- Triggered by defined conditions (confidence threshold, authority boundary, novel situation)
- Agent provides full context to the escalation target
- Control transfers cleanly — no ambiguity about who owns the decision
- Post-escalation, the agent may resume execution based on the human's decision
- Escalation events are logged and analysed for pattern improvement

**When to use:** Built into every autonomous and orchestrator agent as a fundamental capability. This is not a failure mode — it is a design feature.

**Governance consideration:** Escalation triggers must be defined at design time. Escalation response SLAs must be set. Chronic escalation patterns should trigger process or authority redesign.

---

### 2.5 Agent-to-Agent Coordination

**Pattern:** Agents coordinate with each other to complete work that spans multiple agent capabilities, with or without human involvement.

**Characteristics:**
- Agents invoke, inform, and hand off to other agents
- Shared protocols for state transfer and context passing
- May form agent chains or agent networks for complex tasks
- Human visibility into agent-to-agent coordination is maintained
- An orchestrator agent or human serves as the coordination authority

**When to use:** Complex automated workflows; multi-domain tasks; high-volume processing pipelines; situations where human coordination would be a bottleneck.

**Governance consideration:** Agent-to-agent coordination must be architecturally visible — not hidden. The full chain of agent interactions must be auditable. Human intervention points must be defined even in fully automated chains.

---

### 2.6 Human Override

**Pattern:** A human intervenes to stop, redirect, or take over agent activity regardless of the agent's current state or autonomy level.

**Characteristics:**
- Universal capability — applies to all agent types and all situations
- Cannot be refused, delayed, or circumvented by the agent
- Override is logged with full context (who, when, why, what state)
- Agent gracefully transfers state to the overriding human
- Post-override recovery procedures are defined

**When to use:** Emergency situations; detected agent errors; regulatory requirements; trust recalibration events; any situation where a human determines that agent activity should cease.

**Governance consideration:** This is a **fundamental principle**, not a pattern. Override capability must be designed into every agent from inception. Override authority must be defined (who can override which agents).

---

### Collaboration Pattern Summary

| Pattern | Direction | Autonomy Level | Primary Use |
|---------|-----------|---------------|-------------|
| Delegation | Human → Agent | High | Task assignment |
| Supervision | Agent → Human (review) | Medium | Quality assurance |
| Peer Collaboration | Bidirectional | Shared | Complex problem-solving |
| Escalation | Agent → Human | Triggered | Exception handling |
| Agent-to-Agent | Agent ↔ Agent | Variable | Automated workflows |
| Human Override | Human → Agent (interrupt) | Revoked | Emergency/control |

---

## Part 3: Trust and Autonomy Levels

Trust between humans and agents is not binary. ZORBA defines a five-level **Trust and Autonomy Scale** that governs how much independence an agent has in any given context.

### The ZORBA Autonomy Scale

| Level | Name | Description | Human Involvement |
|-------|------|-------------|-------------------|
| **A0** | **Inert** | Agent has no authority to act. Provides information only when queried. | Human performs all actions |
| **A1** | **Supervised** | Agent performs actions, but every output requires human approval before taking effect. | Human reviews 100% of outputs |
| **A2** | **Guided** | Agent performs actions autonomously for routine cases; flags exceptions and edge cases for human review. | Human reviews exceptions + periodic sampling |
| **A3** | **Trusted** | Agent operates autonomously within defined boundaries. Human reviews by exception only. Agent self-monitors and self-escalates. | Human reviews escalations and periodic audits |
| **A4** | **Autonomous** | Agent operates with full authority within its domain. Self-governing within defined constraints. Human oversight is structural (audit, policy) rather than operational. | Human sets policy and reviews systemic performance |

### Trust Calibration

Autonomy levels are not static. They are calibrated based on:

- **Performance history** — Agents that demonstrate consistent quality earn higher trust
- **Domain risk** — Higher-risk domains warrant lower autonomy levels
- **Regulatory requirements** — Some domains have mandated human oversight levels
- **Organisational maturity** — Organisations new to agentic operations start lower
- **Incident history** — Trust can be recalibrated downward after failures

### Trust Calibration Protocol

```
1. Initial deployment: Agent starts at A1 (Supervised)
2. Performance review period: Defined duration with 100% human review
3. Trust assessment: Performance metrics, error rates, escalation quality
4. Promotion decision: Human authority required to increase autonomy level
5. Continuous monitoring: Ongoing performance tracking with automated alerts
6. Recalibration trigger: Defined conditions that cause trust level review
   (error spike, novel situation class, regulatory change, incident)
7. Demotion protocol: Process for reducing autonomy with defined recovery path
```

### Autonomy Level by ZORBA Layer

Different layers have different maximum appropriate autonomy levels:

| Layer | Typical Maximum Autonomy | Rationale |
|-------|-------------------------|-----------|
| L1: Strategy | A0 (Inert) | Strategic decisions require human authority |
| L2: Objectives | A1 (Supervised) | Objective-setting requires human judgement |
| L3: Capabilities | A2 (Guided) | Capability design requires human oversight with agent input |
| L4: Processes | A3 (Trusted) | Process orchestration can be highly automated |
| L5: Activities | A4 (Autonomous) | Routine activities can be fully autonomous |
| L6: Work | A4 (Autonomous) | Work execution at scale requires agent autonomy |

These are **defaults, not mandates**. A highly regulated industry may require A2 maximum at L5. A mature, data-rich operation may justify A3 at L3. The point is that the decision is **made explicitly**.

---

## Part 4: Workforce Composition Design

Workforce composition — the blend of human and agent capabilities across the enterprise — is an architectural decision. ZORBA provides a structured approach.

### Composition Assessment

For each capability, process, or activity, assess:

| Factor | Question |
|--------|----------|
| **Repeatability** | Is this work consistent and pattern-based, or novel each time? |
| **Data intensity** | Does this work primarily involve processing structured data? |
| **Judgement complexity** | Does this require nuanced human judgement? |
| **Speed requirement** | Does the required speed exceed human capacity? |
| **Scale requirement** | Does the required volume exceed human capacity? |
| **Relationship dependency** | Does this require human relationships or empathy? |
| **Regulatory mandate** | Do regulations require human involvement? |
| **Error consequence** | What is the impact of errors — reversible or catastrophic? |
| **Creative requirement** | Does this require genuine creative originality? |

### Composition Profiles

Based on assessment, each function receives a composition profile:

- **Human-Essential (H):** Work that must be performed by humans due to judgement, creativity, regulatory, or relationship requirements. Agents support but do not perform.

- **Human-Led, Agent-Supported (H+a):** Human performs the primary work with agent assistance — preparation, analysis, follow-up.

- **Blended (H=A):** Genuinely shared between humans and agents, with clear division of responsibilities within the function.

- **Agent-Led, Human-Supervised (h+A):** Agent performs primary work with human oversight — review, exception handling, quality assurance.

- **Agent-Essential (A):** Work that is optimally or necessarily performed by agents due to speed, scale, data intensity, or consistency requirements. Humans govern but do not perform.

### Composition Evolution

Workforce composition is not static. ZORBA expects and enables composition evolution over time:

```
Typical evolution path:
H → H+a → H=A → h+A → A

As agent capabilities mature and trust is calibrated,
functions naturally shift toward greater agent involvement.
This shift must be deliberate, governed, and reversible.
```

**Critical principle:** The path can go in either direction. If an agent-led function experiences quality degradation, trust recalibration may shift it back toward human-led. Composition is a continuous design decision, not a one-way migration.

---

## Putting It Together

The Blended Workforce Model gives organisations a practical vocabulary and structure for answering the question ZORBA poses: **where does the human end and the agent begin?**

The answer is: **it depends** — on the agent type, the collaboration pattern, the trust level, the composition profile, the domain, the risk, and the regulatory context. But with ZORBA, it depends on **deliberate architectural decisions**, not on whatever happens to emerge when someone connects an AI to a business process.

The organisations that thrive in the agentic era will be those that design their blended workforce intentionally. ZORBA provides the blueprint.

---

*Previous: [← Framework Architecture](02-architecture.md) | Next: [Domain Reference Model →](04-domain-reference.md)*

---

*© 2026 Zontally. All rights reserved.*
