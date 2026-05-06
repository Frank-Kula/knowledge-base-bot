# Mock 数据

Apifox 提供了一个高效的 Mock 引擎，能够根据接口文档自动生成合理的响应数据，无需额外配置。

Mock 数据可应用于以下场景：

1. 前后端并行开发时，API 文档已完成但接口尚未开发，前端可以使用 Mock 数据进行开发。
2. 当 API 涉及不便直接调用的生产数据时，前端可以借助 Mock 数据进行开发。
3. 测试过程中，外部数据需要测试数据集时，可以使用 Mock 数据作为数据源。

## 开始使用

<Steps>
  <Step>
    指定一个接口或导入接口文档，这个接口需要有设定好的返回值。
  </Step>
  <Step>
    复制 Mock URL：
      
    在 “文档模式” 下，位于 “接口” 标签页中。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480512/image-preview)
</Background>

    在 “调试模式” 下，位于 “Mock” 标签页中。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480515/image-preview)
</Background>

  </Step>
  <Step>
    访问这个 URL 就能获取 Mock 数据，刷新页面数据就会更新。

<Background>

![CleanShot 2024-11-29 at 16.42.18@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/480516/image-preview)
</Background>

  </Step>
</Steps>

## Apifox 的 Mock 功能能做什么？

Apifox 的 Mock 功能可以满足以下需求：

