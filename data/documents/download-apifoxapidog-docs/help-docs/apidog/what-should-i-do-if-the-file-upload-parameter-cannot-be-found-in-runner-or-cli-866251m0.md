# What should I do if the file upload parameter cannot be found in Runner or CLI?

Apidog only stores the local file path, not the file itself. Therefore, when running tests using Runner or CLI on different machines, you may encounter errors where the file cannot be found.

To resolve this:
1. Upload the file to the Runner/CLI machine where the test scenario is running.
2. In Apidog, open the corresponding test step, and use the "Batch Edit" to replace the file path parameter value with  with the file path in Runner/CLI machine(e.g. `/opt/apidog/runner/yourfilename.jpg`), or replace it with a variable and then pass the file path through the variable value.


<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352026/image-preview)
    
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352027/image-preview)
</Background>


For specific usage, please refer to the [uploading-files-in-cli](https://docs.apidog.com/apidog-cli-options-609656m0#uploading-files-in-cli).


