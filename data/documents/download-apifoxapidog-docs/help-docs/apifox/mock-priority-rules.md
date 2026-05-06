# Mock 优先级

在 Apifox 中，默认的数据 Mock 方式是智能 Mock，它会根据响应的数据结构自动生成 Mock 数据。另一种常用的 Mock 方式是直接使用响应示例作为 Mock 数据。

具体设置方法如下：

<Steps>
  <Step>
    打开 “项目设置 -> 功能设置 -> Mock 设置”
  </Step>
  <Step>
   将 “智能 Mock 优先” 改成 “响应示例优先”
      <Background>

![CleanShot 2024-12-03 at 16.02.23@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/481035/image-preview)
</Background>

  </Step>
</Steps>




## **智能 Mock 优先**

- 这是 “默认 Mock 方式” 的默认选项

- 在此设置下，Mock 方式的优先级顺序为：**高级 Mock 期望 > 智能 Mock**。

## **响应示例优先**

- Mock 方式的优先级顺序变为：**高级 Mock 期望 > 响应示例 > 智能 Mock**。

- 如果某个接口没有设置响应示例，系统会自动降级使用智能 Mock

无论选择哪种优先级顺序，只要设置了 Mock 期望，它都会被最优先使用。
