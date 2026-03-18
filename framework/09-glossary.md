# Glossary

**Zontally Reference Business Architecture**
**Version:** v0.1 (Draft)

---

## Traditional Enterprise Architecture Terms

| Term | Definition |
|------|-----------|
| **Activity** | A discrete, bounded unit of work within a process, with defined inputs, outputs, and a performer. ZORBA Layer 5. |
| **Business Architecture** | The discipline of defining and organising how an enterprise creates, delivers, and captures value through its structure, capabilities, and processes. |
| **Capability** | An organisational ability required to achieve objectives — what the enterprise needs to be able to do, independent of how it does it. ZORBA Layer 3. |
| **Domain** | A major functional area of the enterprise (e.g., Finance, Marketing, Operations). ZORBA defines 12 enterprise domains. |
| **Enterprise Architecture** | The practice of designing the structure of an organisation — its strategy, operations, information, and technology — as an integrated whole. |
| **Objective** | A measurable goal that translates strategy into accountable outcomes. ZORBA Layer 2. |
| **Operating Model** | The blueprint for how an organisation delivers value through its people, processes, and technology. |
| **Process** | A structured sequence of activities that delivers a capability. The "how" of the enterprise. ZORBA Layer 4. |
| **Reference Architecture** | A standardised model that provides a common vocabulary and structure for describing a domain. ZORBA is a reference architecture for the blended enterprise. |
| **Strategy** | The organisation's purpose, vision, direction, and competitive positioning. ZORBA Layer 1. |
| **Value Chain** | The full set of activities an organisation performs to create and deliver value to its customers. |
| **Work** | The actual execution — instances of activities being performed, producing outputs. ZORBA Layer 6. |

---

## Agentic Enterprise Terms (Introduced by ZORBA)

| Term | Definition |
|------|-----------|
| **Agent** | An AI-powered entity that operates with a degree of autonomy within the enterprise — making decisions, executing tasks, and collaborating with humans and other agents within defined authority boundaries. Distinguished from a "tool" by its capacity for autonomous action. |
| **Agent Auditor** | A role responsible for independent assessment of agent compliance, performance, and governance adherence. |
| **Agent Owner** | The human or team accountable for a specific agent's configuration, performance, and fitness for purpose. |
| **Agent Platform** | The technology infrastructure, tooling, and operations that enable enterprise agents to operate. Managed within the Technology & Data domain. |
| **Agentic Maturity Profile** | A structured assessment of a domain's readiness for agent participation, showing the current and target human/agent split across activities. |
| **Authority Boundary** | The explicitly defined limits of an agent's decision-making and action-taking power. Agents must not act outside their authority boundary. |
| **Authority Grantor** | The human who approved an agent's autonomy level and authority boundaries. Accountable for the appropriateness of the authority granted. |
| **Autonomous Agent** | An agent type that executes defined work independently within bounded authority, without requiring human involvement for each instance. See [Workforce Model](03-workforce-model.md). |
| **Autonomy Level** | A classification (A0–A4) that defines how much independence an agent has. Ranges from A0 (Inert — information only) to A4 (Autonomous — full authority within scope). |
| **Blended Workforce** | An organisational workforce comprising both human workers and AI agents, operating as an integrated team with defined roles, responsibilities, and governance. |
| **Capability Composition Matrix** | A ZORBA assessment tool for determining the appropriate workforce composition (human, agent, or blended) for each capability. |
| **Chain of Accountability** | ZORBA's model for resolving the accountability question when agents act. Maps accountability through Agent Owner, Authority Grantor, Process Owner, Domain Owner, and Governance Function. |
| **Chief Agent Officer** | An executive role responsible for enterprise-wide agent strategy, governance, and risk management. |
| **Co-Pilot Agent** | An agent type that works alongside a specific human, augmenting their capabilities while the human retains decision authority. See [Workforce Model](03-workforce-model.md). |
| **Composition Profile** | A classification of the human/agent workforce mix for a function: Human-Essential (H), Human-Led (H+a), Blended (H=A), Agent-Led (h+A), or Agent-Essential (A). |
| **Decision Authority Matrix (DAM)** | A governance artefact that defines, for every significant decision type, whether a human or agent has authority to make it, and under what conditions. |
| **Domain Agent Steward** | A role responsible for agent governance within a specific enterprise domain. |
| **Escalation** | The mechanism by which an agent transfers control to a human (or higher-authority agent) when encountering situations outside its authority or capability. A design feature, not a failure mode. |
| **Escalation Packet** | The structured bundle of information an agent must provide when escalating: context, actions taken, assessment, recommendations, and state. |
| **Execution Orchestrator** | An agentic pattern in which an agent manages end-to-end process execution, routing work to appropriate human and agent performers. |
| **Governance Gradient** | The ZORBA concept that governance intensity varies across layers — highest at Strategy, evolving to continuous monitoring at Work. |
| **Governance Maturity Level** | A classification (G1–G5) of how mature an organisation's agent governance is, from Ad Hoc to Optimising. |
| **Human Override** | The foundational governance principle that any human with appropriate authority can stop, redirect, or take over agent activity at any time. Non-negotiable in ZORBA. |
| **Orchestrator Agent** | An agent type that coordinates and manages workflows involving multiple humans and/or agents. See [Workforce Model](03-workforce-model.md). |
| **Specialist Agent** | An agent type with deep expertise in a narrow domain, invoked for specific tasks. See [Workforce Model](03-workforce-model.md). |
| **Trust Calibration** | The ongoing process of adjusting an agent's autonomy level based on observed performance, trust signals, and changing context. |
| **Trust Signal** | An observable indicator (positive or negative) that informs trust calibration decisions. Examples: decision quality, escalation appropriateness, error rates. |
| **Workforce Composition** | The designed blend of human and agent capability for a given function, process, or activity. An explicit architectural decision in ZORBA. |
| **Workforce Composition Audit** | An assessment of whether the actual human/agent mix matches the designed composition, and whether the designed composition remains appropriate. |

