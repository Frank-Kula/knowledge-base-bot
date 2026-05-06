# 请求体多示例配置

Apifox 支持为 **JSON、XML、Raw、MsgPack** 类型的请求体配置多个示例，满足以下场景需求：
- 为不同业务场景配置示例（如正常请求/异常请求）
- 符合 OAS 3.0/3.1 规范，支持导出标准 OpenAPI 文档
- 在调试、自动化测试中快速切换不同示例


<Background>   
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499929/image-preview)
</Background>




## 创建示例

### 直接添加示例

> Apifox 版本需大于 `2.7.0`

<Steps>
  <Step>
    进入 **“修改接口”** 页面，在请求参数中选择相应的 **“请求体”** 标签，点击 `+ 添加示例`
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499647/image-preview)
</Background>

  </Step>
  <Step>
    **填写示例信息**：
   - 示例名称<span style="color: gray; opacity: 0.8;">（选填，默认 `示例 1`/`示例 2`）</span>
   - 示例值<span style="color: gray; opacity: 0.8;">（必填）</span>
   - 说明<span style="color: gray; opacity: 0.8;">（支持 Markdown）</span>
   - OAS 字段名称<span style="color: gray; opacity: 0.8;">（导出 OpenAPI 时的字段名，不填则使用序号）</span>
   - OAS 扩展<span style="color: gray; opacity: 0.8;">（自定义扩展字段，导出时保留）</span>
<Background>

![CleanShot 2025-03-03 at 12.03.35@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/499648/image-preview)
</Background>

  </Step>
  <Step>
    **保存后生效**，调试时即可选择不同示例。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499649/image-preview)
</Background>
  :::tip[]
    Raw 类型的请求体调试时仅显示第一个示例值。
  :::
  </Step>
</Steps>


### 提取参数为示例


<Steps>
  <Step>
    调试时填写请求体，点击 **“提取 -> 提取到请求示例”**
      
    <Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499650/image-preview)
    </Background>

  </Step>
  <Step>
    可选择保存为 **“新增示例”** 或 **“覆盖已有示例”**
      
<Background>

![CleanShot 2025-03-03 at 12.24.55@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/499651/image-preview)
</Background>

:::tip[]
默认填充当前调试值到示例。
:::
      
  </Step>

</Steps>



## 使用示例

### 调试场景

<Steps>
  <Step>
    切换到 **“运行”** 页面，选择 **“自动生成”** 标签。
  </Step>
  <Step>
    点击下拉框选择示例，示例值将自动填充。
      <Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499649/image-preview)
</Background>
  </Step>
  <Step>
    支持实时切换示例发送请求。
  
  </Step>
    
</Steps>

:::info 高级配置

点击 “自动生成” 下拉图标，可选择使用：
- **请求示例值**：选择已定义的示例
- **发送时自动变化**：根据 [Mock](https://docs.apifox.com/smart-mock.md) 规则随机生成值
- **自动生成设置**：请参考[生成请求](https://docs.apifox.com/generate-request.md)模块文档

:::



### 文档展示

- **单示例时**：保持简洁展示（隐藏名称）

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499657/image-preview)
</Background>



- **多示例时**：左右布局切换，显示示例名称与 Markdown 说明。

  
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499658/image-preview)
</Background>

:::tip[]
Tab 显示优先级顺序：
- **示例名称 > OAS 字段名称 > 序号（从`1`开始自动递增）**
- 优先显示非空项
:::


## OAS 兼容性


### OAS 字段名称

用于控制导出 OpenAPI 文档时示例的字段名：

1. **配置方式**  
   在示例配置中填写 `OAS 字段名称`
   
    <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/499700/image-preview" width="580px" />
    </Background>


2. **导出规则**  
   - **填写时**：直接作为 `examples` 对象内元素的字段名
   - **未填写时**：自动使用序号（从 `1` 开始递增）
   
    <Container>
      <Columns>
          <Column>
                **填写时**
          </Column>
          <Column>
            **未填写时**
          </Column>
      </Columns>
        ---
      <Columns>
          <Column>


            ```json
             "examples": {
               "example1": {
                  "value": {
                    "name": "张三",
                    "category": "Lorem eu non",
                    "birthday": "2009-05-10"
                  },
                  "summary": "示例 1",
                  "description": "这是一个`示例 1`"
                },
                "example2": {
                  "value": {
                    "name": "昂婷婷",
                    "category": "et",
                    "birthday": "2012-10-28"
                  },
                  "summary": "示例 2",
                  "description": "这是一个`示例 2`"
                }
              }       
            ```

          </Column>
          <Column>
            ```json
            "examples": {
                "1": {
                  "value": {
                    "name": "张三",
                    "category": "Lorem eu non",
                    "birthday": "2009-05-10"
                  },
                  "summary": "示例 1",
                  "description": "这是一个`示例 1`"
                },
                "2": {
                  "value": {
                    "name": "昂婷婷",
                    "category": "et",
                    "birthday": "2012-10-28"
                  },
                  "summary": "示例 2",
                  "description": "这是一个`示例 2`"
                }
              }
            ```

          </Column>
        </Columns>
    </Container>



### OAS 扩展

支持为示例添加自定义 OAS 扩展：

1. **配置方法**  
   在示例配置的 `OAS 扩展` 字段中输入 JSON 格式键值对：
   ```json
   {
     "x-demo": true,
     "x-scenario": "error_case"
   }
   ```
   
    <Background>
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/499962/image-preview" width="580px" />
    </Background>


2. **导出效果**  
   扩展字段会完整保留至生成的 OpenAPI 文档：
    ```json
    "examples": {
        "example1": {
          "x-demo": true,
          "x-scenario": "error_case",
          "value": {
            "name": "张三",
            "category": "Lorem eu non",
            "birthday": "2009-05-10"
          },
          "summary": "示例 1",
          "description": "这是一个`示例 1`"
        }
    }
    ```


## 常见问题


<Accordion title="旧项目如何启用多示例？" defaultOpen>
  无需手动操作！当你在旧接口中添加第 2 个示例时，系统自动完成格式升级。
</Accordion>


<Accordion title="导出 OAS 文档时如何处理多示例？" defaultOpen={false}>
  自动按照 OAS 3.1 规范生成 examples 对象，OAS 字段名称作示例唯一标识，不填则使用序号（从 1 开始）。
   
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499683/image-preview)
</Background>
</Accordion>

<Accordion title="导出的 OAS 文档中示例顺序会变化吗？" defaultOpen={false}>
  不会，示例顺序与 Apifox 中的添加顺序完全一致。
</Accordion>

<Accordion title="如何让导出的示例名称更友好？" defaultOpen={false}>
  在示例配置中填写 OAS 字段名称（如 `example1`），导出时会直接作为示例键名。
    

<Container>
  <Columns>
      <Column>
            **配置**
      </Column>
      <Column>
        **示例效果**
      </Column>
  </Columns>
    ---
  <Columns>
      <Column>
        
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499700/image-preview)
</Background>

      </Column>
      <Column>


<Background>
    ![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/499690/image-preview)
</Background>

      </Column>
    </Columns>
</Container>


</Accordion>

