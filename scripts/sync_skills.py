#!/usr/bin/env python3
"""Copy selected canonical skills into another repository."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
MANIFEST_PATH = ROOT / "skills-manifest.json"


def available_skills() -> set[str]:
    """Return active skill names from the catalog manifest."""
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    return {
        str(entry["name"])
        for entry in manifest.get("skills", [])
        if entry.get("status") == "active"
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy selected skills to <target>/.agents/skills."
    )
    parser.add_argument("target", type=Path, help="Target repository directory")
    parser.add_argument("skills", nargs="+", help="Skill names to copy")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing target skill directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files",
    )
    return parser.parse_args()


def copy_skill(source: Path, destination: Path, *, force: bool, dry_run: bool) -> None:
    """Copy one skill directory with explicit overwrite behavior."""
    if destination.exists() and not force:
        raise FileExistsError(
            f"{destination} already exists; use --force to replace it"
        )
    if dry_run:
        print(f"DRY-RUN copy {source} -> {destination}")
        return
    if destination.exists():
        shutil.rmtree(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print(f"Copied {source.name} -> {destination}")


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    if not target.is_dir():
        print(f"ERROR: target directory does not exist: {target}", file=sys.stderr)
        return 2

    known = available_skills()
    requested = list(dict.fromkeys(args.skills))
    unknown = sorted(set(requested) - known)
    if unknown:
        print(
            f"ERROR: unknown skills {unknown}; available={sorted(known)}",
            file=sys.stderr,
        )
        return 2

    destination_root = target / ".agents" / "skills"
    try:
        for name in requested:
            source = SKILLS_ROOT / name
            if not (source / "SKILL.md").is_file():
                raise FileNotFoundError(f"canonical skill is incomplete: {source}")
            copy_skill(
                source,
                destination_root / name,
                force=args.force,
                dry_run=args.dry_run,
            )
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Synchronized {len(requested)} skill(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
