# Why Aren't Test Steps Automatically Synchronized When the API Use Case Changes?

1. If the step is imported from an endpoint use case - and choose how to `copy`
When the use case of an endpoint is changed, the steps are not changed, and there is no correlation between the two.

2. If the step is to import from an endpoint use case - and select the "Reference" method
Any changes in the endpoint use case will be synchronized to the test step content, and vice versa step changes will also be synchronized to the endpoint use case.

Therefore, if you need the test steps to be in full sync with the endpoint use case, choose to import the steps by `reference`.

<Background>
 
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352621/image-preview)
</Background>


