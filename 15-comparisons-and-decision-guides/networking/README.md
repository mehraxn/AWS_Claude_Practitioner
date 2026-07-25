# Networking Decision Guides

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

## Topic Overview

These guides compare network controls, private and hybrid connectivity, DNS policies, edge delivery, and global routing without duplicating canonical service lessons.

## Learning Objectives

- Select between security groups and network ACLs.
- Select endpoints, peering, Transit Gateway, VPN, and Direct Connect.
- Distinguish Route 53, CloudFront, and Global Accelerator decisions.
- Explain availability, security, performance, cost, and operational trade-offs.

## Ordered Guides

| # | Guide | CPP | SAA | Status |
|---|---|:---:|:---:|---|
| 1 | [CloudFront vs Global Accelerator](01-cloudfront-vs-global-accelerator.md) | Yes | Yes | Supporting guide |
| 2 | [Hybrid and multi-VPC connectivity](02-vpc-connectivity-options.md) | Awareness | Yes | Batch 3 expanded |
| 3 | [Security groups vs network ACLs](03-security-groups-vs-network-acls.md) | Yes | Yes | Batch 3 complete |
| 4 | [DNS, edge delivery, and global routing](04-dns-edge-and-global-routing.md) | Yes | Yes | Batch 3 complete |

## Related Services and Patterns

- [Amazon VPC foundations](../../07-networking-and-content-delivery/amazon-vpc/01-overview.md)
- [VPC endpoints and PrivateLink](../../07-networking-and-content-delivery/amazon-vpc/04-endpoint-services.md)
- [Amazon Route 53](../../07-networking-and-content-delivery/amazon-route-53/01-overview.md)
- [Amazon CloudFront](../../07-networking-and-content-delivery/amazon-cloudfront/01-overview.md)
- [AWS Global Accelerator](../../07-networking-and-content-delivery/aws-global-accelerator/01-overview.md)

These decisions support multi-AZ three-tier VPCs, multi-account hubs, centralized egress/inspection, hybrid connectivity, and multi-Region entry points.

## Official References

- [Amazon VPC documentation](https://docs.aws.amazon.com/vpc/)
- [Route 53 routing policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html)
- [Amazon CloudFront documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [AWS Global Accelerator documentation](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

Official references checked: 2026-07-23.

## Navigation

- [Back to comparison guides](../README.md)
