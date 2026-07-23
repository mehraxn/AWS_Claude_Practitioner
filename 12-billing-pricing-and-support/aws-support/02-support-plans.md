# AWS Support plans

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

<!-- Source provenance is maintained in docs/reorganization/PHASE-4-CANONICAL-SOURCE-MAP.csv. -->

### AWS Cloud Practitioner (CLF-C02) — Exam-Ready Reference

---

## 📌 Quick Overview Table

 Feature  Basic  Developer  Business  Enterprise On-Ramp  Enterprise
------------------
 Price  Free  $29mo (or 3% of usage)  $100mo (or 10% of usage)  $5,500mo (or 10% of usage)  $15,000mo (or 10% of usage)
 Target  All AWS customers  DevTest environments  Production workloads  Business-critical workloads  Mission-critical workloads
 AWS Trusted Advisor  7 core checks  7 core checks  Full checks  Full checks  Full checks
 Technical Support  ❌ None  1 contact, business hours  Unlimited contacts, 247  Unlimited contacts, 247  Unlimited contacts, 247
 Support Channels  Docs, forums, Service Health Dashboard  Email only  Email, Chat, Phone  Email, Chat, Phone  Email, Chat, Phone
 TAM (Technical Account Manager)  ❌  ❌  ❌  ✅ Pool of TAMs (shared)  ✅ Dedicated TAM
 Concierge Support Team  ❌  ❌  ❌  ✅  ✅
 AWS Health API  ❌  ❌  ✅  ✅  ✅
 3rd-Party Software Support  ❌  ❌  ✅  ✅  ✅
 Infrastructure Event Management  ❌  ❌  For a fee  ✅ (1 per year)  ✅
 Operations Reviews  Well-Architected  ❌  ❌  ❌  ✅  ✅

---

## 🟢 TIER 1 — Basic Support

### What It Is
The default plan automatically included for every AWS account at no charge.
No additional signup required — it activates the moment you create an AWS account.

