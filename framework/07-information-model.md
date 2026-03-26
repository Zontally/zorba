# ZORBA Information Model

## Overview

The ZORBA Information Model defines the **universal business object graph** — the node types, edge types, composition rules, and traversal patterns that allow humans and AI agents to represent, query, and reason about any enterprise architecture.

This model is deliberately **framework-agnostic**. While ZORBA's [12-domain taxonomy](04-domain-reference.md) provides a recommended starting template, the information model supports any classification scheme — APQC Process Classification Framework (PCF), TOGAF, custom taxonomies, or hybrids. The data model is not ZORBA-specific; it is a universal business architecture object model that ZORBA (and any other framework) instantiates.

### Design Principles

1. **Framework-agnostic meta-model.** Object types and relationship types are independent of any particular domain taxonomy. A customer already using APQC/PCF can deploy the same object graph with their existing classification.

2. **Permissive, not rigid.** A 50-person company with a single line of business and a multinational conglomerate with dozens of operating units must both be representable without forcing unnatural structures. Cardinalities are generous; required fields are minimal.

3. **Machine-readable by design.** Every object and relationship is typed, directional, and traversable. AI agents must be able to query the graph — "what objectives connect to this capability?", "what processes does this team own?", "trace this work item back to strategic intent" — without human intermediation.

4. **Recommended templates + customisation.** The object types and relationship types defined here are a recommended starting set. Organisations are encouraged to extend, rename, or restructure them to fit their reality.

---

## Core Business Objects

The following table defines the **node types** in the business object graph. Each object type is independent of any particular framework — ZORBA's 12 domains, APQC's process groups, or a bespoke taxonomy all instantiate the same types.

### Object Type Reference

| Object Type | Description | Required? | Cardinality Notes |
|-------------|-------------|-----------|-------------------|
| **Framework** | A top-level container representing a classification scheme (e.g., "ZORBA v1", "APQC PCF v7.3", "Custom Retail Ops"). An organisation may have multiple active frameworks. | Yes (≥1) | One or more per organisation. Multiple frameworks may coexist. |
| **Domain** | A major area of enterprise activity. In ZORBA this maps to the [12 domains](04-domain-reference.md); in APQC/PCF it maps to process categories; in a custom framework it maps to whatever top-level grouping the organisation uses. | Yes (≥1) | Domains nest: a domain may contain sub-domains to arbitrary depth (recommended ≤4 levels). |
| **Capability** | What the organisation can do — an ability independent of how it is delivered. Maps to ZORBA [Layer 3](02-architecture.md). | Recommended | Capabilities nest within domains. A capability may belong to multiple domains (shared capability). |
| **Process** | How work flows — a structured sequence of activities that delivers a capability. Maps to ZORBA [Layer 4](02-architecture.md). | Recommended | A process belongs to one or more capabilities. Processes may be shared across lines of business. |
| **Activity** | A discrete unit of work within a process. Maps to ZORBA [Layer 5](02-architecture.md). | Optional | Activities compose within processes. An activity may appear in multiple processes (reusable activity). |
| **Work Item** | An actual instance of executed work — a ticket, transaction, case, or task. Maps to ZORBA [Layer 6](02-architecture.md). | Optional | Work items are instances of activities. Volume is unbounded. |
| **Strategy** | A strategic intent document — vision statement, strategic plan, strategic theme. Maps to ZORBA [Layer 1](02-architecture.md). | Recommended | Typically few per organisation. May be scoped to a line of business or shared across the enterprise. |
| **Objective** | A measurable target — OKR, KPI target, goal, milestone. Maps to ZORBA [Layer 2](02-architecture.md). | Recommended | Objectives nest (strategic → tactical → operational). An objective may align to multiple strategies. |
| **Initiative** | A bounded effort to achieve one or more objectives — a programme, project, or workstream. | Optional | Initiatives connect objectives to work. An initiative may serve multiple objectives. |
| **Role** | A named function performed by a human or agent — "Financial Controller", "Tier-1 Support Agent", "Data Steward". | Recommended | Roles are assigned to teams and may be filled by humans, agents, or both. |
| **Agent** | An AI agent participating in the workforce. See the [Blended Workforce Model](03-workforce-model.md) for agent taxonomy and trust levels. | Optional | An agent may fill one or more roles. Agent objects carry autonomy-level and trust metadata. |
| **Team** | A group of humans and/or agents that owns or operates business objects. | Recommended | Teams own processes, capabilities, or domains. A team may contain sub-teams. |
| **Organisational Unit** | A structural entity within the enterprise — holding company, subsidiary, business unit, brand, division, region, department, or any other organisational grouping. Organisational Units nest recursively to model any corporate structure. | Yes (≥1) | Organisational Units are the **root of the object graph**. Every other object is ultimately scoped to one or more Organisational Units. Nest to arbitrary depth. |
| **Metric** | A measurable indicator — KPI, SLA, quality score, throughput measure. In ZORBA, **Measurements** are first-class peers to Activities within Processes, making process performance evaluation an explicit architectural concern alongside process execution. | Optional | Metrics attach to objectives, processes, capabilities, or any other object type. Measurements (a specialisation of Metric) sit as peers to Activities under Processes. |
| **WardleyMap** | A Wardley Map expressed as code using the Online Wardley Maps (OWM) DSL. Contains the map source (OWM DSL text), scoped to an Organisational Unit or Domain. Maps visualise the evolution of capabilities, processes, and their dependencies. | Optional | Maps can be scoped to domains, capabilities, value chains, or custom boundaries. Multiple maps may represent different views of the same architecture. |

