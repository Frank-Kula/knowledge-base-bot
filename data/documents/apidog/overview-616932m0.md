# Overview

Apidog provides comprehensive billing features that enable you to manage payment methods, change plans, and track resource usage for your team or organization.

For a complete comparison of all plans, visit our [pricing page](https://apidog.com/pricing/).

## Billing Units

Apidog's billing operates at two levels:

- **Team**: Subscribe to a plan for an individual team
- **Organization**: Subscribe to a plan that covers all teams within the organization

:::info[]
If you're a member of multiple teams or organizations, paid features only apply to those with active subscriptions. Each paid team or organization is billed separately.
:::

## Billing Amount

Apidog charges based on the number of members in a team or organization.

**Calculation:**  
Billing amount = Subscription plan price * Number of members

### What Counts as a Member?

Team size includes all IDs visible in **Team** → **Members**:
- **Members**: Full team access
- **Guests**: Access to a single project only

<Background>
![Team members view](https://api.apidog.com/api/v1/projects/544525/resources/343469/image-preview)
</Background>

:::tip[]
API consumers who only read shared documentation don't need to join the Apidog team. **Apidog does NOT charge for documentation readers.**
:::

## Billing Methods

Apidog offers two payment methods to suit different organizational needs:

| Method | Payment Type | Billing Cycle | Best For |
|--------|--------------|---------------|----------|
| **Flexible Subscription** | Credit card | Monthly or Annual | Teams needing automatic seat management |
| **Annual Fixed-Seat** | Bank transfer | Annual only | Companies requiring invoices before payment |

### Flexible Subscription (Credit Card)

The recommended subscription method with automatic seat calculation and charging.

**Getting started:**
1. Click **Upgrade** in the top-right corner of the Apidog app
2. Select your desired plan
3. Click **Start free trial**
4. Enter your credit card information

:::tip[]
Learn more about [upgrading your plan](https://docs.apidog.com/upgrading-your-plan-617209m0.md).
:::

**Trial period:**
- Cancel anytime during the trial
- Trial automatically converts to a regular subscription when it ends

#### Billing Cycles

**Monthly subscriptions:**

Apidog charges at the beginning of each billing cycle. The invoice includes:
- Base charge for current team size
- Prorated charges for members added in the previous month
- Credits for members removed in the previous month

**Annual subscriptions:**

- Initial charge based on current team size for the full year
- No new invoices if team size remains unchanged
- When team size changes, a new invoice is generated the following month:
  - **New members**: Prorated charge from join date to subscription end
  - **Departed members**: Refund for unused portion of their subscription

#### Payment Failure

If payment fails:
1. Your plan temporarily reverts to Free until the invoice is paid.
2. Stripe notifies team administrators via email about the failure reason.
3. Stripe automatically retries payment up to four times over five days. You can also manually pay the invoice anytime to restore the subscription.
5. Your team's data will become read-only, but it will not be deleted.
6. Since free plan only supports up to four users, only the first four team members can continue editing until payment is made. The rest of the team will have read-only access.

### Annual Fixed-Seat (Bank Transfer)

Suitable for companies that cannot use credit cards or require invoices before payment.

**Access this option:**  
Click **"Unable to use the credit card or need an invoice first? Click to upgrade"** at the top of the Upgrade interface.

<Background>
![Annual fixed-seat upgrade option](https://api.apidog.com/api/v1/projects/544525/resources/343515/image-preview)
</Background>

**Key features:**
- **Annual subscriptions only** (monthly is not available)
- **Fixed seat count**: Specify the number of seats when subscribing
- **Flexible member management**: Add or remove members within your purchased seat limit
- **Seat expansion**: Can purchase additional seats during the subscription (cannot decrease)

<Background>
![Seat selection interface](https://api.apidog.com/api/v1/projects/544525/resources/343516/image-preview)
</Background>

**Process:**
1. Initiate subscription and receive an invoice
2. Subscription activates upon payment
3. Receive renewal reminder near subscription end
4. Renew to continue subscription

:::tip[]
Learn more about [annual fixed-seats](https://docs.apidog.com/alternative-payment-methods-617224m0.md).
:::

## Billing System

All payments are encrypted and processed via **Stripe**, the payment provider trusted by Twitter, Pinterest, and Lyft.

**Stripe Customer Portal features:**
- View and download invoices
- Update credit card information
- Modify payment methods
- Manage recurring billing

**Access the portal:**  
Click **Manage Plan** on the Plans page to open Stripe's customer portal.

<Background>
![Manage Plan button](https://api.apidog.com/api/v1/projects/544525/resources/343519/image-preview)
</Background>

:::tip[]
Learn more about [managing subscriptions](https://docs.apidog.com/managing-subscriptions-617217m0.md).
:::

## Exceeding Usage Capacity

When your team exceeds the capacity allocated in your plan:

| Access Level | Permissions |
|--------------|-------------|
| **Team Members** | Read-only access to all projects |
| **Team Administrators** | Manage team members, upgrade plan, or reduce usage capacity |

## Contact Support

If you have questions about payment or refunds, our support team is here to help.

**Email:** support@apidog.com

:::tip[About JCT]
Apidog, Inc. is a United States company. For payments made in Japan, we do not charge Japanese Consumption Tax (JCT).
:::

