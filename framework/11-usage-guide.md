# Usage Guide

*How to use ZORBA in practice — whether you're a platform provider, a practitioner, or a contributor.*

---

## Who Is ZORBA For?

ZORBA is designed for three audiences:

1. **Platform providers** — embed ZORBA's taxonomy into your product as a reference data model
2. **Practitioners** — fork the repo, tailor the taxonomy to your organisation, and generate your own documentation
3. **Contributors** — extend ZORBA with new Industry Editions or improve the core

Each path starts with the same source: human-readable YAML files that compile into machine-readable JSON and generate documentation.

---

## The Source Format

ZORBA's taxonomy lives in YAML files under `core/domains/`. Each file defines one domain with its capabilities and processes:

```yaml
domain:
  id: 738201
  number: 1
  name: "Strategy & Governance"
  subtitle: "Setting direction and ensuring accountability"
  classification: management_function
  description: |
    This domain encompasses the enterprise's ability to define
    its purpose, set strategic direction, and govern operations.

  capabilities:
    - id: 482910
      number: 1.1
      name: "Define Strategic Direction"
      description: |
        Establishing the organisation's long-term intent...

      processes:
        - id: 193847
          number: 1.1.1
          name: "Develop Enterprise Vision & Mission"
          agentic_profile: "H+a"
          agentic_note: "Fundamentally human; agents support research and benchmarking"
```

Every domain, capability, and process carries a **unique 6-digit ID** that remains stable even when names or numbering change. This is what platform providers should reference.

---

## For Platform Providers

### Embedding ZORBA in Your Product

ZORBA provides a ready-made taxonomy for any platform that needs to model business operations — workforce management, process mining, GRC, ERP configuration, or agentic orchestration.

**Step 1: Use the compiled JSON**

Run the build to produce `dist/zorba-core.json`:

```bash
npm install
npm run compile
```

This gives you a single JSON file containing the full taxonomy — domains, capabilities, processes, agentic profiles, and all metadata. Use this as reference data in your application.

**Step 2: Reference by ID, not by name**

Always reference ZORBA objects by their 6-digit ID. Names and descriptions may evolve across versions; IDs are immutable.

```json
{
  "process_ref": 193847,
  "framework": "zorba-core",
  "version": "0.1.0"
}
```

**Step 3: Stay current**

Pin to a specific ZORBA version in your product. When a new version is released, review the changelog and update your mappings. Semantic versioning tells you what changed:

- **Patch** (0.1.1) — descriptions, typos, agentic notes
- **Minor** (0.2.0) — new processes or capabilities added
- **Major** (1.0.0) — breaking changes to structure or IDs

**Step 4: Extend with Industry Editions**

If the core taxonomy doesn't cover your vertical, use or create an [Industry Edition](08-industry-editions.md). Editions extend the core with sector-specific domains, capabilities, and processes whilst keeping the universal management functions intact.

### API Integration Pattern

```javascript
const zorba = require('./dist/zorba-core.json');

// Look up a process by ID
const process = zorba.domains
  .flatMap(d => d.capabilities)
  .flatMap(c => c.processes)
  .find(p => p.id === 193847);

console.log(process.name);            // "Develop Enterprise Vision & Mission"
console.log(process.agentic_profile); // "H+a"
```

---

## For Practitioners

### Tailoring ZORBA to Your Organisation

ZORBA is a reference — a starting point, not a straitjacket. Every organisation is different. Fork the repo and make it yours.

**Step 1: Fork the repository**

```bash
git clone https://github.com/Zontally/zorba.git my-org-taxonomy
cd my-org-taxonomy
```

**Step 2: Edit the YAML**

Modify `core/domains/*.yaml` to reflect your organisation:

- **Rename processes** to match your internal language
- **Remove processes** that don't apply to you
- **Add processes** specific to your operations
- **Adjust agentic profiles** to reflect your actual human/agent workforce mix
- **Update descriptions** with your context

When adding new processes, generate a random 6-digit ID (100000–999999) and ensure it's unique across your taxonomy.

**Step 3: Build your taxonomy**

```bash
npm install
npm run build
```

This runs three steps:
1. **Validate** — checks your YAML against the schema
2. **Compile** — produces `dist/zorba-core.json` with your customisations
3. **Generate** — creates markdown documentation from your YAML

