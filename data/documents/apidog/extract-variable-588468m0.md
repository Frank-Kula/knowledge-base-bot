# Extract Variable

Apidog allows you to visually extract values from API responses and save them as variables for use in subsequent requests.

## How to Extract Variables

<Steps>
  <Step>
    **Add Extract Variable Processor**
    
    In the **Post Processors** section of your request, hover over **+ Add** and select **Extract Variable**.
    
    <Tabs>
      <Tab title="Design-first Mode">
        <Background>
          ![Post Processors Design Mode](https://api.apidog.com/api/v1/projects/544525/resources/352194/image-preview)
        </Background>
      </Tab>
      <Tab title="Request-first Mode">
        <Background>
          ![Post Processors Request Mode](https://api.apidog.com/api/v1/projects/544525/resources/352193/image-preview)
        </Background>
      </Tab>
    </Tabs>
  </Step>
  <Step>
    **Configure Extraction Settings**
    
    *   **Variable Name**: Define the name of the variable to store.
    *   **Scope**: Choose where the variable will be accessible (Local, Environment, or Global).
    *   **Source**: Select where to extract data from (e.g., Response JSON, Header, Cookie).
  </Step>
  <Step>
    **Define Extraction Rule**
    
    For JSON or XML responses, use JSONPath or XPath to target specific data.
    
    <Background>
      ![Configure Extraction](https://api.apidog.com/api/v1/projects/544525/resources/342756/image-preview)
    </Background>
  </Step>
  <Step>
    **Execute and Verify**
    
    Click **Send**. The variable will be updated, and you can view the extraction log in the **Console**.
    
    <Background>
      ![Extraction Log](https://api.apidog.com/api/v1/projects/544525/resources/342758/image-preview)
    </Background>
  </Step>
</Steps>

## Quick Extraction from Response
You can quickly create extraction rules directly from the response panel:
1.  Hover over a field in the response.
2.  Click **Extract Variable**.
3.  The rule will be automatically populated in the Post Processors.

<Background>
  ![Quick Extract from Response](https://api.apidog.com/api/v1/projects/544525/resources/348242/image-preview)
</Background>

## Supported Extraction Sources

| Source | Description | Method |
| :--- | :--- | :--- |
| **Response JSON** | Extract data from JSON bodies. | JSONPath |
| **Response XML** | Extract data from XML bodies. | XPath |
| **Response Text** | Extract text from raw responses. | Regular Expressions (Regex) |
| **Response Header** | Extract specific header values. | Header Name |
| **Response Cookie** | Extract specific cookie values. | Cookie Name |
| **Response Time** | Store the request duration. | N/A |

## JSONPath Extraction Tool

To help you construct correct JSONPath expressions, Apidog provides a visual extraction tool:

1.  Click the <Icon icon="ph-bold-arrow-square-out"/> icon next to the JSONPath input field.
    <Background>
    ![Open JSONPath Tool](https://api.apidog.com/api/v1/projects/544525/resources/342819/image-preview)
    </Background>

2.  Enter your expression. The tool shows the JSON response on the left and the extraction result on the right.
    
    <Background>
      ![JSONPath Tool Interface](https://api.apidog.com/api/v1/projects/544525/resources/342817/image-preview)
    </Background>

:::tip[Handling Arrays]
Elements with wildcards (e.g., `books[*]`) return an array. To extract a single value without brackets, enable **Continue extracting** and specify the array index in the tool.
:::

