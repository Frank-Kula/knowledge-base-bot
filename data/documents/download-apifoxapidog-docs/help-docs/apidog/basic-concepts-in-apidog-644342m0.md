# Basic Concepts in Apidog

This article introduces the core concepts in Apidog, an API-first tool designed for efficient API design, testing, and collaboration. Many concepts differ from similar products like Postman. Understanding these will help you navigate Apidog's workflow effectively.


## Project

A **Project** in Apidog is the primary unit of collaboration, containing modules, environments, test scenarios, and more. It serves as a container for all API-related work within a team.

### Key Components of a Project
- **Modules**: Logical groupings of endpoints and related components.
- **Environments**: Variable sets for different deployment stages (e.g., development, staging, production).
- **Test Scenarios**: Collections of requests for automated testing.
- **Endpoint Specifications**: API documentation based on OpenAPI/Swagger standards.

### Comparison with Postman

| Apidog Concept | Equivalent in Postman | Description |
|----------------|-----------------------|-------------|
| Project | Workspace | Top-level organizational unit for collaboration. |
| Module | Collection Folder | Groups related endpoints. |
| Team | Team | Shared access and collaboration features. |

:::tip[]
Projects enable seamless collaboration, allowing multiple users to work on APIs simultaneously while maintaining version control and access permissions.
:::

## Module

A **[Module](https://docs.apidog.com/module-1261913m0.md)** organizes endpoints logically within a project, similar to a "service" in microservices architecture. Each module represents a standalone OpenAPI specification file.

### Features of a Module
- Contains related endpoints, schemas, responses, and security schemes.
- Configured with a **Base URL** per environment for automatic URL generation.
- Supports import/export operations at the module level for better standards compliance.


### When to Use Modules
- For microservices: Each service as a separate module.
- For multiple APIs: Group endpoints by functionality or domain.
- Default: New projects start with one module; add more as needed for multiple base URLs.

:::info[]
Modules align with OpenAPI Specification (OAS), facilitating integration with other tools and maintaining clean API boundaries.
:::

## Endpoint

An **Endpoint** is the core element in Apidog's API-first approach, representing a specific API operation (e.g., `GET /users/{id}`).

### Endpoint Management
- Grouped in directory structures for organization.
- Supports [definition editing](https://docs.apidog.com/endpoint-basics-533932m0.md), preview, request sending, and save as [endpoint cases](https://docs.apidog.com/debugging-cases-541771m0.md).
- Linked to **endpoint cases** for saved request examples.

### Differences from Postman

| Aspect | Apidog (Endpoint-based) | Postman (Request-based) |
|--------|-------------------------|--------------------------|
| Basic Unit | Endpoint (API spec) | Request (individual call) |
| Spec Changes | Auto-updates cases and tests | Manual rewrite required |
| Structure | OAS extension with debugging | Separate specs and requests |

:::warning[]
In Apidog, changes to endpoint specs propagate automatically to all dependent cases, reducing maintenance overhead through this specification-driven approach.
:::

## Environment

An **[Environment](https://docs.apidog.com/environments-variables-in-apidog-577823m0.md)** manages variables and base URLs for different deployment contexts, enabling seamless switching between dev, staging, and production.

### Key Features
- Contains environment variables for dynamic values.
- Supports multiple **[Base URLs](https://docs.apidog.com/environment-management-584758m0.md)** per environment for microservices.
- Automatic URL construction: Base URL + Endpoint Path.

<Background>
![Environment setup](https://api.apidog.com/api/v1/projects/544525/resources/358407/image-preview)
</Background>

### Base URL Example

Suppose a project with three services:

| Service | Base URL (Prod) | Endpoint Path | Full URL |
|---------|-----------------|---------------|----------|
| User | `https://user.example.com` | `GET /user/{id}` | `https://user.example.com/user/{id}` |
| Order | `https://order.example.com` | `GET /order/{id}` | `https://order.example.com/order/{id}` |
| Product | `https://product.example.com` | `GET /product/{id}` | `https://product.example.com/product/{id}` |

<Background>
![URL generation](https://api.apidog.com/api/v1/projects/544525/resources/358408/image-preview)
</Background>

:::tip[]
No need for manual `{{BaseUrl}}` placeholders; Apidog detects the module and applies the correct base URL automatically.
:::

## Request

A **Request** is a standalone API call, not tied to endpoint specs, similar to Postman's requests.

### Request Capabilities
- [Create](https://docs.apidog.com/send-requests-in-apidog-626721m0.md) independent of specs.
- [Parse](https://docs.apidog.com/saving-requests-as-endpoints-629856m0.md) successful requests into endpoint specs.
- Use for ad-hoc testing or undocumented APIs.

:::info[]
Requests provide flexibility for scenarios where API specs aren't predefined, bridging the gap between design-first and request-first workflows.
:::

## Test Scenario

A **Test Scenario** executes batches of requests, akin to Postman Collections, with advanced automation features.

### Features
- Series of requests from [endpoint specs or cases](https://docs.apidog.com/create-a-test-scenario-599311m0.md) that can [auto-sync](https://docs.apidog.com/sync-data-from-endpoints-and-endpoint-cases-603709m0.md) as API spec changes.
- [Logic components](https://docs.apidog.com/flow-control-conditions-599419m0.md): `If`, `For`, `ForEach`.
- Data [passing](https://docs.apidog.com/pass-data-between-requests-601617m0.md) between requests.
- [Dynamic parameter generation](https://docs.apidog.com/dynamic-values-541766m0.md).

### Advanced Capabilities
- Test reports and performance testing.
- Data-driven testing.
- CI/CD integration.

:::tip[]
Test scenarios auto-sync with API spec changes, ensuring tests remain valid as APIs evolve.
:::

## Design-first Mode & Request-first Mode

Apidog's APIs module features two modes that can be switched at the bottom left corner of the interface: `Design-first Mode` and `Request-first Mode`.

<Background>
<p style="text-align: center">
    <img src="https://api.apidog.com/api/v1/projects/544525/resources/369337/image-preview" style="width: 640px" />
</p>
</Background>


Both modes provide similar functionalities but with different interfaces, catering to different team workflows.

### Design-first Mode
- **Recommended** for teams practicing API-design first.
- Define API specs before development and testing.
- Ideal for planned, specification-driven projects.

### Request-first Mode
- Suitable for teams focusing on backend development first.
- Create requests, then generate specs from successful calls.
- Perfect for undocumented APIs or third-party integrations.

:::tip[]
Learn more about [Design-first Mode & Request-first Mode](https://docs.apidog.com/design-first-vs-request-first-541775m0.md).
:::

## Summary

Understanding these core concepts will help you leverage Apidog's API-first approach for efficient design, testing, and collaboration. Start with creating a project, organize endpoints into modules, define environments for different stages, and build test scenarios for automation.

For further reading, explore the linked documentation pages or try Apidog's interface to see these concepts in action.

--- 

## Read to Kick-off?
<CardGroup cols={2}>
  <Card title="Start from Scratch" href="https://docs.apidog.com/get-started-with-apidog-644404m0.md">
    Get Started with Apidog from Scratch
  </Card>
</CardGroup>

**OR**

<CardGroup cols={2}>
  <Card title="Migrate to Apidog" href="https://docs.apidog.com/migration-guide-overview-633036m0.md">
    Start by migrating to Apidog
  </Card>
</CardGroup>
