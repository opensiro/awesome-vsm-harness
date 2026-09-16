#!/usr/bin/env python3
"""Validate deterministic Awesome VSM Harness relationships to the canonical Index."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

INDEX_BLOB_BASE = "https://github.com/opensiro/vsm-harness-index/blob/main"
ASSESSMENT_LINK_RE = re.compile(
    r"\[Assessment\]\("
    + re.escape(INDEX_BLOB_BASE)
    + r"/assessments/([A-Za-z0-9._-]+)\.md\)"
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
STATE_VECTOR_RE = re.compile(
    r"(?<![A-Za-z0-9])(?:A|C|P|—|\?)(?:\s+(?:A|C|P|—|\?)){5}(?![A-Za-z0-9])"
)
STATE_ASSIGNMENT_RE = re.compile(
    r"\bS(?:1|2|3\*?|4|5)\s*(?:=|:)\s*(?:A|C|P|—|\?)(?![A-Za-z0-9])"
)
RANK_VALUE_RE = re.compile(
    r"\b(?:autonomy\s+)?rank(?:ing)?\s*(?:#|=|:)?\s*\d+\b", re.IGNORECASE
)


def normalize_repository_url(url: str) -> str:
    normalized = url.strip().rstrip("/")
    if normalized.lower().endswith(".git"):
        normalized = normalized[:-4]
    return normalized.lower()


def parse_front_matter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return {}


def has_explicit_anchor(text: str, harness_id: str) -> bool:
    pattern = re.compile(
        r'<a\s+[^>]*id=["\']'
        + re.escape(harness_id)
        + r'["\'][^>]*>\s*</a>',
        re.IGNORECASE,
    )
    return bool(pattern.search(text))


def validate(readme_text: str, index_dir: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    entries = 0

    tldr_path = index_dir / "TLDR.md"
    rankings_path = index_dir / "RANKINGS.md"
    tldr_text = tldr_path.read_text(encoding="utf-8") if tldr_path.is_file() else ""
    rankings_text = (
        rankings_path.read_text(encoding="utf-8") if rankings_path.is_file() else ""
    )

    if not tldr_path.is_file():
        errors.append(f"canonical Index file missing: {tldr_path}")
    if not rankings_path.is_file():
        errors.append(f"canonical Index file missing: {rankings_path}")

    for line_number, line in enumerate(readme_text.splitlines(), start=1):
        assessment_match = ASSESSMENT_LINK_RE.search(line)
        if not assessment_match:
            continue

        entries += 1
        harness_id = assessment_match.group(1)
        prefix = f"README.md:{line_number} [{harness_id}]"

        assessment_path = index_dir / "assessments" / f"{harness_id}.md"
        if not assessment_path.is_file():
            errors.append(
                f"{prefix}: canonical assessment does not exist: assessments/{harness_id}.md"
            )
            continue

        front_matter = parse_front_matter(assessment_path.read_text(encoding="utf-8"))
        canonical_harness_id = front_matter.get("harness_id")
        canonical_repository = front_matter.get("repository")

        if canonical_harness_id != harness_id:
            errors.append(
                f"{prefix}: assessment harness_id is {canonical_harness_id!r}, "
                f"expected {harness_id!r}"
            )

        links = MARKDOWN_LINK_RE.findall(line)
        upstream_links = [
            (label, url) for label, url in links if not url.startswith(INDEX_BLOB_BASE)
        ]
        if not upstream_links:
            errors.append(f"{prefix}: missing upstream repository link")
        elif canonical_repository is None:
            errors.append(f"{prefix}: assessment front matter has no repository field")
        elif normalize_repository_url(upstream_links[0][1]) != normalize_repository_url(
            canonical_repository
        ):
            errors.append(
                f"{prefix}: upstream repository {upstream_links[0][1]!r} does not match "
                f"Index repository {canonical_repository!r}"
            )

        expected_tldr = f"{INDEX_BLOB_BASE}/TLDR.md#{harness_id}"
        expected_ranking = f"{INDEX_BLOB_BASE}/RANKINGS.md#{harness_id}"
        urls = [url for _, url in links]

        if expected_tldr not in urls:
            errors.append(f"{prefix}: missing canonical TL;DR link {expected_tldr}")
        if expected_ranking not in urls:
            errors.append(f"{prefix}: missing canonical Ranking link {expected_ranking}")

        if tldr_text and not has_explicit_anchor(tldr_text, harness_id):
            errors.append(f"{prefix}: TLDR.md has no explicit anchor #{harness_id}")
        if rankings_text and not has_explicit_anchor(rankings_text, harness_id):
            errors.append(f"{prefix}: RANKINGS.md has no explicit anchor #{harness_id}")

        if STATE_VECTOR_RE.search(line):
            errors.append(
                f"{prefix}: duplicates a canonical six-state VSM vector; "
                "link to the Index instead"
            )
        if STATE_ASSIGNMENT_RE.search(line):
            errors.append(
                f"{prefix}: duplicates a canonical per-system VSM state assignment; "
                "link to the Index instead"
            )
        if RANK_VALUE_RE.search(line):
            errors.append(
                f"{prefix}: duplicates a canonical numeric ranking; link to the Index instead"
            )

    if entries == 0:
        errors.append("README.md: no Index-backed curated harness entries found")

    return errors, entries


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--index-dir", type=Path, required=True)
    args = parser.parse_args()

    if not args.readme.is_file():
        print(f"ERROR: README not found: {args.readme}", file=sys.stderr)
        return 2
    if not args.index_dir.is_dir():
        print(f"ERROR: Index checkout not found: {args.index_dir}", file=sys.stderr)
        return 2

    errors, entries = validate(args.readme.read_text(encoding="utf-8"), args.index_dir)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {entries} curated harness entries against canonical Index checkout.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
