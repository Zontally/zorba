#!/usr/bin/env node

/**
 * ZORBA Validator — validate.js
 *
 * Validates YAML source files against ZORBA schema rules.
 * Runs as a pre-build step; exits with code 1 on validation failure.
 *
 * Usage:
 *   node build/validate.js              # validate core
 *   node build/validate.js --all        # validate core + all editions
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '..');
const CORE_DIR = path.join(ROOT, 'core', 'domains');
const EDITIONS_DIR = path.join(ROOT, 'editions');

const VALID_PROFILES = ['H', 'H+a', 'H=A', 'h+A', 'A'];
const VALID_CLASSIFICATIONS = ['value_chain', 'management_function'];

let errors = [];
let warnings = [];

function addError(file, msg) {
  errors.push(`ERROR [${file}]: ${msg}`);
}

function addWarning(file, msg) {
  warnings.push(`WARN  [${file}]: ${msg}`);
}

function readYaml(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    return yaml.load(content);
  } catch (e) {
    addError(filePath, `Failed to parse YAML: ${e.message}`);
    return null;
  }
}

function validateId(id, context, file) {
  if (!id) {
    addError(file, `Missing ID for ${context}`);
    return false;
  }
  if (typeof id !== 'string') {
    addError(file, `ID must be a string for ${context}, got: ${typeof id}`);
    return false;
  }
  if (!/^\d{6}$/.test(id)) {
    addError(file, `ID "${id}" for ${context} must be exactly 6 digits`);
    return false;
  }
  return true;
}

function validateDomain(data, file, allIds) {
  if (!data || !data.domain) {
    addError(file, 'Missing top-level "domain" key');
    return;
  }

  const domain = data.domain;

  // Domain-level validation
  validateId(domain.id, `domain "${domain.name || '(unnamed)'}"`, file);
  if (domain.id && allIds.has(domain.id)) {
    addError(file, `Duplicate ID "${domain.id}" — already used by "${allIds.get(domain.id)}"`);
  } else if (domain.id) {
    allIds.set(domain.id, `domain: ${domain.name}`);
  }

  if (!domain.name) addError(file, 'Domain missing "name"');
  if (!domain.subtitle) addWarning(file, 'Domain missing "subtitle"');
  if (!domain.description) addWarning(file, 'Domain missing "description"');
  if (!domain.classification) {
    addError(file, 'Domain missing "classification"');
  } else if (!VALID_CLASSIFICATIONS.includes(domain.classification)) {
    addError(file, `Invalid classification "${domain.classification}" — must be one of: ${VALID_CLASSIFICATIONS.join(', ')}`);
  }
  if (domain.number === undefined) addWarning(file, 'Domain missing "number"');

  if (!domain.capabilities || !Array.isArray(domain.capabilities)) {
    addError(file, 'Domain missing "capabilities" array');
    return;
  }

  if (domain.capabilities.length === 0) {
    addWarning(file, 'Domain has zero capabilities');
  }

  // Capability-level validation
  for (const cap of domain.capabilities) {
    const capLabel = `capability "${cap.name || cap.id || '(unnamed)'}"`;

    // Suppressed capabilities only need a valid ID
    if (cap.suppress) {
      validateId(cap.id, capLabel, file);
      continue;
    }

    validateId(cap.id, capLabel, file);
    if (cap.id && allIds.has(cap.id)) {
      addError(file, `Duplicate ID "${cap.id}" — already used by "${allIds.get(cap.id)}"`);
    } else if (cap.id) {
      allIds.set(cap.id, `capability: ${cap.name}`);
    }

    if (!cap.name) addError(file, `${capLabel} missing "name"`);
    if (!cap.number) addWarning(file, `${capLabel} missing "number"`);
    if (!cap.description) addWarning(file, `${capLabel} missing "description"`);

    if (!cap.processes || !Array.isArray(cap.processes)) {
      addError(file, `${capLabel} missing "processes" array`);
      continue;
    }

    if (cap.processes.length === 0) {
      addWarning(file, `${capLabel} has zero processes`);
    }

    // Process-level validation
    for (const proc of cap.processes) {
      const procLabel = `process "${proc.name || proc.id || '(unnamed)'}" in ${capLabel}`;

      validateId(proc.id, procLabel, file);
      if (proc.id && allIds.has(proc.id)) {
        addError(file, `Duplicate ID "${proc.id}" — already used by "${allIds.get(proc.id)}"`);
      } else if (proc.id) {
        allIds.set(proc.id, `process: ${proc.name}`);
      }

      if (!proc.name) addError(file, `${procLabel} missing "name"`);
      if (!proc.number) addWarning(file, `${procLabel} missing "number"`);

      if (!proc.agentic_profile) {
        addError(file, `${procLabel} missing "agentic_profile"`);
      } else if (!VALID_PROFILES.includes(proc.agentic_profile)) {
        addError(file, `${procLabel} has invalid agentic_profile "${proc.agentic_profile}" — must be one of: ${VALID_PROFILES.join(', ')}`);
      }

      if (!proc.agentic_note) {
        addWarning(file, `${procLabel} missing "agentic_note"`);
      }
    }
  }
}

function validateDirectory(dir, allIds) {
  if (!fs.existsSync(dir)) {
    console.log(`  Directory not found: ${dir} (skipping)`);
    return;
  }

  const files = fs.readdirSync(dir).filter(f => f.endsWith('.yaml')).sort();
  console.log(`  Validating ${files.length} files in ${path.relative(ROOT, dir)}/`);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const data = readYaml(filePath);
    if (data) {
      validateDomain(data, file, allIds);
    }
  }
}

function main() {
  const args = process.argv.slice(2);
  const allIds = new Map();

  console.log('ZORBA Validator\n');

  // Validate core
  console.log('Core:');
  validateDirectory(CORE_DIR, allIds);

  // Validate editions
  if (args.includes('--all') && fs.existsSync(EDITIONS_DIR)) {
    const editions = fs.readdirSync(EDITIONS_DIR)
      .filter(f => fs.existsSync(path.join(EDITIONS_DIR, f, 'edition.yaml')));

    for (const edition of editions) {
      console.log(`\nEdition: ${edition}`);
      const overridesDir = path.join(EDITIONS_DIR, edition, 'overrides');
      const extensionsDir = path.join(EDITIONS_DIR, edition, 'extensions');
      // Edition IDs get their own scope — overrides may replace core IDs
      const editionIds = new Map();
      validateDirectory(overridesDir, editionIds);
      // Extensions must not collide with core or overrides
      const extIds = new Map([...allIds, ...editionIds]);
      validateDirectory(extensionsDir, extIds);
    }
  }

  // Report
  console.log('\n--- Results ---');

  if (warnings.length > 0) {
    console.log(`\n${warnings.length} warning(s):`);
    warnings.forEach(w => console.log(`  ${w}`));
  }

  if (errors.length > 0) {
    console.log(`\n${errors.length} error(s):`);
    errors.forEach(e => console.log(`  ${e}`));
    console.log('\nValidation FAILED.');
    process.exit(1);
  } else {
    console.log(`\n✓ Validation passed. ${allIds.size} unique IDs verified.`);
    if (warnings.length > 0) {
      console.log(`  (${warnings.length} warnings — review recommended)`);
    }
  }
}

main();
