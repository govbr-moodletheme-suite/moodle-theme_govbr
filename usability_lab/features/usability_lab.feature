Feature: Usability lab routes
  In order to validate the standalone Gov.BR usability lab
  As a test runner
  I want key pages to render and expose expected headings

  Scenario Outline: Main routes are available
    When I request the page "<path>"
    Then the response status should be 200
    And the page should contain "<title>"

    Examples:
      | path                 | title                                       |
      | /                    | Gov.BR Theme Usability Lab                  |
      | /scenario/login/     | Scenario 1: Login and First Impression      |
      | /scenario/dashboard/ | Scenario 2: Dashboard Orientation           |
      | /scenario/course/    | Scenario 3: Course Page Comprehension       |
      | /scenario/settings/  | Scenario 4: Theme Settings Discoverability  |
