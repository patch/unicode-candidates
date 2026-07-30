"""Tests for the proposal-ledger validator."""

from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


SCRIPT_DIRECTORY = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIRECTORY.parent
sys.path.insert(0, str(SCRIPT_DIRECTORY))

import validate_proposal_ledgers as validator  # noqa: E402


class ProposalLedgerValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, text: str) -> Path:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def report(self) -> validator.ValidationReport:
        return validator.ValidationReport(self.root)

    def document(self, relative_path: str, text: str) -> validator.MarkdownDocument:
        return validator.MarkdownDocument.read(self.write(relative_path, text))

    def test_split_table_row_preserves_code_span_pipe(self) -> None:
        cells = validator.split_table_row("| S-01 | `a | b` | value |")

        self.assertEqual(("S-01", "`a | b`", "value"), cells)

    def test_malformed_field_id_is_reported(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| X-01 | Requirement | Value | `unknown` | Support | | Later |\n",
        )
        report = self.report()

        validator.validate_field_ids(
            document,
            expected_ids=None,
            report=report,
        )

        self.assertTrue(
            any("malformed field ID 'X-01'" in error for error in report.errors)
        )

    def test_duplicate_and_missing_field_ids_are_reported(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | First | Value | `unknown` | Support | | Later |\n"
            "| S-01 | Second | Value | `unknown` | Support | | Later |\n",
        )
        report = self.report()

        validator.validate_field_ids(
            document,
            expected_ids={"S-01", "S-02"},
            report=report,
        )

        messages = "\n".join(report.errors)
        self.assertIn("duplicate field ID S-01", messages)
        self.assertIn("missing template field ID S-02", messages)

    def test_candidate_field_requires_support(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | Requirement | Value | `unknown` | | | Later |\n",
        )
        report = self.report()

        validator.validate_candidate_fields(document, report)

        self.assertTrue(
            any("blank support and destination" in error for error in report.errors)
        )

    def test_candidate_value_state_and_refresh_are_checked(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | Requirement | | `complete` | Support | | |\n",
        )
        report = self.report()

        validator.validate_candidate_fields(document, report)

        messages = "\n".join(report.errors)
        self.assertIn("unexplained blank current value", messages)
        self.assertIn("invalid state '`complete`'", messages)
        self.assertIn("blank refresh condition", messages)

    def test_template_field_defaults_are_checked(self) -> None:
        document = self.document(
            "template.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | Requirement | Filled | `supported` | | | Later |\n",
        )
        report = self.report()

        validator.validate_template_fields(document, report)

        messages = "\n".join(report.errors)
        self.assertIn("current value must be blank", messages)
        self.assertIn("template state must be `unknown`", messages)
        self.assertIn("blank support and destination", messages)

    def test_local_heading_fragment_is_checked(self) -> None:
        self.write("target.md", "## Existing heading\n")
        document = self.document(
            "source.md",
            "[Valid](target.md#existing-heading)\n"
            "[Invalid](target.md#missing-heading)\n",
        )
        report = self.report()

        validator.validate_local_links(document, report)

        self.assertEqual(1, len(report.errors))
        self.assertIn("missing-heading", report.errors[0])

    def test_ledger_control_requires_nonblank_stable_fields(self) -> None:
        document = self.document(
            "ledger.md",
            "| Field | Value |\n"
            "| --- | --- |\n"
            "| Candidate or repertoire | |\n",
        )
        report = self.report()

        validator.validate_ledger_control(document, report)

        messages = "\n".join(report.errors)
        self.assertIn("blank Ledger control field Candidate or repertoire", messages)
        self.assertIn("missing Ledger control field Scope", messages)

    def test_readiness_rows_require_all_columns(self) -> None:
        document = self.document(
            "ledger.md",
            "## Readiness summary\n\n"
            "| Route | Assessment | Support | Adverse | Blocks | Refresh | Decision |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| Character proposal | Not ready | Evidence | Gap | Work | "
            "Refresh | Defer |\n"
            "| Emoji proposal | Not ready | | Gap | Work | Refresh | Defer |\n",
        )
        report = self.report()

        validator.validate_readiness_summary(document, report)

        self.assertTrue(
            any("Emoji proposal readiness row has a blank" in error
                for error in report.errors)
        )

    def test_invalid_literal_refresh_date_is_an_error(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | Requirement | Value | `unknown` | Support | | 2026-02-30 |\n",
        )
        report = self.report()

        validator.validate_refresh_dates(document, date(2026, 1, 1), report)

        self.assertTrue(
            any("invalid literal refresh date 2026-02-30" in error
                for error in report.errors)
        )

    def test_passed_literal_refresh_date_is_a_warning(self) -> None:
        document = self.document(
            "ledger.md",
            "| ID | Requirement | Value | State | Support | Rights | Refresh |\n"
            "| --- | --- | --- | --- | --- | --- | --- |\n"
            "| S-01 | Requirement | Value | `unknown` | Support | | 2026-01-01 |\n",
        )
        report = self.report()

        validator.validate_refresh_dates(document, date(2026, 1, 2), report)

        self.assertTrue(
            any("passed literal refresh date 2026-01-01" in warning
                for warning in report.warnings)
        )

    def test_possible_public_email_address_is_a_warning(self) -> None:
        document = self.document(
            "ledger.md",
            "Submitter: person@example.org\n",
        )
        report = self.report()

        validator.validate_public_email_addresses(document, report)

        self.assertEqual(1, len(report.warnings))

    def test_last_reviewed_alone_does_not_make_ledger_stale(self) -> None:
        ledger_path = self.write(
            "Candidates/Test/Research/Proposal requirements ledger.md",
            "---\nlast_reviewed: 2026-01-01\n---\n",
        )
        self.write(
            "Candidates/Test/Research/Research note.md",
            "---\nlast_reviewed: 2099-01-01\n---\n",
        )
        report = self.report()

        validator.validate_candidate_freshness(
            validator.MarkdownDocument.read(ledger_path),
            {
                "last_reviewed": date(2026, 1, 1),
                "evidence_cutoff": date(2026, 1, 1),
                "official_guidance_cutoff": date(2026, 1, 1),
            },
            template_guidance_cutoff=date(2026, 1, 1),
            report=report,
        )

        self.assertEqual([], report.warnings)

    def test_newer_evidence_cutoff_makes_ledger_stale(self) -> None:
        ledger_path = self.write(
            "Candidates/Test/Research/Proposal requirements ledger.md",
            "---\nevidence_cutoff: 2026-01-01\n---\n",
        )
        self.write(
            "Candidates/Test/Research/Research note.md",
            "---\nevidence_cutoff: 2026-01-02\n---\n",
        )
        report = self.report()

        validator.validate_candidate_freshness(
            validator.MarkdownDocument.read(ledger_path),
            {
                "last_reviewed": date(2026, 1, 1),
                "evidence_cutoff": date(2026, 1, 1),
                "official_guidance_cutoff": date(2026, 1, 1),
            },
            template_guidance_cutoff=date(2026, 1, 1),
            report=report,
        )

        self.assertTrue(
            any("evidence cut-off 2026-01-02" in warning
                for warning in report.warnings)
        )

    def test_current_project_passes_strict_validation(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()

        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = validator.main(
                ["--repo-root", str(PROJECT_ROOT), "--warnings-as-errors"]
            )

        self.assertEqual(0, result, stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
