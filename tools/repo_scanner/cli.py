from __future__ import annotations

import argparse
import sys
from pathlib import Path

from tools.repo_scanner.report import render_report
from tools.repo_scanner.scan import run_scan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scan a local repository for legibility and layout signals (read-only)."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Directory to scan (default: current working directory)",
    )
    return parser


def resolve_scan_root(path_str: str) -> Path:
    path = Path(path_str).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")
    if not path.is_dir():
        raise NotADirectoryError(f"Not a directory: {path}")
    return path.resolve()


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        root = resolve_scan_root(args.path)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    result = run_scan(root)
    print(render_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
