# Fixing ENOTFOUND: getaddrinfo ENOTFOUND www Error

This is a typical **DNS (Domain Name System) resolution error**, belonging to the same category as [ENOTFOUND: Couldn't resolve host](https://docs.apidog.com/fixing-enotfound-couldnt-resolve-host-error-1650534m0.md).


`getaddrinfo ENOTFOUND www` means that when the system attempted to resolve the domain name in your request, it **could not find a host named "www"**.

## Possible Causes

This error is almost certainly caused by an **incomplete or malformed URL**.

1. **Incomplete URL (most likely cause):** When sending a request in Apidog, you may have entered only `www` without specifying a full domain name.
   For example, you intended to request `http://www.example.com`, but only entered `www`.

2. **Missing protocol prefix:** Even if you entered a full domain name, you may have omitted the **`http://`** or **`https://`** prefix, causing the system to fail to recognize it as a complete web address.

## How to Fix

You only need to focus on correcting the request URL in Apidog.

In the request address bar of Apidog, make sure you’ve entered a complete and valid address that includes the **`http://`** or **`https://`** prefix.

