# AWS Cloud Practitioner and Solutions Architect Associate Notes

![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)
![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)

This repository contains educational study notes for AWS Certified Cloud Practitioner (CPP) and AWS Certified Solutions Architect – Associate (SAA).

> [!IMPORTANT]
> This repository is being reorganized. Existing legacy notes are preserved until the controlled migration and duplicate-consolidation phases are complete.

## Repository Status

Phase 3 controlled migration is complete. Of 185 move-map entries, 135 high-confidence unique notes were moved into canonical category paths and 50 unresolved notes remain preserved in their original locations. Those unresolved files include 38 entries in destination-collision groups, 11 manual-review entries, and one archive-later terminology item.

Duplicate consolidation, terminology review, and content-quality improvement have not yet occurred. Neither certification track nor repository coverage should be considered complete or guaranteed.

## Organization Strategy

Canonical notes are grouped by numbered subject category. Service directories use lowercase kebab-case, lesson files use numbered kebab-case names, and every category has a `README.md` index. Cross-service comparisons live in `15-comparisons-and-decision-guides/`; exam guides, revision material, and practice resources belong in `16-exam-preparation/`.

CPP material emphasizes service recognition, cloud concepts, benefits, basic pricing, and shared responsibility. SAA material adds architecture decisions, integrations, resilience, performance, security, and cost trade-offs. A note may carry both badges when supported by current exam scope.

## Main Sections

- `01-cloud-fundamentals/` through `14-ai-ml-analytics-and-other-services/`: subject notes
- `15-comparisons-and-decision-guides/`: selection guides and service comparisons
- `16-exam-preparation/`: exam-focused review material
- `90-archive/`: traceable historical, duplicate, or obsolete material retained after review
- `docs/`: repository policy, maps, standards, and reorganization records
- `scripts/`: standard-library validation and reporting tools

See the [repository map](docs/repository-map.md) for the complete navigation table.

## Study-Note Structure

Canonical lessons generally start with a service or topic title and supported certification badges, then explain the problem, core concepts, features, use cases, pricing, security, resilience, scalability, cost optimization, certification-specific depth, comparisons, exam scenarios, traps, questions, and references. Awareness-level notes omit sections that would otherwise be empty.

## Navigating and Contributing

Start with a category `README.md`, then follow its topic table. Migrated topics link to their canonical directories; duplicate and uncertain notes remain accessible from the legacy directories until later review. Before proposing or updating a lesson, read [CONTRIBUTING.md](CONTRIBUTING.md), check for duplicates, use the naming standard, distinguish CPP fundamentals from SAA design depth, cite official AWS sources, and run the repository validation commands.

Official AWS documentation and current official exam guides are the primary authorities. Date-sensitive claims must record when they were checked; third-party sources are supplementary. AWS services, prices, quotas, terminology, and exam scopes can change, so verify time-sensitive material against current official sources. These notes are independent educational material and do not guarantee exam outcomes.
