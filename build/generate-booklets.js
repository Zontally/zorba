#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const DIST_DIR = path.join(ROOT, 'dist');
const FRAMEWORK_DIR = path.join(ROOT, 'framework');
const TEMP_DIR = path.join(ROOT, 'build', '.tmp-booklets');
const PANDOC_DEFAULTS = path.join(ROOT, 'build', 'booklet', 'pandoc.yaml');

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

function readFrameworkFiles() {
  if (!exists(FRAMEWORK_DIR)) {
    throw new Error(`Framework directory not found: ${FRAMEWORK_DIR}`);
  }
  return fs.readdirSync(FRAMEWORK_DIR)
    .filter(name => name.endsWith('.md'))
    .sort((a, b) => a.localeCompare(b));
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
    const outputPath = path.join(DIST_DIR, `zorba-${slug}-booklet.pdf`);
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

  lines.push('## Domain Summary');
  lines.push('');
  lines.push(toPipeTable(
    ['Domain #', 'Domain', 'Classification', 'Capabilities', 'Processes', 'Measurements'],
    domains.map(domain => [
      domain.number || '',
      domain.name || '',
      domain.classification || '',
      (domain.capabilities || []).length,
      countProcesses(domain),
      countMeasurements(domain)
    ])
  ));
  lines.push('');

  lines.push('## Capabilities');
  lines.push('');
  lines.push(toPipeTable(
    ['Domain #', 'Domain', 'Capability #', 'Capability', 'Processes'],
    domains.flatMap(domain => {
      const capabilities = [...(domain.capabilities || [])].sort(cmpByNumberThenName);
      return capabilities.map(cap => [
        domain.number || '',
        domain.name || '',
        cap.number || '',
        cap.name || '',
        (cap.processes || []).length
      ]);
    })
  ));
  lines.push('');

  lines.push('## Processes');
  lines.push('');
  lines.push(toPipeTable(
    ['Domain #', 'Capability #', 'Process #', 'Process', 'Agentic Profile', 'Agentic Note'],
    domains.flatMap(domain => {
      const capabilities = [...(domain.capabilities || [])].sort(cmpByNumberThenName);
      return capabilities.flatMap(cap => {
        const processes = [...(cap.processes || [])].sort(cmpByNumberThenName);
        return processes.map(proc => [
          domain.number || '',
          cap.number || '',
          proc.number || '',
          proc.name || '',
          proc.agentic_profile || '',
          proc.agentic_note || ''
        ]);
      });
    })
  ));
  lines.push('');

  lines.push('## Measurements');
  lines.push('');

  for (const domain of domains) {
    const capabilities = [...(domain.capabilities || [])].sort(cmpByNumberThenName);
    const rows = capabilities.flatMap(cap => {
      const processes = [...(cap.processes || [])].sort(cmpByNumberThenName);
      return processes.flatMap(proc => {
        const measurements = [...(proc.measurements || [])].sort(cmpByNumberThenName);
        return measurements.map(measurement => [
          cap.number || '',
          cap.name || '',
          proc.number || '',
          proc.name || '',
          measurement.number || '',
          measurement.name || '',
          measurement.what || '',
          measurement.why || '',
          measurement.how || '',
          measurement.frequency || '',
          measurement.direction || ''
        ]);
      });
    });

    lines.push(`### ${domain.number || ''} ${domain.name || ''}`.trim());
    lines.push('');

    if (!rows.length) {
      lines.push('_No measurements in this domain._');
      lines.push('');
      continue;
    }

    lines.push(toPipeTable(
      [
        'Capability #',
        'Capability',
        'Process #',
        'Process',
        'Measurement #',
        'Measurement',
        'What',
        'Why',
        'How',
        'Frequency',
        'Direction'
      ],
      rows
    ));
    lines.push('');
  }

  return lines.join('\n');
}

function renderBookletMarkdown(target, compiled, frameworkFiles) {
  const prettyEditionName = target.slug === 'core'
    ? 'Core'
    : (compiled.name || target.slug);

  const sections = [];
  sections.push(`# ZORBA ${prettyEditionName} Booklet`);
  sections.push('');
  sections.push(`_Version ${compiled.version || ''}_`);
  sections.push('');
  sections.push(`_Generated ${new Date().toISOString()}_`);
  sections.push('');
  sections.push('\\newpage');
  sections.push('');
  sections.push('# Framework');
  sections.push('');

  for (const fileName of frameworkFiles) {
    const filePath = path.join(FRAMEWORK_DIR, fileName);
    const title = fileName.replace(/^\d+-/, '').replace(/\.md$/, '').replace(/-/g, ' ');
    const content = fs.readFileSync(filePath, 'utf8');
    sections.push(`## ${title}`);
    sections.push('');
    sections.push(content.trim());
    sections.push('');
    sections.push('\\newpage');
    sections.push('');
  }

  sections.push(renderDataModelSection(compiled));
  sections.push('');

  return sections.join('\n');
}

function ensureDir(dirPath) {
  fs.mkdirSync(dirPath, { recursive: true });
}

function renderPdf(markdownPath, outputPdfPath, title) {
  const args = [
    markdownPath,
    '--defaults', PANDOC_DEFAULTS,
    '--metadata', `title=${title}`,
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

  ensureDir(TEMP_DIR);
  ensureDir(DIST_DIR);

  const frameworkFiles = readFrameworkFiles();
  const targets = discoverCompiledTargets();

  if (!targets.length) {
    throw new Error('No compiled JSON targets found in dist/. Run compile first.');
  }

  console.log('Generating ZORBA booklet PDFs...');

  for (const target of targets) {
    const compiled = readJson(target.inputPath);
    const markdown = renderBookletMarkdown(target, compiled, frameworkFiles);
    const markdownPath = path.join(TEMP_DIR, `zorba-${target.slug}-booklet.md`);
    fs.writeFileSync(markdownPath, markdown, 'utf8');

    const pdfTitle = target.slug === 'core'
      ? 'ZORBA Core Booklet'
      : `ZORBA ${compiled.name || target.slug} Booklet`;

    renderPdf(markdownPath, target.outputPath, pdfTitle);
    console.log(`  → ${path.relative(ROOT, target.outputPath)}`);
  }

  console.log('Booklet generation complete.');
}

main();
