#!/usr/bin/env python3
"""Validate the reusable proposal ledger and its candidate projections."""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable, Iterator, Sequence
from urllib.parse import unquote


TEMPLATE_PATH = Path("Methods/Proposal requirements ledger.md")
CANDIDATE_LEDGER_PATTERN = "Candidates/**/Research/Proposal requirements ledger.md"

FIELD_ID_PATTERN = re.compile(r"^[SCE]-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
DATE_PATTERN = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
EMAIL_PATTERN = re.compile(
    r"(?<![\w.+-]) [\w.+-]+ @ [A-Za-z0-9.-]+ \. [A-Za-z]{2,} (?![\w.-])",
    re.VERBOSE,
)
URI_SCHEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
HEADING_PATTERN = re.compile(
    r"^ [ ]{0,3} [#]{1,6} \s+ (?P<text> .*? ) (?: \s+ [#]+ )? \s*$",
    re.VERBOSE,
)
HTML_TAG_PATTERN = re.compile(r"< [^>]+ >", re.VERBOSE)
HEADING_PUNCTUATION_PATTERN = re.compile(r"[^\w\s-]")
TABLE_SEPARATOR_CELL_PATTERN = re.compile(r":?-{3,}:?")
MARKDOWN_LINK_PATTERN = re.compile(
    r"""\]\(
        (?:
            < (?P<angled> [^>\n]+ ) >
            |
            (?P<plain> [^)\s]+ )
        )
        (?:
            \s+
            (?:
                " [^"]* "
                |
                ' [^']* '
                |
                \( [^)]* \)
            )
        )?
    \)""",
    re.VERBOSE,
)

ALLOWED_STATES = {
    "`unknown`",
    "`provisional`",
    "`supported`",
    "`not applicable`",
    "`blocked`",
    "`submission-ready`",
}

LEDGER_CONTROL_FIELDS = {
    "Candidate or repertoire",
    "Scope",
    "Candidate phase",
    "Routes under evaluation",
    "Evidence cut-off",
    "Stable Unicode version checked",
    "Emoji version checked, if applicable",
    "Official-guidance check",
    "Ledger revision",
    "Principal unresolved decision",
}

READINESS_ROUTES = ("Character proposal", "Emoji proposal")


@dataclass(frozen=True)
class TableRow:
    line_number: int
    cells: tuple[str, ...]

    @property
    def field_id(self) -> str | None:
        if self.cells and FIELD_ID_PATTERN.fullmatch(self.cells[0]):
            return self.cells[0]
        return None


@dataclass(frozen=True)
class FieldRowSchema:
    current_value: int
    state: int
    refresh: int
    support: int | None = None


FIELD_ROW_SCHEMAS = {
    # Full ledger row: ID, requirement, value, state, support, rights, refresh.
    7: FieldRowSchema(current_value=2, state=3, refresh=6, support=4),
    # N4502-F mapping: ID, form item, answer/reference, state, refresh.
    5: FieldRowSchema(current_value=2, state=3, refresh=4),
}


@dataclass(frozen=True)
class MarkdownDocument:
    path: Path
    lines: tuple[str, ...]
    frontmatter: dict[str, str]
    tables: tuple[tuple[TableRow, ...], ...]

    @classmethod
    def read(cls, path: Path) -> MarkdownDocument:
        text = path.read_text(encoding="utf-8")
        lines = tuple(text.splitlines())
        return cls(
            path=path,
            lines=lines,
            frontmatter=parse_frontmatter(lines),
            tables=tuple(parse_tables(lines)),
        )

    @property
    def field_rows(self) -> tuple[TableRow, ...]:
        return tuple(
            row
            for row in self.id_rows
            if row.field_id is not None
        )

    @property
    def id_rows(self) -> tuple[TableRow, ...]:
        return tuple(
            row
            for table in self.tables
            if table and table[0].cells and table[0].cells[0] == "ID"
            for row in table[1:]
            if not is_separator_row(row)
        )


class ValidationReport:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def display_path(self, path: Path) -> str:
        try:
            return str(path.relative_to(self.repo_root))
        except ValueError:
            return str(path)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warning(self, message: str) -> None:
        self.warnings.append(message)

    def emit(self) -> None:
        for message in self.errors:
            print(f"ERROR: {message}", file=sys.stderr)
        for message in self.warnings:
            print(f"WARNING: {message}", file=sys.stderr)


def parse_frontmatter(lines: Sequence[str]) -> dict[str, str]:
    if not lines or lines[0] != "---":
        return {}

    values: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            break
        if line.startswith((" ", "\t", "-")) or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip()
    return values


def split_table_row(line: str) -> tuple[str, ...]:
    """Split a table row without breaking escaped or code-span pipes."""

    content = line.strip()
    if not content.startswith("|"):
        return ()

    content = content[1:]
    if content.endswith("|"):
        content = content[:-1]

    cells: list[str] = []
    current: list[str] = []
    code_delimiter = 0
    index = 0

    while index < len(content):
        character = content[index]

        if character == "\\" and index + 1 < len(content):
            current.extend((character, content[index + 1]))
            index += 2
            continue

        if character == "`":
            run_end = index
            while run_end < len(content) and content[run_end] == "`":
                run_end += 1
            run_length = run_end - index
            if code_delimiter == 0:
                code_delimiter = run_length
            elif code_delimiter == run_length:
                code_delimiter = 0
            current.append(content[index:run_end])
            index = run_end
            continue

        if character == "|" and code_delimiter == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(character)
        index += 1

    cells.append("".join(current).strip())
    return tuple(cells)


def is_separator_row(row: TableRow) -> bool:
    return bool(row.cells) and all(
        TABLE_SEPARATOR_CELL_PATTERN.fullmatch(cell) for cell in row.cells
    )


def parse_tables(lines: Sequence[str]) -> Iterator[tuple[TableRow, ...]]:
    current: list[TableRow] = []

    for line_number, line in enumerate(lines, start=1):
        if line.lstrip().startswith("|"):
            current.append(TableRow(line_number, split_table_row(line)))
            continue
        if current:
            yield tuple(current)
            current = []

    if current:
        yield tuple(current)


def parse_date(
    value: str,
    *,
    path: Path,
    key: str,
    report: ValidationReport,
) -> date | None:
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        report.error(
            f"{report.display_path(path)}: frontmatter {key} must be a valid "
            f"YYYY-MM-DD calendar date, found {value!r}"
        )
        return None

    if parsed.isoformat() != value:
        report.error(
            f"{report.display_path(path)}: frontmatter {key} must use YYYY-MM-DD, "
            f"found {value!r}"
        )
        return None
    return parsed


def optional_date(value: str | None) -> date | None:
    if value is None:
        return None
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        return None
    return parsed if parsed.isoformat() == value else None


def require_frontmatter(
    document: MarkdownDocument,
    keys: Iterable[str],
    date_keys: Iterable[str],
    report: ValidationReport,
) -> dict[str, date]:
    parsed_dates: dict[str, date] = {}
    date_key_set = set(date_keys)
    display_path = report.display_path(document.path)

    for key in keys:
        value = document.frontmatter.get(key)
        if not value:
            report.error(f"{display_path}: missing frontmatter {key}")
            continue
        if key in date_key_set:
            parsed = parse_date(
                value,
                path=document.path,
                key=key,
                report=report,
            )
            if parsed is not None:
                parsed_dates[key] = parsed

    return parsed_dates


def validate_table_shapes(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)

    for table in document.tables:
        expected_columns = len(table[0].cells)
        for row in table[1:]:
            if len(row.cells) != expected_columns:
                report.error(
                    f"{display_path}:{row.line_number}: table row has "
                    f"{len(row.cells)} columns; expected {expected_columns}"
                )


def local_links(lines: Sequence[str]) -> Iterator[tuple[int, str]]:
    for line_number, line in enumerate(lines, start=1):
        for match in MARKDOWN_LINK_PATTERN.finditer(line):
            yield line_number, match.group("angled") or match.group("plain")


def heading_anchors(lines: Sequence[str]) -> set[str]:
    anchors: set[str] = set()
    counts: Counter[str] = Counter()

    for line in lines:
        match = HEADING_PATTERN.fullmatch(line)
        if match is None:
            continue
        text = HTML_TAG_PATTERN.sub("", match.group("text")).lower()
        base = HEADING_PUNCTUATION_PATTERN.sub("", text)
        base = re.sub(r"\s", "-", base)
        duplicate_number = counts[base]
        anchor = base if duplicate_number == 0 else f"{base}-{duplicate_number}"
        anchors.add(anchor)
        counts[base] += 1

    return anchors


def validate_local_links(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)

    anchors_by_path: dict[Path, set[str]] = {}

    for line_number, target in sorted(set(local_links(document.lines))):
        if not target or target.startswith("//") or URI_SCHEME_PATTERN.match(target):
            continue

        path_target, fragment_marker, fragment = target.partition("#")
        path_text = unquote(path_target.split("?", 1)[0])
        linked_path = document.path if not path_text else Path(path_text)
        if path_text and not linked_path.is_absolute():
            linked_path = (document.path.parent / linked_path).resolve()
        if not linked_path.exists():
            report.error(
                f"{display_path}:{line_number}: broken local link to {target}"
            )
            continue

        if (
            fragment_marker
            and fragment
            and not fragment.startswith("^")
            and linked_path.suffix.lower() == ".md"
        ):
            decoded_fragment = unquote(fragment)
            anchors = anchors_by_path.get(linked_path)
            if anchors is None:
                linked_lines = tuple(
                    linked_path.read_text(encoding="utf-8").splitlines()
                )
                anchors = heading_anchors(linked_lines)
                anchors_by_path[linked_path] = anchors
            if decoded_fragment not in anchors:
                report.error(
                    f"{display_path}:{line_number}: broken heading fragment "
                    f"in local link to {target}"
                )


def validate_field_ids(
    document: MarkdownDocument,
    *,
    expected_ids: set[str] | None,
    report: ValidationReport,
) -> set[str]:
    display_path = report.display_path(document.path)

    for row in document.id_rows:
        if row.field_id is None:
            malformed_id = row.cells[0] if row.cells else ""
            report.error(
                f"{display_path}:{row.line_number}: malformed field ID "
                f"{malformed_id!r}"
            )

    ids = [row.field_id for row in document.field_rows]
    concrete_ids = [field_id for field_id in ids if field_id is not None]
    counts = Counter(concrete_ids)

    for field_id in sorted(field_id for field_id, count in counts.items() if count > 1):
        report.error(f"{display_path}: duplicate field ID {field_id}")

    found_ids = set(concrete_ids)
    if expected_ids is not None:
        for field_id in sorted(expected_ids - found_ids):
            report.error(f"{display_path}: missing template field ID {field_id}")
        for field_id in sorted(found_ids - expected_ids):
            report.error(f"{display_path}: unexpected field ID {field_id}")

    return found_ids


def validate_candidate_fields(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)

    for row in document.field_rows:
        field_id = row.field_id
        schema = FIELD_ROW_SCHEMAS.get(len(row.cells))
        if schema is None:
            permitted_counts = ", ".join(str(count) for count in FIELD_ROW_SCHEMAS)
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has "
                f"{len(row.cells)} columns; expected {permitted_counts}"
            )
            continue

        current_value = row.cells[schema.current_value]
        state = row.cells[schema.state]
        refresh = row.cells[schema.refresh]

        if not current_value:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has an "
                "unexplained blank current value"
            )
        if state not in ALLOWED_STATES:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has invalid "
                f"state {state!r}"
            )
        if not refresh:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has a blank "
                "refresh condition"
            )
        if schema.support is not None and not row.cells[schema.support]:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has a blank "
                "support and destination"
            )


