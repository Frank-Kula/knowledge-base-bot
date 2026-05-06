# How Can I Capture and Validate Stripe Webhooks in ApiDog During CI/CD?

**Q: Does ApiDog support listening for Stripe webhooks directly?**
No, ApiDog does not natively support listening for webhooks. However, you can still validate webhook events by leveraging your backend and database.

**Q: What is the recommended approach to test Stripe webhooks with ApiDog?**
You can follow these steps:
1. Set Up a Webhook Receiver in Your Backend:
- Create an endpoint in your backend service to capture incoming Stripe webhooks.
- Store the webhook event data in a Stripe event logs table in your database.
2. Validate Webhook Data in ApiDog:
- Use ApiDog’s Post-Request Processor to query your database.
- Retrieve the stored webhook event and validate it against expected results.

**Q: Can ApiDog directly query the database for validation?**
Yes, ApiDog supports connecting to a database in the corresponding environment. You can configure it to retrieve webhook event records and verify them in your tests.

**Q: How does this method fit into a CI/CD workflow?**
During automated tests in your CI/CD pipeline:
- The backend captures and logs webhook events.
- ApiDog queries the database to verify the expected webhook event was received.
- The test passes if the logged data matches expectations.

**Q: What if I need real-time webhook testing?**
If real-time webhook validation is required, consider using a webhook relay service (e.g., Stripe CLI, Ngrok) to forward events to an accessible test environment.
