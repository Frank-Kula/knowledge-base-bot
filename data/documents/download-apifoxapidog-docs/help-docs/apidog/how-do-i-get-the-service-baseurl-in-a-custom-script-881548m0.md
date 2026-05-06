# How do I get the service baseURL in a custom script?

Apidog provides the `pm.request.getBaseUrl()` method to get the baseURL of the current endpoint.

It is recommended to use the above instead of `pm.environment.get('BASE_URL')` , as the latter may not be able to return the correct baseURL if the endpoint is not using the default service.

In addition, you can `pm.environment.get("BASE_URLS")` get the baseURL of all services through .
For more details about services and baseURLs, see [Environments & services](https://docs.apidog.com/environment-management-584758m0.md)
