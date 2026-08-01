# CPP Cloud Fundamentals: Tricky Points and Misunderstandings

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)

## Purpose

Use this file after completing the normal Cloud Fundamentals lessons. It concentrates on the statements, comparisons, and scenario wording that learners most often misunderstand in the AWS Certified Cloud Practitioner exam.

This is an original study guide. It does not reproduce or attempt to reconstruct live certification questions.

## Scope

This file focuses on:

- CLF-C02 Domain 1: Cloud Concepts;
- the AWS shared responsibility model from Domain 2 because it is a foundational cloud concept;
- basic cloud economics, migration, AWS Cloud Adoption Framework, and AWS Well-Architected reasoning;
- concept recognition rather than service configuration.

For the full explanations, review:

- [Cloud Concepts and Benefits](02-cloud-concepts-and-benefits.md)
- [Cloud Value and AWS Design Principles](03-cloud-value-and-design-principles.md)
- [AWS Shared Responsibility Model](01-shared-responsibility-model.md)
- [AWS Well-Architected Framework Fundamentals](04-well-architected-framework-fundamentals.md)
- [AWS Cloud Adoption Framework](05-aws-cloud-adoption-framework.md)
- [Cloud Migration Journey and the 7 Rs](06-cloud-migration-journey-and-7-rs.md)
- [AWS Migration Service Selection](07-migration-service-selection.md)
- [Cloud Economics and Licensing](08-cloud-economics-and-licensing.md)

## How to Use This File

1. Read a section without memorizing isolated keywords.
2. Explain why each incorrect statement is incorrect.
3. For every practice question, explain why all distractors fail.
4. Add personal mistakes to the error-log template near the end.
5. Revisit the normal lesson whenever a comparison still feels uncertain.

## Five Rules That Prevent Many CPP Mistakes

1. **Do not trust absolute words.** Statements containing *always*, *never*, *completely*, *automatically*, or *guaranteed* are often too strong.
2. **Identify what the question asks for.** It might ask for a benefit, a responsibility, a framework, a migration strategy, a service, or a cost concept.
3. **Choose the most direct match.** A distractor can be a real AWS concept but still solve a different problem.
4. **Managed does not mean responsibility-free.** AWS manages more of the stack, but customers still manage data, access, and configuration.
5. **The cloud provides capabilities, not automatic outcomes.** An application is not automatically secure, highly available, scalable, or inexpensive merely because it runs on AWS.

## Common Misconceptions

