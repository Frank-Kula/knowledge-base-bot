# Custom CSS, JavaScript, HTML

When publishing your API documentation, you can add custom global HTML, CSS, and JavaScript to personalize page styles and extend functionality.

This feature is useful for:

- Embedding third-party services (e.g., chatbots, AI assistants)

- Modifying default styles (e.g., font, color, background)

- Adding interactive elements (e.g., buttons, popups, quick feedback)

By using this feature wisely, your documentation can better reflect your brand identity and improve the user experience.

## CSS

With custom CSS, you can change fonts, hide elements, adjust margins, alter colors, and more.

Since the documentation structure may change in future updates, we recommend following these two principles to ensure your styles remain effective:

1. Use reserved CSS variables
2. Use reserved CSS class names

### Use reserved CSS variables

Apidog provides a set of CSS variables prefixed with `--g-` to control basic page styles such as font, color, and background. These variables adapt well to both light and dark modes, making your styles more stable and maintainable.


<Accordion title="Common Variables Reference" defaultOpen={false}>
```css
/* Theme color. Note that this variable is read-only. Modifying this variable directly in CSS will not take effect. If you need to modify it, you need to modify it in "Customize-Appearance-Accent Color". */
--g-color-primary: ;
    
/* Fonts */
--g-font-family: ;
    
/* Text colors*/
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
  /* Dark mode*/
  ...
}
    
/* Background*/
--g-background-image: ;
:root.dark{
  /* Dark mode*/
  --g-background-image: ;
}
--g-background-repeat: ;
--g-background-attachment: ;
--g-background-position: ;
    
```
</Accordion>

> Example: Change main text color
>
> ```css
> :root {
>   --g-text-color: #222; /* Darker gray */
> }
> ```

### Use reserved CSS class names

To target specific areas for styling, use Apidog’s reserved class names with the `.g-` prefix, which are relatively stable and less likely to break due to DOM changes.

<Accordion title="Common CSS Class Reference" defaultOpen={false}>

```css
/* Body */
.g-body

/* Brand Logo */
.g-brand
.g-logo
.g-logo-img
.g-title

/* Top Navigation Header */
.g-header

/* Primary Navigation (Top) */
.g-header-top-navbar
.g-header-top-navbar-left         /* Left navigation container */
.g-header-top-navbar-left-item
.g-header-top-navbar-left-item-active
.g-header-top-navbar-right        /* Right navigation container */
.g-header-top-navbar-right-item
.g-header-top-navbar-right-item-active

/* Secondary Navigation */
.g-header-secondly-navbar
.g-header-secondly-navbar-item

/* Tertiary Navigation (Even if there is no secondary navigation, still use tertiary)*/
.g-header-tertiary-navbar
.g-header-tertiary-navbar-item
.g-header-tertiary-navbar-item-active

/* Left Sidebar */
.g-sidebar                       /* The entire sidebar container */
.g-sidebar-menu                  /* Menu area (including all directory items) */
.g-sidebar-item-category         /* Grouping (such as folder directory name) */
.g-sidebar-item-list             /* Sub-item container under the group */
.g-sidebar-item-link             /* Specific directory link item */
.g-sidebar-item-link-active      /* Currently activated directory link*/

.g-sidebar-section               /* Customized additional area (such as document description)*/
.g-sidebar-section-heading       /* Subheading of custom area */

```
</Accordion>


> Example: Hide the left sidebar
>
> ```css
> .g-sidebar {
>   display: none;
> }
> ```

### Inspecting page structure and class names

In addition to the reserved CSS variables and class names mentioned above, you can also use the browser's developer tools to find the class name corresponding to the page element you want to modify, and then write CSS to adjust the style.

It is recommended to use class names starting with `.g-` first. These are reserved by the platform, have a relatively stable structure, and are not easy to fail. For other structural class names, please use them with caution to avoid style failure after product upgrades.

You can open the published doc site in the browser and use the developer tools (developer mode/console) to view the page structure and style class names:

- **Mac**: `Command + Option + I`or`fn + F12`

