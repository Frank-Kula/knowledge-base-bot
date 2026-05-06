# Custom SMTP Configured Successfully, but Allowlisted Users Don’t Receive OTP Emails

### Problem Description

After publishing a documentation site and enabling **Email Allowlist**, users are required to receive a one-time password (OTP) via email to access the documentation.

The following setup has been completed:

* Custom SMTP server is enabled
* SMTP host, port, username, and password are configured
* SMTP configuration test passes (for example, via cURL)

However, in actual usage, allowlisted users never receive the OTP email.


### Possible Cause

This is a common issue caused by a **mismatch between the SMTP port and the encryption settings**.

Taking **AWS SES** as an example:

* Port **587** does **not use SSL encryption by default**
* If you configure:

  * Port 587
  * And enable SSL / encryption in the custom SMTP settings
* The result may be:

  * SMTP tests appear to succeed
  * But transactional emails (such as OTP codes) fail to be delivered


### Solution

Please review and adjust your custom SMTP configuration:

1. If you are using **port 587**

   * Disable the **SSL / encryption** option
2. Save the configuration
3. Try accessing the documentation site again to trigger the OTP email

> If your SMTP provider requires SSL encryption, make sure the port you use matches the encryption method (for example, port 465 is typically used for SSL).


### Applies To

* Published documentation sites
* Email Allowlist enabled
* OTP verification via email
* Custom SMTP servers (such as AWS SES)

