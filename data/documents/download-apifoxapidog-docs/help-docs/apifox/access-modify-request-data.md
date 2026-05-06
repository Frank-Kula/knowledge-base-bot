# 脚本读取/修改接口请求信息

脚本读取/修改接口请求信息主要使用`pm.request`。

:::tip[]

- 只有在前置脚本里修改请求信息才是有效的，在后置脚本里修改无效。
- 通过脚本取出来的接口参数，如果参数包含变量，变量是不会替换成对应的值。如想要获取替换后的值，可使用`pm.variables.replaceIn`方法处理：
  ```js
  // pm.variables.replaceIn 处理参数里的变量
  var body = pm.variables.replaceIn(pm.request.body.raw);
  var jsonData = JSON.parse(body);
  ```

:::

## URL 相关信息

```js
// 获取 url 对象
var urlObj = pm.request.url;

// 获取完整接口请求 URL，包含 query 参数
var url = urlObj.toString();

// 获取协议（http 或 https）
var protocol = urlObj.protocol;

// 获取 端口
var port = urlObj.port;
```

## Header 参数


<Tabs>
  <Tab title="获取 Header 参数">
    ```js
    // 获取 Header 参数对象
    var headers = pm.request.headers;

    // 获取 key 为 field1 的 header 参数的值
    var field1 = headers.get("field1");

    // 以键值对象方式获取所有 header 参数
    var headersObject = headers.toObject();

    // 遍历整个 header
    headers.each((item) => {
      console.log(item.key); // 输出参数名
      console.log(item.value); // 输出参数值
    });
    ```
  </Tab>
  <Tab title="修改 Header 参数">
    ```js
    // 获取 Header 参数对象
    var headers = pm.request.headers;

    // 增加 header 参数
    headers.add({
      key: "field1",
      value: "value1",
    });

    // 修改 header 参数（如不存在则新增）
    headers.upsert({
      key: "field2",
      value: "value2",
    });
    ```
  </Tab>
</Tabs>


## Query 参数

<Tabs>
  <Tab title="获取 Query 参数">
    ```js
    // 获取 Query 参数对象
    var queryParams = pm.request.url.query;

    // 获取 key 为 field1 的 query 参数的值
    var field1 = queryParams.get("field1");

    // 以键值对象方式获取所有 query 参数
    var quertParamsObject = queryParams.toObject();

    // 遍历整个 query
    queryParams.each((item) => {
      console.log(item.key); // 输出参数名
      console.log(item.value); // 输出参数值
    });
```
  </Tab>
  <Tab title="修改 Query 参数">
    ```js
    // 获取 Query 参数对象
    var queryParams = pm.request.url.query;

    // 增加 query 参数
    queryParams.add({
      key: "field1",
      value: "value1",
    });

    // 修改 query 参数（如不存在则新增）
    queryParams.upsert({
      key: "field2",
      value: "value2",
    });
    ```
  </Tab>
</Tabs>



## Body 参数

Body 参数来自`pm.request.body`，它是一个`RequestBody` 实例。

> 参考：http://www.postmanlabs.com/postman-collection/RequestBody.html

:::tip[]

- 如需修改 Body 里的数据，推荐在 Body 里引用变量，然后在前置脚本里设置对应变量的值，即可达到修改的目的。
- Body 参数也支持直接修改，使用方式如下：

```js
var body = pm.request.body.toJSON();
console.log("body 对象", body);

var bodyStr = body.raw;
console.log("body 字符串", bodyStr);

var bodyJSON = JSON.parse(bodyStr);
bodyJSON.id = 100;
pm.request.body.update(JSON.stringify(bodyJSON, null, 2));
console.log("修改后 body", pm.request.body.toJSON());
```

:::

### Body 类型为 form-data

<Tabs>
  <Tab title="获取 form-data 信息">
    ```js
    // 当 body 类型为 form-data 时，从 pm.request.body.formdata 获取请求参数
    var formData = pm.request.body.formdata;

    // 获取 key 为 field1 的 form-data 参数的值
    var field1 = formData.get("field1");
    console.log(field1); // 控制台打印 field1

    // 以键值对象方式获取所有 formdata 参数
    var formdataObject = formData.toObject();
    console.log(formdataObject); // 控制台打印 formdataObject

    // 遍历整个 form-data 数据
    formData.each((item) => {
      console.log(item.key); // 控制台打印参数名
      console.log(item.value); // 控制台打印参数值
    });
    ```

  </Tab>
  <Tab title="修改 form-data 信息">
    ```js
    pm.request.body.update({
        mode: 'formdata',
        formdata: [{
            key: 'foo',
            value: 'bar'
        }]
    });
    ```
  </Tab>
</Tabs>


> 你可以使用该方法实现文件路径参数化。

### Body 类型为 x-www-form-urlencode

<Tabs>
  <Tab title="获取 x-www-form-urlencode 信息">
    ```js
    // 当 body 类型为 x-www-form-urlencode** 时，从 pm.request.body.urlencoded 获取请求参数
    var formData = pm.request.body.urlencoded;

    // 获取 key 为 field1 的 form-data 参数的值
    var field1 = formData.get("field1");

    // 以键值对象方式获取所有 formdata 参数
    var formdataObject = formData.toObject();

    // 遍历整个 form 数据
    formData.each((item) => {
      console.log(item.key); // 控制台打印参数名
      console.log(item.value); // 控制台打印参数值
    });
    ```

  </Tab>
  <Tab title="修改 x-www-form-urlencode 信息">
    ```js
    pm.request.body.update({
        mode: 'urlencoded',
        urlencoded: [{
            key: 'foo',
            value: 'bar'
        }]
    });
    ```
  </Tab>
</Tabs>



### Body 类型为 json

获取 json 信息

```js
// 当 body 类型为 json 时，从 pm.request.body.raw 获取请求参数

try {
  var jsonData = JSON.parse(pm.request.body.raw);
  console.log(jsonData); // 控制台打印参整个 json 数据
} catch (e) {
  console.log(e);
}
```

### Body 类型为 raw


<Tabs>
  <Tab title="获取 raw 信息">
    ```js
    // 当 body 类型为 raw 时，从 pm.request.body.raw 获取请求参数

    var raw = pm.request.body.raw;
    console.log(raw); // 控制台打印参整个 raw 数据
    ```
  </Tab>
  <Tab title="修改 raw 信息">
    ```js
    pm.request.body.update('Hello World!');
    ```
  </Tab>
</Tabs>


### Body 类型为 GraphQL

设置 GraphQL 信息

```js
pm.request.body.update({
    mode: 'graphql',
    graphql: {
        query: `
            query Square($ten: Int!) {
                square(n: $ten)
            }
        `,
        variables: { ten: 10 }
    }
});
```
