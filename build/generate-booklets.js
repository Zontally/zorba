#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const DIST_DIR = path.join(ROOT, 'dist');
const FRAMEWORK_DIR = path.join(ROOT, 'framework');
const TEMP_DIR = path.join(ROOT, 'build', '.tmp-booklets');
const PANDOC_DEFAULTS = path.join(ROOT, 'build', 'booklet', 'pandoc.yaml');
const PANDOC_MODEL_DEFAULTS = path.join(ROOT, 'build', 'booklet', 'pandoc-model.yaml');
const PACKAGE_JSON = path.join(ROOT, 'package.json');

function exists(filePath) {
  return fs.existsSync(filePath);
}

function assertToolInstalled(command, versionFlag = '--version') {
  const check = spawnSync(command, [versionFlag], { encoding: 'utf8' });
  if (check.error || check.status !== 0) {
    throw new Error(
      `Required tool "${command}" is not available. Install it before running booklet generation.`
    );
  }
}

function readJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function readPackageVersion() {
  const pkg = readJson(PACKAGE_JSON);
  return pkg.version || '';
}

function formatGeneratedTimestamp(date = new Date()) {
  return new Intl.DateTimeFormat('en-GB', {
    dateStyle: 'long',
    timeStyle: 'short'
  }).format(date);
}

function readFrameworkFiles() {
  if (!exists(FRAMEWORK_DIR)) {
    throw new Error(`Framework directory not found: ${FRAMEWORK_DIR}`);
  }
  return fs.readdirSync(FRAMEWORK_DIR)
    .filter(name => name.endsWith('.md'))
    .sort((a, b) => a.localeCompare(b));
}

