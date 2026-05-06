# Fixing the connect EHOSTUNREACH Error

## Symptoms

When sending a request in Apidog, the following error is returned:

```
connect EHOSTUNREACH
```


However, the same endpoint can be accessed successfully using Postman or a web browser.

## Cause

When the endpoint URL points to a private network address (for example, `172.x.x.x` or `192.168.x.x`), applications on **macOS 11 and later** must be explicitly granted permission to access the local network.

If Apidog is not granted **Local Network** access, the system will block the connection, causing the request to fail.

## Solution

1. Open **System Settings**
2. Go to **Privacy & Security**
3. Select **Local Network**
4. Locate **Apidog** and enable access
5. Close and reopen Apidog, then resend the request

## If the Issue Persists

If **Local Network** permission is already enabled and the error `connect EHOSTUNREACH` still occurs after restarting Apidog, continue checking the following items:

### 1. Switch Agent / Proxy

Make sure the Agent currently used by Apidog matches the network environment of the endpoint.

In the error prompt, click **"Switch Agent"**, select an appropriate Agent, and resend the request.

### 2. Verify Proxy / VPN Configuration

If the endpoint is only accessible through a VPN or system proxy:

* Check whether the Apidog Agent:

  * Is configured to use the system proxy
  * Is running in a network environment that has access to the VPN

If necessary, temporarily disable the proxy or VPN to compare and verify.

### 3. Quick Self-Check (Optional)

Run the following command in the environment where the Agent is located:

```bash
curl http://<endpoint-url>
```

If the endpoint cannot be reached from the command line either, it indicates that the network environment itself cannot connect to the endpoint.

