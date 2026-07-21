"""Report duplicate, versioned, case-only, trailing-space, and similar filenames."""

from __future__ import annotations

import difflib
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION_RE = re.compile(r"(?:^|[\s_.()\-])(v1|v2|final|new|claude[\s_-]+version|claude[\s_-]+code)(?:$|[\s_.()\-])", re.I)


def files() -> list[Path]:
    """Return repository files while excluding Git internals and generated output."""
    return sorted(
        path for path in ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.relative_to(ROOT).parts
        and "__pycache__" not in path.relative_to(ROOT).parts
        and path.relative_to(ROOT).parts[:2] != ("reports", "generated")
    )


def normalized(name: str) -> str:
    """Normalize a filename for duplicate comparison."""
    value = unicodedata.normalize("NFKC", Path(name).stem).casefold().strip()
    value = VERSION_RE.sub(" ", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def report_group(label: str, paths: list[Path]) -> None:
    """Print one candidate group."""
    print(f"{label}:")
    for path in paths:
        print(f"  - {path.relative_to(ROOT).as_posix()}")


def main() -> int:
    """Scan and report candidates without selecting canonical content."""
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
    paths = files()
    groups: list[tuple[str, list[Path]]] = []
    for label, key in (
        ("Case-only filename difference", lambda path: path.name.casefold()),
        ("Trailing-space filename difference", lambda path: path.name.rstrip().casefold()),
    ):
        bucket: dict[str, list[Path]] = defaultdict(list)
        for path in paths:
            bucket[key(path)].append(path)
        for members in bucket.values():
            distinct = {path.name for path in members}
            if len(members) > 1 and len(distinct) > 1:
                groups.append((label, members))
    normalized_groups: dict[str, list[Path]] = defaultdict(list)
    for path in paths:
        if path.name != "README.md":
            normalized_groups[normalized(path.name)].append(path)
    for members in normalized_groups.values():
        if len(members) > 1:
            groups.append(("Same normalized filename", members))
    for path in paths:
        if VERSION_RE.search(path.name):
            groups.append(("Version-suffixed filename", [path]))
    names: dict[str, Path] = {}
    for path in paths:
        key = normalized(path.name)
        if len(key) >= 8 and key not in names:
            names[key] = path
    keys = sorted(names)
    similar_seen: set[tuple[str, str]] = set()
    for index, left in enumerate(keys):
        for right in keys[index + 1:]:
            if left == right:
                continue
            ratio = difflib.SequenceMatcher(None, left, right).ratio()
            if ratio >= 0.88 and (left, right) not in similar_seen:
                similar_seen.add((left, right))
                groups.append((f"Similar filenames ({ratio:.0%})", [names[left], names[right]]))
    if groups:
        for label, members in groups:
            report_group(label, members)
        print(f"Duplicate scan found {len(groups)} candidate group(s); review is required.")
        return 1
    print(f"Duplicate scan passed: {len(paths)} file(s), no candidates found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
