# 使用 discriminator 实现多态数据结构

在部分场景下，一个对象可能有多种不同的结构形式，例如图书既可能是电子书，也可能是纸质书。此时可以通过`discriminator`字段来区分不同的 Schema 类型。

`discriminator` 通常与 `oneOf` 或 `anyOf` 配合使用，用于告诉系统 “某个字段的值代表了对象所属的具体类型”。

* **propertyName**：指定用于区分类型的字段名称。
* **mapping**：定义字段值与对应 Schema 的映射关系。


## 在 Apifox 中的设置方式

### 方式一：通过 JSON Schema 设置


<Steps>
  <Step title="通过可视化界面配置 oneOf">
      
    打开接口请求体或响应体编辑页，选择要定义为 “组合模式” 的字段。点击 “高级设置 → 组合模式 → oneOf”，在 `oneOf` 中引用你需要组合的数据模型，例如 `eBook` 和 `Paperback`。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583497/image-preview)
</Background>

  </Step>
  <Step title="通过 JSON Schema 添加 discriminator">
    在编辑器中点击 JSON Schema 切换到代码模式。
 <Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583470/image-preview)
</Background>
      
    添加 `discriminator` 配置，例如：
    
```js
"discriminator": {
    "propertyName": "type",
    "mapping": {
        "ebook": "#/definitions/211412987",
        "paperback": "#/definitions/211412988"
    }
}

```
      
将 `211412987` 和 `211412988` 替换为你实际数据模型的 ID，打开 JSON Schema 配置面板的时候就可以看到。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/583500/image-preview)
</Background>

      
  </Step>
  <Step title="查看效果">


保存后，Apifox 会根据 `type` 字段自动识别不同类型。


<Background>

![01-apifox.gif](https://api.apifox.com/api/v1/projects/5097254/resources/583473/image-preview)
</Background>

  </Step>
</Steps>




### 方式二：通过导入 OpenAPI 文件

将定义写入 OpenAPI YAML 或 JSON 文件，例如：

```yaml
components:
  schemas:
    Book:
      discriminator:
        propertyName: type
        mapping:
          ebook: '#/components/schemas/eBook'
          paperback: '#/components/schemas/Paperback'
      properties:
        type:
          type: string
          description: Book type
```

完整定义如下：

```yaml
openapi: 3.0.3
info:
  title: Book Example with Discriminator
  version: 1.0.0

components:
  schemas:
    Book:
      type: object
      properties:
        type:
          type: string
          description: Book type

    eBook:
      allOf:
        - $ref: '#/components/schemas/Book'
        - type: object
          properties:
            fileFormat:
              type: string
              description: File format of the eBook (e.g. PDF, EPUB)
          required:
            - fileFormat

    Paperback:
      allOf:
        - $ref: '#/components/schemas/Book'
        - type: object
          properties:
            pageCount:
              type: integer
              description: Number of pages in the book
          required:
            - pageCount

    BookUnion:
      oneOf:
        - $ref: '#/components/schemas/eBook'
        - $ref: '#/components/schemas/Paperback'
      discriminator:
        propertyName: type
        mapping:
          ebook: '#/components/schemas/eBook'
          paperback: '#/components/schemas/Paperback'

paths:
  /books:
    get:
      summary: Get a book example
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BookUnion'

```

在 Apifox 中选择导入 OpenAPI 文件。

<Background>

![CleanShot 2025-10-22 at 11.18.25@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/583474/image-preview)
</Background>


导入后，Apifox 会自动识别 `discriminator`，并在数据模型和接口中正确映射类型。

<Background>

![02-apifox.gif](https://api.apifox.com/api/v1/projects/5097254/resources/583475/image-preview)
</Background>

