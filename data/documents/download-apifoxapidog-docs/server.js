import http from 'http';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = process.env.PORT || 3000;

// MIME 类型映射
const mimeTypes = {
  '.html': 'text/html',
  '.js': 'text/javascript',
  '.css': 'text/css',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.wav': 'audio/wav',
  '.mp4': 'video/mp4',
  '.woff': 'application/font-woff',
  '.ttf': 'application/font-ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'application/font-otf',
  '.wasm': 'application/wasm',
  '.md': 'text/markdown',
  '.txt': 'text/plain'
};

const server = http.createServer((req, res) => {
  // 解析请求路径
  let filePath = '.' + req.url;
  if (filePath === './') {
    filePath = './index.html';
  }

  // 如果请求的是目录，尝试查找 index.html
  if (filePath.endsWith('/')) {
    filePath += 'index.html';
  }

  const extname = String(path.extname(filePath)).toLowerCase();
  const contentType = mimeTypes[extname] || 'application/octet-stream';

  // 读取文件
  fs.readFile(filePath, (error, content) => {
    if (error) {
      if (error.code === 'ENOENT') {
        // 文件不存在，尝试列出目录内容
        const dirPath = filePath.replace(/\/[^/]*$/, '') || '.';
        listDirectory(dirPath, req.url, res);
      } else {
        res.writeHead(500);
        res.end(`服务器错误: ${error.code}`);
      }
    } else {
      // 如果是 markdown 文件，返回 HTML 格式
      if (extname === '.md') {
        const html = generateMarkdownHTML(content.toString(), req.url);
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
        res.end(html, 'utf-8');
      } else {
        res.writeHead(200, { 'Content-Type': contentType });
        res.end(content, 'utf-8');
      }
    }
  });
});

// 列出目录内容
function listDirectory(dirPath, urlPath, res) {
  fs.readdir(dirPath, { withFileTypes: true }, (err, files) => {
    if (err) {
      res.writeHead(500);
      res.end(`读取目录错误: ${err.code}`);
      return;
    }

    let html = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>文档目录 - ${urlPath}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
      background: #f5f5f5;
    }
    h1 {
      color: #333;
      border-bottom: 2px solid #4CAF50;
      padding-bottom: 10px;
    }
    .breadcrumb {
      margin-bottom: 20px;
      color: #666;
    }
    .breadcrumb a {
      color: #4CAF50;
      text-decoration: none;
    }
    .breadcrumb a:hover {
      text-decoration: underline;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    li {
      margin: 8px 0;
      padding: 10px;
      background: white;
      border-radius: 4px;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    li:hover {
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }
    a {
      color: #333;
      text-decoration: none;
      display: flex;
      align-items: center;
    }
    a:hover {
      color: #4CAF50;
    }
    .icon {
      margin-right: 10px;
      font-size: 18px;
    }
    .file-icon { color: #2196F3; }
    .dir-icon { color: #FF9800; }
  </style>
</head>
<body>
  <h1>📁 文档目录</h1>
  <div class="breadcrumb">
    ${generateBreadcrumb(urlPath)}
  </div>
  <ul>`;

    // 先显示目录，再显示文件
    const dirs = files.filter(f => f.isDirectory());
    const fileList = files.filter(f => f.isFile());

    dirs.forEach(file => {
      const href = path.join(urlPath, file.name).replace(/\\/g, '/');
      html += `<li><a href="${href}"><span class="icon dir-icon">📁</span> ${file.name}/</a></li>`;
    });

    fileList.forEach(file => {
      const href = path.join(urlPath, file.name).replace(/\\/g, '/');
      const isMarkdown = file.name.endsWith('.md');
      html += `<li><a href="${href}"><span class="icon file-icon">${isMarkdown ? '📄' : '📄'}</span> ${file.name}</a></li>`;
    });

    html += `</ul></body></html>`;
    res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
    res.end(html, 'utf-8');
  });
}

// 生成面包屑导航
function generateBreadcrumb(urlPath) {
  const parts = urlPath.split('/').filter(p => p);
  let breadcrumb = '<a href="/">首页</a>';
  let currentPath = '';
  
  parts.forEach(part => {
    currentPath += '/' + part;
    breadcrumb += ` / <a href="${currentPath}">${part}</a>`;
  });
  
  return breadcrumb;
}

// 生成 Markdown HTML
function generateMarkdownHTML(markdown, urlPath) {
  // 简单的 Markdown 转 HTML（可以后续使用 marked 等库增强）
  let html = markdown
    .replace(/^# (.*$)/gim, '<h1>$1</h1>')
    .replace(/^## (.*$)/gim, '<h2>$1</h2>')
    .replace(/^### (.*$)/gim, '<h3>$1</h3>')
    .replace(/^#### (.*$)/gim, '<h4>$1</h4>')
    .replace(/^\*\*(.*)\*\*/gim, '<strong>$1</strong>')
    .replace(/^\*(.*)\*/gim, '<em>$1</em>')
    .replace(/^\- (.*$)/gim, '<li>$1</li>')
    .replace(/^\d+\. (.*$)/gim, '<li>$1</li>')
    .replace(/\n/g, '<br>');

  return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${urlPath}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      max-width: 900px;
      margin: 0 auto;
      padding: 40px 20px;
      background: #f5f5f5;
      line-height: 1.6;
    }
    .container {
      background: white;
      padding: 40px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    h1 {
      color: #333;
      border-bottom: 3px solid #4CAF50;
      padding-bottom: 10px;
      margin-top: 0;
    }
    h2 {
      color: #555;
      margin-top: 30px;
      border-bottom: 2px solid #e0e0e0;
      padding-bottom: 5px;
    }
    h3, h4 {
      color: #666;
      margin-top: 20px;
    }
    a {
      color: #4CAF50;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    code {
      background: #f4f4f4;
      padding: 2px 6px;
      border-radius: 3px;
      font-family: 'Courier New', monospace;
    }
    pre {
      background: #f4f4f4;
      padding: 15px;
      border-radius: 5px;
      overflow-x: auto;
    }
    .back-link {
      display: inline-block;
      margin-bottom: 20px;
      color: #666;
      text-decoration: none;
    }
    .back-link:hover {
      color: #4CAF50;
    }
  </style>
</head>
<body>
  <div class="container">
    <a href="javascript:history.back()" class="back-link">← 返回</a>
    <div>${html}</div>
  </div>
</body>
</html>`;
}

server.listen(PORT, () => {
  console.log(`🚀 服务器已启动！`);
  console.log(`📖 访问地址: http://localhost:${PORT}`);
  console.log(`📁 文档目录: http://localhost:${PORT}/help-docs/`);
  console.log(`\n按 Ctrl+C 停止服务器`);
});









