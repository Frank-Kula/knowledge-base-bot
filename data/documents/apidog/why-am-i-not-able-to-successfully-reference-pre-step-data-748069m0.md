# Why am I not able to successfully reference pre-step data?

Firstly, make sure you're now in "Tests" module. "Referencing pre-step data" feature is available only in Tests module but not APIs module.

If you're now surely in Tests module, switch to the "Actual Request" tab to confirm whether the pre-step data referenced in the request has been successfully incorporated. 

If the reference in the actual request still appears as `{{$.n.response.body.abc}}` instead of showing actual data, it indicates that the reference has not been applied. 

In this case, consider the following common reasons:
1. Have you run the entire test scenario instead of just a single step? Referencing pre-step data requires running the complete test scenario for it to take effect.
2. Verify if the step ID is correct and corresponds to the step you intend to reference.
3. Ensure that the JSONPath used matches the data source accurately.
