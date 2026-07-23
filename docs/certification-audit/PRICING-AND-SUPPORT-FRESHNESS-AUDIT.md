# Pricing and Support Freshness Audit

Checked: **2026-07-21**. Exact prices, discounts, quotas, plan features, and response times are volatile and must be rechecked at implementation.

| Area | Classification | Finding | Action |
|---|---|---|---|
| AWS Support plan names and features | requires-live-verification | Existing support lessons contain plan comparisons that need line-by-line comparison to the current official Support pages. | Batch 8 factual review; cite checked date. |
| Response times and TAM claims | conceptually-correct-but-date-sensitive | Numeric response commitments and account-team descriptions can change. | Retain concepts only after live verification. |
| Trusted Advisor access | conceptually-correct-but-date-sensitive | Access varies by check and support entitlement. | Avoid blanket all-or-nothing claims. |
| AWS Health terminology | outdated | Older Personal Health Dashboard terminology remains in provenance and may appear in prose. | Use AWS Health Dashboard in active notes. |
| AWS Free Tier | requires-live-verification | Offers and eligibility change. | Cite current Free Tier page and checked date. |
| EC2 On-Demand, Spot, Reserved Instances, Savings Plans | partial-topic | Core models are represented, but comparison depth and current caveats are uneven. | Consolidate decision guidance in Batch 8. |
| Data-transfer and NAT costs | requires-live-verification | Exact charges vary by Region, direction, and architecture. | Teach cost drivers; cite current pricing pages. |
| Exact discounts and free usage | unsupported | Any unreferenced percentage or quantity must not be treated as current. | Verify or remove during Phase 6. |

Primary scope anchors: [CPP guide](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02.html) and [SAA guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03.html). Pricing pages must be consulted for each implementation item.
