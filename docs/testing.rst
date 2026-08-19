Unit Test Scenarios
====================

This page lists the minimum unit scenarios for the standalone usability lab.

Scope
-----

* Application: ``usability_lab/lab``
* Test runner: Django built-in test framework
* Current implementation file: ``usability_lab/lab/tests.py``

Scenario matrix
----------------

1. Home route

   * ``GET /`` returns HTTP 200.
   * Response includes the scenario catalogue title.

2. Login scenario route

   * ``GET /scenario/login/`` returns HTTP 200.
   * Response contains the login scenario heading.

3. Dashboard scenario route

   * ``GET /scenario/dashboard/`` returns HTTP 200.
   * Response contains dashboard orientation heading.

4. Course scenario route

   * ``GET /scenario/course/`` returns HTTP 200.
   * Response contains the course comprehension heading.

5. Settings scenario route

   * ``GET /scenario/settings/`` returns HTTP 200.
   * Response contains the settings discoverability heading.

Suggested additions
--------------------

1. Notes and metrics rendering

   * Confirm notes panel controls and metrics fields are present.

2. Accessibility smoke checks

   * Confirm skip-link exists in all scenario pages.

Run command
-----------

.. code-block:: bash

   cd usability_lab
   python manage.py test
