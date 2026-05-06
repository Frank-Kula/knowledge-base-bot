# 导入 apiDoc


支持导入 apiDoc 中的 `api_data.json` 或 `api_data.js` 文件，有关于文本格式详情说明请参考[项目地址](https://apidocjs.com)。

## 导出 apiDoc 数据


<Steps>
  <Step>
    本地安装 node 环境，使用 `0.29.0` 版本的 `apidoc`，进入源代码文件所在目录，运行 `npx apidoc@0.29.0 -i src -o dist` 命令。
  </Step>
  <Step>
    `src` 是接口的源代码文件，`dist` 是 apidoc 命令编译后生成的文件，`dist` 下面的 `api_data.js` 和 `api_data.json` 文件就是需导入至 Apifox 的接口文件。
      
<Background>
  <img src="https://api.apifox.com/api/v1/projects/5097254/resources/468213/image-preview" width="300px" />

</Background>

  </Step>

</Steps>




## 导入 apiDoc 数据

打开 Apifox 中的 “项目设置” 面板，点击 “导入数据 -> apiDoc”，上传`api_data.js` 或 `api_data.json` 文件。

<Background>
![CleanShot 2024-09-29 at 12.27.29@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/468214/image-preview)
</Background>


