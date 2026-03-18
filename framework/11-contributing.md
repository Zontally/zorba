# Contributing to ZORBA

*ZORBA is an open reference architecture. It gets better when more people shape it.*

---

## Why Contribute?

ZORBA aims to be the definitive reference architecture for the agentic enterprise — but no single organisation can map every industry, every edge case, or every emerging pattern of human-agent collaboration. We need practitioners, platform builders, and domain experts to challenge, extend, and refine it.

Every contribution — from fixing a typo to proposing an entirely new Industry Edition — makes the framework more useful for everyone.

---

## Ways to Contribute

### 🐛 Report an Issue

Found something wrong? A process that's misclassified, an agentic profile that feels off, a gap in coverage?

1. Go to [GitHub Issues](https://github.com/Zontally/zorba/issues)
2. Check if someone's already raised it
3. Open a new issue with a clear description

Good issues include:
- **Bug reports** — incorrect data, broken links, schema validation failures
- **Gap analysis** — "Domain X is missing a capability for Y"
- **Agentic profile challenges** — "Process Z should be H=A, not h+A, because..."
- **Terminology feedback** — "This name is confusing in the context of industry X"

Don't worry about format. Clear beats formal.

### 💡 Propose a Change

Have an idea for improving the taxonomy, adding a capability, or restructuring a domain?

1. Open a [GitHub Issue](https://github.com/Zontally/zorba/issues) describing your proposal
2. Tag it as `enhancement` or `discussion`
3. The community and maintainers will discuss it

We'd rather have ten rough ideas than one perfect proposal. Start the conversation.

### 🔧 Submit a Pull Request

Ready to make the change yourself? Brilliant.

**Step 1: Fork the repository**

```bash
git clone https://github.com/Zontally/zorba.git
cd zorba
```

**Step 2: Create a branch**

```bash
git checkout -b your-branch-name
```

Use descriptive branch names: `fix/finance-process-profile`, `feat/healthcare-edition`, `docs/governance-clarity`.

**Step 3: Make your changes**

- Edit YAML source files in `core/domains/`
- Edit framework documents in `framework/`
- Add new Industry Edition files in `editions/`

**Step 4: Validate and build**

```bash
npm install
npm run build
```

This validates your YAML, compiles JSON, and generates documentation. Fix any errors before committing.

**Step 5: Commit and push**

```bash
git add -A
git commit -m "Brief description of your change"
git push origin your-branch-name
```

**Step 6: Open a Pull Request**

Go to [github.com/Zontally/zorba](https://github.com/Zontally/zorba) and open a PR against `main`. Describe what you changed and why.

### 🌍 Build an Industry Edition

This is the most impactful contribution you can make. ZORBA's core is industry-agnostic — but real organisations operate in specific verticals. Industry Editions tailor the taxonomy for sectors like healthcare, financial services, manufacturing, or government.

See [Industry Editions](08-industry-editions.md) for the full specification. In short:

1. Start from the core taxonomy
2. Add sector-specific capabilities and processes
3. Adjust agentic profiles for your industry's regulatory and operational context
4. Document the rationale

If you're building an edition, open an issue first so we can coordinate and avoid duplicated effort.

### 📝 Improve Documentation

Documentation contributions are just as valuable as taxonomy changes. If something's unclear, fix it. If an example would help, add one. The framework documents in `framework/` are hand-written markdown — edit them directly.

---

## Contribution Guidelines

### YAML Source Files

- **Use unique 6-digit IDs** (100000–999999) for any new domain, capability, or process
- **Check for ID collisions** across the entire taxonomy before committing
- **Follow the existing structure** — look at other domain files for the pattern
- **Include agentic profiles and notes** for every process
- **Write descriptions** that explain the *why*, not just the *what*

### Commit Messages

Keep them concise and descriptive:

```
feat: add regulatory reporting processes to finance domain
fix: correct agentic profile for incident response (H=A → H+a)
docs: clarify workforce model terminology
edition: initial healthcare edition — clinical operations domain
```

### Pull Request Etiquette

- **One concern per PR** — don't bundle unrelated changes
- **Describe the reasoning** — *why* you're making the change matters more than *what*
- **Be open to feedback** — the taxonomy reflects collective judgement
- **Reference issues** — link to the GitHub issue if one exists

---

## What We're Looking For

### High-Priority Contributions

- **Industry Editions** — especially healthcare, financial services, manufacturing, government, and education
- **Agentic profile validation** — real-world data on how human-agent work is actually distributed
- **Gap analysis** — capabilities or processes that are missing from the core
- **Internationalisation** — how ZORBA terminology maps to non-English business contexts
- **Integration examples** — how you've embedded ZORBA in your platform or tooling

### Always Welcome

- Typo fixes and clarity improvements
- Better examples and use cases
- Schema improvements
- Build tooling enhancements
- Accessibility improvements to the documentation site

---

## Community

ZORBA is maintained by [Zontally](https://zontally.com) and shaped by its community.

- **GitHub Discussions** — [github.com/Zontally/zorba/discussions](https://github.com/Zontally/zorba/discussions) for open conversation
- **Issues** — [github.com/Zontally/zorba/issues](https://github.com/Zontally/zorba/issues) for bugs and proposals
- **Pull Requests** — [github.com/Zontally/zorba/pulls](https://github.com/Zontally/zorba/pulls) for contributions

We don't have a mailing list or Slack yet. If demand grows, we'll set something up. For now, GitHub is home.

---

## Code of Conduct

Be respectful. Be constructive. Assume good intent. This is a professional community building something useful — act accordingly.

Harassment, discrimination, and bad-faith contributions are not tolerated.

---

## Licence

ZORBA is published under a licence that permits use, modification, and redistribution. See the [LICENSE](https://github.com/Zontally/zorba/blob/main/LICENSE) file in the repository for full terms.

By contributing, you agree that your contributions will be published under the same licence.

---

*© 2026 Zontally. All rights reserved.*
