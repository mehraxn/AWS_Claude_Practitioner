# Amazon VPC

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Topic Overview

This sequence covers Amazon VPC foundations, routing, security, observability, private service access, VPC-to-VPC connectivity, hybrid gateway components, and NAT design.

## Learning Objectives

- Explain Regional VPC scope and AZ-scoped subnets.
- Plan CIDRs and distinguish public, private, IPv4, IPv6, and Elastic IP addressing.
- Evaluate route tables, internet gateways, NAT gateways, and egress-only gateways.
- Compare security groups with network ACLs and interpret Flow Logs.
- Select endpoints, PrivateLink, peering, Transit Gateway, VPN, or Direct Connect.

## Ordered Lessons

| # | Lesson | CPP | SAA | Status |
|---|---|:---:|:---:|---|
| 1 | [Amazon VPC foundations](01-overview.md) | Yes | Yes | Batch 3 complete |
| 2 | [Security groups](02-security-groups.md) | Yes | Yes | Supporting lesson |
| 3 | [VPC Flow Logs](03-flow-logs.md) | Yes | Yes | Supporting lesson |
| 4 | [VPC endpoints and PrivateLink](04-endpoint-services.md) | Awareness | Yes | Batch 3 expanded |
| 5 | [VPC peering](05-vpc-peering.md) | Awareness | Yes | Supporting lesson |
| 6 | [Customer gateway](06-customer-gateway.md) | Awareness | Yes | Supporting lesson |
| 7 | [Virtual private gateway](07-virtual-private-gateway.md) | Awareness | Yes | Supporting lesson |
| 8 | [NAT gateway](08-nat-gateway.md) | Yes | Yes | Supporting lesson |
| 9 | [Subnets, route tables, and internet gateways](09-subnets-route-tables-and-internet-gateways.md) | Awareness | Yes | Batch 3 complete |

## CPP Focus

Recognize VPCs, subnets, routes, gateways, security controls, Flow Logs, endpoints, and public, private, or hybrid connectivity.

## SAA Focus

Design non-overlapping address plans, multi-AZ tiers, resilient egress, least-privilege controls, private service access, scalable topology, and redundant hybrid connectivity.

## Related Services, Comparisons, and Patterns

- [AWS Transit Gateway](../aws-transit-gateway/01-overview.md)
- [AWS Direct Connect](../aws-direct-connect/01-overview.md)
- [Security groups vs network ACLs](../../15-comparisons-and-decision-guides/networking/03-security-groups-vs-network-acls.md)
- [Hybrid and multi-VPC connectivity](../../15-comparisons-and-decision-guides/networking/02-vpc-connectivity-options.md)
- [DNS, edge delivery, and global routing](../../15-comparisons-and-decision-guides/networking/04-dns-edge-and-global-routing.md)

These lessons support multi-AZ three-tier, hub-and-spoke, centralized egress/inspection, hybrid connectivity, and restricted administrative-access patterns.

## Official References

- [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [AWS PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/index.html)
- [AWS Transit Gateway Guide](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)

Official references checked: 2026-07-23.

## Navigation

- [Back to networking and content delivery](../README.md)
