# 数据库连接

你可以在项目设置中，配置数据库的连接信息。配置完成后，在接口调试、测试时，前后置操作中可以添加[数据库操作](https://docs.apifox.com/database.md)并引用此处配置的数据库连接信息，从而实现读写数据库数据。


<Background>

![CleanShot 2025-03-18 at 10.05.38@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/504306/image-preview)
</Background>

Apifox 免费版支持连接以下类型的数据库：
- [MySQL](https://docs.apifox.com/mysql.md)
- SQL Server：支持 SQL Server 2014 以上版本
- Oracle（连接 Oracle 数据库需要单独安装 [Oracle Client](https://docs.apifox.com/oracle.md)）
- Db2
- PostgreSQL
- ClickHouse
- MongoDB

升级到商业标准版后，可以额外连接 Redis；升级到商业专业版后，可以额外连接达梦数据库。

## 配置数据库连接


在 Apifox 中设置数据库连接的步骤如下：

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
从可用选项中选择数据库类型，填写必要的连接信息，比如数据库地址、端口、数据库名、用户名和密码。推荐使用**变量**填入，完全以变量形式填入的数据库连接，可以保存在云端用以协同。
:::highlight red 📌
**重要！** 使用变量来配置数据库链接，需注意[**数据安全问题**](#保存机制与数据安全)。
:::
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

## 使用数据库连接

可以在接口请求的前后置操作中，添加 “数据库操作” 来引用数据库连接进行使用，添加之后可以在 “数据库操作” 中指定一个数据库连接。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/504339/image-preview)
</Background>


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
   为数据库操作命名并设置数据库连接，需要确保选择的 “数据库连接” 实际数据已被正确配置。[了解更多](#注意事项)


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/480064/image-preview)
</Background>

  </Step>
  <Step>
输入 SQL 命令。命令中支持使用变量，如 `{{variables}}`。

  </Step>
  <Step>
设置 “提取结果到变量”，支持使用 JSONPath，开启 “控制台打印结果” 开关。
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

## 注意事项

在发送请求执行数据库操作前，需确认所配置的数据库连接信息已正确保存：

- 如果是保存在云端、使用了变量的数据库连接，请在相关变量的 “本地值” 中设置好实际的数据库地址、用户名、密码等连接内容，或通过 set 变量方式设置实际连接内容。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/504343/image-preview)
</Background>

- 如果是保存在本地、使用了固定文本的数据库连接，请在 “项目设置 -> 数据库连接” 中，填入固定文本的实际数据库地址、用户名、密码等连接内容。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/504347/image-preview)
</Background>

- 如果需要通过 **CLI** 运行带数据库连接的测试场景，则[在此了解详细注意事项](https://docs.apifox.com/%E5%AE%89%E8%A3%85%E5%92%8C%E8%BF%90%E8%A1%8C-cli-5637752m0#%E8%BF%90%E8%A1%8C%E5%9C%A8%E7%BA%BF%E6%95%B0%E6%8D%AE)；
- 如果需要通过 **Runner** 运行带数据库连接的测试场景，则[在此了解详细注意事项](https://docs.apifox.com/%E9%80%9A%E7%94%A8-runner-5714000m0#%E5%9C%A8-runner-%E4%B8%AD%E4%BF%9D%E5%AD%98%E6%96%87%E4%BB%B6)。

## 保存机制与数据安全

目前 Apifox 的数据库连接保存方式有两种：

- **保存于 Apifox 云端**。通过在数据库连接中，完全使用变量方式填写，则此条数据库连接的内容会以变量形式保存于 Apifox 云端服务器中。

- **保存于当前配置者本地**。通过在数据库连接中，完全使用固定文本方式填写，则此条数据库连接的内容会以明文形式保存于当前配置者的本地文件内。

关于此两种保存机制的区别：

<table>
  <thead>
    <tr>
      <th>保存机制</th>
      <th>保存方法</th>
      <th>优点</th>
      <th>缺点</th>
    </tr>
  </thead>
  <tbody>
    <tr>
        <td><span style="display: inline-block;width:80px;">云端</span></td>
      <td><span style="display: inline-block;width:120px;">配置时使用变量</span></td>
      <td>
          <div style="width:270px;">
          1. 更方便与其他成员协同使用
          2. 通过 CI、Runner 等方式运行测试场景时可以通过变量 set 数据库连接内容，而非维护专门的本地文件
          </div>
      </td>
        
      <td>
         <Icon icon="material-outline-warning" style="color: #ffce21;" /> 当在变量远程值中使用明文时，数据库名、密码等数据会被明文传输至 Apifox 云端服务器，有数据安全风险（使用变量本地值则仍然保存在本地，无风险）。建议使用 [Vault 变量](https://docs.apifox.com/5831220m0)来避免数据安全风险
        
      </td>
    </tr>
    <tr>
      <td>本地</td>
      <td>配置时使用固定文本</td>
      <td>本地独立保存，没有数据安全风险</td>
      <td>
         <div style="width:360px;">
          1. 不好协同，每个成员均要在数据库连接中自行配置数据
          2. 通过 CI、Runner 等方式运行测试场景时需要通过维护专门的数据库连接本地文件
          </div>
      </td>
    </tr>
  </tbody>
</table>


:::highlight yellow 💡
为了获得良好使用体验与数据安全的平衡，Apifox 推荐以云端保存方式维护数据库连接，并使用 Vault 变量确保数据安全。**极其不建议**在数据库连接的相关**变量远程值中使用明文**，可能造成数据安全风险。
:::

## 了解更多

- [MySQL 数据库操作](https://docs.apifox.com/mysql.md)
- [MongoDB 数据库操作](https://docs.apifox.com/mongodb.md)
- [Redis 数据库操作](https://docs.apifox.com/redis.md)
- [Oracle 数据库操作](https://docs.apifox.com/oracle.md)
