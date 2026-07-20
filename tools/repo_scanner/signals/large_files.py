from __future__ import annotations

from pathlib import Path

from tools.repo_scanner.config import LARGE_FILE_LINE_THRESHOLD
from tools.repo_scanner.models import LargeFileFinding
from tools.repo_scanner.walk import iter_scannable_files


def find_large_files(root: Path) -> tuple[list[LargeFileFinding], int]:
    findings: list[LargeFileFinding] = []
    count = 0
    for rel in iter_scannable_files(root):
        count += 1
        full = root / rel
        try:
            text = full.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
        if lines > LARGE_FILE_LINE_THRESHOLD:
            findings.append(LargeFileFinding(path=str(rel), line_count=lines))
    findings.sort(key=lambda f: (-f.line_count, f.path))
    return findings, count
