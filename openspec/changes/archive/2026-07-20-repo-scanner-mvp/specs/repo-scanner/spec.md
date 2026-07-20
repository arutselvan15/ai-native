## ADDED Requirements

### Requirement: CLI accepts a local directory path

The scanner SHALL accept exactly one optional positional argument: a path to a directory to scan. When omitted, the scanner SHALL use the current working directory. The scanner SHALL reject non-directory paths, missing paths, and paths outside the allowed scan root when a root constraint is applied.

#### Scenario: Default path is current directory

- **WHEN** the user runs the scanner with no path argument from a directory that exists
- **THEN** the scanner SHALL treat that directory as the scan root and exit with code 0 on success

#### Scenario: Invalid path fails clearly

- **WHEN** the user passes a path that does not exist or is not a directory
- **THEN** the scanner SHALL write a clear error message to stderr and exit with a non-zero code

### Requirement: Markdown report on stdout

On successful scan, the scanner SHALL write a human-readable Markdown report to stdout. The report SHALL include titled sections for summary, signals found, suggested next reads, and limitations.

#### Scenario: Successful scan produces Markdown

- **WHEN** the scan completes without fatal errors on a directory containing at least one scannable file
- **THEN** stdout SHALL contain Markdown headings and at least one bullet or table row describing findings

### Requirement: Large file signal

The scanner SHALL flag files whose line count exceeds a documented threshold as large-file signals. The report SHALL list each flagged file with its path relative to the scan root and line count.

#### Scenario: Large Python or Markdown file is flagged

- **WHEN** a `.py` or `.md` file under the scan root exceeds the configured line threshold
- **THEN** the report SHALL include that file under a large-file signal section

### Requirement: Python function complexity signal

For each `.py` file under the scan root (excluding common vendor/venv paths), the scanner SHALL parse the file with the Python AST module and flag functions whose cyclomatic complexity or line span exceeds documented thresholds. The report SHALL list file path, function name, and the metric that triggered the flag.

#### Scenario: Long function is flagged

- **WHEN** a Python function body span exceeds the configured line threshold
- **THEN** the report SHALL include that function in the complexity signal section

#### Scenario: Syntax error in Python file

- **WHEN** a `.py` file cannot be parsed
- **THEN** the scanner SHALL record a parse warning in the report and continue scanning other files without crashing

### Requirement: Workshop layout policy signal

The scanner SHALL detect paths matching `training/**/openspec/config.yaml` under the scan root and report each as a layout policy violation aligned with the repository’s single OpenSpec root convention.

#### Scenario: Nested OpenSpec config reported

- **WHEN** at least one file exists at `training/**/openspec/config.yaml` under the scan root
- **THEN** the report SHALL list each such path under a layout or policy signal section

#### Scenario: Clean layout produces explicit negative finding

- **WHEN** no nested OpenSpec config exists under `training/`
- **THEN** the report SHALL state that no nested OpenSpec configs were found under the checked pattern

### Requirement: Read-only behavior

The scanner MUST NOT create, modify, or delete files under the scan tree. It MAY read file contents and metadata only.

#### Scenario: Scan does not alter source tree

- **WHEN** the scanner runs successfully against a directory
- **THEN** the modification times and contents of source files in that directory SHALL be unchanged compared to before the run

### Requirement: Limitations and scope disclosure

The report SHALL include a limitations section that states which file types were considered, which directories were skipped (e.g. `.venv`, `.git`), and that findings are heuristic—not proof of defects.

#### Scenario: Limitations section present

- **WHEN** a scan completes successfully
- **THEN** the report SHALL include a limitations section mentioning skipped directories and heuristic confidence

### Requirement: Agent-ready context block

The report SHALL end with a short “suggested next reads” list of up to five relative file paths prioritized from the strongest signals, suitable for paste into an AI assistant session.

#### Scenario: Next reads capped and ordered

- **WHEN** multiple signals exist
- **THEN** the suggested next reads section SHALL contain at most five paths and SHALL reference paths that appeared in signal sections
