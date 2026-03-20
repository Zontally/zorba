# Industry Taxonomy

## Overview

ZORBA's **Industry Taxonomy** provides a structured, machine-readable classification of industries, sub-industries, business models, value drivers, and operational signals. It serves as the foundational reference data that powers industry-aware features across the Zontally platform — from [Industry Editions](08-industry-editions.md) and benchmarking to AI-guided strategy-to-execution workflows.

The taxonomy answers a deceptively simple question: **What kind of organisation is this, and what does that imply about how it operates?**

Every enterprise exists within an industry context. That context shapes which business models are viable, which capabilities matter most, how complex the supply chain is, how heavily regulated the operating environment is, and where agentic augmentation delivers the most leverage. The Industry Taxonomy captures these structural realities as data.

---

## Taxonomy Structure

The taxonomy is a two-level hierarchy:

```
Industry
└── Sub-Industry
```

Each level carries a consistent set of attributes that describe the operational character of organisations within that segment.

### Industries

Industries represent broad sectors of economic activity. ZORBA defines **15 industries** covering the full spectrum of enterprise types:

| # | Industry | Slug |
|---|----------|------|
| 1 | Technology & Software | `technology-software` |
| 2 | Financial Services | `financial-services` |
| 3 | Healthcare & Life Sciences | `healthcare-life-sciences` |
| 4 | Manufacturing & Industrial | `manufacturing-industrial` |
| 5 | Retail & Consumer Goods | `retail-consumer-goods` |
| 6 | Energy & Utilities | `energy-utilities` |
| 7 | Telecommunications & Media | `telecommunications-media` |
| 8 | Transportation & Logistics | `transportation-logistics` |
| 9 | Public Sector & Government | `public-sector-government` |
| 10 | Education & Non-Profit | `education-nonprofit` |
| 11 | Real Estate & Construction | `real-estate-construction` |
| 12 | Hospitality, Travel & Leisure | `hospitality-travel-leisure` |
| 13 | Professional Services | `professional-services` |
| 14 | Agriculture & Food Production | `agriculture-food-production` |
| 15 | Mining & Natural Resources | `mining-natural-resources` |

Each industry includes:

- **Definition** — a clear, concise description of the sector
- **Aliases** — alternative names used in common parlance
- **Common business models** — the revenue and delivery models typical across the sector
- **Common value drivers** — the metrics and outcomes that matter most
- **Common capabilities** — the organisational capabilities that define competitive advantage
- **Tags** — lightweight labels for filtering and grouping
- **Signals** — a structured profile of operational characteristics (see below)

### Sub-Industries

Sub-industries represent distinct segments within a broader industry. For example, *Technology & Software* contains 8 sub-industries including Enterprise Software, Vertical SaaS, Cloud Infrastructure, and Cybersecurity.

ZORBA currently defines **88 sub-industries** across the 15 industries.

Sub-industries carry a similar attribute set to industries, but more specific:

- **Definition** — what makes this segment distinct
- **Business models** — the specific models prevalent in this segment
- **Value drivers** — the KPIs and outcomes that define success
- **Typical capabilities** — the organisational capabilities most critical to compete
- **Customer types** — who the organisations in this segment typically serve (e.g. Consumer, SMB, Enterprise, Government)
- **Tags** — segment-specific labels
- **Signals** — operational profile, potentially diverging from the parent industry

---

## Signals

Signals are a structured set of ten dimensions that characterise the operational reality of an industry or sub-industry. Each signal is rated on a five-point scale: `very-low`, `low`, `medium`, `high`, `very-high`.

| Signal | What It Captures |
|--------|-----------------|
| **digitalIntensity** | How central digital technology is to the core operating model |
| **regulatoryIntensity** | The burden and complexity of regulatory and compliance requirements |
| **operationalComplexity** | The inherent complexity of day-to-day operations |
| **assetIntensity** | The degree to which the business depends on physical assets and capital investment |
| **peopleIntensity** | How dependent the operating model is on human labour and expertise |
| **customerComplexity** | The complexity of customer relationships, segmentation, and buying behaviour |
| **salesComplexity** | The complexity of the sales motion (cycle length, stakeholders, deal structure) |
| **serviceIntensity** | How central ongoing service delivery is to the value proposition |
| **supplyChainComplexity** | The complexity of sourcing, logistics, and supply chain management |
| **innovationIntensity** | The pace and importance of product/service innovation to competitive position |

### How Signals Are Used

Signals are not decorative metadata — they drive platform behaviour:

- **Edition selection** — signals help match an organisation to the most appropriate Industry Edition
- **Capability prioritisation** — high `regulatoryIntensity` elevates Risk, Legal & Compliance capabilities; high `peopleIntensity` elevates People & Talent
- **Agentic profile recommendations** — industries with high `digitalIntensity` and `innovationIntensity` tend toward more autonomous agentic patterns; heavily regulated industries skew toward human-led patterns
- **Benchmarking** — signals provide a structured basis for comparing organisations within and across segments
- **AI-guided workflows** — the Zontally platform uses signals to contextualise recommendations, generate industry-appropriate templates, and calibrate default configurations

### Signal Inheritance

Sub-industries inherit the signal profile of their parent industry as a baseline, but may override individual signals where the segment diverges. For example:

- **Technology & Software** has `supplyChainComplexity: low`
- **Cloud Infrastructure** (a sub-industry) keeps this as `low`
- But a future **Hardware Technology** sub-industry might override to `high`

This inheritance model keeps the taxonomy maintainable while allowing precise characterisation at the segment level.

---

## Source Format

