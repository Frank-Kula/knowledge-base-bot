# 导入 cURL

使用诸如 Chrome、Charles 或 Fiddler 等抓包工具，来捕获和记录网页流量。抓取的数据可以导出为 `cURL` 格式，方便分析或重复使用。


## 使用抓包工具

### Chrome

<Steps>
  <Step>
按下 Ctrl+Shift+I（Windows/Linux）或 Cmd+Option+I（Mac）打开开发者工具。
  </Step>
  <Step>
    切换到 “Network” 标签页。
  </Step>
  <Step>
    刷新网页，开始抓取网络流量。
  </Step>
  <Step>
    找到对应接口请求，鼠标右键单击 “Copy -> Copy as cURL”。
      <Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468027/image-preview)
</Background>
  </Step>
</Steps>


### Charles

找到对应接口进行抓包，鼠标右键单击 “Copy cURL Request”，如下图所示。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468028/image-preview)
</Background>


### Fiddler

找到对应接口进行抓包，点击左上角菜单 “File -> Export Sessions -> Selected Sessions”，选项第一个默认 `cURL script`，点击`Next`即可保存为`.bat`文件，文件编辑工具打开该`.bat` 文件并复制内容。有关于该工具的详细使用教程请参考[《Fiddler 抓包》](https://cloud.tencent.com/developer/article/1656688)。

## 导入 cURL 数据


<Steps>
  <Step>
    鼠标移到左侧搜索框旁边的 `+` 号按钮，在下拉列表里点击`导入 cURL 数据`，也可使用 [快捷键](https://docs.apifox.com/keyboard-shortcuts.md) `Ctrl(⌘) + I`。
<Background>
![CleanShot 2024-09-29 at 10.39.16@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/468160/image-preview)
</Background>

  </Step>
  <Step>
    在打开的窗口中，粘贴从前面抓包数据里复制的 `cURL` 格式数据。
      
<Background>
 
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468163/image-preview)
</Background>

  </Step>
  <Step>
    点击确定按钮，可以看到抓包的数据已复制到如下 “快捷请求” 界面。
      
<Background>
![CleanShot 2024-09-29 at 10.48.45@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/468165/image-preview)
</Background>

  </Step>
    <Step>
    快捷调试窗口可以直接调试接口，可以将 “快捷请求” 保存为接口。
        <Background>
![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468166/image-preview)
</Background>
  </Step>

  <Step>
  除了上述提到的导入方法，你也可以将 cURL 命令直接粘贴到地址栏上，Apifox 会自动将其解析。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/468172/image-preview)
</Background>
  </Step>
</Steps>







