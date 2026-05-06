import fs from 'fs/promises';
import path from 'path';
import { xxh64 } from '@node-rs/xxhash';

/**
 * Recursively get all files in a directory
 */
async function getAllFiles(dirPath, arrayOfFiles = []) {
  const files = await fs.readdir(dirPath);

  for (const file of files) {
    const filePath = path.join(dirPath, file);
    const stat = await fs.stat(filePath);

    if (stat.isDirectory()) {
      arrayOfFiles = await getAllFiles(filePath, arrayOfFiles);
    } else {
      arrayOfFiles.push(filePath);
    }
  }

  return arrayOfFiles;
}

/**
 * Calculate the XXHash64 hash of a file
 */
async function calculateFileHash(filePath) {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    const hash = xxh64(content);
    return hash.toString(16);
  } catch (error) {
    console.error(`❌ Error reading file ${filePath}: ${error.message}`);
    return null;
  }
}

/**
 * Extract base filename from a filename with _nav_ suffix
 * Example: "file_nav_xxx.md" -> "file.md"
 */
function getBaseFilename(navFilename) {
  const basename = path.basename(navFilename);
  const match = basename.match(/^(.+)_nav_[^_]+\.md$/);
  if (match) {
    return path.join(path.dirname(navFilename), match[1] + '.md');
  }
  return null;
}

/**
 * Clean up duplicate _nav_ files
 */
async function cleanupNavDuplicates() {
  const helpDocsDir = path.join(process.cwd(), 'help-docs');
  
  console.log('🔍 Scanning help-docs directory for _nav_ files...\n');

  try {
    // Check if directory exists
    await fs.access(helpDocsDir);
  } catch (error) {
    console.error(`❌ Directory not found: ${helpDocsDir}`);
    process.exit(1);
  }

  // Get all files
  const allFiles = await getAllFiles(helpDocsDir);
  console.log(`📁 Found ${allFiles.length} total files\n`);

  // Find all _nav_ files
  const navFiles = allFiles.filter(file => {
    const basename = path.basename(file);
    return basename.includes('_nav_') && basename.endsWith('.md');
  });

  console.log(`🔎 Found ${navFiles.length} files with _nav_ suffix\n`);

  if (navFiles.length === 0) {
    console.log('✅ No _nav_ files found. Nothing to clean up.');
    return;
  }

  // Check if each _nav_ file has a corresponding base file with the same content
  const toDelete = [];
  const skipped = [];
  const errors = [];

  console.log('🔐 Verifying duplicates...\n');

  let processed = 0;
  for (const navFile of navFiles) {
    const baseFile = getBaseFilename(navFile);
    
    if (!baseFile) {
      skipped.push({
        file: navFile,
        reason: 'Cannot extract base filename'
      });
      continue;
    }

    // Check if base file exists
    let baseFileExists = false;
    try {
      await fs.access(baseFile);
      baseFileExists = true;
    } catch (error) {
      // Base file doesn't exist, skip
      skipped.push({
        file: navFile,
        reason: `Base file not found: ${path.basename(baseFile)}`
      });
      processed++;
      if (processed % 50 === 0) {
        process.stdout.write(`   Processed ${processed}/${navFiles.length} files...\r`);
      }
      continue;
    }

    // Calculate hash of both files
    const navHash = await calculateFileHash(navFile);
    const baseHash = await calculateFileHash(baseFile);

    if (!navHash || !baseHash) {
      errors.push({
        file: navFile,
        reason: 'Failed to calculate hash'
      });
      processed++;
      if (processed % 50 === 0) {
        process.stdout.write(`   Processed ${processed}/${navFiles.length} files...\r`);
      }
      continue;
    }

    // If hashes are the same, mark for deletion
    if (navHash === baseHash) {
      toDelete.push({
        navFile,
        baseFile,
        hash: navHash
      });
    } else {
      skipped.push({
        file: navFile,
        reason: 'Content differs from base file'
      });
    }

    processed++;
    if (processed % 50 === 0) {
      process.stdout.write(`   Processed ${processed}/${navFiles.length} files...\r`);
    }
  }

  process.stdout.write(`   Processed ${processed}/${navFiles.length} files\n\n`);

  // Output statistics
  console.log('='.repeat(80));
  console.log('📊 Cleanup Report');
  console.log('='.repeat(80));
  console.log(`\nTotal _nav_ files found: ${navFiles.length}`);
  console.log(`✅ Duplicates to delete: ${toDelete.length}`);
  console.log(`⏭️  Skipped: ${skipped.length}`);
  console.log(`❌ Errors: ${errors.length}\n`);

  if (toDelete.length === 0) {
    console.log('✅ No duplicate _nav_ files found. Nothing to delete.');
    return;
  }

  // Show files to be deleted (first 10 as preview)
  console.log('📋 Files to be deleted (showing first 10):');
  toDelete.slice(0, 10).forEach((item, index) => {
    const relativeNavFile = path.relative(process.cwd(), item.navFile);
    const relativeBaseFile = path.relative(process.cwd(), item.baseFile);
    console.log(`  ${index + 1}. ${relativeNavFile}`);
    console.log(`     (duplicate of: ${relativeBaseFile})`);
  });
  if (toDelete.length > 10) {
    console.log(`  ... and ${toDelete.length - 10} more files\n`);
  } else {
    console.log('');
  }

  // Check run mode
  const args = process.argv.slice(2);
  const dryRun = args.includes('--dry-run');
  const force = args.includes('--force');

  // Default to dry-run mode unless --force is explicitly specified
  if (!force) {
    console.log('🔍 DRY RUN MODE - No files will be deleted');
    console.log(`\nFound ${toDelete.length} duplicate _nav_ files that would be deleted.`);
    console.log(`\nTo actually delete these files, use --force flag:`);
    console.log(`  npm run cleanup-duplicates -- --force`);
    console.log(`\nOr explicitly use --dry-run to preview:`);
    console.log(`  npm run cleanup-duplicates -- --dry-run`);
    return;
  }

  if (dryRun && force) {
    console.log('🔍 DRY RUN MODE (--force ignored when --dry-run is specified)');
    return;
  }

  // Execute deletion
  console.log(`\n🗑️  Deleting ${toDelete.length} duplicate files...\n`);

  let deleted = 0;
  let failed = 0;

  for (const item of toDelete) {
    try {
      await fs.unlink(item.navFile);
      deleted++;
      if (deleted % 50 === 0) {
        process.stdout.write(`   Deleted ${deleted}/${toDelete.length} files...\r`);
      }
    } catch (error) {
      failed++;
      console.error(`\n❌ Failed to delete ${item.navFile}: ${error.message}`);
    }
  }

  process.stdout.write(`   Deleted ${deleted}/${toDelete.length} files\n\n`);

  // Final statistics
  console.log('='.repeat(80));
  console.log('✅ Cleanup Complete');
  console.log('='.repeat(80));
  console.log(`\n✅ Successfully deleted: ${deleted} files`);
  if (failed > 0) {
    console.log(`❌ Failed to delete: ${failed} files`);
  }
  console.log(`\n💾 Space saved: ${deleted} duplicate file(s) removed`);
  console.log('='.repeat(80));
}

// Run cleanup
cleanupNavDuplicates().catch(error => {
  console.error('💥 Error:', error);
  process.exit(1);
});

