#!/usr/bin/env node

/**
 * ZORBA Industry Model Compiler — compile-industries.js
 *
 * Compiles YAML industry source files into a single machine-readable JSON file.
 *
 * Usage:
 *   node build/compile-industries.js
 *
 * Reads:
 *   package.json                   — version (synced into model.yaml before compile)
 *   industries/model.yaml          — model metadata
 *   industries/<slug>.yaml         — one file per industry (with embedded sub-industries)
 *
 * Writes:
 *   dist/zorba-industries.json     — compiled industry model
 */

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const ROOT = path.resolve(__dirname, '..');
const INDUSTRIES_DIR = path.join(ROOT, 'industries');
const DIST_DIR = path.join(ROOT, 'dist');
const PACKAGE_JSON = path.join(ROOT, 'package.json');
const MODEL_YAML = path.join(INDUSTRIES_DIR, 'model.yaml');

/**
 * Writes industries/model.yaml `version` from package.json (semver → vX.Y.Z).
 * Skips the write if already in sync.
 */
function syncIndustryModelVersionFromPackage() {
  const pkg = JSON.parse(fs.readFileSync(PACKAGE_JSON, 'utf8'));
  const ver = (pkg.version || '').trim();
  if (!ver) {
    throw new Error('package.json is missing "version"');
  }
  const versionStr = ver.startsWith('v') ? ver : `v${ver}`;
  let content = fs.readFileSync(MODEL_YAML, 'utf8');
  const newLine = `version: "${versionStr}"`;
  if (!/^version:\s/m.test(content)) {
    throw new Error('industries/model.yaml missing version: field');
  }
  const updated = content.replace(/^version:\s*.+$/m, newLine);
  if (updated !== content) {
    fs.writeFileSync(MODEL_YAML, updated, 'utf8');
    console.log(`  Synced industries/model.yaml version → ${versionStr} (from package.json)`);
  }
}

function readYaml(filePath) {
  const content = fs.readFileSync(filePath, 'utf8');
  return yaml.load(content);
}

function validateIndustry(industry, file) {
  const required = ['id', 'name', 'slug', 'definition', 'status'];
  for (const field of required) {
    if (!industry[field]) {
      throw new Error(`Industry in ${file} missing required field: ${field}`);
    }
  }

  const ids = new Set();
  ids.add(industry.id);

  if (industry.subIndustries) {
    for (const sub of industry.subIndustries) {
      const subRequired = ['id', 'name', 'slug', 'definition', 'status'];
      for (const field of subRequired) {
        if (!sub[field]) {
          throw new Error(`Sub-industry "${sub.name || sub.id}" in ${file} missing required field: ${field}`);
        }
      }
      if (ids.has(sub.id)) {
        throw new Error(`Duplicate ID "${sub.id}" in ${file}`);
      }
      ids.add(sub.id);
    }
  }

  return ids;
}

function main() {
  console.log('Compiling ZORBA Industry Model...');

  if (!fs.existsSync(MODEL_YAML)) {
    throw new Error(`Model metadata not found: ${MODEL_YAML}`);
  }
  syncIndustryModelVersionFromPackage();

  const modelMeta = readYaml(MODEL_YAML);

  // Read all industry files
  const industryFiles = fs.readdirSync(INDUSTRIES_DIR)
    .filter(f => f.endsWith('.yaml') && f !== 'model.yaml')
    .sort();

  if (industryFiles.length === 0) {
    throw new Error(`No industry YAML files found in ${INDUSTRIES_DIR}`);
  }

  const industries = [];
  const allIds = new Set();

  for (const file of industryFiles) {
    const filePath = path.join(INDUSTRIES_DIR, file);
    const data = readYaml(filePath);

    if (!data.industry) {
      throw new Error(`${file} must have a top-level "industry" key`);
    }

    const industry = data.industry;
    const ids = validateIndustry(industry, file);

    // Check for cross-file ID collisions
    for (const id of ids) {
      if (allIds.has(id)) {
        throw new Error(`Duplicate ID "${id}" found in ${file} (already defined in another file)`);
      }
      allIds.add(id);
    }

    industries.push(industry);

    const subCount = industry.subIndustries ? industry.subIndustries.length : 0;
    console.log(`  ${industry.name}: ${subCount} sub-industries`);
  }

  // Build output
  const output = {
    model: modelMeta.model,
    version: modelMeta.version,
    generatedAt: new Date().toISOString(),
    status: modelMeta.status,
    description: modelMeta.description?.trim(),
    industries
  };

  // Stats
  const totalSubs = industries.reduce((sum, ind) =>
    sum + (ind.subIndustries ? ind.subIndustries.length : 0), 0);
  console.log(`\n  Total: ${industries.length} industries, ${totalSubs} sub-industries`);

  // Write
  fs.mkdirSync(DIST_DIR, { recursive: true });
  const outPath = path.join(DIST_DIR, 'zorba-industries.json');
  fs.writeFileSync(outPath, JSON.stringify(output, null, 2), 'utf8');
  console.log(`  → ${path.relative(ROOT, outPath)}`);
  console.log('\nDone.');
}

main();
