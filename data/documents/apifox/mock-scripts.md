# Mock 脚本

有时，你需要根据请求参数返回对应的 Mock 响应，或者维护不同字段之间的逻辑关系。

例如：
- 当请求用户 ID 为 1001 的信息时，返回的数据应包含该 ID，且值为 1001。
- 当 Mock 数据包含开始时间和结束时间等相关字段时，结束时间应晚于开始时间。

这些逻辑关系可以通过 Mock 脚本来实现。

## 工作原理

Mock 脚本的基本实现原理如下：

1. 使用智能 Mock 或其他 Mock 功能生成初始响应数据，这些数据可能还未满足所有约束条件。
2. 使用 Mock 脚本访问 `$$.mockResponse` 对象或 `$$.mockRequest` 对象。
3. 从这两个对象中获取数据，并编写 JavaScript 实现所需的逻辑。
4. 使用 `$$.mockResponse.setBody` 方法，将修改后的数据写入响应内容。
5. Mock 引擎返回最终的响应数据。

## 使用 Mock 脚本

<Steps>
  <Step>
    点击 Mock 选项卡，定位到 Mock 脚本区域
  </Step>
  <Step>
     打开脚本开关来启用它
  </Step>
  <Step>
    编写脚本并保存
  </Step>
</Steps>


<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/481054/image-preview)
</Background>



## 脚本参考

### Mock 脚本示例

```js
// 从智能 Mock 获取 Mock 数据
var responseJson = $$.mockResponse.json();

// 修改 responseJson 中的分页数据
// 1. 把 page 设置为请求参数中的 page
responseJson.page = $$.mockRequest.getParam("page");

// 2. 把 total 设置为 120
responseJson.total = 120;

// 3. 把修改后的 json 写入 $$.mockResponse
$$.mockResponse.setBody(responseJson);
```
这个脚本做了这些事：
1. 先获取一个初始的 Mock 响应（自动生成的）
2. 然后修改这个响应：
   - 把 `page` 值设置为请求中的值
   - 设置一个固定的 `total` 值
3. 最后用这些修改更新 Mock 响应


:::warning[]
Mock 自定义脚本，不能用于前置/后置脚本中。
:::


### `$$.mockRequest` 对象

