import fs from 'fs/promises';
import path from 'path';

/**
 * 修复 .har 文件中 base64 编码的响应内容
 * 当响应内容中有 encoding: "base64" 时，自动解码 text 字段
 */
async function fixHarBase64(harFilePath) {
  try {
    console.log(`📖 读取 HAR 文件: ${harFilePath}`);
    
    // 读取文件内容
    const fileContent = await fs.readFile(harFilePath, 'utf-8');
    const harData = JSON.parse(fileContent);
    
    if (!harData.log || !harData.log.entries) {
      console.log('⚠️  无效的 HAR 文件格式');
      return;
    }
    
    let fixedCount = 0;
    let totalEntries = harData.log.entries.length;
    
    // 遍历所有请求条目
    for (const entry of harData.log.entries) {
      if (entry.response && entry.response.content) {
        const content = entry.response.content;
        
        // 检查是否有 encoding 字段且值为 base64
        if (content.encoding === 'base64' && content.text) {
          try {
            // 解码 base64 内容
            const decodedText = Buffer.from(content.text, 'base64').toString('utf-8');
            
            // 更新 text 字段为解码后的内容
            content.text = decodedText;
            
            // 移除 encoding 字段（因为已经解码了）
            delete content.encoding;
            
            fixedCount++;
            console.log(`  ✅ 已解码: ${entry.request?.url || '未知URL'}`);
          } catch (error) {
            console.log(`  ⚠️  解码失败: ${entry.request?.url || '未知URL'} - ${error.message}`);
          }
        }
      }
    }
    
    if (fixedCount === 0) {
      console.log('ℹ️  未发现需要解码的 base64 内容');
      return;
    }
    
    // 生成输出文件名
    const dir = path.dirname(harFilePath);
    const basename = path.basename(harFilePath, '.har');
    const outputPath = path.join(dir, `${basename}_fixed.har`);
    
    // 保存修复后的文件
    await fs.writeFile(outputPath, JSON.stringify(harData, null, 2), 'utf-8');
    
    console.log(`\n📊 处理完成:`);
    console.log(`   - 总条目数: ${totalEntries}`);
    console.log(`   - 已修复: ${fixedCount}`);
    console.log(`   - 输出文件: ${outputPath}`);
    
  } catch (error) {
    console.error(`❌ 处理失败: ${error.message}`);
    if (error.code === 'ENOENT') {
      console.error(`   文件不存在: ${harFilePath}`);
    } else if (error instanceof SyntaxError) {
      console.error(`   JSON 解析失败，请确认文件格式正确`);
    }
    process.exit(1);
  }
}

// 主函数
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.log('用法: node scripts/fix-har-base64.js <har文件路径>');
    console.log('示例: node scripts/fix-har-base64.js ./example.har');
    process.exit(1);
  }
  
  const harFilePath = args[0];
  
  // 检查文件是否存在
  try {
    await fs.access(harFilePath);
  } catch (error) {
    console.error(`❌ 文件不存在: ${harFilePath}`);
    process.exit(1);
  }
  
  await fixHarBase64(harFilePath);
}

main();















