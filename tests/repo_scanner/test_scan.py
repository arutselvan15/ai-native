from __future__ import annotations

import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

from tools.repo_scanner.cli import main
from tools.repo_scanner.report import render_report
from tools.repo_scanner.scan import run_scan

REPO_ROOT = Path(__file__).resolve().parents[2]


class RepoScannerTests(unittest.TestCase):
    def test_invalid_path_exits_nonzero(self) -> None:
        err = io.StringIO()
        with redirect_stderr(err):
            code = main(["/nonexistent/path/for/repo-scanner"])
        self.assertEqual(code, 2)
        self.assertIn("does not exist", err.getvalue())

    def test_valid_scan_markdown_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "hello.md").write_text("# hi\n", encoding="utf-8")
            (root / "training" / "lab" / "openspec").mkdir(parents=True)
            (root / "training" / "lab" / "openspec" / "config.yaml").write_text(
                "schema: x\n", encoding="utf-8"
            )
            big = "\n".join(f"line {i}" for i in range(301))
            (root / "big.md").write_text(big, encoding="utf-8")
            py = root / "long_fn.py"
            py.write_text(
                "def long_one():\n" + "".join(f"    x = {i}\n" for i in range(70)),
                encoding="utf-8",
            )
            result = run_scan(root)
            report = render_report(result)
            self.assertIn("# Repo scan report", report)
            self.assertIn("## Summary", report)
            self.assertIn("## Signals", report)
            self.assertIn("## Suggested next reads", report)
            self.assertIn("## Limitations", report)
            self.assertIn("training/lab/openspec/config.yaml", report)
            self.assertIn("big.md", report)
            self.assertIn("long_one", report)

    def test_cli_success_stdout(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            Path(tmp, "a.md").write_text("ok\n", encoding="utf-8")
            out = io.StringIO()
            with redirect_stdout(out):
                code = main([tmp])
            self.assertEqual(code, 0)
            self.assertIn("Repo scan report", out.getvalue())

    def test_scan_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "sample.py"
            target.write_text("x = 1\n", encoding="utf-8")
            before = target.read_text(encoding="utf-8")
            mtime_before = os.path.getmtime(target)
            run_scan(Path(tmp))
            self.assertEqual(target.read_text(encoding="utf-8"), before)
            self.assertEqual(os.path.getmtime(target), mtime_before)

    def test_clean_layout_negative_finding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report = render_report(run_scan(Path(tmp)))
            self.assertIn("No nested OpenSpec configs found", report)


class RepoScannerSmoke(unittest.TestCase):
    def test_smoke_ai_native_root(self) -> None:
        """Manual smoke against workshop repo (nested OpenSpec may or may not exist)."""
        result = run_scan(REPO_ROOT)
        report = render_report(result)
        self.assertIn("## Limitations", report)
        self.assertGreater(result.files_scanned_line_count, 0)


if __name__ == "__main__":
    unittest.main()
