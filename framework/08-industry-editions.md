# ZORBA Industry Editions

**Zontally Reference Business Architecture**
**Version:** v0.1 (Draft)

---

## Overview

ZORBA is not a one-size-fits-all framework. While the [core architecture](02-architecture.md), [12 domains](04-domain-reference.md), [agentic patterns](05-agentic-patterns.md), and [governance model](06-governance.md) are universal, the way an organisation *instantiates* these elements varies profoundly by industry. A technology services company managing ServiceNow implementations inhabits a fundamentally different operational reality from a hospital managing clinical pathways or a manufacturer managing production lines.

**Industry Editions** are ZORBA's answer to this reality. They are curated, opinionated compositions of the core framework — pre-configured for a specific vertical. Not a fork. Not a separate product. An **instantiation template** that accelerates adoption by providing industry-relevant defaults, taxonomies, processes, and workforce composition guidance.

Every edition builds on **ZORBA Core**. Every edition is compatible with Core. And every edition can be customised further to suit a specific organisation.

---

## The Edition Model

### ZORBA Core

ZORBA Core is the universal, industry-agnostic foundation:

- The **six-layer architecture** (Strategy → Work) as defined in the [Framework Architecture](02-architecture.md)
- The **12 enterprise domains** and their L2 capabilities as defined in the [Domain Reference Model](04-domain-reference.md)
- The **Blended Workforce Model** — agent types, collaboration patterns, trust levels (see [03-workforce-model.md](03-workforce-model.md))
- The **Agentic Enterprise Patterns** library (see [05-agentic-patterns.md](05-agentic-patterns.md))
- The **Governance & Trust Framework** (see [06-governance.md](06-governance.md))
- The **Information Model** — business object graph, node types, edge types (see [07-information-model.md](07-information-model.md))
- The **meta-model** — how domains, capabilities, processes, activities, and work instances relate

Core is complete on its own. An organisation can adopt ZORBA Core without any industry edition and build their own configuration. But most will benefit from starting with an edition that reflects their operational context.

### Industry Editions

An Industry Edition is a **curated composition** that pre-configures ZORBA Core for a specific vertical. It answers the question: *"Given what we know about this industry, what does a well-architected blended workforce look like?"*

Editions are:

- **Opinionated but not prescriptive** — They recommend; they do not mandate
- **Additive, not subtractive** — They extend Core; they never remove from it
- **Independently versioned** — An edition may release updates on its own cadence, provided it remains compatible with the Core version it targets
- **Composable** — Organisations operating across industries (e.g., a healthcare technology company) can draw from multiple editions

