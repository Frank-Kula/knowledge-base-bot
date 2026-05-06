# How to resolve DB2 database connection errors on Windows?

If you encounter the error `Error: The specified module could not be found.` When connecting to a DB2 database in Apidog, it's usually due to missing environment variables. You can resolve this by configuring the following environment variables:

1. Configure the PATH environment variable:
Add `<Apidog Installation Directory>\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\bin` to the PATH environment variable. For example, if Apidog is installed in `D:\software\Apidog`, you need to add `D:\software\Apidog\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\bin` to the PATH.

2. Configure the LIB environment variable:
Create a new LIB environment variable and set its value to `<Apidog Installation Directory>\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\lib`. For example, if Apidog is installed in `D:\software\Apidog`, the value of LIB should be `D:\software\Apidog\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\lib`.

Example:
```js
SET PATH=D:\software\Apidog\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\bin
SET LIB=D:\software\Apidog\resources\app.asar.unpacked\node_modules\ibm_db\installer\clidriver\lib
```
After configuration, please restart Apidog and try connecting to the DB2 database again.
