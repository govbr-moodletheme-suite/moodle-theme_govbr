from django.test import TestCase


class LabRoutesTests(TestCase):
    def test_home_route(self) -> None:
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Gov.BR Theme Usability Lab")

    def test_login_route(self) -> None:
        response = self.client.get("/scenario/login/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scenario 1: Login and First Impression")

    def test_dashboard_route(self) -> None:
        response = self.client.get("/scenario/dashboard/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scenario 2: Dashboard Orientation")

    def test_course_route(self) -> None:
        response = self.client.get("/scenario/course/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scenario 3: Course Page Comprehension")

    def test_settings_route(self) -> None:
        response = self.client.get("/scenario/settings/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scenario 4: Theme Settings Discoverability")
