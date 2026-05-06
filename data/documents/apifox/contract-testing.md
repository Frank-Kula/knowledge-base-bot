# 契约测试

契约测试（Contract Test）用于校验接口的实际返回结果是否符合 API 文档（OpenAPI）中定义的规范。通过对状态码、响应结构等内容进行一致性检查，可以在研发、调试和测试阶段及时发现接口与文档不一致的问题，确保服务之间的接口行为稳定可靠。

Apifox 的契约测试能力与接口文档深度联动，可在接口运行、调试用例、测试用例及自动化测试步骤中使用，属于默认启用的基础能力。


## 开启契约测试

契约测试支持按模块启用，可根据业务需求在不同阶段使用，相关开关位于 “项目设置 -> 校验响应设置”。


<Background>

![CleanShot 2025-11-18 at 16.13.59@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594590/image-preview)
</Background>

### 接口运行与调试用例

启用后，在“接口管理”的接口运行和调试用例界面可使用“校验响应”，用于调试阶段对接口返回进行一致性验证。

<Background>

![CleanShot 2025-11-18 at 16.46.51@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594619/image-preview)
</Background>


### 测试用例

启用后，在“接口管理”中的“接口测试用例”可执行“校验响应”，在手动测试过程中验证接口行为。

<Background>

![CleanShot 2025-11-18 at 16.52.16@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594624/image-preview)
</Background>


### 自动化测试步骤

启用后，在“自动化测试”模块的测试步骤中可添加“校验响应”，将契约测试纳入完整的自动化测试流程。

<Background>

![CleanShot 2025-11-18 at 16.55.11@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594626/image-preview)
</Background>


## 校验内容（契约项）

Apifox 的契约测试会根据接口文档中的 OpenAPI 规范定义，自动进行以下校验：

### 校验 HTTP 状态码

检查实际响应的 HTTP 状态码是否与文档中定义的状态码一致。例如：

* 文档定义 200，但实际返回 204
* 文档定义多个可能值（如 200、201），按允许范围校验

不一致时将提示校验失败。

<Background>

![CleanShot 2025-11-18 at 16.57.14@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594631/image-preview)
 
![CleanShot 2025-11-18 at 16.58.30@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594634/image-preview)
</Background>


### 校验响应 Body 的数据结构（Schema 校验）

根据文档中定义的 “JSON Schema/数据结构/数据模型” 校验以下内容：

* 字段是否必需
* 字段值是否为 null
* 字段类型是否正确
* 必填字段是否存在
* 数组、Object 的结构是否符合文档定义
* 枚举值是否有效
* ......

这是契约测试的核心校验能力。

<Background>

![CleanShot 2025-11-18 at 17.01.48@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594635/image-preview)
</Background>


### Object 对象的额外字段控制

对于 Object 类型字段：

* 若文档未设置 `additionalProperties`，可选择是否允许实际响应出现文档未定义的额外字段
* 若文档已设置 `additionalProperties`，则按文档规则校验额外字段的允许情况

该能力支持放宽或严格控制响应结构，以适应不同团队的接口约束要求。

<Background>

![CleanShot 2025-11-18 at 17.03.37@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594639/image-preview)

![CleanShot 2025-11-18 at 17.04.08@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/594641/image-preview)
</Background>




