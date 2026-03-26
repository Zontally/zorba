#!/usr/bin/env node

/**
 * ZORBA Documentation Generator — generate-docs.js
 *
 * Generates a single unified MkDocs site containing ZORBA Core, industry
 * taxonomy reference pages (from dist/zorba-industries.json), and all
 * compiled industry editions.
 *
 * Usage:
 *   node build/generate-docs.js              # generate docs (core + all compiled editions)
 *   node build/generate-docs.js --build      # generate docs + run mkdocs build
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '..');
const CORE_DIR = path.join(ROOT, 'core', 'domains');
const DIST_DIR = path.join(ROOT, 'dist');
const DOCS_DIR = path.join(ROOT, 'docs');
const DOCS_DOMAINS_DIR = path.join(DOCS_DIR, 'domains');
const DOCS_FRAMEWORK_DIR = path.join(DOCS_DIR, 'framework');
const EDITIONS_DIR = path.join(ROOT, 'editions');
const FRAMEWORK_DIR = path.join(ROOT, 'framework');
const INDUSTRIES_JSON = path.join(DIST_DIR, 'zorba-industries.json');
const DOCS_INDUSTRY_TAXONOMY_DIR = path.join(DOCS_DIR, 'industry-taxonomy');
const DOCS_INDUSTRIES_DIR = path.join(DOCS_INDUSTRY_TAXONOMY_DIR, 'industries');
const DOCS_SUB_INDUSTRIES_DIR = path.join(DOCS_INDUSTRY_TAXONOMY_DIR, 'sub-industries');

const PROFILE_LEGEND = {
  'H': 'Human-only — agent participation not appropriate',
  'H+a': 'Human-led with light agent support',
  'H=A': 'Balanced human-agent collaboration',
  'h+A': 'Agent-led with human oversight or approval',
  'A': 'Agent-autonomous within defined boundaries'
};

const CLASSIFICATION_LABELS = {
  'value_chain': 'Value Chain',
  'management_function': 'Management Function'
};

function readYaml(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  return yaml.load(content);
}

function slugify(name) {
  return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '').replace(/^-+/, '');
}

function domainFilename(domain) {
  return `${String(domain.number).padStart(2, '0')}-${slugify(domain.name)}.md`;
}

function copyRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) copyRecursive(srcPath, destPath);
    else fs.copyFileSync(srcPath, destPath);
  }
}

// --- Domain doc generation ---

function generateDomainDoc(domain, editionName) {
  const classification = CLASSIFICATION_LABELS[domain.classification] || domain.classification;
  const lines = [];

  lines.push(`# Domain ${domain.number}: ${domain.name} (${domain.id})`);
  lines.push('');
  if (editionName) {
    lines.push(`!!! info "Industry Edition: ${editionName}"`);
    lines.push(`    This is the ${editionName} variant of this domain.`);
    lines.push('');
  }
  lines.push(`*${domain.subtitle}*`);
  lines.push('');
  lines.push(`**Classification:** ${classification}`);
  lines.push('**Version:** v0.1 (Draft)');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Overview');
  lines.push('');
  lines.push(domain.description.trim());
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## ZORBA Hierarchy: Domain → Capability → Process');
  lines.push('');
  lines.push('```');
  lines.push('ZORBA Level    │  APQC Equivalent     │  Description');
  lines.push('───────────────┼──────────────────────┼─────────────────────────────────────');
  lines.push('Domain         │  Category            │  Major area of enterprise activity');
  lines.push('Capability     │  Process Group       │  What the organisation can do');
  lines.push('Process        │  Process             │  How work flows to deliver a capability');
  lines.push('```');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Capabilities & Processes');
  lines.push('');

  for (const cap of (domain.capabilities || [])) {
    lines.push(`### ${cap.number} ${cap.name} (${cap.id})`);
    lines.push('');
    if (cap.description) {
      lines.push(cap.description.trim());
      lines.push('');
    }

    if (cap.processes && cap.processes.length > 0) {
      lines.push('| # | Process | ID | Agentic Profile |');
      lines.push('|---|---------|-----|-----------------|');
      for (const proc of cap.processes) {
        const note = proc.agentic_note || '';
        lines.push(`| ${proc.number} | ${proc.name} | ${proc.id} | ${proc.agentic_profile} — ${note} |`);
      }
    }

    lines.push('');
    lines.push('---');
    lines.push('');
  }

  // Summary table
  lines.push('## Summary');
  lines.push('');
  lines.push('| Capability | ID | Process Count |');
  lines.push('|-----------|-----|---------------|');

  let totalProcesses = 0;
  for (const cap of (domain.capabilities || [])) {
    const procCount = cap.processes ? cap.processes.length : 0;
    totalProcesses += procCount;
    lines.push(`| ${cap.number} ${cap.name} | ${cap.id} | ${procCount} |`);
  }
  lines.push(`| **Total** | | **${totalProcesses} processes** |`);
  lines.push('');
  lines.push('---');
  lines.push('');

  // Agentic profile legend
  lines.push('## Agentic Profile Legend');
  lines.push('');
  lines.push('| Code | Meaning |');
  lines.push('|------|---------|');
  for (const [code, meaning] of Object.entries(PROFILE_LEGEND)) {
    lines.push(`| **${code}** | ${meaning} |`);
  }
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*');
  lines.push('');

  return lines.join('\n');
}

function generateDomainIndex(title, description, domains, filenameFn) {
  const fn = filenameFn || domainFilename;
  const lines = [];
  lines.push(`# ${title}`);
  lines.push('');
  lines.push(description);
  lines.push('');
  lines.push('| # | Domain | Classification | Subtitle |');
  lines.push('|---|--------|---------------|----------|');

  for (const domain of domains) {
    const mdFile = fn(domain);
    const classification = CLASSIFICATION_LABELS[domain.classification] || domain.classification;
    lines.push(`| ${domain.number} | [${domain.name}](${mdFile}) | ${classification} | *${domain.subtitle}* |`);
  }

  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*');
  lines.push('');
  return lines.join('\n');
}

// --- Industry taxonomy (from compiled zorba-industries.json) ---

function escapeTableCell(text) {
  if (text == null || text === '') return '—';
  return String(text).replace(/\|/g, '\\|').replace(/\n/g, ' ');
}

function humanizeSignalKey(key) {
  return key
    .replace(/([a-z])([A-Z])/g, '$1 $2')
    .replace(/_/g, ' ')
    .split(' ')
    .map((w) => w.charAt(0).toUpperCase() + w.slice(1).toLowerCase())
    .join(' ');
}

function signalsMarkdownTable(signals) {
  if (!signals || typeof signals !== 'object') return '';
  const lines = [];
  lines.push('| Dimension | Level |');
  lines.push('|-----------|-------|');
  for (const [k, v] of Object.entries(signals)) {
    lines.push(`| ${escapeTableCell(humanizeSignalKey(k))} | ${escapeTableCell(v)} |`);
  }
  lines.push('');
  return lines.join('\n');
}

function bulletList(items) {
  if (!items || items.length === 0) return '';
  return items.map((x) => `- ${x}`).join('\n') + '\n';
}

function assignSubIndustryFilenames(industries) {
  const slugCount = new Map();
  for (const ind of industries) {
    for (const sub of ind.subIndustries || []) {
      slugCount.set(sub.slug, (slugCount.get(sub.slug) || 0) + 1);
    }
  }
  const filenameBySubId = new Map();
  for (const ind of industries) {
    for (const sub of ind.subIndustries || []) {
      const collision = slugCount.get(sub.slug) > 1;
      const filename = collision ? `${ind.slug}__${sub.slug}.md` : `${sub.slug}.md`;
      filenameBySubId.set(sub.id, filename);
    }
  }
  return filenameBySubId;
}

function generateSubIndustryDoc(sub, industry) {
  const lines = [];
  lines.push(`# ${sub.name}`);
  lines.push('');
  lines.push(`**Sub-industry ID:** \`${sub.id}\`  `);
  lines.push(`**Slug:** \`${sub.slug}\`  `);
  lines.push(`**Status:** ${sub.status || '—'}`);
  lines.push('');
  lines.push(
    `**Parent industry:** [${industry.name}](../industries/${industry.slug}.md)`
  );
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Definition');
  lines.push('');
  lines.push((sub.definition || '').trim());
  lines.push('');

  if (sub.aliases && sub.aliases.length) {
    lines.push('## Aliases');
    lines.push('');
    lines.push(bulletList(sub.aliases));
    lines.push('');
  }

  if (sub.businessModels && sub.businessModels.length) {
    lines.push('## Business models');
    lines.push('');
    lines.push(bulletList(sub.businessModels));
    lines.push('');
  }

  if (sub.valueDrivers && sub.valueDrivers.length) {
    lines.push('## Value drivers');
    lines.push('');
    lines.push(bulletList(sub.valueDrivers));
    lines.push('');
  }

  if (sub.typicalCapabilities && sub.typicalCapabilities.length) {
    lines.push('## Typical capabilities');
    lines.push('');
    lines.push(bulletList(sub.typicalCapabilities));
    lines.push('');
  }

  if (sub.customerTypes && sub.customerTypes.length) {
    lines.push('## Customer types');
    lines.push('');
    lines.push(bulletList(sub.customerTypes));
    lines.push('');
  }

  if (sub.tags && sub.tags.length) {
    lines.push('## Tags');
    lines.push('');
    lines.push(bulletList(sub.tags));
    lines.push('');
  }

  if (sub.signals && Object.keys(sub.signals).length) {
    lines.push('## Intensity signals');
    lines.push('');
    lines.push(signalsMarkdownTable(sub.signals).trimEnd());
    lines.push('');
  }

  lines.push('---');
  lines.push('');
  lines.push(
    '[← Industry taxonomy](../index.md) · ' +
      `[${industry.name}](../industries/${industry.slug}.md)`
  );
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push(
    '*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*'
  );
  lines.push('');
  return lines.join('\n');
}

function truncateSummary(text, maxLen) {
  const t = (text || '').replace(/\s+/g, ' ').trim();
  if (t.length <= maxLen) return t;
  return t.slice(0, maxLen - 1).trim() + '…';
}

function generateIndustryTaxonomyOverviewIndex(data) {
  const lines = [];
  lines.push('# Industry taxonomy');
  lines.push('');
  lines.push(
    `**Model:** \`${data.model || '—'}\` · **Version:** ${data.version || '—'} · **Status:** ${data.status || '—'}`
  );
  lines.push('');
  if (data.description) {
    lines.push(data.description.trim());
    lines.push('');
  }
  if (data.generatedAt) {
    lines.push(`*Compiled: ${data.generatedAt}*`);
    lines.push('');
  }

  lines.push(
    'Each industry has its own page with sector-level signals and traits. Sub-industry pages hold full structured detail (signals, value drivers, capabilities, and more).'
  );
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Industries');
  lines.push('');
  lines.push('| Industry | Summary |');
  lines.push('|----------|---------|');
  for (const ind of data.industries || []) {
    const link = `[${ind.name}](industries/${ind.slug}.md)`;
    lines.push(`| ${link} | ${escapeTableCell(truncateSummary(ind.definition, 200))} |`);
  }
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push(
    '*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*'
  );
  lines.push('');
  return lines.join('\n');
}

function generateIndustryPage(ind, filenameBySubId) {
  const lines = [];
  lines.push(`# ${ind.name}`);
  lines.push('');
  lines.push(`**Industry ID:** \`${ind.id}\`  `);
  lines.push(`**Slug:** \`${ind.slug}\`  `);
  lines.push(`**Status:** ${ind.status || '—'}`);
  lines.push('');
  lines.push('[← Industry taxonomy](../index.md)');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('## Definition');
  lines.push('');
  lines.push((ind.definition || '').trim());
  lines.push('');

  if (ind.aliases && ind.aliases.length) {
    lines.push('## Aliases');
    lines.push('');
    lines.push(bulletList(ind.aliases));
    lines.push('');
  }

  if (ind.commonBusinessModels && ind.commonBusinessModels.length) {
    lines.push('## Common business models');
    lines.push('');
    lines.push(bulletList(ind.commonBusinessModels));
    lines.push('');
  }

  if (ind.commonValueDrivers && ind.commonValueDrivers.length) {
    lines.push('## Common value drivers');
    lines.push('');
    lines.push(bulletList(ind.commonValueDrivers));
    lines.push('');
  }

  if (ind.commonCapabilities && ind.commonCapabilities.length) {
    lines.push('## Common capabilities');
    lines.push('');
    lines.push(bulletList(ind.commonCapabilities));
    lines.push('');
  }

  if (ind.tags && ind.tags.length) {
    lines.push('## Tags');
    lines.push('');
    lines.push(bulletList(ind.tags));
    lines.push('');
  }

  if (ind.signals && Object.keys(ind.signals).length) {
    lines.push('## Industry intensity signals');
    lines.push('');
    lines.push(signalsMarkdownTable(ind.signals).trimEnd());
    lines.push('');
  }

  const subs = ind.subIndustries || [];
  lines.push('## Sub-industries');
  lines.push('');
  if (subs.length === 0) {
    lines.push('*No sub-industries defined.*');
    lines.push('');
  } else {
    lines.push('| Sub-industry | Summary |');
    lines.push('|--------------|---------|');
    for (const sub of subs) {
      const file = filenameBySubId.get(sub.id);
      const link = file ? `../sub-industries/${file}` : '#';
      const label = `[${sub.name}](${link})`;
      lines.push(`| ${label} | ${escapeTableCell(truncateSummary(sub.definition, 160))} |`);
    }
    lines.push('');
  }

  lines.push('---');
  lines.push('');
  lines.push('[← Industry taxonomy](../index.md)');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push(
    '*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*'
  );
  lines.push('');
  return lines.join('\n');
}

function generateIndustryTaxonomyDocs() {
  if (!fs.existsSync(INDUSTRIES_JSON)) {
    console.log(
      '\n  ⚠ Skipping industry taxonomy — no compiled JSON (run npm run compile:industries first)'
    );
    return null;
  }

  const raw = fs.readFileSync(INDUSTRIES_JSON, 'utf8');
  const data = JSON.parse(raw);
  if (!data.industries || !Array.isArray(data.industries)) {
    console.log('\n  ⚠ Skipping industry taxonomy — invalid zorba-industries.json');
    return null;
  }

  fs.mkdirSync(DOCS_INDUSTRIES_DIR, { recursive: true });
  fs.mkdirSync(DOCS_SUB_INDUSTRIES_DIR, { recursive: true });

  const filenameBySubId = assignSubIndustryFilenames(data.industries);

  for (const ind of data.industries) {
    const page = generateIndustryPage(ind, filenameBySubId);
    fs.writeFileSync(path.join(DOCS_INDUSTRIES_DIR, `${ind.slug}.md`), page);
  }

  let subCount = 0;
  for (const ind of data.industries) {
    for (const sub of ind.subIndustries || []) {
      const mdFile = filenameBySubId.get(sub.id);
      if (!mdFile) continue;
      const body = generateSubIndustryDoc(sub, ind);
      fs.writeFileSync(path.join(DOCS_SUB_INDUSTRIES_DIR, mdFile), body);
      subCount++;
    }
  }

  fs.writeFileSync(
    path.join(DOCS_INDUSTRY_TAXONOMY_DIR, 'index.md'),
    generateIndustryTaxonomyOverviewIndex(data)
  );

  console.log(
    `\n  ✓ industry-taxonomy/index.md + ${data.industries.length} industry page(s) + ${subCount} sub-industry page(s)`
  );
  return true;
}

// --- Main ---

function main() {
  const args = process.argv.slice(2);
  const shouldBuild = args.includes('--build');

  console.log('ZORBA Documentation Generator\n');

  // Clean docs dir
  if (fs.existsSync(DOCS_DIR)) {
    fs.rmSync(DOCS_DIR, { recursive: true });
  }
  fs.mkdirSync(DOCS_DOMAINS_DIR, { recursive: true });

  // --- Core domains ---
  const coreFiles = fs.readdirSync(CORE_DIR)
    .filter(f => f.endsWith('.yaml'))
    .sort();

  const coreDomains = [];
  const coreDomainFiles = new Map(); // domain.id → md filename
  console.log(`Core: ${coreFiles.length} domains`);
  for (const file of coreFiles) {
    const data = readYaml(path.join(CORE_DIR, file));
    const domain = data.domain;
    coreDomains.push(domain);
    const outFile = file.replace('.yaml', '.md');
    coreDomainFiles.set(domain.id, outFile);
    fs.writeFileSync(
      path.join(DOCS_DOMAINS_DIR, outFile),
      generateDomainDoc(domain)
    );
    const procCount = domain.capabilities.reduce((sum, c) => sum + (c.processes ? c.processes.length : 0), 0);
    console.log(`  ✓ ${outFile} — ${domain.capabilities.length} capabilities, ${procCount} processes`);
  }

  // Core domain index — use actual YAML-derived filenames
  const coreFilenameFn = (domain) => coreDomainFiles.get(domain.id) || domainFilename(domain);
  fs.writeFileSync(
    path.join(DOCS_DOMAINS_DIR, 'index.md'),
    generateDomainIndex(
      'ZORBA Domain Taxonomy',
      'Detailed capability and process definitions for all ZORBA Core domains.\nEach process carries a unique 6-digit identifier and an agentic profile\nshowing the recommended human/agent workforce composition.',
      coreDomains,
      coreFilenameFn
    )
  );
  console.log('  ✓ domains/index.md');

  // --- Editions ---
  const editionNavSections = []; // { name, slug, domains[] } for mkdocs nav

  if (fs.existsSync(EDITIONS_DIR)) {
    const editionSlugs = fs.readdirSync(EDITIONS_DIR)
      .filter(f => fs.existsSync(path.join(EDITIONS_DIR, f, 'edition.yaml')));

    for (const slug of editionSlugs) {
      const compiledPath = path.join(DIST_DIR, `zorba-${slug}.json`);
      if (!fs.existsSync(compiledPath)) {
        console.log(`\n  ⚠ Skipping edition "${slug}" — no compiled JSON (run compile.js --all first)`);
        continue;
      }

      const compiled = JSON.parse(fs.readFileSync(compiledPath, 'utf8'));
      const editionDomainsDir = path.join(DOCS_DIR, 'editions', slug, 'domains');
      fs.mkdirSync(editionDomainsDir, { recursive: true });

      console.log(`\nEdition: ${compiled.name} (${slug})`);

      // Domain docs
      for (const domain of compiled.domains) {
        const outFile = domainFilename(domain);
        fs.writeFileSync(
          path.join(editionDomainsDir, outFile),
          generateDomainDoc(domain, compiled.name)
        );
        const procCount = domain.capabilities
          ? domain.capabilities.reduce((sum, c) => sum + (c.processes ? c.processes.length : 0), 0)
          : 0;
        console.log(`  ✓ editions/${slug}/domains/${outFile} — ${domain.capabilities ? domain.capabilities.length : 0} capabilities, ${procCount} processes`);
      }

      // Edition domain index
      fs.writeFileSync(
        path.join(editionDomainsDir, 'index.md'),
        generateDomainIndex(
          `${compiled.name} — Domain Taxonomy`,
          `Industry edition based on ZORBA Core.\nEach process carries a unique 6-digit identifier and an agentic profile\nshowing the recommended human/agent workforce composition.`,
          compiled.domains
        )
      );

      // Edition landing page
      const editionIndex = [
        `# ${compiled.name}`,
        '',
        `**Edition:** ${compiled.edition}`,
        `**Extends:** ${compiled.extends || 'core'}`,
        `**Version:** ${compiled.version}`,
        '',
        compiled.stats ? [
          '## Stats',
          '',
          `- **Domains:** ${compiled.stats.totalDomains}`,
          `- **Capabilities:** ${compiled.stats.totalCapabilities}`,
          `- **Processes:** ${compiled.stats.totalProcesses}`,
        ].join('\n') : '',
        '',
        '## Domain Taxonomy',
        '',
        'See [Domain Taxonomy](domains/index.md) for the full reference.',
        '',
        '---',
        '',
        '*© 2026 Zontally · Licensed under [Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)*',
        ''
      ].join('\n');

      fs.writeFileSync(path.join(DOCS_DIR, 'editions', slug, 'index.md'), editionIndex);
      console.log(`  ✓ editions/${slug}/index.md`);

      editionNavSections.push({
        name: compiled.name,
        slug,
        domains: compiled.domains
      });
    }
  }

  // --- Static assets ---
  const STATIC_DIR = path.join(ROOT, 'static');
  if (fs.existsSync(STATIC_DIR)) {
    copyRecursive(STATIC_DIR, DOCS_DIR);
    console.log('\n  ✓ static assets copied');
  }

  // --- Framework docs ---
  fs.mkdirSync(DOCS_FRAMEWORK_DIR, { recursive: true });
  if (fs.existsSync(FRAMEWORK_DIR)) {
    const fwFiles = fs.readdirSync(FRAMEWORK_DIR).filter(f => f.endsWith('.md'));
    for (const f of fwFiles) {
      fs.copyFileSync(path.join(FRAMEWORK_DIR, f), path.join(DOCS_FRAMEWORK_DIR, f));
    }
    console.log('  ✓ framework docs copied');
  }

  const industryTaxonomyResult = generateIndustryTaxonomyDocs();

  // --- Site index from README ---
  const readmePath = path.join(ROOT, 'README.md');
  if (fs.existsSync(readmePath)) {
    fs.copyFileSync(readmePath, path.join(DOCS_DIR, 'index.md'));
    console.log('  ✓ index.md (from README)');
  }

  // --- Copy CHANGELOG into docs ---
  const changelogPath = path.join(ROOT, 'CHANGELOG.md');
  if (fs.existsSync(changelogPath)) {
    fs.copyFileSync(changelogPath, path.join(DOCS_DIR, 'CHANGELOG.md'));
    console.log('  ✓ CHANGELOG.md copied');
  }

  // --- Generate unified mkdocs.yml ---
  const coreMkdocsPath = path.join(ROOT, 'mkdocs.yml');
  const coreMkdocs = fs.readFileSync(coreMkdocsPath, 'utf8');

  // Parse the existing mkdocs.yml to preserve theme/extensions
  const parsed = yaml.load(coreMkdocs);

  // Build framework nav from files
  const fwFiles = fs.existsSync(FRAMEWORK_DIR)
    ? fs.readdirSync(FRAMEWORK_DIR).filter(f => f.endsWith('.md')).sort()
    : [];
  const fwNav = {};
  for (const f of fwFiles) {
    const name = f.replace(/^\d+-/, '').replace('.md', '').replace(/-/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
    fwNav[name] = `framework/${f}`;
  }

  // Build edition nav — just overview links, no individual domains
  const editionNavItems = editionNavSections.map(edition => ({
    [edition.name]: `editions/${edition.slug}/index.md`
  }));

  // Assemble nav — domains and editions as single overview links (no clutter)
  const nav = [
    { 'Home': 'index.md' },
    { 'Framework': Object.entries(fwNav).map(([k, v]) => ({ [k]: v })) },
  ];

  if (industryTaxonomyResult) {
    nav.push({ 'Industry taxonomy': 'industry-taxonomy/index.md' });
  }

  nav.push({ 'Domain Taxonomy': 'domains/index.md' });

  if (editionNavItems.length > 0) {
    nav.push({ 'Industry Editions': editionNavItems });
  }

  parsed.nav = nav;

  fs.writeFileSync(coreMkdocsPath, yaml.dump(parsed, { lineWidth: 120, noRefs: true }));
  console.log('\n  ✓ mkdocs.yml updated');

  // --- Build HTML if requested ---
  if (shouldBuild) {
    console.log('\n  Building HTML docs with mkdocs...');
    const { execSync } = require('child_process');
    try {
      execSync('mkdocs build', { cwd: ROOT, stdio: 'pipe' });
      console.log('  ✓ HTML docs built → site/');
    } catch (e) {
      console.error(`  ✗ mkdocs build failed: ${e.stderr ? e.stderr.toString() : e.message}`);
    }
  }

  console.log('\nDone.');
}

main();
