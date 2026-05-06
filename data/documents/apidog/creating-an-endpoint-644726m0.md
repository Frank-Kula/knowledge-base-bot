# Creating an Endpoint

Endpoints are the fundamental building blocks of APIs in Apidog. This guide introduces how to create and specify endpoints, helping you define your API specifications effectively.

## What is an Endpoint?

An endpoint represents a single API operation that can be invoked via HTTP. Each endpoint consists of:

| Component | Description | Example |
|-----------|-------------|---------|
| **HTTP Method** | The action to perform | `GET`, `POST`, `PUT`, `DELETE` |
| **Path** | The URL path relative to base URL | `/users/{id}` |
| **Parameters** | Path, query, header, or body parameters | `id` (path parameter) |
| **Request Body** | Data sent with the request (for POST/PUT) | JSON schema |
| **Responses** | Expected response formats and status codes | `200 OK`, `404 Not Found` |

:::tip[Key Concept]
Apidog endpoints are specification-driven. When you define an endpoint, you're creating both documentation and a testable interface that automatically generates requests.
:::

## Creating Endpoints

### Prerequisites

Before creating endpoints, ensure you have:
- An Apidog [account](https://apidog.com) and the Apidog [client application](https://apidog.com/download/)
- Basic understanding of HTTP methods and API concepts
- A project created in Apidog where you want to add endpoints, check out the [Overview](https://docs.apidog.com/get-started-with-apidog-644404m0.md) page for more information.

### Quick Start: Basic Endpoint Creation

1. **Navigate to APIs Module**: Click the "APIs" tab in the sidebar
2. **Create New Endpoint**:
   - Click **New HTTP Endpoint** button or **+** in the directory tree then **New HTTP Endpoint**
   - Select the target module / folder

This action places you in Design-first Mode (or you can manually do so before making a request), where you define the API specification first. 

### Endpoint Creation Methods

| Method | When to Use | Steps |
|--------|-------------|-------|
| **Manual Creation** | Starting from scratch | 1. Right-click folder → "New Endpoint"<br>2. Fill in method and path<br>3. Define parameters and responses |
| **[Import from Code](https://docs.apidog.com/migration-guide-overview-633036m0.md)** | Existing API code | 1. Use "Import" feature<br>2. Upload OpenAPI/Swagger file<br>3. Map to modules |
| **[From Request](https://docs.apidog.com/875945m0.md)** | Testing existing APIs | 1. First send a request <br>2. Click "Save"<br>3. Refine the specification |
| **Clone Existing** | Similar endpoints | 1. Right-click endpoint → "Duplicate"<br>2. Modify path and parameters |

## Specifying Endpoint Details

### Basic Information

Every endpoint requires:

- **Name**: Descriptive title (e.g., "Get User Profile")
- **Method**: HTTP verb
- **Path**: URL path with parameters
- **Description**: What the endpoint does

### Parameters

In the Apidog workbench, you can define parameters that customize the endpoint behavior as follows (values are used only as examples):

<Steps>
  <Step>
#### Path Parameters
Used in the URL path itself:

```
GET /users/{userId}/posts/{postId}
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `userId` | integer | Yes | Unique user identifier |
| `postId` | integer | Yes | Post identifier |
</Step>

<Step>    
#### Query Parameters
Optional filters and pagination:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `limit` | integer | No | 10 | Number of results to return |
| `offset` | integer | No | 0 | Number of results to skip |
| `status` | string | No | active | Filter by status |
</Step>

<Step>
#### Request Body (for POST/PUT)
Define the expected input data using JSON Schema:

```json
{
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "User's full name"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "User's email address"
    }
  },
  "required": ["name", "email"]
}
```
</Step>
  
<Step>    
### Responses

Define all possible response formats:

#### Success Response (200 OK)
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com",
  "createdAt": "2023-01-15T10:30:00Z"
}
```

#### Error Responses

| Status Code | Description | Schema |
|-------------|-------------|--------|
| `400` | Bad Request | Error details |
| `401` | Unauthorized | Authentication error |
| `404` | Not Found | Resource not found |
| `500` | Internal Server Error | Server error details |
</Step>
</Steps>

:::tip[]
The **Design** tap includes extended API specification options.
:::

---
<CardGroup cols={2}>
  <Card title="Next Step" href="https://docs.apidog.com/making-a-request-645415m0.md">
    Make a Request
  </Card>
</CardGroup>
