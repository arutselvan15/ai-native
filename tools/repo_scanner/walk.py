from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

from tools.repo_scanner.config import LINE_COUNT_EXTENSIONS, SKIP_DIR_NAMES


def iter_scannable_files(root: Path) -> Iterator[Path]:
    """Yield file paths relative to *root*, skipping denied directory names."""
    root = root.resolve()
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if _is_under_skipped_dir(path, root):
            continue
        if path.suffix.lower() not in LINE_COUNT_EXTENSIONS:
            continue
        yield path.relative_to(root)


def iter_python_files(root: Path) -> Iterator[Path]:
    root = root.resolve()
    for path in root.rglob("*.py"):
        if not path.is_file():
            continue
        if _is_under_skipped_dir(path, root):
            continue
        yield path.relative_to(root)


def _is_under_skipped_dir(path: Path, root: Path) -> bool:
    try:
        rel_parts = path.relative_to(root).parts
    except ValueError:
        return True
    return any(part in SKIP_DIR_NAMES for part in rel_parts)
