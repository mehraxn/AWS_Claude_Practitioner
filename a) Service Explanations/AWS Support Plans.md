# AWS Support Plans README

## What this file covers

This README is a separate study note about the four classic AWS Support plans that are commonly tested in AWS Cloud Practitioner-style questions

1. Basic
2. Developer
3. Business
4. Enterprise

 Important exam note AWS has introduced newer support offerings and is transitioning some older plans. But many exam questions and study materials still use the classic 4-plan comparison. That is why this README focuses on those four plans.

---

## Simple definition

AWS Support plans are service levels that decide how much help you get from AWS, when you can get that help, and what extra support tools and guidance are included.

Think of them like support tiers

 Basic = free, limited help
 Developer = help for building and testing
 Business = help for production workloads
 Enterprise = highest level, with proactive guidance and a dedicated TAM

---

## Core idea in plain English

The more critical your workload is, the stronger support plan you need.

 If you are just learning or using AWS casually, Basic may be enough.
 If you are building or testing applications, Developer may fit.
 If your application is running in production, AWS usually expects Business or higher.
 If your company runs business-critical systems and needs deep guidance, Enterprise is the best fit.

---

# The 4 AWS Support plans

## 1) AWS Basic Support

### Best for

 All AWS customers by default
 Beginners
 Very small projects
 Non-critical workloads

### Main features

 Included at no extra cost
 247 access to

   account and billing support
   AWS documentation
   whitepapers
   AWS rePost community
 AWS Health dashboard access
 Basic Trusted Advisor access (core checks  limited checks)
 Service quota increase requests

### What it does not include

 No technical support cases for architecture or service problems
 No direct technical help from AWS support engineers for troubleshooting your workload
 No phonechat technical support

### Easy memory line

Basic = billing, docs, health, and community — not technical troubleshooting.

---

## 2) AWS Developer Support

### Best for

 Early development
 Testing
 Proof of concept work
 Non-production workloads

### Main features

 Everything in Basic, plus
 Business-hours access to Cloud Support Engineers by email
 General architectural guidance
 Unlimited technical support cases
 One primary contact can open cases
 AWS Health
 Trusted Advisor access beyond Basic core support level
 AWS Support Automation Workflows

### Typical response times

 System impaired less than 12 business hours
 General guidance less than 24 business hours

### What to remember

 Good for development, not for serious production needs
 Support is business hours, not full 247 engineer access for technical issues
 Usually email-based technical support

### Easy memory line

Developer = technical help while building, but only during business hours.

---

## 3) AWS Business Support

### Best for

 Production workloads
 Companies that need fast help during incidents
 Teams that want 247 access to AWS support engineers

### Main features

 Everything in Developer, plus
 247 access to Cloud Support Engineers
 Support by phone, chat, email, and web
 Unlimited cases and contacts
 Full Trusted Advisor checks
 AWS Support API
 Third-party software support guidance
 Architectural guidance
 Support Automation Workflows
 Faster response times for production incidents

### Typical response times

 Production system down less than 1 hour
 Production system impaired less than 4 hours
 System impaired less than 12 hours
 General guidance less than 24 hours

### What it does not include

 No dedicated Technical Account Manager (TAM)
 Less proactive and strategic than Enterprise

### Easy memory line

Business = production support, 247 engineers, but no dedicated TAM.

---

## 4) AWS Enterprise Support

### Best for

 Business-critical workloads
 Large organizations
 Mission-critical applications
 Companies that want both reactive and proactive support

### Main features

 Everything in Business, plus
 Designated Technical Account Manager (TAM)
 Fastest standard response times
 Proactive guidance and strategic support
 Help with architecture reviews and operational planning
 Stronger support for events, launches, and critical workloads
 Concierge-style help for billing and account matters
 Access to advanced proactive services
 Full Trusted Advisor access and deeper operational guidance

### Typical response times

 Business-critical system down less than 15 minutes
 Production system down less than 1 hour
 Production system impaired less than 4 hours
 System impaired less than 12 hours
 General guidance less than 24 hours

### What makes it special

The biggest difference is the dedicated TAM.

A TAM is not just a support agent. A TAM helps your company with

 planning
 best practices
 architectural guidance
 risk reduction
 long-term AWS strategy

### Easy memory line

Enterprise = highest support level, with a TAM and proactive guidance.

---

