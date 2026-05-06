# Why am I getting a "socket hang up" error when sending a request?

A "socket hang up" error indicates a broken connection. Apidog isn't receiving any response or is receiving an incomplete response. 

This can be caused by several factors:

1. **Server-side issues**: 
For example, a breakpoint set in the development environment code that prevents a response from being returned.
Troubleshooting: Try requesting a known working API, such as https://httpbin.org/get. If this request is successful, the issue lies with your target API server.

2. **Client-side timeout configuration**: 
Apidog's timeout setting might be too short, causing the request to terminate before the server can respond.
Troubleshooting: Increase the request timeout in Apidog's settings.

3. **Client-side proxy issues**: 
Your proxy server might be malfunctioning or incorrectly configured, leading to connection interruptions.
Troubleshooting: Try disabling Apidog's proxy settings or switching to a different proxy server.

4. **Large response data**: 
The server might be returning a large amount of data, causing the connection to break.
Troubleshooting: Communicate with the server-side developers to see if the response data can be compressed (e.g. using gzip compression).