| Misconception | Correct understanding | Priority |
|---|---|---|
| The AWS Cloud is always cheaper than on-premises infrastructure. | AWS provides cost-optimization opportunities. Poor sizing, idle resources, unnecessary data transfer, and weak governance can still create high costs. | High |
| Cloud computing means using somebody else's computer. | Cloud computing combines on-demand access, self-service, resource pooling, elasticity, measured usage, and managed capabilities. | Medium |
| Scalability and elasticity are identical. | Scalability is the ability to handle growth. Elasticity adds and removes capacity as demand changes. | Very high |
| High availability means zero downtime. | High availability aims to minimize interruption. It does not promise that failures or downtime are impossible. | Very high |
| Fault tolerance and disaster recovery are the same. | Fault tolerance continues operating through failure. Disaster recovery restores service after a disruptive event. | High |
| A backup makes a workload highly available. | A backup supports restoration. It does not keep the workload continuously serving traffic during a failure. | High |
| Moving an application to AWS automatically makes it resilient. | Customers must design the workload across failure boundaries and test recovery. | Very high |
| A Region is one data center. | A Region is a separate geographic area containing multiple Availability Zones. | Very high |
| An Availability Zone is always one building. | An Availability Zone consists of one or more discrete data centers with independent infrastructure. | High |
| Public cloud means customer data is public. | Public cloud refers to the provider model. Customer resources remain logically isolated and access controlled. | Very high |
| Hybrid cloud means using two AWS Regions. | Hybrid cloud integrates on-premises or private environments with public-cloud resources. | High |
| Serverless means no servers exist. | Servers still exist, but AWS manages the underlying infrastructure and much of the platform operation. | Very high |
| A managed service means AWS handles every security task. | The customer still manages data, identities, permissions, application behavior, and supported configuration choices. | Very high |
| AWS is responsible for patching every operating system. | AWS patches the infrastructure it manages. The customer normally patches the guest OS on Amazon EC2. | Very high |
| AWS compliance automatically makes every customer compliant. | AWS provides compliant infrastructure and evidence. Customers must configure and operate workloads according to their own requirements. | Very high |
| Pay-as-you-go means every AWS service uses the same billing unit. | Pricing dimensions vary by service, usage, region, request type, storage, and data transfer. | High |
| Operational expenditure means there can be no upfront cost. | The exam concept is the shift toward ongoing consumption. Some contracts, commitments, migration work, or purchases can still involve upfront spending. | Medium |
| Reserved Instances reserve a specific physical EC2 server for the customer. | Reserved Instances are mainly a pricing and capacity-reservation concept depending on the offering; they are not equivalent to owning a dedicated server. | High |
| AWS Support operates the customer's application. | Support assists with AWS-related guidance and issues. The customer remains responsible for operating the workload unless another managed service or partner agreement applies. | Medium |
| All AWS services are available in every Region. | Service and feature availability can differ by Region. | High |
| A global service stores all customer data in every Region. | Global service scope does not automatically describe where all customer data is stored or processed. | Medium |
| Migrating to AWS automatically modernizes an application. | Rehosting can move an application with minimal change. Modernization requires deliberate architectural changes. | High |
| Retain means a migration has failed. | Retain is a valid decision when a workload should remain where it is for now. | Medium |
| Retire means moving the workload to a cheaper service. | Retire means decommissioning a workload that is no longer needed. | High |
| AWS Migration Hub performs every migration. | Migration Hub provides visibility and tracking. Other tools perform discovery, replication, transfer, or migration. | Very high |
| AWS License Manager grants permission to use any software license in AWS. | License Manager helps track and govern supported licenses. Vendor agreements determine legal eligibility. | High |

## Confusing Concept Comparisons

### Agility, scalability, and elasticity

| Concept | Main question | Example | Common trap |
|---|---|---|---|
| Agility | How quickly can we provision, experiment, and change? | Create a test environment in minutes. | Confusing speed of delivery with capacity changes. |
| Scalability | Can the system handle long-term growth? | Add application servers as the business grows. | Assuming scaling must be automatic. |
| Elasticity | Can capacity grow and shrink with current demand? | Scale out during a sale and scale in afterward. | Treating elasticity as only scaling up. |

**Memory rule:** agility is about **speed of change**, scalability is about **capacity for growth**, and elasticity is about **matching capacity to demand**.

### Availability, fault tolerance, reliability, durability, and disaster recovery

| Concept | What it protects | Core meaning |
|---|---|---|
| High availability | Service access | Minimize interruption and restore service quickly. |
| Fault tolerance | Continued operation | Continue operating when a component fails. |
| Reliability | Correct operation over time | Perform the intended function and recover from failures. |
| Durability | Stored data | Preserve data over time despite hardware failures. |
| Disaster recovery | Major disruption | Restore service and data after a serious event. |

**Trap:** a system can store data durably while the application is temporarily unavailable.

### CapEx, OpEx, fixed cost, variable cost, and TCO

| Term | Meaning | Typical exam signal |
|---|---|---|
| Capital expenditure | Upfront investment in owned assets | Buying servers or building a data center. |
| Operational expenditure | Ongoing cost of running and consuming services | Paying for used cloud resources. |
| Fixed cost | Cost that changes little with short-term consumption | Purchased capacity or facility cost. |
| Variable cost | Cost that changes with consumption | Compute hours, storage used, or requests. |
| Total cost of ownership | Direct and indirect lifetime cost | Hardware, facilities, staffing, maintenance, licensing, and operations. |

**Trap:** OpEx and variable cost are related exam ideas, but they are not perfect synonyms in every accounting context.

### IaaS, PaaS, and SaaS

