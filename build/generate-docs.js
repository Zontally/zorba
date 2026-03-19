#!/usr/bin/env node

/**
 * ZORBA Documentation Generator — generate-docs.js
 *
 * Generates human-readable Markdown documentation from YAML source files.
 * Output is designed for MkDocs consumption.
 *
 * Usage:
 *   node build/generate-docs.js              # generate from core
 *   node build/generate-docs.js --edition <name>  # generate from compiled edition
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '..');
const CORE_DIR = path.join(ROOT, 'core', 'domains');
const DOCS_DIR = path.join(ROOT, 'docs');
const DOCS_DOMAINS_DIR = path.join(ROOT, 'docs', 'domains');
const DOCS_FRAMEWORK_DIR = path.join(ROOT, 'docs', 'framework');
const FRAMEWORK_DIR = path.join(ROOT, 'framework');

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

function generateDomainDoc(domain) {
  const classification = CLASSIFICATION_LABELS[domain.classification] || domain.classification;
  const lines = [];

  // Header
  lines.push(`# Domain ${domain.number}: ${domain.name} (${domain.id})`);
  lines.push('');
  lines.push(`*${domain.subtitle}*`);
  lines.push('');
  lines.push(`**Classification:** ${classification}`);
  lines.push('**Version:** v0.1 (Draft)');
  lines.push('');
  lines.push('---');
  lines.push('');

  // Description
  lines.push('## Overview');
  lines.push('');
  lines.push(domain.description.trim());
  lines.push('');
  lines.push('---');
  lines.push('');

  // ZORBA hierarchy reference
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

  // Capabilities and processes
  lines.push('## Capabilities & Processes');
  lines.push('');

  for (const cap of domain.capabilities) {
    lines.push(`### ${cap.number} ${cap.name} (${cap.id})`);
    lines.push('');
    if (cap.description) {
      lines.push(cap.description.trim());
      lines.push('');
    }

    lines.push('| # | Process | ID | Agentic Profile |');
    lines.push('|---|---------|-----|-----------------|');

    for (const proc of cap.processes) {
      const note = proc.agentic_note || '';
      lines.push(`| ${proc.number} | ${proc.name} | ${proc.id} | ${proc.agentic_profile} — ${note} |`);
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
  for (const cap of domain.capabilities) {
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
  lines.push('*Part of the [ZORBA Domain Reference Model](../framework/04-domain-reference.md)*');
  lines.push('');
  lines.push('---');
  lines.push('');
  lines.push('*© 2026 Zontally. All rights reserved.*');
  lines.push('');

  return lines.join('\n');
}

function main() {
  console.log('ZORBA Documentation Generator\n');

  // Ensure output directory exists
  fs.mkdirSync(DOCS_DOMAINS_DIR, { recursive: true });

  // Read all core domain YAML files
  const files = fs.readdirSync(CORE_DIR)
    .filter(f => f.endsWith('.yaml'))
    .sort();

  console.log(`Generating docs for ${files.length} domains...\n`);

  for (const file of files) {
    const data = readYaml(path.join(CORE_DIR, file));
    const domain = data.domain;
    const outFile = file.replace('.yaml', '.md');
    const outPath = path.join(DOCS_DOMAINS_DIR, outFile);
    const markdown = generateDomainDoc(domain);
    fs.writeFileSync(outPath, markdown, 'utf8');

    const procCount = domain.capabilities.reduce((sum, c) => sum + (c.processes ? c.processes.length : 0), 0);
    console.log(`  ✓ ${outFile} — ${domain.capabilities.length} capabilities, ${procCount} processes`);
  }

  // Generate index page
  const indexLines = [];
  indexLines.push('# ZORBA Domain Taxonomy');
  indexLines.push('');
  indexLines.push('Detailed capability and process definitions for all ZORBA domains.');
  indexLines.push('Each process carries a unique 6-digit identifier and an agentic profile');
  indexLines.push('showing the recommended human/agent workforce composition.');
  indexLines.push('');
  indexLines.push('| # | Domain | Classification | Subtitle |');
  indexLines.push('|---|--------|---------------|----------|');

  for (const file of files) {
    const data = readYaml(path.join(CORE_DIR, file));
    const domain = data.domain;
    const mdFile = file.replace('.yaml', '.md');
    const classification = CLASSIFICATION_LABELS[domain.classification] || domain.classification;
    indexLines.push(`| ${domain.number} | [${domain.name}](${mdFile}) | ${classification} | *${domain.subtitle}* |`);
  }

  indexLines.push('');
  indexLines.push('---');
  indexLines.push('');
  indexLines.push('*© 2026 Zontally. All rights reserved.*');
  indexLines.push('');

  fs.writeFileSync(path.join(DOCS_DOMAINS_DIR, 'index.md'), indexLines.join('\n'), 'utf8');
  console.log('\n  ✓ index.md — domain index page');

  // Copy static assets into docs/
  const STATIC_DIR = path.join(ROOT, 'static');
  if (fs.existsSync(STATIC_DIR)) {
    const copyRecursive = (src, dest) => {
      fs.mkdirSync(dest, { recursive: true });
      for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        if (entry.isDirectory()) copyRecursive(srcPath, destPath);
        else fs.copyFileSync(srcPath, destPath);
      }
    };
    copyRecursive(STATIC_DIR, DOCS_DIR);
    console.log('  ✓ static assets copied');
  }

  // Copy framework docs into docs/framework/
  fs.mkdirSync(DOCS_FRAMEWORK_DIR, { recursive: true });
  if (fs.existsSync(FRAMEWORK_DIR)) {
    const fwFiles = fs.readdirSync(FRAMEWORK_DIR).filter(f => f.endsWith('.md'));
    for (const f of fwFiles) {
      fs.copyFileSync(path.join(FRAMEWORK_DIR, f), path.join(DOCS_FRAMEWORK_DIR, f));
      console.log(`  ✓ framework/${f} (copied)`);
    }
  }

  // Generate docs/index.md from README
  const readmePath = path.join(ROOT, 'README.md');
  if (fs.existsSync(readmePath)) {
    fs.copyFileSync(readmePath, path.join(DOCS_DIR, 'index.md'));
    console.log('  ✓ index.md (from README)');
  }

  console.log('\nDone.');
}

// --- Edition documentation generation ---

function generateEditionDocs(editionName) {
  const DIST_DIR = path.join(ROOT, 'dist');
  const compiledPath = path.join(DIST_DIR, `zorba-${editionName}.json`);

  if (!fs.existsSync(compiledPath)) {
    throw new Error(
      `Compiled edition not found: ${compiledPath}\n` +
      `Run "node build/compile.js --edition ${editionName}" first.`
    );
  }

  const compiled = JSON.parse(fs.readFileSync(compiledPath, 'utf8'));
  const editionDocsDir = path.join(ROOT, `docs-${editionName}`);
  const editionDomainsDir = path.join(editionDocsDir, 'domains');
  const editionFrameworkDir = path.join(editionDocsDir, 'framework');

  fs.mkdirSync(editionDomainsDir, { recursive: true });

  console.log(`\nGenerating documentation for edition: ${compiled.name}`);
  console.log(`  Output: docs-${editionName}/\n`);

  // Generate domain docs from compiled JSON (suppressed nodes already removed)
  for (const domain of compiled.domains) {
    const outFile = `${String(domain.number).padStart(2, '0')}-${domain.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '')}.md`;
    const outPath = path.join(editionDomainsDir, outFile);
    const markdown = generateDomainDoc(domain);
    fs.writeFileSync(outPath, markdown, 'utf8');

    const procCount = domain.capabilities
      ? domain.capabilities.reduce((sum, c) => sum + (c.processes ? c.processes.length : 0), 0)
      : 0;
    console.log(`  ✓ ${outFile} — ${domain.capabilities ? domain.capabilities.length : 0} capabilities, ${procCount} processes`);
  }

  // Generate index page for edition
  const indexLines = [];
  indexLines.push(`# ${compiled.name} — Domain Taxonomy`);
  indexLines.push('');
  indexLines.push(`Industry edition based on ZORBA Core.`);
  indexLines.push('Each process carries a unique 6-digit identifier and an agentic profile');
  indexLines.push('showing the recommended human/agent workforce composition.');
  indexLines.push('');
  indexLines.push('| # | Domain | Classification | Subtitle |');
  indexLines.push('|---|--------|---------------|----------|');

  for (const domain of compiled.domains) {
    const mdFile = `${String(domain.number).padStart(2, '0')}-${domain.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '')}.md`;
    const classification = CLASSIFICATION_LABELS[domain.classification] || domain.classification;
    indexLines.push(`| ${domain.number} | [${domain.name}](${mdFile}) | ${classification} | *${domain.subtitle}* |`);
  }

  indexLines.push('');
  indexLines.push('---');
  indexLines.push('');
  indexLines.push('*© 2026 Zontally. All rights reserved.*');
  indexLines.push('');

  fs.writeFileSync(path.join(editionDomainsDir, 'index.md'), indexLines.join('\n'), 'utf8');
  console.log(`\n  ✓ index.md — edition domain index`);

  // Copy framework docs into edition docs
  fs.mkdirSync(editionFrameworkDir, { recursive: true });
  if (fs.existsSync(FRAMEWORK_DIR)) {
    const fwFiles = fs.readdirSync(FRAMEWORK_DIR).filter(f => f.endsWith('.md'));
    for (const f of fwFiles) {
      fs.copyFileSync(path.join(FRAMEWORK_DIR, f), path.join(editionFrameworkDir, f));
    }
    console.log(`  ✓ framework docs copied`);
  }

  // Copy static assets
  const STATIC_DIR = path.join(ROOT, 'static');
  if (fs.existsSync(STATIC_DIR)) {
    const copyRecursive = (src, dest) => {
      fs.mkdirSync(dest, { recursive: true });
      for (const entry of fs.readdirSync(src, { withFileTypes: true })) {
        const srcPath = path.join(src, entry.name);
        const destPath = path.join(dest, entry.name);
        if (entry.isDirectory()) copyRecursive(srcPath, destPath);
        else fs.copyFileSync(srcPath, destPath);
      }
    };
    copyRecursive(STATIC_DIR, editionDocsDir);
    console.log('  ✓ static assets copied');
  }

  // Generate edition index
  const editionIndex = [
    `# ${compiled.name}`,
    '',
    `**Edition:** ${compiled.edition}`,
    `**Extends:** ${compiled.extends || 'core'}`,
    `**Version:** ${compiled.version}`,
    `**Compiled:** ${compiled.compiled_at}`,
    '',
    `## Stats`,
    '',
    `- **Domains:** ${compiled.stats.totalDomains}`,
    `- **Capabilities:** ${compiled.stats.totalCapabilities}`,
    `- **Processes:** ${compiled.stats.totalProcesses}`,
    '',
    `## Domain Taxonomy`,
    '',
    `See [Domain Taxonomy](domains/index.md) for the full reference.`,
    '',
    '---',
    '',
    '*© 2026 Zontally. All rights reserved.*',
    ''
  ].join('\n');

  fs.writeFileSync(path.join(editionDocsDir, 'index.md'), editionIndex, 'utf8');
  console.log(`  ✓ edition index.md`);

  // Generate edition-specific mkdocs.yml
  const domainNavEntries = compiled.domains.map(domain => {
    const mdFile = `${String(domain.number).padStart(2, '0')}-${domain.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/-+$/, '')}.md`;
    return `      - "${domain.name}": domains/${mdFile}`;
  });

  // Read core mkdocs.yml for theme/extensions config
  const coreMkdocs = fs.readFileSync(path.join(ROOT, 'mkdocs.yml'), 'utf8');
  const themeMatch = coreMkdocs.match(/^theme:[\s\S]*?(?=\n\w)/m);
  const extMatch = coreMkdocs.match(/^markdown_extensions:[\s\S]*$/m);
  const cssMatch = coreMkdocs.match(/^extra_css:[\s\S]*?(?=\n\w)/m);

  // Read framework dir for nav entries
  const fwFiles = fs.existsSync(FRAMEWORK_DIR)
    ? fs.readdirSync(FRAMEWORK_DIR).filter(f => f.endsWith('.md')).sort()
    : [];
  const fwNavEntries = fwFiles.map(f => {
    const name = f.replace(/^\d+-/, '').replace('.md', '').replace(/-/g, ' ')
      .replace(/\b\w/g, c => c.toUpperCase());
    return `      - "${name}": framework/${f}`;
  });

  const editionMkdocs = [
    `site_name: ${compiled.name}`,
    `site_description: ${compiled.name} — Industry Edition of ZORBA`,
    `docs_dir: docs-${editionName}`,
    `site_dir: site-${editionName}`,
    '',
    themeMatch ? themeMatch[0].trim() : '',
    '',
    cssMatch ? cssMatch[0].trim() : '',
    '',
    'nav:',
    '  - Home: index.md',
    '  - Framework:',
    ...fwNavEntries,
    '  - Domain Taxonomy:',
    `      - Overview: domains/index.md`,
    ...domainNavEntries,
    '',
    extMatch ? extMatch[0].trim() : '',
    ''
  ].join('\n');

  const mkdocsPath = path.join(ROOT, `mkdocs-${editionName}.yml`);
  fs.writeFileSync(mkdocsPath, editionMkdocs, 'utf8');
  console.log(`  ✓ mkdocs-${editionName}.yml`);

  // Build HTML docs with mkdocs
  console.log(`\n  Building HTML docs with mkdocs...`);
  const { execSync } = require('child_process');
  try {
    execSync(`mkdocs build -f mkdocs-${editionName}.yml`, { cwd: ROOT, stdio: 'pipe' });
    console.log(`  ✓ HTML docs built → site-${editionName}/`);
  } catch (e) {
    console.error(`  ✗ mkdocs build failed: ${e.stderr ? e.stderr.toString() : e.message}`);
  }

  console.log('\nDone.');
}

// --- Main ---

const args = process.argv.slice(2);
const editionIdx = args.indexOf('--edition');

if (editionIdx !== -1 && args[editionIdx + 1]) {
  generateEditionDocs(args[editionIdx + 1]);
} else {
  main();
}