The industry taxonomy is maintained as YAML source files in the `industries/` directory:

```
industries/
├── model.yaml                        # Model metadata (version, status)
├── technology-software.yaml          # One file per industry
├── financial-services.yaml
├── healthcare-life-sciences.yaml
├── manufacturing-industrial.yaml
├── retail-consumer-goods.yaml
├── energy-utilities.yaml
├── telecommunications-media.yaml
├── transportation-logistics.yaml
├── public-sector-government.yaml
├── education-nonprofit.yaml
├── real-estate-construction.yaml
├── hospitality-travel-leisure.yaml
├── agriculture-food-production.yaml
└── mining-natural-resources.yaml
```

### Industry File Structure

Each industry file follows this structure:

```yaml
industry:
  id: "ind_technology_software"
  name: "Technology & Software"
  slug: "technology-software"
  definition: "Organisations that create, deliver, or enable digital products, platforms, and infrastructure."
  status: "active"
  aliases: ["Technology", "Software", "Tech"]
  commonBusinessModels: ["SaaS", "Subscription", "Usage-based", "Platform", "Licensing"]
  commonValueDrivers: ["Growth", "Retention", "Productivity", "Platform adoption", "Innovation speed"]
  commonCapabilities: ["Product management", "Engineering", "Customer support", "Revenue operations", "Security"]
  tags: ["digital", "cloud", "platform"]
  signals:
    digitalIntensity: "very-high"
    regulatoryIntensity: "medium"
    # ... all 10 signals

  subIndustries:
    - id: "subind_enterprise_software"
      name: "Enterprise Software"
      slug: "enterprise-software"
      definition: "Software companies serving business customers..."
      status: "active"
      businessModels: ["SaaS", "Subscription", "Licensing"]
      valueDrivers: ["ARR growth", "Net retention", "Adoption", "Time to value"]
      typicalCapabilities: ["Sales", "Customer success", "Support", "Product", "Engineering"]
      customerTypes: ["SMB", "Mid-market", "Enterprise"]
      tags: ["b2b", "applications"]
      signals:
        digitalIntensity: "very-high"
        # ... all 10 signals
```

### ID Conventions

- Industry IDs use the prefix `ind_` (e.g. `ind_financial_services`)
- Sub-industry IDs use the prefix `subind_` (e.g. `subind_enterprise_software`)
- IDs must be globally unique across the entire taxonomy

---

## Build Pipeline

The industry taxonomy is compiled as part of the standard ZORBA build:

```bash
# Compile industry model only
npm run compile:industries

# Full build (includes industry compilation)
npm run build
```

The compiler (`build/compile-industries.js`):

1. Reads `industries/model.yaml` for metadata
2. Reads all `industries/<slug>.yaml` files
3. Validates required fields and unique IDs
4. Outputs `dist/zorba-industries.json`

The compiled JSON is the distribution format consumed by the Zontally platform and any downstream tooling.

---

## Relationship to Industry Editions

The Industry Taxonomy and [Industry Editions](08-industry-editions.md) are complementary but distinct:

| Aspect | Industry Taxonomy | Industry Edition |
|--------|------------------|-----------------|
| **What it is** | Classification and signal data | Customised ZORBA domain model |
| **Granularity** | Industry → Sub-industry | One edition per sub-industry (or industry) |
| **Content** | Business models, value drivers, signals | Overridden domains, capabilities, processes |
| **Format** | `industries/<slug>.yaml` → `dist/zorba-industries.json` | `editions/<name>/` → `dist/zorba-<name>.json` |
| **Purpose** | Describe *what kind* of organisation | Describe *how* it should be structured in ZORBA |

The taxonomy tells you that Enterprise Software companies typically have very high sales complexity and digital intensity. The Enterprise Software *edition* translates that knowledge into concrete domain, capability, and process definitions — renaming "Product/Service & Innovation" to "Product & Innovation", sharpening process names to use software-specific terminology, and so on.

In the Zontally platform, an organisation's **industry and sub-industry selection** drives which edition is recommended, and the **signals** calibrate default configurations within that edition.

---

## Extending the Taxonomy

### Adding a Sub-Industry

To add a new sub-industry, edit the relevant industry YAML file and add an entry to the `subIndustries` list. Ensure:

- The `id` is globally unique (use the `subind_` prefix)
- All required fields are populated (`id`, `name`, `slug`, `definition`, `status`)
- All 10 signals are specified
- Run `npm run compile:industries` to validate

### Adding an Industry

To add a new top-level industry:

1. Create a new file `industries/<slug>.yaml`
2. Follow the standard industry file structure
3. Use the `ind_` prefix for the ID
4. Include all required fields and at least one sub-industry
5. Run `npm run compile:industries` to validate and compile

### Status Values

Industries and sub-industries support a `status` field:

- `active` — included in compiled output and available in the platform
- `draft` — work in progress, included in output but flagged
- `deprecated` — scheduled for removal, included with deprecation notice

---

## Current Coverage

The v1.0 taxonomy covers **15 industries** and **88 sub-industries**, spanning:

- Digital-native sectors (Technology, Fintech, Digital Health)
- Heavily regulated sectors (Financial Services, Healthcare, Energy, Public Sector)
- Asset-intensive sectors (Manufacturing, Real Estate, Transportation)
- People-intensive sectors (Professional Services, Education, Hospitality)
- Mission-driven sectors (Non-Profit, Public Health & Education)

This provides sufficient coverage for the majority of enterprise segmentation use cases. The taxonomy is designed to grow incrementally — new sub-industries can be added without disrupting existing ones.

