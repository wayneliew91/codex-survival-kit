#!/usr/bin/env python3
"""Validate Codex skill packages without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_AUX = {"README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"}
SENSITIVE_PATTERNS = [
    ("Windows user path", re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE)),
    ("OpenAI-style secret", re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{6,}")),
    ("GitHub token", re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{8,}")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]


def _read(path: Path) -> tuple[str | None, list[str]]:
    try:
        return path.read_text(encoding="utf-8"), []
    except (OSError, UnicodeError) as exc:
        return None, [f"{path}: cannot read UTF-8 text: {exc}"]


def _parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, [f"{path}: missing YAML frontmatter"]
    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        return {}, [f"{path}: unterminated YAML frontmatter"]

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}: invalid frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in fields:
            errors.append(f"{path}: duplicate frontmatter field {key!r}")
        fields[key] = value.strip('"\'')

    if set(fields) != {"name", "description"}:
        errors.append(f"{path}: frontmatter must contain exactly name and description")
    return fields, errors


def _check_links(markdown_path: Path, repo_root: Path) -> list[str]:
    text, errors = _read(markdown_path)
    if text is None:
        return errors
    for raw_target in LINK_RE.findall(text):
        target = raw_target.strip().split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:", "/")):
            continue
        resolved = (markdown_path.parent / target).resolve()
        try:
            resolved.relative_to(repo_root.resolve())
        except ValueError:
            errors.append(f"{markdown_path}: relative link escapes repository: {raw_target}")
            continue
        if not resolved.exists():
            errors.append(f"{markdown_path}: broken relative link: {raw_target}")
    return errors


def _check_sensitive_text(path: Path) -> list[str]:
    text, errors = _read(path)
    if text is None:
        return errors
    for label, pattern in SENSITIVE_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: sensitive pattern detected ({label})")
    return errors


def validate_skill_dir(skill_dir: Path, repo_root: Path) -> list[str]:
    skill_dir = Path(skill_dir)
    repo_root = Path(repo_root)
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    text, read_errors = _read(skill_md)
    errors.extend(read_errors)
    if text is None:
        return errors

    fields, fm_errors = _parse_frontmatter(text, skill_md)
    errors.extend(fm_errors)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if name and not NAME_RE.fullmatch(name):
        errors.append(f"{skill_md}: name must use lowercase letters, numbers, and hyphens")
    if name and skill_dir.name != name:
        errors.append(f"{skill_md}: folder name {skill_dir.name!r} must match frontmatter name {name!r}")
    if description and not description.startswith("Use when"):
        errors.append(f"{skill_md}: description must start with 'Use when'")
    if not description:
        errors.append(f"{skill_md}: description must not be empty")

    if not (skill_dir / "agents" / "openai.yaml").is_file():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")

    for forbidden in FORBIDDEN_AUX:
        if (skill_dir / forbidden).exists():
            errors.append(f"{skill_dir / forbidden}: forbidden auxiliary file inside skill package")

    for path in skill_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() in {".md", ".yaml", ".yml", ".txt", ".json", ".py", ".sh"}:
            errors.extend(_check_sensitive_text(path))
        if path.suffix.lower() == ".md":
            errors.extend(_check_links(path, repo_root))

    return errors


def validate_repo(repo_root: Path) -> list[str]:
    repo_root = Path(repo_root).resolve()
    skills_root = repo_root / "skills"
    if not skills_root.is_dir():
        return [f"{skills_root}: missing skills directory"]

    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not skill_dirs:
        return [f"{skills_root}: no skill directories found"]

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill_dir(skill_dir, repo_root))
    return errors


def main(argv: list[str]) -> int:
    repo_root = Path(argv[1] if len(argv) > 1 else ".")
    errors = validate_repo(repo_root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed: {len(errors)} error(s).")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