| Model | Customer controls more of | Provider manages more of | Typical example |
|---|---|---|---|
| IaaS | OS, application, data, configuration | Physical infrastructure and virtualization | Amazon EC2 |
| PaaS | Application code, data, supported configuration | OS and platform layers | Managed application or database platform |
| SaaS | Users, data, and permitted configuration | Complete application stack | Hosted business application |

**Trap:** these are responsibility and abstraction models, not rankings of security or quality.

### Public, private, and hybrid cloud

| Model | Meaning | Not the same as |
|---|---|---|
| Public cloud | Provider-operated cloud infrastructure shared with logical isolation | Publicly accessible customer data |
| Private cloud | Cloud-style environment dedicated to one organization | A private subnet in AWS |
| Hybrid cloud | Integrated on-premises/private environment and public cloud | A Multi-Region AWS deployment |

### Region, Availability Zone, and edge location

| Component | Main purpose | Common misunderstanding |
|---|---|---|
| Region | Geographic deployment and data-residency boundary | One data center |
| Availability Zone | Isolated failure boundary inside a Region | A logical subnet or guaranteed single building |
| Edge location | Deliver or route content closer to users | A full replacement for an AWS Region |

### AWS CAF, Well-Architected Framework, and Well-Architected Tool

| Item | Main focus | Best question wording |
|---|---|---|
| AWS Cloud Adoption Framework | Organization-wide transformation readiness and capabilities | “How should the organization prepare people, governance, platform, security, and operations?” |
| AWS Well-Architected Framework | Workload architecture best practices and trade-offs | “How should this workload be reviewed for security, reliability, performance, cost, operations, and sustainability?” |
| AWS Well-Architected Tool | Service that supports structured workload reviews | “Which AWS service helps document a Well-Architected review?” |

### The 7 Rs of migration

| Strategy | Change level | Best clue |
|---|---:|---|
| Rehost | Low | Move quickly with minimal changes. |
| Relocate | Low at workload level | Move a platform or environment without redesigning individual workloads. |
| Replatform | Low to moderate | Make limited optimizations without full redesign. |
| Refactor or re-architect | High | Redesign for cloud-native capabilities. |
| Repurchase | Product replacement | Move to another product, often SaaS. |
| Retain | No migration now | Keep the workload where it is. |
| Retire | Remove | Decommission what is no longer needed. |

### Migration service recognition

| Requirement | Best starting point | What it does not primarily do |
|---|---|---|
| Discover servers, usage, and dependencies | AWS Application Discovery Service | It does not migrate every discovered workload. |
| Rehost supported servers | AWS Application Migration Service | It is not a database schema-conversion tool. |
| Migrate and replicate database data | AWS Database Migration Service | It does not generally redesign the application. |
| Convert database schema for a different engine | AWS schema-conversion tooling | It is not an offline transfer device. |
| Transfer files and objects online | AWS DataSync | It is not primarily a database replication service. |
| Transfer large data sets offline | AWS Snow Family device | It is not a migration dashboard. |
| Track migration progress | AWS Migration Hub | It does not replace the migration tools. |

### Rightsizing and scaling

| Concept | Purpose | Trap |
|---|---|---|
| Rightsizing | Select an appropriate resource type and size for observed needs. | It is not necessarily automatic. |
| Scaling | Change capacity to meet demand or growth. | Scaling a badly sized design does not remove waste by itself. |
| Scheduling | Turn resources on or off at expected times. | It does not react to unexpected traffic unless combined with other controls. |

## Shared Responsibility Traps

### The fundamental boundary

- **AWS is responsible for security of the cloud:** facilities, physical hardware, foundational networking, and virtualization infrastructure.
- **The customer is responsible for security in the cloud:** data, identities, permissions, configuration, application code, and the layers retained by the selected service model.

### Responsibility changes by service type

| Area | Amazon EC2 | Managed database service | AWS Lambda | Amazon S3 |
|---|---|---|---|---|
| Physical facilities and hardware | AWS | AWS | AWS | AWS |
| Virtualization and underlying platform | AWS | AWS | AWS | AWS |
| Guest operating system | Customer | AWS manages more of this layer | AWS | Not applicable to customer |
| Application code | Customer | Customer application | Customer function code | Customer applications using S3 |
| Data | Customer | Customer | Customer | Customer |
| IAM and access configuration | Customer | Customer | Customer | Customer |
| Supported service configuration | Customer | Customer | Customer | Customer |

