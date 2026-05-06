# How to get service base URL in custom script?


Apidog provides `pm.request.getBaseUrl()` to retrieve the base URL of the current endpoint.

It's recommended to use this method instead of `pm.environment.get('BASE_URL')`, as the latter might not return the correct base URL if the endpoint doesn't use the default server. 

For more details on services and base URLs, see [Environments & services](https://docs.apidog.com/environment-management-584758m0.md).

