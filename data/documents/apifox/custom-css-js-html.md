# 自定义页面代码（ CSS / JS / HTML）

你可以在发布 API 文档时，自定义添加全局的 HTML、CSS 和 JavaScript 代码，实现页面的个性化样式调整与功能扩展。

该功能适用于以下场景：

- 嵌入第三方服务（如聊天机器人、AI 智能问答助手）

- 修改默认样式（如字体、颜色、背景）

- 添加额外的页面交互（如按钮、动态提示、快捷反馈）

合理使用这项功能，可以让文档更贴近你的品牌风格，也能增强用户的阅读与互动体验。

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/585311/image-preview)
</Background>


## CSS

通过添加自定义 CSS，你可以修改页面字体、隐藏元素、调整边距、改变颜色等等。

由于文档页面结构可能在后续迭代中发生调整，为了保证你的样式持续有效，建议遵循以下两条原则：

1. 使用保留的 CSS 变量
2. 使用保留的 CSS 类名

### 使用保留的 CSS 变量

Apifox 提供了一批以 `--g-` 开头的 CSS 变量，用于控制字体、颜色、背景等页面基础样式。这些变量在浅色或深色模式下都具备良好适配性，使用它们可以提升自定义样式的稳定性和可维护性。


<Accordion title="常见变量参考" defaultOpen={false}>
```css
/* 主题色。注意，这个变量是只读变量，在 CSS 里直接修改这个变量不会生效，如需修改需要到“个性化配置-外观设置-主题色”里修改 */
--g-color-primary: ;
    
/* 字体 */
--g-font-family: ;
    
/* 文字颜色*/
--g-text-color: ;
--g-text-color-active: ;
--g-text-color-dark: ; 
--g-text-color-hover: ;
--g-text-color-inverse: ;
--g-text-color-secondary: ;
--g-text-color-secondary-dark: ;
--g-text-color-sub: ; 
--g-text-color-tertiary: ;
:root[data-theme='dark']{
  /* 暗色模式*/
  ...
}
    
/* 背景图案*/
--g-background-image: ;
:root.dark{
  /* 暗色模式*/
  --g-background-image: ;
}
--g-background-repeat: ;
--g-background-attachment: ;
--g-background-position: ;
    
```
</Accordion>




> 示例：修改主文本颜色
>
> ```css
> :root {
>   --g-text-color: #222; /* 更深一点的灰色 */
> }
> ```

### 使用保留的 CSS 类名

如果你需要针对特定区域调整样式，可以使用 Apifox 预留的 `.g-` 前缀类名，这些类名相对稳定，不容易因 DOM 结构变化而失效。


<Accordion title="常见 CSS 类参考" defaultOpen={false}>

```css
/* Body */
.g-body

/* 品牌 Logo */
.g-brand
.g-logo
.g-logo-img
.g-title

/* 顶部导航 Header */
.g-header

/* 一级导航（顶部导航） */
.g-header-top-navbar
.g-header-top-navbar-left         /* 左侧导航容器 */
.g-header-top-navbar-left-item
.g-header-top-navbar-left-item-active
.g-header-top-navbar-right        /* 右侧导航容器 */
.g-header-top-navbar-right-item
.g-header-top-navbar-right-item-active

/* 二级导航 */
.g-header-secondly-navbar
.g-header-secondly-navbar-item

/* 三级导航（即使没有二级导航，仍用 tertiary 命名） */
.g-header-tertiary-navbar
.g-header-tertiary-navbar-item
.g-header-tertiary-navbar-item-active

/* 左侧目录树 Sidebar */
.g-sidebar                       /* 整个侧边栏容器 */
.g-sidebar-menu                  /* 菜单区域（包含所有目录项） */
.g-sidebar-item-category         /* 分组（例如文件夹目录名） */
.g-sidebar-item-list             /* 分组下的子项容器 */
.g-sidebar-item-link             /* 具体的目录链接项 */
.g-sidebar-item-link-active      /* 当前激活的目录链接 */

.g-sidebar-section               /* 自定义的额外区域（如文档说明） */
.g-sidebar-section-heading       /* 自定义区域的小标题 */

```
</Accordion>


> 示例：隐藏左侧目录栏
>
> ```css
> .g-sidebar {
>   display: none;
> }
> ```

### 查看页面结构和类名

除了上面提到的保留的 CSS 变量和类名，你也可以通过浏览器的开发者工具，查找你想修改的页面元素对应的 class 名称，然后写 CSS 来调整样式。

建议优先使用 `.g-` 开头的类名，这些是平台保留的，结构相对稳定，不容易失效。对于其他结构类名，请谨慎使用，避免产品升级后样式失效。

你可以在浏览器中打开已发布的文档站，使用开发者工具（开发者模式 / 控制台）查看页面结构和样式类名：

- **Mac**：按下 `Command + Option + I`或`fn + F12`

- **Windows**：按下 `Ctrl + Shift + I`或`fn + F12`或`F12`

打开后，点击左上角的 “元素选择工具”（鼠标图标），再点击页面上的任意区域，即可查看该区域对应的 HTML 标签和类名。

