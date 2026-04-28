#!/usr/bin/env node

/**
 * ZORBA Compiler — compile.js
 *
 * Compiles YAML source files into a single machine-readable JSON object graph.
 * Supports core compilation and edition merging (override + extend).
 *
 * Usage:
 *   node build/compile.js                    # compile core only
 *   node build/compile.js --edition <name>   # compile core + edition
 *   node build/compile.js --all              # compile core + all editions
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const XLSX = require('xlsx');

const ROOT = path.resolve(__dirname, '..');
const CORE_DIR = path.join(ROOT, 'core', 'domains');
const EDITIONS_DIR = path.join(ROOT, 'editions');
const DIST_DIR = path.join(ROOT, 'dist');

// --- Helpers ---

function readYaml(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  return yaml.load(content);
}

function readAllDomains(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir)
    .filter(f => f.endsWith('.yaml'))
    .sort()
    .map(f => {
      const data = readYaml(path.join(dir, f));
      return data.domain;
    });
}

function collectIds(domains) {
  const ids = new Map(); // id → { type, name, file }
  for (const domain of domains) {
    addId(ids, domain.id, 'domain', domain.name);
    if (domain.capabilities) {
      for (const cap of domain.capabilities) {
        addId(ids, cap.id, 'capability', cap.name);
        if (cap.processes) {
          for (const proc of cap.processes) {
            addId(ids, proc.id, 'process', proc.name);
          }
        }
      }
    }
  }
  return ids;
}

function addId(ids, id, type, name) {
  if (ids.has(id)) {
    const existing = ids.get(id);
    throw new Error(
      `Duplicate ID "${id}": "${name}" (${type}) conflicts with "${existing.name}" (${existing.type})`
    );
  }
  ids.set(id, { type, name });
}

function computeStats(domains) {
  let totalCapabilities = 0;
  let totalProcesses = 0;
  let totalMeasurements = 0;
  const profileCounts = {};

  for (const domain of domains) {
    if (domain.capabilities) {
      totalCapabilities += domain.capabilities.length;
      for (const cap of domain.capabilities) {
        if (cap.processes) {
          totalProcesses += cap.processes.length;
          for (const proc of cap.processes) {
            const profile = proc.agentic_profile || 'unknown';
            profileCounts[profile] = (profileCounts[profile] || 0) + 1;
            if (proc.measurements) {
              totalMeasurements += proc.measurements.length;
            }
          }
        }
      }
    }
  }

  return {
    totalDomains: domains.length,
    totalCapabilities,
    totalProcesses,
    totalMeasurements,
    profileCounts
  };
}

// --- Core compilation ---

function compileCore() {
  console.log('Compiling ZORBA Core...');

  const domains = readAllDomains(CORE_DIR);
  if (domains.length === 0) {
    throw new Error(`No YAML files found in ${CORE_DIR}`);
  }

  // Validate unique IDs
  collectIds(domains);

  const stats = computeStats(domains);
  console.log(`  ${stats.totalDomains} domains, ${stats.totalCapabilities} capabilities, ${stats.totalProcesses} processes, ${stats.totalMeasurements} measurements`);

  const core = {
    edition: 'core',
    name: 'ZORBA Core',
    version: require(path.join(ROOT, 'package.json')).version,
    compiled_at: new Date().toISOString(),
    stats,
    domains
  };

  return core;
}

// --- Edition compilation ---

function compileEdition(editionName, core) {
  const editionDir = path.join(EDITIONS_DIR, editionName);
  const editionFile = path.join(editionDir, 'edition.yaml');

  if (!fs.existsSync(editionFile)) {
    throw new Error(`Edition file not found: ${editionFile}`);
  }

  console.log(`Compiling edition: ${editionName}...`);

  const editionMeta = readYaml(editionFile);

  // Deep clone core domains
  let domains = JSON.parse(JSON.stringify(core.domains));

  // Apply overrides
  const overridesDir = path.join(editionDir, 'overrides');
  if (fs.existsSync(overridesDir)) {
    const overrides = readAllDomains(overridesDir);
    for (const override of overrides) {
      const idx = domains.findIndex(d => d.id === override.id);
      if (idx === -1) {
        throw new Error(`Edition "${editionName}" overrides domain ID "${override.id}" which does not exist in core`);
      }
      // Merge: override capabilities replace core capabilities with same ID, add new ones
      if (override.capabilities) {
        for (const overrideCap of override.capabilities) {
          const capIdx = domains[idx].capabilities.findIndex(c => c.id === overrideCap.id);
          if (capIdx !== -1) {
            // Replace existing capability
            domains[idx].capabilities[capIdx] = overrideCap;
          } else {
            // Add new capability
            domains[idx].capabilities.push(overrideCap);
          }
        }
      }
      // Override domain-level fields if provided
      if (override.name) domains[idx].name = override.name;
      if (override.subtitle) domains[idx].subtitle = override.subtitle;
      if (override.description) domains[idx].description = override.description;
    }
  }

  // Apply extensions (new domains or new capabilities in new domain files)
  const extensionsDir = path.join(editionDir, 'extensions');
  if (fs.existsSync(extensionsDir)) {
    const extensions = readAllDomains(extensionsDir);
    for (const ext of extensions) {
      const existingIdx = domains.findIndex(d => d.id === ext.id);
      if (existingIdx !== -1) {
        // Extend existing domain with new capabilities
        if (ext.capabilities) {
          domains[existingIdx].capabilities.push(...ext.capabilities);
        }
      } else {
        // Entirely new domain
        domains.push(ext);
      }
    }
  }

  // Apply suppress flags — remove suppressed nodes from the distribution
  let suppressedCount = 0;
  for (const domain of domains) {
    if (domain.suppress) {
      suppressedCount++;
      continue; // Domain-level suppression handled below
    }
    if (domain.capabilities) {
      const beforeCount = domain.capabilities.length;
      domain.capabilities = domain.capabilities.filter(cap => {
        if (cap.suppress) {
          suppressedCount++;
          console.log(`  ⊘ Suppressed: ${cap.number} ${cap.name} (${cap.id})`);
          return false;
        }
        // Check for suppressed processes within capabilities
        if (cap.processes) {
          const procBefore = cap.processes.length;
          cap.processes = cap.processes.filter(proc => {
            if (proc.suppress) {
              suppressedCount++;
              console.log(`  ⊘ Suppressed: ${proc.number} ${proc.name} (${proc.id})`);
              return false;
            }
            return true;
          });
        }
        return true;
      });
    }
  }
  // Remove suppressed domains
  const domainsBefore = domains.length;
  domains = domains.filter(d => !d.suppress);
  suppressedCount += (domainsBefore - domains.length);

  if (suppressedCount > 0) {
    console.log(`  ${suppressedCount} node(s) suppressed`);
  }

  // Validate unique IDs across merged result
  collectIds(domains);

  const stats = computeStats(domains);
  console.log(`  ${stats.totalDomains} domains, ${stats.totalCapabilities} capabilities, ${stats.totalProcesses} processes, ${stats.totalMeasurements} measurements`);

  return {
    edition: editionName,
    name: editionMeta.edition?.name || editionName,
    extends: 'core',
    version: require(path.join(ROOT, 'package.json')).version,
    compiled_at: new Date().toISOString(),
    stats,
    domains
  };
}

// --- Output ---

function writeJson(filename, data) {
  fs.mkdirSync(DIST_DIR, { recursive: true });
  const outPath = path.join(DIST_DIR, filename);
  fs.writeFileSync(outPath, JSON.stringify(data, null, 2), 'utf8');
  console.log(`  → ${path.relative(ROOT, outPath)}`);
}

function sanitizeSheetName(name) {
  return name
    .replace(/[:\\/?*[\]]/g, ' ')
    .trim()
    .slice(0, 31) || 'Domain';
}

function getUniqueSheetName(baseName, usedNames) {
  let candidate = baseName;
  let index = 2;

  while (usedNames.has(candidate)) {
    const suffix = ` (${index})`;
    const maxBaseLength = 31 - suffix.length;
    candidate = `${baseName.slice(0, maxBaseLength)}${suffix}`;
    index++;
  }

  usedNames.add(candidate);
  return candidate;
}

function addHeaderAutoFilter(worksheet) {
  const range = XLSX.utils.decode_range(worksheet['!ref'] || 'A1:A1');
  worksheet['!autofilter'] = {
    ref: XLSX.utils.encode_range({
      s: { c: range.s.c, r: 0 },
      e: { c: range.e.c, r: range.e.r }
    })
  };
}

function writeMeasurementsWorkbook(baseFilename, compiled) {
  fs.mkdirSync(DIST_DIR, { recursive: true });

  const workbook = XLSX.utils.book_new();
  const usedSheetNames = new Set();
  const domainsSummaryRows = [];

  for (const domain of compiled.domains || []) {
    let processCount = 0;
    let measurementCount = 0;

    for (const capability of domain.capabilities || []) {
      processCount += (capability.processes || []).length;
      for (const process of capability.processes || []) {
        measurementCount += (process.measurements || []).length;
      }
    }

    domainsSummaryRows.push({
      Domain: `${domain.number}. ${domain.name}`,
      Subtitle: domain.subtitle || '',
      Description: domain.description || '',
      Classification: domain.classification || '',
      Capabilities: (domain.capabilities || []).length,
      Processes: processCount,
      Measurements: measurementCount
    });
  }

  const domainsWorksheet = XLSX.utils.json_to_sheet(domainsSummaryRows);
  addHeaderAutoFilter(domainsWorksheet);
  const domainsSheetName = getUniqueSheetName('Domains', usedSheetNames);
  XLSX.utils.book_append_sheet(workbook, domainsWorksheet, domainsSheetName);

  for (const domain of compiled.domains || []) {
    const rows = [];

    for (const capability of domain.capabilities || []) {
      for (const process of capability.processes || []) {
        for (const measurement of process.measurements || []) {
          const domainLabel = `${domain.number}. ${domain.name}`;
          const capabilityLabel = `${capability.number}. ${capability.name}`;
          const processLabel = `${process.number}. ${process.name}`;
          rows.push({
            Domain: domainLabel,
            Capability: capabilityLabel,
            Process: processLabel,
            'Measurement ID': measurement.id,
            'Measurement Number': measurement.number,
            'Measurement Name': measurement.name,
            What: measurement.what,
            Why: measurement.why,
            How: measurement.how,
            Frequency: measurement.frequency,
            Direction: measurement.direction
          });
        }
      }
    }

    const worksheet = XLSX.utils.json_to_sheet(rows);
    addHeaderAutoFilter(worksheet);
    const baseSheetName = sanitizeSheetName(`${domain.number} ${domain.name}`);
    const sheetName = getUniqueSheetName(baseSheetName, usedSheetNames);
    XLSX.utils.book_append_sheet(workbook, worksheet, sheetName);
  }

  const outPath = path.join(DIST_DIR, `${baseFilename}.xlsx`);
  XLSX.writeFile(workbook, outPath);
  console.log(`  → ${path.relative(ROOT, outPath)}`);
}

// --- Main ---

function main() {
  const args = process.argv.slice(2);
  const core = compileCore();
  writeJson('zorba-core.json', core);
  writeMeasurementsWorkbook('zorba-core', core);

  if (args.includes('--all')) {
    // Compile all editions
    if (fs.existsSync(EDITIONS_DIR)) {
      const editions = fs.readdirSync(EDITIONS_DIR)
        .filter(f => {
          const editionFile = path.join(EDITIONS_DIR, f, 'edition.yaml');
          return fs.existsSync(editionFile);
        });
      for (const edition of editions) {
        const compiled = compileEdition(edition, core);
        writeJson(`zorba-${edition}.json`, compiled);
        writeMeasurementsWorkbook(`zorba-${edition}`, compiled);
      }
    }
  } else {
    const editionIdx = args.indexOf('--edition');
    if (editionIdx !== -1 && args[editionIdx + 1]) {
      const editionName = args[editionIdx + 1];
      const compiled = compileEdition(editionName, core);
      writeJson(`zorba-${editionName}.json`, compiled);
      writeMeasurementsWorkbook(`zorba-${editionName}`, compiled);
    }
  }

  console.log('\nDone.');
}

main();
