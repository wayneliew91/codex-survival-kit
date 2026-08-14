#!/usr/bin/env python3
"""Synchronize canonical standalone skills into the Codex plugin package."""

from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
TARGET = ROOT / "plugins" / "codex-survival-kit" / "skills"


def file_map(root: Path) -> dict[Path, Path]:
    if not root.exists():
        return {}
    return {p.relative_to(root): p for p in root.rglob("*") if p.is_file()}


def differences() -> list[str]:
    source = file_map(SOURCE)
    target = file_map(TARGET)
    problems: list[str] = []

    for rel in sorted(source.keys() - target.keys()):
        problems.append(f"missing from plugin mirror: {rel.as_posix()}")
    for rel in sorted(target.keys() - source.keys()):
        problems.append(f"extra in plugin mirror: {rel.as_posix()}")
    for rel in sorted(source.keys() & target.keys()):
        if not filecmp.cmp(source[rel], target[rel], shallow=False):
            problems.append(f"content differs: {rel.as_posix()}")
    return problems


def sync() -> None:
    if TARGET.exists():
        shutil.rmtree(TARGET)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SOURCE, TARGET)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the plugin mirror differs")
    args = parser.parse_args()

    if args.check:
        problems = differences()
        if problems:
            for problem in problems:
                print(f"ERROR: {problem}")
            print(f"Plugin mirror check failed: {len(problems)} difference(s).")
            return 1
        print("Plugin mirror is synchronized.")
        return 0

    sync()
    print(f"Synchronized {SOURCE} -> {TARGET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
