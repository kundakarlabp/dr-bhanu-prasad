#!/usr/bin/env python3
"""Validate the personal Agent Skills catalog using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
MANIFEST_PATH = ROOT / "skills-manifest.json"

REQUIRED_FRONTMATTER = {"name", "description"}
REQUIRED_SECTION_GROUPS = {
    "purpose": {"purpose"},
    "workflow": {"workflow"},
    "validation": {
        "validation",
        "validate",
        "quality checks",
        "safety checks",
        "consistency audit",
        "validation evidence",
    },
    "failure": {"failure and uncertainty handling", "failure handling"},
}
SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)\b(?:api[_-]?key|access[_-]?token|secret[_-]?key)\s*=\s*['\"][^'\"]+['\"]"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Parse the simple YAML subset used by SKILL.md files."""
    if not text.startswith("---\n"):
        raise ValueError("missing opening YAML frontmatter delimiter")
    try:
        raw, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("missing closing YAML frontmatter delimiter") from exc

    metadata: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, body


def headings(body: str) -> set[str]:
    """Return normalized second-level Markdown headings."""
    found: set[str] = set()
    for line in body.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            found.add(match.group(1).strip().lower())
    return found


def validate_skill(skill_dir: Path) -> list[str]:
    """Validate one skill directory and return human-readable errors."""
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir.relative_to(ROOT)}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    try:
        metadata, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{skill_file.relative_to(ROOT)}: {exc}"]

    missing_metadata = sorted(REQUIRED_FRONTMATTER - metadata.keys())
    if missing_metadata:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: missing frontmatter keys {missing_metadata}"
        )

    declared_name = metadata.get("name", "")
    if declared_name != skill_dir.name:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: name {declared_name!r} does not match directory {skill_dir.name!r}"
        )
    if len(metadata.get("description", "")) < 40:
        errors.append(
            f"{skill_file.relative_to(ROOT)}: description is too short for reliable activation"
        )

    body_headings = headings(body)
    for label, accepted in REQUIRED_SECTION_GROUPS.items():
        if not body_headings.intersection(accepted):
            errors.append(
                f"{skill_file.relative_to(ROOT)}: missing {label} section; accepted headings={sorted(accepted)}"
            )

    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            errors.append(
                f"{skill_file.relative_to(ROOT)}: possible credential or private key detected"
            )
            break

    if not text.endswith("\n"):
        errors.append(f"{skill_file.relative_to(ROOT)}: file must end with newline")
    return errors


def validate_manifest(skill_names: set[str]) -> list[str]:
    """Validate manifest structure and agreement with skill directories."""
    errors: list[str] = []
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"skills-manifest.json: {exc}"]

    entries = manifest.get("skills")
    if not isinstance(entries, list):
        return ["skills-manifest.json: 'skills' must be a list"]

    manifest_names: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"skills-manifest.json: entry {index} must be an object")
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"skills-manifest.json: entry {index} has invalid name")
            continue
        manifest_names.append(name)

    if len(manifest_names) != len(set(manifest_names)):
        errors.append("skills-manifest.json: duplicate skill names")

    manifest_set = set(manifest_names)
    if manifest_set != skill_names:
        errors.append(
            "skills-manifest.json: catalog mismatch "
            f"missing={sorted(skill_names - manifest_set)} extra={sorted(manifest_set - skill_names)}"
        )
    return errors


def main() -> int:
    """Run all validations and return a process exit code."""
    if not SKILLS_ROOT.is_dir():
        print(f"ERROR: missing skills root: {SKILLS_ROOT.relative_to(ROOT)}")
        return 1

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))
    errors.extend(validate_manifest({path.name for path in skill_dirs}))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
