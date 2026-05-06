# How to auto - group endpoints on Swagger/OpenAPI import?

When importing a Swagger/OpenAPI file in Apidog, the grouping of APIs is automatically completed based on the endpoint's tags. The system will set the first tag of the endpoint as the folder of the endpoint. 
If there is a slash ("/") in the tag, then the "/" will be used as the delimiter to distinguish the parent and child directory structures.
For example, when you set the endpoint tag as ["Orders/User Orders/Sub Folder"], after completing the import endpoint, this endpoint will automatically be located in a hierarchical directory like Orders->User Orders->Sub Folder. 
In addition, if you expect the existing endpoint directory after the import to be exactly the same as the directory in the import source when importing the Swagger file, you need to turn on the "And update endpoint folder" switch. 

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/354407/image-preview)
</Background>


