# What should I do if the endpoint parameter is an upload file and cannot be found in Runner or CLI?

Apidog only saves the local path of the file, not the file itself. As a result, when running tests using Runner or CLI on different machines, you may get an error that the file cannot be found.

Solution(s):

1. Upload the file to the server where the test scenario is run

2. Open the corresponding test step in Apidog, replace the file path parameter with the real path on the machine through the batch operation of the parameter, or replace it with a variable and then pass the file path through the variable value.

For details, refer to File Upload in the CLI. [Installing and running Apidog CLI](https://docs.apidog.com/installing-and-running-apidog-cli-605135m0.md)
