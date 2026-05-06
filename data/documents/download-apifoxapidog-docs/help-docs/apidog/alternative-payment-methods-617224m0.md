# Alternative Payment Methods

If your organization cannot use credit cards or requires an invoice before payment, Apidog supports generating invoices first with payment via credit card or bank transfer.

:::tip[]
Apidog version 2.5.28 or later is required for this feature.
:::

## Getting an Invoice First

### Step 1: Navigate to Plans

1. Go to **Team** → **Plan**
2. Click **Upgrade**

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372034/image-preview)
</Background>

### Step 2: Select Alternative Payment Method

In the subscription plans page, click **"Unable to use the credit card or need an invoice first? Click to upgrade"**

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372038/image-preview)
</Background>

### Step 3: Configure Your Order

Select your desired:
- **Plan**: Basic, Professional, or Enterprise
- **Term**: Annual (monthly not available for this payment method)
- **Seats**: Number of team members

<Background>
![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372037/image-preview)
</Background>

### Step 4: Generate Invoice

Click **Get Invoice** to receive Stripe's invoice information. Use this invoice to:
- Request budget approval
- Complete internal audit processes
- Process payment via credit card or bank transfer

<Background>
![Generated invoice](https://api.apidog.com/api/v1/projects/544525/resources/372039/image-preview)
</Background>

## Understanding the Seat System

The seat system is designed for teams using payment methods that don't involve credit card binding.

### What is a Seat?

A **seat** is a paid position for a team member with:
- **Duration**: Annual (yearly billing)
- **Price**: Billing unit price per seat

:::tip[]
The seat system only applies when you choose payment methods without credit card binding. With credit card binding, Stripe automatically charges or refunds based on actual user count fluctuations, making the seat system unnecessary.
:::

### How Seats Work

| Feature | Description |
|---------|-------------|
| **Purchase** | Buy a fixed number of seats for your team |
| **Flexibility** | Invite or remove members within your seat count |
| **Restriction** | Cannot reduce the number of purchased seats |
| **Reassignment** | Freely reassign seats when members leave |

:::warning[]
Team members with the **Guest** role are also included in paid seats.
:::

**Example:**

Team A has 10 members and purchases 10 seats. All members can access paid features.

Later:
- 2 employees leave
- 3 new employees join

Team A can:
1. Reassign 2 existing seats to 2 new employees
2. Purchase 1 additional seat for the third new employee
3. Total seats: 11

### Reducing Seat Count

You can reduce the number of seats on the purchase page by clicking the **Seats** section.

**If you cannot reduce seats:**
1. Your team likely has members equal to the seat count
2. Remove members from **Team** → **Members/Permissions**
3. Return to the Plan page to purchase fewer seats

## Managing Your Plan

### Purchasing Additional Seats

When your team needs to add new members beyond your current seat count:

**Calculation:**  
Additional seat cost = Seat unit price × Number of additional seats × (Days remaining in order ÷ Total days in order)

**How to add seats:**
1. Go to **Team** → **Plan**
2. Click **Add Seats**
3. Enter the number of seats to purchase
4. System automatically calculates the prorated cost

<Background>
![Add seats button](https://api.apidog.com/api/v1/projects/544525/resources/372040/image-preview)

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/372041/image-preview)   
</Background>

### Renewal and Upgrading

To renew or upgrade your plan:
1. Go to **Team** → **Plan**
2. Click **Upgrade/Renewal**

<Background>
![Upgrade/Renewal button](https://api.apidog.com/api/v1/projects/544525/resources/372042/image-preview)
</Background>


### Switching Between Seat System and Subscription System

#### From Subscription to Seat System

If your team is currently on a subscription plan (monthly or annual) and needs to transition to the seat system:

1. Cancel the existing subscription
2. New seat system order begins after the current billing cycle ends

#### From Seat System to Subscription

If your team is currently on the seat system and wants to switch to a subscription model:

1. Wait until the current prepaid term ends
2. New subscription activates after the existing order expires

## Requesting Contracts and Invoices

### Viewing Invoices

1. Go to **Home** → **Team**
2. Switch to the **Plan** tab
3. Click **Invoices/Manage**

### Requesting a Contract

Contact us via email: **sales@apidog.com**

## FAQs

### What happens when the paid version expires?

- **30-day notice**: Notification sent within the software before expiration
- **Automatic downgrade**: Team reverts to the free version
- **Capacity impact**: If usage exceeds free plan capacity, team functionality will be affected

### How is the price calculated for adding seats mid-order?

Within a single team, all members have the same expiration time.

**Calculation:**  
Cost of adding seats = Original seat price × Number of seats added × (Days remaining in order ÷ Total days in order)

The system automatically calculates the required cost when you click **Add Seats** and enter the number of seats to purchase.

