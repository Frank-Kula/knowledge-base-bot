# General Runner Docker Container "Not Found" Error.

Q: What is the issue? 
A: When attempting to run the General Runner Docker container as per the Apidog documentation (https://docs.apidog.com/general-runner-755233m0), users encounter a "Not Found" error. The error occurs when the runner attempts to reach the endpoint:https://api.apidog.com/api/v1/self-hosted-runners/0/general-configs
The log file shows that the runner ID appears as 0, which likely indicates a misconfiguration.

Q: What causes this issue? 
A: The issue may stem from an incorrect Docker deployment configuration, particularly related to the -v (volume) option. If the specified path for volume mounting is invalid or lacks proper permissions, the runner might fail to retrieve its configuration, resulting in a "Not Found" error.

Q: How can I resolve this issue? 
A: To fix the problem, ensure that the -v option in your Docker command specifies a valid path with the correct permissions.
If the issue persists, try removing the -v option and running the container without volume mounting.Example:
Before (Potential Issue): 
> docker run -d --name apidog-runner -v /invalid/path:/app/config apidog/general-runner

After (Fixed Version): 
> docker run -d --name apidog-runner apidog/general-runner

If you require volume persistence, ensure that /app/config is correctly mapped to an accessible directory on your host system.

Q: What if the issue persists after trying the resolution? 
A: If the problem continues, try the following:
Verify that your API token and self-hosted runner setup in Apidog are correctly configured. 
Check your network connectivity to ensure the container can access https://api.apidog.com.
Review the complete log file for additional error messages. 
Contact Apidog support with your error logs for further troubleshooting.