### Frequently tested responsibility traps

- AWS providing encryption features does not guarantee that the customer enabled or configured them correctly.
- AWS can provide highly durable infrastructure, but the customer decides retention, access, deletion, and backup strategy.
- AWS patches the EC2 host and infrastructure; the customer normally patches the guest OS and installed applications.
- AWS manages more of the platform for RDS and Lambda, but the customer still owns data classification and access decisions.
- AWS compliance reports describe AWS controls; the customer must still meet workload-specific compliance obligations.
- Root-user protection, IAM permissions, access keys, and resource policies are customer responsibilities.
- A customer can transfer some operational work to AWS without transferring accountability for business data.

## Cloud Economics and Licensing Traps

### Cost optimization does not mean “choose the cheapest item”

A cost-optimized choice satisfies the requirement at the lowest appropriate total cost. A cheaper option that fails security, availability, performance, or compliance requirements is not cost optimized.

### Pay-as-you-go does not eliminate waste

Common sources of waste include:

- oversized resources;
- idle resources;
- forgotten test environments;
- unnecessary data transfer;
- unused storage or snapshots;
- purchasing the wrong commitment;
- failing to scale in;
- poor tagging and ownership visibility.

### Economies of scale

AWS aggregates demand across many customers and operates at large scale. The benefit is not that every individual service becomes free; it is that customers can consume provider-scale infrastructure without building the entire supply chain themselves.

### BYOL versus license included

| Model | Meaning | Key trap |
|---|---|---|
| Bring Your Own License | Use an eligible existing customer license in AWS. | Vendor terms decide eligibility. AWS tooling cannot override the agreement. |
| License included | License cost is included in the AWS service or instance price. | The customer still needs to follow product and service terms. |

### Reserved pricing and flexible pricing

- On-Demand is flexible and suitable for short-term or uncertain use.
- Commitment-based pricing can reduce cost for predictable eligible usage.
- Spot pricing can reduce compute cost for interruption-tolerant workloads.
- Dedicated Hosts can address eligible licensing or tenancy requirements but are not the default low-cost option.

**Trap:** a pricing option is correct only when the workload's usage pattern and constraints match it.

## Framework and Migration Traps

### Well-Architected pillars

| Pillar | Main question | Common confusion |
|---|---|---|
| Operational Excellence | Can we run, observe, and improve the workload effectively? | Treating it as only monitoring. |
| Security | Are identities, data, systems, and events protected? | Assuming encryption alone is sufficient. |
| Reliability | Can the workload perform correctly and recover from failure? | Treating backups as full high availability. |
| Performance Efficiency | Are resources selected and used efficiently as demand changes? | Choosing the biggest resource by default. |
| Cost Optimization | Are we avoiding unnecessary cost while meeting requirements? | Choosing the cheapest option even when it fails requirements. |
| Sustainability | Are we minimizing resource use and environmental impact per outcome? | Treating it as unrelated to efficiency. |

### AWS CAF perspectives

| Perspective | Main concern |
|---|---|
| Business | Strategy, value, and business outcomes |
| People | Skills, culture, leadership, and change |
| Governance | Decision rights, risk, finance, and policy |
| Platform | Cloud foundation, architecture, and delivery environment |
| Security | Protection, assurance, identity, and compliance |
| Operations | Service operation, observability, support, and recovery |

**Memory rule:** AWS CAF is mainly about **organizational transformation**; Well-Architected is mainly about **workload quality**.

### Migration journey

- **Assess:** build the business case, understand the portfolio, and evaluate readiness.
- **Mobilize:** close capability gaps, create the landing foundation, and prepare migration plans.
- **Migrate and modernize:** execute migration waves, validate outcomes, and improve workloads where justified.

**Trap:** the stages are not isolated technical commands. Real programs iterate and learn across waves.

## Exam-Language Dictionary

