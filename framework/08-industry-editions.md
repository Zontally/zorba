# ZORBA Industry Editions

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
- **Additive, not subtractive** — They extend Core; they sometimes remove from it
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

## Edition Lifecycle

### Versioning

Each edition carries its own version number alongside the Core version it targets:

```
ZORBA Core v1.2
└── ZORBA for Enterprise Software v1.0 (targets Core v1.x)
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

---

*Previous: [← Information Model](07-information-model.md)*

---

*© 2026 Zontally. All rights reserved.*