你也可以使用搜索功能（`Cmd/Ctrl + F`）定位某个类名。

<Background>

![CleanShot 2025-07-09 at 17.55.28@2x.png](https://api.apifox.com/api/v1/projects/5097254/resources/544059/image-preview)
</Background>


## JavaScript

自定义 JavaScript 适用于嵌入第三方服务的需求（如 AI 助手、客服面板等），请注意 Apifox 的自定义 JavaScript 区域不支持直接写 `<script>` 和 `<style>` 标签。你需要将这些内容改写为纯 JavaScript 实现，例如：


<Container>
  
<Columns>
  <Column>
    **❌ 原始写法**
      
     ---
      
     
```js
<script>
    window.difyChatbotConfig = { token: 'xxx' };
</script>
<script src="https://udify.app/embed.min.js" defer></script>
<style>
  #dify-chatbot-bubble-button {
    background-color: #1C64F2 !important;
  }
</style>

```
      
  </Column>
    
  <Column>
    **✅ 适配后的纯 JS 写法**
      
     ---   
     
    ```js
    window.difyChatbotConfig = {
      token: 'xxx'
    };

    var script = document.createElement('script');
    script.src = 'https://udify.app/embed.min.js';
    script.defer = true;
    document.head.appendChild(script);

    var style = document.createElement('style');
    style.textContent = `
      #dify-chatbot-bubble-button {
        background-color: #1C64F2 !important;
      }
    `;
    document.head.appendChild(style);

   ```

  </Column>
</Columns>

</Container>

如果你想嵌入第三方脚本或样式，但不确定怎么改写为纯 JS 格式，可以复制下面的 Prompt 提示词粘贴到 AI 工具（如 DeepSeek）中，让 AI 帮你自动转换：


```html
我正在使用 Apifox 的“自定义 JavaScript”功能，要求只能填写纯 JavaScript 代码，不能包含任何 <script> 或 <style> 标签。

请将以下代码片段转换为纯 JavaScript 写法，要求如下：
1. 将 <script> 标签改写为 document.createElement('script') 动态创建方式；
2. 将 <style> 内容注入到新建的 style 标签中并插入 head；
3. 所有 DOM 操作请使用标准方法（如 createElement、appendChild），不能使用 document.write；
4. 如果原代码使用了 window.addEventListener('DOMContentLoaded'...)，请替换为 'load' 事件，更稳定；
5. 最终生成的 JavaScript 要能直接在浏览器中运行，不要附带解释说明。

以下是我要转换的原始代码：
---
（请将你的原始代码粘贴在这里）
---

```


