from __future__ import annotations

from pathlib import Path

from tools.repo_scanner.config import NESTED_OPENSPEC_GLOB
from tools.repo_scanner.models import LayoutFinding


def find_layout_violations(root: Path) -> list[LayoutFinding]:
    root = root.resolve()
    matches = sorted(root.glob(NESTED_OPENSPEC_GLOB))
    return [LayoutFinding(path=str(p.relative_to(root))) for p in matches if p.is_file()]
