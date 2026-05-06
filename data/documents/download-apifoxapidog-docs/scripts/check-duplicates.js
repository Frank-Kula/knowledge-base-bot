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
 * Check for duplicate files in the help-docs directory
 */
async function checkDuplicates() {
  const helpDocsDir = path.join(process.cwd(), 'help-docs');
  
  console.log('🔍 Scanning help-docs directory...\n');

  try {
    // Check if directory exists
    await fs.access(helpDocsDir);
  } catch (error) {
    console.error(`❌ Directory not found: ${helpDocsDir}`);
    process.exit(1);
  }

  // Get all files
  const allFiles = await getAllFiles(helpDocsDir);
  console.log(`📁 Found ${allFiles.length} files\n`);

  // Calculate hash for each file
  console.log('🔐 Calculating hashes...');
  const hashMap = new Map(); // hash -> [file1, file2, ...]
  
  let processed = 0;
  for (const filePath of allFiles) {
    const fileHash = await calculateFileHash(filePath);
    
    if (fileHash) {
      if (!hashMap.has(fileHash)) {
        hashMap.set(fileHash, []);
      }
      hashMap.get(fileHash).push(filePath);
    }
    
    processed++;
    if (processed % 100 === 0) {
      process.stdout.write(`   Processed ${processed}/${allFiles.length} files...\r`);
    }
  }
  
  process.stdout.write(`   Processed ${processed}/${allFiles.length} files\n\n`);

  // Find duplicate files (files with same hash, count > 1)
  const duplicates = [];
  for (const [fileHash, files] of hashMap.entries()) {
    if (files.length > 1) {
      duplicates.push({
        hash: fileHash,
        files: files,
        count: files.length
      });
    }
  }

  // Output results
  console.log('='.repeat(80));
  console.log('📊 Duplicate Files Report');
  console.log('='.repeat(80));
  console.log(`\nTotal unique files: ${hashMap.size}`);
  console.log(`Total files scanned: ${allFiles.length}`);
  console.log(`Duplicate groups found: ${duplicates.length}\n`);

  if (duplicates.length === 0) {
    console.log('✅ No duplicate files found!');
  } else {
    console.log('⚠️  Found duplicate files:\n');
    
    // Sort by duplicate count (most duplicates first)
    duplicates.sort((a, b) => b.count - a.count);
    
    let totalDuplicateFiles = 0;
    duplicates.forEach((group, index) => {
      console.log(`Group ${index + 1} (${group.count} files with same content):`);
      console.log(`  Hash: ${group.hash}`);
      group.files.forEach((file, fileIndex) => {
        const relativePath = path.relative(process.cwd(), file);
        console.log(`  ${fileIndex + 1}. ${relativePath}`);
      });
      console.log('');
      totalDuplicateFiles += group.count;
    });

    // Statistics
    const uniqueDuplicateFiles = duplicates.reduce((sum, group) => sum + group.count, 0);
    const spaceWasted = duplicates.reduce((sum, group) => {
      // Space wasted per duplicate group = (file count - 1) * file size
      // Simplified: assume all files have the same size
      return sum + (group.count - 1);
    }, 0);
    
    console.log('='.repeat(80));
    console.log('📈 Statistics:');
    console.log(`  Duplicate groups: ${duplicates.length}`);
    console.log(`  Total duplicate files: ${uniqueDuplicateFiles}`);
    console.log(`  Unique content files: ${hashMap.size}`);
    console.log(`  Potential space savings: ${spaceWasted} duplicate file(s) could be removed`);
    console.log('='.repeat(80));
  }
}

// Run the check
checkDuplicates().catch(error => {
  console.error('💥 Error:', error);
  process.exit(1);
});