| Wording in the question | Most likely concept or direction |
|---|---|
| “Provision in minutes” | Agility |
| “Experiment quickly” | Agility |
| “Add and remove capacity with demand” | Elasticity |
| “Support long-term growth” | Scalability |
| “Avoid guessing peak capacity” | Elasticity and variable usage |
| “Reduce large upfront investment” | CapEx-to-OpEx shift |
| “Pay only for consumed resources” | Usage-based pricing |
| “Continue operating after a component fails” | Fault tolerance |
| “Minimize service interruption” | High availability |
| “Restore after a major disruption” | Disaster recovery |
| “Preserve stored data over time” | Durability |
| “Deploy close to worldwide users” | Global reach |
| “Keep some systems on premises” | Hybrid cloud |
| “Move with almost no change” | Rehost |
| “Make limited optimizations during migration” | Replatform |
| “Redesign for cloud-native benefits” | Refactor or re-architect |
| “Replace the existing application with SaaS” | Repurchase |
| “Keep the workload where it is for now” | Retain |
| “Decommission unused application” | Retire |
| “Organization-wide cloud readiness” | AWS CAF |
| “Review one workload against best practices” | Well-Architected Framework |
| “Document a structured architecture review” | AWS Well-Architected Tool |
| “Move database with ongoing replication” | AWS DMS |
| “Move files over the network” | AWS DataSync |
| “Network is too slow for a huge transfer” | AWS Snow Family |
| “See migration progress in one place” | AWS Migration Hub |
| “Existing eligible software licenses” | BYOL |
| “Reduce manual, inconsistent provisioning” | Automation and infrastructure as code |

## One-Word Changes That Change the Answer

| Original wording | Likely answer | Changed wording | New likely answer |
|---|---|---|---|
| “Handle growth” | Scalability | “Grow and shrink automatically with demand” | Elasticity |
| “Minimize downtime” | High availability | “Continue with no interruption after one component fails” | Fault tolerance |
| “Restore after failure” | Disaster recovery | “Keep serving during failure” | High availability or fault tolerance |
| “Move quickly with no changes” | Rehost | “Make limited platform improvements” | Replatform |
| “Make limited improvements” | Replatform | “Redesign for cloud-native features” | Refactor |
| “Prepare the organization” | AWS CAF | “Review the workload” | Well-Architected Framework |
| “Transfer files online” | DataSync | “Replicate a database continuously” | DMS |
| “Track migrations” | Migration Hub | “Perform server rehosting” | Application Migration Service |
| “Use an existing eligible license” | BYOL | “License is bundled into price” | License included |

## Simple Decision Trees

### Identify the cloud benefit

```text
Is the problem about delivery speed?
├── Yes → Agility
└── No
    Is it about changing capacity?
    ├── Add and remove with current demand → Elasticity
    └── Support increasing demand over time → Scalability
```

### Identify the migration strategy

```text
Should the workload be removed?
├── Yes → Retire
└── No
    Should it remain where it is for now?
    ├── Yes → Retain
    └── No
        Replace it with another product?
        ├── Yes → Repurchase
        └── No
            Redesign substantially?
            ├── Yes → Refactor or re-architect
            └── No
                Make limited optimizations?
                ├── Yes → Replatform
                └── Move with minimal change → Rehost or relocate,
                    depending on what is being moved
```

### Select a migration tool category

```text
What is being moved or managed?
├── Database data and ongoing replication → AWS DMS
├── Database schema to another engine → Schema-conversion tooling
├── Files or objects over the network → AWS DataSync
├── Very large data with insufficient network → AWS Snow Family
├── Servers to be rehosted → Application Migration Service
├── Existing environment to be discovered → Application Discovery Service
└── Migration status to be tracked → AWS Migration Hub
```

## True or False: Trick Statements

1. **The cloud is automatically cheaper for every workload.**

   **False.** Cost depends on design, usage, pricing choices, operations, and governance.

2. **Elasticity includes scaling in when demand falls.**

   **True.** Elasticity matches capacity in both directions.

3. **A scalable workload must already be automatically elastic.**

   **False.** A workload can support growth without automatic scale-in and scale-out.

