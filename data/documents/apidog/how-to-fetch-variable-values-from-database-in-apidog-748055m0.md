# How to fetch variable values from database in Apidog?

Apidog offers a unique feature: connecting to a database to retrieve data, setting it as a variable, and using it in requests. Here are the steps:

<Steps>
  <Step>
    In the **Run** tab (DESIGN Mode) or **Request** tab (DEBUG Mode), navigate to Post Processors.
  </Step>
  <Step>
    Hover over "Add PostProcessor" and select "Database operation".
      
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342780/image-preview)
  </Step>
  <Step>
   Name the database operation and set up the database connection. Learn more about Database connections.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342782/image-preview)
  </Step>
  <Step>
Enter the SQL command. The command supports using `{{variables}}` within it.

  </Step>
  <Step>
Set "Extract Result To Variable". JSONPath is supported.
  </Step>
  <Step>
Click Send to execute the request. You can view the database operation's results in the Console.

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/342783/image-preview)
  </Step>
</Steps>


:::highlight purple
Learn more about [Database operations](https://docs.apidog.com/database-operations-in-apidog-588469m0.md).
:::
