# Send a request and save as an endpoint

In Apidog, you can first send a request and then directly save this request as an API specification.


<Steps>
  <Step>
    In Apidog, click "New Request".
<Background>

![CleanShot 2025-11-05 at 16.58.41@2x.png](https://api.apidog.com/api/v1/projects/544525/resources/365347/image-preview)
</Background>
  </Step>
  <Step>
    Paste the following URL into the address bar:  `https://mock.apidog.com/m1/710637-685828-default/category/1`
      
<Background>      
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352131/image-preview)
</Background>
  </Step>
   <Step>
    Send the request and receive the response.
<Background>      
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352132/image-preview)
</Background>
  </Step>
  <Step>
    Click "Save as endpoint" to save this request as an endpoint. 
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352133/image-preview)
</Background>
  </Step>
   <Step>
       Switch to the "Preview" tab to see the endpoint spec.
<Background>
       ![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352134/image-preview)
</Background>
:::tip[]
If your interface does not match the image above, please switch to `Request-first Mode`.
    
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/352135/image-preview)
:::
      The actual sent request and the response become the endpoint's example, and the schema will be automatically parsed and generated. This is the most convenient method for generating an API spec.
  </Step>
</Steps>


:::tip[]
Note that the endpoint spec generated in this way can recognize **Query Params** in a REST API, but it **cannot** recognize **Path Params**. For example, in the above case, the correct request URL spec should be `/category/{id}`, where `{id}` was not recognized because it was an integer `1` in the actual request. You will need to manually change it to `{id}` in the path of the endpoint spec.
:::

<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/add-an-assertion-645440m0">
    Add an assertion
  </Card>
</CardGroup>
