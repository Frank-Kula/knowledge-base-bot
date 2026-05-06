import axios from 'axios';
import { XMLParser } from 'fast-xml-parser';
import fs from 'fs/promises';
import path from 'path';
import { xxh64 } from '@node-rs/xxhash';

export const SITES = {
  apifox: {
    sitemapUrl: 'https://docs.apifox.com/sitemap.xml',
    outputDir: '../apifox'
  },
  apidog: {
    sitemapUrl: 'https://docs.apidog.com/sitemap.xml',
    outputDir: '../apidog'
  }
};

async function fetchSitemap(sitemapUrl) {
  console.log(`📥 Fetching sitemap from ${sitemapUrl}...`);
  const response = await axios.get(sitemapUrl, {
    headers: {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
  });
  return response.data;
}

function parseUrls(xmlData) {
  const parser = new XMLParser();
  const result = parser.parse(xmlData);
  
  const urls = result.urlset.url.map(item => item.loc);
  console.log(`📋 Found ${urls.length} URLs in sitemap`);
  return urls;
}

/**
 * Filter duplicate nav URLs
 * For URLs with nav parameter, if the corresponding base URL (with nav parameter removed) already exists, skip it
 * If base URL doesn't exist, add the base URL to download list (instead of nav URL)
 */
function filterDuplicateNavUrls(urls) {
  // Use Set to track already added base URLs
  const baseUrlSet = new Set();
  const filteredUrls = [];
  let navUrlsFiltered = 0;
  
  for (const url of urls) {
    try {
      const urlObj = new URL(url);
      const nav = urlObj.searchParams.get('nav');
      
      if (nav) {
        // This is a URL with nav parameter
        // Remove nav parameter to create base URL
        urlObj.searchParams.delete('nav');
        const baseUrl = urlObj.toString();
        
        if (!baseUrlSet.has(baseUrl)) {
          // Base URL doesn't exist, add base URL (instead of nav URL)
          baseUrlSet.add(baseUrl);
          filteredUrls.push(baseUrl);
        } else {
          // Base URL already exists, skip this nav URL
          navUrlsFiltered++;
        }
      } else {
        // This is a base URL (without nav parameter)
        if (!baseUrlSet.has(url)) {
          baseUrlSet.add(url);
          filteredUrls.push(url);
        }
      }
    } catch (error) {
      // If URL parsing fails, keep original URL as-is
      console.warn(`⚠️  Failed to parse URL: ${url}, keeping as-is`);
      filteredUrls.push(url);
    }
  }
  
  if (navUrlsFiltered > 0) {
    console.log(`🔍 Filtered out ${navUrlsFiltered} duplicate nav URLs`);
    console.log(`   Reduced from ${urls.length} to ${filteredUrls.length} URLs`);
  }
  
  return filteredUrls;
}

function getFilenameFromUrl(url) {
  const urlObj = new URL(url);
  let pathname = urlObj.pathname;
  
  // Remove leading slash
  pathname = pathname.replace(/^\//, '');
  
  // Handle root path
  if (!pathname) {
    pathname = 'index';
  }
  
  // Replace slashes with underscores for nested paths
  pathname = pathname.replace(/\//g, '_');
  
  // Handle query parameters (nav=xxx)
  const nav = urlObj.searchParams.get('nav');
  if (nav) {
    pathname = `${pathname}_nav_${nav}`;
  }
  
  return `${pathname}.md`;
}

// Calculate XXHash64 hash of file content
function calculateHash(content) {
  return xxh64(content).toString(16);
}

// Build content hash index (hash -> filename)
// Used to quickly find if files with same content exist
async function buildContentIndex(outputDir) {
  const index = new Map(); // hash -> filename
  
  try {
    const files = await fs.readdir(outputDir);
    console.log(`   Scanning ${files.length} existing files...`);
    
    let processed = 0;
    for (const file of files) {
      if (!file.endsWith('.md')) continue;
      
      try {
        const filepath = path.join(outputDir, file);
        const content = await fs.readFile(filepath, 'utf-8');
        const hashValue = calculateHash(content);
        
        // If multiple files have same content, record the first one found
        if (!index.has(hashValue)) {
          index.set(hashValue, file);
        }
        
        processed++;
        if (processed % 100 === 0) {
          process.stdout.write(`   Processed ${processed} files...\r`);
        }
      } catch (error) {
        // Ignore files that failed to read
        continue;
      }
    }
    
    if (processed > 0) {
      process.stdout.write(`   Processed ${processed} files\n`);
    }
  } catch (error) {
    // Directory doesn't exist or cannot be read
  }
  
  return index;
}

async function downloadMarkdown(url, outputDir, contentIndex) {
  const mdUrl = `${url}.md`;
  const filename = getFilenameFromUrl(url);
  const filepath = path.join(outputDir, filename);
  
  try {
    // Download new content
    const response = await axios.get(mdUrl, {
      timeout: 30000,
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
      }
    });
    
    const newContent = response.data;
    const contentHash = calculateHash(newContent);
    
    // Check if file with same content exists (via hash index)
    const existingFile = contentIndex.get(contentHash);
    
    if (existingFile) {
      if (existingFile === filename) {
        // Filename is also same, meaning no change at all
        console.log(`⏭️  Skipped (unchanged): ${filename}`);
        return { success: true, url: mdUrl, filename, status: 'skipped' };
      } else {
        // Filename is different but content is same, meaning URL changed but content didn't
        console.log(`⏭️  Skipped (same content, different URL): ${filename} (same as ${existingFile})`);
        return { success: true, url: mdUrl, filename, status: 'skipped', existingFile };
      }
    }
    
    // Check if file with current filename exists
    let fileExists = false;
    try {
      await fs.access(filepath);
      fileExists = true;
    } catch (error) {
      fileExists = false;
    }
    
    // If file exists, compare content hash
    if (fileExists) {
      const existingContent = await fs.readFile(filepath, 'utf-8');
      const existingHash = calculateHash(existingContent);
      
      if (existingHash === contentHash) {
        // Content is same, skip
        console.log(`⏭️  Skipped (unchanged): ${filename}`);
        return { success: true, url: mdUrl, filename, status: 'skipped' };
      }
    }
    
    // Write file (new file or updated file)
    await fs.writeFile(filepath, newContent, 'utf-8');
    
    // Update index
    contentIndex.set(contentHash, filename);
    
    const status = fileExists ? 'updated' : 'new';
    console.log(`${fileExists ? '🔄 Updated' : '✅ Downloaded'}: ${filename}`);
    
    return { success: true, url: mdUrl, filename, status };
  } catch (error) {
    console.error(`❌ Failed: ${mdUrl} - ${error.message}`);
    return { success: false, url: mdUrl, error: error.message };
  }
}

export async function downloadSite(siteName, siteConfig) {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`📚 Downloading docs for: ${siteName.toUpperCase()}`);
  console.log(`${'='.repeat(60)}\n`);
  
  try {
    // Ensure output directory exists
    await fs.mkdir(siteConfig.outputDir, { recursive: true });
    
    // Build content hash index (for detecting duplicate content)
    console.log('📑 Building content index...');
    const contentIndex = await buildContentIndex(siteConfig.outputDir);
    console.log(`   Found ${contentIndex.size} unique content files\n`);
    
    // Fetch and parse sitemap
    const xmlData = await fetchSitemap(siteConfig.sitemapUrl);
    const urls = parseUrls(xmlData);
    
    // Filter duplicate nav URLs at sitemap level
    const filteredUrls = filterDuplicateNavUrls(urls);
    
    console.log(`\n🚀 Starting incremental download of ${filteredUrls.length} markdown files...\n`);
    
    const results = {
      success: [],
      failed: [],
      new: [],
      updated: [],
      skipped: []
    };
    
    // Download files with concurrency limit
    const CONCURRENCY = 5;
    for (let i = 0; i < filteredUrls.length; i += CONCURRENCY) {
      const batch = filteredUrls.slice(i, i + CONCURRENCY);
      const batchResults = await Promise.all(
        batch.map(url => downloadMarkdown(url, siteConfig.outputDir, contentIndex))
      );
      
      batchResults.forEach(result => {
        if (result.success) {
          results.success.push(result);
          if (result.status === 'new') {
            results.new.push(result);
          } else if (result.status === 'updated') {
            results.updated.push(result);
          } else if (result.status === 'skipped') {
            results.skipped.push(result);
          }
        } else {
          results.failed.push(result);
        }
      });
      
      // Small delay between batches to avoid rate limiting
      if (i + CONCURRENCY < filteredUrls.length) {
        await new Promise(resolve => setTimeout(resolve, 500));
      }
    }
    
    // Summary
    console.log(`\n📊 Download Summary for ${siteName}:`);
    console.log(`   ✅ New: ${results.new.length}`);
    console.log(`   🔄 Updated: ${results.updated.length}`);
    console.log(`   ⏭️  Skipped (unchanged): ${results.skipped.length}`);
    console.log(`   ❌ Failed: ${results.failed.length}`);
    console.log(`   📦 Total processed: ${results.success.length}`);
    
    if (results.failed.length > 0) {
      console.log('\n❌ Failed URLs:');
      results.failed.forEach(f => console.log(`   - ${f.url}: ${f.error}`));
    }
    
    return results;
  } catch (error) {
    console.error(`💥 Error downloading ${siteName}:`, error.message);
    return { 
      success: [], 
      failed: [{ url: siteConfig.sitemapUrl, error: error.message }],
      new: [],
      updated: [],
      skipped: []
    };
  }
}

async function main() {
  const args = process.argv.slice(2);
  
  // If specific sites provided, download only those; otherwise download all
  let sitesToDownload = args.length > 0 
    ? args.filter(arg => SITES[arg])
    : Object.keys(SITES);
  
  if (args.length > 0 && sitesToDownload.length === 0) {
    console.log(`❌ Unknown site(s): ${args.join(', ')}`);
    console.log(`   Available sites: ${Object.keys(SITES).join(', ')}`);
    process.exit(1);
  }
  
  console.log(`🎯 Sites to download: ${sitesToDownload.join(', ')}`);
  
  const allResults = {};
  
  for (const siteName of sitesToDownload) {
    allResults[siteName] = await downloadSite(siteName, SITES[siteName]);
  }
  
  // Final summary
  console.log(`\n${'='.repeat(60)}`);
  console.log('📊 FINAL SUMMARY');
  console.log(`${'='.repeat(60)}`);
  
  for (const [siteName, results] of Object.entries(allResults)) {
    console.log(`\n${siteName}:`);
    console.log(`   ✅ New: ${results.new.length}`);
    console.log(`   🔄 Updated: ${results.updated.length}`);
    console.log(`   ⏭️  Skipped: ${results.skipped.length}`);
    console.log(`   ❌ Failed: ${results.failed.length}`);
    console.log(`   📦 Total: ${results.success.length}`);
  }
}

// Only run main when this file is executed directly (not imported)
if (import.meta.url === `file://${process.argv[1].replace(/\\/g, '/')}`) {
  main();
}

