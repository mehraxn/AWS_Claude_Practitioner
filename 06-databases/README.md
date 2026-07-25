# Databases

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Overview

This category covers managed relational, NoSQL, and in-memory database choices authorized for CPP recognition and SAA architecture design.

## Learning Objectives

- Distinguish relational, key-value/document, cache, and analytical workloads.
- Select availability, scaling, consistency, backup, recovery, and multi-Region features.
- Apply private access, least privilege, encryption, monitoring, and cost trade-offs.

## Lesson Order

| Order | Topic | CPP | SAA | Status |
|---:|---|:---:|:---:|---|
| 1 | [Amazon RDS](amazon-rds/README.md) | Yes | Yes | Batch 4 complete |
| 2 | [Amazon Aurora](amazon-aurora/README.md) | Yes | Yes | Batch 4 expanded |
| 3 | [Amazon DynamoDB](amazon-dynamodb/README.md) | Yes | Yes | Batch 4 complete |
| 4 | [Amazon ElastiCache](amazon-elasticache/01-overview.md) | Yes | Yes | Batch 4 expanded |

## CPP Focus

Recognize RDS as managed relational, Aurora as AWS-designed MySQL/PostgreSQL-compatible relational, DynamoDB as managed key-value/document NoSQL, and ElastiCache as in-memory caching.

## SAA Focus

Design around data/access model, transactions and consistency, HA and replication, backup/recovery, scaling, connections, caching, security, failure behavior, and cost.

## Related Services and Comparisons

- [Database selection guide](../15-comparisons-and-decision-guides/databases/01-database-selection-guide.md)
- [Amazon Redshift](../14-ai-ml-analytics-and-other-services/analytics/amazon-redshift/01-overview.md)
- [AWS Backup](../05-storage/aws-backup/01-overview.md)
- [VPC endpoints](../07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md)
- [Architecture patterns](../13-architecture-and-design-patterns/README.md)

## Official References

- [AWS database services](https://aws.amazon.com/products/databases/)
- [AWS database decision guide](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html)

[Back to the repository learning map](../README.md)
