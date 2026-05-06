# Managing Subscriptions

This guide explains how to monitor your subscription status, understand pricing changes based on team size, and manage plan modifications.

## Monitoring Your Subscription

### Plan Usage

View current plan usage on the **Team** → **Plans** page.

<Background>
![Plan usage overview](https://api.apidog.com/api/v1/projects/544525/resources/372044/image-preview)
</Background>

### Invoices

Access invoices by clicking **Invoices** on the **Team** → **Plans** page.

<Background>
![Invoices button](https://assets.apidog.com/uploads/help/2023/08/21/6f0910cdcaa8f668059811fe86cc26a5.png)
</Background>

### Payment Information

View and modify payment information by clicking **Invoices** on the **Team** → **Plans** page.

<Background>
![Payment information](https://assets.apidog.com/uploads/help/2023/08/21/6f0910cdcaa8f668059811fe86cc26a5.png)
</Background>

## Pricing Impact of Team Size Changes

Apidog reviews team member changes monthly, regardless of whether you're on a monthly or annual subscription.

### Adding New Members

#### Monthly Subscription

**Formula:**
- Current month's charge = Plan price × Current team members
- Additional charge at billing cycle end = Plan price × Number of new users × (Days of usage ÷ Total days in month)

**Example:**

Team A (10 members) subscribed to the Basic Plan ($12/member/month) on May 20. A new user joined on May 25.

**Actual payments:**
1. **May 20**: \$12 × 10 = $120
2. **June 20**: (\$12 × 11) + (\$12 × 25/30) = \$132 + \$10 = $142

#### Annual Subscription

**Formula:**
- Current order price = Plan price × Current team members × 12
- Additional charge next month = Plan price × Number of new users × 12 × (Days of usage ÷ 365)

**Example:**

Team A (10 members) subscribed to the Basic Plan ($12/member/month) on May 20. A new user joined on May 25.

**Actual payments:**
1. **May 20 (Year 1)**: \$12 × 10 × 12 = \$1,440
2. **June 20 (Year 1)**: \$12 × 1 × 12 × (360/365) = \$142 (prorated for new member)
3. **May 20 (Year 2)**: \$12 × 11 × 12 = \$1,584

### Removing Members

#### Monthly Subscription

**Formula:**
- Current month's charge = Plan price × Current team members
- Refund at billing cycle end = Plan price × Number of removed users × (Unused days ÷ Total days in month)
- Next month's charge = Plan price × Current team size (refunds applied as credit)

**Example:**

Team A (10 members) subscribed to the Basic Plan ($12/member/month) on May 20. A member was removed on May 25.

**Actual payments:**
1. **May 20**: \$12 × 10 = \$120
2. **June 20**: \$12 × 9 = \$108 (refund of $10 applied as credit for future payment)

#### Annual Subscription

**Formula:**
- Current order price = Plan price × Current team members × 12
- Refund next month = Plan price × Number of removed users × 12 × (Unused days ÷ 365)
- Next year's charge = Plan price × Current team size × 12 (refunds applied as credit)

**Example:**

Team A (10 members) subscribed to the Basic Plan ($12/member/month) on May 20. A member was removed on May 25.

**Actual payments:**
1. **May 20 (Year 1)**: \$12 × 10 × 12 = \$1,440
2. **June 20 (Year 1)**: Refund of \$142 retained as team credit (visible in invoice)
3. **May 20 (Year 2)**: \$12 × 9 × 12 = \$1,296 (refund credit applied)

## Plan Changes

### Upgrading to a Higher-Tier Monthly Plan

**Formula:**
- Current month's charge = Lower-tier price × Current team members
- Upgrade charge = (Higher-tier price × Current team members) - (Lower-tier price × Current team members × Unused days ÷ Total days in month)

**Example:**

Team A (10 members) on Basic Plan (\$12/member/month, billing on the 20th) upgraded to Professional Plan (\$24/member/month) on May 25.

**Actual payments:**
1. **May 20**: \$12 × 10 = \$120
2. **May 25**: (\$24 × 10) - (\$12 × 10 × 25/30) = \$240 - \$100 = \$140 (upgrade difference)
3. **June 20**: \$24 × 10 = \$240

### Upgrading to a Higher-Tier Annual Plan

**Formula:**
- Current order price = Lower-tier price × Current team members × 12
- Upgrade charge = (Higher-tier price × Current team members × 12) - (Lower-tier price × Current team members × Unused days ÷ 365)

**Example:**

Team A (10 members) on annual Basic Plan (\$9/member/month) upgraded to annual Professional Plan (\$18/member/month) on May 25.

**Actual payments:**
1. **Initial annual order**: \$9 × 10 × 12 = \$1,080
2. **May 25 (upgrade)**: (\$18 × 10 × 12) - (\$9 × 10 × 12 × Unused days/365)

### Downgrading or Canceling Subscription

#### Monthly Downgrade

Downgrades take effect at the end of your billing cycle.

**Formula:**
- Current month's charge = Plan price × Current team members
- Downgrade to Free Plan next month

**Example:**

Team A (10 members) on Basic Plan (billing on the 20th) downgraded to Free Plan on May 25.

**Actual payments:**
1. **May 20**: \$12 × 10 = \$120
2. **June 20**: Downgrade to Free Plan (no charge)

#### Annual Downgrade

Downgrades take effect at the end of your billing cycle.

**Formula:**
- Annual order price = Plan price × Current team size × 12
- Downgrade to Free Plan at subscription end

**Example:**

Team A (10 members) on annual Basic Plan subscribed on May 20 and downgraded to Free Plan on May 25.

**Actual payments:**
1. **May 20 (Year 1)**: \$9 × 10 × 12 = \$1,080
2. **May 20 (Year 2)**: Downgrade to Free Plan (no charge)

### Switching from Monthly to Annual Billing

The change takes effect immediately.

**Formula:**
- Current monthly charge = Monthly plan price × Current team size
- Annual charge (pay difference) = (Annual plan price × Current team size × 12) - (Monthly plan price × Current team size × Unused days ÷ Days in month)

### Switching from Annual to Monthly Billing

The change does NOT take effect immediately. The annual plan continues until the end of the subscription period, then the monthly plan activates.

**Formula:**
- Annual order price = Annual plan price × Current team size × 12
- Monthly order price = Monthly plan price × Current team size (starts after annual expires)

## FAQs

### Are paid plans available for both web and desktop?

Yes, all plans include Mac, Windows, Web, and Linux applications.

### Can I get a free trial?

- **14-day free trial** available when you provide payment information
- Billing occurs automatically after the trial period
- Cancel anytime during the trial and continue using the service for the remaining trial days

### How do I cancel my subscription?

**Option 1: Via Apidog**
1. Go to **Team** → **Plan**
2. Click **Upgrade Plan**
3. Click **Downgrade** under the Free Plan

**Option 2: Via Stripe**
1. Go to **Invoices**
2. Click **Manage Plan**
3. Click **Cancel plan** on the Stripe page

:::info[]
The downgrade takes effect at the end of your billing interval.
:::

### Who can manage subscriptions?

| Role | Permissions |
|------|-------------|
| **Team Administrator** | Upgrade, downgrade, modify payment information |
| **All Team Members** | Contribute personal credits to the team |
| **Email Notifications** | Sent exclusively to team administrators |

### What happens after downgrading?

Your team can continue using higher-tier plan features normally until the end of the plan's billing cycle.

### Why are invoices sometimes different from the plan price?

Invoices may differ due to:

| Reason | Impact |
|--------|--------|
| **Payment with Credits** | Invoice reflects discounted price after applying credits |
| **Adding/removing members** | Invoice adjusted based on membership duration |
| **Plan upgrades/downgrades** | Invoice reflects price difference for the time period |
| **Switching billing intervals** | Invoice adjusted for appropriate pricing based on chosen interval |

### What if I live in a region with a mandatory refund policy?

If you live in the European Union, United Kingdom, or another region with mandatory refund policies:
- **Standard refund period**: 72 hours
- **EU extended period**: 14 days beyond the standard period

To initiate a refund, contact us:
- **Via app**: Use the in-app support
- **Via email**: sales@apidog.com

Please inform us if there's a mandatory refund policy in your region.

### Unable to use credit card or need invoice first?

We support generating an invoice first for budget requests or audits. Payment can be made via credit card or bank transfer depending on your team's situation.

See the [Alternative Payment Methods](https://docs.apidog.com/alternative-payment-methods-617224m0.md) documentation for details.