`$$.mockRequest` 对象代表 Mock 脚本中的传入请求，类似于 Postman 的 [`pm.request`](https://docs.apifox.com/postman-script-api#pmrequest) 对象，但它提供了一些额外功能。

1. **`getParam(key: string)` 方法**：获取请求中的参数，无论参数位于 *（Query、Body 等）* 哪个位置。

2. **访问 Cookies**：允许你获取请求中的 cookie 值。

脚本参考：
```javascript
// 获取请求参数
var userId = $$.mockRequest.getParam("userId");

// 获取请求头
var headerUserId = $$.mockRequest.headers.get("userId");

// 获取请求 cookies
var cookieUserId = $$.mockRequest.cookies.get("userId");

// 获取请求体中的 JSON 数据
var requestJsonData = $$.mockRequest.body.toJSON();

// 获取请求体中的字符串数据
var requestStringData = $$.mockRequest.body.toString();

// 获取请求体中的 form-data
var formDataUserId = $$.mockRequest.formdata.get("userId");

// 获取请求体中的 urlencoded 数据
var urlencodedUserId = $$.mockRequest.urlencoded.get("userId");
```

### $$.mockResponse 对象

`$$.mockResponse` 是 Apifox 提供的一个 Mock 响应对象，用于动态控制接口返回的数据。它不仅可以获取响应信息，还可以针对每个字段灵活设置想要的返回数据。

它类似于 Postman 的 [`pm.response`](https://docs.apifox.com/postman-script-api#pmresponse) 对象，但提供了更多控制 Mock 响应的方法。

- **`setBody(body: any)` 方法**：设置响应体。
- **`setCode(code: number)` 方法**：设置响应的 HTTP 状态码。
- **`setDelay(duration: number)` 方法**：为 Mock 响应添加延迟，模拟网络延迟。


脚本参考：

```javascript
// 获取系统自动生成的 JSON 格式响应数据
var responseJsonData = $$.mockResponse.json();

// 设置接口返回 JSON 格式 Body
$$.mockResponse.setBody({ id: "1", name: "Apple" });

// 设置接口返回 string 格式 Body
$$.mockResponse.setBody("Hello World!");

// 设置接口返回的 HTTP 状态码
$$.mockResponse.setCode(200);

// 设置 Mock 响应延时，单位为毫秒
$$.mockResponse.setDelay(3000);

// 获取 HTTP 状态码
var statusCode = $$.mockResponse.code;

// 获取 HTTP header
var myHeader = $$.mockResponse.headers.get("X-My-Header");

// 删除当前请求里 key 为 X-My-Header 的 header
$$.mockResponse.headers.remove("X-My-Header")

// 给当前请求添加一个 key 为 X-My-Header 的 header。
$$.mockResponse.headers.add({ key: "X-My-Header", value: "hello"});

// upsert key 为 X-My-Header 的 header（如不存在则新增，如已存在则修改）。
$$.mockResponse.headers.upsert({ key: "X-My-Header", value: "hello"})
```




### 其它示例

模拟分页：

```js
var MockJs = require('mockjs');

// 总数据
var total = 120;

// 当前页（从请求参数中获取）
// var pageNumber = $$.mockRequest.getParam('pageNumber');
var pageNumber = 1;

// 页容量（从请求参数中获取）
// var pageSize = $$.mockRequest.getParam('pageSize');
var pageSize = 10;

// 设置分页数据
function pageList(pageNumber, pageSize, total) {
  const list = [];
  // 计算起始索引
  const startIndex = (pageNumber - 1) * pageSize;

  for (let i = startIndex; i < startIndex + pageSize && i < total; i++) {
    const id = i + 1;
    // 生成姓名
    const name = MockJs.mock('@cname');
    // 引用姓名作为图片名
    const photoUrls = MockJs.mock(`@image('200x100', @color, ${name})`);
    list.push({
      id,
      name,
      photoUrls,
      status: MockJs.Random.boolean()
    });
  }

  return {
    code: 0,
    message: 'ok',
    data: {
      list,
      pageNumber,
      "pageSize": list.length,
      total,
    },
  };
}

// 返回分页数据
$$.mockResponse.setBody(pageList(pageNumber, pageSize, total));
```

<Background>

![image.png](https://api.apifox.com/api/v1/projects/5097254/resources/525159/image-preview)
</Background>

更多示例参考：
```js
var MockJs = require('mockjs');

// 获取“智能 Mock”自动生成的 json
var responseJson = $$.mockResponse.json();

// 根据请求参数（包括 query、body、path）修改响应值
if ($$.mockRequest.getParam('id') === '123') {
  responseJson.data = null;
  responseJson.code = 400104;
  responseJson.errorMessage = '数据不存在';
  $$.mockResponse.setBody(responseJson);
  $$.mockResponse.setCode(404);
}

// 根据请求的 header 修改响应值
if (!$$.mockRequest.headers.get('token')) {
  responseJson.data = null;
  responseJson.code = 400103;
  responseJson.errorMessage = '没有权限';
  $$.mockResponse.setBody(responseJson);
  $$.mockResponse.setCode(403);
}

// 根据请求的 cookie 修改响应值
if ($$.mockRequest.cookies.get('projectId') === '123') {
  var idList = [1, 2, 3, 4, 5, 6, 7, 8];
  $$.mockResponse.setBody({
    code: 0,
    data: idList.map(function (id) {
      return {
        id: id,
        name: MockJs.mock('@cname'),
        email: MockJs.mock('@email'),
        city: MockJs.mock('@city'),
      };
    }),
  });
}

// 设置返回延迟
$$.mockResponse.setDelay(500);

// 添加 header
$$.mockResponse.headers.add({
  key: 'X-Token',
  value: '<token>',
});

// 添加或修改 header
$$.mockResponse.headers.upsert({
  key: 'X-Token',
  value: '<token>',
});

```

## 常见问题


<Accordion title="如何在 Mock 脚本中使用 Apifox 变量？" defaultOpen>
Mock 脚本**不能使用变量**。这是因为变量是 Apifox 客户端的功能，但 Mock 引擎不是客户端的一部分，所以它无法引用客户端中的变量。
</Accordion>

<Accordion title="如何在 Mock 脚本中使用 log 语句输出到控制台？" defaultOpen={false} >
Mock 脚本不提供日志功能。这是因为控制台是 Apifox 客户端的功能，但 Mock 引擎不是客户端的一部分，所以它无法向客户端输出日志。
</Accordion>

<Accordion title="为什么我不能在 Mock 脚本中使用 pm 对象？" defaultOpen={false} >
Mock 脚本在 Mock 服务器上执行，而前置和后置脚本是在发送请求的 Apifox 客户端上执行。这是完全不同的环境，所以脚本语法不能在它们之间共享。
</Accordion>

