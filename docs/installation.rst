Installation
============

Requirements
------------

* Python 3.10+
* Django >= 5.2, < 6.1
* behave-django >= 1.7, < 2.0

Run the usability lab locally
-------------------------------

.. code-block:: bash

   cd usability_lab
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver

Open ``http://127.0.0.1:8000/`` — the home page lists the available scenarios (login,
dashboard, course, settings).

Development tooling
--------------------

To install linting, SAST and coverage-gate tooling (used by pre-commit and CI):

.. code-block:: bash

   cd usability_lab
   pip install -r requirements-dev.txt

See :doc:`development` for how these tools are wired into pre-commit and CI.