**Step 4: Serve your documentation**

```bash
pip install mkdocs-material
python3 -m mkdocs serve
```

Your organisation now has a browsable, searchable taxonomy at `http://127.0.0.1:8000` — generated directly from your YAML source of truth.

**Step 5: Keep it alive**

Commit your changes. Review quarterly. As your organisation evolves — new capabilities, shifting automation levels, restructured domains — update the YAML and rebuild. The taxonomy should reflect reality, not aspiration.

### Example: Customising a Process

Suppose your organisation has fully automated invoice processing. Update the agentic profile:

```yaml
# Before (ZORBA default)
- id: 847291
  number: 8.3.2
  name: "Process Incoming Invoices"
  agentic_profile: "H=A"
  agentic_note: "Balanced — agents handle matching and routing, humans review exceptions"

# After (your organisation)
- id: 847291
  number: 8.3.2
  name: "Process Incoming Invoices"
  agentic_profile: "A"
  agentic_note: "Fully automated via AP platform — human review only for flagged exceptions over £10k"
```

### Example: Adding an Organisation-Specific Process

```yaml
- id: 550123
  number: 6.4.5
  name: "Manage Partner SLA Compliance"
  agentic_profile: "h+A"
  agentic_note: "Agent monitors SLA metrics continuously; humans intervene on breach escalation"
```

---

## The Build System

### Commands

| Command | What It Does |
|---------|-------------|
| `npm run validate` | Checks all YAML files against the ZORBA schema |
| `npm run compile` | Compiles YAML into `dist/zorba-core.json` |
| `npm run generate` | Generates markdown documentation in `docs/` |
| `npm run build` | Runs all three in sequence |

### Directory Structure

```
zorba/
├── core/
│   ├── domains/          # YAML source files (one per domain)
│   └── schema/           # JSON Schema for validation
├── editions/             # Industry Edition overrides
├── build/
│   ├── validate.js       # Schema validation
│   ├── compile.js        # YAML → JSON compiler
│   └── generate-docs.js  # YAML → Markdown generator
├── framework/            # Hand-written framework documents
├── dist/                 # Compiled output (generated)
├── docs/                 # Documentation site (generated)
├── static/               # Static assets (logos, images)
└── mkdocs.yml            # MkDocs configuration
```

### What's Source, What's Generated?

| Directory | Source or Generated? | Edit directly? |
|-----------|---------------------|----------------|
| `core/` | Source | ✅ Yes — this is your source of truth |
| `framework/` | Source | ✅ Yes — hand-written prose documents |
| `static/` | Source | ✅ Yes — logos and static assets |
| `dist/` | Generated | ❌ No — rebuilt by `compile` |
| `docs/` | Generated | ❌ No — rebuilt by `generate` |

---

## Agentic Profiles

Every process in ZORBA carries an agentic profile — a recommendation for how human and agent work should be balanced:

| Code | Meaning | Example |
|------|---------|---------|
| **H** | Human-only — agent participation not appropriate | Crisis leadership, board governance |
| **H+a** | Human-led with light agent support | Strategy development, creative direction |
| **H=A** | Balanced human-agent collaboration | Financial planning, campaign management |
| **h+A** | Agent-led with human oversight | Invoice processing, log analysis |
| **A** | Agent-autonomous within defined boundaries | Data backup, system monitoring |

These are starting points. Your organisation's actual profiles should reflect your maturity, risk appetite, and regulatory context. Update them in the YAML as your workforce model evolves.

---

## Staying Connected to Upstream

If you've forked ZORBA, you can pull improvements from the upstream repository:

```bash
git remote add upstream https://github.com/Zontally/zorba.git
git fetch upstream
git merge upstream/main
```

Resolve any conflicts in your customised YAML files. Your unique IDs and upstream IDs won't collide if you've used fresh random 6-digit IDs for your additions.

---

## Next Steps

- Read the [Architecture](02-architecture.md) to understand the structural model
- Browse the [Domain Reference](04-domain-reference.md) for an overview of all 12 domains
- Explore the [Domain Taxonomy](../domains/index.md) for detailed process-level data
- Review [Industry Editions](08-industry-editions.md) if you're building for a specific vertical

---

*© 2026 Zontally. All rights reserved.*