4. **High availability guarantees zero downtime.**

   **False.** It aims to minimize interruption.

5. **Fault tolerance is generally a stronger continuity goal than high availability.**

   **True.** Fault-tolerant systems aim to continue through component failure.

6. **A backup alone keeps an application available during a server failure.**

   **False.** A backup supports recovery, not continuous serving.

7. **A public-cloud resource must be publicly accessible from the internet.**

   **False.** Public cloud describes the provider model, not the resource's access policy.

8. **A hybrid architecture can combine an on-premises environment with AWS.**

   **True.** Integration between private/on-premises systems and public cloud is hybrid cloud.

9. **A Region is a single data center.**

   **False.** It contains multiple Availability Zones.

10. **All AWS services and features are available in every Region.**

    **False.** Regional availability varies.

11. **Serverless means no physical servers exist.**

    **False.** AWS operates the servers and platform.

12. **AWS patches the guest operating system on every EC2 instance.**

    **False.** The customer normally patches the EC2 guest OS.

13. **The customer remains responsible for its data when using a managed service.**

    **True.** Data classification, access, and permitted configuration remain customer responsibilities.

14. **Using an AWS managed service removes all customer security responsibility.**

    **False.** The responsibility boundary shifts but does not disappear.

15. **AWS compliance certifications automatically make the customer's application compliant.**

    **False.** Customer architecture and operations must satisfy the relevant requirements.

16. **Pay-as-you-go means every service is billed per second.**

    **False.** Billing dimensions differ by service.

17. **Rightsizing means selecting capacity that matches workload needs.**

    **True.** It reduces overprovisioning and underprovisioning.

18. **Cost optimization always means selecting the option with the lowest listed price.**

    **False.** The option must first meet all requirements.

19. **AWS CAF and the Well-Architected Framework are two names for the same framework.**

    **False.** CAF addresses organizational transformation; Well-Architected evaluates workloads.

20. **The Well-Architected Tool can support a structured review of a workload.**

    **True.** It helps apply the Framework's review process.

21. **Rehost means substantially redesigning an application for cloud-native services.**

    **False.** Rehost moves with minimal change.

22. **Replatform allows limited optimization without a complete redesign.**

    **True.** It is often described as “lift, tinker, and shift.”

23. **Retain can be a valid migration strategy.**

    **True.** Some workloads should remain in place for technical, legal, or business reasons.

24. **Retire means replacing an application with SaaS.**

    **False.** That is repurchase; retire means decommission.

25. **Migration Hub is mainly used to track and view migration progress.**

    **True.** It does not perform every migration task itself.

26. **AWS DMS is primarily used to transfer general file shares.**

    **False.** It is mainly for database migration and replication.

27. **AWS DataSync can help transfer files and object data online.**

    **True.** It is designed for online data movement.

28. **A Snow Family device is useful when network transfer is impractical.**

    **True.** It supports offline or edge use cases depending on the device and service.

29. **AWS License Manager changes vendor licensing terms.**

    **False.** It helps manage license usage; vendor agreements remain authoritative.

30. **BYOL is valid only when the customer's license terms permit use in AWS.**

    **True.** Eligibility depends on the software vendor's terms.

## Mini Scenario Questions

### Question 1: seasonal traffic

A retailer receives unpredictable traffic during promotions and wants capacity to increase during peaks and decrease afterward.

- A. Agility
- B. Elasticity
- C. Durability
- D. Retain

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — Elasticity.** The requirement is to match capacity to changing demand.

- **A** is tempting because cloud resources can be provisioned quickly, but agility is about delivery and experimentation.
- **C** concerns preservation of stored data.
- **D** is a migration strategy.

</details>

### Question 2: rapid experiment

A development team wants to create a test environment in minutes and delete it after a one-day experiment.

- A. Agility
- B. Fault tolerance
- C. Durability
- D. Dedicated tenancy

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: A — Agility.** Rapid provisioning and experimentation are agility benefits.

- **B** concerns operation through component failure.
- **C** concerns stored data.
- **D** is a tenancy decision, not the stated benefit.

</details>

### Question 3: guest operating system

