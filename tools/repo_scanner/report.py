from __future__ import annotations

from tools.repo_scanner.config import (
    COMPLEXITY_THRESHOLD,
    LARGE_FILE_LINE_THRESHOLD,
    LONG_FUNCTION_LINE_THRESHOLD,
    LINE_COUNT_EXTENSIONS,
)
from tools.repo_scanner.models import ScanResult


def render_report(result: ScanResult) -> str:
    lines: list[str] = [
        "# Repo scan report",
        "",
        "## Summary",
        "",
        f"- Scan root: `{result.root}`",
        f"- Files checked for size ({', '.join(sorted(LINE_COUNT_EXTENSIONS))}): {result.files_scanned_line_count}",
        f"- Python files analyzed (AST): {result.python_files_scanned}",
        f"- Large-file signals: {len(result.large_files)}",
        f"- Complexity signals: {len(result.complexity)}",
        f"- Layout policy matches: {len(result.layout_violations)}",
        "",
        "## Signals",
        "",
        "### Large files",
        "",
    ]
    if result.large_files:
        lines.append(f"Threshold: more than {LARGE_FILE_LINE_THRESHOLD} lines.")
        lines.append("")
        for item in result.large_files:
            lines.append(f"- `{item.path}` — {item.line_count} lines")
    else:
        lines.append("_No large files found._")
    lines.extend(["", "### Python complexity", ""])
    if result.complexity:
        lines.append(
            f"Thresholds: function span > {LONG_FUNCTION_LINE_THRESHOLD} lines "
            f"and/or cyclomatic complexity > {COMPLEXITY_THRESHOLD} (heuristic)."
        )
        lines.append("")
        for item in result.complexity:
            lines.append(
                f"- `{item.path}` `{item.function_name}` — "
                f"span {item.line_span} lines, complexity {item.complexity} ({item.reason})"
            )
    else:
        lines.append("_No complexity signals found._")
    if result.parse_warnings:
        lines.extend(["", "#### Parse warnings", ""])
        for warn in result.parse_warnings:
            lines.append(f"- {warn}")
    lines.extend(["", "### Workshop layout (nested OpenSpec)", ""])
    if result.layout_violations:
        lines.append("Paths matching `training/**/openspec/config.yaml`:")
        lines.append("")
        for item in result.layout_violations:
            lines.append(f"- `{item.path}`")
    else:
        lines.append("_No nested OpenSpec configs found under `training/`._")
    lines.extend(["", "## Suggested next reads", ""])
    for path in _suggested_reads(result):
        lines.append(f"- `{path}`")
    if not _suggested_reads(result):
        lines.append("_No prioritized paths (no signals)._")
    lines.extend(["", "## Limitations", ""])
    skipped = ", ".join(f"`{name}`" for name in result.skipped_dir_names)
    lines.append(
        f"- Skipped directory names during walk: {skipped}."
    )
    lines.append(
        f"- Size scan includes {', '.join(sorted(LINE_COUNT_EXTENSIONS))} only; "
        "complexity uses a simple AST heuristic, not a full linter."
    )
    lines.append(
        "- Findings indicate review candidates, not confirmed defects. "
        "Verify manually before changing code."
    )
    lines.append("")
    return "\n".join(lines)


def _suggested_reads(result: ScanResult) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []

    def add(path: str) -> None:
        if path not in seen:
            seen.add(path)
            ordered.append(path)

    for item in result.layout_violations:
        add(item.path)
    for item in result.complexity:
        add(item.path)
    for item in result.large_files:
        add(item.path)
    return ordered[:5]