- **Windows**: `Ctrl + Shift + I`or`fn + F12`or`F12`

Upon opening, click the "Element Selector" (the mouse icon), and then click any area on the page to view the HTML tags and class names corresponding to that area.

You can also use the search function (`Cmd/Ctrl + F`) to locate a class name.

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358429/image-preview)
</Background>


## JavaScript

Custom JavaScript is used to embed third-party services like AI assistants or support widgets. Note: Apidog's custom JavaScript field does not support `<script>` or `<style>` tags. You must convert these into pure JavaScript. For example:

<Container>
  
<Columns>
  <Column>
    **❌ Original(not supported)**
      
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
    **✅ Converted to Pure JavaScript**
      
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

If you want to embed a third-party script or style but are not sure how to rewrite it into pure JS format, you can copy the prompt below and paste it into an AI tool (such as Claude) to let AI help you convert it automatically:

```
I'm using Apidog's "Custom JavaScript" feature, which only allows pure JavaScript (no <script> or <style> tags).

Please convert the following code to pure JavaScript. Here are the requirements:
1. Rewrite the <script> tag to document.createElement('script') dynamic creation method;
2. Inject the <style> content into the newly created style tag and insert the head;
3. Please use standard methods (such as createElement, appendChild) for all DOM operations, and do not use document.write;
4. If the original code uses window.addEventListener('DOMContentLoaded'...), please replace it with the 'load' event, which is more stable;
5. The final generated JavaScript should be able to run directly in the browser without any explanation.

Original code:
---
(paste your code here)
---

```

