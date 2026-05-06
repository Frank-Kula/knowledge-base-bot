# Get Started with Apidog

This guide will help you get started quickly, from setting up your account to making your first API requests.


## Video Guide

<Video src="https://www.youtube.com/watch?v=ZdfWsGJ-BUM&list=PLIioFgXX9kneLUQ71f7y_t7DJWCHxs9SI"></Video>

Checkout the complete [Getting Started with Apidog](https://www.youtube.com/watch?v=ZdfWsGJ-BUM&list=PLIioFgXX9kneLUQ71f7y_t7DJWCHxs9SI) playlist on YouTube. 

## Prerequisites

Before you begin, ensure you have:

1. **Account Setup**: Sign up for a free Apidog account at [app.apidog.com](https://app.apidog.com/user/login) if you haven't already.
2. **Sign In**: Log in to the Apidog [web application](https://app.apidog.com) or client application (Download [Here](https://apidog.com/download/)).
3. **Open A Project**: Start a new project or [import](https://docs.apidog.com/migration-guide-overview-633036m0.md) an existing project to organize your APIs. Learn more about [projects and basic concepts](https://docs.apidog.com/basic-concepts-in-apidog-644342m0.md) or [Apidog UI guide](https://docs.apidog.com/navigating-apidog-644142m0.md).

:::tip[The Pet Store project]
The Pet Store project is a built-in Apidog sample that helps you learn key concepts and features. Get started by clicking **Create Sample Project** on the Apidog welcome page.
<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369338/image-preview)
</Background>
:::


## Choose Your Development Model

Apidog supports two primary API development approaches:

| Model | Description | Best For | Workflow |
|-------|-------------|----------|----------|
| **Design-first** | Define API specifications before implementation | Teams prioritizing planning and documentation | Spec → Request → Test → Share |
| **Request-first** | Build and test APIs from actual requests | Agile teams, prototyping, undocumented APIs | Request → Spec → Test → Share |
:::tip[]
Both models are fully supported and can be switched anytime. Choose based on your team's workflow preferences. Learn more about [Design-first Mode & Request-first Mode](https://docs.apidog.com/design-first-vs-request-first-541775m0.md).
:::

## Design-first Model

In the Design-first approach, you define your API specifications upfront, ensuring clarity and consistency before implementation. This method is ideal for teams that prioritize planning and want to create comprehensive documentation from the start.

<Steps>
<Step>
[Specify a new endpoint](https://docs.apidog.com/creating-an-endpoint-644726m0.md)
Define your API endpoint with path, method, parameters, and responses. This creates the foundation of your API specification.
</Step>
<Step>
[Switch to Design-first mode](#switching-between-modes)
In the bottom-left corner of the Apidog interface, select "Design-first" mode to continue designing your endpoint.
</Step>
<Step>
[Make a request to the endpoint](https://docs.apidog.com/making-a-request-645415m0.md)
Test your defined endpoint by sending actual requests to validate the design.
</Step>
<Step>
[Add an assertion](https://docs.apidog.com/adding-an-assertion-645440m0.md)
Set up automated checks to ensure your API responses meet expected criteria.
</Step>
<Step>
[Create a test scenario](https://docs.apidog.com/creating-test-scenarios-645499m0.md)
Build comprehensive test suites that cover multiple endpoints and use cases.
</Step>
<Step>
[Share your API documentation](https://docs.apidog.com/sharing-api-documentation-645507m0.md)
Publish and share your API docs with stakeholders for feedback and integration.
</Step>
<Step>
[Explore advanced features](https://docs.apidog.com/explore-more-645526m0.md)
Dive deeper into Apidog's capabilities like environments, schemas, and collaboration tools.
</Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Start with Design-first" href="https://docs.apidog.com/creating-an-endpoint-644726m0.md" target="_self">
    Specify your first endpoint
  </Card>
</CardGroup>


## Request-first Model

The Request-first approach starts with actual API calls, allowing you to prototype and validate APIs quickly. This method is perfect for teams working with existing backends, third-party APIs, or when you need to document undocumented endpoints.

<Steps>
<Step>
[Send a request](https://docs.apidog.com/making-a-request-645415m0.md)
Make an API call to test or explore an existing endpoint.
</Step>
<Step>
[Switch to Request-first mode](#switching-between-modes)
In the bottom-left corner of the Apidog interface, select "Request-first" mode.
</Step>
<Step>
[Add an assertion](https://docs.apidog.com/adding-an-assertion-645440m0.md)
Implement automated validation rules to ensure API reliability and correctness.
</Step>
<Step>
[Create a test scenario](https://docs.apidog.com/creating-test-scenarios-645499m0.md)
Develop comprehensive test suites that simulate real-world API interactions.
</Step>
<Step>
[Share your API documentation](https://docs.apidog.com/sharing-api-documentation-645507m0.md)
Generate and distribute professional API documentation for your team and partners.
</Step>
<Step>
[Explore advanced features](https://docs.apidog.com/explore-more-645526m0.md)
Discover Apidog's full range of testing, collaboration, and automation tools.
</Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Start with Request-first" href="https://docs.apidog.com/making-a-request-645415m0.md" target="_self">
    Send your first request
  </Card>
</CardGroup>

## Switching Between Modes

You can switch between Design-first and Request-first modes at any time using the toggle in the bottom-left corner of the interface:
<Background> 
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/369339/image-preview)
</Background>

This flexibility allows you to adapt your workflow as your project evolves.
