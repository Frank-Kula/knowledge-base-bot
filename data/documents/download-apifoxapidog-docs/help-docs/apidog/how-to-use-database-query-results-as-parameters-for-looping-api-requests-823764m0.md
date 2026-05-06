# How to use database query results as parameters for looping API requests?

Apidog supports using database query results as parameters to loop through API requests. You can follow these steps:

<Steps>
  <Step title="Add a Database Operation step">
    In your test scenario, add a "Database Operation" step. Execute your SQL query and extract the result into a variable (e.g., `id`). Ensure your SQL query returns an array-formatted result.
<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/350016/image-preview)
</Background>
  </Step>
  <Step title="Add a Foreach Loop step">
    In your test scenario, add a "Foreach Loop" step. Set the "Array to iterate over" to the previously extracted variable, e.g., `{{id}}`. The current element of the iteration will be automatically stored in the `$item` variable.
<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/350014/image-preview)
</Background>
  </Step>
  <Step title="Add an API Request step">
    Under the Foreach Loop step, add the API request you want to run repeatedly. In the request parameters, use `{{$.step id.element}}` to reference the values from the loop variable. For example, if your database query result id is an array of objects containing a userId field and the step id of the Foreach loop step is 2, you can use `{{$.2.element}}` as the value for your API parameter.
<Background>
  ![](https://api.apidog.com/api/v1/projects/544525/resources/350018/image-preview)
</Background>
  </Step>
</Steps>




