# GovBR Usability Lab

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.md)

This project provides a standalone usability testing lab implemented only with Python and Django.

## Requirements

- Python 3.10+
- Django >= 5.2 and < 6.1
- behave-django >= 1.7 and < 2.0

## Test Strategy

1. Unit tests with Django test runner (`python manage.py test`).
2. BDD scenarios with behave-django (`python manage.py behave`).

Documentation: published at https://govbr-moodletheme-suite.github.io/moodle-theme_govbr/
(built automatically on every push to `docs/` via `.github/workflows/docs.yml`, using the
[moodle-docs-theme](https://pypi.org/project/moodle-docs-theme/) Sphinx theme). To build
locally:

```bash
pip install sphinx moodle-docs-theme
sphinx-build -W -b html docs docs/_build/html
```

Pages: `docs/overview.rst`, `docs/installation.rst`, `docs/testing.rst`,
`docs/usability-test-plan.rst`, `docs/development.rst`.

## Run Locally

```bash
cd usability_lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Run Tests

```bash
cd usability_lab
python manage.py test
python manage.py behave
```

## Pre-commit

Enable local quality gates:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r usability_lab/requirements-dev.txt
pre-commit install
pre-commit install --hook-type pre-push
```

What runs locally:

- Lint: Python, CSS, JavaScript, Markdown, and HTML.
- SAST: bandit and semgrep.
- Pre-push gate: unit tests, behave-django scenarios, and coverage validation.

Coverage policy:

- Minimum required coverage: 80% (hard fail below this).
- Ideal target: 95%.
- If `usability_lab/.coverage-baseline` exists, current coverage cannot be lower than that baseline.

## Packaging

To create a release archive from git metadata:

```bash
./scripts/build-release-zip.sh
```

The script uses `git archive` with repository attributes.

Release archives include runtime Django code (for `usability_lab`) and exclude only development files:

- CI and editor metadata (`.github/`, `.vscode/`)
- local documentation (`docs/`)
- test suites (`usability_lab/features/`, `usability_lab/lab/tests.py`)
- packaging helpers (`scripts/`)