def validate_template_fields(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)

    for row in document.field_rows:
        field_id = row.field_id
        schema = FIELD_ROW_SCHEMAS.get(len(row.cells))
        if schema is None:
            permitted_counts = ", ".join(str(count) for count in FIELD_ROW_SCHEMAS)
            report.error(
                f"{display_path}:{row.line_number}: {field_id} has "
                f"{len(row.cells)} columns; expected {permitted_counts}"
            )
            continue

        if row.cells[schema.current_value]:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} template "
                "current value must be blank"
            )
        if row.cells[schema.state] != "`unknown`":
            report.error(
                f"{display_path}:{row.line_number}: {field_id} template state "
                "must be `unknown`"
            )
        if not row.cells[schema.refresh]:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} template has "
                "a blank refresh condition"
            )
        if schema.support is not None and not row.cells[schema.support]:
            report.error(
                f"{display_path}:{row.line_number}: {field_id} template has "
                "a blank support and destination"
            )


def latest_candidate_evidence(
    ledger: MarkdownDocument,
) -> tuple[date, Path] | None:
    research_directory = ledger.path.parent
    overview = research_directory.parent / "Overview.md"
    note_paths = [
        path
        for path in research_directory.rglob("*.md")
        if path != ledger.path
    ]
    if overview.is_file():
        note_paths.append(overview)

    evidence: list[tuple[date, Path]] = []

    for path in note_paths:
        frontmatter = parse_frontmatter(
            tuple(path.read_text(encoding="utf-8").splitlines())
        )
        evidence_date = optional_date(frontmatter.get("evidence_cutoff"))
        if evidence_date is not None:
            evidence.append((evidence_date, path))

    return max(evidence, default=None, key=lambda item: item[0])


