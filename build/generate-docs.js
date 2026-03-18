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

main();
