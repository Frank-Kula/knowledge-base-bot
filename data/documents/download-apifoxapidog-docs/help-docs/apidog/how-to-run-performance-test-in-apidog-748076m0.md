# How to run performance test in Apidog?

:::tip[]
The performance testing feature is currently in Beta. If you met any problems, please join the [Technical Support Discord](https://discord.gg/9ebhMYEX6t) and provide your feedback.
:::

Performance testing involves sending large-scale service requests to an API to identify performance bottlenecks, assess stability, expose potential risks under pressure, and ensure the API can operate reliably and respond to requests under high load.

![Performance Testing](https://assets.apidog.com/uploads/help/2024/03/06/cf4d456b44c16b723b3e8bb13798857e.png)

## Set configuration items

Before running a performance test, you need to specify the runtime environment and optionally test data for the test scenario, as well as configure the performance test settings.

### Runtime environment

The runtime environment in the test scenario inherits from the current project's environments.

### Test data

After associating test data, virtual users will use the variables defined in the test data to execute requests. You can choose to run in either "Random Match" or "Sequential Match" mode:

- **Random Match:** Each virtual user randomly selects a row of data from the test data to run. In this mode, all virtual users will select one test data row and execute the performance test.
  
- **Sequential Match:** Each virtual user selects a row of data from the test data in order. Note: If the number of virtual users exceeds the number of test data rows, the excess virtual users will not start the performance test.

:::highlight purple
[Learn more about test data](https://docs.apidog.com/data-driven-testing-602987m0.md).
:::

### Virtual users (Concurrent users)

Supports up to 100 virtual users. Within the specified test time, it simulates online users running the test scenario in parallel repeatedly.

### Test duration

The total runtime of the performance test. During this period, each virtual user will continuously loop through all APIs in the test scenario.

### Ramp-up duration

Users typically access a service gradually over time, rather than instantly. To simulate this, set a ramp-up time to gradually increase the number of parallel users over the first X minutes (X is the preset value). If X is set to 0, all virtual users start immediately at the beginning of the test.

## Running the performance test

After triggering the performance test, an intuitive visualization panel will display key metrics such as **Total Requests, Avg Throughput, Avg Response Time, Maximum/Minimum Response Time, and Errors** for each API.

![Performance Test Visualization](https://assets.apidog.com/uploads/help/2024/03/06/4d9afac82624116edc11c7ab2d0feed1.png)

Only one performance test can be run for a project at a time. If a higher-priority test needs to be conducted, click the "Terminate" button in the top right corner.

## Viewing the test process

During the performance test, you can hover over the test chart to view the test details for each time period in real-time.

![Test Details](https://assets.apidog.com/uploads/help/2024/03/06/d8a984af97cd47a4092f80cb1e0ad05b.png)

Click "Error" to check failed requests for the API and analyze possible causes. You can also filter API requests in the filter bar.

![Error Analysis](https://assets.apidog.com/uploads/help/2024/03/06/6e93908a4e884daae70d77626ff0663a.png)

Due to the large volume of API requests in a performance test, only failed requests are categorized and displayed statistically. Detailed error information and request details for each API are not recorded. If you encounter unexpected errors, run a "Functional Test" first and resolve all issues before running a "Performance Test."

## Viewing test reports

Click the **"Test Reports"** tab to view historical test reports for the current test scenario. 

![Test Reports](https://assets.apidog.com/uploads/help/2024/03/06/20073e941ab93c276e1780d9125b8a7e.png)


## FAQ

**Q: How can I export performance test reports?**

A: Performance testing is currently in the beta stage, and Apidog does not yet support exporting performance test reports. You can only view the results within the Apidog client.

**Q: How can I view the actual requests and responses in the performance tests?**

A: Apidog's performance testing does not provide the ability to view the actual requests and responses. 

This is because performance testing focuses on evaluating the API's behavior under high load, and these APIs should have already 100% passed functional testing. Any issues are likely caused by server performance, not the request/response content. 

Therefore, viewing the actual requests and responses would not help troubleshoot performance-related problems. Therefore, the performance testing feature in Apidog does not provide the functionality to view the actual requests and responses.
