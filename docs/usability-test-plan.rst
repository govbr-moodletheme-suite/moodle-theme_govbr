Usability Test Plan
=====================

This plan is executed with the standalone Django app in ``usability_lab/``.

Objective
---------

Validate if the Gov.BR visual language and interaction patterns are understandable and
efficient without depending on a full Moodle instance.

Recommended participants
-------------------------

* 5 to 8 users per iteration.
* Mixed profile: administrators, teachers, students.

Core scenarios
--------------

1. Login and first impression

   * Open the login page.
   * Identify institutional header, login form, and help text.
   * Report confidence level before signing in.

2. Dashboard orientation

   * Locate main navigation and active section.
   * Identify where announcements and shortcuts are.
   * Explain where they would click to access courses.

3. Course page comprehension

   * Find the course title and key actions.
   * Locate a module card and open details.
   * Confirm if visual hierarchy is clear.

4. Theme settings discoverability

   * Open the settings simulation page.
   * Change brand colour and logo path.
   * Confirm if feedback and save action are obvious.

5. Accessibility-focused pass

   * Navigate using keyboard only.
   * Evaluate focus visibility and skip-link discoverability.
   * Confirm contrast and text legibility.

Metrics
-------

* Task success rate (%).
* Time on task (seconds).
* Number of critical errors.
* Post-task confidence score (1-5).
* SUS-like subjective score (optional).

Evidence capture
-----------------

* Session recording (screen + voice).
* Export notes from the lab notes panel.
* Annotate pain points by scenario ID.
