# Creating Test Scenarios

This guide explains how to create test scenarios that execute multiple API requests sequentially, with data passing between requests. Test scenarios are essential for testing complex workflows where the output of one request serves as input for subsequent requests.

## Prerequisites

Before you begin, ensure you have:
- Basic understanding of API requests in Apidog
- At least two API endpoints configured in your project
- Familiarity with JSON data structures

## Step-by-Step Guide

### Step 1: Create a New Test Scenario

1. Switch to the **Tests** module in Apidog
2. Click **"New Test Scenario"**
3. Enter a descriptive name (e.g., "Pet Store Workflow")
4. Click **Continue**

<details>
<summary>📷 Visual Reference</summary>
<Background>
![Create new test scenario](https://api.apidog.com/api/v1/projects/544525/resources/352124/image-preview)
</Background>
</details>

---

### Step 2: Import API Endpoints

1. Hover over **Add Step**
2. Select **"Import from endpoint case"**
3. Choose the endpoints you want to test sequentially

<details>
<summary>📷 Visual Reference</summary>
<Background>
![Import endpoint cases](https://api.apidog.com/api/v1/projects/544525/resources/352125/image-preview)
</Background>
</details>

---

### Step 3: Select Specific Test Cases
1. Select the following cases in order:
   - *Add a new pet to the store (Success)*
   - *Find pet by ID (Pets sold)*

<details>
<summary>📷 Visual Reference</summary>
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344576/image-preview" style="width:640px" alt="Select test cases"/>
</Background>
</details>

---

### Step 4: Configure Data Passing Between Requests

1. Click on *Find pet by ID (Pets sold)*
2. Locate the **petId** parameter in Path params
3. Delete the existing value
4. Click the **Magic Wand** icon

<details>
<summary>📷 Visual Reference</summary>
<Background>
![Magic wand icon](https://api.apidog.com/api/v1/projects/544525/resources/344577/image-preview)
</Background>
</details>

---

### Step 5: Extract Data Using JSONPath

1. Select **"Retrieve pre-step data"**
2. Choose the previous step: *Add a new pet to the store (Success)*
3. Click the **JSONPath Extraction Tool** icon

<details>
<summary>📷 Visual Reference</summary>
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344578/image-preview" style="width:400px" alt="JSONPath extraction tool"/>
</Background>
</details>

---

### Step 6: Define JSONPath Expression

1. In the JSONPath Extraction Tool:
   - Left side shows the previous request's response
   - Right side shows extraction results
2. Enter the expression: `$.data.id`
3. Verify the extracted result matches the expected pet ID

<details>
<summary>📷 Visual Reference</summary>
<Background>
<img src="https://api.apidog.com/api/v1/projects/544525/resources/344579/image-preview" style="width:640px" alt="JSONPath expression"/>
</Background>
</details>

---

### Step 7: Apply the Data Extraction

1. Click **Insert** in the Retrieve pre-step data dialog
2. The expression will populate the **petId** parameter field

<details>
<summary>📷 Visual Reference</summary>
<Background>
![Insert JSONPath expression](https://api.apidog.com/api/v1/projects/544525/resources/344587/image-preview)
</Background>
</details>

---

### Step 8: Execute the Test Scenario

1. Click **Save** in the top-right corner
2. Set the environment to **Local mock**
3. Click **Run** to execute the scenario

---

### Step 9: Review Test Results

1. Examine the test report
2. Expand each step to see request/response details
3. Verify that the **petId** in the second request matches the ID returned from the first request

<details>
<summary>📷 Visual Reference</summary>
<Background>
![Test report](https://api.apidog.com/api/v1/projects/544525/resources/344580/image-preview)
</Background>
</details>

---

## Tips for Effective Test Scenarios

1. **Start Simple**: Begin with 2-3 requests before building complex scenarios
2. **Use Descriptive Names**: Name your test scenarios clearly (e.g., "User Registration Flow")
3. **Validate Data**: Always verify extracted data matches expected values
4. **Environment Management**: Test in different environments (Local, Staging, Production)
5. **Documentation**: Add comments to explain complex data passing logic

---
<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/sharing-api-documentation-645507m0.md">
    Publishing API Docs
  </Card>
</CardGroup>