:::tip[]
- 出于安全考虑，自定义 JavaScript 仅在使用 [自定义域名](https://docs.apifox.com/custom-domain.md) 访问文档站时生效。

- 如果通过 Apifox 提供的默认文档地址访问（如 `https://xxx.apifox.cn/` 开头），自定义 JS 将不会被加载执行。


- 请确保代码本身可靠，避免影响正常加载或破坏页面结构。

- 如果需要等待页面加载完成后再执行代码，请使用`load`而不是`DOMContentLoaded`，例如：

    ```js
    window.addEventListener('load', function () {
      // 所有资源加载完成后执行
    });
    ```
:::


### 示例：点击按钮展开/收起 iframe 对话窗口


<Accordion title='“点击按钮展开/收起 iframe 对话窗口” 脚本' defaultOpen={false}>

```js
window.addEventListener('load', () => {
  // 创建按钮容器
  const buttonWrapper = document.createElement('div');
  buttonWrapper.style.position = 'fixed';
  buttonWrapper.style.bottom = '24px';
  buttonWrapper.style.right = '24px';
  buttonWrapper.style.zIndex = '9999';

  // 创建按钮
  const button = document.createElement('button');
  button.textContent = '💬 问问我';
  button.style.padding = '8px 12px';
  button.style.background = 'rgb(178 145 249)';
  button.style.color = '#fff';
  button.style.border = 'none';
  button.style.borderRadius = '6px';
  button.style.cursor = 'pointer';

  buttonWrapper.appendChild(button);
  document.body.appendChild(buttonWrapper);

  // 创建 iframe 容器
  const iframeWrapper = document.createElement('div');
  iframeWrapper.style.display = 'none';
  iframeWrapper.style.position = 'fixed';
  iframeWrapper.style.bottom = '72px';
  iframeWrapper.style.right = '24px';
  iframeWrapper.style.width = '360px';
  iframeWrapper.style.height = '680px';
  iframeWrapper.style.background = '#fff';
  iframeWrapper.style.borderRadius = '8px';
  iframeWrapper.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
  iframeWrapper.style.zIndex = '9999';
  iframeWrapper.style.overflow = 'hidden';

  // 创建 iframe
  const iframe = document.createElement('iframe');
  iframe.src = 'https://apifox.com/'; // 替换成你自己的地址
  iframe.style.width = '100%';
  iframe.style.height = '100%';
  iframe.style.border = 'none';

  iframeWrapper.appendChild(iframe);
  document.body.appendChild(iframeWrapper);

  // 点击按钮切换显示隐藏
  button.addEventListener('click', () => {
    iframeWrapper.style.display =
      iframeWrapper.style.display === 'none' ? 'block' : 'none';
  });
});

```
</Accordion>

**使用方法：**

<Steps>
  <Step>
    将代码粘贴到 Apifox 自定义 JS 区域
  </Step>
  <Step>
    访问你的自定义域名文档站
  </Step>
  <Step>
    右下角会出现一个按钮，点击后弹出对话窗口（iframe）
  </Step>
    <Step>
    替换 `iframe.src` 为你自己的 AI 服务地址，如：
        
    ```js
    iframe.src = 'https://udify.app/chat?token=xxx'
    ```
    
    这里用 Apifox 官网地址来演示：
    
<Background>

![02-apifox-custom-js-css-html.gif](https://api.apifox.com/api/v1/projects/5097254/resources/544830/image-preview)
</Background>

        
  </Step>
</Steps>


### 示例：嵌入 Dify 聊天应用

<Accordion title='“嵌入 Dify 聊天应用” 脚本' defaultOpen={false}>
    
**❌ 转换前（不可直接嵌入）：**

```js
<script>
 window.difyChatbotConfig = {
  token: 'fSuVCBsxxxxxxx',
  systemVariables: {
    // user_id: 'YOU CAN DEFINE USER ID HERE',
    // conversation_id: 'YOU CAN DEFINE CONVERSATION ID HERE, IT MUST BE A VALID UUID',
  },
  userVariables: {
    // avatar_url: 'YOU CAN DEFINE USER AVATAR URL HERE',
    // name: 'YOU CAN DEFINE USER NAME HERE',
  },
 }
</script>
<script
 src="https://udify.app/embed.min.js"
 id="fSuVCBsxxxxxxx"
 defer>
</script>
<style>
  #dify-chatbot-bubble-button {
    background-color: #1C64F2 !important;
  }
  #dify-chatbot-bubble-window {
    width: 24rem !important;
    height: 40rem !important;
  }
</style>
```

    
**✅ 转换后（可嵌入）：**
    
```js
// 设置全局配置
window.difyChatbotConfig = {
  token: 'fSuVCBsxxxxxxx', // 需要替换
  systemVariables: {
    // user_id: 'YOUR_USER_ID',
    // conversation_id: 'VALID_UUID',
  },
  userVariables: {
    // avatar_url: 'https://example.com/avatar.png',
    // name: 'User Name',
  }
};

// 插入 embed.min.js 脚本
var script = document.createElement('script');
script.src = 'https://udify.app/embed.min.js';
script.defer = true;
script.id = 'fSuVCBsxxxxxxx'; // 需要替换
document.head.appendChild(script);

// 注入样式（等价于 <style> 标签）
var style = document.createElement('style');
style.textContent = `
  #dify-chatbot-bubble-button {
    background-color: #1C64F2 !important;
  }
  #dify-chatbot-bubble-window {
    width: 24rem !important;
    height: 40rem !important;
  }
`;
document.head.appendChild(style);

```

</Accordion>

    
**使用方法：**

<Steps>
  <Step>
    在 Dify 中创建一个应用，应用发布后选择“嵌入网站”，将代码复制下来，并用上文提到的 Prompt 提示词转换成纯 JavaScript 格式。
      
<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/544803/image-preview)
</Background>

      
    将转换后的代码粘贴到 Apifox 自定义 JS 区域。
  </Step>
  <Step>
    访问你的自定义域名文档站
  </Step>
  <Step>
    右下角会出现一个按钮，点击后弹出对话窗口。
    
<Background>

![01-apifox-custom-js-css-html.gif](https://api.apifox.com/api/v1/projects/5097254/resources/544822/image-preview)
</Background>

      
  </Step>

</Steps>


## HTML

即将推出...

## 常见问题


<Accordion title="自定义 JS 没有生效？" defaultOpen>

请确认是否使用了 [自定义域名](https://docs.apifox.com/custom-domain.md) 访问文档。只有在绑定并使用你自己的域名时，JavaScript 代码才会被加载执行。
</Accordion>

<Accordion title="为什么推荐使用 load 而不是 DOMContentLoaded" defaultOpen={false}>
在自定义 JavaScript 中，你可能会用如下方式来等待页面加载完成后再执行代码：

```js
window.addEventListener('DOMContentLoaded', function () {
  // 页面结构加载完毕，执行逻辑
});
```

但在 Apifox 中，这种写法 **可能不会生效**，因为自定义 JS 的注入时机通常早于页面结构完成，`DOMContentLoaded` 事件可能已经触发过了，导致这段代码不会执行。

为确保代码在正确的时机运行，我们推荐使用：

```js
window.addEventListener('load', function () {
  // 所有资源加载完成后执行
});
```

`load` 事件会在页面包括图片、iframe、样式等所有资源加载完毕之后才触发，因此在 Apifox 的文档加载流程中更加稳定可靠。

</Accordion>
