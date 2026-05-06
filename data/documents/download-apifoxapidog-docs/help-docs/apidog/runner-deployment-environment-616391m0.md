# Runner Deployment Environment

Apidog Runner is a command-line tool that executes scheduled API tests and automation tasks in server environments. This reference guide outlines the hardware, runtime, and network requirements for deploying Runner in production or CI/CD environments.

Understanding these requirements ensures optimal performance and reliability when running automated API tests at scale.

## Hardware Requirements

### Recommended Server Configuration

| Component | Minimum Requirement | Recommended | Purpose |
|-----------|-------------------|-------------|---------|
| **CPU** | 2 cores | 4+ cores | Runner executes scheduled tasks concurrently, requiring adequate processing power |
| **Memory** | 4GB RAM | 8GB+ RAM | Runner loads and generates large amounts of data during scheduled tasks; larger teams need more memory |
| **Disk Space** | 30GB | 50GB+ | Accommodates log storage and test artifacts |

:::warning[]
For larger teams or high-frequency test execution, increase memory to 8GB or more to prevent performance degradation.
:::


## Runtime Parameters

Configure the following environment variables when deploying Runner:

| Parameter Name | Description | Example Value |
| -------------- | ----------- | ------------- |
| `TZ` | Configure the time zone for Runner execution. Scheduled tasks will run according to the set time zone and time. Refer to [TZ identifier](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) for configuration. | `America/Los_Angeles` |


## Network Environment

### Server Communication Requirements

Runner needs to communicate with the Apidog server. Ensure that the network environment of the server executing the Runner can access the Apidog server and supports the WebSocket protocol.

**Required Protocols:**
- HTTPS (port 443)
- WebSocket (WSS)

:::info[Firewall Configuration]
Ensure your firewall allows outbound connections to Apidog servers on ports 443 (HTTPS) and WebSocket connections for real-time communication.
:::

### Automated Testing Requirements

For scheduled tasks for automated testing, the server's network environment must be able to access all requested URLs to initiate requests normally. After running automated tests, test reports will be uploaded—please ensure that the server network environment can access AWS domain names.


### Data Import Requirements
For scheduled tasks that import data, ensure that the server's network environment can access the URL of the data source to be imported.
