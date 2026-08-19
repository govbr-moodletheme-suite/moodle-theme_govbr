Development
============

Running tests
--------------

.. code-block:: bash

   cd usability_lab
   python manage.py test       # Unit tests (Django test runner)
   python manage.py behave     # BDD scenarios (behave-django)

See :doc:`testing` for the scenario matrix and :doc:`usability-test-plan` for the moderated
usability-testing protocol these automated scenarios support.

Pre-commit
----------

Install the local quality gates:

.. code-block:: bash

   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r usability_lab/requirements-dev.txt
   pre-commit install
   pre-commit install --hook-type pre-push

What runs on every commit:

* **Lint**: Python (ruff), CSS (stylelint), JavaScript (eslint), Markdown (markdownlint-cli2),
  Django HTML templates (djlint).
* **SAST**: bandit and semgrep.

What runs on every push (``pre-push`` stage):

* Django unit tests + behave-django BDD scenarios.
* Coverage report, gated at a minimum of 80%.
* If ``usability_lab/.coverage-baseline`` exists, current coverage must not regress below it
  (enforced by ``scripts/check_coverage_gate.py``).

Coverage policy
----------------

* Minimum required coverage: 80% (hard fail below this).
* Ideal target: 95%.
* Coverage must not be lower than the value stored in ``usability_lab/.coverage-baseline``.

CI/CD
-----

``.github/workflows/django-ci.yml`` (**Django Quality and Coverage**) runs on every push and
pull request against ``main``: it installs dependencies, runs the same pre-commit hooks
(including the ``pre-push`` stage), and uploads the coverage report to Codecov.

``.github/workflows/release-zip.yml`` (**Build Release ZIP**) runs on ``workflow_dispatch`` and
on published GitHub Releases: it packages a distributable ZIP and attaches it as a release
artifact.

Packaging
---------

To build a release archive locally from git metadata:

.. code-block:: bash

   ./scripts/build-release-zip.sh

The script uses ``git archive`` together with ``.gitattributes`` ``export-ignore`` rules. Today
the release archive **includes** the ``usability_lab/`` runtime code and excludes only:

* CI and editor metadata (``.github/``, ``.vscode/``)
* local documentation (``docs/``)
* packaging helpers (``scripts/``)
* ``usability_lab``'s test suites (``usability_lab/features/``, ``usability_lab/lab/tests.py``)

.. note::
   An earlier commit message on this repository stated the intent that the whole
   ``usability_lab/`` app should be excluded from the release package. The behavior actually
   implemented in ``.gitattributes`` (and documented in the root ``README.md``) only excludes
   its test suites, not the app itself — this documentation describes what is implemented
   today, not that earlier stated intent.