### Recommended Attributes per Object Type

Every object carries a common set of base attributes plus type-specific extensions.

**Base attributes (all object types):**

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String (UUID) | Globally unique identifier |
| `type` | Enum | The object type (from table above) |
| `name` | String | Human-readable name |
| `description` | Text | Prose description |
| `framework_id` | String (UUID) | The framework this object belongs to (or `null` for framework-independent objects) |
| `parent_id` | String (UUID) | Parent object of the same type (for hierarchical nesting), nullable |
| `owner_id` | String (UUID) | The team or role that owns this object, nullable |
| `status` | Enum | `draft`, `active`, `deprecated`, `archived` |
| `tags` | String[] | Freeform tags for filtering and grouping |
| `metadata` | Map | Arbitrary key-value pairs for custom attributes |
| `created_at` | Timestamp | Creation timestamp |
| `updated_at` | Timestamp | Last modification timestamp |

**Type-specific attributes:**

| Object Type | Additional Attributes |
|-------------|----------------------|
| **Framework** | `version`, `source` (e.g., "ZORBA", "APQC", "Custom"), `uri` (canonical reference) |
| **Domain** | `level` (depth in hierarchy, 1 = top) |
| **Capability** | `maturity_level`, `workforce_composition` (human/agent/blended), `target_composition`, `evolution_stage` (enum: genesis, custom, product, commodity), `evolution_target` (same enum — where it's heading), `evolution_confidence` (float 0-1), `pst_phase` (enum: pioneer, settler, town_planner) |
| **Process** | `process_type` (core, support, management), `sla`, `automation_percentage`, `evolution_stage` (enum: genesis, custom, product, commodity), `evolution_target` (same enum — where it's heading), `evolution_confidence` (float 0-1), `pst_phase` (enum: pioneer, settler, town_planner) |
| **Activity** | `performer_type` (human-only, agent-capable, agent-preferred, agent-only), `autonomy_level` (A0–A4) |
| **Work Item** | `performer_id`, `confidence`, `review_status`, `lineage` (trace to strategy), `started_at`, `completed_at` |
| **Strategy** | `time_horizon`, `scope` (enterprise, LOB, domain) |
| **Objective** | `target_value`, `current_value`, `unit`, `cadence` (annual, quarterly, monthly), `objective_type` (OKR, KPI, goal) |
| **Organisational Unit** | `unit_type` (holding_company, subsidiary, business_unit, brand, division, region, department, team, custom), `legal_entity` (boolean), `industry_edition` (e.g., "ZORBA for Healthcare", nullable), `country`, `currency` |
| **Initiative** | `start_date`, `end_date`, `budget`, `initiative_status` (planned, active, completed, cancelled) |
| **Role** | `performer_type` (human, agent, either), `authority_level` |
| **Agent** | `agent_type` (see [Workforce Model](03-workforce-model.md)), `trust_level`, `autonomy_level`, `platform`, `model` |
| **Team** | `team_type` (human, blended, agent-only), `member_count`, `agent_count` |
| **Metric** | `unit`, `direction` (higher-is-better, lower-is-better, target-is-best), `frequency`, `source_system`. **Measurement-specific** (when used as a process peer): `what` (what it measures), `why` (why it matters), `how` (formula/calculation method), `frequency` (daily/weekly/monthly/quarterly/annually), `direction` (higher_is_better, lower_is_better) |
| **WardleyMap** | `owm_source` (Text - the OWM DSL map code), `map_scope` (enum: domain, capability, value_chain, custom), `evolution_context` (Text - narrative context for the map) |

---

## Relationship Types

Relationships are the **edges** in the business object graph. Every relationship is **typed** and **directional** — source → target — with defined cardinality and semantics.

### Relationship Type Reference

| Relationship Type | Description | Source Type(s) | Target Type(s) | Cardinality | Required? |
|-------------------|-------------|----------------|-----------------|-------------|-----------|
| **contains** | Hierarchical parent-child within the same type | Domain, Capability, Process, Objective, Team | Same as source | 1:N | No |
| **belongs_to** | Object is classified under a framework or domain | Any | Framework, Domain | N:1 or N:M | Recommended |
| **decomposes_into** | Compositional: a higher-level object breaks down into lower-level objects of a different type | Domain → Capability, Capability → Process, Process → Activity | (implied by pairing) | 1:N | Recommended |
| **instantiates** | A work item is an instance of an activity | Work Item | Activity | N:1 | Recommended |
| **aligns_to** | Strategic alignment: an object contributes to a higher-level intent | Objective → Strategy, Initiative → Objective, Work Item → Initiative | (implied by pairing) | N:M | Recommended |
| **owns** | Accountability: a team or role is accountable for an object | Team, Role | Domain, Capability, Process, Activity, Initiative | 1:N | Recommended |
| **performs** | Agency: a human, agent, or team executes work | Agent, Role, Team | Activity, Work Item | N:M | Recommended |
| **measures** | A metric measures the performance of an object | Metric | Objective, Process, Capability, Activity, Domain | N:M | Optional |
| **depends_on** | A dependency between objects | Process, Capability, Activity | Process, Capability, Activity | N:M | Optional |
| **collaborates_with** | Two objects work together (non-hierarchical) | Team, Agent, Role | Team, Agent, Role | N:M | Optional |
| **fills** | An agent or human fills a role | Agent, (Human reference) | Role | N:M | Recommended |
| **scoped_to** | Object is scoped to an organisational unit. This is the primary mechanism for multi-entity modelling — each OU gets its own domain trees, strategies, and teams. | Any | Organisational Unit | N:M | Recommended |
| **parent_unit** | An organisational unit belongs to a parent unit (corporate hierarchy). | Organisational Unit | Organisational Unit | N:1 | Optional (top-level units have no parent) |
| **maps** | A Wardley Map visualises objects | WardleyMap | Domain, Capability, Process, Organisational Unit | 1:N | Optional |
| **evolves_to** | Tracks planned evolution movement | Capability, Process | Capability, Process | 1:1 | Optional |

### Relationship Attributes

Every relationship edge carries:

| Attribute | Type | Description |
|-----------|------|-------------|
| `id` | String (UUID) | Unique edge identifier |
| `type` | Enum | Relationship type (from table above) |
| `source_id` | String (UUID) | Source object |
| `target_id` | String (UUID) | Target object |
| `metadata` | Map | Arbitrary key-value pairs (e.g., `effective_from`, `weight`, `notes`) |
| `status` | Enum | `active`, `proposed`, `deprecated` |
| `created_at` | Timestamp | Creation timestamp |

---

## Composition Rules

### Hierarchical Nesting

Objects of the same type may nest to arbitrary depth using the `contains` relationship. Recommended maximum depths:

| Object Type | Recommended Max Depth | Example |
|-------------|----------------------|---------|
| Organisational Unit | Unbounded | Holding Co → Subsidiary → Business Unit → Division → Department |
| Domain | 4 | Enterprise → Division → Department → Sub-function |
| Capability | 5 | L0 → L1 → L2 → L3 → L4 |
| Process | 3 | End-to-end → Sub-process → Procedure |
| Objective | 3 | Strategic → Tactical → Operational |
| Team | 4 | Organisation → Division → Squad → Sub-team |

These are recommendations, not constraints. The model imposes no hard limits.

### Organisational Structure & Multi-Instantiation

The **Organisational Unit** object type is the root of the entire business object graph. It models corporate structure — holding companies, subsidiaries, business units, brands, divisions, regions, departments — as a recursive hierarchy. Every other object in the model is ultimately `scoped_to` one or more Organisational Units.

```
OU: ACME Corp (type: holding_company)
├── OU: ACME Health (type: business_unit, industry_edition: "ZORBA for Healthcare")
│   ├── Domain: "Supply Chain" → healthcare-specific capabilities
│   │   └── Capability: "Pharmaceutical Procurement"
│   │       └── Process: "Controlled Substance Supply Chain"
│   ├── Domain: "Operations & Delivery" → clinical service delivery
│   └── Strategy: "ACME Health 2027 Growth Plan"
│
├── OU: ACME Digital (type: business_unit, industry_edition: "ZORBA for Technology Service Providers")
│   ├── Domain: "Supply Chain" → completely different: subcontractors, cloud vendors
│   │   └── Capability: "Technology Partner Management"
│   │       └── Process: "Vendor Onboarding & Compliance"
│   ├── Domain: "Operations & Delivery" → project & service delivery
│   └── Strategy: "ACME Digital Platform Strategy"
│
├── OU: ACME Corp Group Functions (type: division)
│   ├── Domain: "Finance" (shared — group-wide)
│   ├── Domain: "Risk, Legal & Compliance" (shared — group governance)
│   └── Domain: "People & Talent" (shared — group HR)
│
└── Strategy: "ACME Corp Group Strategy 2026–2030" (scoped to top-level OU, inherited by all children)
```

**Rules governing Organisational Units and multi-instantiation:**

1. **Every object is scoped to an Organisational Unit** via the `scoped_to` relationship. Objects at a parent OU are visible to all child OUs (inheritance). Objects at a child OU are private to that unit by default.
2. **Each OU may adopt a different Industry Edition.** ACME Health runs "ZORBA for Healthcare" while ACME Digital runs "ZORBA for Technology Service Providers" — both within the same group.
3. **Domains instantiate per OU.** ACME Health's "Supply Chain" and ACME Digital's "Supply Chain" are separate domain trees with entirely different capabilities, processes, and workforce compositions.
4. **Shared objects** (group strategy, group finance) are scoped to a parent OU and referenced by all children. They exist once.
5. **No forced symmetry.** ACME Health may decompose "Supply Chain" into 15 capabilities while ACME Digital uses 3. The model does not require structural parity across OUs.
6. **Cross-OU references** are permitted — a shared group capability (e.g., "Group Procurement") may be consumed by processes in multiple child OUs.
7. **OU types are flexible.** The `unit_type` attribute accepts standard values (holding_company, subsidiary, business_unit, brand, division, region, department) but also `custom` for anything else. The hierarchy is not prescriptive — a flat company might have one OU; a multinational might have dozens nested 5+ levels deep.

### Shared vs. Owned

| Pattern | Description | Example |
|---------|-------------|---------|
| **Shared** | Object exists once, referenced by multiple consumers | Corporate strategy, group-wide compliance process |
| **Owned** | Object is scoped to a single owner (LOB, team, domain) | LOB-specific sales process, team-level objective |
| **Federated** | Object is defined centrally but instantiated locally with permitted variation | Standard procurement process with LOB-specific variations |

### Framework Overlay

Multiple frameworks may coexist in the same object graph. This enables organisations to maintain their existing taxonomy while adopting ZORBA.

**Example: APQC/PCF overlay on ZORBA**

| APQC PCF Category | ZORBA Domain Equivalent | Mapping Type |
|-------------------|------------------------|--------------|
| 1.0 Develop Vision & Strategy | Strategy & Governance | Direct |
| 2.0 Develop & Manage Products & Services | Product & Innovation | Direct |
| 3.0 Market & Sell Products & Services | Marketing + Sales | Split |
| 4.0 Deliver Products & Services | Operations & Delivery + Supply Chain | Split |
| 5.0 Manage Customer Service | Customer Success & Service | Direct |
| 6.0 Develop & Manage Human Capital | People & Talent | Direct |
| 7.0 Manage Information Technology | Technology & Data | Direct |
| 8.0 Manage Financial Resources | Finance | Direct |
| 9.0 Acquire, Construct & Manage Assets | Corporate Services (partial) | Partial |
| 10.0 Manage EHS | Risk, Legal & Compliance (partial) | Partial |
| 11.0 Manage External Relationships | Strategy & Governance (partial) | Partial |
| 12.0 Develop & Manage Business Capabilities | Cross-cutting | Distributed |
| 13.0 Manage Knowledge, Improvement & Change | Cross-cutting | Distributed |

To implement a dual-framework overlay:

1. Create two `Framework` objects: "ZORBA v1" and "APQC PCF v7.3".
2. Create `Domain` objects for each framework's top-level categories.
3. Use `belongs_to` relationships to classify capabilities, processes, and activities under both frameworks simultaneously.
4. A single `Process` object (e.g., "Procure-to-Pay") can belong to ZORBA's "Supply Chain" domain AND APQC's "4.0 Deliver Products & Services" — the model supports N:M classification.

---

## Traversal Patterns

The information model is designed for both human exploration and programmatic agent traversal. Below are common query patterns expressed as graph traversals.

### Strategic Alignment Queries

**"Show me all objectives connected to this capability."**
```
Capability --(decomposes_into)--> Process
Process --(aligns_to)--> Objective  [via Initiative or directly]
  OR
Capability --(aligns_to)--> Objective  [direct link if established]
```

**"Trace this work item back to strategic intent."**
```
Work Item --(instantiates)--> Activity
Activity --(part of)--> Process
Process --(aligns_to | decomposes_into⁻¹)--> Capability
Capability --(aligns_to)--> Objective
Objective --(aligns_to)--> Strategy
```

### Workforce Composition Queries

**"What agents are operating in this process?"**
```
Process --(decomposes_into)--> Activity
Activity <--(performs)-- Agent
```

**"What's the workforce composition (human vs. agent) for this domain?"**
```
Domain --(decomposes_into)--> Capability --(decomposes_into)--> Process --(decomposes_into)--> Activity
Aggregate: Activity.performer_type counts → {human-only: N, agent-capable: N, agent-preferred: N, agent-only: N}
```

### Ownership Queries

**"What processes does this team own?"**
```
Team --(owns)--> Process [direct]
  OR
Team --(owns)--> Capability --(decomposes_into)--> Process [inherited]
```

**"Who is accountable for this domain?"**
```
Domain <--(owns)-- Team
Team <--(fills)-- Role [where authority_level = 'accountable']
```

### Impact Analysis Queries

**"If this capability is deprecated, what is affected?"**
```
Capability --(decomposes_into)--> Process --> Activity --> Work Item
Capability <--(depends_on)-- other Capabilities/Processes
Capability <--(measures)-- Metric
Capability <--(aligns_to)-- Objective
```

### Evolution and Workforce Queries

**"Show me all genesis-stage capabilities that need human-heavy workforce."**
```
Capability [evolution_stage = "genesis"] --> filter by pst_phase = "pioneer"
```

**"What capabilities are evolving toward commodity and can shift to agent-heavy workforce?"**
```
Capability [evolution_target = "commodity"] --> check current workforce_composition
Capability --(evolves_to)--> Future Capability [evolution_stage = "commodity"]
```

**"Map all pioneer capabilities and their current workforce composition."**
```
Capability [pst_phase = "pioneer"] --> get workforce_composition + target_composition
Capability --(decomposes_into)--> Process [pst_phase = "pioneer"]
Process --(performs)--> Team [team_type] + Agent
```

**"Find wardley maps that visualise this domain's evolution."**
```
Domain <--(maps)-- WardleyMap --> extract owm_source + evolution_context
```

---

## Extensibility

The information model is a **recommended starting set**, not a closed schema.

### Custom Object Types

Organisations may define additional object types that participate in the same graph. Common extensions:

| Custom Type | Description | Example |
|-------------|-------------|---------|
| **Application** | A software system that supports capabilities or processes | "SAP S/4HANA", "Salesforce" |
| **Data Entity** | A business data object managed within processes | "Customer Record", "Invoice" |
| **Policy** | A governance document that constrains how work is performed | "Data Retention Policy" |
| **Risk** | An identified risk attached to objectives or processes | "Supplier Concentration Risk" |
| **Location** | A physical or virtual place where work is performed | "London HQ", "AWS eu-west-1" |

Custom types inherit all base attributes and participate in relationships using the standard edge types plus any custom relationship types.

### Custom Relationship Types

Define new edge types using the same schema as built-in relationships:

```json
{
  "type": "supports",
  "description": "An application supports a process",
  "source_types": ["Application"],
  "target_types": ["Process", "Activity"],
  "cardinality": "N:M",
  "required": false
}
```

### Custom Attributes

The `metadata` map on every object and relationship is the primary extension point. For structured extensions, organisations may define **attribute schemas** — named sets of key-value pairs with type constraints — and register them against object types.

### Tagging and Metadata Conventions

Tags and metadata enable cross-cutting classification without modifying the core schema:

| Convention | Example | Purpose |
|------------|---------|---------|
| `lob:<name>` tag | `lob:retail` | Line-of-business scoping |
| `region:<code>` tag | `region:emea` | Geographic scoping |
| `maturity:<level>` tag | `maturity:optimised` | Maturity classification |
| `sensitivity:<level>` metadata | `sensitivity:confidential` | Information classification |
| `review_cycle` metadata | `review_cycle:quarterly` | Governance cadence |

---

## Example Instantiations

### Example 1: Small Company (50 People)

**Scenario:** A SaaS startup with one product, one market, and a flat organisational structure.

```
Framework: "ZORBA v1" (lite)
├── Domain: "Strategy"
│   ├── Strategy: "2026 Growth Plan"
│   └── Objective: "Reach £5M ARR by Q4"
│       └── Initiative: "Enterprise Sales Push"
├── Domain: "Product"
│   ├── Capability: "Product Development"
│   │   └── Process: "Feature Delivery"
│   │       ├── Activity: "Requirements Analysis" [agent-capable]
│   │       ├── Activity: "Development" [human-only]
│   │       ├── Activity: "Code Review" [blended]
│   │       └── Activity: "Testing" [agent-preferred]
│   └── Capability: "Product Support"
│       └── Process: "Bug Triage"
├── Domain: "Revenue" (combines Sales + Marketing + CS)
│   ├── Capability: "Demand Generation"
│   └── Capability: "Customer Onboarding"
├── Domain: "Operations" (combines Finance + People + Corp Services)
│   ├── Capability: "Financial Management"
│   └── Capability: "Hiring"
└── Team: "Engineering"
    ├── Role: "Senior Developer" (×8 humans)
    ├── Role: "QA Agent" (×2 agents)
    └── Agent: "CodeReview-Bot" → fills "Code Reviewer" role
```

**Key observations:**
- Only 4 domains (not 12) — ZORBA's taxonomy is compressed to fit the reality
- Domains are renamed to match the company's language ("Revenue" not "Sales + Marketing")
- Agent presence is minimal but explicit
- The model is sparse — many optional object types are unused

### Example 2: Multi-LOB Enterprise

**Scenario:** A financial services group with three lines of business (Retail Banking, Wealth Management, Insurance) and shared corporate functions.

```
Framework: "ZORBA v1"
├── [Shared] Domain: "Strategy & Governance"
│   ├── Strategy: "Group 5-Year Plan"
│   ├── Objective: "Group ROE >15%"
│   └── Team: "Group Executive Committee"
├── [Shared] Domain: "Finance"
│   ├── Capability: "Group Financial Reporting"
│   └── Capability: "Regulatory Capital Management"
├── [Shared] Domain: "Risk, Legal & Compliance"
│   ├── Capability: "Group Risk Oversight"
│   └── Capability: "AI Governance & Agent Compliance"
│
├── [LOB: Retail Banking] Domain: "Customer Success & Service"
│   ├── Capability: "Retail Customer Support"
│   │   └── Process: "Complaint Resolution"
│   │       ├── Activity: "Classify Complaint" [agent-only, A4]
│   │       ├── Activity: "Attempt Auto-Resolution" [agent-preferred, A3]
│   │       └── Activity: "Complex Resolution" [human-only, A0]
│   └── Team: "Retail Service" (200 humans, 45 agents)
│
├── [LOB: Wealth Management] Domain: "Customer Success & Service"
│   ├── Capability: "HNW Client Advisory"
│   │   └── Process: "Portfolio Review"
│   └── Team: "Wealth Advisory" (50 humans, 8 agents)
│
├── [LOB: Insurance] Domain: "Operations & Delivery"
│   ├── Capability: "Claims Processing"
│   │   └── Process: "Motor Claims End-to-End"
│   └── Team: "Claims Operations" (300 humans, 120 agents)
│
└── [Shared] Domain: "Technology & Data"
    ├── Capability: "Agent Platform Management"
    └── Team: "Platform Engineering" (40 humans, 15 agents)
```

**Key observations:**
- "Customer Success & Service" is instantiated separately for Retail Banking and Wealth Management — same domain name, different decomposition
- Corporate functions (Strategy, Finance, Risk, Technology) are shared
- Agent density varies dramatically by LOB — Insurance Claims is 29% agent, Wealth Advisory is 14%
- The model accommodates this without structural distortion

### Example 3: APQC/PCF Mapping

**Scenario:** An organisation already using APQC/PCF that wants to add ZORBA's workforce composition layer.

```
Framework: "APQC PCF v7.3"
├── Domain: "1.0 Develop Vision & Strategy"
│   └── Capability: "1.1 Define Business Concept & Strategy"
│       └── Process: "1.1.1 Assess the External Environment"
│           └── Activity: "1.1.1.1 Analyse market trends" [agent-preferred, A3]
│
Framework: "ZORBA v1" (overlay)
├── Domain: "Strategy & Governance"
│   └── [links to same Capability: "1.1 Define Business Concept & Strategy"]
│   └── [links to same Process: "1.1.1 Assess the External Environment"]

Shared objects:
  Capability "1.1 Define Business Concept & Strategy"
    belongs_to → "APQC PCF v7.3" / "1.0 Develop Vision & Strategy"
    belongs_to → "ZORBA v1" / "Strategy & Governance"
```

The same capability, process, and activity objects are classified under **both** frameworks simultaneously. APQC provides the process taxonomy; ZORBA adds the workforce composition, agent governance, and blended workforce metadata that APQC does not address.

---

## Implementation Notes

### Serialisation

The information model is serialisation-agnostic. Recommended formats:

- **JSON/JSON-LD** for API interchange and agent consumption
- **YAML** for human-authored configuration
- **Graph database** (property graph or RDF) for large-scale traversal
- **Relational** with junction tables for relationship N:M cardinality

### Agent Discoverability

For agents to traverse the business object graph effectively (see [Architecture](02-architecture.md), "Architecture as Operating System"):

1. Every object must be addressable by `id`.
2. Relationships must be queryable by `source_id`, `target_id`, and `type`.
3. The graph must support reverse traversal — given a target, find all sources.
4. Bulk queries (e.g., "all objects of type Activity where performer_type = agent-preferred") must be efficient.
5. Schema introspection — agents must be able to discover available object types, relationship types, and attribute schemas at runtime.

### Versioning

Objects carry `created_at` and `updated_at` timestamps. For full change history, implementations should maintain an **event log** or **version history** per object. Framework-level versioning (e.g., "ZORBA v1" → "ZORBA v2") is managed via the Framework object's `version` attribute.

---

*Previous: [← Glossary](13-glossary.md)*

---

*© 2026 Zontally. All rights reserved.*
