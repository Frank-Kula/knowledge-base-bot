# Why does Apidog report an error when the response is too large?

Apidog's front-end may run into issues related to Node.js string length limits when handling oversized interface responses. Node.js uses the V8 engine, which has a limit on the length of a single string, usually around 337MB. When the response size exceeds this limit, it can lead to out-of-memory or string processing errors.