A company runs software on Amazon EC2. Who normally patches the guest operating system?

- A. AWS
- B. The customer
- C. AWS Artifact
- D. The hardware manufacturer directly

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — The customer.** EC2 is an infrastructure service; the customer manages the guest OS.

- **A** manages the underlying infrastructure and host layers.
- **C** provides access to AWS compliance documentation.
- **D** is not the shared-responsibility answer.

</details>

### Question 4: organizational readiness

A company wants a framework to organize cloud transformation across business, people, governance, platform, security, and operations.

- A. AWS Well-Architected Framework
- B. AWS Cloud Adoption Framework
- C. AWS Migration Hub
- D. AWS Support Center

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — AWS CAF.** Its perspectives cover organizational transformation capabilities.

- **A** reviews workload architecture.
- **C** tracks migration progress.
- **D** is not the transformation framework.

</details>

### Question 5: architecture review

A team wants to evaluate a workload against operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

- A. AWS CAF
- B. AWS Well-Architected Framework
- C. AWS DMS
- D. AWS Artifact

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — AWS Well-Architected Framework.** Those are its six pillars.

- **A** addresses organizational transformation.
- **C** migrates databases.
- **D** provides compliance reports and agreements.

</details>

### Question 6: minimal-change migration

A company must move an existing application quickly without changing its architecture.

- A. Refactor
- B. Rehost
- C. Repurchase
- D. Retire

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — Rehost.** The defining clue is minimal change.

- **A** requires substantial redesign.
- **C** replaces the product.
- **D** decommissions it.

</details>

### Question 7: limited optimization

A company will move a self-managed database to a managed database platform with limited application changes.

- A. Replatform
- B. Retain
- C. Rehost
- D. Retire

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: A — Replatform.** The company makes a limited platform optimization without a full redesign.

- **B** keeps the workload in place.
- **C** implies minimal change and no meaningful platform optimization.
- **D** removes the workload.

</details>

### Question 8: large offline transfer

A company must move hundreds of terabytes, but the available network cannot meet the deadline.

- A. AWS Migration Hub
- B. AWS Snow Family
- C. AWS CAF
- D. AWS Well-Architected Tool

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — AWS Snow Family.** An offline transfer device is appropriate when the network is insufficient.

- **A** tracks migration progress.
- **C** guides organizational adoption.
- **D** supports architecture reviews.

</details>

### Question 9: ongoing database replication

A source database must remain active while changes are copied to a target database to reduce cutover downtime.

- A. AWS DataSync
- B. AWS DMS
- C. AWS Migration Hub
- D. AWS License Manager

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — AWS DMS.** It supports database migration and ongoing replication for supported sources and targets.

- **A** focuses on file and object transfer.
- **C** tracks migration status.
- **D** manages supported license usage.

</details>

### Question 10: online file transfer

A company wants to transfer file data to AWS over the network using a managed data-transfer service.

- A. AWS DataSync
- B. AWS DMS
- C. AWS Artifact
- D. AWS CAF

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: A — AWS DataSync.** It supports online movement of file and object data.

- **B** is for databases.
- **C** provides compliance documentation.
- **D** is a transformation framework.

</details>

### Question 11: existing software license

A company wants to use an existing software license on AWS, and the vendor terms allow it.

- A. License included
- B. Bring Your Own License
- C. Elasticity
- D. Consolidated billing

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B — BYOL.** The customer uses an eligible existing license.

- **A** means the license is included in the AWS price.
- **C** is a capacity concept.
- **D** combines billing across accounts.

</details>

### Question 12: cost-effective choice

Two architectures satisfy every requirement. One costs less over the expected workload lifetime and has similar operational effort.

- A. Select the more expensive design because cloud resources are always better when larger.
- B. Select the lower-total-cost design.
- C. Select both regardless of need.
- D. Return to on premises automatically.

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B.** Cost optimization compares eligible designs after all requirements are met.

- **A** assumes larger or more expensive means better.
- **C** creates unnecessary duplication.
- **D** ignores the stated comparison.

</details>

### Question 13: public cloud

A learner says, “Because AWS is a public cloud, every EC2 instance is open to the internet.” Which response is correct?