```
┌─────────────────────────────────────────────────────────────────┐
│                        ZORBA Core                               │
│  6-layer architecture · 12 domains · meta-model · governance    │
│  agentic patterns · information model · glossary                │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┤
│ Tech     │ Health-  │ Financial│ Manufac- │ Profess- │ Retail & │
│ Service  │ care     │ Services │ turing   │ ional    │ Consumer │
│ Providers│          │          │          │ Services │          │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

---

## What an Industry Edition Contains

Each Industry Edition customises the following eight dimensions of ZORBA Core:

### 1. Domain Emphasis

Not all 12 domains carry equal weight in every industry. An edition defines which domains are **primary** (core to the industry's value chain), **secondary** (important but supporting), and **foundational** (necessary but not differentiating).

| Dimension | Technology Service Providers | Healthcare | Manufacturing |
|-----------|---------------------------|------------|---------------|
| **Primary** | Operations & Delivery, Technology & Data, Customer Success | Operations & Delivery, Risk/Legal/Compliance, People & Talent | Operations & Delivery, Supply Chain, Product & Innovation |
| **Secondary** | Sales, Strategy & Governance, People & Talent | Technology & Data, Product & Innovation, Finance | Technology & Data, Finance, Quality (within Operations) |
| **Foundational** | Finance, Marketing, Supply Chain, Corporate Services | Marketing, Sales, Corporate Services, Supply Chain | Sales, Marketing, People & Talent, Corporate Services |

### 2. Extended Domain Taxonomy

Core defines L2 capabilities for each domain. Editions extend these with **industry-specific L2 and L3 capabilities** that reflect the operational vocabulary and structure of the vertical.

**Example — Operations & Delivery:**

| Level | ZORBA Core | Tech Service Providers | Healthcare |
|-------|-----------|----------------------|------------|
| L2 | Production / Service Delivery | Service Delivery Management | Clinical Service Delivery |
| L3 | — | Incident Management | Patient Triage & Assessment |
| L3 | — | Change Management | Clinical Pathway Management |
| L3 | — | Problem Management | Treatment Administration |
| L3 | — | Release Management | Discharge Planning |
| L2 | Quality Management & Assurance | Service Quality & SLA Management | Clinical Quality & Patient Safety |
| L3 | — | SLA Monitoring & Reporting | Adverse Event Management |
| L3 | — | Customer Satisfaction Measurement | Clinical Audit |

### 3. Reference Processes

Editions pre-map **industry-standard processes** onto ZORBA's six-layer architecture, complete with workforce composition markers (as defined in the [Framework Architecture](02-architecture.md)).

- **Technology Service Providers:** ITIL-aligned service processes, project delivery lifecycles, practice management workflows
- **Healthcare:** Patient admission-to-discharge pathways, clinical decision flows, regulatory reporting processes
- **Financial Services:** Trade lifecycle, KYC/AML processes, regulatory reporting workflows
- **Manufacturing:** Production planning, quality inspection, supply chain fulfilment processes

### 4. Agentic Maturity Profiles

While Core defines agentic maturity at the domain level (see [Domain Reference Model](04-domain-reference.md)), editions refine this to **industry-specific activities** — identifying which activities are most ready for agent participation in the context of that particular vertical.

| Activity Area | Tech Services Readiness | Healthcare Readiness | Manufacturing Readiness |
|---------------|------------------------|---------------------|------------------------|
| Incident triage & classification | ●●●●● | ●●●○○ | ●●●●○ |
| Document generation | ●●●●● | ●●●●● | ●●●●○ |
| Scheduling & resource allocation | ●●●●○ | ●●●●● | ●●●●● |
| Diagnostic/analytical decisions | ●●●○○ | ●●○○○ | ●●●●○ |
| Regulatory compliance monitoring | ●●●●○ | ●●●●● | ●●●●● |
| Customer/patient interaction | ●●●○○ | ●●○○○ | ●●○○○ |

### 5. Workforce Composition Templates

Recommended **human/agent splits by domain** for the industry, expressed using ZORBA's composition notation (H, H+a, H=A, h+A, A):

| Domain | Tech Services | Healthcare | Financial Services |
|--------|--------------|------------|-------------------|
| Strategy & Governance | H+a | H+a | H+a |
| Operations & Delivery | H=A | H+a | h+A |
| Technology & Data | h+A | H=A | h+A |
| Customer Success & Service | H=A | H+a | H=A |
| People & Talent | H+a | H+a | H+a |
| Finance | h+A | h+A | H=A |
| Risk, Legal & Compliance | H+a | H+a | H=A |

### 6. Compliance & Governance Overlays

Industry-specific regulatory requirements that extend ZORBA's [Governance & Trust Framework](06-governance.md):

| Industry | Key Regulatory Frameworks | Agent-Specific Implications |
|----------|--------------------------|---------------------------|
| Technology Service Providers | SOC 2, ISO 27001, GDPR, industry-specific client requirements | Agent access controls, data handling policies, audit trail requirements for client data |
| Healthcare | HIPAA, FDA (where applicable), clinical governance standards | Strict limits on agent autonomy in clinical decisions, patient data handling, consent management |
| Financial Services | Basel III/IV, MiFID II, SOX, AML/KYC regulations | Agent decision audit trails for regulated activities, model risk management, explainability requirements |
| Manufacturing | ISO 9001, industry safety standards, environmental regulations | Agent authority limits for safety-critical operations, quality record integrity |
| Retail & Consumer | PCI DSS, consumer protection, GDPR/CCPA | Agent handling of payment data, personalisation within privacy bounds |

### 7. Metrics Library

Industry-standard KPIs pre-mapped to ZORBA domains and layers:

- **Technology Service Providers:** SLA attainment, mean time to resolution (MTTR), utilisation rate, customer satisfaction (CSAT), net promoter score (NPS), backlog velocity, revenue per consultant
- **Healthcare:** Patient wait times, readmission rates, bed occupancy, clinical outcome measures, staff-to-patient ratios, regulatory compliance scores
- **Financial Services:** Cost-to-income ratio, trade settlement rates, regulatory capital ratios, customer lifetime value, fraud detection rates

### 8. Agent Role Catalogue

Recommended AI agent roles specific to the industry, extending the agent types defined in the [Blended Workforce Model](03-workforce-model.md):

**Example — Technology Service Providers:**

| Agent Role | Domain | Primary Function | Autonomy Level |
|-----------|--------|-----------------|----------------|
| Incident Triage Agent | Operations & Delivery | Classify, prioritise, and route incoming incidents | A3–A4 |
| Change Risk Assessor | Operations & Delivery | Evaluate change requests against risk criteria and historical patterns | A2–A3 |
| Knowledge Curator | Customer Success & Service | Generate, maintain, and recommend knowledge articles | A3 |
| Resource Scheduler | People & Talent / Operations | Optimise consultant allocation across engagements | A3 |
| SLA Monitor | Customer Success & Service | Continuously monitor service levels and alert on breach risk | A4 |
| Customer Health Analyst | Customer Success & Service | Score customer health and recommend intervention actions | A3 |
| Proposal Drafter | Sales | Generate proposal documents from templates, requirements, and historical data | A2–A3 |
| Platform Monitor | Technology & Data | Monitor ServiceNow instances and recommend optimisations | A3–A4 |

---

## ZORBA for Technology Service Providers — Flagship Edition

The first planned Industry Edition targets **technology service providers** — the companies that implement, manage, and extend enterprise platforms. This includes ServiceNow ecosystem partners, managed service providers (MSPs), IT consulting firms, and technology integrators.

### Why This Edition First

Technology service providers are:

1. **Architecturally literate** — They understand frameworks, processes, and governance
2. **Experiencing acute workforce pressure** — Talent scarcity in the ServiceNow ecosystem is well-documented
3. **Naturally suited to agentic augmentation** — Much of their delivery work is pattern-based and well-documented
4. **Early adopters** — Technology companies adopt new operational models faster than most verticals
5. **Zontally's home market** — Deep domain expertise and existing relationships

### Target Market

| Segment | Description | Typical Size |
|---------|-------------|-------------|
| Boutique consultancies | Specialist ServiceNow or IT advisory firms | 10–50 people |
| Mid-market integrators | Multi-practice technology service firms | 50–500 people |
| Large MSPs | Managed service providers with multiple platform practices | 500–5,000 people |
| Global system integrators | Large-scale technology consulting and outsourcing | 5,000+ people |

### Domain Emphasis

| Domain | Emphasis | Rationale |
|--------|----------|-----------|
| **Operations & Delivery** | ★★★★★ Primary | Service delivery is the core value proposition |
| **Technology & Data** | ★★★★★ Primary | Platform expertise is the product |
| **Customer Success & Service** | ★★★★☆ Primary | Client retention and expansion drive growth |
| **Sales** | ★★★★☆ Secondary | Pipeline and deal management are critical |
| **Strategy & Governance** | ★★★☆☆ Secondary | Practice strategy and governance maturity |
| **People & Talent** | ★★★☆☆ Secondary | Talent acquisition and utilisation are key constraints |
| **Finance** | ★★☆☆☆ Foundational | Standard financial operations |
| **Product & Innovation** | ★★☆☆☆ Foundational | IP and accelerator development where applicable |
| **Marketing** | ★★☆☆☆ Foundational | Demand generation and thought leadership |
| **Risk, Legal & Compliance** | ★★☆☆☆ Foundational | Client compliance requirements, SOC 2 |
| **Supply Chain** | ★☆☆☆☆ Foundational | Minimal — primarily subcontractor management |
| **Corporate Services** | ★☆☆☆☆ Foundational | Standard corporate operations |

### Industry-Specific Capabilities

The edition extends Core with the following L2/L3 capabilities:

**Operations & Delivery — Extended:**
- Service Delivery Management (Incident, Problem, Change, Release)
- Practice Management (methodology, standards, tooling per practice)
- Engagement Delivery (project/programme execution for client work)
- Managed Services Operations (ongoing client environment management)

**Technology & Data — Extended:**
- Platform Operations (ServiceNow instance management, upgrades, monitoring)
- Solution Architecture (client solution design and documentation)
- Development & Configuration (platform development practices)
- Integration Management (client system integrations)

**Customer Success & Service — Extended:**
- Customer Lifecycle Management (onboarding → adoption → expansion → renewal)
- Service Level Management (SLA design, monitoring, reporting)
- Customer Health & Advocacy (health scoring, reference programme)

**People & Talent — Extended:**
- Resource Management (consultant allocation, bench management, utilisation)
- Skills & Certification Management (platform certifications, skill matrices)
- Practice Development (training, mentoring, career pathways per practice)

**Sales — Extended:**
- Solution Selling (technical pre-sales, proof of concept, demos)
- Partner & Alliance Management (platform vendor relationships)
- Proposal & RFP Management (bid management, proposal generation)

### High Agent-Readiness Areas

Activities with the strongest case for immediate agent participation:

| Activity | Current State | Agent Opportunity | Expected Impact |
|----------|--------------|-------------------|----------------|
| Incident triage & classification | Manual review by L1 engineers | Agent classifies, prioritises, routes; resolves known issues autonomously | 60–80% of L1 incidents handled without human intervention |
| Change risk assessment | Manual CAB review process | Agent evaluates risk against historical data and policy | Faster change cycles, reduced risk of missed impacts |
| Knowledge article generation | Sporadic, human-authored | Agent generates articles from resolved incidents and documented solutions | 10x knowledge base growth, continuous freshness |
| Resource scheduling | Spreadsheets and manual allocation | Agent optimises allocation against skills, availability, utilisation targets | Higher utilisation, better skills matching |
| SLA monitoring & alerting | Dashboard-based, reactive | Agent continuously monitors and proactively alerts on breach risk | Shift from reactive to predictive SLA management |
| Customer health scoring | Quarterly manual reviews | Agent continuously scores from engagement data, support tickets, usage patterns | Real-time health visibility, earlier intervention |
| Proposal generation | Manual, time-intensive | Agent drafts proposals from templates, past wins, and requirements | 70% reduction in proposal preparation time |
| Platform monitoring | Reactive monitoring with basic alerts | Agent monitors instances, detects anomalies, recommends or executes remediation | Reduced downtime, proactive optimisation |

### Reference Frameworks

The Technology Service Providers edition maps to established industry frameworks:

| Framework | Mapping |
|-----------|---------|
| **ITIL 4** | Service management processes map to Operations & Delivery capabilities. ITIL practices become reference processes within the edition. |
| **COBIT 2019** | IT governance objectives align with Strategy & Governance and Risk, Legal & Compliance domains. |
| **SAFe** | Agile delivery practices map to Engagement Delivery capabilities. Portfolio management maps to Strategy & Governance. |
| **CMMI** | Maturity levels inform the edition's capability maturity assessment approach. |
| **SIAM** | Service integration patterns map to multi-supplier Operations & Delivery scenarios. |

### Example Organisation Structures

**Boutique Consultancy — 30 People**

```
┌─────────────────────────────────────┐
│         Managing Director (H)       │
├──────────┬──────────┬───────────────┤
│ Delivery │ Sales &  │ Operations    │
│ (12H+4A) │ Growth   │ (3H+6A)      │
│          │ (4H+2A)  │               │
│ Consult- │ Account  │ Finance,      │
│ ants,    │ mgmt,    │ HR, admin,    │
│ architects│ pre-sales│ scheduling   │
└──────────┴──────────┴───────────────┘
H = Human  A = Agent