---

## ZORBA Layer Abbreviations

| Abbreviation | Layer |
|-------------|-------|
| **L1** | Strategy |
| **L2** | Objectives |
| **L3** | Capabilities |
| **L4** | Processes |
| **L5** | Activities |
| **L6** | Work |

## ZORBA Autonomy Scale

| Code | Level | Description |
|------|-------|-------------|
| **A0** | Inert | Information only, no authority to act |
| **A1** | Supervised | Acts, but every output requires human approval |
| **A2** | Guided | Autonomous for routine; flags exceptions for review |
| **A3** | Trusted | Autonomous within boundaries; human reviews by exception |
| **A4** | Autonomous | Full authority within scope; human oversight is structural |

## ZORBA Decision Authority Levels

| Code | Level | Description |
|------|-------|-------------|
| **D1** | Human-Only | No agent involvement in the decision |
| **D2** | Human-Decided, Agent-Prepared | Agent prepares, human decides |
| **D3** | Agent-Decided, Human-Approved | Agent decides, human approves before effect |
| **D4** | Agent-Decided, Human-Notified | Agent decides and acts, human notified |
| **D5** | Agent-Decided, Exception-Reported | Agent decides and acts, human sees exceptions only |

## ZORBA Workforce Composition Codes

| Code | Composition | Description |
|------|-------------|-------------|
| **H** | Human-Essential | Must be performed by humans |
| **H+a** | Human-Led, Agent-Supported | Human performs, agent assists |
| **H=A** | Blended | Genuinely shared responsibility |
| **h+A** | Agent-Led, Human-Supervised | Agent performs, human oversees |
| **A** | Agent-Essential | Optimally performed by agents |

## ZORBA Process Notation

| Symbol | Meaning |
|--------|---------|
| **[H]** | Human-executed step |
| **[A]** | Agent-executed step |
| **[H→A]** | Human-to-agent handoff |
| **[A→H]** | Agent-to-human escalation |
| **[H+A]** | Collaborative step |
| **[A⟲]** | Agent autonomous loop |

---

*Previous: [← Governance & Trust Framework](06-governance.md) | Back to: [README →](../index.md)*

---

*© 2026 Zontally. All rights reserved.*
