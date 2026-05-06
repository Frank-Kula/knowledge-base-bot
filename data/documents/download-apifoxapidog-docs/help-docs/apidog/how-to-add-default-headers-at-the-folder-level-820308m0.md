# How to add default headers at the folder level?

Apidog doesn't directly support adding headers in folder settings. 

However, you can achieve this using pre-request scripts at the folder setting. This allows all requests within that folder to inherit these headers.

For example, to add a custom header "X-Custom-Header":

```javascript
pm.request.headers.add({
    key: 'X-Custom-Header',
    value: 'Example Value',
});
```

See [Pre-request Scripts](https://docs.apidog.com/pre-processor-scripts-593607m0) for more information on how to use them.

