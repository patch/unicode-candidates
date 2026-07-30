# Project scripts

These scripts provide lightweight, portable validation for project records. They do not replace source review or research judgement.

- [`validate_proposal_ledgers.py`](validate_proposal_ledgers.py) checks the project template and every candidate proposal requirements ledger for structural drift, stale cut-off indicators, broken local links and fragments, missing support, incomplete readiness summaries and possible public e-mail addresses.

Run it from the project root with Python 3.10 or later:

```sh
python3 scripts/validate_proposal_ledgers.py
```

Treat warnings as failures for a pre-commit check:

```sh
python3 scripts/validate_proposal_ledgers.py --warnings-as-errors
```

The validator uses only the Python standard library. Its tests use `unittest`:

```sh
python3 -m unittest scripts/test_validate_proposal_ledgers.py
```

## Scripting conventions

In regular expressions, prefer a character class to alternation for single-character choices. In verbose mode, use insignificant horizontal whitespace to expose token boundaries, as in `< (?P<name> [^>]+ ) >`, and format dense nested groups or alternatives vertically; add line breaks for structure, not for every token.
