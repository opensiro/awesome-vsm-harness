#!/usr/bin/env python3
"""Render repository-owned public curation metrics for Awesome VSM Harness."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from validate_index_consistency import ASSESSMENT_LINK_RE


def parse_curated_ids(text: str) -> list[str]:
    identities = ASSESSMENT_LINK_RE.findall(text)
    unique = list(dict.fromkeys(identities))
    if len(identities) != len(unique):
        raise ValueError("duplicate canonical Index assessment link in curated README")
    return unique


def compute_core_metrics(repo: Path) -> dict[str, object]:
    identities = parse_curated_ids((repo / "README.md").read_text(encoding="utf-8"))
    return {
        "curated_representative_entries": len(identities),
        "curated_entry_ids": identities,
    }


def render(repo: Path) -> str:
    return json.dumps(
        {"schema_version": 1, **compute_core_metrics(repo)},
        indent=2,
        ensure_ascii=False,
    ) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--source-root", type=Path)
    parser.add_argument("--stdout-core-json", action="store_true")
    args = parser.parse_args()

    repo = (args.source_root or Path(__file__).resolve().parents[1]).resolve()
    if args.stdout_core_json:
        print(json.dumps(compute_core_metrics(repo), sort_keys=True))
        return 0

    output = repo / "data" / "metrics.json"
    rendered = render(repo)
    if args.check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != rendered:
            raise SystemExit(
                "stale generated metric file: data/metrics.json; "
                "run python scripts/render_metrics.py"
            )
        print("Awesome metrics are current")
        return 0

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
