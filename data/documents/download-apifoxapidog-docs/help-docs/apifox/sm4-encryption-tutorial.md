# 前置脚本中使用 SM4 加密完整教程

本教程将一步步教你如何在前置脚本中使用 SM4 加密来加密请求体。

## 前置条件

1. 确保使用 **Apifox 桌面客户端**（WEB 版不支持 `fox.liveRequire`）
2. 确保网络连接正常（需要从 npm 下载 `gm-crypto` 库）
3. 了解基本的 JavaScript 语法

## 步骤一：理解 SM4 加密的基本概念

SM4 是中国国家密码管理局发布的商用密码算法标准，是一种分组密码算法。

**关键参数：**
- **密钥（key）**：32 位十六进制字符串（64 个字符），例如：`0123456789abcdeffedcba9876543210`
- **初始化向量（IV）**：CBC 模式需要，32 位十六进制字符串
- **加密模式**：
  - **ECB 模式**：不需要 IV，简单但安全性较低
  - **CBC 模式**：需要 IV，安全性更高（推荐）

## 步骤二：准备请求体数据

在加密之前，我们需要获取请求体的原始数据。如果请求体中包含变量（如 `{{variable}}`），需要先进行变量替换。

```javascript
// 获取请求体，并替换其中的变量
const originalBody = pm.variables.replaceIn(pm.request.body.raw);
console.log('原始请求体:', originalBody);
```

**说明：**
- `pm.request.body.raw`：获取请求体的原始字符串
- `pm.variables.replaceIn()`：将字符串中的变量（如 `{{variable}}`）替换为实际值
- 如果请求体是 JSON 格式，变量替换后仍然是 JSON 字符串

## 步骤三：加载 gm-crypto 库

使用 `fox.liveRequire` 动态加载 `gm-crypto` 库：

```javascript
fox.liveRequire("gm-crypto", (module) => {
  // 在这里使用加密库
});
```

**注意：** `fox.liveRequire` 是异步的，回调函数会在库加载完成后执行。

## 步骤四：执行加密操作

在回调函数中执行加密：

```javascript
fox.liveRequire("gm-crypto", (module) => {
  try {
    // 1. 从模块中解构出 SM4
    const { SM4 } = module;
    
    // 2. 设置密钥（32 位十六进制字符串）
    const key = '0123456789abcdeffedcba9876543210';
    
    // 3. 获取原始请求体
    const originalBody = pm.variables.replaceIn(pm.request.body.raw);
    
    // 4. 执行加密（ECB 模式）
    const encryptedData = SM4.encrypt(originalBody, key, {
      inputEncoding: 'utf8',    // 输入编码为 UTF-8
      outputEncoding: 'base64'   // 输出编码为 Base64
    });
    
    console.log('加密后的数据:', encryptedData);
    
    // 5. 更新请求体
    pm.request.body.update(encryptedData);
    
  } catch (error) {
    console.error('加密过程中发生错误:', error);
    throw error;
  }
});
```

## 步骤五：完整示例代码

### 示例 1：ECB 模式加密（简单，不需要 IV）

```javascript
// 步骤 1：获取原始请求体（处理变量替换）
const originalBody = pm.variables.replaceIn(pm.request.body.raw);
console.log('原始请求体:', originalBody);

// 步骤 2：加载加密库并执行加密
fox.liveRequire("gm-crypto", (module) => {
  try {
    const { SM4 } = module;
    
    // 设置密钥（32 位十六进制字符串，64 个字符）
    const key = '0123456789abcdeffedcba9876543210';
    
    // ECB 模式加密
    const encryptedData = SM4.encrypt(originalBody, key, {
      inputEncoding: 'utf8',      // 输入编码
      outputEncoding: 'base64'   // 输出编码（也可以是 'hex'）
    });
    
    console.log('加密后的数据:', encryptedData);
    
    // 更新请求体为加密后的数据
    pm.request.body.update(encryptedData);
    
    console.log('请求体已更新，准备发送请求');
  } catch (error) {
    console.error('加密过程中发生错误:', error);
    throw error;
  }
});
```

