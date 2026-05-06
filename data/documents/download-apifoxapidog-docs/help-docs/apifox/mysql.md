# MySQL

MySQL 是一个广受欢迎的关系型数据库管理系统，具有结构化数据存储、高性能、高可扩展性等特点。

Apifox 提供了对 MySQL 数据库的连接与操作能力，支持在接口调用前或者调用后执行 SQL 语句。

## 连接数据库


<Steps>
  <Step>
    在接口页面，点击接口中的 “前置/后置操作”，选择 “数据库操作”。
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480342/image-preview)

</Background>

  </Step>
  <Step>
点击 “数据库连接” 下拉框，选择 “数据库连接管理”，再点击右上角的 “新建” 按钮。
      <Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480349/image-preview)

</Background>

  </Step>
  <Step>
    在弹出的窗口中，选择 **MySQL** 数据库类型，填写相关连接信息，包括数据库地址、端口、用户名、密码和数据库名。你可以将相关的信息存在变量中，然后测试连接是否成功。
      <Background>

![CleanShot 2025-06-04 at 16.50.30@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/530922/image-preview)
</Background>


  </Step>
    
    <Step>
    **SSL 连接（可选）**
        
    新版 Apifox 默认支持 SSL 自动连接。如需手动配置 SSL，可在连接设置中切换到 **SSL 标签**，选择模式：

    - Prefer（默认）：支持时使用 SSL，不支持则使用非 SSL

    - Require：必须使用 SSL，否则连接失败

    - Verify CA：使用 SSL 并验证服务器 CA 证书

    - Verify Full：在 Verify CA 的基础上验证服务器主机名

    可上传 CA 证书、客户端证书、私钥（可直接输入或选择本地文件，内容会显示在输入框中）。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/555874/image-preview)
</Background>


  </Step>
    
</Steps>

:::tip[]
Apifox 推荐通过云端保存的方式集中管理数据库连接信息，并使用 Vault 变量保护敏感字段，建议避免在环境变量的 “远程值” 中填写数据库相关的明文内容。
:::

## 操作数据库


Apifox 支持标准 SQL 查询，但不支持存储过程这类复杂的 SQL 操作。


### 查（SELECT）

执行查询语句，从数据库中读取数据。

示例：

```sql
SELECT * FROM users WHERE id = 1;
```

也可以结合变量传参：

```sql
SELECT * FROM users WHERE id = '{{user_id}}';
```

数据库查询步骤执行后会返回查询结果的结构化数据，格式是一个数组对象，即使只查询到一条记录也会被包装在数组中，例如：

```json
[
    {
        "id": 1,
        "name": "jack"
    }
]
```
你可以通过 [JSONPath](https://docs.apifox.com/jsonpath.md) 提取其中的字段并保存为变量，例如：
- 变量名：`user_id`
- JSONPath：`$[0].id`

如果要保存整个结果集，则设置为 `$`，例如：

- 变量名：`userList`
- JSONPath：`$`，

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/530962/image-preview)
</Background>




### 增（INSERT）

向数据库中插入新数据。

示例：

```sql
INSERT INTO users (id, name, email) VALUES (1, 'Tom', 'tom@example.com');
```

支持动态数据：

```sql
INSERT INTO users (id, name) VALUES ('{{user_id}}', '{{user_name}}');
```

### 删（DELETE）

从数据库中删除数据。

示例：

```sql
DELETE FROM users WHERE id = 1;
```

使用变量：

```sql
DELETE FROM users WHERE id = '{{user_id}}';
```

### 改（UPDATE）

更新数据库中的已有记录。

示例：

```sql
UPDATE users SET name = 'Jerry' WHERE id = 1;
```

支持动态更新：

```sql
UPDATE users SET name = '{{new_name}}' WHERE id = '{{user_id}}';
```

## 在自动化测试中的使用

自动化测试中支持数据库操作，测试步骤里的 SQL 语句支持使用 “动态值表达式” 以及 “变量”。

### 使用动态值表达式

可以在 SQL 中通过动态值读取前置步骤的接口响应，例如：

```sql
SELECT * FROM products WHERE id = '{{$.1.response.body.products[0].id}}'
```

<Background>

![02-apifox-数据库操作.gif](https://api.apifox.com/api/v1/projects/5097254/resources/530969/image-preview)
</Background>


### 使用变量

在上游测试步骤中通过 “提取变量” 方式定义变量名（例如 `products_id`）：

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/530970/image-preview)
</Background>

然后在下游测试步骤的 SQL 中通过`{{变量名}}`引用：

```sql
SELECT * FROM products WHERE id = '{{products_id}}'
```

### 使用 ForEach 循环数据

数据库操作也支持在测试步骤中**使用 ForEach 循环**实现批量操作。

**示例一：循环中按字段查询**

```sql
SELECT * FROM products WHERE id = '{{$.4.element.id}}';
```

表达式里的数字`4`是 ForEach 步骤的 ID，在实际使用时需要替换为你自己流程中 ForEach 步骤的 ID。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/530995/image-preview)
</Background>

表达式可以通过动态值来获取：

<Background>

![06-apifox-foreach-数据库.gif](https://api.apifox.com/api/v1/projects/5097254/resources/530981/image-preview)
</Background>


**示例二：循环中插入多个字段**

```sql
INSERT INTO products (id, title) VALUES ('{{$.4.element.id}}', '{{$.4.element.title}}');
```

这在进行批量插入、验证数据是否存在等场景中非常有用。


## 常见问题


<Accordion title="连接 MySQL 8 时遇到认证失败怎么办？" defaultOpen>
目前最新的 MySQL 模块对 MySQL8 的`caching_sha2_password`加密方式支持不够完善，而`caching_sha2_password`是默认的加密方式。

需要指定`mysql_native_password`模式修改 MySQL 账号密码，用其他工具连接 MySQL 后执行下面的 SQL 来修改对应账号的密码。

```SQL
ALTER USER 'username'@'%' IDENTIFIED WITH mysql_native_password BY '123456'
```

记得手动替换上面的用户名和密码。
</Accordion>





