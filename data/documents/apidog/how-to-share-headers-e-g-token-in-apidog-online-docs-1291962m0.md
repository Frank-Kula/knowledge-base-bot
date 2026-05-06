# How to Share Headers (e.g., Token) in Apidog Online Docs?

**I have to manually enter the same header each time I use “Try It” to test an API. Is there a way to share it automatically?**

Yes. It is recommended to use *variables* to share headers across API requests. Here are two common approaches:

### Method 1: Use a variable directly in the API’s header

Set the header like this in your API definition:

```js
Authorization: Bearer {{ACCESS_TOKEN}}
```

When using the **“Try It”** feature in the online docs, users only need to enter the `ACCESS_TOKEN` value once at the top. All APIs that reference `{{ACCESS_TOKEN}}` will automatically fill in the value—no need to enter it repeatedly.

<Background>

![apidog-7-24.gif](https://api.apidog.com/api/v1/projects/544525/resources/359022/image-preview)
</Background>



### Method 2: Define a global header params using a variable


<Steps>
  <Step>
    Go to **Environment Management → Global Params**
  </Step>
  <Step>
    Add a header-type param, for example:

   ```js
   Name: Authorization  
   Type: string
   Default Value: Bearer {{ACCESS_TOKEN}}
   ```
   
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359024/image-preview)
</Background>

  </Step>
  <Step>
    APIs in the project will use this global param by default. You can also choose to enable or disable it for specific APIs.
      
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359023/image-preview)
</Background>

  </Step>
    <Step>
    The online docs will automatically inherit the variable value, allowing multiple APIs to share it.
        
<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/359025/image-preview)
</Background>

  </Step>
</Steps>

Whether you define the variable directly in the API’s header or reference it through global params, as long as the same variable name (e.g., `{{ACCESS_TOKEN}}`) is used, you only need to enter it once in the online docs. It will then be shared across all relevant requests—greatly improving the testing experience.

