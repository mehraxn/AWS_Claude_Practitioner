# AWS Budgets

## Simple definition

AWS Budgets is an AWS cost management service that helps you set spending or usage limits and alerts you when you are close to, or over, those limits.

## Core idea in plain English

Think of AWS Budgets like a spending guardrail for your AWS account. You decide how much money, usage, or commitment coverage you want, and AWS Budgets watches it for you. If your spending or usage goes too high, it can alert you and even trigger actions.

## Main use cases

 Set a monthly cloud spending limit.
 Get alerts before costs become too high.
 Track service usage against a target.
 Monitor Reserved Instance (RI) and Savings Plans coverage or utilization.
 Help teams stay within cost targets.
 Automate cost-control actions when thresholds are reached.

## Key features

 Cost budgets for tracking AWS spending.
 Usage budgets for tracking service usage.
 RI and Savings Plans budgets for utilization and coverage.
 Alerts and notifications when actual or forecasted values reach thresholds.
 Forecasting to warn you before the end of the budget period.
 Budget actions to apply automated responses.
 Filtering by service, account, tag, region, and more.
 Custom time periods or recurring budgets.

## How it works

1. You create a budget in the AWS Billing and Cost Management area.
2. You choose what to track, such as cost, usage, RI utilization, or Savings Plans coverage.
3. You set a budget amount or target.
4. You add alert thresholds, such as 80%, 90%, and 100%.
5. AWS Budgets compares your actual and forecasted data to the thresholds.
6. When a threshold is reached, AWS sends notifications.
7. If configured, AWS Budgets can also trigger budget actions.

## Why it is important for the exam

AWS Budgets is important because the Cloud Practitioner exam often tests cost awareness and cost control.

You should know that

 AWS Budgets helps plan and control costs.
 It can alert on actual and forecasted spending.
 It is used for cost governance, not resource performance monitoring.
 It is different from services that only analyze past costs.
 It can help enforce spending rules with budget actions.

## Related AWS services and differences

### AWS Budgets vs Cost Explorer

 AWS Budgets Sets limits, tracks against targets, and sends alerts or actions.
 Cost Explorer Analyzes and visualizes historical cost and usage data.

### AWS Budgets vs AWS Cost and Usage Report (CUR)

 AWS Budgets Good for alerts and simple cost control.
 CUR Detailed raw billing data for deep reporting and analysis.

### AWS Budgets vs AWS Pricing Calculator

 AWS Budgets Tracks real AWS usage and costs after or during usage.
 AWS Pricing Calculator Estimates cost before you deploy.

### AWS Budgets vs CloudWatch

 AWS Budgets Monitors billing, usage, RISavings Plans targets.
 CloudWatch Monitors performance metrics, logs, and operational events.

## Common exam traps

 Trap 1 Thinking AWS Budgets is only for past costs.
  It also supports forecasted alerts.

 Trap 2 Confusing AWS Budgets with Cost Explorer.
  Budgets = limits and alerts. Cost Explorer = analysis and visualization.

 Trap 3 Thinking AWS Budgets monitors CPU or memory.
  That is usually Amazon CloudWatch, not AWS Budgets.

 Trap 4 Assuming it is only for cost budgets.
  It can also track usage, RI utilization, RI coverage, Savings Plans utilization, and Savings Plans coverage.

 Trap 5 Thinking budgets only notify people.
  They can also be connected to budget actions.

## Easy real-world example

A startup wants to keep its AWS bill under $200 per month.

It creates an AWS Budget with

 A monthly cost budget of $200
 Alerts at 80%, 90%, and 100%
 Notifications sent to the finance lead and cloud admin

Now the team gets warned before the bill gets out of control. If they also configure an action, AWS can help apply a cost-control response when the threshold is reached.

## Final summary

AWS Budgets is a cost control service. It helps you define targets for AWS spending or usage, sends alerts when actual or forecasted amounts cross thresholds, and can trigger actions to help control costs.

For the exam, remember it as the AWS service for budget limits, alerts, and cost governance.

## Short exam answer

AWS Budgets is an AWS cost management service that lets you set custom budgets for cost, usage, Reserved Instances, and Savings Plans, then receive alerts or trigger actions when thresholds are reached.

## Memory trick

Budgets = Boundaries for your bill.

If Cost Explorer is the dashboard, AWS Budgets is the alarm system.
