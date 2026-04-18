# Gov.BR Theme Usability Lab (Django)

This local app provides independent UX test scenarios for the Gov.BR Moodle theme.

## Requirements

- Python 3.10+
- Django >= 5.2 and < 6.1
- behave-django >= 1.7 and < 2.0

## Why this exists

- Run usability sessions without depending on a Moodle instance.
- Validate visual hierarchy, discoverability, and accessibility patterns quickly.
- Record lightweight evidence during moderated sessions.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Included scenarios

1. Login and first impression.
2. Dashboard orientation.
3. Course page comprehension.
4. Theme settings discoverability.

## Notes capture

The fixed panel stores notes in browser local storage and can export JSON evidence for each session.

It also supports participant metrics and a single participant report export containing:

- participant ID and role
- per-scenario completion and time
- critical errors and confidence score
- free-form session notes

## Run unit tests

```bash
python manage.py test
```

## Run BDD scenarios

```bash
python manage.py behave
```

## Pre-commit and coverage gate

Install development tooling:

```bash
pip install -r requirements-dev.txt
pre-commit install
pre-commit install --hook-type pre-push
```

Coverage rules enforced in pre-push and CI:

- Minimum coverage: 80%.
- Ideal target: 95%.
- Coverage must be greater than or equal to `./.coverage-baseline` when this file is present.

## CI/CD parity

The CI workflow runs the same pre-commit checks and uploads coverage reports to Codecov.

## Packaging policy

This app is development-only and is excluded from release archives through `.gitattributes` (`export-ignore`).