### 示例 2：CBC 模式加密（推荐，更安全）

```javascript
// 步骤 1：获取原始请求体
const originalBody = pm.variables.replaceIn(pm.request.body.raw);
console.log('原始请求体:', originalBody);

// 步骤 2：加载加密库并执行加密
fox.liveRequire("gm-crypto", (module) => {
  try {
    const { SM4 } = module;
    
    // 设置密钥（32 位十六进制字符串）
    const key = '0123456789abcdeffedcba9876543210';
    
    // 设置初始化向量（32 位十六进制字符串）
    const iv = '0123456789abcdeffedcba9876543210';
    
    // CBC 模式加密
    const encryptedData = SM4.encrypt(originalBody, key, {
      iv: iv,                    // 初始化向量
      mode: SM4.constants.CBC,   // 加密模式为 CBC
      inputEncoding: 'utf8',      // 输入编码
      outputEncoding: 'hex'       // 输出编码（也可以是 'base64'）
    });
    
    console.log('加密后的数据:', encryptedData);
    
    // 更新请求体
    pm.request.body.update(encryptedData);
    
    console.log('请求体已更新，准备发送请求');
  } catch (error) {
    console.error('加密过程中发生错误:', error);
    throw error;
  }
});
```

### 示例 3：如果接口需要 JSON 格式的加密数据

如果接口需要接收 JSON 格式，例如 `{"data": "加密后的字符串"}`：

```javascript
const originalBody = pm.variables.replaceIn(pm.request.body.raw);
console.log('原始请求体:', originalBody);

fox.liveRequire("gm-crypto", (module) => {
  try {
    const { SM4 } = module;
    const key = '0123456789abcdeffedcba9876543210';
    
    // 加密
    const encryptedData = SM4.encrypt(originalBody, key, {
      inputEncoding: 'utf8',
      outputEncoding: 'base64'
    });
    
    // 包装成 JSON 格式
    const encryptedBody = JSON.stringify({
      data: encryptedData
    });
    
    // 更新请求体
    pm.request.body.update(encryptedBody);
    
    console.log('请求体已更新为 JSON 格式:', encryptedBody);
  } catch (error) {
    console.error('加密过程中发生错误:', error);
    throw error;
  }
});
```

## 步骤六：在 Apifox 中配置

### 1. 打开接口详情页

在 Apifox 中打开需要加密的接口。

### 2. 添加前置操作

1. 点击 **"前置操作"** 标签
2. 点击 **"添加前置操作"**
3. 选择 **"自定义脚本"**

### 3. 粘贴脚本代码

将上面的示例代码粘贴到脚本编辑器中。

### 4. 修改密钥和参数

根据你的实际需求修改：
- **密钥（key）**：替换为你的实际密钥
- **初始化向量（iv）**：如果使用 CBC 模式，替换为你的实际 IV
- **输出编码**：根据接口要求选择 `base64` 或 `hex`

### 5. 测试运行

1. 点击 **"发送"** 按钮发送请求
2. 查看控制台输出，确认加密是否成功
3. 在请求详情中查看实际发送的请求体

## 常见问题解答

### Q1: 为什么回调函数没有执行？

**可能原因：**
1. 网络问题导致库加载失败
2. 使用了 WEB 版 Apifox（不支持 `fox.liveRequire`）
3. 库加载超时

**解决方法：**
- 确保使用桌面客户端
- 检查网络连接
- 查看控制台是否有错误信息

### Q2: 如何知道加密是否成功？

在脚本中添加 `console.log` 输出：
```javascript
console.log('原始请求体:', originalBody);
console.log('加密后的数据:', encryptedData);
console.log('请求体已更新');
```

### Q3: 密钥和 IV 应该从哪里获取？

- 密钥和 IV 通常由后端开发人员提供
- 或者从接口文档中获取
- 也可以从环境变量中读取：
  ```javascript
  const key = pm.environment.get('SM4_KEY');
  const iv = pm.environment.get('SM4_IV');
  ```

