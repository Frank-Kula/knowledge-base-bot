# How to Automatically Group Endpoints When Importing Swagger/OpenAPI into Apidog?


When importing a Swagger/OpenAPI file into Apidog, the endpoint structure is organized based on the `tags` defined for each endpoint. Specifically, the first value in the `tags` array determines the folder where the endpoint will be placed.

If the tag contains a slash (`/`), Apidog interprets it as a path separator and automatically creates a nested folder structure.

**Example:**  
For a tag such as `["Orders/User Orders/Sub Folder"]`, the endpoint will be organized under:  

**Orders → User Orders → Sub Folder**

If no tags are specified, the endpoint will be imported into the root **folder** of the project.

Additionally, if you want to retain the original folder structure from the source file, make sure to enable the **"Update Endpoint Folder Structure"** option during the import process.

