# Integration Testing

Integration testing focuses on individual components and their interactions rather than attempting to test the entire application at once. This approach helps identify pieces of your application that aren’t able to communicate properly or places where data isn’t flowing between components as required.

With Apidog, you can test how your application’s APIs work together using requests and test scenarios. You can send API requests in a pre-defined order to test complex operations and observe the flow of data to and from endpoints. You can also send API requests to other systems or services to ensure your application can integrate with them as needed.

### Integration test setup in Apidog

<Video src="https://www.youtube.com/watch?v=tKIblUbRFug"></Video>

To set up integration tests for your application in Apidog, use the following framework:

1. **API requests**: The basic unit of testing is an API request. Each request tests a specific piece of functionality by calling an API endpoint. Learn more about [send requests](https://docs.apidog.com/sending-requests-548328m0.md).

2. **Pre/post-request processors**: For each request, you can add scripts, assertions, extracting variables, and database operations to test and validate the response code, headers, body data, and more. Learn more about [add Pre/post-request processors](https://docs.apidog.com/prepost-processors-in-apidog-588246m0.md).

3. **Test scenarios**: When you need to send multiple requests consecutively, build continuous test scenarios, or repeat requests with different test data, you can create a test scenario and add the necessary requests to it. Learn more about [test scenarios](https://docs.apidog.com/create-a-test-scenario-599311m0.md).

4. **Environments**: When making API requests, it is often necessary to switch between development, testing, and production environments. Apidog makes it convenient to send requests to different environments - you simply need to click and select the desired environment at the top right corner of the interface. Learn more about [Create and use environments](https://docs.apidog.com/environment-management-584758m0.md).

7. **Mock Servers**: Simulate other systems with mock servers. You can test how your application interacts with other APIs and systems without connecting to the actual resources. Instead, you can use Apidog to set up a mock server that simulates the behavior of a real API server by accepting requests and returning responses. Learn more about [setting up mock servers](https://docs.apidog.com/cloud-mock-621066m0.md).

### Run integration tests in Apidog

After setting up your integration tests in Apidog, you can run them in the following ways:

1. **Manually**: You can run a single request, or run a test scenario to get a test report. Learn more about [run a test scenario](https://docs.apidog.com/run-a-test-scenario-602063m0.md).

2. **Scheduled Automation**: You can set up "Scheduled Tasks" to automatically run configured automated test scenarios at specified times, obtain task execution results, and meet the requirements for scheduled testing and regression. Learn more about [Scheduled tasks](https://docs.apidog.com/scheduled-tasks-603702m0.md).

3. **CI/CD Pipeline**: You can run test scenarios as part of your regular application build process using the Apidog CLI. Execute your test suites after every code push and view test reports in Apidog. Learn more about [CI/CD integration](https://docs.apidog.com/cicd-in-apidog-609698m0.md).

