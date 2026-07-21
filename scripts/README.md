# Validation and Reporting Scripts

All tools use Python 3's standard library, ignore `.git`, handle Unicode paths, and leave repository content unchanged except for the explicitly generated report.

| Script | Purpose |
|---|---|
| `validate-file-names.py` | Validate canonical naming rules; use `--foundation-only` or `--all` |
| `validate-markdown-links.py` | Check local Markdown targets and anchors; use `--foundation-only` or `--all` |
| `detect-duplicate-filenames.py` | Report normalized, versioned, case-only, trailing-space, and similar filenames |
| `generate-repository-report.py` | Write `reports/generated/repository-summary.md` |
| `execute-approved-migration.py` | Prepare, dry-run, execute, and finalize the manifest-driven Phase 3 migration |

## Windows PowerShell

```powershell
python scripts/validate-file-names.py --foundation-only
python scripts/validate-markdown-links.py --foundation-only
python scripts/detect-duplicate-filenames.py
python scripts/generate-repository-report.py
python scripts/execute-approved-migration.py --dry-run
```

## Unix-Like Shell

```bash
python3 scripts/validate-file-names.py --foundation-only
python3 scripts/validate-markdown-links.py --foundation-only
python3 scripts/detect-duplicate-filenames.py
python3 scripts/generate-repository-report.py
python3 scripts/execute-approved-migration.py --dry-run
```

Replace `--foundation-only` with `--all` for an audit of legacy content. Repository-wide warnings are reports for review and do not authorize automatic renames or rewrites.

The migration helper also supports `--prepare`, category-filtered execution such as `--category 04 --execute`, and `--finalize`. Execution is explicit, refuses overwrites, and is intended only for an approved migration phase.

[Back to repository home](../README.md)
