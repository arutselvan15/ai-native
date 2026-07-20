from __future__ import annotations

SKIP_DIR_NAMES: frozenset[str] = frozenset(
    {
        ".git",
        ".venv",
        "venv",
        "__pycache__",
        "node_modules",
        ".cursor",
    }
)

LARGE_FILE_LINE_THRESHOLD = 300
LONG_FUNCTION_LINE_THRESHOLD = 60
COMPLEXITY_THRESHOLD = 10

LINE_COUNT_EXTENSIONS: frozenset[str] = frozenset({".py", ".md"})
PYTHON_EXTENSION = ".py"

NESTED_OPENSPEC_GLOB = "training/**/openspec/config.yaml"