function normalizeFrameworkAssetPaths(content) {
  let normalized = content
    .replace(/src=["']\.\.\/\.\.\/assets\/images\//g, 'src="static/assets/images/')
    .replace(/\]\(\.\.\/\.\.\/assets\/images\//g, '](static/assets/images/');

  // Pandoc-to-PDF drops raw HTML img tags; convert them to markdown images.
  normalized = normalized.replace(
    /<img\s+[^>]*src=["']([^"']+)["'][^>]*alt=["']([^"']*)["'][^>]*>/gi,
    (_match, src, alt) => `![${alt || ''}](${src})`
  );

  // Render markdown links as plain text labels in PDFs (no clickable targets).
  normalized = normalized.replace(/(^|[^!])\[([^\]]+)\]\(([^)]+)\)/g, '$1$2');

  return normalized;
}

function discoverCompiledTargets() {
  if (!exists(DIST_DIR)) {
    throw new Error(`Dist directory not found: ${DIST_DIR}. Run compile first.`);
  }

  const files = fs.readdirSync(DIST_DIR).filter(name =>
    name.startsWith('zorba-') &&
    name.endsWith('.json') &&
    name !== 'zorba-industries.json'
  );

  const targets = files.map(filename => {
    const slug = filename.replace(/^zorba-/, '').replace(/\.json$/, '');
    const inputPath = path.join(DIST_DIR, filename);
    const outputPath = path.join(DIST_DIR, `zorba-${slug}.pdf`);
    return { slug, inputPath, outputPath };
  });

  targets.sort((a, b) => {
    if (a.slug === 'core') return -1;
    if (b.slug === 'core') return 1;
    return a.slug.localeCompare(b.slug);
  });

  return targets;
}

function parseNumericToken(text) {
  if (text === undefined || text === null) return Number.MAX_SAFE_INTEGER;
  const normalized = String(text).trim();
  const parts = normalized.split(/[^0-9]+/).filter(Boolean).map(v => Number(v));
  if (!parts.length || parts.some(Number.isNaN)) return Number.MAX_SAFE_INTEGER;
  let acc = 0;
  for (let i = 0; i < parts.length; i += 1) {
    acc = (acc * 1000) + parts[i];
  }
  return acc;
}

function cmpByNumberThenName(a, b) {
  const numberCmp = parseNumericToken(a.number) - parseNumericToken(b.number);
  if (numberCmp !== 0) return numberCmp;
  return String(a.name || '').localeCompare(String(b.name || ''));
}

function escapeCell(value) {
  const raw = value === undefined || value === null ? '' : String(value);
  return raw.replace(/\|/g, '\\|').replace(/\n/g, '<br>');
}

function formatClassification(value) {
  if (value === undefined || value === null) return '';
  return String(value)
    .replace(/_/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());
}

function toPipeTable(headers, rows) {
  const headerLine = `| ${headers.join(' | ')} |`;
  const dividerLine = `| ${headers.map(() => '---').join(' | ')} |`;
  const bodyLines = rows.map(row => `| ${row.map(escapeCell).join(' | ')} |`);
  return [headerLine, dividerLine, ...bodyLines].join('\n');
}

function countProcesses(domain) {
  return (domain.capabilities || []).reduce((sum, cap) => sum + (cap.processes || []).length, 0);
}

function countMeasurements(domain) {
  return (domain.capabilities || []).reduce((sum, cap) => {
    return sum + (cap.processes || []).reduce((procSum, proc) => procSum + (proc.measurements || []).length, 0);
  }, 0);
}

function renderDataModelSection(compiled) {
  const domains = [...(compiled.domains || [])].sort(cmpByNumberThenName);
  const lines = [];

  lines.push('# Data Model');
  lines.push('');
  lines.push('## Model Summary');
  lines.push('');
  lines.push(`- Edition: ${compiled.edition || ''}`);
  lines.push(`- Version: ${compiled.version || ''}`);
  lines.push(`- Compiled at: ${compiled.compiled_at || ''}`);
  lines.push(`- Domains: ${compiled.stats?.totalDomains ?? domains.length}`);
  lines.push(`- Capabilities: ${compiled.stats?.totalCapabilities ?? ''}`);
  lines.push(`- Processes: ${compiled.stats?.totalProcesses ?? ''}`);
  lines.push(`- Measurements: ${compiled.stats?.totalMeasurements ?? ''}`);
  lines.push('');

  for (const domain of domains) {
    lines.push(`## ${domain.number || ''} ${domain.name || ''}`.trim());
    lines.push('');
    lines.push(`- Classification: ${formatClassification(domain.classification)}`);
    lines.push(`- Capabilities: ${(domain.capabilities || []).length}`);
    lines.push(`- Processes: ${countProcesses(domain)}`);
    lines.push(`- Measurements: ${countMeasurements(domain)}`);
    lines.push('');

    const capabilities = [...(domain.capabilities || [])].sort(cmpByNumberThenName);

    if (!capabilities.length) {
      lines.push('_No capabilities defined for this domain._');
      lines.push('');
      continue;
    }

    for (const capability of capabilities) {
      lines.push(`### ${capability.number || ''} ${capability.name || ''}`.trim());
      lines.push('');

      const processes = [...(capability.processes || [])].sort(cmpByNumberThenName);
      if (!processes.length) {
        lines.push('_No processes defined for this capability._');
        lines.push('');
        continue;
      }

      for (const process of processes) {
        lines.push(`#### ${process.number || ''} ${process.name || ''}`.trim());
        lines.push('');
        lines.push(`- Agentic Profile: ${process.agentic_profile || ''}`);
        if (process.agentic_note) {
          lines.push(`- Agentic Note: ${process.agentic_note}`);
        }
        lines.push('');

        const measurements = [...(process.measurements || [])].sort(cmpByNumberThenName);
        if (!measurements.length) {
          lines.push('_No measurements defined for this process._');
          lines.push('');
          continue;
        }

        lines.push(toPipeTable(
          ['Measurement #', 'Measurement', 'What', 'Why', 'How', 'Frequency', 'Direction'],
          measurements.map(measurement => [
            measurement.number || '',
            measurement.name || '',
            measurement.what || '',
            measurement.why || '',
            measurement.how || '',
            measurement.frequency || '',
            measurement.direction || ''
          ])
        ));
        lines.push('');
      }
    }
  }

  return lines.join('\n');
}

function renderFrameworkBookletMarkdown(frameworkFiles, version) {
  const generatedAt = formatGeneratedTimestamp();
  const sections = [];
  sections.push(`\\fancyfoot[L]{Version ${version}}`);
  sections.push('');
  sections.push('\\begin{titlepage}');
  sections.push('\\centering');
  sections.push('\\vspace*{1cm}');
  sections.push('\\includegraphics[width=0.7\\textwidth]{static/assets/logo-dark.png}');
  sections.push('\\par');
  sections.push('\\vspace{2cm}');
  sections.push('{\\Huge\\bfseries ZORBA framework\\par}');
  sections.push('\\vspace{1.5cm}');
  sections.push('{\\Large The Reference Architecture for the Agentic Enterprise\\par}');
  sections.push('\\vspace{1cm}');
  sections.push('ZORBA is an open business architecture framework that defines how organisations operate when humans and AI agents work as one. From strategy to execution, across every domain, for any industry.');
  sections.push('\\par');
  sections.push('\\vspace{0.75cm}');
  sections.push(`{\\large Version ${version}\\par}`);
  sections.push('\\vfill');
  sections.push(`{\\large Generated ${generatedAt}\\par}`);
  sections.push('\\end{titlepage}');
  sections.push('');
  sections.push('\\tableofcontents');
  sections.push('');
  sections.push('\\newpage');
  sections.push('');
  sections.push('# Introduction');
  sections.push('');
  sections.push('This volume contains the complete ZORBA framework guidance and methodology.');
  sections.push('');
  sections.push('\\newpage');
  sections.push('');

  for (const fileName of frameworkFiles) {
    const filePath = path.join(FRAMEWORK_DIR, fileName);
    const content = fs.readFileSync(filePath, 'utf8');
    sections.push(normalizeFrameworkAssetPaths(content).trim());
    sections.push('');
    sections.push('\\newpage');
    sections.push('');
  }

  return sections.join('\n');
}

function renderModelBookletMarkdown(target, compiled, version) {
  const generatedAt = formatGeneratedTimestamp();
  const rawEditionName = target.slug === 'core'
    ? 'Core'
    : (compiled.name || target.slug);
  const prettyEditionName = rawEditionName.replace(/^ZORBA\s+/i, '').trim();
  const frameworkPdfUrl = `https://github.com/zontally/zorba/releases/download/v${version}/zorba-framework.pdf`;

  const sections = [];
  sections.push(`\\fancyfoot[L]{Version ${version}}`);
  sections.push('');
  sections.push(`# ZORBA ${prettyEditionName} Model`);
  sections.push('');
  sections.push('## Part 2: Edition Data Model');
  sections.push('');
  sections.push('This volume contains the compiled domain, capability, process, and measurement model tables.');
  sections.push('');
  sections.push(`Understand the ZORBA framework by reading Part 1: [Framework](${frameworkPdfUrl}).`);
  sections.push('');
  sections.push(`_Version ${version}_`);
  sections.push('');
  sections.push(`_Generated ${generatedAt}_`);
  sections.push('');
  sections.push('\\tableofcontents');
  sections.push('');
  sections.push('\\newpage');
  sections.push('');
  sections.push(renderDataModelSection(compiled));
  sections.push('');

  return sections.join('\n');
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function renderPdf(markdownPath, outputPdfPath, defaultsPath = PANDOC_DEFAULTS) {
  const resourcePath = [
    ROOT,
    FRAMEWORK_DIR,
    path.join(ROOT, 'static'),
    path.join(ROOT, 'docs')
  ].join(path.delimiter);

  const args = [
    markdownPath,
    '--defaults', defaultsPath,
    '--resource-path', resourcePath,
    '--output', outputPdfPath
  ];

  const result = spawnSync('pandoc', args, { encoding: 'utf8' });
  if (result.error || result.status !== 0) {
    throw new Error(
      `Pandoc failed for ${path.basename(outputPdfPath)}\n${result.stderr || result.stdout || ''}`
    );
  }
}

function main() {
  assertToolInstalled('pandoc');
  assertToolInstalled('xelatex');
  if (!exists(PANDOC_DEFAULTS)) {
    throw new Error(`Pandoc defaults file not found: ${PANDOC_DEFAULTS}`);
  }
  if (!exists(PANDOC_MODEL_DEFAULTS)) {
    throw new Error(`Pandoc model defaults file not found: ${PANDOC_MODEL_DEFAULTS}`);
  }

  ensureDir(TEMP_DIR);
  ensureDir(DIST_DIR);

  const frameworkFiles = readFrameworkFiles();
  const targets = discoverCompiledTargets();
  const version = readPackageVersion();

  if (!targets.length) {
    throw new Error('No compiled JSON targets found in dist/. Run compile first.');
  }

  console.log('Generating ZORBA booklet PDFs...');

  const frameworkMarkdown = renderFrameworkBookletMarkdown(frameworkFiles, version);
  const frameworkMarkdownPath = path.join(TEMP_DIR, 'zorba-framework-booklet.md');
  const frameworkPdfPath = path.join(DIST_DIR, 'zorba-framework.pdf');
  fs.writeFileSync(frameworkMarkdownPath, frameworkMarkdown, 'utf8');
  renderPdf(frameworkMarkdownPath, frameworkPdfPath);
  console.log(`  → ${path.relative(ROOT, frameworkPdfPath)}`);

  for (const target of targets) {
    const compiled = readJson(target.inputPath);
    const markdown = renderModelBookletMarkdown(target, compiled, version);
    const markdownPath = path.join(TEMP_DIR, `zorba-${target.slug}-model-booklet.md`);
    fs.writeFileSync(markdownPath, markdown, 'utf8');

    renderPdf(markdownPath, target.outputPath, PANDOC_MODEL_DEFAULTS);
    console.log(`  → ${path.relative(ROOT, target.outputPath)}`);
  }

  console.log('Booklet generation complete.');
}

main();
