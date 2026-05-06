# Custom Protocol API

Custom Protocol API is used to manage APIs with custom protocols.

With this feature, you can create and maintain API documentation for different types of protocols (such as Thrift, UDP, Kafka, RabbitMQ, RocketMQ, etc.) in a unified way, all managed centrally within Apidog.

Just like HTTP API documentation, custom protocol API docs also support a folder tree, search and filter options, bulk management, and online sharing — making it easier for teams to collaborate and share externally.

## Creating Custom Protocol API

<Steps>
  <Step>
  Above the folder tree, hover over the **+** icon, then select **New Other Protocol APIs** and click **Other Custom Protocol API**.
      
<Background>
![Creating custom protocol API](https://api.apidog.com/api/v1/projects/544525/resources/365351/image-preview)
</Background>
  </Step>
    
  <Step>
  Select a protocol type (options include Thrift, Kafka, etc., or click **Manage Protocol** to add a custom protocol).
      
    <Background>
    ![Selecting protocol type](https://api.apidog.com/api/v1/projects/544525/resources/362640/image-preview)
    </Background>

    There are default templates available for each protocol.
    <Background>
    ![Manage Protocol](https://api.apidog.com/api/v1/projects/544525/resources/362641/image-preview)

    ![Protocol templates](https://api.apidog.com/api/v1/projects/544525/resources/362642/image-preview)
    </Background>

      
  </Step>
  <Step>
   Fill in the following details:

   - **URI**: The unique ID for the endpoint, used to distinguish it from others (similar to a URL path for HTTP endpoints).
   - **Endpoint Name**: The name of the endpoint.
   - **Basic Information**: Status, maintainers, tags, and other details.
   - **Documentation Details**: Allowing editing descriptions, usage instructions, examples, and more flexibly.
      
<Background>
![Filling in endpoint details](https://api.apidog.com/api/v1/projects/544525/resources/362646/image-preview)
</Background>
  </Step>    
    
  <Step>
    After saving, you'll see the endpoint documentation for the selected protocol created.
          
<Background>
![Custom protocol endpoint documentation](https://api.apidog.com/api/v1/projects/544525/resources/362647/image-preview)
</Background>
  </Step>
</Steps>

## Sharing Custom Protocol API Docs

Custom protocol API docs also support online sharing, making collaboration and external presentation easier.

You can copy a collaboration link to share within the project.

<Background>
![Copying collaboration link](https://api.apidog.com/api/v1/projects/544525/resources/362652/image-preview)
</Background>

You can also go to **Publish Docs** > **Quick Share**, select which endpoints to include, and choose whether to share custom protocol API docs.

<Background>
![Quick share settings](https://api.apidog.com/api/v1/projects/544525/resources/362653/image-preview)
</Background>

