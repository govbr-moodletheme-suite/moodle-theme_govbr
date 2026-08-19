Overview
========

What this repository is today
------------------------------

``moodle-theme_govbr`` will eventually ship a Moodle theme (a Boost child theme) applying the
visual identity, colors, typography and accessibility requirements of the Brazilian Federal
Government Design System (DSGovBR) to Moodle. Building and validating that identity correctly
*before* wiring it into Moodle is the actual purpose of the code that lives here right now:
the ``usability_lab/`` application.

``usability_lab`` is a small, standalone Django app that renders a handful of static scenario
pages (login, dashboard, course, settings) styled with the Gov.BR visual language, so that
usability sessions and interaction reviews can happen **without depending on a running Moodle
instance**. It is explicitly a development/validation tool, not a production artifact — see
:doc:`development` for how it is excluded from release packaging.

Why a usability lab instead of theme code first
-------------------------------------------------

A previous iteration of this repository *did* contain real Moodle theme code (``config.php``,
``lib.php``, SCSS, language strings, Boost layout overrides, a privacy provider). That code
was removed from the repository history while adding this usability-testing harness, and has
not been reconstructed yet. Rebuilding the actual Moodle theme, and republishing this
documentation with it, is planned as a separate, dedicated effort.

Repository layout
------------------

.. code-block:: text

   moodle-theme_govbr/
   ├── docs/                     # This documentation (Sphinx)
   ├── scripts/
   │   ├── build-release-zip.sh  # Packages a release ZIP via `git archive`
   │   └── check_coverage_gate.py
   ├── usability_lab/            # Standalone Django usability-testing app
   │   ├── lab/                  # Scenario views, templates, static assets
   │   ├── features/             # behave-django BDD scenarios
   │   └── usability_lab_project/
   ├── .github/workflows/
   │   ├── django-ci.yml         # Lint, SAST, tests, coverage (usability_lab)
   │   └── release-zip.yml       # Builds and attaches the release ZIP artifact
   ├── .pre-commit-config.yaml
   ├── LICENSE.md                # GPLv3
   └── SECURITY.md

Organization context
---------------------

This repository is one of three in the ``govbr-moodletheme-suite`` organization:

* `workspace <https://github.com/govbr-moodletheme-suite/workspace>`_ — local development
  orchestration (private).
* `govbr-moodletheme-suite.github.io <https://github.com/govbr-moodletheme-suite/govbr-moodletheme-suite.github.io>`_
  — the organization's portal site.
* ``moodle-theme_govbr`` (this repository).