:::tip[]
- For security, custom JavaScript only works when accessing docs via [Custom domain](https://docs.apidog.com/custom-domain-631339m0.md).

- If you access it through the default documentation address provided by Apidog (such as starting with `https://xxx.apidog.io/`), the custom JS will not be loaded and executed. 

- Please ensure that the code itself is reliable to avoid affecting normal loading or destroying the page structure.

- If you need to wait for the page to load before executing the code, use `load` instead of `DOMContentLoaded`, for example:

    ```js
    window.addEventListener('load', function () {
      // Code to run after all resources are loaded
    });
    ```
:::


### Example: Click the button to expand/collapse the iframe dialog


<Accordion title='Script for "Click the button to expand/collapse the iframe dialog"' defaultOpen={false}>

```js
window.addEventListener('load', () => {
  // Create button container
  const buttonWrapper = document.createElement('div');
  buttonWrapper.style.position = 'fixed';
  buttonWrapper.style.bottom = '24px';
  buttonWrapper.style.right = '24px';
  buttonWrapper.style.zIndex = '9999';

  // Create button
  const button = document.createElement('button');
  button.textContent = '💬 Ask me';
  button.style.padding = '8px 12px';
  button.style.background = 'rgb(178 145 249)';
  button.style.color = '#fff';
  button.style.border = 'none';
  button.style.borderRadius = '6px';
  button.style.cursor = 'pointer';

  buttonWrapper.appendChild(button);
  document.body.appendChild(buttonWrapper);

  // Create iframe container
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

  // Create iframe
  const iframe = document.createElement('iframe');
  iframe.src = 'https://apidog.com/'; // Replace with your own address
  iframe.style.width = '100%';
  iframe.style.height = '100%';
  iframe.style.border = 'none';

  iframeWrapper.appendChild(iframe);
  document.body.appendChild(iframeWrapper);

  // Click the button to switch between display and hide
  button.addEventListener('click', () => {
    iframeWrapper.style.display =
      iframeWrapper.style.display === 'none' ? 'block' : 'none';
  });
});

```
</Accordion>

**How to use:**

<Steps>
  <Step>
   Paste the code into Apidog's "Custom JavaScript" area.
  </Step>
  <Step>
   Visit doc sites via your custom domain
  </Step>
  <Step>
   A button appears at the bottom-right corner; click to open the chat iframe.
  </Step>
    <Step>
   Replace `iframe.src` with your AI service, e.g.:
        
    ```js
    iframe.src = 'https://udify.app/chat?token=xxx'
    ```
    
<Background>
![Custom CSS and JavaScript](https://assets.apidog.com/uploads/help/2025/07/11/ts4mf-7u.gif)
</Background>
        
  </Step>
</Steps>


### Example: Embedding Chatbase widget

<Accordion title='Script for "Embedding Chatbase Chat Widget"' defaultOpen={false}>
    
**❌ Before converted to pure JavaScript(invalid):**

```js
<script>
(function () {
  if (
    !window.chatbase ||
    window.chatbase("getState") !== "initialized"
  ) {
    window.chatbase = (...arguments) => {
      if (!window.chatbase.q) {
        window.chatbase.q = [];
      }
      window.chatbase.q.push(arguments);
    };

    window.chatbase = new Proxy(window.chatbase, {
      get(target, prop) {
        if (prop === "q") {
          return target.q;
        }
        return (...args) => target(prop, ...args);
      }
    });
  }

  const onLoad = function () {
    const script = document.createElement("script");
    script.src = "https://www.chatbase.co/embed.min.js";
    script.id = "POCAgi1vQOYcdxxxxxx";
    script.domain = "www.chatbase.co";
    document.body.appendChild(script);
  };

  if (document.readyState === "complete") {
    onLoad();
  } else {
    window.addEventListener("load", onLoad);
  }
})();
</script>
```

    
**✅ After converted to pure JavaScript(valid):**
    
```js
(function () {
  if (
    !window.chatbase ||
    window.chatbase("getState") !== "initialized"
  ) {
    window.chatbase = (...arguments) => {
      if (!window.chatbase.q) {
        window.chatbase.q = [];
      }
      window.chatbase.q.push(arguments);
    };

    window.chatbase = new Proxy(window.chatbase, {
      get(target, prop) {
        if (prop === "q") {
          return target.q;
        }
        return (...args) => target(prop, ...args);
      }
    });
  }

  const onLoad = function () {
    const script = document.createElement("script");
    script.src = "https://www.chatbase.co/embed.min.js";
    script.id = "POCAgi1vQOYcdxxxxxx";
    script.domain = "www.chatbase.co";
    document.body.appendChild(script);
  };

  if (document.readyState === "complete") {
    onLoad();
  } else {
    window.addEventListener("load", onLoad);
  }
})();
```

</Accordion>

    
**How to use:**

<Steps>
  <Step>
  Create a Chatbase app, get the embed code, convert it to pure JS using the prompt above.
      
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358487/image-preview)
</Background>
 Paste the converted code into the Apidog's Custom JS section.
  </Step>
  <Step>
 Visit the doc sites via your custom domain.
  </Step>
  <Step>
 A button will appear at the bottom-right corner. Click it to open a dialog window.    
<Background>
![Custom CSS and JavaScript](https://assets.apidog.com/uploads/help/2025/07/11/ts4mf-7u.gif)
</Background>

  </Step>

</Steps>


## HTML

Coming soon...

## FAQs


<Accordion title="Custom JS not working?" defaultOpen>
Make sure you're visiting the documentation via a [custom domain](https://docs.apidog.com/custom-domain-631339m0.md). Custom JavaScript is only executed when using a bound custom domain. 
</Accordion>

<Accordion title="Why use 'load' instead of 'DOMContentLoaded'?" defaultOpen={false}>
In custom JavaScript, you might use the following method to run code after the page has finished loading:

```js
window.addEventListener('DOMContentLoaded', function () {
  // Run code after the DOM is fully loaded
});
```
    
However, in Apidog, this approach **may not work**. That’s because custom JavaScript is often injected before the page structure is fully built, meaning the `DOMContentLoaded` event may have already fired—causing your code to be skipped.

To ensure your code runs at the right time, we recommend using:

```js
window.addEventListener('load', function () {
  // Run code after all resources are fully loaded
});
```
The `load` event fires only after all resources (images, iframes, styles, etc.) are completely loaded, making it more stable and reliable within Apidog’s documentation loading process.

</Accordion>
