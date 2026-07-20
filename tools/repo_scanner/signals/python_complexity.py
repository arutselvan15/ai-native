from __future__ import annotations

import ast
from pathlib import Path

from tools.repo_scanner.config import COMPLEXITY_THRESHOLD, LONG_FUNCTION_LINE_THRESHOLD
from tools.repo_scanner.models import ComplexityFinding
from tools.repo_scanner.walk import iter_python_files


def find_complexity_issues(root: Path) -> tuple[list[ComplexityFinding], list[str], int]:
    findings: list[ComplexityFinding] = []
    warnings: list[str] = []
    count = 0
    for rel in iter_python_files(root):
        count += 1
        full = root / rel
        try:
            source = full.read_text(encoding="utf-8", errors="replace")
            tree = ast.parse(source, filename=str(rel))
        except SyntaxError as exc:
            warnings.append(f"Parse error in {rel}: {exc.msg}")
            continue
        except OSError as exc:
            warnings.append(f"Could not read {rel}: {exc}")
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                finding = _analyze_function(node)
                if finding is None:
                    continue
                findings.append(
                    ComplexityFinding(
                        path=str(rel),
                        function_name=node.name,
                        line_span=finding[0],
                        complexity=finding[1],
                        reason=finding[2],
                    )
                )
    findings.sort(key=lambda f: (-f.complexity, -f.line_span, f.path))
    return findings, warnings, count


def _analyze_function(node: ast.FunctionDef | ast.AsyncFunctionDef) -> tuple[int, int, str] | None:
    line_span = _function_line_span(node)
    complexity = _cyclomatic_complexity(node)
    long_fn = line_span > LONG_FUNCTION_LINE_THRESHOLD
    complex_fn = complexity > COMPLEXITY_THRESHOLD
    if not long_fn and not complex_fn:
        return None
    if long_fn and complex_fn:
        reason = "both"
    elif long_fn:
        reason = "long_function"
    else:
        reason = "high_complexity"
    return line_span, complexity, reason


def _function_line_span(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    end_lineno = getattr(node, "end_lineno", None)
    if end_lineno is not None:
        return max(end_lineno - node.lineno + 1, 1)
    if not node.body:
        return 0
    end = node.lineno
    for child in ast.walk(node):
        lineno = getattr(child, "lineno", None)
        end_lineno = getattr(child, "end_lineno", None)
        if end_lineno is not None:
            end = max(end, end_lineno)
        elif lineno is not None:
            end = max(end, lineno)
    return max(end - node.lineno + 1, 1)


def _cyclomatic_complexity(node: ast.AST) -> int:
    score = 1
    for child in ast.walk(node):
        if isinstance(child, (ast.If, ast.For, ast.AsyncFor, ast.While, ast.IfExp)):
            score += 1
        elif isinstance(child, ast.ExceptHandler):
            score += 1
        elif isinstance(child, ast.With):
            score += 1
        elif isinstance(child, ast.BoolOp):
            score += max(len(child.values) - 1, 0)
        elif isinstance(child, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            score += 1
    return score
