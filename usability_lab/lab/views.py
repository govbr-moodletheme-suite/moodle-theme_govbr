from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    scenarios = [
        {
            "slug": "login",
            "title": "Login and First Impression",
            "goal": "Check if users can identify institutional elements and sign-in action quickly.",
        },
        {
            "slug": "dashboard",
            "title": "Dashboard Orientation",
            "goal": "Validate if users understand navigation and key content blocks.",
        },
        {
            "slug": "course",
            "title": "Course Page Comprehension",
            "goal": "Assess hierarchy and clarity of course actions and modules.",
        },
        {
            "slug": "settings",
            "title": "Theme Settings Discoverability",
            "goal": "Evaluate if users can find and change configuration controls.",
        },
    ]
    return render(request, "lab/home.html", {"scenarios": scenarios})


def login_scenario(request: HttpRequest) -> HttpResponse:
    return render(request, "lab/scenario_login.html")


def dashboard_scenario(request: HttpRequest) -> HttpResponse:
    return render(request, "lab/scenario_dashboard.html")


def course_scenario(request: HttpRequest) -> HttpResponse:
    return render(request, "lab/scenario_course.html")


def settings_scenario(request: HttpRequest) -> HttpResponse:
    return render(request, "lab/scenario_settings.html")
