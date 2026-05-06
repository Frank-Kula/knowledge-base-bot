# Mock Priority Sequence

Apidog's default mock method is Smart mock, which automatically generates data based on response specifications. However, you can configure the mock engine to prioritize response examples when available.

## Configuration

To change the default mock priority:

<Steps>
  <Step>
    Navigate to **Project Settings** → **Feature Settings** → **Mock Settings**
  </Step>
  <Step>
    Change the **Default mock method** to your preferred option
    <Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/343626/image-preview" style="width: 640px" />
</Background>
  </Step>
</Steps>

## Mock Priority Options

### Smart Mock First (Default)

This is the default setting for the "Default mock method."

**Priority Sequence:**
```
Mock Expectation > Smart Mock
```

| Priority | Method | When Used |
|----------|---------|-----------|
| 1 | **Mock Expectation** | If a matching expectation exists |
| 2 | **Smart Mock** | For all other requests |

### Response Example First

When set to "Response example first," the priority changes to favor predefined examples.

**Priority Sequence:**
```
Mock Expectation > Response Example > Smart Mock
```

| Priority | Method | When Used |
|----------|---------|-----------|
| 1 | **Mock Expectation** | If a matching expectation exists |
| 2 | **Response Example** | If a response example is defined |
| 3 | **Smart Mock** | Fallback for endpoints without examples |

:::info[Fallback Behavior]
For endpoints without a specified response example, Smart mock serves as the fallback, ensuring requests always receive a response.
:::

## Key Considerations

:::tip[]
Regardless of which priority sequence you choose, **mock expectations always take first priority** when they are configured and conditions are met.
:::

