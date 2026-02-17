# Mock API 功能

**来源**: https://docs.apifox.com/mock

## 什么是 Mock

Mock API 可以在接口未开发完成时，提供模拟的响应数据，方便前端开发。

## 创建 Mock

### 步骤

1. 在接口详情页，点击"Mock"
2. 设置期望条件
3. 配置响应数据
4. 启用 Mock

## Mock 规则

### 基础 Mock

固定返回值：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "id": 1,
    "name": "测试数据"
  }
}
```

### 智能 Mock

根据请求参数动态生成响应：
```json
{
  "code": 200,
  "data": {
    "id": "@integer(1, 100)",
    "name": "@string",
    "email": "@email"
  }
}
```

## 高级功能

### 条件 Mock

根据请求参数返回不同数据：
- 请求参数 `type=1`：返回用户信息
- 请求参数 `type=2`：返回订单信息

### 期望模板

支持正则表达式、JSON Path 等多种匹配方式。

## 常见问题

### Q: Mock 数据和实际数据不一致？

A: 这是正常的，Mock 只是模拟数据。等接口开发完成后，使用真实接口即可。

### Q: 如何修改 Mock 数据？

A: 在 Mock 设置中直接编辑，保存后立即生效。