### What You Get
- Access to AWS documentation, whitepapers, and best-practice guides
- Access to AWS rePost (community Q&A forum, formerly AWS Forums)
- Access to AWS Service Health Dashboard (global service status)
- Access to AWS Health Dashboard (your account's specific service health)
- 7 core AWS Trusted Advisor checks (basic security + service limits only)
  - S3 Bucket Permissions
  - Security Groups – Specific Ports Unrestricted
  - IAM Use
  - MFA on Root Account
  - EBS Public Snapshots
  - RDS Public Snapshots
  - Service Limits
- Billing and account support only (not technical)

### What You Do NOT Get
- No access to AWS Support Engineers
- No case submission for technical issues
- No chat, phone, or email technical support
- No Trusted Advisor full checks

### 🏢 Real-World Examples

Example 1 — Personal Learning Account
 John is learning AWS on a personal account and has no production workloads. He uses Basic Support to access documentation, follow AWS tutorials, and monitor the Service Health Dashboard when he suspects an AWS outage. This is sufficient for non-production, learning purposes.

Example 2 — Small Startup, Pre-Launch
 A two-person startup is building their MVP and has no revenue yet. They cannot justify any support spend. They use Basic Support, rely on AWS rePost for community answers, and accept that if something breaks, they will self-diagnose through documentation.

Example 3 — Internal Tool with No SLA
 A company runs a small internal log archiving job on S3. No one depends on it in real time. They keep it on Basic Support because downtime has zero business impact.

### ⚠️ Exam Traps — Basic Support
 🪤 Trap 1 Basic Support is free, so it includes no AWS Trusted Advisor checks. ❌ WRONG — it includes 7 core checks, just not the full suite.

 🪤 Trap 2 You can call AWS support for billing issues on Basic. ✅ TRUE — billing and account support are always included regardless of plan. Exams try to trick you here.

 🪤 Trap 3 AWS Health Dashboard is only available on paid plans. ❌ WRONG — it's available to everyone, including Basic.

 🪤 Trap 4 AWS rePost is AWS official support. ❌ WRONG — it's a community forum, not official AWS engineer support.

---

## 🔵 TIER 2 — Developer Support

### What It Is
Designed for teams experimenting or developing in AWS — not yet running production workloads.
The entry-level paid support plan.

### Pricing
- $29month, OR 3% of monthly AWS usage — whichever is greater

### What You Get (everything in Basic, PLUS)
- Email support during business hours (Mon–Fri)
- 1 primary contact allowed to open support cases
- General architectural guidance (how services fit together)
- Response time SLAs
   Severity  Response Time
  ------
   General Guidance   24 business hours
   System Impaired   12 business hours
- 7 core Trusted Advisor checks (same as Basic — NOT full)
- Access to the full AWS Support Center portal

### What You Do NOT Get
- No 247 access (business hours only)
- No phone or chat support
- No full Trusted Advisor checks
- No TAM
- No third-party software support
- No Health API

### 🏢 Real-World Examples

Example 1 — Solo Developer Building a SaaS
 Maria is a solo developer building a new SaaS application in staging. She doesn't have production users yet but occasionally hits AWS configuration issues she can't solve through documentation alone. Developer Support lets her email AWS engineers and get a response within 24 hours at a low monthly cost.

Example 2 — University Research Project
 A university team is running ML experiments on EC2 spot instances. Their workloads aren't time-critical. They upgrade to Developer Support so they can email AWS when their AMI launch configurations behave unexpectedly. Business-hours support is sufficient since the team only works weekdays.

Example 3 — Startup in Alpha Testing
 A startup with 10 alpha users needs some AWS guidance on architecting their RDS setup. They're not production yet, so Developer Support gives them access to architectural Q&A without the cost of Business Support.

### ⚠️ Exam Traps — Developer Support

 🪤 Trap 1 Developer Support provides 247 support via email. ❌ WRONG — email support is business hours only.

 🪤 Trap 2 Developer Support allows unlimited contacts to open cases. ❌ WRONG — only 1 primary contact can open cases.

 🪤 Trap 3 Developer Support includes full AWS Trusted Advisor checks. ❌ WRONG — still only 7 core checks, just like Basic.

 🪤 Trap 4 If my monthly AWS bill is $5,000, my Developer Support fee is $29. ❌ WRONG — it's the greater of $29 or 3% of usage. 3% of $5,000 = $150. So you pay $150.

 🪤 Trap 5 Developer Support is suitable for production workloads. ❌ WRONG — it's explicitly for devtest environments.

---

## 🟡 TIER 3 — Business Support

### What It Is
The minimum recommended plan for production workloads. AWS explicitly recommends this tier when you have real users depending on your infrastructure.

### Pricing
- $100month OR a tiered percentage of monthly AWS usage — whichever is greater
   Monthly Usage  Support %
  ------
   First $0–$10,000  10%
   $10,001–$80,000  7%
   $80,001–$250,000  5%
   Over $250,000  3%

### What You Get (everything in Developer, PLUS)
- 247 access via phone, email, AND chat
- Unlimited contacts can open support cases
- Full AWS Trusted Advisor checks (all categories unlocked)
- AWS Health API access (programmatic access to service health events)
- Third-party software support (common OS and application stacks like Linux, Windows, SAP, Oracle, etc.)
- Contextual architectural guidance (based on your specific use case — not just general)
- Infrastructure Event Management for a fee (e.g., planned product launches)
- Response time SLAs
   Severity  Response Time
  ------
   General Guidance   24 hours
   System Impaired   12 hours
   Production System Impaired   4 hours
   Production System Down   1 hour

### What You Do NOT Get
- No TAM (Technical Account Manager)
- No Concierge Support
- No dedicated account management
- No free Infrastructure Event Management (costs extra)
- No proactive Well-Architected reviews

### 🏢 Real-World Examples

Example 1 — E-Commerce Platform
 ShopEasy runs their online store entirely on AWS. They have real customers placing orders 247. If their RDS goes down on a Saturday night, they need to reach AWS immediately. Business Support gives them 247 phone access and a 1-hour SLA for production-down situations.

Example 2 — FinTech Company with Compliance Needs
 A payment processing company uses AWS with third-party Oracle DB. Business Support allows them to get AWS help with Oracle on EC2 configuration issues, something lower tiers don't cover. They also use the AWS Health API to integrate AWS service events into their internal monitoring system.

Example 3 — Growth-Stage Startup
 A startup just hit 50,000 daily active users. They upgrade from Developer to Business Support because they now have an SLA with their enterprise clients. With Business Support, they get full Trusted Advisor checks which flag an S3 bucket misconfiguration they had overlooked.

Example 4 — Media Company Before a Live Stream
 A media company plans a major live sports stream. They pay for Infrastructure Event Management so AWS engineers proactively monitor and assist during the event window.

### ⚠️ Exam Traps — Business Support

 🪤 Trap 1 Business Support includes a TAM. ❌ WRONG — TAM is only available in Enterprise On-Ramp and Enterprise plans.

 🪤 Trap 2 Business Support provides Infrastructure Event Management for free. ❌ WRONG — IEM is available for an additional fee at Business tier. It's only included (1 per year) at Enterprise On-Ramp.

 🪤 Trap 3 The fastest response time on Business Support is 24 hours. ❌ WRONG — for a production system down, it's  1 hour.

 🪤 Trap 4 You need Enterprise Support to get full Trusted Advisor checks. ❌ WRONG — full checks unlock at Business level.

 🪤 Trap 5 Business Support costs a flat $100month. ❌ WRONG — $100 is the minimum, but you pay the greater amount based on usage tiers.

 🪤 Trap 6 AWS Health API access requires Enterprise Support. ❌ WRONG — it's available from Business tier onward.

---

## 🟠 TIER 4 — Enterprise On-Ramp Support

### What It Is
A bridge tier introduced in 2021 between Business and Enterprise. Designed for companies with business-critical workloads that need more than Business Support but aren't ready for the full Enterprise commitment.

 📝 Note This is a relatively new plan that is increasingly tested on the CLF-C02 exam.

### Pricing
- $5,500month OR 10% of monthly AWS usage — whichever is greater

### What You Get (everything in Business, PLUS)
- Pool of Technical Account Managers (TAMs) — not a dedicated TAM, but access to a rotating team of TAMs
- Concierge Support Team — for billing and account optimization
- Infrastructure Event Management — 1 per year included (no extra charge)
- Operations reviews, Well-Architected reviews, Trusted Advisor Priority access
- Proactive guidance — not just reactive support
- Response time SLAs
   Severity  Response Time
  ------
   General Guidance   24 hours
   System Impaired   12 hours
   Production System Impaired   4 hours
   Production System Down   1 hour
   Business-Critical System Down   30 minutes

### Key Differentiator from Enterprise
Enterprise On-Ramp gives you a sharedpool TAM vs Enterprise's dedicated TAM. Think of it as timesharing access to a TAM rather than owning one.

### 🏢 Real-World Examples

Example 1 — Regional Bank
 A regional bank runs its core banking APIs on AWS. They have strict SLAs with corporate clients and need 30-minute response time for business-critical failures. However, they can't justify $15,000month for full Enterprise. Enterprise On-Ramp gives them the 30-minute SLA and access to TAMs at a fraction of the cost.

Example 2 — Healthcare Provider
 A telehealth company with 100,000 patients needs proactive architectural guidance before a major platform migration. The TAM pool in Enterprise On-Ramp reviews their architecture, identifies risks, and helps plan the migration — something Business Support doesn't offer proactively.

Example 3 — Gaming Company at Launch
 A gaming studio is launching a new title with 500,000 registered users. The one included Infrastructure Event Management session per year is used for launch day. TAMs monitor the event alongside internal engineers.

### ⚠️ Exam Traps — Enterprise On-Ramp

 🪤 Trap 1 Enterprise On-Ramp includes a dedicated TAM. ❌ WRONG — it includes access to a pool of TAMs, not a single dedicated one. The dedicated TAM is only in full Enterprise.

 🪤 Trap 2 Enterprise On-Ramp and Enterprise have the same response time SLAs. ❌ WRONG — Enterprise has  15 minutes for business-critical systems. Enterprise On-Ramp is  30 minutes.

 🪤 Trap 3 Enterprise On-Ramp doesn't include Infrastructure Event Management. ❌ WRONG — it includes 1 IEM per year at no extra charge.

 🪤 Trap 4 Only Enterprise Support offers Well-Architected Reviews. ❌ WRONG — Enterprise On-Ramp includes access to Well-Architected reviews too.

 🪤 Trap 5 Enterprise On-Ramp is the same as Business Support with a TAM added. ❌ OVERSIMPLIFIED — it also adds Concierge, better SLAs, IEM, and proactive reviews.

---

## 🔴 TIER 5 — Enterprise Support

### What It Is
The highest tier of AWS support. Designed for mission-critical, large-scale enterprise workloads where downtime carries significant financial, regulatory, or reputational risk.

### Pricing
- $15,000month OR a tiered percentage of monthly usage — whichever is greater
   Monthly Usage  Support %
  ------
   First $0–$150,000  10%
   $150,001–$500,000  7%
   $500,001–$1,000,000  5%
   Over $1,000,000  3%

### What You Get (everything in Enterprise On-Ramp, PLUS)
- Dedicated Technical Account Manager (TAM) — single point of contact who knows your infrastructure deeply
- Concierge Support Team
- Unlimited Infrastructure Event Management sessions
- Proactive Well-Architected reviews — ongoing, not just on request
- AWS Incident Detection and Response (optional add-on available)
- Business Reviews — regular cadence with AWS leadership
- Response time SLAs
   Severity  Response Time
  ------
   General Guidance   24 hours
   System Impaired   12 hours
   Production System Impaired   4 hours
   Production System Down   1 hour
   Business-Critical System Down   15 minutes

### The TAM — Deep Dive
The Technical Account Manager (TAM) is the crown jewel of Enterprise Support
- Acts as your primary technical relationship with AWS
- Conducts regular reviews of your environment
- Proactively flags potential issues before they become incidents
- Coordinates other AWS teams on your behalf
- Helps you plan architectural improvements and cost optimization
- Available for strategic planning (new product launches, compliance, migrations)
- Knows your workloads, not just AWS in general

### 🏢 Real-World Examples

Example 1 — Global Bank
 A global bank with $50Myear AWS spend runs trading platforms that must never go down during market hours. Their TAM proactively scheduled a Well-Architected Review of their trading workloads six months before a major infrastructure refresh, flagging three single points of failure. Response for any business-critical issue is guaranteed in 15 minutes.

Example 2 — Fortune 500 Retail Company
 A major retailer runs Black Friday on AWS. Their TAM personally coordinates with AWS infrastructure teams to ensure capacity in the regions used. The TAM sets up a dedicated communication channel during the event and participates in the pre-launch runbook.

Example 3 — Government  Regulated Industry
 A national healthcare insurer must meet HIPAA, SOC2, and FedRAMP requirements. Their TAM helps translate compliance requirements into AWS architecture decisions, coordinates with AWS compliance teams, and participates in auditor meetings as a technical witness.

Example 4 — Streaming Platform
 A video streaming service with 10 million concurrent viewers cannot afford even 1 minute of downtime. Enterprise Support with a dedicated TAM means AWS engineers already know their architecture before any incident occurs, cutting resolution time dramatically.

### ⚠️ Exam Traps — Enterprise Support

 🪤 Trap 1 Enterprise On-Ramp and Enterprise both offer a TAM, so they're essentially the same. ❌ WRONG — Enterprise On-Ramp = pool of TAMs (shared); Enterprise = 1 dedicated TAM who knows your account specifically.

 🪤 Trap 2 The fastest SLA in all of AWS Support is 1 hour. ❌ WRONG — Enterprise offers  15 minutes for business-critical system down. Enterprise On-Ramp offers  30 minutes.

 🪤 Trap 3 The Concierge Support Team is unique to Enterprise Support. ❌ WRONG — Concierge is available in both Enterprise On-Ramp AND Enterprise.

 🪤 Trap 4 A TAM is just a salesperson. ❌ WRONG — A TAM is a senior technical advocate, not a salesperson. They have deep AWS architectural expertise.

 🪤 Trap 5 Infrastructure Event Management is unlimited only in Enterprise. ✅ TRUE — and this IS tested. Enterprise On-Ramp gets 1year, Business gets it for a fee, lower tiers don't get it at all.

---

## ⚡ Critical Exam Comparison SLA Response Times

 This is one of the most heavily tested areas on the Cloud Practitioner exam.

 Severity Level  Basic  Developer  Business  Ent. On-Ramp  Enterprise
------------------
 General Guidance  ❌  24 business hrs  24 hrs  24 hrs  24 hrs
 System Impaired  ❌  12 business hrs  12 hrs  12 hrs  12 hrs
 Production System Impaired  ❌  ❌  4 hrs  4 hrs  4 hrs
 Production System Down  ❌  ❌  1 hr  1 hr  1 hr
 Business-Critical System Down  ❌  ❌  ❌  30 min  15 min

 🔑 Memory Trick
 - Business-critical SLA exists only in Enterprise tiers
 - On-Ramp = 30 min (think on-ramp, you're not fully on the highway yet — still slower)
 - Enterprise = 15 min (fully on the highway — fastest)

---

## 🔍 Feature-by-Feature Deep Dives

### AWS Trusted Advisor
Trusted Advisor scans your AWS account for best practices across 5 categories
1. Cost Optimization — idle resources, underutilized instances
2. Performance — overloaded instances, high-latency content delivery
3. Security — open ports, missing MFA, public S3 buckets
4. Fault Tolerance — lack of redundancy, low backups
5. Service Limits — approaching AWS quotas

 Plan  Checks Available
------
 Basic & Developer  7 core checks (subset of Security + Service Limits only)
 Business, Ent. On-Ramp, Enterprise  All checks across all 5 categories

 🪤 Exam Trap Trusted Advisor checks for cost optimization require a free account. ❌ WRONG — cost optimization checks require Business or higher.

---

### AWS Health Dashboard vs. Service Health Dashboard

 Dashboard  Available To  Shows
---------
 Service Health Dashboard  Everyone (public)  Global AWS service status
 AWS Health Dashboard  All AWS accounts (free)  Events affecting your specific resources
 AWS Health API  Business+ plans  Programmatic access to AWS Health Dashboard data

 🪤 Exam Trap The AWS Health API requires Enterprise Support. ❌ WRONG — it requires Business Support minimum.

---

### Technical Account Manager (TAM)

 Plan  TAM Access
------
 Basic  ❌ None
 Developer  ❌ None
 Business  ❌ None
 Enterprise On-Ramp  ✅ Pool of TAMs (shared, rotating)
 Enterprise  ✅ Dedicated TAM (yours exclusively)

What a TAM does
- Proactive reviews of your environment (not just reactive support)
- Coordinates AWS internal teams on your behalf
- Assists with migrations, launches, architectural decisions
- Participates in your planning cycles
- Acts as your AWS technical advocate

---

### Concierge Support Team

Available in Enterprise On-Ramp and Enterprise only.

The Concierge team specializes in
- Billing optimization — reviewing your spend, recommending savings plans, reserved instances
- Account questions — navigating AWS organizations, consolidated billing
- NOT a technical support channel — that's the TAM's role

---

### Infrastructure Event Management (IEM)

IEM = AWS engineers proactively monitor your environment during a critical business event (product launch, Black Friday, live stream, major migration).

 Plan  IEM Availability
------
 Basic & Developer  ❌ Not available
 Business  ✅ Available for an additional fee
 Enterprise On-Ramp  ✅ 1 per year included
 Enterprise  ✅ Unlimited, included

---

## 🧠 Master Mnemonics

### Remember the 5 Plans (in order)
Big Dogs Build Exceptional Enterprises
- Basic
- Developer
- Business
- Enterprise On-Ramp
- Enterprise

### Remember when TAM appears
TAM = Top AWS Management — Only in the TOP 2 plans (On-Ramp & Enterprise)

### Remember when 247 phone support starts
Business = Big League — 247 phonechatemail starts at Business

### Remember the critical SLA threshold
30-15 — On-Ramp = 30 min, Enterprise = 15 min (for business-critical)

### Remember Trusted Advisor full checks
3 B's get Full = Business, (Enterprise On-Ramp, Enterprise) — full checks from Business up

---

## 📋 Scenario-Based Practice (Exam Style)

### Scenario 1
 A company runs a mission-critical trading platform on AWS. They need a 15-minute response guarantee and a dedicated AWS engineer who knows their architecture. Which support plan should they choose

✅ Answer Enterprise Support
- Dedicated AWS engineer who knows their architecture = Dedicated TAM
- 15-minute response SLA for business-critical = Enterprise only

---

### Scenario 2
 A startup is in the development phase with no production users. They occasionally need help from AWS engineers during business hours. What is the MOST cost-effective plan

✅ Answer Developer Support
- No production workloads → Business plan unnecessary
- Need email support from AWS engineers → Basic not sufficient
- Business hours acceptable → Developer fits

---

### Scenario 3
 A company wants to programmatically receive AWS health events and integrate them into their monitoring system. What is the minimum plan required

✅ Answer Business Support
- AWS Health API = Business tier minimum

---

### Scenario 4
 A company needs access to ALL AWS Trusted Advisor checks and 247 phone support. What is the MINIMUM plan that satisfies both requirements

✅ Answer Business Support
- Full Trusted Advisor + 247 phone = Business minimum

---

### Scenario 5
 A company is planning a major product launch and wants AWS engineers to proactively monitor their environment on the day of the launch. They don't want to pay extra for this service. What is the MINIMUM plan

✅ Answer Enterprise On-Ramp
- Infrastructure Event Management included (1 per year) without extra charge = Enterprise On-Ramp minimum
- Business has IEM but at additional cost

---

### Scenario 6
 A company wants billing optimization advice and account assistance. Which AWS support feature should they use, and what plan do they need

✅ Answer Concierge Support Team, requires Enterprise On-Ramp or Enterprise

---

### Scenario 7
 A company has a personal AWS account for learning. What support features are available to them at no cost

✅ Answer Basic Support includes
- AWS documentation
- AWS rePost community
- Service Health Dashboard
- AWS Health Dashboard
- 7 core Trusted Advisor checks
- Billing support (not technical)

---

### Scenario 8
 A company's production database just went down completely. What is the maximum response time they should expect if they have Business Support

✅ Answer  1 hour
- Production System Down SLA on Business =  1 hour
- Note Business does NOT have the Business-Critical tier that would give  30 min or  15 min

---

## 🚩 Complete List of Exam Traps (Master Summary)

 #  Trap Statement  Truth
---------
 1  Basic Support has NO Trusted Advisor checks  ❌ Basic has 7 core checks
 2  Full Trusted Advisor requires Enterprise Support  ❌ Full checks start at Business
 3  Developer Support gives 247 email access  ❌ Developer is business hours only
 4  Developer Support allows multiple contacts  ❌ Only 1 primary contact
 5  TAM is available in Business Support  ❌ TAM starts at Enterprise On-Ramp
 6  Enterprise On-Ramp has a dedicated TAM  ❌ It's a poolshared TAM; dedicated TAM is Enterprise only
 7  AWS Health API needs Enterprise  ❌ Requires Business minimum
 8  IEM is free from Business tier  ❌ Business charges extra fee for IEM
 9  Concierge is only in Enterprise  ❌ Concierge is in Enterprise On-Ramp AND Enterprise
 10  Business Support's fastest SLA is 4 hours  ❌ Production System Down =  1 hour
 11  The fastest SLA in AWS is 30 minutes  ❌ Enterprise offers  15 minutes
 12  Developer Support is appropriate for production  ❌ Business is minimum for production
 13  3rd-party software support starts at Enterprise  ❌ Starts at Business
 14  AWS Health Dashboard requires a paid plan  ❌ Available to all accounts free
 15  Enterprise On-Ramp and Business have the same SLAs  ❌ On-Ramp adds  30-min business-critical SLA
 16  TAM is a salesperson  ❌ TAM is a senior technical resource
 17  Support plan costs are flat monthly fees  ❌ You pay the greater of flat fee or % of usage

---

## 🗂️ One-Page Cheat Sheet (Print & Memorize)

```
BASIC     → Free  Docs, forums, 7 TA checks, billing only
DEVELOPER → $29+  Email, biz hours, 1 contact, 7 TA checks
                   SLA 24bh  12bh
BUSINESS  → $100+ 247 Phone+Chat+Email, unlimited contacts
                   Full TA checks, Health API, 3rd-party support
                   IEM (extra fee)
                   SLA 24h  12h  4h  1h
ENT ON-RAMP→$5500+ Pool of TAMs, Concierge, IEM (1yr free)
                   Well-Arch reviews, Proactive guidance
                   SLA + 30 min (biz-critical)
ENTERPRISE → $15000+ DEDICATED TAM, unlimited IEM, Concierge
                    SLA + 15 min (biz-critical)

KEY GATES
247 support    → Business+
Full TA checks  → Business+
Health API      → Business+
3rd-party       → Business+
TAM access      → Enterprise On-Ramp+ (shared)  Enterprise (dedicated)
Concierge       → Enterprise On-Ramp+
IEM free        → Enterprise On-Ramp (1yr)  Enterprise (unlimited)
30 min SLA     → Enterprise On-Ramp+
15 min SLA     → Enterprise only
```

---

## 📚 Additional Topics That Complement This

### AWS Support vs. AWS Professional Services
- AWS Support Plans = Ongoing operational support (reactive + some proactive)
- AWS Professional Services = Project-based consulting for implementations, migrations, transformations
- AWS Partners  APN = Third-party companies certified to provide AWS consulting

### AWS rePost (formerly AWS Forums)
- Community-driven Q&A (like Stack Overflow for AWS)
- Available to ALL customers, including Basic
- NOT official AWS engineer support
- AWS employees do sometimes participate, but it's not guaranteed

### AWS IQ
- Marketplace connecting customers with AWS Certified freelancers
- Not part of the support plan structure
- Pay-as-you-go consulting through verified experts

### AWS Managed Services (AMS)
- AWS operates your infrastructure for you
- Goes beyond Support plans — AWS actually manages and operates your AWS environment
- Separate from Support plans entirely

### Well-Architected Framework (linked to higher support tiers)
The AWS Well-Architected Framework has 6 pillars — TAMs use this as the foundation for reviews
1. Operational Excellence
2. Security
3. Reliability
4. Performance Efficiency
5. Cost Optimization
6. Sustainability

Enterprise On-Ramp and Enterprise plans include Well-Architected reviews as part of the TAM engagement.

---

Last updated for CLF-C02 exam objectives. Prices and features are subject to change — always verify at httpsaws.amazon.compremiumsupportplans

## Additional Distinct Source Material

## What this README covers

This study note explains the **four classic AWS Support plans** that often appear in AWS Cloud Practitioner questions:

* **Basic**
* **Developer**
* **Business**
* **Enterprise**

> **Exam note:** AWS has introduced newer support offerings, but many exam questions and study materials still use this classic 4-plan model. That is why this README focuses on these four plans.

---

## Simple definition

**AWS Support plans** decide:

* how much help you get from AWS
* when you can get that help
* how quickly AWS responds
* whether you get extra guidance such as a **Technical Account Manager (TAM)**

---

## Core idea in plain English

As your workload becomes more important, your support plan should become stronger.

* **Basic** is for self-service help.
* **Developer** is for building and testing.
* **Business** is for production workloads.
* **Enterprise** is for business-critical workloads that need proactive guidance and a dedicated TAM.

---

# 1) AWS Basic Support

## Main features

* included for all AWS customers
* account and billing support
* AWS documentation, whitepapers, and AWS re:Post
* AWS Health Dashboard access
* limited Trusted Advisor checks
* service quota increase requests

## What it does **not** include

* no technical support cases for troubleshooting your workload
* no phone, chat, or email access to AWS engineers for technical issues
* no TAM

## What to remember

* good for **development and testing**
* not the normal answer for serious production workloads
* technical support is available during **business hours**, not full 24/7 coverage

## Typical response times

* **Production system down:** less than 1 hour
* **Production system impaired:** less than 4 hours
* **System impaired:** less than 12 hours
* **General guidance:** less than 24 hours

## What makes it special

The biggest keyword is **TAM**.

A TAM helps with:

* planning
* architecture guidance
* best practices
* reducing risk
* long-term AWS strategy

## Easy memory line

**Enterprise = highest support level, plus a dedicated TAM.**

---

# Quick plan summary

| Plan           | Best use                        | Technical support | Hours          | TAM |
| -------------- | ------------------------------- | ----------------- | -------------- | --- |
| **Basic**      | Learning, billing, self-service | No                | N/A            | No  |
| **Developer**  | Development and testing         | Yes               | Business hours | No  |
| **Business**   | Production workloads            | Yes               | 24/7           | No  |
| **Enterprise** | Business-critical workloads     | Yes               | 24/7           | Yes |

---

# Feature comparison

## A. Access and support channels

| Feature                               | Basic                | Developer      | Business                | Enterprise              |
| ------------------------------------- | -------------------- | -------------- | ----------------------- | ----------------------- |
| Cost level                            | Free                 | Paid           | Paid                    | Highest paid            |
| Account and billing support           | Yes                  | Yes            | Yes                     | Yes                     |
| Documentation / whitepapers / re:Post | Yes                  | Yes            | Yes                     | Yes                     |
| AWS Health                            | Yes                  | Yes            | Yes                     | Yes                     |
| Technical support cases               | No                   | Yes            | Yes                     | Yes                     |
| Technical support hours               | No technical support | Business hours | 24/7                    | 24/7                    |
| Technical contact methods             | None                 | Email          | Email, phone, chat, web | Email, phone, chat, web |

## B. Workload fit and operations

| Feature                       | Basic                 | Developer                                       | Business | Enterprise |
| ----------------------------- | --------------------- | ----------------------------------------------- | -------- | ---------- |
| Best for production workloads | No                    | No                                              | Yes      | Yes        |
| Trusted Advisor level         | Limited / core checks | More than Basic, but not full like higher plans | Full     | Full       |
| Third-party software support  | No                    | Limited                                         | Yes      | Yes        |
| AWS Support API               | No                    | No                                              | Yes      | Yes        |
| Unlimited contacts            | No                    | No                                              | Yes      | Yes        |
| Dedicated TAM                 | No                    | No                                              | No       | Yes        |

## C. Guidance and urgency

| Feature                      | Basic                 | Developer                             | Business                   | Enterprise                            |
| ---------------------------- | --------------------- | ------------------------------------- | -------------------------- | ------------------------------------- |
| Proactive strategic guidance | No                    | Low                                   | Medium                     | High                                  |
| Fastest critical response    | No technical response | 12 business hours for system impaired | 1 hour for production down | 15 minutes for business-critical down |

---

# Direct comparison

## Basic vs Developer

| Point                             | Basic        | Developer               |
| --------------------------------- | ------------ | ----------------------- |
| Technical help from AWS engineers | No           | Yes                     |
| Intended use                      | Self-service | Development and testing |
| Technical support timing          | None         | Business hours          |

**Main idea:** Developer adds technical support cases. Basic does not.

---

## Developer vs Business

| Point                    | Developer      | Business   |
| ------------------------ | -------------- | ---------- |
| Intended use             | Non-production | Production |
| Technical support timing | Business hours | 24/7       |
| Incident response        | Slower         | Faster     |
| Contacts                 | Limited        | Unlimited  |

**Main idea:** Business is the usual exam answer for **production workloads**.

---

## Business vs Enterprise

| Point                  | Business   | Enterprise                           |
| ---------------------- | ---------- | ------------------------------------ |
| 24/7 technical support | Yes        | Yes                                  |
| Dedicated TAM          | No         | Yes                                  |
| Proactive guidance     | Medium     | High                                 |
| Best fit               | Production | Business-critical / mission-critical |

**Main idea:** Enterprise adds the **dedicated TAM** and deeper proactive support.

---

# How to choose the right plan

## Choose Business when

* your application runs in production
* you need **24/7 access** to AWS support engineers
* you want faster incident response
* you do **not** need a dedicated TAM

## Choose Enterprise when

* your workloads are business-critical
* downtime is very expensive
* you want proactive planning and strategic guidance
* you need a **dedicated TAM**

---

# Common exam traps

## Trap 1: Confusing Business and Enterprise

If the question says:

* production workload
* 24/7 access to AWS engineers
* no dedicated TAM needed

The answer is usually **Business**.

If the question says:

* dedicated TAM
* strategic guidance
* mission-critical or business-critical system

The answer is usually **Enterprise**.

---

## Trap 2: Thinking Basic includes technical troubleshooting

It does **not**.

Basic includes:

* billing support
* account support
* documentation
* whitepapers
* AWS Health
* AWS re:Post

But it does **not** include technical support cases for troubleshooting your architecture or workload.

---

## Trap 3: Thinking Developer is for production

Usually not.

Developer is mainly for:

* building
* learning
* testing
* non-production use

For production workloads, the better exam answer is usually **Business**.

---

## Example 2: Startup building a prototype

A startup is still developing and testing a mobile app and wants technical guidance while building.

**Best plan:** Developer

## Example 3: SaaS company with a live production app

A SaaS company runs a production workload and wants 24/7 access to AWS support engineers, but does not need a TAM.

**Best plan:** Business

## Example 4: Bank running mission-critical systems

A bank needs fast incident response, proactive planning, and a dedicated TAM.

**Best plan:** Enterprise

---

# Final summary

AWS Support plans grow stronger as your workload becomes more important:

* **Basic** = self-service and billing help
* **Developer** = technical help for development and testing
* **Business** = 24/7 technical support for production
* **Enterprise** = top-tier support with a dedicated TAM

The most important exam shortcut is:

* **Production without TAM -> Business**
* **Production with dedicated TAM -> Enterprise**

---

# Short exam answer

**AWS Support plan cheat sheet:**

* **Basic:** free plan with billing, account, docs, re:Post, and health support, but no technical cases
* **Developer:** paid plan for development and testing with business-hours technical support
* **Business:** paid plan for production workloads with 24/7 technical support
* **Enterprise:** highest plan with Business features plus a dedicated TAM and proactive guidance

---

# Memory trick

Use this order:

**B -> D -> B -> E**

* **Basic** = Bare minimum
* **Developer** = During development
* **Business** = Business is live
* **Enterprise** = Everything + TAM

A simple sentence to remember:

**Build with Developer, run with Business, scale with Enterprise.**
