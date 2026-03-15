# AWS Support Plans README

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

## Best for

* learners
* personal projects
* very small workloads
* non-critical use cases

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

## Easy memory line

**Basic = self-service support only.**

---

# 2) AWS Developer Support

## Best for

* developers building apps
* testing environments
* proof-of-concept work
* non-production workloads

## Main features

* everything in Basic
* technical support cases
* support from Cloud Support Engineers during **business hours**
* general architectural guidance
* one primary contact
* support automation workflows
* more support features than Basic

## Typical response times

* **System impaired:** less than 12 business hours
* **General guidance:** less than 24 business hours

## What to remember

* good for **development and testing**
* not the normal answer for serious production workloads
* technical support is available during **business hours**, not full 24/7 coverage

## Easy memory line

**Developer = technical help while building.**

---

# 3) AWS Business Support

## Best for

* production workloads
* teams that need faster incident help
* companies that want **24/7 access** to AWS support engineers

## Main features

* everything in Developer
* **24/7** access to Cloud Support Engineers
* support by **email, phone, chat, and web**
* unlimited cases and contacts
* full Trusted Advisor checks
* AWS Support API
* support for common third-party software questions
* architectural guidance
* support automation workflows

## Typical response times

* **Production system down:** less than 1 hour
* **Production system impaired:** less than 4 hours
* **System impaired:** less than 12 hours
* **General guidance:** less than 24 hours

## What it does **not** include

* no dedicated TAM
* less proactive than Enterprise

## Easy memory line

**Business = production support with 24/7 access, but no TAM.**

---

# 4) AWS Enterprise Support

## Best for

* business-critical workloads
* large organizations
* mission-critical systems
* companies that want proactive and strategic AWS guidance

## Main features

* everything in Business
* **dedicated Technical Account Manager (TAM)**
* fastest response times
* proactive guidance and planning
* architecture and operational reviews
* launch and event planning support
* concierge-style billing and account help
* stronger long-term strategic support

## Typical response times

* **Business-critical system down:** less than 15 minutes
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

## Choose Basic when

* you only need billing and account help
* you are learning AWS
* you are okay using docs and re:Post instead of opening technical cases

## Choose Developer when

* you are building or testing an application
* you need technical help from AWS
* your environment is not a critical production system

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

## Trap 4: Forgetting the TAM keyword

When you see **TAM**, think **Enterprise**.

---

# Real-world examples

## Example 1: Student using AWS labs

A student uses AWS for learning and only needs billing help, docs, and health information.

**Best plan:** Basic

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
