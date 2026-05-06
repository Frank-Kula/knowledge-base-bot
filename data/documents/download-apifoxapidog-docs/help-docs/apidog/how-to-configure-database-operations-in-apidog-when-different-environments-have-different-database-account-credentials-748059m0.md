# How to configure database operations in Apidog when different environments have different database account credentials?

When working with multiple environments such as testing and production environments, they often have different databases configured. If you are using database operations in your workflows, it implies that these operations need to switch along with the environment changes.

In such scenarios, you can configure multiple database connections under the "Database Connections" settings in Apidog. By setting up database connections for each environment, you can ensure that when switching between environments using the dropdown menu in the top right corner, the database queries will automatically be directed to the corresponding database connection associated with that environment. 

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/342824/image-preview" style="width: 640px" />
</p>
</Background>