# Quick comparison table

 Feature                                Basic                  Developer                                Business                    Enterprise                            
 -------------------------------------  ---------------------  ---------------------------------------  --------------------------  ------------------------------------- 
 Cost                                   Free                   Paid                                     Paid                        Highest paid                          
 Account and billing support            Yes                    Yes                                      Yes                         Yes                                   
 Documentation  rePost  whitepapers  Yes                    Yes                                      Yes                         Yes                                   
 AWS Health                             Yes                    Yes                                      Yes                         Yes                                   
 Technical support cases                No                     Yes                                      Yes                         Yes                                   
 Technical support hours                No technical cases     Business hours                           247                        247                                  
 Contact methods for technical help     None                   Email                                    Phone, chat, email, web     Phone, chat, email, web               
 Best for production workloads          No                     No                                       Yes                         Yes                                   
 Full Trusted Advisor                   No                     No  limited compared with higher plans  Yes                         Yes                                   
 Third-party software support           No                     Limited  not main focus                 Yes                         Yes                                   
 AWS Support API                        No                     No                                       Yes                         Yes                                   
 Dedicated TAM                          No                     No                                       No                          Yes                                   
 Proactive strategic guidance           No                     Low                                      Medium                      High                                  
 Fastest response for critical issues   No technical response  12 business hours for system impaired    1 hour for production down  15 minutes for business-critical down 

---

# Compare them directly

## Basic vs Developer

 Basic is mostly self-service.
 Developer adds technical support for people who are building and testing.
 If you need AWS engineers to answer technical questions, choose Developer or above.

Main difference Developer adds technical support cases.

---

## Developer vs Business

 Developer is for non-production and business-hours help.
 Business is for production and includes 247 access to AWS support engineers.
 Business also gives better incident response and more complete support features.

Main difference Business is the normal answer for production workloads.

---

## Business vs Enterprise

 Both support production systems.
 Business gives 247 technical support.
 Enterprise adds a dedicated TAM, more proactive planning, and stronger strategic support.

Main difference Enterprise is for organizations that need a long-term AWS partner, not just incident support.

---

# How to choose the right plan

## Choose Basic when

 You only need billingaccount help
 You are learning AWS
 Your workload is not important or not in production

## Choose Developer when

 You are building or testing
 You need technical help during development
 Your app is not a critical production system

## Choose Business when

 Your application runs in production
 You need 247 support access
 You need faster response during incidents
 You do not need a dedicated TAM

## Choose Enterprise when

 Your workloads are business-critical
 Downtime is very expensive
 You want strategic and proactive AWS guidance
 You need a dedicated TAM

---

# Common exam traps

## Trap 1 Confusing Business and Enterprise

A question says

 production workload
 247 technical access
 no dedicated TAM needed

Answer Business

If the question says

 dedicated TAM
 proactive guidance
 business-critical or mission-critical

Answer Enterprise

---

## Trap 2 Thinking Basic includes technical troubleshooting

It does not.

Basic helps with

 billing
  n- account
 documentation
 health info
 community support

But it does not provide technical support cases.

---

## Trap 3 Thinking Developer is good for production

Usually no.

Developer is mainly for

 learning
 building
 testing
 non-production workloads

For production, the safer exam answer is usually Business.

---

## Trap 4 Forgetting the TAM keyword

When you see TAM, think Enterprise.

---

# Real-world examples

## Example 1 Small student project

A student uses AWS for practice labs and needs only billing help and documentation.

Best plan Basic

## Example 2 Startup building an app

A startup is still testing a web app and wants technical help during development.

Best plan Developer

## Example 3 SaaS company with production incidents

A SaaS company runs a live app and wants 247 access to AWS engineers, but does not need a TAM.

Best plan Business

## Example 4 Large bank running critical systems

A bank runs business-critical applications and wants strategic help, fast response, and a TAM.

Best plan Enterprise

---

# Final summary

AWS Support plans increase in value as your workload becomes more important

 Basic = free and self-service
 Developer = support for building and testing
 Business = 247 support for production
 Enterprise = top-tier support with a dedicated TAM

For exam questions, the most important rule is

 Production without TAM - Business
 Production with dedicated TAM  strategic guidance - Enterprise

---

# Short exam answer

AWS Support plan cheat sheet

 Basic free, billingaccount, docs, health, no technical cases
 Developer business-hours technical support for development and testing
 Business 247 technical support for production workloads
 Enterprise Business features plus dedicated TAM and proactive strategic guidance

---

# Memory trick

Use this order

B-D-B-E

 Basic = Bare minimum
 Developer = During development
 Business = Business is live in production
 Enterprise = Everything plus TAM

A simple sentence to remember

“Build with Developer, run with Business, scale with Enterprise.”
