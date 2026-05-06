# Why does the client request for the same endpoint succeed, but an error occurs when debugging on the web side: "Unable to request address"?

### Unable to request an address during online documentation or web debugging?
When you try to debug the endpoint in the document shared by Apidog, I get the error "Unable to request the address", possible causes

1. Browser Certificate Issues: 
If your request is HTTPS, the endpoint may redirect to port 443 during the request. Since the client can be set to ignore certificate errors, it can be accessed normally; However, browsers are strict in managing certificates and cannot ignore errors on their own, resulting in access failures and exception prompts.

2. Network or Firewall Restrictions:
Some network environments or firewall settings may block requests from the browser, while client requests are exempt from these restrictions.

### How to solve this problem?


1. Check Network Connection: Make sure that your network connection is working and that the browser can access the target server. You can try to go floder to the target server in your browser for verification.

2. Browser Certificate Management:
- Check if the certificate is valid: Make sure that the server's certificate is signed by a trusted certificate authority and has not expired.

- In the browser's settings, find the "Security" option, and in the "Certificate Management" related settings, manually add the certificate trust for the website.

- If your target service supports HTTP requests, you can try using HTTP instead of HTTPS