Total: 20 humans + 12 agents
Agent roles: Resource Scheduler, SLA Monitor, 
Knowledge Curator, Incident Triage (×2), 
Proposal Drafter, Customer Health Analyst,
Platform Monitor (×2), Finance Agent, 
HR Admin Agent, Marketing Agent
```

**Large MSP — 2,000+ People**

```
┌──────────────────────────────────────────────┐
│              CEO / Executive Team (H)         │
├─────────┬─────────┬─────────┬────────────────┤
│Service  │Managed  │Sales &  │Corporate       │
│Delivery │Services │Marketing│Functions        │
│(600H    │(400H    │(200H    │(150H           │
│ +200A)  │ +300A)  │ +80A)   │ +120A)         │
│         │         │         │                │
│Projects,│NOC, SOC,│Account  │Finance, HR,    │
│consult- │platform │teams,   │legal, IT,      │
│ing,     │ops,     │demand   │governance      │
│advisory │support  │gen      │                │
└─────────┴─────────┴─────────┴────────────────┘
Total: ~1,350 humans + ~700 agents
Agent density highest in Managed Services (43%)
and Corporate Functions (44%)
```

---

## Additional Planned Editions

### ZORBA for Healthcare

**Target market:** Hospitals, health systems, clinical networks, healthcare technology providers.

| Dimension | Details |
|-----------|---------|
| **Primary domains** | Operations & Delivery, Risk/Legal/Compliance, People & Talent |
| **Key capabilities** | Clinical Pathway Management, Patient Journey Orchestration, Regulatory Compliance & Reporting, Workforce Scheduling & Credentialing |
| **High agent-readiness** | Appointment scheduling, clinical documentation, discharge summaries, regulatory reporting, supply management, patient communication |
| **Low agent-readiness** | Clinical diagnosis, treatment decisions, end-of-life care, complex triage |
| **Regulatory overlay** | HIPAA, clinical governance standards, medical device regulations, patient consent frameworks |
| **Key metrics** | Patient wait times, readmission rates, length of stay, clinical outcome measures, staff-to-patient ratios |
| **Defining tension** | Enormous efficiency opportunity vs. patient safety imperatives requiring strict agent autonomy limits |

### ZORBA for Financial Services

**Target market:** Banks, insurance companies, asset managers, fintech firms, payment processors.

| Dimension | Details |
|-----------|---------|
| **Primary domains** | Finance, Risk/Legal/Compliance, Operations & Delivery, Customer Success |
| **Key capabilities** | Trading Operations, Regulatory Reporting, Risk Modelling, Customer Lifecycle Management, Fraud Detection & Prevention |
| **High agent-readiness** | Transaction processing, reconciliation, regulatory reporting, fraud screening, KYC data gathering, portfolio rebalancing |
| **Low agent-readiness** | Credit judgement on novel cases, regulatory interpretation, client relationship management, ethical investment decisions |
| **Regulatory overlay** | Basel III/IV, MiFID II, SOX, AML/KYC, PSD2, consumer protection |
| **Key metrics** | Cost-to-income ratio, regulatory capital ratios, trade settlement rates, fraud detection/false positive rates |
| **Defining tension** | Heavily regulated environment demands explainability and audit trails for every agent action |

### ZORBA for Manufacturing

**Target market:** Discrete and process manufacturers, industrial companies, automotive, aerospace, consumer goods.

| Dimension | Details |
|-----------|---------|
| **Primary domains** | Operations & Delivery, Supply Chain, Product & Innovation |
| **Key capabilities** | Production Planning & Scheduling, Quality Management, Supply Chain Orchestration, Predictive Maintenance, Product Lifecycle Management |
| **High agent-readiness** | Production scheduling, quality inspection, predictive maintenance, demand forecasting, inventory optimisation, logistics coordination |
| **Low agent-readiness** | Product design innovation, supplier negotiation, safety-critical decisions, workforce relations |
| **Regulatory overlay** | ISO 9001, industry safety standards (automotive, aerospace, food), environmental regulations |
| **Key metrics** | OEE (Overall Equipment Effectiveness), defect rates, on-time delivery, inventory turns, maintenance costs |
| **Defining tension** | Physical-digital boundary — agents optimise the digital twin but humans manage the physical reality |

### ZORBA for Professional Services

**Target market:** Management consultancies, law firms, accounting firms, engineering consultancies, design agencies.

| Dimension | Details |
|-----------|---------|
| **Primary domains** | Operations & Delivery, People & Talent, Customer Success, Sales |
| **Key capabilities** | Project Delivery Management, Utilisation & Resource Management, Knowledge Management, Client Relationship Management, Practice Development |
| **High agent-readiness** | Time tracking, resource scheduling, knowledge retrieval, document drafting, project status reporting, invoice generation |
| **Low agent-readiness** | Client advisory, expert judgement, business development relationships, creative problem-solving |
| **Regulatory overlay** | Professional licensing, client confidentiality, industry-specific regulations (legal, accounting) |
| **Key metrics** | Utilisation rate, revenue per professional, project margin, client satisfaction, knowledge reuse rate |
| **Defining tension** | The product is human expertise — agents must augment without commoditising the core value proposition |

### ZORBA for Retail & Consumer

**Target market:** Retailers, e-commerce platforms, consumer brands, hospitality, food & beverage.

| Dimension | Details |
|-----------|---------|
| **Primary domains** | Operations & Delivery, Supply Chain, Customer Success, Marketing |
| **Key capabilities** | Omnichannel Operations, Merchandising & Assortment, Supply Chain & Fulfilment, Customer Experience Management, Demand Planning |
| **High agent-readiness** | Demand forecasting, inventory management, personalised marketing, customer service, pricing optimisation, fulfilment coordination |
| **Low agent-readiness** | Brand strategy, product curation, store experience design, supplier relationship management |
| **Regulatory overlay** | PCI DSS, consumer protection, GDPR/CCPA, food safety (where applicable) |
| **Key metrics** | Revenue per square foot/visit, conversion rate, inventory turn, customer lifetime value, fulfilment speed |
| **Defining tension** | Balancing hyper-personalisation (agent-driven) with authentic brand experience (human-curated) |

---

## Edition Lifecycle

### Versioning

Each edition carries its own version number alongside the Core version it targets:

```
ZORBA Core v1.2
└── ZORBA for Technology Service Providers v1.0 (targets Core v1.x)
└── ZORBA for Healthcare v0.9-beta (targets Core v1.x)
```

Editions follow semantic versioning. A major Core version change may require edition updates; minor Core changes are backwards-compatible.

### Adoption Path

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  1. Assess   │───▶│  2. Adopt    │───▶│  3. Customise│───▶│  4. Evolve   │
│              │    │   Edition    │    │              │    │              │
│ Evaluate fit │    │ Deploy the   │    │ Tailor to    │    │ Contribute   │
│ of edition   │    │ edition as   │    │ organisation │    │ back, track  │
│ to org       │    │ starting     │    │ specifics    │    │ Core updates │
│              │    │ point        │    │              │    │              │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

1. **Assess** — Evaluate which edition best fits the organisation's industry and operating model. Organisations spanning multiple industries may adopt a primary edition and draw capabilities from others.
2. **Adopt** — Deploy the edition as the baseline configuration. This provides immediate structure: domain emphasis, taxonomy, reference processes, and workforce composition templates.
3. **Customise** — Tailor the edition to the specific organisation. Adjust domain weights, extend the taxonomy, modify workforce composition targets, and add organisation-specific processes.
4. **Evolve** — Continuously refine as the organisation matures. Contribute improvements back to the community edition. Track Core and edition updates for compatibility.

### Community Contributions

Industry Editions benefit from community input:

- **Taxonomy extensions** — Industry practitioners contribute L3 and L4 capability definitions
- **Reference processes** — Organisations share proven process patterns (anonymised)
- **Agent role definitions** — New agent roles validated in production
- **Metrics** — Industry-specific KPIs and benchmarks
- **Compliance overlays** — Regulatory expertise from domain specialists

Contributions follow a review process to maintain quality and coherence with Core.

### Migration Paths

| From | To | Approach |
|------|----|----------|
| ZORBA Core (no edition) | Industry Edition | Overlay the edition onto existing Core configuration; map existing customisations to edition structure |
| One Industry Edition | Another | Identify shared Core elements (retained), edition-specific elements (replaced), and custom elements (re-evaluated) |
| Pre-ZORBA (no framework) | Industry Edition | Use the edition as a greenfield starting template; highest adoption velocity |

---

## Commercial Positioning

### IP Model

Each Industry Edition represents **distinct intellectual property**:

- **ZORBA Core** — Open framework, community-maintained, freely available
- **Community Editions** — Open, community-contributed industry editions with Zontally stewardship
- **Commercial Editions** — Zontally-developed and maintained editions with premium content, tooling, and support

### Partner Ecosystem

| Role | Description |
|------|-------------|
| **Edition Contributors** | Industry experts who contribute to community editions (taxonomy, processes, agent roles) |
| **Edition Partners** | Consulting firms licensed to deliver ZORBA adoption using commercial editions |
| **Edition Builders** | Partners who develop new industry editions under Zontally's framework and quality standards |
| **Platform Partners** | Technology vendors who integrate ZORBA editions into their platforms |

### Commercial Model

```
┌─────────────────────────────────────────────────────┐
│                    ZORBA Core                        │
│                  (Open / Free)                       │
├─────────────────────┬───────────────────────────────┤
│  Community Editions │     Commercial Editions        │
│  (Open / Free)      │     (Licensed / Supported)     │
│                     │                               │
│  Community-         │  Zontally-developed:          │
│  contributed,       │  • Premium content            │
│  Zontally-curated   │  • Tooling & templates        │
│                     │  • Professional support       │
│                     │  • Certified training         │
└─────────────────────┴───────────────────────────────┘
```

The flagship **ZORBA for Technology Service Providers** edition will be the first commercial edition, developed and maintained by Zontally with deep domain expertise in the ServiceNow ecosystem.

---

*Previous: [← Information Model](07-information-model.md)*

---

*© 2026 Zontally. All rights reserved.*