- A. Correct; public cloud means public access.
- B. Incorrect; network and access configuration determine reachability.
- C. Correct only for managed services.
- D. Correct only in one Availability Zone.

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B.** Public cloud describes the provider and consumption model, not automatic internet exposure.

- **A**, **C**, and **D** confuse deployment model with access configuration.

</details>

### Question 14: migration tracking

A program manager wants one place to view progress across migration tools and workloads.

- A. AWS Migration Hub
- B. AWS DMS
- C. AWS DataSync
- D. AWS Application Discovery Service

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: A — AWS Migration Hub.** The key word is *track*.

- **B** migrates databases.
- **C** transfers files and objects.
- **D** discovers the existing environment.

</details>

### Question 15: compliance boundary

A company deploys an application on AWS infrastructure that has relevant compliance certifications. Is the application automatically compliant?

- A. Yes, in every case.
- B. No; the customer must still configure and operate the workload according to applicable requirements.
- C. Yes, if it uses EC2.
- D. Yes, if it uses a managed service.

<details>
<summary>Answer and distractor analysis</summary>

**Correct answer: B.** AWS compliance helps customers meet requirements, but customer controls and workload configuration still matter.

- **A**, **C**, and **D** incorrectly transfer all compliance responsibility to AWS.

</details>

## Last-Minute Review

### Ten facts to say aloud

1. The cloud enables cost optimization; it does not guarantee lower cost.
2. Agility is speed, scalability is growth, and elasticity is demand matching.
3. High availability minimizes interruption; fault tolerance continues through failure.
4. A backup is not the same as high availability.
5. Public cloud does not mean public customer data.
6. AWS secures the cloud; customers secure what they place and configure in the cloud.
7. Managed services reduce operational work but do not remove customer responsibility.
8. AWS CAF guides organizational transformation; Well-Architected reviews workloads.
9. Rehost, replatform, and refactor describe increasing levels of change.
10. “Most cost-effective” means the lowest appropriate cost after all requirements are satisfied.

### Dangerous absolute words

Be careful when an option says:

- always;
- never;
- completely;
- automatically;
- guaranteed;
- all responsibility;
- no responsibility;
- every Region;
- zero cost;
- zero downtime.

An absolute statement can be correct, but it needs stronger evidence than a limited statement.

### Confidence check

For each item, select one honest status:

- [ ] I can explain it without notes.
- [ ] I recognize the answer but cannot explain the distractors.
- [ ] I still confuse it with another concept.

Check yourself on:

- [ ] agility, scalability, and elasticity;
- [ ] availability, fault tolerance, durability, and disaster recovery;
- [ ] CapEx, OpEx, fixed cost, variable cost, and TCO;
- [ ] public, private, and hybrid cloud;
- [ ] shared responsibility for EC2, RDS, Lambda, and S3;
- [ ] six Well-Architected pillars;
- [ ] six AWS CAF perspectives;
- [ ] migration journey and 7 Rs;
- [ ] DMS, DataSync, Snow Family, Migration Hub, and discovery tools;
- [ ] BYOL and license included.

## Personal Mistake Log Template

| Date | Question or concept | My answer | Correct answer | Why my answer looked attractive | Exact rule to remember | Review date |
|---|---|---|---|---|---|---|
| YYYY-MM-DD |  |  |  |  |  |  |

## Summary

CPP Cloud Fundamentals questions are usually difficult because several options are true in general while only one directly matches the requirement. Name the requested outcome, avoid absolute claims, apply the correct responsibility boundary, and explain why each distractor solves a different problem.

## References

Sources checked: **2026-08-01**.

- [AWS Certified Cloud Practitioner CLF-C02 exam guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html)
- [CLF-C02 Domain 1: Cloud Concepts](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html)
- [CLF-C02 Domain 2: Security and Compliance](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain2.html)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Well-Architected pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html)
- [AWS Cloud Adoption Framework](https://aws.amazon.com/cloud-adoption-framework/)
- [AWS Prescriptive Guidance: the 7 Rs of migration](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-migration/detailed-portfolio-discovery.html)
