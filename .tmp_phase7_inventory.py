from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMPL = ROOT / "docs" / "content-implementation"
OUT = ROOT / "docs" / "final-review" / "PHASE-7-PRE-RELEASE-INVENTORY.csv"
CPP = "![CPP](https://img.shields.io/badge/CPP-Cloud%20Practitioner-2EA44F?style=for-the-badge&logo=amazonaws&logoColor=white)"
SAA = "![SAA](https://img.shields.io/badge/SAA-Solutions%20Architect-0969DA?style=for-the-badge&logo=amazonaws&logoColor=white)"


def rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        return []
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


selected: set[str] = {"README.md"}
phase_ref: dict[str, str] = {"README.md": "Phase 6 closure and Phase 7 navigation"}
risk_hint: dict[str, str] = {"README.md": "critical"}

for directory in ROOT.iterdir():
    if directory.is_dir() and re.match(r"^(?:0[1-9]|1[0-6]|90)-", directory.name):
        readme = directory / "README.md"
        if readme.is_file():
            rel = readme.relative_to(ROOT).as_posix()
            selected.add(rel)
            risk_hint.setdefault(rel, "medium")

for readme in (ROOT / "15-comparisons-and-decision-guides").rglob("README.md"):
    selected.add(readme.relative_to(ROOT).as_posix())
for readme in (ROOT / "16-exam-preparation").rglob("README.md"):
    selected.add(readme.relative_to(ROOT).as_posix())

for rel in [
    "docs/certification-audit/CPP-COVERAGE-DASHBOARD.md",
    "docs/certification-audit/SAA-COVERAGE-DASHBOARD.md",
    "docs/content-implementation/PHASE-6-FINAL-BACKLOG-RECONCILIATION.csv",
    "docs/content-implementation/PHASE-6-FINAL-COVERAGE-RECONCILIATION.md",
    "docs/content-implementation/PHASE-6-FINAL-VALIDATION.md",
    "docs/content-implementation/PHASE-6-COMPLETION-SUMMARY.md",
]:
    selected.add(rel)
    risk_hint[rel] = "critical"
    phase_ref[rel] = "Phase 6 final reconciliation"

for batch in range(1, 11):
    for row in rows(IMPL / f"PHASE-6-BATCH-{batch}-POST-IMPLEMENTATION.csv"):
        rel = row.get("target_path", "")
        if rel and (ROOT / rel).is_file():
            selected.add(rel)
            phase_ref[rel] = f"Phase 6 Batch {batch}: {row.get('backlog_id', '')}"
            risk_hint.setdefault(rel, "medium")
    for row in rows(IMPL / f"PHASE-6-BATCH-{batch}-PRE-IMPLEMENTATION.csv"):
        if row.get("risk_level") not in {"critical", "high"}:
            continue
        rel = row.get("target_path", "")
        if rel and (ROOT / rel).is_file():
            selected.add(rel)
            risk_hint[rel] = row["risk_level"]

for root_name in ["11-migration-and-hybrid-cloud", "12-billing-pricing-and-support", "14-ai-ml-analytics-and-other-services"]:
    for path in (ROOT / root_name).rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        selected.add(rel)
        risk_hint[rel] = "high"

for path in (ROOT / "16-exam-preparation").rglob("*.md"):
    rel = path.relative_to(ROOT).as_posix()
    selected.add(rel)
    risk_hint[rel] = "high"

inventory_by_path = {
    row["canonical_path"]: row
    for row in rows(ROOT / "docs" / "certification-audit" / "CANONICAL-CONTENT-INVENTORY.csv")
}

fields = [
    "path", "file_type", "category", "canonical_owner", "cpp_badge", "saa_badge",
    "has_references", "has_internal_links", "phase_status_reference",
    "last_verification_date", "qa_risk", "planned_review", "notes",
]
output: list[dict[str, str]] = []
for rel in sorted(selected):
    path = ROOT / rel
    if not path.is_file():
        continue
    body = path.read_text(encoding="utf-8", errors="replace") if path.suffix.lower() == ".md" else ""
    inv = inventory_by_path.get(rel, {})
    dates = re.findall(r"20\d{2}-\d{2}-\d{2}", body)
    if rel == "README.md" or "DASHBOARD" in path.name or "FINAL-" in path.name:
        file_type = "control-or-navigation"
    elif path.name == "README.md":
        file_type = "navigation"
    elif rel.startswith("15-"):
        file_type = "comparison"
    elif rel.startswith("13-"):
        file_type = "architecture-pattern-or-reference"
    elif rel.startswith("16-"):
        file_type = "exam-preparation"
    else:
        file_type = "canonical-lesson"
    output.append({
        "path": rel,
        "file_type": file_type,
        "category": rel.split("/", 1)[0],
        "canonical_owner": "yes" if rel in inventory_by_path and file_type == "canonical-lesson" else "no",
        "cpp_badge": str(CPP in body).lower(),
        "saa_badge": str(SAA in body).lower(),
        "has_references": str(bool(re.search(r"^## References\s*$", body, re.M))).lower(),
        "has_internal_links": str(bool(re.search(r"\[[^]]+\]\((?!https?://|#)[^)]+\)", body))).lower(),
        "phase_status_reference": phase_ref.get(rel, "Phase 7 volatile or navigation review"),
        "last_verification_date": max(dates) if dates else inv.get("last_verified", "not-recorded"),
        "qa_risk": risk_hint.get(rel, "low"),
        "planned_review": "full high-risk review" if risk_hint.get(rel) in {"critical", "high"} else "structure, navigation, and consistency review",
        "notes": "Pre-release inventory completed before Phase 7 repository-content repairs.",
    })

with OUT.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(output)

print(f"Created {OUT.relative_to(ROOT).as_posix()} with {len(output)} rows")
