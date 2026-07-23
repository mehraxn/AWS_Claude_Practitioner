# Amazon Aurora

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

Amazon Aurora is an AWS-designed MySQL- and PostgreSQL-compatible relational database in the Amazon RDS family.

## Learning Objectives

- Explain Aurora storage, writers, readers, endpoints, and failover.
- Compare provisioned Aurora and Aurora Serverless v2.
- Evaluate Aurora Global Database, security, recovery, and cost.

## Lesson Order

| Order | Lesson | Focus |
|---:|---|---|
| 1 | [Aurora overview](01-overview.md) | Cluster architecture, endpoints, replicas, Serverless, Global Database, security, and cost |
| 2 | [Aurora Provisioned](02-provisioned.md) | Explicitly sized Aurora compute |
| 3 | [Aurora Serverless](03-serverless.md) | Automatically adjusting Aurora compute |

## Certification Focus

- **CPP:** managed relational database, compatibility, availability, and service recognition.
- **SAA:** endpoints, readers, failover, Serverless v2, Global Database, recovery, and cost.

## Related Services, Comparisons, and Patterns

- [Amazon RDS](../amazon-rds/README.md)
- [Database selection guide](../../15-comparisons-and-decision-guides/databases/01-database-selection-guide.md)
- [TLS with RDS and Aurora](../../13-architecture-and-design-patterns/transport-layer-security/02-tls-with-load-balancers-and-rds.md)
- [Back to databases](../README.md)

## Official References

- [Amazon Aurora documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html)
