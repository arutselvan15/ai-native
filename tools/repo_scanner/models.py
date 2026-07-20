from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class LargeFileFinding:
    path: str
    line_count: int


@dataclass
class ComplexityFinding:
    path: str
    function_name: str
    line_span: int
    complexity: int
    reason: str  # "long_function" | "high_complexity" | "both"


@dataclass
class LayoutFinding:
    path: str


@dataclass
class ScanResult:
    root: str
    large_files: list[LargeFileFinding] = field(default_factory=list)
    complexity: list[ComplexityFinding] = field(default_factory=list)
    layout_violations: list[LayoutFinding] = field(default_factory=list)
    parse_warnings: list[str] = field(default_factory=list)
    files_scanned_line_count: int = 0
    python_files_scanned: int = 0
    skipped_dir_names: tuple[str, ...] = ()
