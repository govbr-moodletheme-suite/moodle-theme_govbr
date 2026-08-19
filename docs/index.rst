moodle-theme_govbr
===================

.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
   :target: https://github.com/govbr-moodletheme-suite/moodle-theme_govbr/blob/main/LICENSE.md
   :alt: License

.. image:: https://github.com/govbr-moodletheme-suite/moodle-theme_govbr/actions/workflows/django-ci.yml/badge.svg
   :target: https://github.com/govbr-moodletheme-suite/moodle-theme_govbr/actions/workflows/django-ci.yml
   :alt: Django Quality and Coverage

``moodle-theme_govbr`` is the repository intended for a Moodle theme aligned with the
Brazilian Federal Government Design System (`DSGovBR <https://www.gov.br/ds/>`_), part of the
`govbr-moodletheme-suite <https://github.com/govbr-moodletheme-suite>`_ organization.

.. important::
   The Moodle theme code (``version.php``, ``config.php``, ``lib.php``, SCSS, language
   strings, Boost layout overrides) is **not implemented yet** in this repository — it is
   planned but out of scope for the current development phase. What exists today, and what
   this documentation actually describes, is the **usability testing lab**: a standalone
   Django application used to validate the Gov.BR visual language and interaction patterns
   *before* a real Moodle theme is built on top of them.

Contents
--------

.. toctree::
   :maxdepth: 2

   overview
   installation
   testing
   usability-test-plan
   development
