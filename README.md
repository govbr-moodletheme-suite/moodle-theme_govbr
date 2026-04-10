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

Documentation:

- `docs/testing/UNIT_TEST_SCENARIOS.md`
- `docs/usability/TEST_PLAN.md`

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
