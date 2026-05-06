# Unable to use credit cards?

We support generating an invoice for your order first, which you use to request/audit your budget, and then, depending on your team's situation, we support payment by credit card/bank transfer.


:::tip[]
To support this, your Apidog version needs to be 2.5.28 or later
:::

## How to get the invoice first?

Team administrators can go to Team Page - Plan and click "Upgrade".
<Background>
![](https://assets.apidog.com/help/assets/images/click-upgrade-0aeb28f15062bf01b3983611f9bcf000.png)
</Background>
In the subscrption plans, click on the text below.
<Background>
![](https://assets.apidog.com/help/assets/images/choose-plan-apidog-73a333c9b1b9624cd74f1e54a65116c6.png)
</Background>
Enter the order page and select the plan, term, seats.

<Background>
![](https://assets.apidog.com/help/assets/images/click-to-upgrade-checkout-571a876dcfb5b9107cbbc5a16e2a4ae5.png)
</Background>

Click on "Get Invoice" to get Stripe's invoice information, which you use to request/audit your budget, and then support credit card/bank transfer for payment, depending on your team's situation.

<Background>

![image.png](https://api.apidog.com/api/v1/projects/544525/resources/358935/image-preview)
</Background>

### What is a seat?
Because of the inconvenience of payment, we have adopted the seat system to manage the staff changes of your paid team. The unit of time is yearly, and the price of the seat is the billing unit price.

:::tip[]
The seat system only applies when you choose payment methods that don't involve credit card binding. When you bind a credit card, Stripe will automatically charge or refund your card based on actual user count fluctuations, making the seat system unnecessary.
:::

What you buy is a paid seat for your team, and you can invite/delete members within the number of seats. After purchasing the seats, the number of seats cannot be reduced.

Within your allocated seats, you can freely change team members at any time. This means if someone leaves your organization, you can remove their access and assign that seat to a new team member without any additional cost.

:::highlight purple 
**Example**
Team A currently has 10 people, so they purchase 10 seats. All team members can now access the paid features. Later, if two employees leave and three new employees join, Team A can simply reassign the two existing seats to two of the new employees and purchase just one additional seat for the third new employee. This brings their total to 11 seats. 

:::

The number of seats in the paid interface can be reduced by clicking on the "Seats" section on the purchase page. If you can't reduce the number of seats, it's usually because your team already has the corresponding number of members, so you can remove the members on the team page - "Members/Permissions", and then click on the Plan to purchase fewer seats.

:::tip[]
Team members with the role of visitors are also included in the paid seats.
:::

## Managing your plan

### Purchasing additional seats

When your team has already purchased the paid version and you want to add new team members, you can do so by purchasing additional seats.

Purchasing additional seats is to purchase additional paid seats within the current team order time. The price is calculated as follows: Seat unit price × number of additional seats × (days remaining in the order ÷ number of days in the order).

On the Team Page, go to Plan section, then click the 'Add Seats' button.
<Background>
![](https://assets.apidog.com/uploads/help/2024/05/29/aeff33f807b6fa8f4bb60690c65deb81.png)

![](https://assets.apidog.com/uploads/help/2024/05/29/681f5b4158d0759f0b024b3632a5c6ac.png)
</Background>

### Renewal/Upgrading plan

On the "Team" - "Plan", click Upgrade/Renewal.
<Background>
![](https://assets.apidog.com/uploads/help/2024/05/29/aeff33f807b6fa8f4bb60690c65deb81.png)
</Background>

### Switch between seat system and subscription system

If your team is currently on a Monthly Basic Plan and needs to transition to a Seat System, the existing subscription will need to be canceled first. A new order for the Seat System will not commence until after the current billing cycle has concluded.

If your team is currently on an Annual Basic Plan and needs to switch to a subscription-only model, you will need to wait until the current prepaid term ends before subscribing. The new subscription cannot be activated until after the existing order has fully expired.

## Requesting a contract and invoice

To see the invoices, please go to the Home - Team page, switch to `Plan` tab, and click on `Invoices/Manage` button.

To request a contract, please contact us by email: sales@apidog.com

## FAQs

**Q: What happens when the paid version expires?**

A: We will send a notification within the software 30 days before the paid version order expires.
When the paid version expires, the team will automatically downgrade to the free version. However, when your group uses capacity, which exceeds the capacity of the current plan, your team's functionality will be affected.


**Q: How to calculate the price for adding seats in the middle of an order?**

A: Within a single team, all members have the same expiration time. The cost of adding seats in the middle of an order = original price of seats × number of seats added × (days remaining in the order / number of days in the order).

You can click on the "Add Seats" button, enter the number of people you want to buy seats for, and the system will automatically calculate the required cost for you.
