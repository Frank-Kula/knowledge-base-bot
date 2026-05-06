# 断言示例

后置脚本是在`请求发送完成后`执行的代码片段。主要用来`断言`请求返回的结果是否正确、将请求返回的结果数据写入环境变量等。

## 断言请求返回的结果是否正确

```javascript
// pm.response.to.have 示例
pm.test('返回结果状态码为 200', function() {
  pm.response.to.have.status(200);
});

// pm.expect() 示例
pm.test('当前为正式环境', function() {
  pm.expect(pm.environment.get('env')).to.equal('production');
});

// response assertions 示例
pm.test('返回结果没有错误', function() {
  pm.response.to.not.be.error;
  pm.response.to.have.jsonBody('');
  pm.response.to.not.have.jsonBody('error');
});

// pm.response.to.be* 示例
pm.test('返回结果没有错', function() {
  // assert that the status code is 200
  pm.response.to.be.ok; // info, success, redirection, clientError,  serverError, are other variants
  // assert that the response has a valid JSON body
  pm.response.to.be.withBody;
  pm.response.to.be.json; // this assertion also checks if a body  exists, so the above check is not needed
});
```

## 将请求返回的结果数据写入环境变量

```javascript
// 获取 JSON 格式的请求返回数据
var jsonData = pm.response.json();

// 将 jsonData.token 的值写入环境变量
pm.environment.set('token', jsonData.token);
```

## 检查 response body 是否包含某个字符串

```js
pm.test('Body matches string', function() {
  pm.expect(pm.response.text()).to.include('string_you_want_to_search');
});
```

## 检查 response body 是否包含等于字符串

```js
pm.test('Body is correct', function() {
  pm.response.to.have.body('response_body_string');
});
```

## 检查 json 值

```js
pm.test('Your test name', function() {
  var jsonData = pm.response.json();
  pm.expect(jsonData.value).to.eql(100);
});
```

## 检查 header 是否有设置 Content-Type

```js
pm.test('Content-Type header is present', function() {
  pm.response.to.have.header('Content-Type');
});
```

## 检查请求响应耗时是否低于 200 毫秒

```js
pm.test('Response time is less than 200ms', function() {
  pm.expect(pm.response.responseTime).to.be.below(200);
});
```

## 检查 HTTP 状态码是否为 200

```js
pm.test('Status code is 200', function() {
  pm.response.to.have.status(200);
});
```

## 检查 HTTP 状态码名称是否包含某个字符串

```js
pm.test('Status code name has string', function() {
  pm.response.to.have.status('Created');
});
```

## 是否正确的 POST 请求状态码

```js
pm.test('Successful POST request', function() {
  pm.expect(pm.response.code).to.be.oneOf([201, 202]);
});
```

## 断言库的使用示例

Apifox 内置了`ChaiJS`作为断言库，以下是常用的断言测试脚本示例，但并非全部示例，更多用法请参考文档： [ChaiJS expect BDD library](http://chaijs.com/api/bdd/)

## 断言目标字符串包含另一个字符串

```javascript
pm.test('断言目标字符串包含另一个字符串', function() {
  pm.expect('foobar').to.have.string('bar');
});
```

## 断言目标严格等于某值

断言目标严格等于(`===`)某值。

```javascript
const TEN = 10;
pm.test('Check if number is equal to 10', function() {
  pm.expect(TEN).to.equal(10);
});
```

如果设置了`deep`标记，则断言目标深度等于`value`

```javascript
pm.test('断言目标深度等于提供的 JSON', function() {
  pm.expect(data1).to.deep.equal(data2);
});
```

**注意：**

1. 设置`deep`标记，然后使用`equal`和`property`断言。该标记可以让其后的断言不是比较对象本身，而是递归比较对象的键值对。

## 断言深度等于某值

相当于`deep.equal(value)`的简写。

```javascript
pm.test('Check response value', function() {
  var jsonData = pm.response.json();
  pm.expect(jsonData.value).to.eql(100);
});
```

## 断言当前环境

```javascript
pm.test('Check if environment is production', function() {
  pm.expect(pm.environment.get('env')).to.equal('production');
});
```

## 断言数据类型

```javascript
pm.test('Check if target is string', function() {
  pm.expect('Postman').to.be.a('string');
});
pm.test('Check if target is an object', function() {
  pm.expect({ a: 1 }).to.be.an('object');
});
pm.test('Check if target is undefined', function() {
  pm.expect(undefined).to.be.an('undefined');
});
```

**注意：**

1. 推荐在做其他断言前，先使用 `.a` 方法检查模板的数据类型。
2. 数据类型是大小写敏感的。

## 断言是否为空

```javascript
pm.test('Check if array is empty', function() {
  pm.expect([]).to.be.empty;
});
pm.test('Check if string is empty', function() {
  pm.expect('').to.be.empty;
});
```

还可以使用 `.a`方法检查数据类型后，在断言是否为空。

示例:

```javascript
pm.test('Check if array is empty', function() {
  pm.expect([]).to.be.an('array').that.is.empty;
});
```

## 断言目标对象的键值

```javascript
pm.test('Check if object contains all provided keys', function() {
  pm.expect({ a: 1, b: 2 }).to.have.all.keys('a', 'b');
});
pm.test('Checking if object contains any ONE of the keys', function() {
  pm.expect({ a: 1, b: 2 }).to.have.any.keys('a', 'b');
});
pm.test('Check if object contains any NONE of the provided keys', function() {
  pm.expect({ a: 1, b: 2 }).to.not.have.any.keys('c', 'd');
});
```

## 断言目标对象是否包含指定属性

```javascript
pm.test('Check if object contains the property', function() {
  pm.expect({ a: 1 }).to.have.property('a');
});
```

**注意:**

1. 目标对象必须是 `object`、`set`、`array` 或 `map`。
2. 如果 `.keys` 前面没有 `.all` 或 `.any`，则默认为 `.all`。
3. 由于只有部分数据类型的目标对象可使用 `.keys` 方法，建议先用 `.a`方法断言数据类型。

```javascript
pm.test('Check if object contains all the keys', function() {
  pm.expect({ a: 1, b: 2 })
    .to.be.an('object')
    .that.has.all.keys('a', 'b');
});
```

## 断言目标对象的 length

```javascript
pm.test('Check the length of the target', function() {
  pm.expect('foo').to.have.lengthOf(3);
});
pm.test('Check the size of the target', function() {
  pm.expect([1, 2, 3]).to.have.lengthOf(2);
});
```

## 断言目标对象的成员 (members)

```javascript
pm.test('Check if the target has same members as the array set', function() {
  pm.expect([1, 2, 3]).to.have.members([2, 1, 3]);
});
```

**注意:**

1. 默认情况下， `.members` 使用严格比较。
2. members 的顺序不会影响结果。

## 断言目标对象包含指定 item

```javascript
pm.test('Check if the target array includes the number provided', function() {
  pm.expect([1, 2, 3]).to.include(2);
});
pm.test(
  'Check if the target object includes the properties provided',
  function() {
    pm.expect({ a: 1, b: 2, c: 3 }).to.include({ a: 1, b: 2 });
  },
);
```

**注意：** 建议在 `.include` 前先使用 `.a` 方法判断数据类型。

**示例：**

```javascript
pm.test(
  'Check if the target is an array that includes the number specified',
  function() {
    pm.expect([1, 2, 3])
      .to.be.an('array')
      .that.includes(2);
  },
);
```

