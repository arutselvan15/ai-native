from __future__ import annotations

from pathlib import Path

from tools.repo_scanner.config import SKIP_DIR_NAMES
from tools.repo_scanner.models import ScanResult
from tools.repo_scanner.signals import large_files, layout_policy, python_complexity


def run_scan(root: Path) -> ScanResult:
    root = root.resolve()
    large, line_count_files = large_files.find_large_files(root)
    complexity, parse_warnings, py_count = python_complexity.find_complexity_issues(root)
    layout = layout_policy.find_layout_violations(root)
    return ScanResult(
        root=str(root),
        large_files=large,
        complexity=complexity,
        layout_violations=layout,
        parse_warnings=parse_warnings,
        files_scanned_line_count=line_count_files,
        python_files_scanned=py_count,
        skipped_dir_names=tuple(sorted(SKIP_DIR_NAMES)),
    )
