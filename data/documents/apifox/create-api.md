# 新建接口


Apifox 为 API 设计者提供了直观的界面来新建接口。下面是一个 “通过 ID 查询宠物信息” 的接口示例：

## 新建接口

<Steps>
  <Step>
  **新建接口：** 打开一个新的选项卡，点击 `新建接口` 创建一个新的接口。
      
<Background>      

![CleanShot 2025-11-05 at 15.20.12@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/588461/image-preview)
</Background>     
    </Step>
  <Step>
      
  **定义请求路径：** 在接口路径栏中输入 <CopyToClipboard>`/category/{id}`</CopyToClipboard>，定义该接口的请求路径。如下：
   - **名称：** 通过 ID 获取类别
   - **Path 参数：**
     - **参数名：** `id`
     - **类型：** `integer`
     - **示例值：** `1`
<Background>
![定义路径](https://api.apifox.com/api/v1/projects/5097254/resources/465512/image-preview)
</Background>
    </Step>
  <Step>
  **设置响应结构：**
    - 滚动至 `返回响应` 部分。
    - 在 “成功(200)” 响应下，点击 “+” 创建一个名为 “data” 的字段。
<Background>      
![设置响应](https://api.apifox.com/api/v1/projects/5097254/resources/465514/image-preview)
</Background>
    </Step>
  <Step>
  **引用数据模型：**
    - 选中 “data” 字段。
    - 将类型设置为 `Object`，并选择 “引用模型”。
  <Background>         
    ![引用模型](https://api.apifox.com/api/v1/projects/5097254/resources/465517/image-preview)
  </Background>
    - 从列表中选择 “Category” 或相关的数据模型。
      
    <Background>
    ![引用模型](https://api.apifox.com/api/v1/projects/5097254/resources/465519/image-preview)
    </Background>

:::tip[使用数据模型]
对于常用的结构数据，可以将其定义为[数据模型](https://docs.apifox.com/create-data-schema.md)，并在请求或响应中进行引用。
:::

    </Step>
  <Step>
  **添加响应示例：**
    - 在 `响应示例` 部分，点击 `添加示例`。
<Background>
![添加示例](https://api.apifox.com/api/v1/projects/5097254/resources/465520/image-preview)
</Background>
    </Step>
  <Step>
  **生成示例数据：**
    - 为示例命名为 “成功示例”。
    - 点击 `自动生成` 以生成数据。
    - 点击 `确定` 以保存示例。
<Background>
  ![生成数据](https://api.apifox.com/api/v1/projects/5097254/resources/465522/image-preview)
</Background>
    </Step>
  <Step>
  **保存接口：** 点击 `保存` 按钮以保存该接口。
<Background>
![保存 API](https://api.apifox.com/api/v1/projects/5097254/resources/465524/image-preview)
</Background>
    </Step>
    <Step>          
    <a href="https://docs.apifox.com/send-api-request.md" 
       style="
          display: inline-block;
          padding: 12px 24px;
          border: 1px solid var(--ui-border-color-base,#eaecf0);
          background-color: #9373ee;
          color: #fff;
          text-decoration: none;
          border-radius: 12px;
          font-weight: 800;
          font-size: 15px;
          margin: 5px 0;
       "
    >
       发送接口请求 <Icon icon="material-outline-arrow_forward" color="white"/>
    </a>
    </Step>
</Steps>

## 了解更多

:::tip[导入现有接口]

你可以导入已有的 OAS 文件 *（如 OpenAPI/Swagger 的 `.json` 或 `.yaml` 文件）* ，而不是从头开始创建接口。详情请见[导入数据](https://docs.apifox.com/manual-import.md)章节。
:::


