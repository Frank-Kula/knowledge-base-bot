import cron from 'node-cron';
import { downloadSite, SITES } from './download-docs.js';

// 每天早上 11:00 执行同步
const SYNC_CRON = '0 11 * * *';

async function runSync() {
  console.log(`\n${'='.repeat(60)}`);
  console.log(`⏰ 定时同步任务开始 - ${new Date().toLocaleString('zh-CN')}`);
  console.log(`${'='.repeat(60)}\n`);

  const sitesToDownload = Object.keys(SITES);
  console.log(`🎯 同步站点: ${sitesToDownload.join(', ')}`);

  for (const siteName of sitesToDownload) {
    await downloadSite(siteName, SITES[siteName]);
  }

  console.log(`\n✅ 同步完成 - ${new Date().toLocaleString('zh-CN')}`);
}

// 启动定时任务
function startScheduler() {
  console.log('🚀 文档同步调度器启动');
  console.log(`📅 同步计划: 每天早上 11:00`);
  console.log(`📁 同步目录: ${Object.values(SITES).map(s => s.outputDir).join(', ')}`);

  // 立即执行一次同步（可选）
  if (process.argv.includes('--now')) {
    console.log('\n⚡ 立即执行同步...');
    runSync().catch(console.error);
  }

  // 定时任务
  cron.schedule(SYNC_CRON, () => {
    runSync().catch(console.error);
  }, {
    timezone: 'Asia/Shanghai'
  });

  console.log('\n按 Ctrl+C 停止调度器');
}

startScheduler();