### Q4: 如何从环境变量读取密钥？

```javascript
// 从环境变量读取密钥和 IV
const key = pm.environment.get('SM4_KEY') || '0123456789abcdeffedcba9876543210';
const iv = pm.environment.get('SM4_IV') || '0123456789abcdeffedcba9876543210';

fox.liveRequire("gm-crypto", (module) => {
  // ... 使用 key 和 iv
});
```

### Q5: 如何加密 JSON 对象？

如果请求体是 JSON 对象，先转换为字符串再加密：

```javascript
// 获取 JSON 对象
const bodyObj = JSON.parse(pm.variables.replaceIn(pm.request.body.raw));

// 转换为字符串
const bodyString = JSON.stringify(bodyObj);

// 加密字符串
fox.liveRequire("gm-crypto", (module) => {
  const { SM4 } = module;
  const key = '0123456789abcdeffedcba9876543210';
  
  const encryptedData = SM4.encrypt(bodyString, key, {
    inputEncoding: 'utf8',
    outputEncoding: 'base64'
  });
  
  pm.request.body.update(encryptedData);
});
```

### Q6: 如何验证加密结果？

可以在后置脚本中解密验证（仅用于测试）：

```javascript
// 后置脚本：解密验证
fox.liveRequire("gm-crypto", (module) => {
  try {
    const { SM4 } = module;
    const key = '0123456789abcdeffedcba9876543210';
    
    // 获取响应中的加密数据（假设接口返回了加密数据）
    const encryptedData = pm.response.json().data;
    
    // 解密
    const decryptedData = SM4.decrypt(encryptedData, key, {
      inputEncoding: 'base64',
      outputEncoding: 'utf8'
    });
    
    console.log('解密后的数据:', decryptedData);
  } catch (error) {
    console.error('解密错误:', error);
  }
});
```

## 完整示例：加密并发送请求

这是一个完整的示例，包含错误处理和日志输出：

```javascript
console.log('=== 开始 SM4 加密流程 ===');

// 1. 获取原始请求体
const originalBody = pm.variables.replaceIn(pm.request.body.raw);
console.log('步骤 1 - 原始请求体:', originalBody);

// 2. 从环境变量读取密钥（如果没有则使用默认值）
const key = pm.environment.get('SM4_KEY') || '0123456789abcdeffedcba9876543210';
console.log('步骤 2 - 使用密钥:', key.substring(0, 8) + '...');

// 3. 加载加密库并执行加密
fox.liveRequire("gm-crypto", (module) => {
  try {
    console.log('步骤 3 - 加密库加载成功');
    
    const { SM4 } = module;
    
    // 4. 执行加密（ECB 模式）
    console.log('步骤 4 - 开始加密...');
    const encryptedData = SM4.encrypt(originalBody, key, {
      inputEncoding: 'utf8',
      outputEncoding: 'base64'
    });
    
    console.log('步骤 5 - 加密完成');
    console.log('加密后的数据（前 50 个字符）:', encryptedData.substring(0, 50) + '...');
    
    // 5. 更新请求体
    pm.request.body.update(encryptedData);
    console.log('步骤 6 - 请求体已更新');
    console.log('=== SM4 加密流程完成 ===');
    
  } catch (error) {
    console.error('=== 加密失败 ===');
    console.error('错误信息:', error.message);
    console.error('错误堆栈:', error.stack);
    throw error;
  }
});
```

## 总结

使用 SM4 加密的完整流程：

1. ✅ 获取原始请求体（处理变量替换）
2. ✅ 加载 `gm-crypto` 库
3. ✅ 设置密钥（和 IV，如果使用 CBC 模式）
4. ✅ 执行加密操作
5. ✅ 更新请求体
6. ✅ 发送请求

记住：
- 必须使用桌面客户端
- 确保网络连接正常
- 密钥必须是 32 位十六进制字符串（64 个字符）
- 在回调函数中更新请求体
- 添加错误处理和日志输出便于调试