1. [根据接口文档自动生成数据](https://docs.apifox.com/smart-mock.md)
2. [返回接口文档中指定的响应示例](https://docs.apifox.com/smart-mock.md)
3. [返回自定义的指定响应数据](https://docs.apifox.com/custom-mock.md)
4. [根据不同的请求参数返回不同的自定义响应](https://docs.apifox.com/custom-mock.md)
5. [根据请求参数返回相关的响应数据](https://docs.apifox.com/mock-scripts.md)


## Mock 服务器

Apifox 提供了三种 Mock 方式：本地 Mock、云端 Mock 和 Runner Mock。

### 本地 Mock

本地 Mock 是与 Apifox 客户端一起安装的本地服务器，它会在 Apifox 客户端启动时自动启用，并且只有在 Apifox 客户端运行时才能使用。


- 本地 Mock 适用于本地前端调试场景
- 你可以在环境管理弹窗中的本地 Mock 环境下查看该本地 Mock 服务器的 URL

    <Background>

    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480518/image-preview)
    </Background>

- 本地 Mock 服务器不能关闭或从环境中移除
- 本地 Mock 只能在 Apifox 客户端使用，网页版不支持

### 云端 Mock

云端 Mock 的功能与本地 Mock 相同，但它部署在 Apifox 的服务器上。与本地 Mock 不同，云端 Mock 不依赖本地机器的开启，您可以在任何机器上随时访问云端 Mock 数据。

- 云端 Mock 适用于公开 API 的沙箱环境
- 云端 Mock 支持加密访问
- 默认情况下为关闭状态，您可以随时开启或关闭云端 Mock。

<Background>

![CleanShot 2024-11-29 at 16.46.03@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/480519/image-preview)
</Background>


:::caution[]
Apifox 提供的云端 Mock URL 会不定时变更，仅供测试使用，“切勿” 用于生产环境。
:::

:::highlight purple
了解更多[云端 Mock](https://docs.apifox.com/cloud-mock.md)的信息。
:::

### Runner Mock

Runner Mock 服务器部署在团队自有的 [Runner](https://docs.apifox.com/universal-runner.md) 上。团队需要先在服务器上部署 Runner，之后所有成员都可以使用该 Runner 来 Mock 数据，它不依赖于本地机器是否开启。

Runner Mock 适用于大规模自动化测试的数据源或非公开 API 的沙箱环境。

:::highlight purple
了解更多[自托管 Runner Mock](https://docs.apifox.com/runner-mock.md)的信息。
:::

## 访问 Mock 服务器

访问 Mock 服务器主要有两种方式：URL 访问和 Apifox 发送。

### URL 访问

在 Apifox 的每个 HTTP 接口中，都可以找到“Mock”模块。

- 在 “文档模式” 下，位于 “接口” 标签页中；
- 在 “调试模式” 下，位于 “Mock” 标签页中。

在这里，你可以复制 Mock URL，并在任何地方使用它来请求 Mock 数据。

如果接口配置了多个响应或多个 Mock 预期，每个响应/预期都会有独立的 Mock URL。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480522/image-preview)
</Background>

你可以点击 “快捷请求” 按钮直接在 Apifox 中发起这些请求。

:::caution[]
请注意，如果使用 “点击复制”，它只会复制 URL，不包括请求方法和请求体。在发起请求时，你需要手动添加这些必要的部分。
:::


### 在 Apifox 中访问 Mock 数据

在每个 Apifox 项目中，你可以在右上角的环境管理中找到本地 Mock 和云端 Mock。

当你将环境切换到本地 Mock 或云端 Mock 时，Apifox 中的请求将会发送到对应的 Mock 环境。

:::caution[]
只有路径以 "/" 开头的 Apifox 接口才会发送到 Mock 环境。带有自定义前置 URL 或不以 "/" 开头的接口将不会发送到 Mock 环境。
:::



## Mock 请求 URL 使用说明

在使用 Mock 功能时，请确保请求的 `Method` 与接口定义中的一致。假设：

- 项目 ID：`18600`
- 接口 ID：`89343`
- 接口路径：`/users/123`
- 请求方式：`POST`

则对应的 Mock 请求地址如下：

### 本地 Mock 地址
```http
POST http://127.0.0.1:4523/m1/18600-0-default/users/123
或
POST http://127.0.0.1:4523/m2/18600-0-default/89343
```

### 云端 Mock 地址
```http
POST https://mock.apifox.cn/m1/18600-0-default/users/123
或
POST https://mock.apifox.cn/m2/18600-0-default/89343
```

只需定义接口或数据结构，Apifox 即自动生成 Mock 数据，无需额外配置，访问上述地址即可获取返回结果。



## Mock URL 格式说明

### 本地 Mock

- **路径模式**
  ```
  http://127.0.0.1:4523/m1/{项目 ID}-{版本编号}-{服务编号}/{接口路径}
  ```
  示例：
  ```
  http://127.0.0.1:4523/m1/18600-0-0/users/123
  ```

- **ID 模式**
  ```
  http://127.0.0.1:4523/m2/{项目 ID}-{版本编号}-{服务编号}/{接口 ID}
  ```
  示例：
  ```
  http://127.0.0.1:4523/m2/18600-0-0/84924
  ```

### 云端 Mock

- **路径模式**
  ```
  https://mock.apifox.cn/m1/{项目 ID}-{版本编号}-{服务编号}/{接口路径}
  ```
  示例：
  ```
  https://mock.apifox.cn/m1/18600-0-0/users/123
  ```

- **ID 模式**
  ```
  https://mock.apifox.cn/m2/{项目 ID}-{版本编号}-{服务编号}/{接口 ID}
  ```
  示例：
  ```
  https://mock.apifox.cn/m2/18600-0-0/84924
  ```

:::warning 注意
Apifox 提供的云端 Mock URL 会不定时变更，仅供测试使用，“切勿” 用于生产环境。若有需要可以使用[自托管 Runner Mock](https://docs.apifox.com/runner-mock.md)功能。
:::



### 参数说明

- **项目 ID**：在 Apifox 中打开项目，进入「项目设置」页面查看。

    <Frame>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/513159/image-preview)
    </Frame>

- **接口 ID**：在「接口名称」处即可查看。

    <Frame>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/513157/image-preview)
    </Frame>

- **版本编号**：默认填写 `0`，表示主版本（多版本功能尚未上线）。
- **服务编号**：默认服务填写 `default`。当默认服务下不存在该接口时，系统会自动查找其他服务中的同路径接口。



### 使用提示

:::tip 使用建议
1. 本地 Mock 服务默认监听在 `127.0.0.1`，如需其他设备访问，请将 IP 替换为本机局域网地址。若无法访问，请检查防火墙或端口 `4523` 是否被拦截。

2. 若项目内存在多个接口具有相同的 `Method + Path`，请使用以下方式避免冲突：
   - **路径模式**：添加 `?apifoxApiId={接口 ID}` 查询参数。
   - **ID 模式**：无需额外操作，直接使用接口 ID。

3. 若接口路径不是以 `/` 开头，只能使用 **接口 ID 模式**。

4. 启动 Apifox 即默认启动 Mock 服务，无需手动开启。

5. Mock 服务的 `前置 URL` 是固定的，无法修改。
:::



### 本地旧版 Mock

- **路径模式**
  ```
  http://127.0.0.1:4523/mock/{项目 ID}/{接口路径}
  ```
  示例：
  ```
  http://127.0.0.1:4523/mock/18600/users/123
  ```

- **ID 模式**
  ```
  http://127.0.0.1:4523/mock2/{项目 ID}/{接口 ID}
  ```
  示例：
  ```
  http://127.0.0.1:4523/mock2/18600/84924
  ```

> 当前仍支持旧版地址，但将逐步废弃，建议尽快切换到新版格式。


## 如何获取接口 Mock URL？

进入「接口详情」页面，点击右侧的「Mock」模块，即可查看当前接口的 Mock 地址。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/507978/image-preview)

</Background>

