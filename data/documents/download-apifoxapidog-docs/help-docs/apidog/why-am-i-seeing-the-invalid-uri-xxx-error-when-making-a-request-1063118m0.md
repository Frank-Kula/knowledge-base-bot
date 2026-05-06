# Why am I seeing the "Invalid URI xxx" error when making a request?

1. Check if the endpoint is linked to a service with an empty `Base URL`.

   If you're using inheritance (e.g., a parent folder), ensure that both the parent and root folders have their `Base URL` properly configured (i.e., not empty). You can read [Environments & variables](https://docs.apidog.com/environments-variables-1368140f0.md)

2. Verify if the `Base URL` is defined using a variable.

   If a variable is used for the `Base URL`, ensure that the corresponding global or environment variable has a valid value assigned.

3. If neither of the above resolves the issue.

   Please share the following details with our technical support team to assist further:

   - The current version of Apidog you're using  
   - The service assigned to the endpoint  
   - The relevant environment configuration from Environment Management  

