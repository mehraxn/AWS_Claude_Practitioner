# Exam Preparation

These canonical guides teach requirement extraction, service selection, distractor elimination, and architecture trade-offs using original scenarios. They do not contain exam dumps or questions recalled from live certification exams.

| Topic | CPP | SAA | Status |
|---|:---:|:---:|---|
| [CPP scenario reasoning](01-cpp-scenario-reasoning.md) | Core | — | Domain-linked CLF-C02 reasoning and service recognition |
| [SAA architecture scenario reasoning](02-saa-architecture-scenario-reasoning.md) | — | Core | Constraint-driven SAA-C03 architecture selection |

## How to Use These Guides

1. Review the linked canonical lesson for a weak domain.
2. Solve scenarios by writing the requirement and constraints before looking at alternatives.
3. Explain why each rejected option fails a requirement.
4. Recheck current AWS documentation when a service feature, quota, price, or product name matters.

Official exam guides and service lists are the scope authority, but AWS describes service lists as non-exhaustive and subject to change. These notes support study; they do not guarantee exam success.

## CPP Study Path

1. [Cloud fundamentals](../01-cloud-fundamentals/README.md) and [global infrastructure](../02-global-infrastructure/README.md).
2. [Identity and governance](../03-identity-governance-and-organizations/README.md), then [security and compliance](../09-security-and-compliance/README.md).
3. [Compute](../04-compute/README.md), [storage](../05-storage/README.md), [databases](../06-databases/README.md), and networking awareness in [networking and content delivery](../07-networking-and-content-delivery/README.md).
4. [Monitoring and management](../10-monitoring-management-and-deployment/README.md), [billing, pricing, and support](../12-billing-pricing-and-support/README.md), and migration awareness in [migration and hybrid cloud](../11-migration-and-hybrid-cloud/README.md).
5. Review analytics/AI awareness and the Well-Architected material through the [service index](../docs/service-index.md), then complete the [CPP scenario-reasoning guide](01-cpp-scenario-reasoning.md).

## SAA Study Path

1. Review identity, governance, compute, storage, databases, and [VPC/networking](../07-networking-and-content-delivery/README.md).
2. Study [serverless and application integration](../08-serverless-and-application-integration/README.md), security, monitoring, migration/hybrid connectivity, and analytics selection.
3. Work through [architecture patterns](../13-architecture-and-design-patterns/README.md) for availability, failure behavior, disaster recovery, decoupling, serverless design, and security.
4. Use the [comparison guides](../15-comparisons-and-decision-guides/README.md) to practice service selection and cost, security, performance, and operational trade-offs.
5. Complete the [SAA architecture scenario-reasoning guide](02-saa-architecture-scenario-reasoning.md).

## Final Readiness Checklist

- [ ] Review the current official exam guide and domain outline.
- [ ] Revisit every weak area shown in the CPP or SAA coverage dashboard.
- [ ] Explain why plausible alternatives fail each scenario constraint.
- [ ] Review security, failure behavior, monitoring, and cost for architecture choices.
- [ ] Verify volatile service names, pricing, quotas, and Regional availability in current AWS documentation.
- [ ] Use only original practice material; do not use or share exam dumps.