def validate_candidate_freshness(
    ledger: MarkdownDocument,
    ledger_dates: dict[str, date],
    template_guidance_cutoff: date | None,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(ledger.path)
    ledger_guidance = ledger_dates.get("official_guidance_cutoff")

    if (
        template_guidance_cutoff is not None
        and ledger_guidance is not None
        and ledger_guidance < template_guidance_cutoff
    ):
        report.warning(
            f"{display_path}: official-guidance cut-off "
            f"{ledger_guidance.isoformat()} predates template cut-off "
            f"{template_guidance_cutoff.isoformat()}"
        )

    latest_evidence = latest_candidate_evidence(ledger)
    ledger_evidence = ledger_dates.get("evidence_cutoff")

    if (
        latest_evidence is not None
        and ledger_evidence is not None
        and latest_evidence[0] > ledger_evidence
    ):
        report.warning(
            f"{display_path}: {report.display_path(latest_evidence[1])} has "
            f"evidence cut-off {latest_evidence[0].isoformat()}, after the "
            f"ledger cut-off {ledger_evidence.isoformat()}"
        )


def validate_ledger_control(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)
    control_tables = [
        table
        for table in document.tables
        if table
        and table[0].cells == ("Field", "Value")
    ]
    if len(control_tables) != 1:
        report.error(
            f"{display_path}: expected one Ledger control table, found "
            f"{len(control_tables)}"
        )
        return

    rows = [
        row for row in control_tables[0][1:] if not is_separator_row(row)
    ]
    counts = Counter(row.cells[0] for row in rows if row.cells)
    for field in sorted(
        field for field, count in counts.items() if count > 1
    ):
        report.error(f"{display_path}: duplicate Ledger control field {field}")

    values = {
        row.cells[0]: row.cells[1]
        for row in rows
        if len(row.cells) == 2
    }
    for field in sorted(LEDGER_CONTROL_FIELDS):
        if field not in values:
            report.error(f"{display_path}: missing Ledger control field {field}")
        elif not values[field]:
            report.error(f"{display_path}: blank Ledger control field {field}")


def validate_public_email_addresses(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)
    for line_number, line in enumerate(document.lines, start=1):
        if EMAIL_PATTERN.search(line):
            report.warning(
                f"{display_path}:{line_number}: possible public e-mail address; "
                "confirm that publication is intentional"
            )


def readiness_section(lines: Sequence[str]) -> tuple[str, ...]:
    try:
        start = lines.index("## Readiness summary") + 1
    except ValueError:
        return ()

    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return tuple(lines[start:end])


def validate_readiness_summary(
    document: MarkdownDocument,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)
    section = readiness_section(document.lines)
    if not section:
        report.error(f"{display_path}: missing or empty Readiness summary section")
        return

    rows = [
        split_table_row(line)
        for line in section
        if line.lstrip().startswith("|")
    ]
    for route in READINESS_ROUTES:
        route_rows = [row for row in rows if row and row[0] == route]
        if not route_rows:
            report.error(f"{display_path}: missing {route} readiness row")
            continue
        if len(route_rows) > 1:
            report.error(f"{display_path}: duplicate {route} readiness row")
            continue

        route_row = route_rows[0]
        if len(route_row) != 7:
            report.error(
                f"{display_path}: {route} readiness row has "
                f"{len(route_row)} columns; expected 7"
            )
            continue
        for column_number, cell in enumerate(route_row, start=1):
            if not cell:
                report.error(
                    f"{display_path}: {route} readiness row has a blank "
                    f"column {column_number}"
                )


def validate_refresh_dates(
    document: MarkdownDocument,
    today: date,
    report: ValidationReport,
) -> None:
    display_path = report.display_path(document.path)

    for row in document.field_rows:
        schema = FIELD_ROW_SCHEMAS.get(len(row.cells))
        if schema is None:
            continue
        for date_text in DATE_PATTERN.findall(row.cells[schema.refresh]):
            refresh_date = optional_date(date_text)
            if refresh_date is None:
                report.error(
                    f"{display_path}:{row.line_number}: {row.field_id} has "
                    f"invalid literal refresh date {date_text}"
                )
            elif refresh_date < today:
                report.warning(
                    f"{display_path}: {row.field_id} has passed literal "
                    f"refresh date {date_text}"
                )


def validate_template(
    path: Path,
    report: ValidationReport,
) -> tuple[MarkdownDocument, set[str], date | None]:
    document = MarkdownDocument.read(path)
    validate_table_shapes(document, report)
    validate_local_links(document, report)
    template_ids = validate_field_ids(document, expected_ids=None, report=report)
    validate_template_fields(document, report)
    dates = require_frontmatter(
        document,
        keys=("title", "method_status", "official_guidance_cutoff", "last_reviewed"),
        date_keys=("official_guidance_cutoff", "last_reviewed"),
        report=report,
    )

    if not template_ids:
        report.error(f"{report.display_path(path)}: contains no field IDs")
    else:
        print(f"INFO: Template contains {len(template_ids)} stable field IDs.")

    return document, template_ids, dates.get("official_guidance_cutoff")


def validate_candidate_ledger(
    path: Path,
    *,
    template_ids: set[str],
    template_guidance_cutoff: date | None,
    today: date,
    report: ValidationReport,
) -> None:
    document = MarkdownDocument.read(path)
    print(f"INFO: Validating {report.display_path(path)}")

    validate_table_shapes(document, report)
    validate_local_links(document, report)
    validate_field_ids(document, expected_ids=template_ids, report=report)
    validate_candidate_fields(document, report)
    validate_ledger_control(document, report)
    validate_public_email_addresses(document, report)
    ledger_dates = require_frontmatter(
        document,
        keys=(
            "title",
            "last_reviewed",
            "evidence_cutoff",
            "official_guidance_cutoff",
        ),
        date_keys=("last_reviewed", "evidence_cutoff", "official_guidance_cutoff"),
        report=report,
    )
    validate_candidate_freshness(
        document,
        ledger_dates,
        template_guidance_cutoff,
        report,
    )
    validate_readiness_summary(document, report)
    validate_refresh_dates(document, today, report)


def parse_arguments(argv: Sequence[str] | None = None) -> argparse.Namespace:
    inferred_root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(
        description=(
            "Validate the proposal requirements template and all candidate ledgers."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=inferred_root,
        help="project root (default: inferred from this script)",
    )
    parser.add_argument(
        "--warnings-as-errors",
        action="store_true",
        help="return a failure status when freshness warnings are present",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    arguments = parse_arguments(argv)
    repo_root = arguments.repo_root.expanduser().resolve()
    report = ValidationReport(repo_root)
    template_path = repo_root / TEMPLATE_PATH

    if not template_path.is_file():
        print(f"ERROR: Missing template: {TEMPLATE_PATH}", file=sys.stderr)
        return 1

    _, template_ids, template_guidance_cutoff = validate_template(
        template_path,
        report,
    )

    ledger_paths = sorted(repo_root.glob(CANDIDATE_LEDGER_PATTERN))
    for ledger_path in ledger_paths:
        validate_candidate_ledger(
            ledger_path,
            template_ids=template_ids,
            template_guidance_cutoff=template_guidance_cutoff,
            today=date.today(),
            report=report,
        )

    if not ledger_paths:
        report.warning("No candidate proposal requirements ledgers were found")

    report.emit()
    failed = bool(
        report.errors or (arguments.warnings_as_errors and report.warnings)
    )
    status = "failed" if failed else "passed"
    print(
        f"Proposal ledger validation {status}: {len(ledger_paths)} ledger(s), "
        f"{len(report.errors)} error(s), {len(report.warnings)} warning(s).",
        file=sys.stderr if failed else sys.stdout,
    )

    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
