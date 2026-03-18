# Target Tracking Scaling Policy

## Simple definition

A Target Tracking Scaling Policy is an Auto Scaling policy in AWS that automatically adds or removes resources to keep a chosen metric close to a target value.

Example keep average CPU utilization around 50%.

---

## Core idea in plain English

Think of it like a thermostat.

You set the temperature you want in a room. The thermostat automatically adjusts heating or cooling to stay near that target.

Target tracking works the same way.

You choose

 a metric, such as CPU usage
 a target value, such as 50%

AWS then automatically scales out when the metric goes above the target and scales in when it goes below the target.

---

## Main use cases

Target tracking scaling is used when you want AWS to automatically keep performance steady without manually setting many alarm thresholds.

Common use cases

 Web applications with changing traffic
 EC2 Auto Scaling groups
 ECS services that need to add or remove tasks
 Applications where CPU or request load changes over time
 Systems that should stay responsive while also saving cost

---

## Key features

 Automatic scaling based on a target metric
 Simple to configure compared to step scaling
 AWS manages CloudWatch alarms for you
 Can scale out and in automatically
 Works well for metrics like CPU utilization or request count per target
 Helps balance performance and cost
 Usually scales in more carefully than it scales out, to protect availability

---

## How it works

### 1. You choose a metric

This is the value AWS watches.

Examples

 Average CPU utilization
 Average request count per target
 ECS service average CPU or memory usage

### 2. You choose a target value

This is the level AWS tries to maintain.

Examples

 CPU at 50%
 Request count per target at a chosen level

### 3. AWS monitors the metric

AWS watches the metric through Amazon CloudWatch.

### 4. AWS scales automatically

 If the metric is above the target, AWS adds capacity
 If the metric is below the target, AWS removes capacity

### 5. AWS keeps adjusting

AWS keeps trying to maintain the metric at or near the target value.

So instead of saying

 “Add 2 instances when CPU is above 70%”

You say

 “Keep CPU around 50%”

That is why target tracking is easier for many workloads.

---

## Why it is important for the exam

For the AWS Certified Cloud Practitioner exam, target tracking scaling is important because AWS often tests whether you understand the simplest and most automatic scaling option.

You should remember this

 Target tracking = easiest dynamic scaling option
 AWS manages alarms automatically
 Good when you want to maintain a metric near a target value

In many exam questions, if the scenario says

 traffic changes automatically
 the company wants less manual work
 the system should maintain performance

then Target Tracking Scaling Policy is often the best answer.

---

## Related AWS services and differences

### Target tracking vs Step scaling

Target tracking

 You set a target value
 AWS decides how to scale
 Easier and more automatic

Step scaling

 You define exact thresholds and responses
 Example add 1 instance at 60%, add 3 at 80%
 More manual and more detailed

Exam tip if the question asks for the simpler or more automatic solution, choose target tracking.

### Target tracking vs Simple scaling

Simple scaling is older and more basic.

It uses one alarm and one scaling adjustment, usually with cooldowns.

Target tracking is smarter, more automatic, and usually preferred.

### Target tracking vs Scheduled scaling

Target tracking reacts to real-time demand.

Scheduled scaling happens at a known time.

Example

 Scheduled scaling add capacity every day at 9 AM
 Target tracking add capacity when CPU rises

### Target tracking and CloudWatch

CloudWatch provides the metrics.

With target tracking, AWS automatically creates and manages the needed CloudWatch alarms.

### Related services

 Amazon EC2 Auto Scaling – scales EC2 instances in an Auto Scaling group
 Amazon ECS Service Auto Scaling – scales ECS tasks
 Application Auto Scaling – scales supported AWS services beyond EC2, such as ECS, DynamoDB, Aurora replicas, and more
 Amazon CloudWatch – provides metrics used for scaling

---

## Common exam traps

### Trap 1 Confusing target tracking with step scaling

If the question gives exact thresholds like

 above 60%, add 1 instance
 above 80%, add 2 more

that is step scaling, not target tracking.

### Trap 2 Forgetting that AWS manages alarms

In target tracking, AWS handles the CloudWatch alarms for you.

If the exam asks for a solution with less operational effort, this is a big clue.

### Trap 3 Thinking target tracking means fixed capacity

It does not keep a fixed number of instances.

It keeps a metric near a target value by changing capacity.

### Trap 4 Mixing it up with scheduled scaling

If demand is predictable by time, scheduled scaling may fit better.

If demand changes based on real traffic, target tracking is usually the better choice.

### Trap 5 Choosing the wrong metric

A good target tracking metric should reflect load in a useful way.

For exam thinking, CPU utilization and request count are common examples.

---

## Easy real-world example

A company runs an online store on Amazon EC2.

On normal days, traffic is small. During promotions, traffic increases quickly.

The company wants the website to stay fast, but it does not want to pay for too many servers when traffic is low.

They create a target tracking scaling policy with

 Metric average CPU utilization
 Target 50%

What happens

 If CPU rises above 50%, AWS launches more EC2 instances
 If CPU drops below 50%, AWS removes some instances

Result

 Good performance during high traffic
 Lower cost during quiet times
 Very little manual work

---

## Final summary

A Target Tracking Scaling Policy is an AWS Auto Scaling policy that automatically keeps a chosen metric close to a target value.

It is one of the easiest and most automatic dynamic scaling methods in AWS.

You choose the metric and target value, and AWS handles the scaling actions for you.

For the exam, remember that target tracking is best when you want

 automatic scaling
 less manual setup
 steady performance
 cost efficiency

---

## Short exam answer

Target tracking scaling policy automatically adds or removes capacity to keep a selected metric, such as CPU utilization, near a target value. It is a simple and highly automated dynamic scaling method in AWS.

---

## Memory trick

Target Tracking = Thermostat Scaling

 Thermostat keeps room temperature near a target
 Target tracking keeps CPU, requests, or another metric near a target

So remember

Set the target, let AWS adjust.
