from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("scenario/login/", views.login_scenario, name="scenario-login"),
    path("scenario/dashboard/", views.dashboard_scenario, name="scenario-dashboard"),
    path("scenario/course/", views.course_scenario, name="scenario-course"),
    path("scenario/settings/", views.settings_scenario, name="scenario-settings"),
]
