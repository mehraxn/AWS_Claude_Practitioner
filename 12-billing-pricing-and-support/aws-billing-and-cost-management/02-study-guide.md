# 💰 AWS Cloud Practitioner — Fixed vs Variable Costs

 A complete study guide to understand, recognize, and never get tricked by Fixed vs Variable cost questions on the AWS exam.

---

## 📌 Table of Contents

1. [The Core Concept](#the-core-concept)
2. [Fixed Costs — Full Explanation](#fixed-costs)
3. [Variable Costs — Full Explanation](#variable-costs)
4. [Side-by-Side Comparison Table](#comparison-table)
5. [Real-World Analogy](#real-world-analogy)
6. [All AWS Service Examples](#aws-service-examples)
7. [On-Premises vs AWS Cost Model](#on-premises-vs-aws)
8. [⚠️ Exam Traps & Tricks](#exam-traps)
9. [Quick Memory Tricks](#memory-tricks)
10. [Practice Questions](#practice-questions)

---

## The Core Concept

The cloud changed how companies pay for technology.

Before AWS (on-premises), companies had to guess how much infrastructure they needed, buy it upfront, and pay for it forever — whether they used it or not.

With AWS, you only pay for what you actually use, when you use it.

This is the difference between Fixed and Variable costs.

---

## Fixed Costs

### Definition
 A fixed cost is an expense that does not change based on how much you use a resource. You pay the same amount regardless of usage — even if you use it 0% or 100%.

### Key Characteristics
- Paid upfront OR on a recurring schedule regardless of consumption
- Cannot be easily scaled up or down
- You are committed to paying it
- Tied to ownership or long-term agreements
- Common in on-premises  traditional IT environments

### Examples of Fixed Costs

#### Physical Infrastructure
- Buying a physical server → You pay $10,000 whether it runs 1 job or 1 million jobs
- Purchasing networking switches and routers → Fixed price upfront
- Buying storage arrays (SANNAS hardware) → Paid once, regardless of how much data you store
- Purchasing data center floor space → You rent the rack space monthly, used or not

#### Contracts and Agreements
- Signing a 3-year data center lease → You pay every month for 3 years no matter what
- Annual hardware maintenance contracts → Same cost every year
- Software perpetual licenses → You buy the license once at a fixed price
- Internet bandwidth contracts (dedicated line) → You pay for the full pipe, used or not
- Third-party support agreements → Fixed annual fee

#### Human Resources
- Hiring a full-time IT administrator → Fixed salary regardless of workload
- Retaining a DBA (Database Administrator) on staff → Same salary every month
- Hiring a data center security guard → Fixed cost per shift

#### AWS-Specific Fixed Examples
- Reserved Instances (All Upfront) → You pay 100% of the cost upfront for 1 or 3 years, no matter how much you use the instance
- Savings Plans (committed spend) → You commit to spending a fixed dollar amount per hour for 1 or 3 years
- Dedicated Hosts (upfront payment option) → Fixed cost for a physical server dedicated to you

---

## Variable Costs

### Definition
 A variable cost is an expense that changes based on your actual consumption. The more you use, the more you pay. The less you use, the less you pay. If you use nothing, you pay nothing.

### Key Characteristics
- Billed based on actual usage (per second, per GB, per request, per hour)
- Scales automatically with your workload
- No upfront commitment required
- You can stop using it and the cost goes to zero
- This is the default AWS pricing model

### Examples of Variable Costs

#### Compute
- EC2 On-Demand instances → Billed per second (Linux) or per hour (Windows) of actual runtime
- AWS Lambda → Billed per request AND per millisecond of execution time — zero cost when idle
- AWS Fargate → Billed per vCPU and GB of memory per second while tasks are running
- Amazon ECS (Fargate launch type) → Pay only when containers are running
- AWS Batch → Pay only for EC2 or Fargate resources used during job execution

#### Storage
- Amazon S3 → Billed per GB stored per month + per GETPUT request
- Amazon EBS → Billed per GB provisioned per month
- Amazon EFS → Billed per GB of data stored (scales automatically)
- Amazon Glacier → Billed per GB stored + per retrieval request
- AWS Backup → Billed per GB of backup data stored

#### Database
- Amazon DynamoDB (On-Demand mode) → Billed per read and write request
- Amazon Aurora Serverless → Billed per Aurora Capacity Unit (ACU) per second — scales to zero
- Amazon RDS → Billed per hour the DB instance is running
- Amazon Redshift (per-query pricing) → Billed per TB of data scanned per query

#### Networking  Data Transfer
- Data Transfer OUT from AWS → Billed per GB transferred to the internet
- Amazon CloudFront → Billed per GB of data delivered + per HTTP request
- AWS Direct Connect → Billed per GB of data transferred over the connection
- Amazon API Gateway → Billed per million API calls received
- Elastic Load Balancer → Billed per Load Balancer Capacity Unit (LCU) per hour based on traffic

#### Other Services
- Amazon SQS → Billed per million requests
- Amazon SNS → Billed per million publishdelivery requests
- Amazon SES → Billed per 1,000 emails sent
- Amazon Rekognition → Billed per image or video minute analyzed
- Amazon Textract → Billed per page processed
- Amazon Translate → Billed per character translated
- AWS Step Functions → Billed per state transition
- Amazon Comprehend → Billed per unit of text processed

---

## Comparison Table

 Dimension  Fixed Cost  Variable Cost 
---------
 Payment trigger  Time (monthly, annually, upfront)  Usage (per second, per GB, per request) 
 Usage dependency  ❌ No — you pay regardless  ✅ Yes — only pay when you use 
 Scalability  Hard to scale  Scales automatically 
 Risk  High — pay even when idle  Low — costs match workload 
 Predictability  Very predictable  Can vary (but can be estimated) 
 Common in  On-premises  Traditional IT  AWS Cloud 
 Best for  Stable, predictable, 247 workloads  Variable, spiky, or unpredictable workloads 
 Examples  Server purchase, leases, contracts  Per-second EC2, S3 GB-month, Lambda requests 

---

## Real-World Analogy

### Fixed Cost → Buying a Car
- You pay $30,000 upfront
- You pay insurance every month no matter how much you drive
- You pay for parking whether you use it or not
- The car sits in your garage on weekends — you still paid for it

### Variable Cost → Uber
- You only pay when you actually take a ride
- Quiet week You pay almost nothing
- Busy week with lots of trips You pay more
- You never pay for a car sitting idle

AWS is Uber for infrastructure.

---

## AWS Service Examples

### Clearly Variable (Pay-per-use)
 Service  Billing Unit 
------
 Lambda  Per request + per 1ms of duration 
 S3  Per GB stored + per request 
 DynamoDB On-Demand  Per readwrite unit 
 CloudFront  Per GB delivered + per request 
 SQS  Per million requests 
 SNS  Per million notifications 
 API Gateway  Per million calls 
 Aurora Serverless  Per ACU-second 
 Fargate  Per vCPUmemory second 
 Rekognition  Per image analyzed 

### Clearly Fixed (Committed  Upfront)
 Item  Why It's Fixed 
------
 Reserved Instance (All Upfront)  100% paid upfront for 1-3 years 
 Savings Plans  Commit to $hour for 1-3 years 
 Dedicated Host (upfront)  Pay for physical server regardless of usage 
 On-prem server purchase  One-time capital expense 
 Data center lease  Monthly commitment 

### Tricky Middle Ground (Partially Fixed)
 Item  Explanation 
------
 Reserved Instance (No Upfront)  You commit to 1-3 years but pay monthly — still a commitment, partially fixed 
 Provisioned DynamoDB  You provision readwrite capacity in advance — you pay for it even if unused 
 Provisioned Concurrency (Lambda)  You pre-warm Lambda instances — fixed cost regardless of invocations 
 EBS Volumes  You pay per GB provisioned, not per GB used — more fixed-like 

---

## On-Premises vs AWS

 Scenario  On-Premises  AWS 
---------
 Weekend traffic spike  Must buy servers sized for peak — pay for idle capacity all week  Auto Scaling adds instances on weekends, removes them Monday 
 New product launch (uncertain demand)  Buy servers upfront, might be too few or too many  Start small, scale instantly, pay only for actual usage 
 Decommission a workload  Stuck with hardware you bought  Stop the instance → cost goes to $0 immediately 
 Storage growth  Buy storage arrays in large chunks  S3 scales to any size, billed exactly per GB used 
 Disaster recovery  Must buy duplicate hardware for DR site  Spin up resources in another Region only when needed 

The AWS value proposition for variable costs
 You stop paying for capacity you might need and start paying for capacity you actually use.

---

## Exam Traps

### ⚠️ Trap 1 Reserved Instances Sound Variable But Are Fixed
- The trick Reserved Instances save money (up to 72%) so students think they are a cost optimization tool and assume they are still variable.
- Reality When you choose All Upfront or commit to 1-3 years, you have a fixed cost commitment. You pay whether you use the instance or not.
- Remember The discount is the reward for accepting a fixed cost.

---

### ⚠️ Trap 2 Per Hour Sounds Fixed But Is Variable
- The trick Paying per hour sounds like a scheduledfixed payment.
- Reality You only pay for the hours the instance is actually running. Stop the instance = stop the charge. That is variable.
- Key The unit of measurement is small (per hour, per second), but the billing is still usage-based.

---

### ⚠️ Trap 3 EBS Volumes Are Billed on Provisioned Size, Not Used Size
- The trick You provision a 500 GB EBS volume but only use 10 GB. You might think you pay for 10 GB.
- Reality You pay for the full 500 GB provisioned, regardless of how much data is on it. This makes EBS more fixed-like than S3.
- Contrast with S3 S3 bills exactly what you store — pure variable.

---

### ⚠️ Trap 4 Annual Contract Keywords Are Always Fixed
- Watch for these keywords in answers
  - Annual maintenance contract → Fixed
  - Multi-year lease → Fixed
  - Upfront purchase → Fixed
  - Perpetual license → Fixed
  - Committed spend → Fixed

---

### ⚠️ Trap 5 Provisioned DynamoDB Is NOT the Same as On-Demand DynamoDB
- Provisioned mode → You set readwrite capacity units in advance. You pay for them even if not used. → More Fixed
- On-Demand mode → You pay per actual request. Zero traffic = near zero cost. → Pure Variable
- The exam may describe a scenario and ask which mode fits variable cost model — always pick On-Demand.

---

### ⚠️ Trap 6 Data Transfer Has Nuance
- Data Transfer IN to AWS → Always FREE (variable but the variable is always $0)
- Data Transfer OUT to internet → Variable, billed per GB
- Data Transfer between AWS services in the same Region → Often free
- Data Transfer between Regions → Billed per GB — variable
- Don't confuse free with fixed — free is still usage-based, just at $0unit.

---

### ⚠️ Trap 7 The Workload Pattern Clue
- Whenever the exam says workload spikes on weekends or unpredictable traffic → the answer almost always involves variableon-demand pricing.
- Whenever the exam says steady-state workload running 247 for years → Fixed costs (Reserved Instances, Savings Plans) make more financial sense.
- The exam tests whether you can match cost model to workload pattern.

---

### ⚠️ Trap 8 Savings Plans Are a Fixed Commitment
- Savings Plans look attractive and flexible, but they require you to commit to a minimum spend per hour for 1 or 3 years.
- If your actual usage is below that commitment, you still pay the committed amount.
- This is a fixed cost disguised as a flexible product.

---

## Memory Tricks

```
FIXED  = I OWN it, so I OWE it (lease, purchase, contract)
         → You pay regardless of use

VARIABLE = I USE it, so I PAY it (per second, per GB, per request)
           → Zero use = Zero cost
```

```
AWS DEFAULT = VARIABLE
AWS DISCOUNT = you accept FIXED in exchange for lower price
```

```
On-Premises keywords → FIXED
  - Purchase, buy, lease, contract, maintenance, license, upfront

AWS Cloud keywords → VARIABLE
  - Per second, per GB, per request, on-demand, consumption, usage
```

---

## Practice Questions

Q1. A company pays the same amount every month for a server regardless of how busy the server is. What type of cost is this
 ✅ Fixed Cost

Q2. An AWS customer is billed $0.023 per GB stored in S3 each month. In January they store 100 GB, in February 500 GB. What type of cost is this
 ✅ Variable Cost

Q3. A company signs a 3-year Reserved Instance contract and pays everything upfront. Is this fixed or variable
 ✅ Fixed Cost (committed upfront regardless of usage)

Q4. A Lambda function is invoked 0 times one month. What is the Lambda cost
 ✅ $0.00 — This is a variable cost. No usage = no charge.

Q5. Which AWS pricing model best supports a workload with unpredictable, spiky traffic
 ✅ On-Demand (Variable) pricing — scales with usage, no commitment

Q6. A company provisions a 1 TB EBS volume but only writes 50 GB of data. What size are they billed for
 ✅ 1 TB — EBS bills on provisioned size, not used size

Q7. A company has a DBA on a full-time salary to manage databases. Is this fixed or variable
 ✅ Fixed Cost — salary does not change based on database queries

Q8. Which of the following is a variable cost in AWS
- A. Reserved Instance (All Upfront)
- B. Annual support contract
- C. Per-request DynamoDB On-Demand billing
- D. Dedicated Host (upfront payment)
 ✅ C — Per-request billing changes with actual usage

---

## Summary Cheat Sheet

```
┌─────────────────────────────────────────────────────────┐
│                    FIXED COSTS                          │
│  • Server purchase        • Data center lease           │
│  • Hardware maintenance   • Perpetual software license  │
│  • Reserved Instance      • Savings Plans               │
│  • Dedicated Host         • Full-time IT staff salary   │
│  KEY You pay the same amount regardless of usage       │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│                   VARIABLE COSTS                        │
│  • EC2 On-Demand          • Lambda per-request          │
│  • S3 per GB-month        • DynamoDB On-Demand          │
│  • CloudFront per GB      • Fargate per second          │
│  • API Gateway per call   • SQS per million msgs        │
│  KEY You pay based on actual consumption only          │
└─────────────────────────────────────────────────────────┘

THE GOLDEN RULE
  If usage = 0 and cost = 0 → VARIABLE
  If usage = 0 and cost  0 → FIXED
```

---

AWS Cloud Practitioner Study Guide  Fixed vs Variable Costs
Good luck on your exam! 🚀