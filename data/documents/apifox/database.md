# 数据库操作

前置/后置操作支持添加数据库操作。选择并连接数据库后，你可以对数据表执行增删改查等操作。操作结果可以在控制台打印，也可以提取为变量。这些变量可以在不同场景下使用，比如作为其他接口的请求参数、断言条件、自定义脚本，或者用于其他数据库操作。

## 快速上手

下面是数据库操作的具体步骤。


<Steps>
  <Step>
    在运行标签页 *（文档模式）* 或请求标签页 *（调试模式）* 中，导航到后置操作。
  </Step>
  <Step>
    鼠标光标悬停在 “添加后置操作” 上并选择 “数据库操作”。
      

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480051/image-preview)

</Background>



  </Step>
  <Step>
   为数据库操作命名并设置数据库连接，需要确保选择的 “数据库连接” 实际数据已被正确配置。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480064/image-preview)
</Background>

  </Step>
  <Step>
输入 SQL 命令。命令中支持使用变量，如 `{{variables}}`。

  </Step>
  <Step>
设置 “提取结果到变量”，支持使用 JSONPath，开启 “控制台打印结果” 开关。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/569916/image-preview)
</Background>

  </Step>
  <Step>
点击发送请求，你可以在控制台查看数据库操作的结果。


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480067/image-preview)
</Background>

  </Step>
</Steps>

如果在自动化测试中使用了 “数据库操作” 步骤，或者在接口请求的前后置操作中使用了 “数据库操作”，也可以按照上述方式进行使用。

:::tip[]
Apifox 支持标准 SQL 查询，但不支持存储过程这类复杂的 SQL 操作。
:::

## 数据库连接

Apifox 免费版支持连接以下类型的数据库：

- MySQL
- SQL Server：支持 SQL Server 2014 以上版本
- Oracle
- Db2
- PostgreSQL
- ClickHouse
- MongoDB


升级到付费版后，还可以额外连接以下数据库：

- 达梦数据库
- Redis



在 Apifox 中设置 “数据库连接” 的步骤如下：

<Steps>
  <Step>
打开 “项目设置 -> 数据库连接”。

<Background>

![CleanShot 2024-11-28 at 18.36.28@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/480151/image-preview)
</Background>

    </Step>
  <Step>
点击右上角的 “新建” 来创建数据库连接。
    </Step>
  <Step>
从可用选项中选择数据库类型，填写必要的连接信息，比如数据库地址、端口、数据库名、用户名和密码。推荐使用变量填入，完全以变量形式填入的数据库连接，可以保存在云端用以协同。
      
<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/504328/image-preview" style="width: 440px" />
</p>
</Background>


    </Step>
  <Step>
除了用户名密码的本地连接方式，你还可以通过 SSH 隧道建立更安全的连接，更好地保护数据传输。
      
<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/504330/image-preview" style="width: 440px" />
</p>

</Background>

  </Step>
  <Step>
点击 “保存”，这个连接就可以在前置和后置操作中使用了。
    </Step>
</Steps>

:::tip[]
Apifox 非常重视数据安全。数据库的地址、端口、用户名、密码和数据库名仅保存在本地，不会同步到云端。即使在同一团队中，成员之间也无法共享数据库连接信息，每位成员需要手动配置自己的数据库连接。
:::

:::tip[MySQL 使用提示]

目前最新的 mysql 模块对 MySQL8 的`caching_sha2_password`加密方式支持不够完善，而`caching_sha2_password`是默认的加密方式。

需要指定`mysql_native_password`模式修改 MySQL 账号密码，用其他工具连接 MySQL 后执行下面的 SQL 来修改对应账号的密码。

```SQL
ALTER USER 'username'@'%' IDENTIFIED WITH mysql_native_password BY '123456'
```

记得手动替换上面的用户名和密码。
:::

## 在不同环境中连接数据库

在多个环境 （如测试环境、生产环境等） 中工作时，通常需要配置不同的数据库。如果工作流程涉及数据库操作，那么这些操作也必须随着环境的变化而切换。

在这种情况下，你可以在 Apifox 的 “数据库连接” 设置中配置多个数据库连接。为每个环境设置好对应的数据库连接后，当你通过右上角的下拉菜单切换环境时，数据库查询将自动连接到对应环境的数据库。

<Background>
<p style="text-align: center">
    <img src="https://api.apifox.com/api/v1/projects/5097254/resources/480154/image-preview" style="width: 440px" />
</p>
</Background>

## 在脚本中连接数据库

在 Apifox 自定义脚本中，你可以用 JavaScript 连接数据库，执行 SQL 查询并操作结果。


<Steps>
  <Step title="配置数据库">
    请将以下配置替换为你自己的数据库信息：
```js
var dbConfig = {
    type: 'mysql',          // 数据库类型：mysql / postgresql / sqlserver 等
    host: '127.0.0.1',      // 数据库地址
    port: '3306',           // 端口号
    username: 'root',       // 用户名
    password: '123456',     // 密码
    database: 'test',       // 数据库名
}
```
  </Step>
  <Step title="执行 SQL 查询">
通过 `pm.dataSource(dbConfig).query` 执行 SQL 查询：

```javascript
// 假设你有一个环境变量 petId
var petId = pm.environment.get('petId');

pm.dataSource(dbConfig).query(
    `SELECT * FROM pets WHERE id = ${petId};`,
    (error, results) => {
        console.log('error', error);
        console.log('results', results);

        // 可以做断言
        pm.test("查询结果验证", function () {
            pm.expect(results[0].name).to.eql("示例宠物名");
        });

        // 保存结果到变量，供后续接口使用
        pm.environment.set('petName', results[0].name);
    }
);
```
  </Step>
  <Step title="发送接口请求">
    发送请求，检查结果是否符合预期。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/569926/image-preview)
</Background>

      
  </Step>
</Steps>




## 操作非关系型数据库（NoSQL）

MongoDB 操作请参考 [MongoDB 操作](https://docs.apifox.com/mongodb.md)。

Redis 操作请参考 [Redis 操作](https://docs.apifox.com/redis.md)。

## 在 Apifox CLI 中使用数据库操作

Apifox 支持用命令行工具（CLI）在任何平台上执行测试场景。用 CLI 可以实时从服务器获取测试场景配置并高效运行。

但是因为数据库操作是本地存储的，所以 CLI 无法动态获取你的数据库配置。

这种情况下，你需要把数据库操作导出为配置文件，放在运行 CLI 的机器上。详细了解 [Apifox CLI](https://docs.apifox.com/install-and-run-cli.md)。

## 常见问题


<Accordion title="我能在 Apifox 的一个数据库操作中组合多个 SQL 查询吗？" defaultOpen>
Apifox 中每个数据库操作只能执行一个 SQL 查询。如果要运行多个 SQL 查询，需要分成多个数据库操作来执行。
</Accordion>



