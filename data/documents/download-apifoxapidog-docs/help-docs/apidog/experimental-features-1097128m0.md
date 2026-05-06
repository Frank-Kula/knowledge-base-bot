# Experimental Features

:::info[Version Requirement]
Apidog version 2.7.14 or later is required to access experimental features.
:::

When using Apidog for endpoint debugging and testing, application stability and performance depend on your local device's resources. To optimize the experience across different hardware configurations, Apidog offers experimental features that help balance resource consumption and execution efficiency.

These features allow you to customize how Apidog utilizes system resources based on your device's capabilities and usage scenarios.

<Background>
![experimental features of Apidog.png](https://api.apidog.com/api/v1/projects/544525/resources/356561/image-preview)
</Background>

## Available Features

| Feature | Description | When to Enable | Resource Impact |
|---------|-------------|----------------|-----------------|
| **Send API requests using independent processes** | Uses separate processes for API requests to prevent excessive memory usage and reduce lag | Computers with smaller memory capacity | Reduces memory pressure |
| **Run test scenarios using independent processes** | Uses separate processes for test scenarios to improve execution speed | Computers with adequate memory and when faster test execution is needed | Increases memory usage |
| **Optimize local service process memory** | Automatically reclaims memory from the local service process (handles local Mock and OpenAPI export) | Computers with smaller memory capacity | Reduces memory usage but may slow down local service requests |

:::tip
The "Run test scenarios using independent processes" feature will not activate if your system is experiencing high memory pressure, protecting your device from performance degradation.
:::

## Recommendations

- **Low-memory devices**: Enable "Send API requests using independent processes" and "Optimize local service process memory"
- **High-performance devices**: Enable "Run test scenarios using independent processes" for faster test execution
- **Balanced approach**: Test each feature individually to find the optimal configuration for your workflow

