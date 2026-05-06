# Test Cases

Starting from Apidog version `2.7.29`, you can now add test cases directly on the endpoint details page.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361465/image-preview" />
</Background>

Each test case represents a set of request parameters for the endpoint. Users can organize and manage all test cases systematically, then run them with one click to complete testing for the current endpoint.

:::tip[Test Cases vs. Debug Cases]

- **Test cases**
  - **Purpose:** To verify whether the endpoint behaves as expected across different request scenarios, focusing on comprehensiveness.
  - **Covers a wide range of scenarios:** positive, negative, boundary, and security.
  - Usually less frequently modified or executed.

- **Debug cases**
  - **Purpose:** To quickly verify endpoint responses during development or troubleshooting, focusing on speed.
  - Generally limited to basic scenarios such as success and failure.
  - Often modified and run frequently.
:::

## Creating Test Cases

You can create test cases in several ways:

### 1. Manual Creation

In the **Test Cases** tab of the endpoint details page, click **+ Add Case** to manually create one.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361471/image-preview" />
</Background>

### 2. Import from Debug Cases

When adding a test case, you can choose **Import from Debug Cases** to copy or move the existing debug cases into test cases.

- **Copy**: Use this when you still need the debug case for quick validation but also want it as a test case.
- **Move**: Use this when the debug case is no longer frequently used for debugging and was primarily written for testing exceptions. This directly converts it into a test case, making migration quicker if test cases were originally created as debug cases.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361480/image-preview" />
</Background>

## Test Case Details

A test case contains the following information:

- **Group:** Organized by test purpose (positive, negative, boundary, etc.).
- **Case Name:** The name of the test case.
- **Request Parameters:** Path, Query, Header, and form-data Body parameters.
- **Request Body:** Supports RAW, JSON, XML, etc.
- **Pre/Post Processors**
- **Response Validation:** Enable/disable validation and specify response components to be validated.

> [!NOTE]
> Since test cases are less frequently updated, they must be manually synchronized with endpoint changes. For example, if a new field is added to the endpoint, you'll need to click **Update** in the test case to update it.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361483/image-preview" />
</Background>

Any edits to test case details must be saved by clicking **Save**. If there are unsaved changes, the system will prompt you.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361486/image-preview" />
</Background>

## Managing Test Cases

In the Test Cases tab, you can manage all created test cases. Use the search and filter features in the upper left corner to easily find the test cases you need. You can also use the group tab to quickly view test cases by group. For operations on specific test cases:

- **Single Test Case:** You can open a new tab to view, modify, and run a test case. Basic operations include copying, moving test case to other groups, copying the cURL of the test case, and deleting the test case.
- **Multiple Test Cases:** When you select multiple test cases in the list, action buttons will appear in the upper right corner, allowing you to batch-group, delete, and synchronize with endpoint updates.

## Running Test Cases

When viewing a test case, click the **Run** button to send a request with its parameters. The actual response will then be displayed.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361786/image-preview" />
</Background>

You can also use **Run All** or select multiple test cases from the list and run them together. The interface will show which cases are currently running and which have results.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361488/image-preview" />
</Background>

After a batch run, you can open a test case to view its execution results directly.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361489/image-preview" />
</Background>

## Test Reports

After running tests in bulk, you can check all historical reports in the **Test Reports** at the top right.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361491/image-preview" />
</Background>

Click a report to view detailed results, helping with issue tracing and analysis.

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361492/image-preview" />
</Background>

An overview of how test cases works:

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361499/image-preview" />
</Background>

## Best Practices for Single Endpoint Testing

Single endpoint testing usually involves two roles: backend developers and QA engineers.

- **Backend Developers:** Write and debug endpoint code.
- **QA Engineers:** Perform comprehensive API testing and identify issues.

With Apidog now supporting test cases for endpoints, the workflow can be more efficient:

- QA engineers can directly write and manage unit test cases within the endpoint documentation.
- Developers can use existing test cases to run tests, view results, and fix issues themselves — without waiting for QA engineer feedback or lengthy communication.

**Best Practice Workflow:**

<Background>
<img style="width: 460px;" src="https://api.apidog.com/api/v1/projects/544525/resources/361508/image-preview" />
</Background>

This workflow can improve collaborative efficiency:

1. Test cases can be written right after endpoint documentations are finalized, visible to all team members in Apidog.
2. Developers can test endpoints themselves after debugging—no need to wait for QA engineers.
3. Developers can fix issues directly based on test results—no extra tickets or handoffs required.
4. Clear test results make problem explanations straightforward, avoiding miscommunication.

