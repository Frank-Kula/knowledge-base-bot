# How do I access and search the runner logs to identify the issue when a problem arises with a runner?

1. Use `the docker ps` command to find the problematic Runner information;

2. Based on the Runner container ID, run the following command to query valid logs
```
# View the last 100 lines of the log for container ID abc123, recommended:
docker logs --tail 100 abc123

# View logs from the past 5 minutes:
docker logs --since 5m abc123

# View logs from 5 minutes before a specific timestamp:
docker logs --until 2023-10-01T00:00:00 abc123
docker logs --until 5m abc123

# View the log for container ID abc123, not recommended if data is voluminous:
docker logs abc123.
```
If you need to export logs to technical support, go to the opt/runner/logs floder in the Runner container and export the entire logs folder.


:::note[]
The logs in the container are the logs collected by different business processes.
:::



