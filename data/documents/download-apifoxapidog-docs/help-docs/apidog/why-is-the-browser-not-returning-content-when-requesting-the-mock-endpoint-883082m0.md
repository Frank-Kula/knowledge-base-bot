# Why Is the Browser Not Returning Content When Requesting the Mock endpoint?

When the browser requests that the mock endpoint does not return content, please confirm the following:

1. Path matching: Ensure that the URL path you are visiting is exactly the same as the endpoint path defined in the document.

2. Method matching: Confirm that the request method (such as GET, POST, etc.) is consistent with the endpoint method defined in the document.
The browser address bar only supports GET requests, and non-GET requests cannot be made directly. If you need to test a POST request, you can use Apidog to initiate a request.

3. Schemas Configuration: Check that the endpoint of the mock is correctly configured for the expected matching responses.

If all of the above are confirmed, but the problem is still not resolved, you can provide more information (such as screenshots of interface definitions, mock settings in the project settings, etc.) to technical support for further troubleshooting.


:::tip[]
For more information about mocking, see [Mock data automatically](https://docs.apidog.com/smart-mock-618190m0.md)
:::




