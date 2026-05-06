# Why Scheduled test scenario endedup with 0 request?

### Q: Why did my scheduled test scenario ended up with 0 request?
**A**: No request was passed through the scheduled tas because the environment set for the scheduled run was set to "**Private**." In Apidog, when an environment is private, scheduled tests may not have access to the required variables, leading to failed requests.

### Q: How can I fix this issue?
**A:** To resolve this, change the environment from "**Private**" to "**Shared**" in Apidog. This allows all requests in the scheduled test to execute successfully.Once can find the environment setting in two different ways. first one is -Follow these steps:
Go to your Apidog project. on the right top of the screen you can find the environment selection option and if you click on the three parallel lines, you will find a new window and there you can find the settings for the environment. 

<Background>
  
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/351377/image-preview)
</Background>
There you will have othe other important setting we are talking here is - **Shared** & **Private** option for the environment. Change the environment type from Private to Shared.
Save the changes and re-run your scheduled test.



### Q: Will changing the environment to "Shared" affect other tests?

**A**: No, sharing an environment only makes it accessible to all scheduled tests and team members (if applicable). Ensure that sensitive data is handled securely if working in a team.

### **Q: What if my requests still fail after changing the environment?**

**A:** If issues persist, check:

1. API URLs and parameters to ensure they are correct.
2. Environment variables to confirm they are properly defined.
3. Network and authorization settings to verify API access.
If the issue continues, try running the test manually to identify specific errors.


